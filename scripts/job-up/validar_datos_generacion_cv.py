"""Validación aislada del contenido de un CV antes de cualquier composición."""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Any, Iterator


ID_CONTENIDO = re.compile(r"^C-\d{3}$")
ID_BLOQUE = re.compile(r"^B-\d{3}$")
PLACEHOLDER = re.compile(r"{{[^}]+}}")
CLAVES_PROHIBIDAS = {"carta", "carta_presentacion", "composicion", "maquetacion"}


class ValidationError(ValueError):
    """Agrupa los incumplimientos del contrato de datos de generación."""

    def __init__(self, codigos: set[str]):
        self.codigos = sorted(codigos)
        super().__init__("; ".join(self.codigos))


@dataclass(frozen=True)
class Unidad:
    valor: dict[str, Any]
    seccion: str | None


def _normalizar(texto: str) -> str:
    return "".join(
        caracter
        for caracter in unicodedata.normalize("NFD", texto.lower())
        if unicodedata.category(caracter) != "Mn"
    )


def _recorrer(valor: Any) -> Iterator[tuple[str | None, Any]]:
    if isinstance(valor, dict):
        for clave, hijo in valor.items():
            yield clave, hijo
            yield from _recorrer(hijo)
    elif isinstance(valor, list):
        for hijo in valor:
            yield from _recorrer(hijo)


def _unidades(datos: dict[str, Any]) -> Iterator[Unidad]:
    encabezado = datos.get("contenido_cv", {}).get("encabezado", {})
    for clave in ("nombre_completo",):
        if isinstance(encabezado.get(clave), dict):
            yield Unidad(encabezado[clave], None)
    for clave in ("unidades", "contacto"):
        for unidad in encabezado.get(clave, []):
            if isinstance(unidad, dict):
                yield Unidad(unidad, None)
    for seccion in datos.get("contenido_cv", {}).get("secciones", []):
        if not isinstance(seccion, dict):
            continue
        id_seccion = seccion.get("id_seccion")
        for bloque in seccion.get("bloques", []):
            if not isinstance(bloque, dict):
                continue
            for clave in ("cabecera", "unidades"):
                for unidad in bloque.get(clave, []):
                    if isinstance(unidad, dict):
                        yield Unidad(unidad, id_seccion)


def _textos(datos: dict[str, Any]) -> list[str]:
    return [str(unidad.valor.get("texto", "")) for unidad in _unidades(datos)]


