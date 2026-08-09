import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "job-up" / "verificar_paquete_presentacion.py"


def load_module():
    spec = importlib.util.spec_from_file_location("verificador_paquete_presentacion", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class VerificadorPaquetePresentacionTests(unittest.TestCase):
    def test_lidl_queda_bloqueado_mientras_falten_canal_y_artefactos(self):
        module = load_module()
        candidate = ROOT / "boveda-entrevista-profesional" / "busqueda-empleo" / "candidaturas" / "CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite"
        blockers = module.validar_paquete(candidate / "paquete-presentacion.md", candidate)
        self.assertIn("canal_envio_no_confirmado", blockers)
        self.assertIn("artefactos_presentacion_pendientes", blockers)
        self.assertNotIn("presentada_debe_ser_false", blockers)

    def test_no_permite_transicion_a_presentada_sin_evidencia_completa(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory) / "paquete-presentacion.md"
            package.write_text("presentada: false\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                module.validar_transicion_presentada(package, {"canal": "Indeed"})

    def test_acepta_evidencia_minima_de_envio_real(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory) / "paquete-presentacion.md"
            package.write_text("presentada: false\n", encoding="utf-8")
            evidence = {
                "canal": "Indeed",
                "fecha_hora": "2026-08-09T12:00:00+01:00",
                "ejecutado_por": "persona_responsable",
                "confirmacion": "confirmacion-indeed-001",
            }
            self.assertIsNone(module.validar_transicion_presentada(package, evidence))


if __name__ == "__main__":
    unittest.main()
