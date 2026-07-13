---
id: sesion-20260713-1344-integracion-operacion-graphify-carrera-ai
titulo: Integración y operación de Graphify en Carrera AI
inicio: 2026-07-13
cierre:
estado: abierta
tipo: sesion
host: carrera-ai
---

# Sesión PCS - Integración y operación de Graphify

## Contexto inmediato

El host `carrera-ai` utiliza Graphify como índice derivado para reducir la carga de contexto y dirigir consultas hacia documentos relevantes. La configuración actual mantiene tres corpus independientes:

- `.pcs/`: estado, decisiones y sesiones de continuidad PCS.
- `docs/`: SPEC, núcleo metodológico, ideas de debate, evaluación y presentación.
- `boveda-entrevista-profesional/`: documentación operativa y metodológica de la entrevista y sus artefactos relacionados.

Cada corpus tiene su propio `graphify-out/`. La separación evita mezclar documentos con finalidades, autoridades y ciclos de actualización diferentes.

## Objetivo

Dejar registrada la integración operativa de Graphify en el host, sus límites de corpus, el uso de `run-graphify.bat` como actualizador común y la decisión de utilizar Ollama como backend local para la extracción semántica.

## Capa episódica

Durante esta línea de trabajo se verificó que `run-graphify.bat` ya procesa secuencialmente `boveda-entrevista-profesional/`, `docs/` y `.pcs/`. También se crearon o actualizaron las instrucciones locales que deben orientar a las herramientas:

- `.pcs/AGENTS.md` define la jerarquía entre estado, decisiones, sesiones y grafo derivado.
- `.pcs/.graphifyignore` excluye salidas, temporales, configuración y artefactos auxiliares del propio corpus PCS.
- `docs/AGENTS.md` mantiene las reglas específicas del corpus documental metodológico.
- `docs/.graphifyignore` mantiene sus exclusiones propias.
- `AGENTS.md` raíz documenta los tres corpus, sus grafos y el papel de `run-graphify.bat`.

La extracción semántica del script utiliza `graphify extract . --backend ollama`, de modo que el modelo de IA utilizado para esa fase permanece en el entorno local a través de Ollama.

## Capa semántica

Graphify es una capa de navegación y recuperación dirigida, no una fuente normativa. La precedencia de interpretación queda establecida así:

1. El estado actual informa del presente operativo.
2. Las decisiones vigentes fijan determinaciones aplicables.
3. Las sesiones aportan contexto histórico y trazabilidad.
4. Los grafos ayudan a localizar y relacionar esas fuentes.

Las relaciones `INFERRED` y `AMBIGUOUS` deben verificarse en los documentos originales. La presencia de una relación, comunidad o nodo central no crea por sí misma una decisión, acción, requisito o cambio de estado.

## Ideas y líneas cognitivas abiertas

- Medir si el grafo PCS reduce realmente la carga de contexto inicial sin aumentar las consultas irrelevantes.
- Comparar la precisión de consultas dirigidas con la lectura manual de sesiones históricas.
- Revisar el coste de tokens y el tiempo de actualización cuando cambien sesiones, decisiones o estado.
- Decidir si los artefactos `graphify-out/` deben permanecer locales y regenerables o si alguna parte debe versionarse.
- Comprobar el comportamiento cuando Ollama no esté disponible o el grafo esté desactualizado.

## Acciones derivadas

- No se crea una acción formal en esta sesión. Las líneas abiertas anteriores quedan como criterios de revisión y no como tareas operativas hasta que se definan alcance, responsable y resultado esperado.

## Decisiones derivadas

- `DEC-20260713-1344-001-integrar-graphify-tres-corpus` queda vigente y sustituye a `DEC-20260710-2308-001-separar-corpus-graphify`, porque la decisión anterior describía únicamente dos corpus.

## Problemas o bloqueos

- La utilidad de Graphify todavía no está validada mediante una comparación controlada de recuperación y coste de contexto.
- Los grafos pueden quedar obsoletos tras cambios documentales si no se ejecuta el actualizador.
- Las inferencias del grafo pueden conectar contexto histórico con decisiones actuales de forma engañosa si no se verifica la fuente.

## Documentos afectados

- `AGENTS.md`.
- `.pcs/AGENTS.md`.
- `.pcs/.graphifyignore`.
- `.pcs/estado/estado-actual.md`.
- `.pcs/decisiones/DEC-20260710-2308-001-separar-corpus-graphify.md`.
- `.pcs/decisiones/DEC-20260713-1344-001-integrar-graphify-tres-corpus.md`.
- `docs/AGENTS.md`.
- `docs/.graphifyignore`.
- `run-graphify.bat`.

## Rehidratación futura

- **Dónde quedó el trabajo:** Graphify está organizado en tres corpus independientes y se actualiza mediante `run-graphify.bat` con extracción semántica local a través de Ollama.
- **Leer primero:** `.pcs/estado/estado-actual.md`, `DEC-20260713-1344-001-integrar-graphify-tres-corpus.md`, `.pcs/AGENTS.md` y `AGENTS.md`.
- **Líneas abiertas a retomar:** medir utilidad, coste, precisión, obsolescencia y necesidad real de consultas transversales.
- **Riesgos de malinterpretación:** no tratar el grafo como fuente normativa, no confundir sesiones históricas con estado vivo y no mezclar corpus sin una decisión posterior.
- **Siguiente gesto recomendado:** ejecutar una validación controlada de consultas PCS con y sin grafo, registrando fuentes recuperadas, tokens y correcciones necesarias.

## Trazabilidad

- Sesión de origen: nueva sesión operativa para Graphify en `carrera-ai`.
- Decisión derivada: `DEC-20260713-1344-001-integrar-graphify-tres-corpus.md`.
- Estado relacionado: `.pcs/estado/estado-actual.md`.
- Actualizador: `run-graphify.bat`.
- Estado de la sesión: abierta, pendiente de revisión de utilidad.
- PCS Core: no modificado.