def _guia_por_referencia(guion: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {fila["ref"]: fila for fila in guion.get("mapa", []) if isinstance(fila, dict) and "ref" in fila}


def validar_datos_generacion_cv(guion: dict[str, Any], datos: dict[str, Any]) -> None:
    """Valida el contrato editorial, factual y de frontera del JSON de CV."""
    errores: set[str] = set()
    guia = _guia_por_referencia(guion)
    unidades = list(_unidades(datos))
    ids_contenido = [unidad.valor.get("id_contenido") for unidad in unidades]
    ids_bloque = [
        bloque.get("id_bloque")
        for seccion in datos.get("contenido_cv", {}).get("secciones", [])
        if isinstance(seccion, dict)
        for bloque in seccion.get("bloques", [])
        if isinstance(bloque, dict)
    ]

    if any(not isinstance(identificador, str) or not ID_CONTENIDO.fullmatch(identificador) for identificador in ids_contenido):
        errores.add("ID_CONTENIDO_INVALIDO")
    if len(ids_contenido) != len(set(ids_contenido)):
        errores.add("ID_CONTENIDO_DUPLICADO")
    if any(not isinstance(identificador, str) or not ID_BLOQUE.fullmatch(identificador) for identificador in ids_bloque):
        errores.add("ID_BLOQUE_INVALIDO")
    if len(ids_bloque) != len(set(ids_bloque)):
        errores.add("ID_BLOQUE_DUPLICADO")

    fuentes: set[str] = set()
    for fuente in datos.get("generacion", {}).get("fuentes_factuales", []):
        identificador = fuente.get("id") if isinstance(fuente, dict) else None
        if not isinstance(identificador, str) or not identificador.strip():
            errores.add("IDENTIFICADOR_FACTUAL_AUSENTE")
        else:
            fuentes.add(identificador)
    unidades_por_id = {
        unidad.valor.get("id_contenido"): unidad.valor
        for unidad in unidades
        if isinstance(unidad.valor.get("id_contenido"), str)
    }
    for unidad in unidades:
        trazabilidad = unidad.valor.get("trazabilidad")
        if not isinstance(trazabilidad, dict):
            errores.add("TRAZABILIDAD_INCOMPLETA")
            continue
        modo = trazabilidad.get("modo")
        refs = trazabilidad.get("refs_guion", [])
        ref_seccion = trazabilidad.get("ref_seccion_guion")
        if modo == "mapa":
            if not refs:
                errores.add("REFERENCIA_M_AUSENTE")
            for referencia in refs:
                fila = guia.get(referencia)
                if fila is None:
                    errores.add("REFERENCIA_M_INEXISTENTE")
                    continue
                if fila.get("presencia") == "omitir":
                    errores.add("CONTENIDO_OMITIDO_MATERIALIZADO")
                if ref_seccion != fila.get("seccion") or (unidad.seccion is not None and unidad.seccion != fila.get("seccion")):
                    errores.add("SECCION_DESTINO_INCORRECTA")
        elif modo == "continuidad":
            if refs:
                errores.add("CONTINUIDAD_CON_REFERENCIA_M")
            if not ref_seccion:
                errores.add("CONTINUIDAD_SIN_SECCION")
        elif modo != "dato_factual":
            errores.add("MODO_TRAZABILIDAD_INVALIDO")
        for origen in trazabilidad.get("origen_factual", []):
            identificador = origen.get("fuente") if isinstance(origen, dict) else None
            if not isinstance(identificador, str) or not identificador.strip():
                errores.add("IDENTIFICADOR_FACTUAL_AUSENTE")
            if not isinstance(origen, dict) or identificador not in fuentes or not origen.get("refs"):
                errores.add("TRAZABILIDAD_FACTUAL_INVALIDA")
        if not trazabilidad.get("origen_factual"):
            errores.add("TRAZABILIDAD_FACTUAL_INVALIDA")

    for fila in guia.values():
        if fila.get("presencia") == "incluir" and fila.get("obligatoria"):
            cobertura = next(
                (item for item in datos.get("control", {}).get("cobertura_mapa", []) if item.get("ref_guion") == fila["ref"]),
                None,
            )
            if not cobertura or cobertura.get("estado") != "cumplida" or not cobertura.get("refs_contenido"):
                errores.add("COBERTURA_OBLIGATORIA_INCOMPLETA")
                continue
            for id_contenido in cobertura["refs_contenido"]:
                unidad = unidades_por_id.get(id_contenido)
                trazabilidad = unidad.get("trazabilidad", {}) if unidad else {}
                if not unidad or fila["ref"] not in trazabilidad.get("refs_guion", []):
                    errores.add("COBERTURA_OBLIGATORIA_REFERENCIA_INVALIDA")

    for restriccion in datos.get("control", {}).get("restricciones", []):
        if restriccion.get("cumple") is not True:
            errores.add("RESTRICCION_INCUMPLIDA")
    for restriccion_guion in guion.get("restricciones", []):
        restriccion = next(
            (
                fila
                for fila in datos.get("control", {}).get("restricciones", [])
                if fila.get("id_restriccion") == restriccion_guion.get("id")
            ),
            None,
        )
        refs_guion = set(restriccion_guion.get("refs_guion", []))
        refs_contenido = restriccion.get("refs_contenido", []) if restriccion else []
        if (
            not restriccion
            or restriccion.get("cumple") is not True
            or not refs_guion.issubset(restriccion.get("refs_guion", []))
            or not refs_contenido
        ):
            errores.add("RESTRICCION_SIN_COBERTURA_ESTRUCTURADA")
            continue
        for id_contenido in refs_contenido:
            unidad = unidades_por_id.get(id_contenido)
            trazabilidad = unidad.get("trazabilidad", {}) if unidad else {}
            if not unidad or not refs_guion.issubset(trazabilidad.get("refs_guion", [])):
                errores.add("RESTRICCION_SIN_COBERTURA_ESTRUCTURADA")

    texto_normalizado = "\n".join(_normalizar(texto) for texto in _textos(datos))
    for termino in guion.get("lexico", {}).get("prohibidos", []):
        if _normalizar(termino) in texto_normalizado:
            errores.add("LEXICO_PROHIBIDO")
    lexico_control = datos.get("control", {}).get("lexico", {})
    if lexico_control.get("terminos_prohibidos_detectados"):
        errores.add("LEXICO_PROHIBIDO")
    for uso in lexico_control.get("usos_condicionados", []):
        if uso.get("cumple_limite") is not True:
            errores.add("LEXICO_CONDICIONADO_INCUMPLIDO")
    for uso_guion in guion.get("lexico", {}).get("condicionados", []):
        uso = next(
            (fila for fila in lexico_control.get("usos_condicionados", []) if fila.get("termino") == uso_guion.get("termino")),
            None,
        )
        refs_guion = set(uso_guion.get("refs_guion", []))
        refs_contenido = uso.get("refs_contenido", []) if uso else []
        if (
            not uso
            or uso.get("cumple_limite") is not True
            or not refs_guion.issubset(uso.get("refs_guion", []))
            or not refs_contenido
        ):
            errores.add("USO_CONDICIONADO_SIN_TRAZABILIDAD")
            continue
        for id_contenido in refs_contenido:
            unidad = unidades_por_id.get(id_contenido)
            trazabilidad = unidad.get("trazabilidad", {}) if unidad else {}
            if not unidad or not refs_guion.issubset(trazabilidad.get("refs_guion", [])):
                errores.add("USO_CONDICIONADO_SIN_TRAZABILIDAD")

    idioma = datos.get("candidatura", {}).get("idioma_cv")
    if not idioma or idioma != guion.get("idioma_cv"):
        errores.add("IDIOMA_AUSENTE_O_INCORRECTO")
    for clave, valor in _recorrer(datos):
        clave_normalizada = _normalizar(clave) if clave else ""
        if clave_normalizada != "sin_decisiones_de_composicion" and any(
            prohibido in clave_normalizada for prohibido in CLAVES_PROHIBIDAS
        ):
            errores.add("CARTA_O_COMPOSICION_PROHIBIDA")
        if isinstance(valor, str):
            if PLACEHOLDER.search(valor):
                errores.add("PLACEHOLDER_DETECTADO")
    # El gate de salida es metadato normativo requerido por la plantilla, no
    # contenido visible ni una decisión de diseño. La frontera se controla en
    # los textos que llegarán al CV.
    for texto in _textos(datos):
        if any(prohibido in _normalizar(texto) for prohibido in CLAVES_PROHIBIDAS):
            errores.add("CARTA_O_COMPOSICION_PROHIBIDA")
    validaciones = datos.get("control", {}).get("validaciones", {})
    if not validaciones or any(resultado is not True for resultado in validaciones.values()):
        errores.add("VALIDACION_DECLARADA_PENDIENTE")

    if errores:
        raise ValidationError(errores)


def componer_cv_pasivo(datos: dict[str, Any]) -> list[dict[str, Any]]:
    """Devuelve el orden y texto consumible sin abrir candidatura ni guion."""
    resultado: list[dict[str, Any]] = []
    for seccion in sorted(datos.get("contenido_cv", {}).get("secciones", []), key=lambda item: item.get("orden", 0)):
        bloques = []
        for bloque in sorted(seccion.get("bloques", []), key=lambda item: item.get("orden", 0)):
            unidades = [*bloque.get("cabecera", []), *bloque.get("unidades", [])]
            textos = [
                unidad.get("texto", "")
                for unidad in sorted(unidades, key=lambda item: item.get("orden", 0))
            ]
            bloques.append({"id_bloque": bloque.get("id_bloque"), "textos": textos})
        resultado.append({"id_seccion": seccion.get("id_seccion"), "titulo": seccion.get("titulo_visible"), "bloques": bloques})
    return resultado
