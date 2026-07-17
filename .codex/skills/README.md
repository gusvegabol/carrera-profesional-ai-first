# README — Skills locales activas del host

Este directorio solo mantiene la skill local que sigue siendo propia de `carrera-ai`.

La gobernanza PCS reutilizable, los comandos `pcs::`, los flujos de hosts y las operaciones transversales deben consultarse en el Core estable:

`C:/Users/gusve/Documents/Apps/project-continuity-system`

## Skill local vigente

| Nombre skill | Cuándo se ejecuta | Observación |
|---|---|---|
| `pcs-obsidian-corrige-links` | Cuando hay que convertir referencias documentales crudas en notas de Obsidian de este repositorio a wikilinks y verificar que no queden restos. | Se conserva junto con `agents/openai.yaml` porque sigue siendo una ayuda local ligada a `boveda-entrevista-profesional/`. |

## Regla operativa

Si una tarea afecta a gobernanza PCS, `hosts/hosts.yaml`, prompts `pcs::`, plantillas comunes o utilidades transversales, no debe resolverse desde esta carpeta local de skills. Debe remitirse al Core estable y a sus flujos vigentes.
