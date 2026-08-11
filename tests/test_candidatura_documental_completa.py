import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANDIDATE = ROOT / "boveda-entrevista-profesional" / "busqueda-empleo" / "candidaturas" / "CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite"
PLAYBOOKS = ROOT / "docs" / "metodologia" / "playbooks"
TEMPLATES = ROOT / "boveda-entrevista-profesional" / "busqueda-empleo" / "proceso" / "plantillas"
IDEAS = ROOT / "docs" / "ideas-y-debates" / "mejoras-job-up"


def documentalmente_completa(texto: str, carpeta: Path) -> bool:
    """Predicado de contrato usado por estas pruebas, sin añadir runtime."""
    if "estado: documentalmente_completa" not in texto:
        return False
    if "presentada: false" not in texto:
        return False
    if "gate_candidatura_presentacion: no_aplica_en_esta_fase" not in texto:
        return False
    if not (carpeta / "cv.pdf").exists():
        return False
    if "carta_requerida: true" in texto and not (carpeta / "carta-presentacion.pdf").exists():
        return False
    return True


class CandidaturaDocumentalCompletaTests(unittest.TestCase):
    def test_cand_020_es_documentalmente_completa_y_no_presentada(self):
        ficha = (CANDIDATE / "candidatura.md").read_text(encoding="utf-8")
        self.assertTrue(documentalmente_completa(ficha, CANDIDATE))

    def test_falta_carta_requerida_no_permite_cierre(self):
        texto = (
            "estado: documentalmente_completa\n"
            "presentada: false\n"
            "gate_candidatura_presentacion: no_aplica_en_esta_fase\n"
            "carta_requerida: true\n"
        )
        self.assertFalse(documentalmente_completa(texto, CANDIDATE / "no-existe"))

    def test_carta_no_requerida_no_crea_dependencia_de_presentacion(self):
        texto = (
            "estado: documentalmente_completa\n"
            "presentada: false\n"
            "gate_candidatura_presentacion: no_aplica_en_esta_fase\n"
            "carta_requerida: false\n"
        )
        self.assertTrue(documentalmente_completa(texto, CANDIDATE))

    def test_rutas_canonicas_y_futuras_estan_separadas(self):
        self.assertTrue((PLAYBOOKS / "PLAYBOOK_COMPONER_CV.md").exists())
        self.assertTrue((TEMPLATES / "TEMPLATE_DATOS_GENERACION_CV.json").exists())
        self.assertTrue((IDEAS / "futuro" / "presentacion").is_dir())
        self.assertFalse((IDEAS / "PLAYBOOK_COMPONER_CV.md").exists())

    def test_no_hay_paquete_activo_en_cand_020(self):
        self.assertFalse((CANDIDATE / "paquete-presentacion.md").exists())
        self.assertFalse((CANDIDATE / "evaluacion-presentacion-candidatura.md").exists())


if __name__ == "__main__":
    unittest.main()
