"""Pruebas del contrato de guion de carta de presentación."""

from pathlib import Path
import importlib.util
import unittest


ROOT = Path(__file__).resolve().parents[1]
PLAYBOOK = ROOT / "docs" / "metodologia" / "playbooks" / "PLAYBOOK_GUION_CARTA_PRESENTACION.md"
TEMPLATE = ROOT / "boveda-entrevista-profesional" / "busqueda-empleo" / "proceso" / "plantillas" / "TEMPLATE_GUION_CARTA_PRESENTACION.md"
CAND_DIR = ROOT / "boveda-entrevista-profesional" / "busqueda-empleo" / "candidaturas" / "CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite"
GUIDE = CAND_DIR / "guion-carta-presentacion.md"
GATE = CAND_DIR / "evaluacion-gate-guion-carta-contenido.md"
MODULE_PATH = ROOT / "scripts" / "job-up" / "verificar_guion_carta.py"


def load_module():
    spec = importlib.util.spec_from_file_location("verificar_guion_carta", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class PlaybookAndTemplateTests(unittest.TestCase):
    def test_contract_declares_cv_letter_separation_and_gate(self):
        playbook = read(PLAYBOOK)
        template = read(TEMPLATE)
        self.assertIn("alcance: exclusivo_carta_presentacion", playbook)
        self.assertIn("gate_entrada: GATE-CANDIDATURA-GUION", playbook)
        self.assertIn("GATE-GUION-CARTA-CONTENIDO", playbook)
        self.assertIn("empresa_anonima", playbook)
        self.assertIn("motivacion_declarada", playbook)
        self.assertIn("Qué debe interpretar del CV", template)
        self.assertIn("Qué debe contextualizar", template)
        self.assertIn("Qué NO debe repetir", template)


class LidlArtifactTests(unittest.TestCase):
    def test_lidl_artifacts_exist_and_do_not_contain_final_letter(self):
        guide = read(GUIDE)
        gate = read(GATE)
        self.assertIn("CAND-2026-020", guide)
        self.assertIn("Lidl Supermercados SAU", guide)
        self.assertIn("Indeed", guide)
        self.assertIn("#teamlidl", guide)
        self.assertIn("HER-03", guide)
        self.assertIn("HER-07", guide)
        self.assertIn("HER-10", guide)
        self.assertIn("estado_guion: apto", guide)
        self.assertNotIn("carta-presentacion.md", guide)
        self.assertNotIn("carta.docx", guide)
        self.assertNotIn("carta.pdf", guide)
        self.assertIn("recomendacion_ia: aprobar", gate)
        self.assertIn("resultado_evaluacion: apto", gate)
        self.assertIn("decision_humana: aprobado", gate)
        self.assertIn("estado_gate: aprobado", gate)

    def test_lidl_keeps_external_source_optional_and_motivation_uninvented(self):
        guide = read(GUIDE)
        self.assertIn("url: https://empleo.lidl.es/", guide)
        self.assertIn("consultada", guide)
        self.assertIn("motivacion_declarada: ninguna", guide)
        self.assertIn("promoción interna", guide)
        self.assertIn("No afirmar", guide)
        self.assertIn("comparto plenamente sus valores", guide.lower())


class RequiredScenarioTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def test_t1_url_aportada_al_inicio_no_se_vuelve_a_pedir(self):
        result = self.module.resolver_fuente_externa(True, "https://empleo.example/", False)
        self.assertFalse(result["solicitar_url"])
        self.assertEqual("usar_url_registrada", result["estado"])

    def test_t2_empresa_identificada_sin_url_permite_pedirla_sin_bloquear(self):
        result = self.module.resolver_fuente_externa(True, "", False)
        self.assertTrue(result["solicitar_url"])
        self.assertFalse(result["bloquea"])

    def test_t3_empresa_anonima_no_pide_url_ni_inventa_identidad(self):
        result = self.module.clasificar_destinatario("", "Indeed", "Randstad", True)
        self.assertFalse(result["solicitar_url"])
        self.assertTrue(result["empresa_anonima"])
        self.assertEqual("intermediario_con_empresa_anonima", result["tipo"])

    def test_t4_motivacion_ausente_no_se_inventa(self):
        self.assertEqual("no_registrada", self.module.clasificar_motivacion(""))

    def test_t5_motivacion_explicita_es_utilizable(self):
        self.assertEqual("declarada", self.module.clasificar_motivacion("Me interesa volver a operaciones de supermercados."))

    def test_t6_cultura_sin_conexion_no_se_convierte_en_afinidad(self):
        self.assertFalse(self.module.puede_atribuir_afinidad("equipo dinámico", False))

    def test_t7_keyword_sin_evidencia_queda_prohibida(self):
        self.assertEqual("prohibido_como_atributo", self.module.clasificar_keyword("SAP", False))

    def test_t8_segundo_cv_requiere_correccion(self):
        estado = self.module.evaluar_estado_guion(segundo_cv=True, generico=False, motivacion_faltante=False)
        self.assertEqual("requiere_correccion", estado)

    def test_t9_guion_generico_requiere_correccion(self):
        estado = self.module.evaluar_estado_guion(segundo_cv=False, generico=True, motivacion_faltante=False)
        self.assertEqual("requiere_correccion", estado)


if __name__ == "__main__":
    unittest.main()
