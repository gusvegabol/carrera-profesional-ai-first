# README — Skills locales del proyecto

Este directorio reúne las skills locales de CODEX específicas de este repositorio.

Su función es capturar flujos repetibles, contratos operativos y ayudas guiadas que pertenecen a este proyecto y no al comportamiento general de CODEX.

Reglas prácticas de uso:

- una skill local se usa cuando la tarea coincide con su ámbito y conviene seguir un flujo ya fijado;
- estas skills no sustituyen `README.md`, `AGENTS.md`, `.codex/AGENTS.md` ni los documentos canónicos de `core/`;
- si una skill depende de documentos del proyecto, esos documentos siguen siendo la autoridad de fondo;
- la fecha de última revisión de la tabla se toma del `LastWriteTime` actual del fichero `SKILL.md` de cada skill local.

Convención de nombres:

- las skills PCS reutilizables usan el prefijo `pcs-` en su nombre operativo y en el `name` de su `SKILL.md`;
- las skills de host o de dominio local no usan ese prefijo salvo que sean una extensión reutilizable de PCS.

## Índice de skills

| Nombre skill | Cuándo se ejecuta | Fecha última revisión |
|---|---|---|
| `drive-mueve-fichero` | Cuando hay que mover ficheros de Google Drive por nombre, URL o ID a carpetas del proyecto, exportar Google Docs u otros ficheros exportables a `.md`, verificar la carpeta final o, si procede, enviar el origen a la papelera. | 2026-06-15 17:41 |
| `pcs-generar-system-prompt-host-anfitrion` | Cuando se necesita generar en `.tmp/` el system prompt corto de un workspace ChatGPT para un host anfitrión PCS ya registrado en `hosts/hosts.yaml`. | 2026-06-18 17:19 |
| `pcs-gestionar-hosts` | Cuando hay que crear, registrar, añadir, actualizar o archivar un host PCS en `hosts/hosts.yaml`, o validar YAML/frontmatter relacionado con ese flujo. | 2026-06-15 10:49 |
| `pcs-gestionar-notion-codex` | Cuando CODEX recibe una URL o page ID aprobado desde `pcs-prompts-codex`, especialmente en ciclos de trabajo ligados a un host PCS, al repositorio local o a una respuesta coordinada en Notion. | 2026-06-15 13:46 |
| `pcs-genera-documentos-host-anfitrion` | Cuando se necesita generar en `.tmp/` los borradores coordinados de `README` y `AGENTS` para un host anfitrión PCS ya registrado en `hosts/hosts.yaml`. | 2026-06-19 13:06 |
| `pcs-pagina-tempo-notion` | Cuando se necesita convertir una página de Notion de `pcs-prompts-codex`, `pcs-respuestas-prompts-codex` o `pcs-documentos` en un documento temporal dentro de `.tmp/`, o rechazar páginas que vengan de otra colección. | 2026-06-17 22:23 |

## Mantenimiento

Si se añade una skill nueva a `.codex/skills/`, este índice debe actualizarse.

Si una skill cambia de alcance, conviene revisar tanto la columna "Cuándo se ejecuta" como la fecha de última revisión.
