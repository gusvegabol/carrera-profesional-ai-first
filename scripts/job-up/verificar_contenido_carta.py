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
_GUIDE_REF_PATTERN = re.compile(r"\bA-\d{3}\b")
_EVIDENCE_PATTERN = re.compile(r"\b(?:HER|GRAN)-\d{2}\b")


def _matches(text: str, patterns: tuple[str, ...]) -> list[str]:
    lowered = text.casefold()
    return [pattern for pattern in patterns if re.search(pattern, lowered)]


def _table_cells(line: str) -> list[str]:
    if not line.lstrip().startswith("|"):
        return []
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def parse_guide_authorizations(guide_text: str) -> dict[str, set[str]]:
    """Devuelve el conjunto factual seleccionado por cada A-NNN del guion."""
    selected: dict[str, set[str]] = {}
    for line in guide_text.splitlines():
        cells = _table_cells(line)
        if len(cells) < 6 or not _GUIDE_REF_PATTERN.fullmatch(cells[0]):
            continue
        selected[cells[0]] = set(_EVIDENCE_PATTERN.findall(cells[4]))
    return selected


def _parse_authorized_claims(content_text: str) -> list[dict[str, object]]:
    marker = "## 6.1 Conjunto cerrado de afirmaciones autorizadas"
    if marker not in content_text:
        return []
    block = content_text.split(marker, 1)[1]
    block = block.split("\n## ", 1)[0]
    claims: list[dict[str, object]] = []
    for line in block.splitlines():
        cells = _table_cells(line)
        if len(cells) != 4 or cells[0] in {"claim_id", "---"}:
            continue
        if not cells[0].startswith("CL-"):
            continue
        claims.append(
            {
                "claim_id": cells[0],
                "refs_guion": set(_GUIDE_REF_PATTERN.findall(cells[1])),
                "evidencias": set(_EVIDENCE_PATTERN.findall(cells[2])),
                "frase": cells[3],
            }
        )
    return claims


def _normalise(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().casefold()


def _visible_sentences(text: str) -> list[str]:
    return [
        item.strip()
        for item in re.findall(r"[^.!?]+[.!?]", text, flags=re.DOTALL)
        if len(item.split()) >= 3
    ]


def validar_autorizacion_editorial(
    guide_text: str,
    content_text: str,
    visible_text: str,
) -> dict[str, object]:
    """Exige autorización A-NNN y respaldo factual para cada afirmación cerrada."""
    selected = parse_guide_authorizations(guide_text)
    claims = _parse_authorized_claims(content_text)
    errors: list[str] = []
    factual_errors: list[str] = []
    declared_sentences = set()

    if not claims:
        errors.append("falta_conjunto_cerrado_de_afirmaciones")

    for claim in claims:
        refs = claim["refs_guion"]
        evidences = claim["evidencias"]
        phrase = str(claim["frase"])
        declared_sentences.add(_normalise(phrase))
        if not refs:
            errors.append(f"{claim['claim_id']}:sin_A-NNN")
        compatible_evidence: set[str] = set()
        for ref in refs:
            if ref not in selected:
                errors.append(f"{claim['claim_id']}:{ref}_inexistente")
            else:
                compatible_evidence.update(selected[ref])
        if evidences and not evidences.issubset(compatible_evidence):
            factual_errors.append(f"{claim['claim_id']}:evidencia_no_seleccionada")

    undeclared = [
        sentence
        for sentence in _visible_sentences(visible_text)
        if _normalise(sentence) not in declared_sentences
        and not re.match(r"^(?:Estimado|A la atención|Atentamente)", sentence, re.IGNORECASE)
        and not re.fullmatch(r"(?:Gustavo Vega|[\w.+-]+@[\w.-]+|\d[\d ]+)[.!]?", sentence)
    ]
    if undeclared:
        errors.append("afirmacion_visible_fuera_del_conjunto_cerrado")

    return {
        "autorizacion_editorial": not errors,
        "trazabilidad_factual": not factual_errors,
        "errores_autorizacion": errors,
        "errores_factuales": factual_errors,
        "afirmaciones_visibles_no_declaradas": undeclared,
        "estado": "apto" if not errors and not factual_errors else "requiere_correccion",
    }


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
    artifact_path = Path(path)
    source = artifact_path.read_text(encoding="utf-8")
    visible = extract_visible_letter(source)
    result = auditar_texto_visible(visible)
    guide_path = artifact_path.with_name("guion-carta-presentacion.md")
    if guide_path.exists():
        authorization = validar_autorizacion_editorial(
            guide_path.read_text(encoding="utf-8"), source, visible
        )
        result.update(authorization)
        if authorization["estado"] != "apto":
            result["estado"] = "requiere_correccion"
    else:
        result.update(
            {
                "autorizacion_editorial": False,
                "trazabilidad_factual": False,
                "errores_autorizacion": ["guion_no_disponible"],
                "errores_factuales": [],
                "afirmaciones_visibles_no_declaradas": [],
                "estado": "requiere_correccion",
            }
        )
    return result


if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) != 2:
        raise SystemExit("Uso: python verificar_contenido_carta.py <contenido-carta.md>")
    print(json.dumps(auditar_archivo(sys.argv[1]), ensure_ascii=False, indent=2))
