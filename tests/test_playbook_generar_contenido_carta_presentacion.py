import re
import unittest
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / "scripts/job-up/verificar_contenido_carta.py"
_SPEC = importlib.util.spec_from_file_location("verificar_contenido_carta", VERIFIER)
_MODULE = importlib.util.module_from_spec(_SPEC)
assert _SPEC and _SPEC.loader
_SPEC.loader.exec_module(_MODULE)
auditar_texto_visible = _MODULE.auditar_texto_visible
extract_visible_letter = _MODULE.extract_visible_letter
validar_autorizacion_editorial = _MODULE.validar_autorizacion_editorial


CAND_DIR = (
    ROOT
    / "boveda-entrevista-profesional"
    / "busqueda-empleo"
    / "candidaturas"
    / "CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite"
)
CONTENT = CAND_DIR / "contenido-carta-presentacion.md"
CONTENT_GATE = CAND_DIR / "evaluacion-gate-contenido-carta-composicion.md"
GUIDE_GATE = CAND_DIR / "evaluacion-gate-guion-carta-contenido.md"
GUIDE = CAND_DIR / "guion-carta-presentacion.md"
PLAYBOOK = ROOT / "docs/metodologia/playbooks/PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION.md"
TEMPLATE = ROOT / "boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_CONTENIDO_CARTA_PRESENTACION.md"


class CartaContentContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = CONTENT.read_text(encoding="utf-8")
        cls.guide = GUIDE.read_text(encoding="utf-8")
        cls.playbook = PLAYBOOK.read_text(encoding="utf-8")
        cls.template = TEMPLATE.read_text(encoding="utf-8")
        cls.consolidated = extract_visible_letter(cls.content)

    def test_v11_contract_is_active_in_trial(self):
        self.assertIn('version: "1.1.0"', self.playbook)
        self.assertIn('version: "1.1.0"', self.template)
        self.assertIn("estado: en_prueba", self.playbook)
        self.assertIn("estado: en_prueba", self.template)
        self.assertIn("conjunto cerrado de afirmaciones autorizadas", self.playbook.casefold())
        self.assertIn("conjunto cerrado de afirmaciones autorizadas", self.template.casefold())
        for test_id in ("T19", "T20", "T21", "T22"):
            self.assertIn(test_id, self.playbook)
            self.assertIn(test_id, self.template)

    def test_real_artifact_and_gate_preconditions(self):
        self.assertTrue(CONTENT.exists())
        self.assertIn("decision_humana: aprobado", GUIDE_GATE.read_text(encoding="utf-8"))
        self.assertIn("estado_gate: aprobado", GUIDE_GATE.read_text(encoding="utf-8"))
        self.assertIn("estado_guion: apto", self.guide)
        self.assertIn("estado_contenido: apto", self.content)
        self.assertIn("recomendacion_gate: aprobar", self.content)
        self.assertTrue((CAND_DIR / "carta-presentacion.docx").exists())
        self.assertTrue((CAND_DIR / "carta-presentacion.pdf").exists())
        self.assertTrue((CAND_DIR / "evaluacion-composicion-carta-presentacion.md").exists())
        self.assertFalse((CAND_DIR / "carta-presentacion.tex").exists())

    def test_real_artifact_requires_editorial_and_factual_authority(self):
        guide = GUIDE.read_text(encoding="utf-8")
        result = validar_autorizacion_editorial(guide, self.content, self.consolidated)
        self.assertTrue(result["autorizacion_editorial"])
        self.assertTrue(result["trazabilidad_factual"])
        self.assertEqual("apto", result["estado"])
        self.assertNotIn("negociaba directamente", self.consolidated.casefold())
        self.assertNotIn("cuadres de caja", self.consolidated.casefold())

    def test_roles_and_mandatory_sequence_are_recorded(self):
        for phrase in (
            "Redactor senior",
            "Recruiter senior",
            "Auditor factual",
            "Primera lectura recruiter",
            "Segunda lectura recruiter",
            "corrección factual",
        ):
            self.assertIn(phrase, self.content)
        self.assertIn("ROL 1 — Redactor", self.playbook)
        self.assertIn("ROL 2 — Recruiter", self.playbook)
        self.assertIn("ROL 3 — Auditor", self.playbook)
        self.assertIn("segunda lectura como recruiter", self.playbook)

    def test_human_gate_approval_records_only_composition_authorization(self):
        gate = CONTENT_GATE.read_text(encoding="utf-8")
        self.assertIn('version_contenido: "1.1.0"', gate)
        self.assertIn("decision_humana_anterior: no_aprobado", gate)
        self.assertIn("estado_gate_anterior: requiere_correccion", gate)
        self.assertIn("decision_humana: aprobado", gate)
        self.assertIn("estado_gate: aprobado", gate)
        self.assertIn("autoriza únicamente el avance desde el contenido semántico a la futura composición", gate)
        self.assertIn("GATE-CANDIDATURA-PRESENTACION", gate)

    def test_t1_no_personal_motivation(self):
        self.assertIn("motivaciones_autorizadas: []", self.content)
        self.assertNotRegex(self.consolidated.casefold(), r"me apasiona|siempre he querido|me identifico con|admiro lidl|comparto sus valores")

    def test_t2_culture_is_context_only(self):
        self.assertIn("contexto de Lidl", self.content)
        self.assertNotRegex(self.consolidated.casefold(), r"me identifico|comparto sus valores|admiro lidl|me apasiona")

    def test_t3_anonymous_company_rule_is_in_contract(self):
        self.assertIn("# 26. Empresa anónima", self.playbook)
        self.assertIn("empresa_anonima:", self.guide)
        self.assertIn("| Empresa objetivo |", self.template)
        self.assertIn("| Destinatario |", self.template)

    def test_t4_unauthorized_keywords_are_absent(self):
        for term in ("SAP", "tesorería", "banca", "experiencia previa en Lidl", "FP terminada"):
            self.assertNotIn(term.casefold(), self.consolidated.casefold())

    def test_t5_unselected_evidence_is_absent(self):
        for term in ("HER-01", "HER-02", "HER-05", "HER-09", "programación", "inteligencia artificial"):
            self.assertNotIn(term.casefold(), self.consolidated.casefold())

    def test_t6_second_cv_control(self):
        self.assertIn("resultado: interpreta_y_conecta", self.content)
        self.assertNotIn("repite_cv", self.content)

    def test_t7_generic_letter_control(self):
        self.assertIn("podria_enviarse_a_otra_empresa_cambiando_solo_el_nombre: no", self.content)

    def test_t8_artificial_enthusiasm_control(self):
        self.assertIn("elogios genéricos", self.content.casefold())
        self.assertIn("Elogios genéricos | no", self.content)

    def test_t9_length_range(self):
        match = re.search(r"palabras_reales: (\d+)", self.content)
        self.assertIsNotNone(match)
        words = int(match.group(1))
        self.assertGreaterEqual(words, 180)
        self.assertLessEqual(words, 280)

    def test_t10_untraceable_claim_control(self):
        self.assertIn("No se detectan afirmaciones profesionales nuevas", self.content)
        self.assertIn("# 26. No expansión semántica", self.template)

    def test_t11_new_evidence_is_not_added(self):
        self.assertIn("Nueva evidencia profesional", self.content)
        self.assertIn("detectada: no", self.content)

    def test_t12_semantic_boundary_is_closed(self):
        self.assertIn("No se detecta ninguna decisión nueva", self.content)
        self.assertIn("No se detecta ninguna decisión nueva ni expansión semántica", self.content)

    def test_t13_restriction_is_not_visible_content(self):
        result = auditar_texto_visible("Realizaba cuadres de caja y desarrollé un sistema en Excel para mejorar su control.")
        self.assertEqual("apto", result["estado"])
        self.assertEqual([], result["lenguaje_defensivo"])

    def test_t14_auditor_voice_is_rejected(self):
        result = auditar_texto_visible("La evidencia demuestra que el candidato cumple el requisito.")
        self.assertEqual("requiere_correccion", result["estado"])
        self.assertTrue(result["voz_auditor_sistema"])

    def test_t15_meta_analytical_language_is_rejected(self):
        result = auditar_texto_visible("Según el análisis, esta experiencia conecta con la necesidad de la oferta.")
        self.assertEqual("requiere_correccion", result["estado"])
        self.assertTrue(result["lenguaje_metaanalitico"])

    def test_t16_visible_internal_precaution_is_rejected(self):
        result = auditar_texto_visible("Mi experiencia se limita a realizar cuadres de caja.")
        self.assertEqual("requiere_correccion", result["estado"])
        self.assertTrue(result["lenguaje_defensivo"])

    def test_t17_anti_ai_reasonable_coverage(self):
        result = auditar_texto_visible("Me complace enormemente aportar soluciones innovadoras en un entorno dinámico y desafiante.")
        self.assertEqual("requiere_correccion", result["estado"])
        self.assertTrue(result["senales_ia"])
        self.assertIn("anti-IA", self.playbook)

    def test_t18_factual_regression_requires_second_recruiter(self):
        result = auditar_texto_visible("Sin afirmar experiencia en Lidl, mi experiencia se limita a tiendas anteriores.")
        self.assertTrue(result["requiere_segunda_lectura_recruiter"])
        self.assertEqual("requiere_correccion", result["estado"])
        self.assertIn("Control de regresión tras auditoría", self.template)

    def test_t19_factual_evidence_not_selected_is_rejected(self):
        guide = "| A-001 | función | idea | hecho | HER-03 | necesidad | incluir | 1 | límite |"
        content = "## 6.1 Conjunto cerrado de afirmaciones autorizadas\n\n| claim_id | Refs. guion | Evidencia | Frase |\n| --- | --- | --- | --- |\n| CL-001 | A-001 | HER-09 | Gestioné pedidos. |\n"
        result = validar_autorizacion_editorial(guide, content, "Gestioné pedidos.")
        self.assertFalse(result["trazabilidad_factual"])
        self.assertEqual("requiere_correccion", result["estado"])
        self.assertIn("evidencia_no_seleccionada", " ".join(result["errores_factuales"]))

    def test_t20_factual_trace_without_editorial_authorization_is_rejected(self):
        guide = "| A-001 | función | idea | hecho | HER-03 | necesidad | incluir | 1 | límite |"
        content = "## 6.1 Conjunto cerrado de afirmaciones autorizadas\n\n| claim_id | Refs. guion | Evidencia | Frase |\n| --- | --- | --- | --- |\n| CL-001 |  | HER-03 | Gestioné pedidos. |\n"
        result = validar_autorizacion_editorial(guide, content, "Gestioné pedidos.")
        self.assertFalse(result["autorizacion_editorial"])
        self.assertIn("sin_A-NNN", " ".join(result["errores_autorizacion"]))

    def test_t21_block_with_insufficient_a_ref_is_rejected(self):
        guide = "| A-001 | función | idea | hecho | HER-03 | necesidad | incluir | 1 | límite |"
        content = "## 6.1 Conjunto cerrado de afirmaciones autorizadas\n\n| claim_id | Refs. guion | Evidencia | Frase |\n| --- | --- | --- | --- |\n| CL-001 | A-001 | HER-03 | Gestioné pedidos. |\n"
        result = validar_autorizacion_editorial(guide, content, "Gestioné pedidos. También negocié contratos.")
        self.assertFalse(result["autorizacion_editorial"])
        self.assertTrue(result["afirmaciones_visibles_no_declaradas"])

    def test_t22_auditor_requires_editorial_and_factual_authority(self):
        guide = "| A-001 | función | idea | hecho | HER-03 | necesidad | incluir | 1 | límite |"
        content = "## 6.1 Conjunto cerrado de afirmaciones autorizadas\n\n| claim_id | Refs. guion | Evidencia | Frase |\n| --- | --- | --- | --- |\n| CL-001 | A-001 | HER-03 | Gestioné pedidos. |\n"
        result = validar_autorizacion_editorial(guide, content, "Gestioné pedidos.")
        self.assertTrue(result["autorizacion_editorial"])
        self.assertTrue(result["trazabilidad_factual"])
        self.assertEqual("apto", result["estado"])


if __name__ == "__main__":
    unittest.main()
