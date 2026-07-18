# Carrera AI

Flujo operativo vigente: flujo PCS 2.0 (`Usuario -> Work -> Usuario`).

## Qué es este proyecto

Carrera AI es un proyecto para convertir la experiencia profesional real de una persona en un Perfil Profesional Accionable mediante entrevista asistida por IA, con evidencias, narrativas y opciones profesionales. La correspondencia con ESCO se investiga de forma paralela y no forma parte del alcance vigente.

## Objetivo del proyecto

El objetivo es diseñar y validar una forma de entrevista que permita reconstruir trayectorias profesionales completas, extraer experiencia tácita útil y transformarla en salidas profesionales revisables por la propia persona.

## Versión global actual

`Carrera AI 2.0` está `en desarrollo`.

Su objetivo es validar un primer Perfil Profesional Accionable integral y revisable mediante cobertura profesional, inmersión en profundidad, evidencias y síntesis de trayectoria. ESCO queda fuera del criterio de finalización de `2.0` y continúa como investigación paralela.

La fuente funcional de verdad es [Versionado funcional de Carrera AI](docs/VERSIONADO_CARRERA_AI.md). El procedimiento de transición está en [Flujo de cambio de versión](docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md).

## Estado actual

El estado operativo vivo del host se consulta en `./.pcs/estado/estado-actual.md`.

Actualmente, el foco activo está en la revisión metodológica de la entrevista de cobertura profesional y en decidir si la arquitectura recomendada debe orientar el primer piloto. `docs/DOCUMENTO_SPEC_CARRERA_AI.md` sigue siendo la referencia funcional visible, mientras que el núcleo metodológico y el debate de cobertura concentran la exploración actual.

## Estructura relevante del proyecto

- `./.pcs/` como memoria operativa local del host.
- `./docs/` como documentación funcional y metodológica del proyecto.
- `./boveda-entrevista-profesional/` como bóveda de trabajo para conceptos, métodos, patrones, fricciones, ejemplos y playbook de entrevista.

## Relación con PCS

Este repositorio es el proyecto registrado en PCS con alias `carrera-ai`.

PCS aporta la gobernanza común y la continuidad operativa; este host aporta el contexto funcional y metodológico propio del proyecto. La fuente normativa común aplicable se consulta en el Core activo:

`C:/Users/gusve/Documents/Apps/project-continuity-system`

En particular, la referencia viva de gobernanza de hosts está en:

`C:/Users/gusve/Documents/Apps/project-continuity-system/core/CONTRATO_CANONICO_GOBERNANZA_HOSTS.md`

## Continuidad operativa

- Las sesiones registran historia en `./.pcs/sesiones/`.
- El estado vivo se consulta en `./.pcs/estado/estado-actual.md`.
- Las acciones abiertas viven en `./.pcs/acciones/`.
- Las decisiones vigentes viven en `./.pcs/decisiones/`.

## Comandos PCS en Work

Las peticiones que comiencen por `pcs::` deben encaminarse por referencia viva al Core, sin copiar sus flujos dentro de este proyecto. El orden de consulta es:

- `C:/Users/gusve/Documents/Apps/project-continuity-system/prompts/work-comandos/INDEX_COMANDOS.md`
- `C:/Users/gusve/Documents/Apps/project-continuity-system/prompts/work-comandos/COMANDOS_GOBERNANZA.md`
- el documento específico que indique el índice para cada comando

Si el comando no figura en el índice o el alias indicado no existe en `C:/Users/gusve/Documents/Apps/project-continuity-system/hosts/hosts.yaml`, el agente debe avisar y detenerse sin realizar cambios.

## Documentación principal del proyecto

- `./docs/DOCUMENTO_SPEC_CARRERA_AI.md`
- `./docs/VERSIONADO_CARRERA_AI.md`
- `./docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md`
- `./docs/AGENTS.md`
- `./docs/metodologia/conceptos/idea-central.md`
- `./docs/trabajo-en-curso/debates/05_Evaluacion_experta_y_recomendacion_de_enfoque.md`
- `./docs/Ideas debate - como afrontar entrevista cobertura profesional/06_Presentacion_propuesta_recomendada.html`
- `./boveda-entrevista-profesional/README.md`
- `./boveda-entrevista-profesional/INDEX.md`

## Siguiente gesto recomendado

Revisar la recomendación metodológica actual, decidir si orienta el primer piloto de cobertura profesional y mantener separadas, hasta decisión explícita, la cobertura, la profundidad y la correspondencia ESCO.
