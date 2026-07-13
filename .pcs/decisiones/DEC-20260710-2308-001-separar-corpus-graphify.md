---
id: DEC-20260710-2308-001-separar-corpus-graphify
titulo: Separar los corpus de Graphify por finalidad documental
estado: sustituida
fecha_registro: 2026-07-13
fecha_adopcion: 2026-07-13
fecha_vigencia: 2026-07-13
fecha_sustitucion: 2026-07-13
sustituida_por: DEC-20260713-1344-001-integrar-graphify-tres-corpus
tipo: decision
host: carrera-ai
sesion_origen: sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai
---

# DEC-20260710-2308-001-separar-corpus-graphify — Separar los corpus de Graphify por finalidad documental

> Esta decisión quedó sustituida el 2026-07-13 por `DEC-20260713-1344-001-integrar-graphify-tres-corpus`, que incorpora `.pcs/` como tercer corpus y fija `run-graphify.bat` con Ollama como actualizador común.

## Decisión

Graphify se ejecutará por corpus documental independiente y no sobre la raíz completa del repositorio. La entrada operativa vigente, `run-graphify.bat`, procesará por separado:

- `boveda-entrevista-profesional/`, como corpus de documentación operativa y metodológica de la entrevista y sus artefactos relacionados.
- `docs/`, como corpus de SPEC funcional, núcleo metodológico, ideas de debate, evaluación y presentación.

La separación es una regla operativa vigente para la indexación y recuperación de contexto. Los grafos, informes y salidas generados son artefactos derivados; no sustituyen a las fuentes documentales ni crean por sí mismos decisiones, requisitos o cambios de estado PCS.

## Motivo

Las carpetas tienen finalidades documentales distintas. Mantenerlas separadas reduce el riesgo de generar relaciones artificiales entre documentos que no comparten autoridad ni propósito, evita comunidades contaminadas y facilita recuperar únicamente el contexto pertinente para una consulta.

La separación también hace visible qué corpus respalda una respuesta. Si una pregunta necesita información de ambos ámbitos, la respuesta debe componer consultas o resultados de ambos grafos de forma explícita, conservando la procedencia de cada fuente.

## Contexto

La configuración actual de `run-graphify.bat` ejecuta Graphify primero en `boveda-entrevista-profesional/` y después en `docs/`. En `docs/.graphifyignore` se excluyen `superpowers/`, `graphify-out/`, `AGENTS.md` y `.graphifyignore`, porque son material de proceso, salida generada o configuración operativa, no fuentes metodológicas del corpus.

Esta decisión formaliza una práctica que ya se está utilizando. No implica que la utilidad de Graphify esté validada de forma definitiva: esa utilidad se revisará más adelante con evidencia de uso, calidad de recuperación, coste de contexto y ausencia de contaminación entre corpus.

## Alternativas descartadas

- Ejecutar Graphify sobre la raíz completa del repositorio.
- Fusionar `boveda-entrevista-profesional/` y `docs/` en un único grafo.
- Indexar `docs/superpowers/` como si fuera parte del núcleo metodológico; sus documentos sirven al proceso de especificación y planificación de la herramienta Superpowers.
- Tratar el grafo, sus comunidades o sus nodos centrales como autoridad normativa sin confirmar la fuente original.

## Impacto esperado

- Las consultas deben dirigirse al corpus adecuado y conservar la procedencia de sus resultados.
- Las salidas de Graphify pueden vivir dentro de cada corpus, pero deben considerarse regenerables y derivadas.
- Las herramientas que consulten `docs/` deben respetar `docs/AGENTS.md` y `docs/.graphifyignore`.
- La separación no modifica `docs/DOCUMENTO_SPEC_CARRERA_AI.md`, el playbook de profundidad, el futuro playbook de cobertura ni la metodología del núcleo.
- La separación no altera el alcance de PCS ni convierte documentos de `docs/` en decisiones canónicas por el hecho de estar indexados.

## Alcance

Esta decisión cubre únicamente los límites de corpus y la ejecución de Graphify. No prohíbe leer manualmente documentos de ambos corpus cuando una tarea lo requiera, siempre que se indique la procedencia y se respeten las reglas de cada ámbito.

No se autoriza una fusión automática ni silenciosa de grafos. Cualquier cambio de este límite deberá revisarse como una decisión posterior y apoyarse en evidencia de uso, no en una inferencia del propio Graphify.

## Relaciones

- Sesión origen: `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`.
- Estado afectado: `.pcs/estado/estado-actual.md`.
- Acciones afectadas: ninguna acción formal abierta; la ejecución operativa queda descrita en `run-graphify.bat`.
- Decisión anterior o sustituida: ninguna.

## Revisión

La decisión permanece vigente mientras la separación siga ofreciendo recuperación más precisa y contexto más manejable. Se revisará cuando exista experiencia suficiente para comparar, como mínimo, precisión de recuperación, relaciones irrelevantes, coste de contexto, trazabilidad y necesidad real de consultas transversales.

## Trazabilidad

- `run-graphify.bat`
- `docs/AGENTS.md`
- `docs/.graphifyignore`
- `.pcs/estado/estado-actual.md`
- `.pcs/sesiones/sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`
