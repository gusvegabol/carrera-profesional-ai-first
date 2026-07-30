# Registros de generación

Esta carpeta contiene los registros JSON de ejecuciones fallidas del generador
documental. Los archivos se excluyen de Git; este README documenta el formato.
El contrato formal está en
`SCHEMA_REGISTRO_GENERACION_ERROR_1.0.json`.

## Nombre

```text
generacion-error-<id-candidatura>-<yyyymmdd-HHMMSS>-<id-ejecucion>.json
```

El identificador de ejecución debe ser único y no reutilizable.

## Campos mínimos

```json
{
  "schema_version": "1.0",
  "fecha": "2026-07-30T21:15:00+01:00",
  "resultado": "fallido",
  "execution_id": "20260730-211500-a1b2c3d4",
  "id_candidatura": "CAND-2026-017",
  "entrada_recibida": "ruta/al/datos-generacion.json",
  "fase": "validacion_json",
  "codigo_error": "JSON_INVALIDO",
  "campo_o_ruta": "ruta/al/datos-generacion.json",
  "mensaje": "Descripción técnica del fallo",
  "documentos_publicados": [],
  "documentos_restaurados": [],
  "documentos_sin_publicar_o_restaurar": []
}
```

Si la candidatura aún no puede identificarse, `id_candidatura` será `null`.
`fecha` siempre debe ser ISO 8601 con zona horaria. Las listas siempre serán
listas, aunque estén vacías.

## Comportamiento ante fallos del registro

El script debe informar siempre del error en consola. Si no puede persistir el
JSON por permisos, bloqueo o falta de espacio, lo comunicará explícitamente y
no intentará ocultar el fallo.

`job-up-inicia-sesion` conservará los registros sin `fecha` válida y comunicará
que no pudo eliminarlos.
