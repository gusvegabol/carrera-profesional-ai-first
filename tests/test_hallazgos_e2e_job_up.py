import unittest
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / ".codex/skills/job-up-candidatura-oferta/SKILL.md").read_text(encoding="utf-8")
PLAYBOOK = (ROOT / "docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md").read_text(encoding="utf-8")
COMPOSITOR = (ROOT / "scripts/job-up/componer_carta_presentacion.py").read_text(encoding="utf-8")
DATA_CORE = (ROOT / "boveda-entrevista-profesional/busqueda-empleo/fuentes/datos-core-busqueda.md").read_text(encoding="utf-8")
CANDIDATE = ROOT / "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-021-obramat-coordinador-linea-cajas"
CANDIDATE_CLOSED = ROOT / "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-023-estudio-santa-lucia-auxiliar-administrativo"


def load_transition_module():
    helper_path = ROOT / "scripts/job-up/orquestar_transiciones.py"
    if not helper_path.is_file():
        return None
    spec = importlib.util.spec_from_file_location("orquestar_transiciones", helper_path)
    if spec is None or spec.loader is None:
        return None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class HallazgosE2ETests(unittest.TestCase):
    def test_t_e2e_01_fotografia_cv_default_no_pregunta(self):
        self.assertIn("fotografía incluida por defecto", SKILL)
        self.assertIn("no genera pregunta, pendiente ni bloqueo", SKILL)
        self.assertIn("fotografía se incluye por defecto", PLAYBOOK)
        self.assertIn("fotografia: incluir", (CANDIDATE / "candidatura.md").read_text(encoding="utf-8"))

    def test_t_e2e_02_vehiculo_propio_es_reutilizable(self):
        self.assertIn("Vehículo propio", DATA_CORE)
        self.assertIn("dato profesional reutilizable", DATA_CORE)
        self.assertIn("vehículo propio", (CANDIDATE / "candidatura.md").read_text(encoding="utf-8").lower())

    def test_t_e2e_03_movilidad_se_resuelve_antes_del_gate(self):
        self.assertIn("Antes de cerrar `GATE-CANDIDATURA-GUION`", PLAYBOOK)
        self.assertIn("movilidad territorial", PLAYBOOK.lower())
        self.assertIn("Decisión específica", PLAYBOOK)

    def test_t_e2e_04_cultura_es_contexto_temprano(self):
        self.assertIn("Tras identificar la empresa", PLAYBOOK)
        self.assertIn("La cultura es contexto", PLAYBOOK)
        self.assertIn("afinidad personal", PLAYBOOK)

    def test_t_e2e_05_y_06_transiciones_deterministas(self):
        self.assertIn("gate aprobado", SKILL)
        self.assertIn("continúa automáticamente", SKILL)
        self.assertIn("no se requiere revisión humana", SKILL)

    def test_t_e2e_06b_revision_carta_aprobada_selecciona_veredicto_sin_pausa(self):
        """La transición efectiva no puede limitarse a una regla declarativa."""
        module = load_transition_module()
        self.assertIsNotNone(module, "falta el mecanismo ejecutable de transición")
        estado = {
            "gate_contenido_carta_composicion": "aprobado",
            "carta_compuesta": True,
            "gate_carta_revision_humana": "aprobado",
            "gate_veredicto_carta": "pendiente",
            "cv_aprobado": True,
            "datos_pendientes": [],
            "bloqueo_tecnico": False,
            "presentada": False,
        }
        self.assertEqual(
            module.siguiente_accion_carta(estado),
            "PLAYBOOK_VEREDICTO_FINAL_CARTA",
        )

    def test_t_e2e_06c_contenido_carta_aprobado_selecciona_composicion(self):
        module = load_transition_module()
        self.assertIsNotNone(module)
        self.assertEqual(
            module.siguiente_accion_carta(
                {
                    "gate_contenido_carta_composicion": "aprobado",
                    "carta_compuesta": False,
                    "gate_carta_revision_humana": "pendiente",
                    "gate_veredicto_carta": "pendiente",
                    "datos_pendientes": [],
                    "presentada": False,
                }
            ),
            "PLAYBOOK_COMPONER_CARTA_PRESENTACION",
        )

    def test_t_e2e_06d_gate_humano_pendiente_sigue_si_endpoint_humano(self):
        module = load_transition_module()
        self.assertIsNotNone(module)
        self.assertEqual(
            module.siguiente_accion_carta(
                {
                    "gate_contenido_carta_composicion": "aprobado",
                    "carta_compuesta": True,
                    "gate_carta_revision_humana": "pendiente",
                    "gate_veredicto_carta": "pendiente",
                    "datos_pendientes": [],
                    "presentada": False,
                }
            ),
            "ESPERAR_DECISION_HUMANA",
        )

    def test_t_e2e_06e_veredicto_aprobado_cierra_sin_presentacion(self):
        module = load_transition_module()
        self.assertIsNotNone(module)
        self.assertEqual(
            module.siguiente_accion_carta(
                {
                    "gate_contenido_carta_composicion": "aprobado",
                    "carta_compuesta": True,
                    "gate_carta_revision_humana": "aprobado",
                    "gate_veredicto_carta": "aprobado",
                    "cv_aprobado": True,
                    "datos_pendientes": [],
                    "presentada": False,
                }
            ),
            "CIERRE_DOCUMENTAL",
        )

    def test_t_e2e_06f_gate_bloqueado_no_continua(self):
        module = load_transition_module()
        self.assertIsNotNone(module)
        self.assertEqual(
            module.siguiente_accion_carta(
                {
                    "gate_contenido_carta_composicion": "aprobado",
                    "carta_compuesta": True,
                    "gate_carta_revision_humana": "aprobado",
                    "gate_veredicto_carta": "bloqueado",
                    "cv_aprobado": True,
                    "datos_pendientes": [],
                    "presentada": False,
                }
            ),
            "BLOQUEO_TECNICO",
        )

    def test_t_e2e_07_hard_wrap_y_saltos_manuales(self):
        self.assertIn("hard wrapping Markdown", (ROOT / "docs/metodologia/playbooks/PLAYBOOK_COMPONER_CARTA_PRESENTACION.md").read_text(encoding="utf-8"))
        self.assertIn("saltos_manuales_word_por_salto_simple: prohibidos", (ROOT / "boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_COMPOSICION_CARTA_PRESENTACION.md").read_text(encoding="utf-8"))
        self.assertNotIn("add_break()", COMPOSITOR)

    def test_t_e2e_08_render_generado_no_equivale_a_inspeccion(self):
        self.assertIn("render_generado", COMPOSITOR)
        self.assertIn("render_inspeccionado", COMPOSITOR)
        self.assertIn("pendiente_de_inspeccion_real", COMPOSITOR)

    def test_t_e2e_09_identidad_dinamica(self):
        for forbidden in ("CAND-2026-020", "Lidl", "Tamaraceite"):
            self.assertNotIn(forbidden, COMPOSITOR)
        evaluation = (CANDIDATE / "evaluacion-composicion-carta-presentacion.md").read_text(encoding="utf-8")
        self.assertIn("CAND-2026-021", evaluation)

    def test_t_e2e_10_y_11_fin_documental(self):
        ficha = (CANDIDATE_CLOSED / "candidatura.md").read_text(encoding="utf-8")
        self.assertIn("estado: documentalmente_completa", ficha)
        self.assertIn("presentada: false", ficha)
        self.assertIn("no_aplica_en_esta_fase", ficha)
        self.assertFalse((CANDIDATE_CLOSED / "paquete-presentacion.md").exists())

    def test_t_e2e_12_contrato_visual_carta(self):
        playbook = (ROOT / "docs/metodologia/playbooks/PLAYBOOK_COMPONER_CARTA_PRESENTACION.md").read_text(encoding="utf-8")
        template = (ROOT / "boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_COMPOSICION_CARTA_PRESENTACION.md").read_text(encoding="utf-8")
        for text in (playbook, template):
            self.assertIn("18 pt", text)
            self.assertIn("10,5 pt", text)
            self.assertIn("fecha", text.lower())
            self.assertIn("asunto", text.lower())
        self.assertIn("JUSTIFY", COMPOSITOR)

    def test_recomendacion_carta_no_es_paquete(self):
        active = (ROOT / "docs/metodologia/playbooks/PLAYBOOK_VEREDICTO_FINAL_CARTA.md").read_text(encoding="utf-8")
        template = (ROOT / "boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_VEREDICTO_FINAL_CARTA.md").read_text(encoding="utf-8")
        self.assertNotIn("recomendacion_inclusion_paquete", active)
        self.assertNotIn("recomendacion_inclusion_paquete", template)
        self.assertIn("recomendacion_inclusion_carta", active)


if __name__ == "__main__":
    unittest.main()
