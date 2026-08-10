"""Validaciones pequeñas y deterministas del contrato del guion de carta."""

from __future__ import annotations


def clasificar_destinatario(
    empresa: str,
    plataforma: str,
    intermediario: str = "",
    empresa_anonima: bool = False,
) -> dict[str, object]:
    """Separa plataforma, intermediario y empleador sin inferir identidades."""
    if empresa_anonima or not empresa.strip():
        return {
            "empresa_objetivo": "",
            "plataforma_publicadora": plataforma,
            "intermediario": intermediario,
            "destinatario_real": "empresa no identificada",
            "tipo": "intermediario_con_empresa_anonima",
            "empresa_anonima": True,
            "solicitar_url": False,
        }
    tipo = "intermediario_con_empresa_identificada" if intermediario.strip() else "empresa_identificada"
    return {
        "empresa_objetivo": empresa,
        "plataforma_publicadora": plataforma,
        "intermediario": intermediario,
        "destinatario_real": empresa,
        "tipo": tipo,
        "empresa_anonima": False,
        "solicitar_url": False,
    }


def resolver_fuente_externa(
    empresa_identificada: bool,
    url_registrada: str,
    empresa_anonima: bool,
) -> dict[str, object]:
    """Aplica la regla de URL opcional sin convertirla en bloqueo."""
    if empresa_anonima or not empresa_identificada:
        return {"estado": "no_aplica", "solicitar_url": False, "bloquea": False}
    if url_registrada.strip():
        return {"estado": "usar_url_registrada", "solicitar_url": False, "bloquea": False}
    return {"estado": "url_opcional_pendiente", "solicitar_url": True, "bloquea": False}


def clasificar_motivacion(texto: str) -> str:
    return "declarada" if texto.strip() else "no_registrada"


def puede_atribuir_afinidad(senal_cultural: str, conexion_factual: bool) -> bool:
    del senal_cultural
    return bool(conexion_factual)


def clasificar_keyword(termino: str, tiene_evidencia: bool) -> str:
    del termino
    return "utilizable" if tiene_evidencia else "prohibido_como_atributo"


def evaluar_estado_guion(
    *,
    segundo_cv: bool,
    generico: bool,
    motivacion_faltante: bool,
    bloqueo: bool = False,
    actualizacion_factual: bool = False,
    revision_origen: bool = False,
) -> str:
    """Devuelve el estado con la precedencia normativa del playbook."""
    if bloqueo:
        return "bloqueado"
    if actualizacion_factual:
        return "requiere_actualizacion_factual"
    if revision_origen:
        return "requiere_revision_origen"
    if motivacion_faltante:
        return "requiere_interaccion_usuario"
    if segundo_cv or generico:
        return "requiere_correccion"
    return "apto"


__all__ = [
    "clasificar_destinatario",
    "resolver_fuente_externa",
    "clasificar_motivacion",
    "puede_atribuir_afinidad",
    "clasificar_keyword",
    "evaluar_estado_guion",
]
