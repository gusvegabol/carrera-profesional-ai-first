"""Controles deterministas del veredicto final de una carta.

El módulo no redacta ni modifica artefactos. Valida precondiciones, normaliza
hallazgos de los tres roles y aplica la síntesis contractual sin votación.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Iterable


RESULTADOS = ("APTA", "APTA_CON_RESERVAS", "NO_APTA")
CATEGORIAS = ("bloqueante", "reserva_relevante", "reserva_menor", "observacion")
VALORES_INCREMENTALES = ("alto", "medio", "bajo")
RECOMENDACIONES = ("incluir", "incluir_con_reservas", "no_incluir")
ESTADOS_GATE = ("pendiente", "aprobado", "bloqueado")

_ROLES = ("recruiter", "editorial", "auditor")


def _campo_frontmatter(texto: str, campo: str) -> str:
    patron = rf"^{re.escape(campo)}:\s*(.*?)\s*$"
    coincidencia = re.search(patron, texto, re.MULTILINE)
    return coincidencia.group(1).strip().strip("`").strip('"') if coincidencia else ""


def validar_precondiciones(candidatura_dir: Path) -> list[str]:
    """Devuelve bloqueos de entrada sin modificar el expediente."""
    requeridos = (
        "carta-presentacion.pdf",
        "carta-presentacion.docx",
        "contenido-carta-presentacion.md",
        "guion-carta-presentacion.md",
        "candidatura.md",
        "analisis-oferta.md",
        "cv.pdf",
        "evaluacion-composicion-carta-presentacion.md",
    )
    bloqueos = [nombre for nombre in requeridos if not (candidatura_dir / nombre).is_file()]

    candidatura = candidatura_dir / "candidatura.md"
    if candidatura.is_file():
        texto = candidatura.read_text(encoding="utf-8")
        if _campo_frontmatter(texto, "gate_carta_revision_humana").lower() != "aprobado":
            bloqueos.append("gate_carta_revision_humana_no_aprobado")
        if _campo_frontmatter(texto, "gate_candidatura_presentacion").lower() not in {"no_abierto", "pendiente", "no_aplica_en_esta_fase"}:
            bloqueos.append("gate_candidatura_presentacion_debe_seguir_fuera_de_alcance_o_no_abierto")
        if _campo_frontmatter(texto, "presentada").lower() != "false":
            bloqueos.append("presentada_debe_seguir_false")

    evaluacion = candidatura_dir / "evaluacion-composicion-carta-presentacion.md"
    if evaluacion.is_file():
        texto = evaluacion.read_text(encoding="utf-8")
        if _campo_frontmatter(texto, "estado_gate").lower() != "aprobado":
            bloqueos.append("revision_humana_carta_no_aprobada")

    return bloqueos


def validar_roles(roles: dict[str, dict[str, Any]]) -> None:
    """Comprueba que existen las tres evaluaciones independientes."""
    faltantes = [rol for rol in _ROLES if rol not in roles]
    if faltantes:
        raise ValueError(f"roles_faltantes: {', '.join(faltantes)}")
    for rol in _ROLES:
        evaluacion = roles[rol]
        if evaluacion.get("aplicado") is not True:
            raise ValueError(f"rol_no_aplicado: {rol}")
        if evaluacion.get("fuentes_compartidas_con_otro_rol") is True:
            raise ValueError(f"independencia_no_respetada: {rol}")


def _normalizar_hallazgo(hallazgo: dict[str, Any]) -> dict[str, Any]:
    categoria = str(hallazgo.get("categoria", "")).strip()
    if categoria not in CATEGORIAS:
        raise ValueError(f"categoria_hallazgo_invalida: {categoria}")
    descripcion = str(hallazgo.get("descripcion", "")).strip()
    if not descripcion:
        raise ValueError("hallazgo_sin_descripcion")
    return {
        "id": str(hallazgo.get("id", "")).strip() or None,
        "rol": str(hallazgo.get("rol", "")).strip() or None,
        "categoria": categoria,
        "descripcion": descripcion,
        "fase_responsable": str(hallazgo.get("fase_responsable", "")).strip() or None,
    }


def sintetizar_hallazgos(
    roles: dict[str, dict[str, Any]],
    *,
    valor_incremental: str,
) -> dict[str, Any]:
    """Aplica la síntesis determinista, sin añadir hallazgos editoriales."""
    validar_roles(roles)
    if valor_incremental not in VALORES_INCREMENTALES:
        raise ValueError(f"valor_incremental_invalido: {valor_incremental}")

    hallazgos: list[dict[str, Any]] = []
    for rol in _ROLES:
        for raw in roles[rol].get("hallazgos", []):
            normalizado = _normalizar_hallazgo({**raw, "rol": raw.get("rol", rol)})
            hallazgos.append(normalizado)

    # Duplicados exactos se eliminan preservando el orden de origen.
    unicos: list[dict[str, Any]] = []
    vistos: set[tuple[str, str, str]] = set()
    for hallazgo in hallazgos:
        clave = (hallazgo["categoria"], hallazgo["descripcion"], hallazgo["fase_responsable"] or "")
        if clave not in vistos:
            vistos.add(clave)
            unicos.append(hallazgo)

    if valor_incremental == "bajo" and not any(h["categoria"] == "bloqueante" for h in unicos):
        if not any(h["categoria"] == "reserva_relevante" and "incremental" in h["descripcion"].lower() for h in unicos):
            unicos.append({
                "id": "SYN-VALOR-001",
                "rol": "sintesis",
                "categoria": "reserva_relevante",
                "descripcion": "El valor incremental frente al CV es bajo.",
                "fase_responsable": "veredicto_final_carta",
            })

    agrupados = {categoria: [h for h in unicos if h["categoria"] == categoria] for categoria in CATEGORIAS}
    if agrupados["bloqueante"]:
        resultado = "NO_APTA"
    elif agrupados["reserva_relevante"]:
        resultado = "APTA_CON_RESERVAS"
    else:
        resultado = "APTA"
    return {"resultado": resultado, "hallazgos": agrupados, "hallazgos_planos": unicos}


def recomendar_inclusion(resultado: str, valor_incremental: str, *, motivo_canal: str | None = None) -> str:
    """Separa recomendación de inclusión del resultado de calidad."""
    if resultado not in RESULTADOS:
        raise ValueError(f"resultado_invalido: {resultado}")
    if valor_incremental not in VALORES_INCREMENTALES:
        raise ValueError(f"valor_incremental_invalido: {valor_incremental}")
    if resultado == "NO_APTA":
        return "no_incluir"
    if resultado == "APTA_CON_RESERVAS":
        return "no_incluir" if motivo_canal else "incluir_con_reservas"
    return "incluir"


def estado_gate_salida(resultado: str) -> str:
    """El veredicto nunca aprueba el gate humano."""
    if resultado not in RESULTADOS:
        raise ValueError(f"resultado_invalido: {resultado}")
    return "pendiente" if resultado in {"APTA", "APTA_CON_RESERVAS"} else "bloqueado"


def registrar_informacion_nueva(descripcion: str, fase_responsable: str) -> dict[str, str]:
    """Devuelve una incidencia, sin incorporar la información al veredicto."""
    if not descripcion.strip() or not fase_responsable.strip():
        raise ValueError("incidencia_fuera_de_fase_incompleta")
    return {
        "tipo": "incidencia_fuera_de_fase",
        "descripcion": descripcion.strip(),
        "fase_responsable": fase_responsable.strip(),
        "incorporada": "no",
    }


def validar_sintesis(resultado: str, hallazgos: dict[str, Iterable[Any]], valor_incremental: str) -> None:
    """Valida la coherencia entre hallazgos, resultado y regla incremental."""
    if resultado not in RESULTADOS:
        raise ValueError(f"resultado_invalido: {resultado}")
    if valor_incremental not in VALORES_INCREMENTALES:
        raise ValueError(f"valor_incremental_invalido: {valor_incremental}")
    bloqueantes = list(hallazgos.get("bloqueante", []))
    relevantes = list(hallazgos.get("reserva_relevante", []))
    if bloqueantes and resultado != "NO_APTA":
        raise ValueError("bloqueante_debe_producir_no_apta")
    if not bloqueantes and relevantes and resultado != "APTA_CON_RESERVAS":
        raise ValueError("reserva_relevante_debe_producir_apta_con_reservas")
    if not bloqueantes and not relevantes and resultado != "APTA":
        raise ValueError("sin_bloqueantes_ni_reservas_debe_producir_apta")
    if valor_incremental == "bajo" and not bloqueantes and not relevantes:
        raise ValueError("valor_incremental_bajo_requiere_reserva_relevante")


__all__ = [
    "CATEGORIAS",
    "ESTADOS_GATE",
    "RECOMENDACIONES",
    "RESULTADOS",
    "VALORES_INCREMENTALES",
    "estado_gate_salida",
    "registrar_informacion_nueva",
    "recomendar_inclusion",
    "sintetizar_hallazgos",
    "validar_precondiciones",
    "validar_roles",
    "validar_sintesis",
]
