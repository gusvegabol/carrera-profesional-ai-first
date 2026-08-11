import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUTURE = ROOT / "docs/ideas-y-debates/mejoras-job-up/futuro/presentacion"
PLAYBOOK = FUTURE / "PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA.md"
TEMPLATE = FUTURE / "TEMPLATE_EVALUACION_PRESENTACION_CANDIDATURA.md"


class ValidarPresentacionCandidaturaTests(unittest.TestCase):
    def test_playbook_define_contrato_y_frontera(self):
        texto = PLAYBOOK.read_text(encoding="utf-8")
        for token in (
            "id: PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA",
            'version: "1.0.0"',
            "estado: en_prueba",
            "entrada_principal: paquete-presentacion.md",
            "artefacto_salida: evaluacion-presentacion-candidatura.md",
            "gate_entrada: GATE-CANDIDATURA-PRESENTACION",
            "gate_salida: GATE-CANDIDATURA-PRESENTACION",
            "paquete listo",
            "gate abierto",
            "orden humana de presentación",
            "envío efectivo",
            "GATE-CANDIDATURA-PRESENTACION = aprobado",
            "presentada = true",
        ):
            self.assertIn(token, texto)

    def test_playbook_cubre_seis_dimensiones_resultados_y_casos(self):
        texto = PLAYBOOK.read_text(encoding="utf-8")
        for dimension in ("D1", "D2", "D3", "D4", "D5", "D6"):
            self.assertIn(dimension, texto)
        for resultado in ("APTA_PARA_PRESENTACION", "APTA_CON_PENDIENTES_HUMANOS", "BLOQUEADA"):
            self.assertIn(resultado, texto)
        for caso in range(1, 13):
            self.assertIn(f"T{caso:02d}", texto)

    def test_template_es_auditable_y_prohibe_presentacion(self):
        texto = TEMPLATE.read_text(encoding="utf-8")
        for seccion in (
            "Identificación",
            "Precondiciones",
            "Canal",
            "Integridad documental",
            "Identidad",
            "Versiones",
            "Compatibilidad con canal",
            "Campos del formulario",
            "Preguntas adicionales",
            "Respuestas preparables",
            "Pendientes humanos",
            "Bloqueantes",
            "Preparación operativa",
            "Resultado",
            "Estado del gate",
            "Control de no presentación",
            "Siguiente acción",
        ):
            self.assertIn(seccion, texto)
        for token in (
            "se_pulso_enviar: false",
            "se_confirmo_candidatura: false",
            "se_envio_email: false",
            "se_realizo_accion_irreversible: false",
            "presentada: false",
            "requiere_decision_humana",
        ):
            self.assertIn(token, texto)

    def test_caso_real_cand_2026_020_queda_fuera_del_flujo_activo(self):
        candidate = ROOT / "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite"
        candidatura = (candidate / "candidatura.md").read_text(encoding="utf-8")
        historical = ROOT / "historico/boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/paquete-presentacion.md"
        candidate_history = ROOT / "historico/boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite"
        self.assertIn("estado: documentalmente_completa", candidatura)
        self.assertIn("gate_candidatura_presentacion: no_aplica_en_esta_fase", candidatura)
        self.assertIn("presentada: false", candidatura)
        self.assertTrue(historical.exists())
        self.assertTrue((candidate_history / "evaluacion-presentacion-candidatura.md").exists())
        self.assertTrue((candidate_history / "paquete-presentacion.md").exists())


if __name__ == "__main__":
    unittest.main()
