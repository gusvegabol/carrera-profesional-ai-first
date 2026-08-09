"""Pruebas de contrato para la implantación de PLAYBOOK_GUION_ADAPTACION_CV."""

from pathlib import Path
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "docs" / "ideas-y-debates" / "mejoras-job-up" / (
    "SPEC-Arquitectura-modular-generación-candidatura-v0-4-0.md"
)
TEMPLATE = ROOT / "docs" / "ideas-y-debates" / "mejoras-job-up" / (
    "TEMPLATE_GUION_ADAPTACION_CV_v2.md"
)
PLAYBOOK = ROOT / "docs" / "ideas-y-debates" / "mejoras-job-up" / (
    "PLAYBOOK_GUION_ADAPTACION_CV.md"
)
LIDL_DIR = (
    ROOT
    / "boveda-entrevista-profesional"
    / "busqueda-empleo"
    / "candidaturas"
    / "CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite"
)
LIDL_GUIDE = LIDL_DIR / "guion-adaptacion-cv.md"
LIDL_EVALUATION = LIDL_DIR / "evaluacion-gate-guion-cv-contenido.md"
LIDL_CANDIDATURE = LIDL_DIR / "candidatura.md"
ASIC_DIR = (
    ROOT
    / "boveda-entrevista-profesional"
    / "busqueda-empleo"
    / "candidaturas"
    / "CAND-2026-019-asic-consultores-responsable-automatizacion-ia"
)
ASIC_CANDIDATURE = ASIC_DIR / "candidatura.md"
ASIC_ENTRY_EVALUATION = ASIC_DIR / "evaluacion-gate-candidatura-guion.md"
ASIC_GUIDE = ASIC_DIR / "guion-adaptacion-cv.md"
ASIC_OUTPUT_EVALUATION = ASIC_DIR / "evaluacion-gate-guion-cv-contenido.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class SpecContractTests(unittest.TestCase):
    def test_spec_declares_cv_only_guion_and_preserves_open_defect(self) -> None:
        spec = read(SPEC)

        self.assertIn("ARQ-22 — Separación de responsabilidades CV/carta", spec)
        self.assertIn("GATE-GUION-CV-CONTENIDO", spec)
        self.assertIn("DEF-ARQ-001", spec)
        self.assertIn("**Estado:** abierto.", spec)
        self.assertIn("futura generación de contenido del CV", spec)
        self.assertIn("ID: INC-001", spec)
        self.assertIn("ID: INC-002", spec)
        self.assertIn("ID: INC-003", spec)
        self.assertIn("`PLAYBOOK_GUION_ADAPTACION_CV` | `en_prueba`", spec)
        self.assertIn("Rama de carta de presentación: pendiente de diseño", spec)


class TemplateAndPlaybookTests(unittest.TestCase):
    def test_template_v21_declares_idioma_and_its_explicit_authority(self) -> None:
        """Evita que la plantilla física retroceda al contrato 2.0."""
        template = read(TEMPLATE)
        frontmatter = template.split("---", 2)[1]
        metadata = yaml.safe_load(frontmatter)

        self.assertEqual("1.0.1", str(metadata["version_playbook"]))
        self.assertEqual("2.1", str(metadata["version_template"]))
        self.assertIn("idioma_cv:", frontmatter)
        self.assertIn(
            "| Autoridad usada para determinar idioma |",
            template,
        )
        self.assertIn("* **Idioma del CV:** [CODIGO_IDIOMA].", template)
        self.assertIn("* [ ] `idioma_cv` está determinado y posee autoridad explícita.", template)
        self.assertIn("## 9. Brief cerrado para la futura generación de contenido del CV", template)
        brief = template.split("## 9. Brief cerrado para la futura generación de contenido del CV", 1)[1]
        self.assertIn("* **Idioma del CV:** [CODIGO_IDIOMA].", brief)

    def test_template_has_required_frontmatter_and_editorial_map(self) -> None:
        template = read(TEMPLATE)
        frontmatter = template.split("---", 2)[1]
        metadata = yaml.safe_load(frontmatter)

        for key in (
            "version_diseno:",
            "fuentes_factuales:",
            "gate_salida: GATE-GUION-CV-CONTENIDO",
        ):
            self.assertIn(key, template)

        self.assertNotIn("estado_gate_salida:", template)
        self.assertIsInstance(metadata["id"], str)
        self.assertIsInstance(metadata["candidatura"], str)
        for value in (
            "incluir",
            "omitir",
            "obligatoria",
            "opcional",
            "alto",
            "medio",
            "bajo",
            "minimo",
        ):
            self.assertIn(value, template)

        for field in (
            "M-NNN",
            "criterio_objetivo",
            "funcion_estrategica",
            "seccion_destino",
            "orden_en_seccion",
            "nivel_detalle",
            "limitaciones_redaccion",
            "defecto_relacionado",
        ):
            self.assertIn(field, template)

        self.assertIn("defecto_relacionado: DEF-ARQ-001", template)

    def test_playbook_declares_cv_only_execution_and_full_regeneration(self) -> None:
        playbook = read(PLAYBOOK)

        self.assertIn("17 pasos", playbook)
        self.assertIn("regeneración completa", playbook)
        self.assertIn("No:\n\n* produce el CV;", playbook)
        self.assertIn("* redacta la carta;", playbook)
        self.assertIn("evaluacion-gate-guion-cv-contenido.md", playbook)
        self.assertIn("DEF-ARQ-001", playbook)
        self.assertIn("estado: abierto", playbook)
        self.assertIn("contradicción entre autoridades", playbook)
        self.assertIn("requiere_revision_origen", playbook)
        self.assertIn("defecto_relacionado: DEF-ARQ-001", playbook)
        self.assertIn("todas las incidencias", playbook)
        self.assertIn("prevalece", playbook)

        self.assertNotIn("generación común CV/carta", playbook)
        self.assertNotIn("cierra `DEF-ARQ-001`", playbook)
        self.assertNotIn("contradicción entre autoridades | `bloqueado`", playbook)


