---
id: sesion-20260720-1242-investigacion-github-carrera-ai-first
titulo: Investigación GitHub para Carrera AI-First
inicio: 2026-07-20 12:42
cierre:
estado: abierta
tipo: sesion
host: carrera-ai
sesion_relacionada: sesion-20260705-concepto-cobertura-profesional-carrera-ai
---

# Sesión PCS — Investigación GitHub para Carrera AI-First

## Contexto inmediato

Se ha añadido el documento `docs/ideas-y-debates/investigacion-github/INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md`, que abre una línea de investigación técnica separada de la entrevista de cobertura profesional.

La investigación no busca encontrar un clon completo ni realizar un fork integral. Busca localizar ideas, arquitecturas, componentes, modelos de datos, prompts o flujos que puedan reutilizarse, adaptarse o servir como referencia para acelerar Carrera AI-First sin desviar la MVP.

## Objetivo

Localizar y evaluar repositorios de GitHub cuyas ideas, arquitecturas o componentes puedan acelerar Carrera AI-First.

La investigación debe permitir decidir:

1. qué partes no merece la pena construir desde cero;
2. qué repositorios contienen componentes realmente separables;
3. qué modelos de datos pueden inspirar el perfil profesional;
4. cómo implementar continuidad y memoria sin sobrediseñar;
5. qué patrones de entrevista pueden reforzar el playbook actual;
6. qué herramientas pueden importar información previa sin condicionar la entrevista;
7. qué opciones existen para visualizar la cobertura profesional;
8. qué componentes pertenecen a la MVP y cuáles a fases posteriores;
9. qué experimentos técnicos ofrecen más aprendizaje con menor coste;
10. qué repositorios deben descartarse para evitar desviaciones.

## Capa episódica

La primera selección del documento procede de una investigación inicial de propósito general. Todavía no constituye una auditoría técnica ni una recomendación definitiva de integración.

La investigación se separa de la decisión metodológica sobre la doble pasada. Puede aportar componentes o referencias, pero no modifica por sí sola el SPEC, los playbooks ni el alcance de Carrera AI-First.

## Primera selección prioritaria

La fase técnica inicial analizará estos ocho repositorios:

1. `noamseg/interview-coach-skill` — entrevista y *storybank*.
2. `wespiper/pyresume` — parsing e importación de CV.
3. `xitanggg/open-resume` — modelo de datos, parser y representación final.
4. `langchain-ai/langgraph` — estado, checkpoints y orquestación.
5. `FareedKhan-dev/langgraph-long-memory` — memoria persistente y continuidad.
6. `Krishna77-ux/Orbit.AI` — visualización, brechas y experiencia de producto.
7. `luillyfe/resume-insights` — pipeline documento → extracción → revisión.
8. `srbhr/Resume-Matcher` — adecuación de perfil a puestos como fase futura.

## Criterios de evaluación

Cada repositorio se revisará según:

- encaje funcional;
- reutilización real;
- calidad arquitectónica;
- madurez;
- dependencias;
- licencia;
- coste de integración;
- riesgo de desvío;
- valor de aprendizaje;
- decisión preliminar: reutilizar, prototipar, estudiar como referencia o descartar.

## Capa semántica

La investigación parte de tres orientaciones provisionales que deben comprobarse técnicamente:

- el mayor valor puede estar en componentes laterales, como parsing de CV, *storybank*, memoria, checkpoints, evaluación, mapas y generación de productos;
- la arquitectura multiagente no debe anticiparse mientras no se demuestre que el flujo guiado por playbooks y artefactos resulta insuficiente;
- el CV debe ser una fuente de contexto, no el centro de un sistema que debe descubrir información omitida o tácita.

## Documentos afectados

- `docs/ideas-y-debates/investigacion-github/INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md`
- `docs/ideas-y-debates/investigacion-github/README.md`
- `docs/ideas-y-debates/investigacion-github/FLUJO_INVESTIGACION_GITHUB.md`
- `docs/ideas-y-debates/investigacion-github/fichas/TEMPLATE_FICHA_REPOSITORIO.md`
- `docs/ideas-y-debates/investigacion-github/fichas/noamseg-interview-coach-skill.md`
- `docs/ideas-y-debates/investigacion-github/comparativas/MATRIZ_COMPARATIVA_REPOSITORIOS.md`
- `docs/ideas-y-debates/investigacion-github/comparativas/RECOMENDACION_COMPONENTES_Y_EXPERIMENTOS.md`
- `docs/trabajo-en-curso/diseno/MATRIZ_EVALUACION_PILOTO_COBERTURA_PROFESIONAL.md`, solo si la investigación propone criterios experimentales que deban separarse de la evaluación del piloto.

## Líneas cognitivas abiertas

- comparar las ocho fichas técnicas de la primera selección en la matriz correspondiente;
- completar la comprobación cruzada de licencia, actividad, stack, dependencias y calidad interna;
- identificar componentes separables sin incorporar complejidad innecesaria;
- diseñar experimentos técnicos baratos y con aprendizaje claro;
- comparar memoria y continuidad externas con los artefactos y checkpoints actuales;
- decidir qué resultados pueden afectar a la MVP y cuáles deben quedar como investigación futura.

## Acciones derivadas

Todavía no se crea una acción PCS separada. La fase documental de fichas se ha
completado con ocho repositorios; la investigación queda abierta para completar
la matriz, formular la recomendación y delimitar el primer experimento técnico.

## Decisiones derivadas

No hay decisiones formales de reutilización, prototipado o descarte. Las fichas
contienen decisiones preliminares según el flujo de investigación, no decisiones
PCS ni autorizaciones de integración.

## Problemas o bloqueos

- Las referencias están verificadas a nivel de propósito general; la auditoría completa de código, actividad, calidad interna y facilidad real de integración sigue pendiente.
- La revisión documental no sustituye la ejecución de experimentos ni confirma todavía la separabilidad real de componentes.
- Existe riesgo de desviar la MVP hacia una arquitectura multiagente o hacia herramientas de CV antes de demostrar su necesidad.

## Rehidratación futura

- **Leer primero:** `docs/ideas-y-debates/investigacion-github/INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md`.
- **Retomar desde:** la matriz comparativa, usando las ocho fichas y manteniendo `noamseg/interview-coach-skill` como calibración del formato.
- **Confirmar antes de avanzar:** licencia, actividad, stack, componentes separables, coste, riesgo de desvío y experimento mínimo.
- **No inferir:** que una selección preliminar equivale a recomendación de integración.
- **Siguiente gesto recomendado:** completar la matriz comparativa y, cuando se delimite su pregunta, revisar si procede ejecutar `EXP-001-entrevista-y-storybank`.

## Trazabilidad

- Sesión relacionada: `sesion-20260705-concepto-cobertura-profesional-carrera-ai`
- Documento origen: `docs/ideas-y-debates/investigacion-github/INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md`
- Estado de proyecto relacionado: `.pcs/estado/estado-actual.md`

## Estado de la sesión

La sesión queda abierta. La calibración del flujo y del template, así como la
fase inicial de fichas, se han completado con ocho repositorios. Su objetivo
sigue siendo investigar y comparar repositorios; no autoriza por sí sola
instalaciones, forks, integración de código ni cambios metodológicos.
