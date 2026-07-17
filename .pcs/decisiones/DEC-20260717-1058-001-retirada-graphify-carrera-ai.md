---
id: DEC-20260717-1058-001-retirada-graphify-carrera-ai
titulo: Retirada de Graphify de carrera-ai
estado: vigente
fecha_registro: 2026-07-17
fecha_adopcion: 2026-07-17
fecha_vigencia: 2026-07-17
tipo: decision
host: carrera-ai
sesion_origen: sesion-20260717-1058-retirada-graphify-carrera-ai
decision_sustituida: DEC-20260713-1344-001-integrar-graphify-tres-corpus
---

# DEC-20260717-1058-001 — Retirada de Graphify de `carrera-ai`

## Decisión

Graphify se retira de `carrera-ai`. No se mantendrán sus scripts, archivos de configuración ni salidas generadas como parte de la operación del host. La localización y verificación de relaciones documentales se realizará directamente sobre las fuentes Markdown y sus enlaces.

La materialización física de esta retirada se registrará y comprobará dentro de la sesión de trabajo relacionada antes de darla por consolidada.

## Motivo

La extracción semántica requiere un coste de tiempo y recursos desproporcionado para el ritmo habitual de cambios documentales de `carrera-ai`. Los resultados dependen además de modelos que no siempre generan salidas estructuradas válidas.

## Contexto

La decisión `DEC-20260713-1344-001-integrar-graphify-tres-corpus` organizó Graphify en tres corpus independientes y estableció `run-graphify.bat` como actualizador común con Ollama local. Esa configuración permitió una operación reproducible, pero la experiencia documentada en PCS Core muestra que las ejecuciones siguen siendo lentas y poco fiables para el mantenimiento cotidiano.

Esta decisión aplica al host `carrera-ai` por analogía controlada con la decisión canónica de PCS Core `DEC-20260715-0004-retirada-graphify-pcs-host`; no modifica PCS Core ni convierte la decisión del Core en una copia local autónoma.

## Alternativas descartadas

- Mantener Graphify como actualizador habitual de la documentación.
- Conservar los grafos como índice operativo que requiera regeneración frecuente.
- Seguir ajustando modelos, lotes o parámetros para sostener el uso diario.

## Impacto esperado

- Menos artefactos derivados y menos cambios pendientes en el repositorio.
- Menor consumo de recursos locales y remotos.
- Verificación documental basada en enlaces Markdown y revisión directa de fuentes.
- Rehidratación PCS basada directamente en estado, decisiones, sesiones y documentos fuente.

## Alcance

La retirada afecta a `run-graphify.bat`, cualquier configuración local de Graphify y los directorios `graphify-out/` del host, incluidos los corpus `.pcs/`, `docs/` y `boveda-entrevista-profesional/`, siempre dentro de la materialización que se compruebe en la sesión relacionada.

No modifica el SPEC, el núcleo metodológico, el playbook de profundidad, la bóveda de entrevista ni las entidades del PCS Core.

## Relaciones

- Decisión de referencia en PCS Core: `DEC-20260715-0004-retirada-graphify-pcs-host`.
- Decisión local sustituida: `DEC-20260713-1344-001-integrar-graphify-tres-corpus`.
- Sesión origen: `sesion-20260717-1058-retirada-graphify-carrera-ai`.
- Estado afectado: `.pcs/estado/estado-actual.md`.

## Revisión futura

Solo una necesidad concreta y aprobada podrá justificar evaluar de nuevo una herramienta de análisis semántico. Esta decisión no registra ni prescribe ninguna alternativa tecnológica.

## Trazabilidad

- `C:/Users/gusve/Documents/Apps/project-continuity-system/.pcs/decisiones/DEC-20260715-0004-retirada-graphify-pcs-host.md`.
- `DEC-20260713-1344-001-integrar-graphify-tres-corpus.md`.
- `sesion-20260717-1058-retirada-graphify-carrera-ai.md`.
- `.pcs/estado/estado-actual.md`.
