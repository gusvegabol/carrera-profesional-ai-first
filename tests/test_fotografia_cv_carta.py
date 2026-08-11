import json
import unittest
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "boveda-entrevista-profesional" / "busqueda-empleo" / "candidaturas" / "CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite"
PLAYBOOK = ROOT / "docs" / "metodologia" / "playbooks" / "PLAYBOOK_CANDIDATURA_POR_OFERTA.md"
GUIDE = ROOT / "boveda-entrevista-profesional" / "busqueda-empleo" / "proceso" / "plantillas" / "GUIA_FORMATO_CV_Y_CARTA.md"
LETTER_TEMPLATE = ROOT / "boveda-entrevista-profesional" / "busqueda-empleo" / "proceso" / "plantillas" / "TEMPLATE_CARTA_PRESENTACION_FORMATO.md"
LETTER_PLAYBOOK = ROOT / "docs" / "metodologia" / "playbooks" / "PLAYBOOK_COMPONER_CARTA_PRESENTACION.md"
SPEC = ROOT / "docs" / "ideas-y-debates" / "mejoras-job-up" / "SPEC-Arquitectura-modular-generación-candidatura-v0-4-0.md"


def media_entries(docx: Path) -> list[str]:
    with ZipFile(docx) as archive:
        return [name for name in archive.namelist() if name.startswith("word/media/")]


class FotografiaCVCartaTests(unittest.TestCase):
    def test_t_foto_01_cv_con_autorizacion_incluye_fotografia(self):
        payload = json.loads((CANDIDATE / "datos-generacion.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["control"]["datos_privados"]["autorizacion"]["fotografia"], "incluir")
        self.assertTrue(media_entries(CANDIDATE / "cv.docx"))

    def test_t_foto_03_carta_autorizada_para_cv_sigue_sin_fotografia(self):
        payload = json.loads((CANDIDATE / "datos-generacion.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["control"]["datos_privados"]["autorizacion"]["fotografia"], "incluir")
        self.assertEqual(media_entries(CANDIDATE / "carta-presentacion.docx"), [])

    def test_t_foto_04_ausencia_de_foto_en_carta_no_bloquea_su_gate(self):
        evaluation = (CANDIDATE / "veredicto-final-carta.md").read_text(encoding="utf-8")
        self.assertIn("resultado_final: APTA", evaluation)
        self.assertIn("estado: aprobado", evaluation)
        self.assertEqual(media_entries(CANDIDATE / "carta-presentacion.docx"), [])

    def test_t_foto_05_fuentes_activas_no_imponen_foto_compartida(self):
        old_rule = "fotografía obligatoria por defecto, tanto en CV como en carta"
        for path in (PLAYBOOK, GUIDE, LETTER_TEMPLATE, LETTER_PLAYBOOK):
            self.assertNotIn(old_rule, path.read_text(encoding="utf-8").lower())
        self.assertIn("carta", GUIDE.read_text(encoding="utf-8").lower())
        self.assertIn("no se incluye por defecto", LETTER_TEMPLATE.read_text(encoding="utf-8").lower())

    def test_t_foto_06_autorizacion_no_implica_renderizado_universal(self):
        self.assertTrue(media_entries(CANDIDATE / "cv.docx"))
        self.assertFalse(media_entries(CANDIDATE / "carta-presentacion.docx"))
        self.assertIn("renderiza fotografías", LETTER_PLAYBOOK.read_text(encoding="utf-8"))

    def test_contrato_especifico_por_artefacto_esta_en_la_spec(self):
        spec = SPEC.read_text(encoding="utf-8")
        self.assertIn("ARQ-24 — Política de fotografía específica por artefacto", spec)
        self.assertIn("la carta no incluye fotografía por", spec.lower())
        self.assertIn("no implica", spec.lower())
        self.assertIn("mostrarla automáticamente en la carta", spec.lower())


if __name__ == "__main__":
    unittest.main()
