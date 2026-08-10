"""Auditoría determinista de guardarraíles visibles de una carta.

El verificador no decide estrategia ni reescribe el texto. Solo identifica
señales que obligan a revisar el contenido con los roles del playbook.
"""

from __future__ import annotations

import re
from pathlib import Path


_DEFENSIVE_PATTERNS = (
    r"\bsin convertir\b",
    r"\bsin afirmar\b",
    r"\bsin presentar\b",
    r"\bsin atribuir\b",
    r"\bmi experiencia se limita\b",
    r"\bno debe confundirse con\b",
    r"\baunque no\b",
)
_AUDITOR_VOICE_PATTERNS = (
    r"\bla evidencia (?:demuestra|acredita)\b",
    r"\bel candidato\b",
    r"\bla candidatura\b",
    r"\bestá confirmado\b",
    r"\bse ha identificado\b",
)
_META_PATTERNS = (
    r"\bsegún el análisis\b",
    r"\bel contexto de la oferta\b",
    r"\bla oferta describe\b",
    r"\besta experiencia conecta con la necesidad\b",
    r"\bde acuerdo con el guion\b",
)
_AI_SIGNAL_PATTERNS = (
    r"\bme complace enormemente\b",
    r"\bdesde siempre\b",
    r"\bapasionad[oa] por\b",
    r"\bsoluciones innovadoras\b",
    r"\bentorno dinámico y desafiante\b",
)


def _matches(text: str, patterns: tuple[str, ...]) -> list[str]:
    lowered = text.casefold()
    return [pattern for pattern in patterns if re.search(pattern, lowered)]


def extract_visible_letter(content: str) -> str:
    """Extrae la carta consolidada sin interpretar el resto del expediente."""
    marker_match = re.search(r"^## \d+\. Carta completa consolidada\s*$", content, re.MULTILINE)
    if not marker_match:
        raise ValueError("No se encontró la carta completa consolidada")
    visible = content[marker_match.end() :]
    next_heading = re.search(r"\n## \d+\.", visible)
    if next_heading:
        visible = visible[: next_heading.start()]
    return visible.strip()


def auditar_texto_visible(text: str) -> dict[str, object]:
    """Devuelve señales y estado; nunca modifica el texto recibido."""
    defensive = _matches(text, _DEFENSIVE_PATTERNS)
    auditor_voice = _matches(text, _AUDITOR_VOICE_PATTERNS)
    meta = _matches(text, _META_PATTERNS)
    ai_signals = _matches(text, _AI_SIGNAL_PATTERNS)
    sentences = [item.strip() for item in re.split(r"[.!?]+", text) if item.strip()]
    utility_ok = bool(sentences) and all(len(sentence.split()) >= 3 for sentence in sentences)
    status = "apto" if not any((defensive, auditor_voice, meta, ai_signals)) and utility_ok else "requiere_correccion"
    return {
        "lenguaje_defensivo": defensive,
        "voz_auditor_sistema": auditor_voice,
        "lenguaje_metaanalitico": meta,
        "senales_ia": ai_signals,
        "utilidad_frase": utility_ok,
        "requiere_segunda_lectura_recruiter": bool(defensive or auditor_voice or meta),
        "estado": status,
    }


def auditar_archivo(path: str | Path) -> dict[str, object]:
    """Audita el texto consolidado de un artefacto Markdown."""
    source = Path(path).read_text(encoding="utf-8")
    return auditar_texto_visible(extract_visible_letter(source))


if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) != 2:
        raise SystemExit("Uso: python verificar_contenido_carta.py <contenido-carta.md>")
    print(json.dumps(auditar_archivo(sys.argv[1]), ensure_ascii=False, indent=2))
