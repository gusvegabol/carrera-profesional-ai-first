---
id: sesion-20260717-1156-migracion-pcs-2-0-carrera-ai
titulo: Migración de carrera-ai a PCS 2.0
inicio: 2026-07-17 11:56
cierre: 2026-07-17 12:42
estado: cerrada
tipo: sesion_trabajo_pcs
sesion_relacionada: sesion-20260717-1058-retirada-graphify-carrera-ai
host: carrera-ai
---

# Migración de carrera-ai a PCS 2.0

## Contexto inmediato

`carrera-ai` ha retirado Graphify y está preparado para validar el flujo de actualización de hosts de PCS 2.0. El registro central lo declara como `pcs_role: host`, `pcs_version: "1.0"`, `status: pendiente_de_actualizacion` y raíz `C:/Users/gusve/Documents/Apps/carrera-profesional-ai-first`.

El Core activo es `pcs-host` con `pcs_version: "2.0"`. La estructura local `.pcs/` contiene `sesiones/`, `acciones/`, `decisiones/` y `estado/`, con memoria histórica que debe preservarse.

## Objetivo

Migrar la orientación y la gobernanza local activa de `carrera-ai` a PCS 2.0, preservando su contenido funcional y su historia, antes de solicitar el cierre registral en PCS Core.

## Capa episódica

- El host parte del commit limpio `db77dee` sobre la rama `codex/migracion-pcs2-carrera-ai`.
- La retirada versionada de Graphify estaba completada, pero una auditoría encontró referencias operativas en configuración local ignorada por Git.
- Se retiraron esas referencias de la configuración de Obsidian y Vault Operator; los JSON resultantes cargan correctamente.
- Las menciones restantes se limitan a entidades históricas `.pcs/` y registros históricos de herramientas.
- El preflight resolvió un único Core activo, una única raíz definitoria y versiones válidas como cadenas.
- La rama seleccionada es B porque `"1.0" < "2.0"` y existe memoria PCS previa.

### Evidencia exacta de preflight

- Antes de crear esta sesión, el árbol versionado del host estaba limpio en `db77dee`.
- El worktree de PCS Core estaba limpio en `08ca80a`, con la adaptación de skills fijada previamente en `0df176d`.
- PyYAML validó el registro, las versiones como cadenas y la existencia de un único Core activo.
- La raíz registrada coincide con la raíz física de esta sesión y la estructura `.pcs/` mínima está completa.
- Los tres JSON locales corregidos tras la auditoría cargan correctamente y no quedan referencias operativas activas a Graphify.
- PyYAML validó el frontmatter de esta sesión y `git diff --check` no detectó errores de formato.

## Capa semántica

La migración afecta a la orientación PCS activa del host, no a su metodología, SPEC, playbooks ni documentación funcional. `README.md` y `AGENTS.md` forman el paquete documental vigente. La capa `.codex/` heredada debe inventariarse porque contiene reglas operativas anteriores, pero no se convierte por ello en parte del paquete documental.

El estado registral no se cambia desde este host. El commit físico de la migración debe preceder a cualquier actualización de `hosts/hosts.yaml`.

## Ideas y líneas cognitivas abiertas

- El inventario clasificó todos los documentos y skills locales heredados.
- Los marcadores de README y AGENTS se resolvieron con hechos verificables.
- Las demás sesiones abiertas del proyecto se preservaron sin reinterpretarlas ni cerrarlas automáticamente.

## Aplicación confirmada

El usuario recibió el resumen posterior a las diferencias y confirmó expresamente:

1. sustituir `README.md` y `AGENTS.md` por las propuestas PCS 2.0;
2. retirar `.codex/AGENTS.md` de la capa activa;
3. retirar seis skills heredadas y conservar `pcs-obsidian-corrige-links`;
4. reescribir `.codex/skills/README.md` como catálogo local reducido;
5. ejecutar, después del commit y la validación física, el cierre de `pcs_version`, la actualización separada de `status` y la segunda pasada C.

## Cambios y preservaciones

### Modificados

