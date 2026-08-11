"""Selección determinista de transiciones del flujo documental de Job-up.

Este módulo no ejecuta playbooks ni modifica expedientes. Representa la
decisión que debe tomar la orquestación después de cada gate para evitar que
una acción determinista se convierta en una pausa conversacional redundante.
"""

from __future__ import annotations

from typing import Mapping, Any


PLAYBOOK_COMPONER_CARTA_PRESENTACION = "PLAYBOOK_COMPONER_CARTA_PRESENTACION"
PLAYBOOK_VEREDICTO_FINAL_CARTA = "PLAYBOOK_VEREDICTO_FINAL_CARTA"
ESPERAR_DECISION_HUMANA = "ESPERAR_DECISION_HUMANA"
CIERRE_DOCUMENTAL = "CIERRE_DOCUMENTAL"
BLOQUEO_TECNICO = "BLOQUEO_TECNICO"


def _estado_gate(estado: Mapping[str, Any], campo: str) -> str:
    return str(estado.get(campo, "")).strip().lower()


def siguiente_accion_carta(estado: Mapping[str, Any]) -> str:
    """Devuelve la siguiente acción de la rama carta sin crear pausas falsas.

    La secuencia se evalúa en orden de seguridad: un bloqueo técnico o una
    candidatura ya presentada detienen; después se comprueban las fases de
    composición y veredicto; por último se permite el cierre documental.
    """

    if estado.get("bloqueo_tecnico") is True:
        return BLOQUEO_TECNICO
    if estado.get("presentada") is True:
        return BLOQUEO_TECNICO
    if estado.get("datos_pendientes"):
        return ESPERAR_DECISION_HUMANA

    contenido_gate = _estado_gate(estado, "gate_contenido_carta_composicion")
    revision_gate = _estado_gate(estado, "gate_carta_revision_humana")
    veredicto_gate = _estado_gate(estado, "gate_veredicto_carta")
    carta_compuesta = estado.get("carta_compuesta") is True
    cv_aprobado = estado.get("cv_aprobado") is True

    if contenido_gate == "bloqueado":
        return BLOQUEO_TECNICO
    if contenido_gate != "aprobado":
        return ESPERAR_DECISION_HUMANA
    if not carta_compuesta:
        return PLAYBOOK_COMPONER_CARTA_PRESENTACION
    if revision_gate == "bloqueado":
        return BLOQUEO_TECNICO
    if revision_gate != "aprobado":
        return ESPERAR_DECISION_HUMANA
    if veredicto_gate == "bloqueado":
        return BLOQUEO_TECNICO
    if veredicto_gate in {"", "pendiente"}:
        return PLAYBOOK_VEREDICTO_FINAL_CARTA
    if veredicto_gate != "aprobado":
        return BLOQUEO_TECNICO
    if cv_aprobado:
        return CIERRE_DOCUMENTAL
    return ESPERAR_DECISION_HUMANA


__all__ = [
    "BLOQUEO_TECNICO",
    "CIERRE_DOCUMENTAL",
    "ESPERAR_DECISION_HUMANA",
    "PLAYBOOK_COMPONER_CARTA_PRESENTACION",
    "PLAYBOOK_VEREDICTO_FINAL_CARTA",
    "siguiente_accion_carta",
]