class CandidateGuideTests(unittest.TestCase):
    def test_lidl_guion_preserves_limits_and_covers_strategy(self) -> None:
        guide = read(LIDL_GUIDE)
        evaluation = read(LIDL_EVALUATION)
        metadata = yaml.safe_load(guide.split("---", 2)[1])

        for evidence in ("HER-03", "HER-07", "HER-04", "HER-08", "HER-10"):
            self.assertIn(evidence, guide)
        self.assertEqual("1.0.1", str(metadata["version_playbook"]))
        self.assertEqual("2.1", str(metadata["version_template"]))
        self.assertEqual("es", metadata["idioma_cv"])
        self.assertIn("IDIOMA_INEQUIVOCO_OFERTA", guide)
        self.assertIn("FP de Técnico Administrativo", guide)
        self.assertIn("tesorería", guide)
        self.assertIn("no afirmar", guide)
        self.assertIn("compras centralizadas", guide)
        for field in (
            "| Motivo |",
            "| Limitaciones de redacción |",
            "| Defecto relacionado |",
            "### 2.1 Seniority",
            "Gancho heredado",
            "Objetivo del CV",
            "Percepción a provocar",
            "Percepción a evitar",
            "Justificación factual y estratégica",
        ):
            self.assertIn(field, guide)
        for criterion in (
            "presencia separada de obligatoriedad",
            "ausencia de keyword stuffing",
            "incidencias factuales nuevas relacionadas con `DEF-ARQ-001`",
            "siguiente fase capaz de operar sin reconstruir estrategia",
        ):
            self.assertIn(criterion, evaluation)
        self.assertIn("decision_humana: aprobado", evaluation)
        self.assertIn("estado_gate: aprobado", evaluation)
        self.assertIn("fecha_decision_humana: 2026-08-07", evaluation)
        self.assertIn("no se reutilizó", evaluation)

    def test_lidl_evaluation_covers_every_design_acceptance_criterion(self) -> None:
        evaluation = read(LIDL_EVALUATION)
        acceptance_criteria = (
            "gate de entrada aprobado",
            "ausencia de bloqueo",
            "posicionamiento heredado intacto",
            "instrucción editorial clara",
            "seniority tratado explícitamente",
            "tono editorial explícito y respaldado",
            "universo candidato razonable",
            "mapa de edición completo",
            "presencia separada de obligatoriedad",
            "obligatoriedad separada de peso",
            "campos no aplicables marcados como `no_aplica`",
            "contenido principal vinculado a criterios objetivos",
            "experiencias y logros prioritarios identificados",
            "prioridades estratégicas con cobertura controlada",
            "selección trazable",
            "omisiones materiales justificadas",
            "ninguna omisión induce a error",
            "cronología comprensible",
            "exclusiones protegidas",
            "léxico respaldado",
            "ausencia de keyword stuffing",
            "duplicación injustificada controlada",
            "ausencia de hechos nuevos incorporados sin propagación",
            "incidencias factuales nuevas relacionadas con `DEF-ARQ-001`",
            "previsión de primer escaneo competitiva",
            "brief coherente",
            "ausencia de redacción final del CV",
            "ausencia de diseño de carta",
            "siguiente fase capaz de operar sin reconstruir estrategia",
        )

        self.assertEqual(29, len(acceptance_criteria))
        for criterion in acceptance_criteria:
            with self.subTest(criterion=criterion):
                self.assertIn(criterion, evaluation)