- `README.md` y `AGENTS.md`.
- `.codex/skills/README.md`.
- `.pcs/estado/estado-actual.md`.
- Esta sesión.

### Retirados de la capa activa

- `.codex/AGENTS.md`.
- `.codex/skills/drive-mueve-fichero/`.
- `.codex/skills/pcs-genera-documentos-host-anfitrion/`.
- `.codex/skills/pcs-generar-system-prompt-host-anfitrion/`.
- `.codex/skills/pcs-gestionar-hosts/`.
- `.codex/skills/pcs-gestionar-notion-codex/`.
- `.codex/skills/pcs-pagina-tempo-notion/`.

La historia de los archivos retirados permanece disponible en Git.

### Conservados

- `.codex/config.toml`.
- `.codex/skills/pcs-obsidian-corrige-links/` y su `agents/openai.yaml`.
- Todas las sesiones, decisiones, acciones y documentos funcionales previos del host.
- El foco metodológico, el SPEC, el playbook y la documentación de la bóveda.

### Excluidos

- No se modificaron la metodología, el SPEC, los playbooks ni el contenido funcional fuera de README y AGENTS.
- No se copiaron comandos, prompts, system prompts, plantillas, fuentes del workspace ni artefactos de ChatGPT Classic.

## Acciones derivadas

- No se crea una ACCIÓN: la migración está acotada por esta sesión y el plan controlado del Core.

## Decisiones derivadas

- No se crea una DECISIÓN: la intervención aplica decisiones y flujos ya vigentes.

## Problemas o bloqueos

- La confirmación documental ya fue recibida y aplicada.
- No quedan bloqueos físicos en el host; `pcs_version` y `status` deben modificarse desde PCS Core mediante sus respectivos flujos guiados.

## Documentos afectados

- Esta sesión.
- `README.md`, `AGENTS.md`, `.codex/AGENTS.md`, `.codex/skills/` y `.pcs/estado/estado-actual.md`.

## Rehidratación futura

- Dónde quedó el trabajo: migración física aplicada; cierre registral pendiente en PCS Core.
- Leer primero: esta sesión, `.pcs/estado/estado-actual.md`, README, AGENTS y la capa `.codex/`.
- Líneas abiertas a retomar: commit del host, cierre registral y segunda pasada C.
- Riesgos de malinterpretación: no tratar referencias históricas a Graphify como reglas activas ni cambiar la metodología de Carrera AI dentro de esta migración.
- Siguiente gesto recomendado: validar y consolidar el commit del host antes de modificar `hosts/hosts.yaml`.

## Checklist de consolidación

- [x] La capa episódica registra el preflight y la clasificación.
- [x] La capa semántica delimita la migración respecto al proyecto funcional.
- [x] Las líneas cognitivas abiertas están identificadas.
- [x] No procede crear una ACCIÓN nueva.
- [x] No procede crear una DECISIÓN nueva.
- [x] ESTADO_PROYECTO está actualizado tras aplicar la migración.
- [x] Los documentos potencialmente afectados están identificados.
- [x] La rehidratación permite continuar desde el inventario.
- [x] La sesión no sustituye al estado vivo.

## Trazabilidad

- Origen: prueba real del flujo PCS 2.0 coordinada desde PCS Core.
- Sesión relacionada: `sesion-20260717-1058-retirada-graphify-carrera-ai`.
- Sesión del Core: `sesion-20260717-1156-validacion-flujo-pcs-2-0-carrera-ai`.
- Estado de proyecto relacionado: `../estado/estado-actual.md`.
- Cierre: validación física completada; el cierre registral corresponde ahora a PCS Core.

## Validación final

- `README.md` y `AGENTS.md` coinciden exactamente con las propuestas confirmadas.
- La única skill local activa es `pcs-obsidian-corrige-links`, validada correctamente.
- No quedan referencias activas a las seis skills retiradas en la orientación local.
- Los tres JSON de configuración saneados cargan correctamente y no contienen referencias operativas a Graphify.
- El frontmatter de esta sesión y de `.pcs/estado/estado-actual.md` carga correctamente como YAML.
- `git diff --check` no detecta errores de espacios ni marcadores sin resolver.
