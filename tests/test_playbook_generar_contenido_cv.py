"""Pruebas de contrato para la generación exclusiva de contenido del CV."""

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
DIRECTORIO = ROOT / "docs" / "ideas-y-debates" / "mejoras-job-up"
PLAYBOOK = DIRECTORIO / "PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA.md"
TEMPLATE = DIRECTORIO / "TEMPLATE_DATOS_GENERACION_CV_v1_FINAL.json"
TRAZABILIDAD = {"modo", "refs_guion", "ref_seccion_guion", "origen_factual"}
CONTROL = {
    "datos_privados",
    "cobertura_mapa",
    "cobertura_estrategica",
    "cobertura_continuidad",
    "restricciones",
    "lexico",
    "primer_escaneo",
    "validaciones",
    "incidencias",
}
VALIDACIONES = {
    "idioma_respetado",
    "solo_cv",
    "sin_placeholders",
    "fidelidad_guion",
    "cobertura_incluir_completa",
    "cobertura_estrategica_completa",
    "sin_contenido_omitido",
    "obligatorios_presentes",
    "peso_alto_respetado",
    "ubicacion_y_orden_respetados",
    "continuidad_limitada_a_lo_autorizado",
    "seniority_respetado",
    "tono_respetado",
    "convencion_gramatical_respetada",
    "restricciones_respetadas",
    "lexico_respetado",
    "sin_keyword_stuffing",
    "duplicacion_controlada",
    "trazabilidad_completa",
    "primer_escaneo_textual_apto",
    "sin_decisiones_de_composicion",
}
PRIMER_ESCANEO = {
    "resultado",
    "perfil_identificable",
    "encaje_visible",
    "senales_fuertes_visibles",
    "refs_contenido_dominantes",
}


def leer(ruta: Path) -> str:
    return ruta.read_text(encoding="utf-8")


class ContratoContenidoCVTests(unittest.TestCase):
    def setUp(self) -> None:
        self.playbook = leer(PLAYBOOK)
        self.template = json.loads(leer(TEMPLATE))

    def test_declara_la_plantilla_final_y_las_versiones_1_2(self) -> None:
        self.assertIn("TEMPLATE_DATOS_GENERACION_CV_v1_FINAL.json", self.playbook)
        self.assertIn("schema_version: 1.2", self.playbook)
        self.assertIn("template_version: 1.2", self.playbook)
        self.assertEqual("datos-generacion-cv", self.template["schema_id"])
        self.assertEqual("1.2", self.template["schema_version"])
        self.assertEqual("TEMPLATE_DATOS_GENERACION_CV_v1.json", self.template["template_id"])
        self.assertEqual("1.2", self.template["template_version"])

    def test_contrasta_trazabilidad_y_control_del_playbook_con_la_plantilla(self) -> None:
        contenido = self.template["contenido_cv"]
        seccion = contenido["secciones"][0]
        continuidad = contenido["secciones"][1]
        unidades_trazables = (
            contenido["encabezado"]["nombre_completo"],
            contenido["encabezado"]["unidades"][0],
            contenido["encabezado"]["contacto"][0],
            seccion["bloques"][0]["cabecera"][0],
            seccion["bloques"][0]["unidades"][0],
            continuidad["bloques"][0]["cabecera"][0],
            continuidad["bloques"][0]["unidades"][0],
        )

        for unidad in unidades_trazables:
            with self.subTest(unidad=unidad["id_contenido"]):
                self.assertIn("id_contenido", unidad)
                self.assertEqual(TRAZABILIDAD, set(unidad["trazabilidad"]))

        control = self.template["control"]
        self.assertEqual(CONTROL, set(control))
        self.assertEqual(VALIDACIONES, set(control["validaciones"]))
        self.assertEqual(PRIMER_ESCANEO, set(control["primer_escaneo"]))

        for campo in TRAZABILIDAD | CONTROL | VALIDACIONES | PRIMER_ESCANEO:
            with self.subTest(campo=campo):
                self.assertIn(campo, self.playbook)

    def test_prohibe_carta_y_composicion_en_datos_generacion(self) -> None:
        playbook_normalizado = " ".join(self.playbook.split())
        self.assertIn(
            "`datos-generacion.json` no puede contener datos, rutas, secciones ni "
            "decisiones de carta de presentación.",
            playbook_normalizado,
        )
        self.assertIn(
            "`datos-generacion.json` no puede contener decisiones de composición ni "
            "maquetación.",
            playbook_normalizado,
        )
        plantilla_serializada = json.dumps(self.template, ensure_ascii=False).lower()
        for campo_prohibido in (
            "carta_presentacion",
            "datos_carta",
            "ruta_carta",
            "secciones_carta",
            "decisiones_composicion",
            "maquetacion",
        ):
            with self.subTest(campo_prohibido=campo_prohibido):
                self.assertNotIn(campo_prohibido, plantilla_serializada)


if __name__ == "__main__":
    unittest.main()
