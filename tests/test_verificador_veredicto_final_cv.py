import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "job-up" / "verificar_veredicto_final_cv.py"


def load_module():
    spec = importlib.util.spec_from_file_location("verificador_veredicto_final_cv", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class VerificadorVeredictoFinalCVTests(unittest.TestCase):
    def test_calcula_huella_y_valida_revision_humana_de_la_misma_version(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pdf = root / "cv.pdf"
            pdf.write_bytes(b"pdf-v1")
            hash_value = module.calcular_huella(pdf)
            revision = root / "revision-humana-cv.md"
            revision.write_text(
                f"""---\nrevision_humana_cv:\n  decision: aprobado_para_veredicto\n  cv_revisado: cv.pdf\n  huella_cv: {hash_value}\n  fecha: 2026-08-08\n  decidido_por: persona_responsable\n---\n""",
                encoding="utf-8",
            )
            data = module.validar_revision_humana(revision, pdf)
            self.assertEqual(data["huella_cv"], hash_value)

    def test_bloquea_revision_de_otra_version_sin_huella_o_con_correccion(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pdf = root / "cv.pdf"
            pdf.write_bytes(b"pdf-v2")
            revision = root / "revision-humana-cv.md"
            revision.write_text(
                """---\nrevision_humana_cv:\n  decision: requiere_correccion\n  cv_revisado: cv.pdf\n  huella_cv: hash-v1\n  fecha: 2026-08-08\n  decidido_por: persona_responsable\n---\n""",
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                module.validar_revision_humana(revision, pdf)

    def test_aplica_precedencia_y_distingue_resultados(self):
        module = load_module()
        self.assertEqual(module.resultado_global("no_apta", "apta", [5] * 6), "bloqueado_por_integridad")
        self.assertEqual(module.resultado_global("apta", "no_apta", [5] * 6), "requiere_correccion_de_flujo")
        self.assertEqual(module.resultado_global("apta", "apta", [4] * 6, no_competitivo=True), "no_competitivo")
        self.assertEqual(module.resultado_global("apta", "apta", [3, 4, 4, 4, 4, 3], corregible=True), "revisar_antes_de_presentar")
        self.assertEqual(module.resultado_global("apta", "apta", [4] * 6), "apto_para_presentacion")

    def test_casos_negativos_de_privacidad_y_composicion_quedan_enroutados(self):
        module = load_module()
        self.assertEqual(
            module.resultado_global("no_apta", "apta", [4] * 6),
            "bloqueado_por_integridad",
            "un dato privado no autorizado es una incidencia de integridad",
        )
        self.assertEqual(
            module.resultado_global("apta", "no_apta", [4] * 6),
            "requiere_correccion_de_flujo",
            "la desaparición o modificación semántica en composición rompe la fidelidad",
        )

    def test_precondiciones_reconocen_fuentes_y_aceptan_revision_aprobada(self):
        module = load_module()
        for candidate_name in (
            "CAND-2026-019-asic-consultores-responsable-automatizacion-ia",
            "CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite",
        ):
            candidate = ROOT / "boveda-entrevista-profesional" / "busqueda-empleo" / "candidaturas" / candidate_name
            blockers = module.validar_precondiciones(candidate)
            self.assertEqual(blockers, [])


if __name__ == "__main__":
    unittest.main()
