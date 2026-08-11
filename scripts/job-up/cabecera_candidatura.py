"""Fuente y representación compartida de la cabecera CV/carta."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


CANONICAL_HEADER_VERSION = "datos-generacion-cv@1.2"
CANONICAL_HEADER_ORIGIN = "datos-generacion.json:contenido_cv.encabezado"
HEADER_FONT = "Calibri"
HEADER_NAME_SIZE = 18
HEADER_TITLE_SIZE = 12
HEADER_CONTACT_SIZE = 10


class CabeceraError(ValueError):
    """La cabecera no puede resolverse o no cumple la autorización."""


@dataclass(frozen=True)
class CabeceraCandidatura:
    nombre: str
    titular: str
    contacto: tuple[str, ...]
    tipos_contacto: tuple[str, ...] = ()
    origen: str = CANONICAL_HEADER_ORIGIN
    version: str = CANONICAL_HEADER_VERSION

    @property
    def lineas(self) -> tuple[str, str, str]:
        return self.nombre, self.titular, " | ".join(self.contacto)


def _authorization(payload: dict[str, Any]) -> dict[str, str]:
    try:
        authorization = payload["control"]["datos_privados"]["autorizacion"]
    except (KeyError, TypeError) as exc:
        raise CabeceraError("Falta la autorización de datos privados del JSON.") from exc
    expected = {"nombre", "apellido_1", "apellido_2", "email", "telefono", "linkedin", "ubicacion", "fotografia"}
    if set(authorization) != expected or any(value not in {"incluir", "omitir"} for value in authorization.values()):
        raise CabeceraError("La autorización de datos privados está incompleta o es inválida.")
    return {str(key): str(value) for key, value in authorization.items()}


def _name_refs(payload: dict[str, Any]) -> set[str]:
    try:
        origins = payload["contenido_cv"]["encabezado"]["nombre_completo"]["trazabilidad"]["origen_factual"]
    except (KeyError, TypeError) as exc:
        raise CabeceraError("Falta la trazabilidad del nombre de cabecera.") from exc
    return {
        str(reference)
        for origin in origins
        if isinstance(origin, dict) and origin.get("fuente") == "datos-privados-candidatura"
        for reference in origin.get("refs", [])
    }


def construir_cabecera_candidatura(payload: dict[str, Any], validar_privacidad: bool = True) -> CabeceraCandidatura:
    """Construye la cabecera desde el mismo encabezado que consume el CV."""
    if payload.get("schema_id") != "datos-generacion-cv" or payload.get("schema_version") != "1.2":
        raise CabeceraError("La cabecera requiere datos-generacion-cv 1.2.")
    try:
        header = payload["contenido_cv"]["encabezado"]
        name = header["nombre_completo"]
        units = sorted(header.get("unidades", []), key=lambda item: int(item.get("orden", 0)))
        contacts = sorted(header.get("contacto", []), key=lambda item: int(item.get("orden", 0)))
    except (KeyError, TypeError, ValueError) as exc:
        raise CabeceraError("Falta la estructura canónica de cabecera.") from exc
    authorization = _authorization(payload) if validar_privacidad else None
    name_text = str(name.get("texto", "")).strip()
    titular = " | ".join(str(item.get("texto", "")).strip() for item in units if str(item.get("texto", "")).strip())
    contact_values = tuple(str(item.get("texto", "")).strip() for item in contacts if str(item.get("texto", "")).strip())
    contact_types = tuple(str(item.get("tipo", "")).strip() for item in contacts)
    if not name_text or not titular or not contact_values or len(contact_values) != len(contact_types):
        raise CabeceraError("La cabecera canónica contiene valores vacíos.")
    if authorization is not None:
        expected_name_refs = {ref for ref, field in {"Nombre": "nombre", "Apellido 1": "apellido_1", "Apellido 2": "apellido_2"}.items() if authorization[field] == "incluir"}
        if _name_refs(payload) != expected_name_refs:
            raise CabeceraError("El nombre de cabecera no coincide con la autorización.")
        expected_contact_types = tuple(field for field in ("email", "telefono", "linkedin", "ubicacion") if authorization[field] == "incluir")
        if set(contact_types) != set(expected_contact_types):
            raise CabeceraError("El contacto de cabecera no coincide con la autorización.")
    return CabeceraCandidatura(name_text, titular, contact_values, contact_types)


def validar_cabecera_contrato(
    header: CabeceraCandidatura,
    authorization: dict[str, str],
    canonical: CabeceraCandidatura | None = None,
) -> None:
    """Valida privacidad y, si se proporciona, igualdad con la cabecera canónica."""
    expected_types = {field for field in ("email", "telefono", "linkedin", "ubicacion") if authorization.get(field) == "incluir"}
    if set(header.tipos_contacto) != expected_types:
        raise CabeceraError("La cabecera contiene datos personales no autorizados.")
    if any(not value.strip() for value in (header.nombre, header.titular, *header.contacto)):
        raise CabeceraError("La cabecera contiene valores vacíos.")
    if canonical is not None and header != canonical:
        raise CabeceraError("La cabecera diverge del contrato canónico de CV.")


def renderizar_lineas_cabecera(header: CabeceraCandidatura) -> tuple[str, str, str]:
    return header.lineas
