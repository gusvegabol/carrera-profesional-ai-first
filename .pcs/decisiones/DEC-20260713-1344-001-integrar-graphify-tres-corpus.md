---
id: DEC-20260713-1344-001-integrar-graphify-tres-corpus
titulo: Mantener tres corpus Graphify y actualización semántica local con Ollama
estado: sustituida
fecha_registro: 2026-07-13
fecha_adopcion: 2026-07-13
fecha_vigencia: 2026-07-13
fecha_sustitucion: 2026-07-17
tipo: decision
host: carrera-ai
sesion_origen: sesion-20260713-1344-integracion-operacion-graphify-carrera-ai
decision_sustituta: DEC-20260717-1058-001-retirada-graphify-carrera-ai
---

# DEC-20260713-1344-001-integrar-graphify-tres-corpus — Mantener tres corpus Graphify y actualización semántica local con Ollama

> Referencia histórica: esta decisión quedó sustituida el 2026-07-17 por `DEC-20260717-1058-001-retirada-graphify-carrera-ai`. El contenido posterior describe únicamente la operación vigente entre su adopción y su sustitución.

## Decisión

Graphify se mantendrá como tres corpus documentales independientes, cada uno con su propio grafo:

- `.pcs/`, con estado, decisiones y sesiones PCS.
- `docs/`, con SPEC, núcleo metodológico, ideas de debate, evaluación y presentación.
- `boveda-entrevista-profesional/`, con documentación operativa y metodológica de la entrevista y sus artefactos relacionados.

`run-graphify.bat` es el actualizador operativo común y ejecuta Graphify secuencialmente en esas tres carpetas. La extracción semántica se realizará mediante el backend local de Ollama (`--backend ollama`).

Los grafos y sus informes son artefactos derivados para navegación y recuperación dirigida. Las fuentes originales conservan la autoridad y deben verificarse antes de utilizarlas para afirmar, decidir o cambiar el estado del proyecto.

## Motivo

Los tres corpus tienen finalidades, autoridades y ritmos de cambio diferentes. Separarlos reduce relaciones artificiales, evita contaminar las comunidades y permite seleccionar el contexto adecuado para cada consulta.

El uso de un único script evita que cada carpeta se actualice con comandos o backends distintos. El backend local de Ollama mantiene la extracción semántica dentro del entorno de trabajo y hace reproducible el procedimiento de referencia.

## Contexto

La decisión anterior `DEC-20260710-2308-001-separar-corpus-graphify` formalizó la separación de `docs/` y `boveda-entrevista-profesional/`. La incorporación operativa de `.pcs/` hace necesario sustituirla para que la decisión PCS coincida con el script y con la configuración actual de los tres corpus.

`.pcs/AGENTS.md`, `.pcs/.graphifyignore`, `docs/AGENTS.md`, `docs/.graphifyignore` y `AGENTS.md` raíz documentan los límites, exclusiones y reglas de interpretación de cada corpus.

## Alternativas descartadas

- Mantener únicamente los grafos de `docs/` y `boveda-entrevista-profesional/`, dejando `.pcs/` fuera de la navegación derivada.
- Ejecutar Graphify sobre la raíz completa del repositorio y fusionar los tres ámbitos.
- Actualizar cada corpus con scripts, backends o criterios diferentes.
- Tratar `graphify-out/`, sus comunidades o sus inferencias como sustitutos del estado, las decisiones o las fuentes documentales.

## Impacto esperado

- Las herramientas pueden consultar el grafo PCS para localizar estado relacionado, decisiones y sesiones, pero deben respetar la precedencia documental.
- `run-graphify.bat` se convierte en la entrada operativa reproducible para actualizar los tres corpus.
- La extracción semántica requiere que Ollama y el modelo local configurado estén disponibles.
- Los cambios documentales pueden dejar los grafos obsoletos hasta la siguiente ejecución del script.
- Los grafos no modifican el SPEC, el playbook, el núcleo metodológico ni el alcance normativo de PCS.
- Las consultas transversales deben componer resultados de corpus separados y conservar la procedencia; no deben fusionar grafos silenciosamente.

## Alcance

Esta decisión cubre únicamente la organización, actualización y uso de los tres corpus Graphify. No autoriza cambios en la metodología de entrevista, el SPEC, el playbook de profundidad ni las entidades del PCS Core.

El grafo PCS puede indexar `estado/`, `decisiones/` y `sesiones/`, pero `estado/estado-actual.md` y las decisiones vigentes mantienen su autoridad propia. Las relaciones `INFERRED` y `AMBIGUOUS` deben verificarse en la fuente original.

## Relaciones

- Sesión origen: `sesion-20260713-1344-integracion-operacion-graphify-carrera-ai.md`.
- Estado afectado: `.pcs/estado/estado-actual.md`.
- Acciones afectadas: ninguna acción formal abierta.
- Decisión anterior sustituida: `DEC-20260710-2308-001-separar-corpus-graphify`.

## Revisión futura

La decisión deberá revisarse cuando exista evidencia suficiente para comparar precisión de recuperación, reducción de contexto inicial, coste de tokens, tiempo de actualización, obsolescencia, relaciones irrelevantes y necesidad real de consultas transversales.

También deberá revisarse si Ollama deja de ser viable en el entorno local o si la extracción semántica exige cambiar de backend. Ese cambio no debe hacerse silenciosamente en el script.

## Trazabilidad

- `run-graphify.bat`.
- `AGENTS.md`.
- `.pcs/AGENTS.md`.
- `.pcs/.graphifyignore`.
- `docs/AGENTS.md`.
- `docs/.graphifyignore`.
- `.pcs/estado/estado-actual.md`.
- `.pcs/sesiones/sesion-20260713-1344-integracion-operacion-graphify-carrera-ai.md`.
