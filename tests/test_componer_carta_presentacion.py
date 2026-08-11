import tempfile
import unittest
import hashlib
import json
import shutil
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts/job-up"))
import componer_carta_presentacion as compositor
import cabecera_candidatura as cabecera


BASE = """---
id: contenido-carta-presentacion-CAND-TEST
estado_contenido: apto
estado_gate_salida: aprobado
---

## 16. Carta completa consolidada

Estimado equipo de selección:

Experiencia operativa con una métrica del 30 % y otra del 80 %.

Atentamente,

Gustavo Vega
gusvegabol@gmail.com
669 549 933

## 17. Control final
"""


class ComposeCartaTests(unittest.TestCase):
    def test_extracts_only_consolidated_section(self):
        self.assertEqual(
            compositor.extract_consolidated_letter(BASE),
            "Estimado equipo de selección:\n\nExperiencia operativa con una métrica del 30 % y otra del 80 %.\n\nAtentamente,\n\nGustavo Vega\ngusvegabol@gmail.com\n669 549 933",
        )

    def test_gate_not_approved_blocks(self):
        text = BASE.replace("estado_gate_salida: aprobado", "estado_gate_salida: pendiente")
        with self.assertRaises(compositor.PreconditionError):
            compositor.validate_preconditions(text, presented=False)

    def test_content_not_apt_blocks(self):
        text = BASE.replace("estado_contenido: apto", "estado_contenido: requiere_correccion")
        with self.assertRaises(compositor.PreconditionError):
            compositor.validate_preconditions(text, presented=False)

    def test_presented_candidate_blocks(self):
        with self.assertRaises(compositor.PreconditionError):
            compositor.validate_preconditions(BASE, presented=True)

    def test_omission_is_detected(self):
        result = compositor.compare_texts("uno\ndos", "uno")
        self.assertFalse(result.equivalent)
        self.assertTrue(result.omissions)

    def test_addition_is_detected(self):
        result = compositor.compare_texts("uno", "uno\ntres")
        self.assertFalse(result.equivalent)
        self.assertTrue(result.additions)

    def test_change_of_figure_is_detected(self):
        result = compositor.compare_texts("redujo un 30 %", "redujo un 20 %")
        self.assertFalse(result.equivalent)
        self.assertTrue(result.changes_figures)

    def test_material_order_change_is_detected(self):
        result = compositor.compare_texts("saludo\napertura\ncierre", "saludo\ncierre\napertura")
        self.assertFalse(result.equivalent)
        self.assertTrue(result.order_changed)

    def test_docx_pdf_difference_is_detected(self):
        self.assertFalse(compositor.compare_texts("uno", "dos").equivalent)

    def test_pdf_incomplete_is_detected(self):
        result = compositor.compare_texts("uno\ndos", "uno")
        self.assertIn("dos", result.omissions)

    def test_empty_page_is_reported(self):
        self.assertTrue(compositor.page_count_issue(actual_pages=2, text="uno\n\n"))

    def test_extra_personal_data_is_detected(self):
        result = compositor.compare_authorized_contacts(
            "Gustavo Vega\ngusvegabol@gmail.com\n669 549 933",
            "Gustavo Vega\ngusvegabol@gmail.com\n669 549 933\nlinkedin.com/in/extra",
        )
        self.assertIn("linkedin.com/in/extra", result)

    def test_rewrite_is_integrity_failure(self):
        result = compositor.compare_texts("Trabajo con stock.", "Gestiono inventarios.")
        self.assertFalse(result.equivalent)

    def test_long_content_is_not_summarized(self):
        result = compositor.layout_status("x " * 5000, max_pages=1, actual_pages=2)
        self.assertEqual(result, "requiere_correccion_composicion")

    def test_render_error_is_composition_correction(self):
        self.assertEqual(compositor.classify_render_error(), "requiere_correccion_composicion")

    def test_space_and_linebreak_differences_are_accepted(self):
        result = compositor.compare_texts("uno dos\ntres", "uno  dos\n\ntres")
        self.assertTrue(result.equivalent)

    def test_cabecera_canonica_se_deriva_del_json_y_privacidad(self):
        root = Path(__file__).resolve().parents[1]
        payload = json.loads((root / "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/datos-generacion.json").read_text(encoding="utf-8"))
        header = cabecera.construir_cabecera_candidatura(payload)
        self.assertEqual(header.nombre, "Gustavo Vega")
        self.assertEqual(header.titular, "Operaciones de supermercados | Pedidos, stock y mejora de procesos")
        self.assertEqual(header.contacto, ("gusvegabol@gmail.com", "669 549 933"))
        self.assertEqual(header.version, "datos-generacion-cv@1.2")

    def test_cabecera_rechaza_dato_personal_no_autorizado(self):
        root = Path(__file__).resolve().parents[1]
        payload = json.loads((root / "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/datos-generacion.json").read_text(encoding="utf-8"))
        payload["contenido_cv"]["encabezado"]["contacto"].append({"tipo": "linkedin", "orden": 3, "texto": "www.linkedin.com/in/gusvegabol"})
        with self.assertRaises(cabecera.CabeceraError):
            cabecera.construir_cabecera_candidatura(payload)

    def test_modo_texto_usa_solo_carta_consolidada_y_no_crea_txt(self):
        root = Path(__file__).resolve().parents[1]
        content = root / "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/contenido-carta-presentacion.md"
        source = compositor.extract_consolidated_letter(content.read_text(encoding="utf-8"))
        self.assertEqual(compositor.extraer_modo_texto(content), source)
        self.assertFalse((content.parent / "carta-presentacion.txt").exists())

    def test_cabecera_ausente_bloquea_composicion_documental(self):
        with self.assertRaises(compositor.PreconditionError):
            compositor.cargar_cabecera_para_candidatura(Path("C:/ruta/inexistente"))

    def test_cabecera_divergente_se_rechaza(self):
        root = Path(__file__).resolve().parents[1]
        payload = json.loads((root / "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/datos-generacion.json").read_text(encoding="utf-8"))
        header = cabecera.construir_cabecera_candidatura(payload)
        divergent = cabecera.CabeceraCandidatura(
            nombre=header.nombre, titular="Director de banca", contacto=header.contacto, origen=header.origen, version=header.version
        )
        with self.assertRaises(cabecera.CabeceraError):
            cabecera.validar_cabecera_contrato(divergent, payload["control"]["datos_privados"]["autorizacion"])

    def test_fuente_cuerpo_y_cabecera_se_comparan_por_separado(self):
        root = Path(__file__).resolve().parents[1]
        route = root / "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite"
        source = compositor.extract_consolidated_letter((route / "contenido-carta-presentacion.md").read_text(encoding="utf-8"))
        body_docx = compositor.extract_docx_body(route / "carta-presentacion.docx")
        body_pdf = compositor.extract_pdf_body(route / "carta-presentacion.pdf")
        header_docx = compositor.extract_docx_header(route / "carta-presentacion.docx")
        header_pdf = compositor.extract_pdf_header(route / "carta-presentacion.pdf")
        self.assertTrue(compositor.compare_texts(source, body_docx).equivalent)
        self.assertTrue(compositor.compare_texts(source, body_pdf).equivalent)
        self.assertEqual(header_docx, header_pdf)

    def test_fuente_semantica_inmutable_durante_composicion(self):
        root = Path(__file__).resolve().parents[1]
        content = root / "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/contenido-carta-presentacion.md"
        evaluation = content.parent / "evaluacion-composicion-carta-presentacion.md"
        evaluation_before = evaluation.read_bytes()
        before = hashlib.sha256(content.read_bytes()).hexdigest()
        try:
            compositor.compose_case(content)
        finally:
            evaluation.write_bytes(evaluation_before)
        after = hashlib.sha256(content.read_bytes()).hexdigest()
        self.assertEqual(before, after)

    def test_real_case_preconditions_are_valid(self):
        root = Path(__file__).resolve().parents[1]
        content = root / "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/contenido-carta-presentacion.md"
        candidate = root / "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/candidatura.md"
        compositor.validate_case_files(content, candidate)

    def test_real_case_outputs_are_semantically_equivalent(self):
        root = Path(__file__).resolve().parents[1]
        route = root / "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite"
        source = compositor.extract_consolidated_letter((route / "contenido-carta-presentacion.md").read_text(encoding="utf-8"))
        docx = compositor.extract_docx_text(route / "carta-presentacion.docx")
        pdf = compositor.extract_pdf_body(route / "carta-presentacion.pdf")
        self.assertTrue((route / "carta-presentacion.docx").is_file())
        self.assertTrue((route / "carta-presentacion.pdf").is_file())
        self.assertTrue(compositor.compare_texts(source, docx).equivalent)
        self.assertTrue(compositor.compare_texts(source, pdf).equivalent)
        self.assertTrue(compositor.compare_texts(docx, pdf).equivalent)
        self.assertEqual(compositor.pdf_page_count(route / "carta-presentacion.pdf"), 1)
        evaluation = (route / "evaluacion-composicion-carta-presentacion.md").read_text(encoding="utf-8")
        self.assertIn('version: "1.1.0"', evaluation)
        self.assertIn("decision_humana: aprobado", evaluation)
        self.assertIn("estado_gate: aprobado", evaluation)
        self.assertIn("reutiliza_cabecera_cv: true", evaluation)
        self.assertIn("revision_visual:", evaluation)
        self.assertIn("impacto_pdf2image: no_bloqueante", evaluation)

    def test_real_case_evaluation_keeps_candidate_identity(self):
        root = Path(__file__).resolve().parents[1]
        source_route = root / "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-021-obramat-coordinador-linea-cajas"
        with tempfile.TemporaryDirectory() as directory:
            route = Path(directory) / source_route.name
            shutil.copytree(source_route, route)
            candidate = route / "candidatura.md"
            candidate.write_text(
                candidate.read_text(encoding="utf-8").replace("presentada: true", "presentada: false"),
                encoding="utf-8",
            )
            content = route / "contenido-carta-presentacion.md"
            compositor.compose_case(content)
            evaluation = (route / "evaluacion-composicion-carta-presentacion.md").read_text(encoding="utf-8")
            self.assertIn("CAND-2026-021", evaluation)
            self.assertNotIn("CAND-2026-020", evaluation)
            self.assertIn("datos_autorizados: [Gustavo Vega, gusvegabol@gmail.com, 669 549 933, linkedin.com/in/gusvegabol]", evaluation)
            document_xml = (route / "carta-presentacion.docx").read_bytes()
            self.assertNotIn(b"<w:br", document_xml)
            document = compositor.Document(route / "carta-presentacion.docx")
            narrative = [paragraph for paragraph in document.paragraphs if "Me gustaría poner" in paragraph.text]
            self.assertEqual(len(narrative), 1)
            self.assertEqual(narrative[0].alignment, compositor.WD_ALIGN_PARAGRAPH.JUSTIFY)

    def test_hard_wrapped_body_joins_lines_without_manual_breaks(self):
        header = cabecera.CabeceraCandidatura(
            nombre="Gustavo Vega",
            titular="Coordinación de cajas y operaciones de tienda",
            contacto=("gusvegabol@gmail.com", "669 549 933"),
            origen="test",
            version="datos-generacion-cv@1.2",
        )
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory) / "carta-presentacion.docx"
            compositor.build_docx(
                "Estimado equipo de selección:\n\nPrimera línea física\nsegunda línea física\ntercera línea física\n\nAtentamente,\n\nGustavo Vega",
                header,
                destination,
                document_date="11 de agosto de 2026",
                subject="Candidatura — Coordinador/a de línea de Cajas — OBRAMAT",
            )
            document = compositor.Document(destination)
            body_text = "\n".join(paragraph.text for paragraph in document.paragraphs)
            self.assertIn("Primera línea física segunda línea física tercera línea física", body_text)
            xml = destination.read_bytes()
            self.assertNotIn(b"<w:br", xml)

    def test_pdf_metadata_extraction_ignores_wrapped_subject(self):
        lines = [
            "11 de agosto de 2026",
            "Asunto: Candidatura — Auxiliar administrativo/a SIN EXPERIENCIA — ESTUDIO SANTA LUCIA DE TIRAJANA,",
            "S. L. / Tecnocasa Gáldar",
            "Estimado equipo de selección:",
            "Presento mi candidatura.",
        ]
        self.assertEqual(
            compositor._strip_document_metadata(lines),
            ["Estimado equipo de selección:", "Presento mi candidatura."],
        )


if __name__ == "__main__":
    unittest.main()
