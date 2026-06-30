---
name: pcs-pagina-tempo-notion
description: Usar cuando se necesite convertir una página de Notion de pcs-prompts-codex, pcs-respuestas-prompts-codex o pcs-documentos en un documento temporal en .tmp/, o cuando haya que rechazar una página que venga de otra colección.
---

# Página temporal de Notion PCS

## Overview

Convierte una página de Notion en un documento local temporal, pero solo si la página pertenece a una de las colecciones PCS aprobadas. La skill valida el origen, exporta solo el cuerpo de la página, revisa que el archivo generado coincida con el contenido leído de Notion y, al final, sincroniza el resultado con FreeFileSync.

## Cuándo usarla

- La entrada es una URL o un ID de página de Notion.
- Se necesita un archivo temporal en `.tmp/` para inspección o depuración.
- El origen debe verificarse antes de exportar.

No continuar si la página no pertenece a:

- `pcs-prompts-codex`
- `pcs-respuestas-prompts-codex`
- `pcs-documentos`

## Flujo

1. Leer la página de Notion.
2. Verificar que su colección o data source padre está entre las permitidas.
3. Detener el proceso si el origen no es válido.
4. Tomar el título de la página como base del nombre de archivo.
5. Sanitizar el título para uso en sistema de archivos, sustituyendo también los espacios por guiones `-`.
6. Escribir solo el cuerpo de la página en `.tmp/`, sin propiedades.
7. Revisar el archivo generado y compararlo con el cuerpo leído de Notion.
8. Ejecutar FreeFileSync como paso final.
9. Informar del resultado.

## Reglas de exportación

- Usar el título de la página de Notion como nombre base del archivo.
- Eliminar o reemplazar caracteres no válidos del sistema de archivos, como `/ \ : * ? " < > |`.
- Sustituir todos los espacios del nombre base por guiones `-`.
- Mantener el archivo dentro de `.tmp/`.
- Si el archivo ya existe en `.tmp/`, sobrescribirlo con el nuevo contenido.
- No incluir propiedades de Notion en el archivo de salida.
- No añadir encabezados, notas o metadatos que no estén en el cuerpo leído.

Ejemplo:

- Incorrecto: `Actualizar estado y sesión flujos.md`
- Correcto: `Actualizar-estado-y-sesión-flujos.md`

## Reglas de revisión

- Revisar el archivo generado antes de declarar éxito.
- Comprobar que el archivo coincide con el cuerpo de Notion.
- Si hay diferencias, tratarlo como fallo y no como éxito parcial.
- Si el cuerpo de Notion no puede leerse con suficiente claridad, detener el flujo y explicar el bloqueo.

## Sincronización final

Si la exportación y la revisión han salido bien:

- ejecutar `C:\Program Files\FreeFileSync\FreeFileSync.exe`
- pasar como argumento la ruta completa del `.ffs_batch` entre comillas porque contiene un espacio en `Mi unidad`
- formato correcto de invocación:

```powershell
& 'C:\Program Files\FreeFileSync\FreeFileSync.exe' 'G:\Mi unidad\Proyectos-IA\AutoSync-project-continuity-system.ffs_batch'
```

- no separar `G:\Mi unidad\Proyectos-IA\AutoSync-project-continuity-system.ffs_batch` en varios argumentos
- si la ejecución devuelve log o salida de sincronización, conservar la ruta del log como referencia de depuración

## Resultado

- Si todo sale bien tras la revisión y la sincronización, responder exactamente: `Documento creado`.
- Si algo falla, responder con errores y suficiente detalle para diagnosticar el problema.

## Errores comunes

- Aceptar una página de una colección no aprobada.
- Escribir propiedades dentro del documento temporal.
- Usar el título bruto sin sanitizar caracteres inválidos del nombre de archivo.
- Conservar espacios en el nombre del archivo temporal en vez de convertirlos a guiones `-`.
- No sobrescribir un archivo existente en `.tmp/`.
- Saltarse la comparación final entre el archivo generado y el cuerpo de Notion.
- Omitir la sincronización final cuando la creación del documento haya sido correcta.
- Pasar la ruta `G:\Mi unidad\Proyectos-IA\AutoSync-project-continuity-system.ffs_batch` sin tratarla como un único argumento citado.
- Intentar abrir solo el archivo `.ffs_batch` sin pasar por `FreeFileSync.exe`.
- Devolver un mensaje de éxito vago en lugar de la frase exacta requerida.
