"""Validación técnica de la frontera entre candidatura completa y envío real."""

from __future__ import annotations

import re
from pathlib import Path


_EVIDENCIA_REQUERIDA = ("canal", "fecha_hora", "ejecutado_por", "confirmacion")


def _campo_frontmatter(texto: str, campo: str) -> str:
    patron = rf"^{re.escape(campo)}:\s*(.*?)\s*$"
    coincidencia = re.search(patron, texto, re.MULTILINE)
    return coincidencia.group(1).strip().strip("`") if coincidencia else ""


def validar_paquete(paquete_path: Path, candidatura_dir: Path) -> list[str]:
    """Devuelve bloqueos sin modificar el paquete ni el estado de candidatura."""
    bloqueos: list[str] = []
    if not paquete_path.is_file():
        return ["paquete_presentacion_faltante"]

    texto = paquete_path.read_text(encoding="utf-8")
    if _campo_frontmatter(texto, "presentada").lower() != "false":
        bloqueos.append("presentada_debe_ser_false")

    candidatura = candidatura_dir / "candidatura.md"
    if candidatura.is_file() and _campo_frontmatter(candidatura.read_text(encoding="utf-8"), "presentada").lower() != "false":
        bloqueos.append("candidatura_presentada_no_es_false")

    canal = re.search(r"\|\s*Canal de envío confirmado\s*\|\s*([^|]+?)\s*\|", texto, re.IGNORECASE)
    if canal is None or canal.group(1).strip().lower() in {"", "pendiente de comprobar", "pendiente"}:
        bloqueos.append("canal_envio_no_confirmado")

    filas_pendientes = []
    for linea in texto.splitlines():
        if any(nombre in linea.lower() for nombre in ("| carta |", "email de presentación", "respuestas de formulario")):
            if any(marca in linea.lower() for marca in ("pendiente", "no creada", "no resueltas", "no resuelto")):
                filas_pendientes.append(linea)
    if filas_pendientes:
        bloqueos.append("artefactos_presentacion_pendientes")

    if "GATE-VEREDICTO-CV` aprobado" not in texto and "GATE-VEREDICTO-CV: aprobado" not in texto:
        bloqueos.append("gate_cv_no_aprobado")

    return bloqueos


def validar_transicion_presentada(paquete_path: Path, evidencia: dict[str, str]) -> None:
    """Valida la evidencia mínima antes de registrar un envío real."""
    if not paquete_path.is_file():
        raise ValueError("paquete_presentacion_faltante")
    texto = paquete_path.read_text(encoding="utf-8")
    if "presentada: false" not in texto:
        raise ValueError("paquete_no_esta_en_estado_no_presentado")
    faltantes = [campo for campo in _EVIDENCIA_REQUERIDA if not str(evidencia.get(campo, "")).strip()]
    if faltantes:
        raise ValueError(f"evidencia_envio_incompleta: {', '.join(faltantes)}")


__all__ = ["validar_paquete", "validar_transicion_presentada"]