class CandidateContrastTests(unittest.TestCase):
    def test_full_contract_has_two_cases_and_no_out_of_scope_generation(self) -> None:
        spec = read(SPEC)

        for candidate in (LIDL_DIR, ASIC_DIR):
            self.assertTrue((candidate / "guion-adaptacion-cv.md").is_file())
            self.assertTrue(
                (candidate / "evaluacion-gate-guion-cv-contenido.md").is_file()
            )
            self.assertTrue((candidate / "datos-generacion.json").is_file())
            self.assertTrue(
                (candidate / "evaluacion-gate-contenido-cv-composicion.md").is_file()
            )
        self.assertIn("candidata a validada", spec)
        self.assertIn("decision_humana: aprobado", read(LIDL_EVALUATION))
        self.assertIn("estado_gate: aprobado", read(LIDL_EVALUATION))
        self.assertIn("decision_humana: aprobado", read(ASIC_OUTPUT_EVALUATION))
        self.assertIn("estado_gate: aprobado", read(ASIC_OUTPUT_EVALUATION))
        self.assertIn("fecha_decision_humana: 2026-08-07", read(LIDL_EVALUATION))
        self.assertIn("fecha_decision_humana: 2026-08-07", read(ASIC_OUTPUT_EVALUATION))
        self.assertIn("| Evaluación GATE-GUION-CV-CONTENIDO | aprobado |", read(LIDL_CANDIDATURE))
        self.assertIn("| Evaluación GATE-GUION-CV-CONTENIDO | aprobado |", read(ASIC_CANDIDATURE))
        self.assertIn(
            "| Evaluación GATE-CONTENIDO-CV-COMPOSICION | aprobado |",
            read(LIDL_CANDIDATURE),
        )
        self.assertIn(
            "| Evaluación GATE-CONTENIDO-CV-COMPOSICION | aprobado |",
            read(ASIC_CANDIDATURE),
        )
        self.assertNotIn("carta-presentacion", read(LIDL_GUIDE))
        self.assertNotIn("carta-presentacion", read(ASIC_GUIDE))

    def test_asic_has_human_approved_entry_gate_and_cv_only_guide(self) -> None:
        candidature = read(ASIC_CANDIDATURE)
        evaluation = read(ASIC_ENTRY_EVALUATION)
        guide = read(ASIC_GUIDE)
        output_evaluation = read(ASIC_OUTPUT_EVALUATION)

        self.assertIn("gate: GATE-CANDIDATURA-GUION", evaluation)
        self.assertIn("recomendacion_ia: aprobar", evaluation)
        self.assertIn("decision_humana: aprobado", evaluation)
        self.assertIn("estado_gate: aprobado", evaluation)
        self.assertIn("artefactos históricos del flujo anterior", candidature)
        self.assertIn("primer año de los tres", candidature)
        self.assertIn("completado_gate_salida_aprobado", candidature)

        for evidence in ("HER-01", "HER-03", "HER-07", "HER-08", "GSC-01"):
            self.assertIn(evidence, guide)
        metadata = yaml.safe_load(guide.split("---", 2)[1])
        self.assertEqual("1.0.1", str(metadata["version_playbook"]))
        self.assertEqual("2.1", str(metadata["version_template"]))
        self.assertEqual("es", metadata["idioma_cv"])
        self.assertIn("IDIOMA_INEQUIVOCO_OFERTA", guide)
        m008_row = next(line for line in guide.splitlines() if "M-008" in line)
        self.assertIn("GSC-01", m008_row)
        self.assertIn("SEC-04", m008_row)
        self.assertNotIn("SEC-02", m008_row)
        self.assertIn("exclusivo del CV", guide)
        self.assertIn("Power Automate", guide)
        self.assertIn("primer curso de tres", guide)
        self.assertIn("decision_humana: aprobado", output_evaluation)
        self.assertIn("estado_gate: aprobado", output_evaluation)
        self.assertIn("fecha_decision_humana: 2026-08-07", output_evaluation)
        self.assertIn("no se reutilizó", output_evaluation)

    def test_asic_output_evaluation_covers_every_design_acceptance_criterion(self) -> None:
        evaluation = read(ASIC_OUTPUT_EVALUATION)
        acceptance_criteria = (
            "gate de entrada aprobado",
            "ausencia de bloqueo",
            "posicionamiento heredado intacto",
            "instrucción editorial clara",
            "seniority tratado explícitamente",
            "tono editorial explícito y respaldado",
            "universo candidato razonable",
            "mapa de edición completo",
            "presencia separada de obligatoriedad",
            "obligatoriedad separada de peso",
            "campos no aplicables marcados como `no_aplica`",
            "contenido principal vinculado a criterios objetivos",
            "experiencias y logros prioritarios identificados",
            "prioridades estratégicas con cobertura controlada",
            "selección trazable",
            "omisiones materiales justificadas",
            "ninguna omisión induce a error",
            "cronología comprensible",
            "exclusiones protegidas",
            "léxico respaldado",
            "ausencia de keyword stuffing",
            "duplicación injustificada controlada",
            "ausencia de hechos nuevos incorporados sin propagación",
            "incidencias factuales nuevas relacionadas con `DEF-ARQ-001`",
            "previsión de primer escaneo competitiva",
            "brief coherente",
            "ausencia de redacción final del CV",
            "ausencia de diseño de carta",
            "siguiente fase capaz de operar sin reconstruir estrategia",
        )

        self.assertEqual(29, len(acceptance_criteria))
        for criterion in acceptance_criteria:
            with self.subTest(criterion=criterion):
                self.assertIn(criterion, evaluation)


if __name__ == "__main__":
    unittest.main()
