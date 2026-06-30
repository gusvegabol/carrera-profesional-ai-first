---
name: drive-mueve-fichero
description: "Use when Codex needs to move Drive files by name, URL, or ID into project folders, export Google Docs or other exportable documents to .md, verify the final parent, or optionally trash the source."
---

# Drive Mueve Fichero

## Ruta rapida

Usar esta skill para trasladar un archivo de Drive desde la raiz a una carpeta del proyecto indicada por ruta relativa, por ejemplo `prompts/codex`.

Priorizar siempre el camino mas corto:

1. Localizar el archivo y la carpeta destino con el conector de Drive.
2. Si el origen ya es Markdown, moverlo con `PATCH files/{id}` y `addParents/removeParents`.
3. Si el origen no es Markdown, exportarlo a `text/markdown`, crear el `.md` en el destino y dejar el original intacto.
4. Verificar el padre final con el conector de Drive.

## Reglas de ejecucion

1. Si el usuario da un ID o URL, no buscar por nombre.
2. Si el destino ya se conoce como carpeta exacta, no resolver rutas extra.
3. Hacer una sola busqueda de archivo y una sola de carpeta cuando haga falta.
4. Leer solo la metadata imprescindible: `mimeType`, `name`, `parents`.
5. No usar `gws auth login` interactivo en el flujo normal.
6. No depender de `gws drive files create/update` si el wrapper da errores de scope.
7. Preferir Drive REST directo con token renovado desde `gws auth export --unmasked`.
8. Si hace falta temporal local, usar `.tmp/` dentro del workspace y borrarlo al terminar.

## Regla de decision

Tomar la decision por metadata, no por la extension visible:

- `.md` real: mover.
- Google Docs u otros documentos exportables: exportar a Markdown.
- Archivo no exportable: detenerse.

Conservar el nombre base del archivo y cambiar a `.md` solo cuando haya conversion.

## Escritura estable

No depender del conector unificado de Drive para la escritura critica si esta en modo solo lectura.

No depender de `gws drive files create/update` como unico camino de escritura si devuelve errores de scopes.

No usar `gws auth login` interactivo como parte normal del flujo.

Preferir un camino directo a Drive REST con un bearer token renovado desde `gws auth export --unmasked` cuando haga falta escritura fiable.

Si hace falta un temporal local, colocarlo dentro del workspace para evitar problemas de ruta.

## Patrón minimo

Cuando el nombre y la carpeta ya son claros, actuar con la secuencia mas corta posible:

- buscar archivo;
- buscar carpeta destino;
- exportar o mover;
- verificar resultado.

No añadir pasos de planificacion intermedios si no cambian la accion.

## Ejemplo de uso

- `$drive-mueve-fichero 'pruebas.gdoc' a la carpeta: 'prompts/codex'`
- `$drive-mueve-fichero 'https://drive.google.com/file/d/.../view' a la carpeta: 'drafts'`
