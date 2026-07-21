---
id: DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo
titulo: Crear una rama operativa de búsqueda de empleo dentro de Carrera AI
estado: vigente
fecha_registro: 2026-07-21
fecha_adopcion: 2026-07-21
fecha_vigencia: 2026-07-21
tipo: decision
host: carrera-ai
---

# DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo — Crear una rama operativa de búsqueda de empleo dentro de Carrera AI

## Enunciado de la decisión

Se crea, dentro de Carrera AI, una rama operativa de búsqueda de empleo destinada a disponer con rapidez de CV adaptados, cartas de presentación y candidaturas revisables para ofertas concretas.

La rama reutiliza la información profesional disponible, en especial [[datos-core-busqueda]], pero queda separada de la investigación metodológica de entrevista. No altera el SPEC, los playbooks ni los criterios de validación de la entrevista profesional.

La ejecución se organizará de forma progresiva: preparación de documentos a partir del texto de una oferta; asistencia en Chrome sobre páginas abiertas por la persona responsable; y, solo tras validación posterior, acceso mediante skills o conectores a portales priorizados. Toda candidatura requerirá aprobación humana por lote antes de enviarse.

## Motivo

La búsqueda de empleo tiene una necesidad inmediata de tiempo y resultados prácticos que no debe quedar bloqueada por la validación completa de Carrera AI como investigación metodológica. La rama operativa permite convertir los aprendizajes pertinentes en activos de candidatura sin exigir que la entrevista profesional esté finalizada.

## Contexto

La tensión entre la continuidad de Carrera AI y la búsqueda activa de empleo quedó registrada en [[sesion-20260721-1651-tension-carrera-ai-y-busqueda-de-trabajo]]. La persona responsable decidió mantener ambas líneas dentro del mismo host con fronteras explícitas, en vez de crear un proyecto independiente o detener la investigación de entrevista.

## Alternativas descartadas

- Pausar Carrera AI por completo para dedicar todo el tiempo a buscar empleo.
- Mantener solo la investigación metodológica y posponer los CV adaptados y las candidaturas.
- Crear un proyecto independiente fuera de `carrera-ai` para la búsqueda de empleo.
- Integrar la preparación de candidaturas dentro del alcance normativo de la entrevista y sus playbooks.

## Impacto esperado

- Reducir el tiempo necesario para preparar documentos de candidatura adecuados a una oferta.
- Mantener una fuente factual única y revisable para las tres orientaciones profesionales disponibles.
- Conservar la investigación de entrevista como línea metodológica independiente, sin cambiar sus objetivos ni sus criterios experimentales.
- Evitar candidaturas duplicadas y automatizaciones sin aprobación humana.

## Alcance

La decisión autoriza la documentación y la ejecución progresiva de la rama operativa bajo `boveda-entrevista-profesional/busqueda-empleo/`.

No autoriza modificar el SPEC ni los playbooks de entrevista, declarar competencias no evidenciadas, crear un proyecto externo, enviar candidaturas sin aprobación por lote, ni almacenar datos personales innecesarios en la matriz profesional.

## Relaciones

- Sesión de origen: [[sesion-20260721-1651-tension-carrera-ai-y-busqueda-de-trabajo]].
- Acción de materialización inicial: [[ACC-20260721-1651-001-activar-rama-operativa-busqueda-empleo-fase-1]].
- Estado operativo: [[estado-actual]].
- Decisión anterior o sustituida: ninguna.

## Revisión futura

Revisar esta decisión si la rama operativa desplaza de forma indebida la investigación de entrevista, si no entrega utilidad práctica en candidaturas, si plantea riesgos de privacidad no resueltos o antes de activar acceso autónomo a nuevos portales de empleo.
