import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "ideas-y-debates" / "mejoras-job-up"
PLAYBOOK = DOCS / "PLAYBOOK_VEREDICTO_FINAL_CV.md"
TEMPLATE = DOCS / "TEMPLATE_VEREDICTO_FINAL_CV.md"
REVISION_TEMPLATE = DOCS / "TEMPLATE_REVISION_HUMANA_CV.md"
PACKAGE_TEMPLATE = DOCS / "TEMPLATE_PAQUETE_PRESENTACION.md"


class ContratoVeredictoFinalCVTests(unittest.TestCase):
    def test_playbook_y_templates_declaran_contrato_v110_completo(self):
        playbook = PLAYBOOK.read_text(encoding="utf-8")
        template = TEMPLATE.read_text(encoding="utf-8")
        revision = REVISION_TEMPLATE.read_text(encoding="utf-8")

        package = PACKAGE_TEMPLATE.read_text(encoding="utf-8")

        self.assertIn('version: "1.1.0"', playbook)
        self.assertIn('version: "1.1.0"', template)
        self.assertIn("revision-humana-cv.md", playbook)
        self.assertIn("GATE-VEREDICTO-CV", playbook)
        self.assertNotIn("GATE-VEREDICTO-CV-PRESENTACION", playbook)
        self.assertIn("GATE-CANDIDATURA-PRESENTACION", package)
        self.assertIn("presentada: true", package)
        self.assertIn("Rol A", playbook)
        self.assertIn("Rol B", playbook)
        for criterio in ("C1", "C2", "C3", "C4", "C5", "C6"):
            self.assertIn(criterio, playbook)
            self.assertIn(criterio, template)
        for resultado in (
            "bloqueado_por_integridad",
            "requiere_correccion_de_flujo",
            "no_competitivo",
            "revisar_antes_de_presentar",
            "apto_para_presentacion",
        ):
            self.assertIn(resultado, playbook)
            self.assertIn(resultado, template)
        for campo in ("decision", "cv_revisado", "huella_cv", "fecha", "decidido_por"):
            self.assertIn(campo, revision)

    def test_casos_reales_tienen_revision_y_veredicto_actual_y_019_archiva_el_historico(self):
        expected = {
            "CAND-2026-019-asic-consultores-responsable-automatizacion-ia": "no_competitivo",
            "CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite": "apto_para_presentacion",
        }
        for candidate, resultado in expected.items():
            path = ROOT / "boveda-entrevista-profesional" / "busqueda-empleo" / "candidaturas" / candidate
            revision = path / "revision-humana-cv.md"
            veredicto = path / "veredicto-final-cv.md"
            self.assertTrue(revision.exists(), candidate)
            self.assertTrue(veredicto.exists(), candidate)
            revision_text = revision.read_text(encoding="utf-8")
            veredicto_text = veredicto.read_text(encoding="utf-8")
            self.assertIn("decision: aprobado_para_veredicto", revision_text)
            self.assertIn("estado_veredicto: completado", veredicto_text)
            self.assertIn(f"resultado_global: {resultado}", veredicto_text)
            self.assertIn("GATE-VEREDICTO-CV", veredicto_text)
            self.assertNotIn("GATE-VEREDICTO-CV-PRESENTACION", veredicto_text)
        historic = ROOT / "boveda-entrevista-profesional" / "busqueda-empleo" / "candidaturas" / "CAND-2026-019-asic-consultores-responsable-automatizacion-ia" / "historico" / "veredicto-final-cv-flujo-anterior.md"
        self.assertTrue(historic.exists())

    def test_lidl_no_se_considera_candidatura_completa_solo_por_aprobar_el_cv(self):
        candidate = ROOT / "boveda-entrevista-profesional" / "busqueda-empleo" / "candidaturas" / "CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite"
        ficha = (candidate / "candidatura.md").read_text(encoding="utf-8")
        paquete = (candidate / "paquete-presentacion.md").read_text(encoding="utf-8")
        self.assertIn("estado: en_preparacion", ficha)
        self.assertIn("paquete_presentacion: pendiente_de_preparacion", ficha)
        self.assertIn("gate_candidatura_presentacion: no_abierto", ficha)
        self.assertIn("estado: pendiente_de_preparacion", paquete)
        self.assertIn("| Canal de envío confirmado | pendiente de comprobar |", paquete)
        self.assertIn("Faltan canal confirmado", paquete)


if __name__ == "__main__":
    unittest.main()
