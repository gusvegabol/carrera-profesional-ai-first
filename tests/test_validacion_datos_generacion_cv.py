"""Pruebas de contrato del validador aislado de datos de generación del CV."""

import json
import sys
import unittest
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts" / "job-up"))

from validar_datos_generacion_cv import (  # noqa: E402
    ValidationError,
    componer_cv_pasivo,
    validar_datos_generacion_cv,
)


FIXTURES = ROOT / "tests" / "fixtures" / "datos-generacion-cv"
PRODUCTOS = ROOT / "boveda-entrevista-profesional" / "busqueda-empleo" / "candidaturas"


def cargar_json(nombre: str) -> dict:
    return json.loads((FIXTURES / nombre).read_text(encoding="utf-8"))


def aplicar_mutacion(documento: dict, mutacion: dict) -> dict:
    resultado = deepcopy(documento)
    partes = [parte for parte in mutacion["ruta"].split("/") if parte]
    destino = resultado
    for parte in partes[:-1]:
        destino = destino[int(parte)] if isinstance(destino, list) else destino[parte]
    ultimo = partes[-1]
    if mutacion["operacion"] == "eliminar":
        if isinstance(destino, list):
            del destino[int(ultimo)]
        else:
            del destino[ultimo]
    else:
        if isinstance(destino, list):
            destino[int(ultimo)] = mutacion["valor"]
        else:
            destino[ultimo] = mutacion["valor"]
    return resultado


def cargar_guion_productivo(
    ruta: Path, *, prohibidos: list[str], condicionados: list[dict], restricciones: list[dict]
) -> dict:
    mapa = []
    for linea in ruta.read_text(encoding="utf-8").splitlines():
        if not linea.startswith("| M-"):
            continue
        partes = [parte.strip() for parte in linea.split("|")]
        mapa.append(
            {
                "ref": partes[1],
                "presencia": partes[5],
                "obligatoria": partes[6] == "obligatoria",
                "seccion": None if partes[11] == "no_aplica" else partes[11],
            }
        )
    return {
        "idioma_cv": "es",
        "mapa": mapa,
        "lexico": {"prohibidos": prohibidos, "condicionados": condicionados},
        "restricciones": restricciones,
    }


class ValidacionDatosGeneracionCVTests(unittest.TestCase):
    def test_los_dos_fixtures_positivos_cumplen_el_contrato(self) -> None:
        for prefijo in ("lidl", "asic"):
            with self.subTest(caso=prefijo):
                validar_datos_generacion_cv(
                    cargar_json(f"{prefijo}-guion.json"),
                    cargar_json(f"{prefijo}-datos.json"),
                )

    def test_los_fixtures_negativos_fallan_por_la_causa_declarada(self) -> None:
        for caso in cargar_json("casos-negativos.json"):
            with self.subTest(caso=caso["id"]):
                guion = cargar_json(f"{caso['caso_base']}-guion.json")
                datos = cargar_json(f"{caso['caso_base']}-datos.json")
                datos = aplicar_mutacion(datos, caso["mutacion"])
                with self.assertRaises(ValidationError) as capturada:
                    validar_datos_generacion_cv(guion, datos)
                self.assertIn(caso["codigo_esperado"], capturada.exception.codigos)

    def test_el_compositor_pasivo_usa_solo_orden_bloques_y_textos_del_json(self) -> None:
        datos = cargar_json("lidl-datos.json")
        resultado = componer_cv_pasivo(datos)
        self.assertEqual(
            ["Operaciones de tienda", "Experiencia principal", "Continuidad"],
            [seccion["titulo"] for seccion in resultado],
        )
        self.assertEqual(
            "Operaciones de supermercados",
            resultado[0]["bloques"][0]["textos"][0],
        )
        self.assertNotIn("guion", json.dumps(resultado, ensure_ascii=False).lower())

    def test_el_metadato_del_gate_de_salida_no_se_confunde_con_composicion(self) -> None:
        datos = cargar_json("lidl-datos.json")
        datos["generacion"]["gate_salida_aplicable"] = (
            "GATE-CONTENIDO-CV-COMPOSICION"
        )

        validar_datos_generacion_cv(cargar_json("lidl-guion.json"), datos)

    def test_los_datos_productivos_cumplen_sus_guiones_aprobados(self) -> None:
        casos = (
            (
                "CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite",
                ["tesorería", "pagos", "banca", "titulación de FP"],
                [],
                [{"id": "R-LID-001", "refs_guion": ["M-007"]}],
            ),
            (
                "CAND-2026-019-asic-consultores-responsable-automatizacion-ia",
                [
                    "Power Automate", "Power Apps", "Copilot Studio", "Azure AI",
                    "Salesforce", "experiencia profesional en IA", "especialista en IA",
                    "Python", "SAP",
                ],
                [{"termino": "inteligencia artificial", "refs_guion": ["M-012"]}],
                [
                    {"id": "R-ASIC-001", "refs_guion": ["M-006"]},
                    {"id": "R-ASIC-002", "refs_guion": ["M-012"]},
                ],
            ),
        )
        for nombre, prohibidos, condicionados, restricciones in casos:
            with self.subTest(candidatura=nombre):
                carpeta = PRODUCTOS / nombre
                guion = cargar_guion_productivo(
                    carpeta / "guion-adaptacion-cv.md",
                    prohibidos=prohibidos,
                    condicionados=condicionados,
                    restricciones=restricciones,
                )
                datos = json.loads((carpeta / "datos-generacion.json").read_text(encoding="utf-8"))
                validar_datos_generacion_cv(guion, datos)

    def test_el_compositor_pasivo_ordena_una_entrada_desordenada_e_ignora_control_y_candidatura(self) -> None:
        datos = cargar_json("lidl-datos.json")
        datos["contenido_cv"]["secciones"][0]["orden"] = 20
        datos["contenido_cv"]["secciones"][1]["orden"] = 10
        datos["contenido_cv"]["secciones"][2]["orden"] = 30
        datos["control"] = {"resultado_externo": "no debe aparecer"}
        datos["candidatura"] = {"empresa": "no debe aparecer"}

        resultado = componer_cv_pasivo(datos)

        self.assertEqual(
            ["Experiencia principal", "Operaciones de tienda", "Continuidad"],
            [seccion["titulo"] for seccion in resultado],
        )
        salida = json.dumps(resultado, ensure_ascii=False)
        self.assertNotIn("resultado_externo", salida)
        self.assertNotIn("no debe aparecer", salida)


if __name__ == "__main__":
    unittest.main()
