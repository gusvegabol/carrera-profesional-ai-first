import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".codex" / "skills" / "job-up-candidatura-oferta" / "SKILL.md"
PLAYBOOK_ROOT = ROOT / "docs" / "metodologia" / "playbooks"
TEMPLATE_ROOT = ROOT / "boveda-entrevista-profesional" / "busqueda-empleo" / "proceso" / "plantillas"

EXPECTED_PLAYBOOKS = (
    "PLAYBOOK_CANDIDATURA_POR_OFERTA.md",
    "PLAYBOOK_GUION_ADAPTACION_CV.md",
    "PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA.md",
    "PLAYBOOK_COMPONER_CV.md",
    "PLAYBOOK_VEREDICTO_FINAL_CV.md",
    "PLAYBOOK_GUION_CARTA_PRESENTACION.md",
    "PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION.md",
    "PLAYBOOK_COMPONER_CARTA_PRESENTACION.md",
    "PLAYBOOK_VEREDICTO_FINAL_CARTA.md",
)

EXPECTED_TEMPLATES = (
    "TEMPLATE_ANALISIS_OFERTA.md",
    "TEMPLATE_CANDIDATURA.md",
    "TEMPLATE_GUION_ADAPTACION_CV.md",
    "TEMPLATE_DATOS_GENERACION_CV.json",
    "TEMPLATE_GUION_CARTA_PRESENTACION.md",
    "TEMPLATE_CONTENIDO_CARTA_PRESENTACION.md",
    "TEMPLATE_COMPOSICION_CARTA_PRESENTACION.md",
    "TEMPLATE_VEREDICTO_FINAL_CV.md",
    "TEMPLATE_VEREDICTO_FINAL_CARTA.md",
)


class JobUpCandidaturaOfertaSkillTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = SKILL.read_text(encoding="utf-8")

    def test_t_skill_01_no_usa_contrato_conjunto_historico(self):
        self.assertNotIn("TEMPLATE_DATOS_GENERACION_CANDIDATURA.json", self.skill)

    def test_t_skill_02_declara_contrato_cv_12(self):
        self.assertIn("TEMPLATE_DATOS_GENERACION_CV.json", self.skill)
        self.assertIn("1.2", self.skill)

    def test_t_skill_03_separa_fotografia_de_carta(self):
        self.assertIn("carta", self.skill.lower())
        self.assertIn("no se incluye por defecto", self.skill.lower())
        self.assertNotIn("fotografía autorizada por defecto en CV y carta", self.skill.lower())

    def test_t_skill_04_no_orquesta_generacion_conjunta(self):
        self.assertIn("rama CV", self.skill)
        self.assertIn("rama carta", self.skill)
        self.assertNotIn("generación conjunta", self.skill.lower())

    def test_t_skill_05_declara_cierre_documental(self):
        self.assertIn("documentalmente_completa", self.skill)
        self.assertIn("presentada: false", self.skill)

    def test_t_skill_06_excluye_presentacion_externa(self):
        self.assertIn("presentación externa queda fuera", self.skill.lower())
        self.assertNotIn("GATE-CANDIDATURA-PRESENTACION", self.skill)

    def test_t_skill_07_referencias_canonicas_existen(self):
        for playbook in EXPECTED_PLAYBOOKS:
            self.assertIn(playbook, self.skill)
            self.assertTrue((PLAYBOOK_ROOT / playbook).is_file())
        for template in EXPECTED_TEMPLATES:
            self.assertTrue((TEMPLATE_ROOT / template).exists())

    def test_t_skill_08_orquestador_de_transiciones_esta_declarado(self):
        self.assertIn("scripts/job-up/orquestar_transiciones.py", self.skill)
        self.assertTrue((ROOT / "scripts/job-up/orquestar_transiciones.py").is_file())


if __name__ == "__main__":
    unittest.main()
