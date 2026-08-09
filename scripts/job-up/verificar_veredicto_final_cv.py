"""Controles técnicos del flujo posterior a la composición del CV.

El módulo no redacta ni modifica candidaturas: solo verifica identidad de versión,
precondiciones y precedencia del resultado del veredicto.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any


_REVISION_FIELDS = ("decision", "cv_revisado", "huella_cv", "fecha", "decidido_por")
_FIELD_PATTERN = re.compile(r"^\s{2,}(decision|cv_revisado|huella_cv|fecha|decidido_por):\s*(.*?)\s*$")


def calcular_huella(path: Path) -> str:
    """Devuelve la huella SHA-256 del artefacto binario indicado."""
    if not path.is_file():
        raise ValueError(f"No existe el artefacto para calcular la huella: {path}")
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _leer_revision(path: Path) -> dict[str, str]:
    if not path.is_file():
        raise ValueError("Falta revision-humana-cv.md.")
    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = _FIELD_PATTERN.match(line)
        if match:
            values[match.group(1)] = match.group(2).strip().strip('"')
    missing = [field for field in _REVISION_FIELDS if not values.get(field)]
    if missing:
        raise ValueError(f"Revisión humana incompleta: {', '.join(missing)}")
    return values


def validar_revision_humana(revision_path: Path, pdf_path: Path) -> dict[str, str]:
    """Valida decisión humana, archivo revisado y huella exacta del PDF actual."""
    values = _leer_revision(revision_path)
    if values["decision"] != "aprobado_para_veredicto":
        raise ValueError("La revisión humana no autoriza el veredicto.")
    if Path(values["cv_revisado"]).name != pdf_path.name:
        raise ValueError("La revisión humana identifica un artefacto distinto del PDF evaluado.")
    current_hash = calcular_huella(pdf_path)
    if values["huella_cv"].lower() != current_hash:
        raise ValueError("revision_humana_corresponde_a_otra_version")
    return values


def resultado_global(
    integridad: str,
    fidelidad: str,
    puntuaciones: list[int],
    *,
    no_competitivo: bool = False,
    corregible: bool = False,
) -> str:
    """Aplica la precedencia normativa sin utilizar la media como gate."""
    if integridad != "apta":
        return "bloqueado_por_integridad"
    if fidelidad != "apta":
        return "requiere_correccion_de_flujo"
    if not puntuaciones or any(score not in range(1, 6) for score in puntuaciones):
        raise ValueError("Las puntuaciones recruiter deben ser enteros entre 1 y 5.")
    if no_competitivo:
        return "no_competitivo"
    if corregible or any(score <= 3 for score in puntuaciones):
        return "revisar_antes_de_presentar"
    return "apto_para_presentacion"


def validar_precondiciones(candidatura_dir: Path) -> list[str]:
    """Devuelve bloqueos de entrada sin modificar ningún artefacto."""
    required = (
        "cv.pdf",
        "cv.docx",
        "datos-generacion.json",
        "guion-adaptacion-cv.md",
        "candidatura.md",
        "analisis-oferta.md",
        "revision-humana-cv.md",
        "manifest-generacion-cv.json",
        "evaluacion-gate-contenido-cv-composicion.md",
    )
    blocked = [name for name in required if not (candidatura_dir / name).is_file()]
    candidature = candidatura_dir / "candidatura.md"
    if candidature.is_file():
        text = candidature.read_text(encoding="utf-8")
        if not re.search(r"^presentada:\s*false\s*$", text, re.MULTILINE):
            blocked.append("presentada_no_es_false")
        auth_block = re.search(r"autorizacion_datos_cv:\s*(.*?)(?=\n---|\n#|\Z)", text, re.DOTALL)
        if auth_block is None or re.search(r":\s*pendiente\s*$", auth_block.group(1), re.MULTILINE):
            blocked.append("autorizacion_privacidad_no_resuelta")
    gate = candidatura_dir / "evaluacion-gate-contenido-cv-composicion.md"
    if gate.is_file() and "aprobado" not in gate.read_text(encoding="utf-8").lower():
        blocked.append("gate_contenido_no_aprobado")
    source_root = candidatura_dir.parents[1] / "fuentes"
    for source in ("datos-core-busqueda.md", "datos-privados-candidatura.md"):
        if not (source_root / source).is_file():
            blocked.append(source)
    return blocked


__all__ = ["calcular_huella", "resultado_global", "validar_precondiciones", "validar_revision_humana"]
