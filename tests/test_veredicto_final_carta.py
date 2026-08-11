import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "job-up" / "verificar_veredicto_final_carta.py"


def load_module():
    spec = importlib.util.spec_from_file_location("verificador_veredicto_final_carta", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def roles(*, recruiter=None, editorial=None, auditor=None):
    base = {
        "recruiter": {"aplicado": True, "fuentes_compartidas_con_otro_rol": False, "hallazgos": []},
        "editorial": {"aplicado": True, "fuentes_compartidas_con_otro_rol": False, "hallazgos": []},
        "auditor": {"aplicado": True, "fuentes_compartidas_con_otro_rol": False, "hallazgos": []},
    }
    for key, value in (("recruiter", recruiter), ("editorial", editorial), ("auditor", auditor)):
        if value:
            base[key]["hallazgos"] = value
    return base


class VeredictoFinalCartaTests(unittest.TestCase):
    def test_t01_carta_correcta_produce_apta_y_t16_deja_gate_pendiente(self):
        module = load_module()
        result = module.sintetizar_hallazgos(roles(), valor_incremental="alto")
        self.assertEqual(result["resultado"], "APTA")
        self.assertEqual(module.estado_gate_salida(result["resultado"]), "pendiente")
        self.assertEqual(module.recomendar_inclusion("APTA", "alto"), "incluir")

    def test_t02_t12_valor_incremental_bajo_es_reserva_relevante(self):
        module = load_module()
        result = module.sintetizar_hallazgos(roles(), valor_incremental="bajo")
        self.assertEqual(result["resultado"], "APTA_CON_RESERVAS")
        self.assertEqual(module.recomendar_inclusion(result["resultado"], "bajo"), "incluir_con_reservas")

    def test_t03_t04_t05_y_t10_bloqueante_gobierna_no_apta(self):
        module = load_module()
        for finding in (
            {"categoria": "bloqueante", "descripcion": "Afirmación no autorizada"},
            {"categoria": "bloqueante", "descripcion": "Empresa o puesto incorrectos"},
            {"categoria": "bloqueante", "descripcion": "Contradicción con el CV"},
        ):
            result = module.sintetizar_hallazgos(roles(auditor=[finding]), valor_incremental="alto")
            self.assertEqual(result["resultado"], "NO_APTA")
            self.assertEqual(module.estado_gate_salida("NO_APTA"), "bloqueado")

    def test_t06_reserva_menor_no_bloquea_y_t07_reserva_moderada_si_cambia_resultado(self):
        module = load_module()
        minor = module.sintetizar_hallazgos(
            roles(editorial=[{"categoria": "reserva_menor", "descripcion": "Reiteración ligera"}]),
            valor_incremental="alto",
        )
        self.assertEqual(minor["resultado"], "APTA")
        relevant = module.sintetizar_hallazgos(
            roles(editorial=[{"categoria": "reserva_relevante", "descripcion": "Foco editorial moderadamente débil"}]),
            valor_incremental="alto",
        )
        self.assertEqual(relevant["resultado"], "APTA_CON_RESERVAS")

    def test_t08_gate_previo_no_aprobado_bloquea(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory)
            (candidate / "candidatura.md").write_text(
                "gate_carta_revision_humana: pendiente\n"
                "gate_candidatura_presentacion: no_abierto\n"
                "presentada: false\n",
                encoding="utf-8",
            )
            blockers = module.validar_precondiciones(candidate)
            self.assertIn("gate_carta_revision_humana_no_aprobado", blockers)

    def test_t08b_presentacion_fuera_de_alcance_no_bloquea_veredicto_ya_aprobado(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            candidate = Path(directory)
            for name in (
                "carta-presentacion.pdf",
                "carta-presentacion.docx",
                "contenido-carta-presentacion.md",
                "guion-carta-presentacion.md",
                "analisis-oferta.md",
                "cv.pdf",
                "evaluacion-composicion-carta-presentacion.md",
                "paquete-presentacion.md",
            ):
                (candidate / name).write_text("", encoding="utf-8")
            (candidate / "candidatura.md").write_text(
                "gate_carta_revision_humana: aprobado\n"
                "gate_candidatura_presentacion: no_aplica_en_esta_fase\n"
                "presentada: false\n",
                encoding="utf-8",
            )
            (candidate / "evaluacion-composicion-carta-presentacion.md").write_text(
                "estado_gate: aprobado\n", encoding="utf-8"
            )
            self.assertNotIn("gate_candidatura_presentacion_debe_seguir_no_abierto", module.validar_precondiciones(candidate))

    def test_t09_informacion_nueva_se_registra_fuera_de_fase_sin_incorporarla(self):
        module = load_module()
        incidence = module.registrar_informacion_nueva("Nuevo hecho profesional", "datos-core")
        self.assertEqual(incidence["tipo"], "incidencia_fuera_de_fase")
        self.assertEqual(incidence["incorporada"], "no")

    def test_t11_no_hay_votacion_por_mayoria(self):
        module = load_module()
        result = module.sintetizar_hallazgos(
            roles(
                recruiter=[{"categoria": "observacion", "descripcion": "Buena lectura"}],
                editorial=[{"categoria": "observacion", "descripcion": "Correcta"}],
                auditor=[{"categoria": "bloqueante", "descripcion": "Gate inválido"}],
            ),
            valor_incremental="alto",
        )
        self.assertEqual(result["resultado"], "NO_APTA")

    def test_t13_valor_medio_y_alto_sin_defectos_es_apta(self):
        module = load_module()
        for value in ("medio", "alto"):
            self.assertEqual(module.sintetizar_hallazgos(roles(), valor_incremental=value)["resultado"], "APTA")

    def test_t14_hecho_util_no_autorizado_no_se_propone_ni_penaliza(self):
        module = load_module()
        result = module.sintetizar_hallazgos(roles(), valor_incremental="alto")
        self.assertEqual(result["resultado"], "APTA")
        self.assertEqual(result["hallazgos_planos"], [])

    def test_t15_roles_independientes_y_t17_no_apta_requiere_nueva_iteracion(self):
        module = load_module()
        with self.assertRaises(ValueError):
            module.validar_roles({"recruiter": {"aplicado": True}})
        with self.assertRaises(ValueError):
            module.validar_roles(
                {
                    "recruiter": {"aplicado": True, "fuentes_compartidas_con_otro_rol": False},
                    "editorial": {"aplicado": True, "fuentes_compartidas_con_otro_rol": True},
                    "auditor": {"aplicado": True, "fuentes_compartidas_con_otro_rol": False},
                }
            )
        self.assertEqual(module.estado_gate_salida("NO_APTA"), "bloqueado")
        self.assertEqual(module.recomendar_inclusion("NO_APTA", "alto"), "no_incluir")

    def test_contrato_documental_y_caso_real(self):
        module = load_module()
        playbook = (ROOT / "docs/metodologia/playbooks/PLAYBOOK_VEREDICTO_FINAL_CARTA.md").read_text(encoding="utf-8")
        template = (ROOT / "boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_VEREDICTO_FINAL_CARTA.md").read_text(encoding="utf-8")
        for token in ("PLAYBOOK_VEREDICTO_FINAL_CARTA", "version: \"1.0.0\"", "estado: en_prueba", "GATE-VEREDICTO-CARTA", "APTA_CON_RESERVAS"):
            self.assertIn(token, playbook)
            self.assertIn(token, template)
        for section in range(1, 38):
            self.assertRegex(template, rf"(?m)^# {section}\.", msg=f"falta sección mínima {section}")
        candidate = ROOT / "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite"
        self.assertEqual(module.validar_precondiciones(candidate), [])
        verdict = (candidate / "veredicto-final-carta.md").read_text(encoding="utf-8")
        self.assertIn("resultado_final: APTA", verdict)
        self.assertIn("estado_gate_salida: aprobado", verdict)
        self.assertIn("decision_humana: aprobado", verdict)


if __name__ == "__main__":
    unittest.main()
