import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts/job-up/generar_candidatura.py"
SOURCE_JSON = ROOT / "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/datos-generacion.json"
TEMPLATE = ROOT / "boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_CV_FORMATO.docx"
PHOTO = ROOT / "boveda-entrevista-profesional/busqueda-empleo/foto-perfil.png"


def load_module():
    spec = importlib.util.spec_from_file_location("generar_candidatura_cv12", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class GeneradorCV12Tests(unittest.TestCase):
    def test_valida_autorizacion_y_rechaza_contacto_no_autorizado(self):
        module = load_module()
        payload = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
        payload["control"]["datos_privados"] = {
            "autorizacion": {
                "nombre": "incluir",
                "apellido_1": "incluir",
                "apellido_2": "omitir",
                "email": "incluir",
                "telefono": "incluir",
                "linkedin": "omitir",
                "ubicacion": "omitir",
                "fotografia": "incluir",
            },
            "fecha_decision": "2026-08-08",
            "decidido_por": "persona_responsable",
        }
        payload["contenido_cv"]["encabezado"]["contacto"].append(
            {"tipo": "linkedin", "texto": "www.linkedin.com/in/gusvegabol"}
        )
        with self.assertRaises(ValueError):
            module.validate_composition_payload(payload)

    def test_cli_publica_solo_tres_artefactos_desde_contrato_1_2(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            candidate = project / "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-prueba"
            template_dir = project / "boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas"
            candidate.mkdir(parents=True)
            template_dir.mkdir(parents=True)
            shutil.copy2(SOURCE_JSON, candidate / "datos-generacion.json")
            shutil.copy2(TEMPLATE, template_dir / "TEMPLATE_CV_FORMATO.docx")
            photo = project / "boveda-entrevista-profesional/busqueda-empleo/foto-perfil.png"
            photo.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(PHOTO, photo)

            def fake_convert(docx, out_dir, *_args, **_kwargs):
                output = out_dir / "cv.pdf"
                output.write_bytes(b"%PDF-1.4\n%%EOF")
                return output

            with patch.object(module, "_load_env", return_value={"RUTA_PROYECTO": str(project), "SOFFICE_PATH": str(project / "soffice.com")}), \
                 patch.object(module, "convert_docx_to_pdf", side_effect=fake_convert), \
                 patch.object(module, "validate_pdf", return_value=None), \
                 patch.object(module, "validate_published_artifacts", return_value=None):
                result = module.main([str(candidate / "datos-generacion.json")])

            self.assertEqual(result, 0)
            self.assertEqual({path.name for path in candidate.iterdir() if path.suffix in {".docx", ".pdf", ".tex"}}, {"cv.docx", "cv.pdf", "cv.tex"})
            self.assertFalse((candidate / "carta-presentacion.docx").exists())
            self.assertFalse((candidate / "carta-presentacion.pdf").exists())
            manifest = json.loads((candidate / "manifest-generacion-cv.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["artefactos"], ["cv_docx", "cv_pdf", "cv_tex"])
            self.assertEqual(manifest["fotografia"], "incluida")


if __name__ == "__main__":
    unittest.main()
