# AGENTS.md — Documentación metodológica y grafo Graphify

## Propósito

Esta carpeta contiene la documentación funcional y metodológica de `carrera-ai`, así como las ideas de debate sobre la entrevista de cobertura profesional.

El grafo generado por Graphify debe servir como índice navegable y capa de recuperación de contexto. No sustituye los documentos fuente ni convierte sus inferencias en decisiones del proyecto.

Estas instrucciones se aplican a `docs/` y a sus subcarpetas, salvo que exista otro `AGENTS.md` más específico.

## Separación de corpus

Graphify se ejecuta por corpus documental independiente y no sobre la raíz completa del repositorio. La entrada operativa vigente es `run-graphify.bat`, que mantiene separados estos dos corpus:

- `boveda-entrevista-profesional/`: documentación operativa y metodológica de la entrevista y sus artefactos relacionados.
- `docs/`: SPEC funcional, núcleo metodológico, ideas de debate, evaluación y presentación.

Esta separación es intencionada: cada carpeta tiene una finalidad documental distinta. Mezclarlas produciría relaciones artificiales, comunidades contaminadas y recuperación de contexto irrelevante. Si en el futuro se necesitan preguntas que crucen ambos corpus, deben resolverse mediante composición o consultas explícitas entre grafos, no mediante una fusión silenciosa.

La decisión PCS que fija este límite es [`DEC-20260710-2308-001-separar-corpus-graphify`](../.pcs/decisiones/DEC-20260710-2308-001-separar-corpus-graphify.md). Su utilidad deberá revisarse más adelante con evidencia de uso, sin cambiar el límite por inferencia de una herramienta.

## Fuentes y jerarquía

Para consultas sobre la metodología de entrevista, priorizar en este orden:

1. `DOCUMENTO_SPEC_CARRERA_AI.md` para objetivos y límites funcionales.
2. `Núcleo Metodológico del Playbook/` para fundamentos, técnicas y marcos metodológicos.
3. `Ideas debate - como afrontar entrevista cobertura profesional/` para propuestas, evaluación y presentación del enfoque.
4. `graphify-out/GRAPH_REPORT.md`, `graphify-out/graph.json` y el HTML generado por Graphify como índices derivados y ayudas de navegación.

Si existe una contradicción, prevalece la fuente documental de mayor autoridad y debe señalarse la contradicción. El grafo no resuelve por sí solo conflictos metodológicos.

## Uso de Graphify

La vía operativa oficial es ejecutar `run-graphify.bat`, que actualiza y extrae los dos corpus de forma separada. Para consultas acotadas sobre este corpus, ejecutar Graphify desde esta carpeta o indicarle explícitamente `docs/`. La salida esperada se conserva en:

```text
docs/graphify-out/
```

Comandos habituales, ejecutados desde `docs/`:

```text
cd docs
graphify query "pregunta concreta"
graphify query "¿Qué enfoque cubre mejor las trayectorias no lineales?"
graphify query "¿Qué evidencia debe conservar una competencia candidata?" --budget 1500
graphify explain "Doble pasada"
graphify path "Doble pasada" "Evidencia conductual"
```

Antes de la primera ejecución, comprobar que `.graphifyignore` excluye `graphify-out/` y los artefactos auxiliares que no deben entrar en el corpus. No indexar la salida del propio grafo como si fuera documentación fuente.

Usar la ejecución definida en `run-graphify.bat` para la generación y actualización de los corpus autorizados. Reservar una ejecución completa para cambios estructurales o cuando el grafo no exista. Si un corpus supera los límites de tamaño que Graphify indique, detenerse: no seleccionar ni añadir subcarpetas fuera del alcance aprobado sin revisar primero la decisión PCS y el script de ejecución.

## Cómo consultar con poco contexto

Para responder a una pregunta metodológica o de debate:

1. Formular una consulta específica con `graphify query`, `graphify explain` o `graphify path`.
2. Leer primero el subgrafo, las comunidades y las fuentes que Graphify devuelva.
3. Abrir únicamente los documentos fuente necesarios para confirmar el razonamiento.
4. Citar el archivo y la ubicación de origen cuando se afirme algo concreto.
5. Indicar si la respuesta procede de una relación `EXTRACTED`, `INFERRED` o `AMBIGUOUS`.

No cargar de entrada toda la carpeta `Núcleo Metodológico del Playbook/` ni todas las ideas si la pregunta puede resolverse mediante una consulta acotada. Ampliar el contexto cuando el informe del grafo muestre conexiones insuficientes, ambiguas o contradictorias.

## Reglas de interpretación

- `EXTRACTED` significa que la relación aparece explícitamente en una fuente.
- `INFERRED` significa que Graphify propone una relación razonable, pero debe verificarse en la fuente antes de tratarla como hecho.
- `AMBIGUOUS` significa que existe incertidumbre y no debe ocultarse ni resolverse por intuición.
- Las comunidades y los nodos centrales ayudan a orientarse; no establecen autoridad metodológica.
- El informe de evaluación de las ideas es una recomendación debatible, no una decisión canónica del playbook ni una actualización automática del SPEC.
- ESCO debe tratarse como correspondencia candidata posterior y revisable, nunca como prueba individual de competencia o certificación.
- Una relación del grafo no crea por sí misma una acción, decisión, requisito funcional o cambio de estado PCS.

## Actualización y trazabilidad

Cuando se creen o modifiquen documentos metodológicos o ideas de debate:

- actualizar Graphify con `--update` cuando el grafo exista;
- comprobar que el informe, el JSON y el HTML reflejan el corpus vigente;
- revisar las diferencias relevantes antes de usar el grafo en una respuesta;
- conservar en la respuesta la distinción entre fuente original y artefacto derivado;
- no sobrescribir manualmente `graph.json`, `GRAPH_REPORT.md` ni el HTML generado para corregir una fuente: corregir la fuente y regenerar.

Los artefactos de Graphify son derivados y pueden regenerarse. Si se incorporan al control de versiones, deben mantenerse como productos reproducibles, no como fuentes normativas.

## Límites y exclusiones

- No leer, indexar, modificar ni usar `.tmp/` salvo autorización expresa del usuario.
- No modificar `DOCUMENTO_SPEC_CARRERA_AI.md` por una inferencia del grafo.
- No convertir un resumen generado por Graphify en una decisión metodológica sin revisar sus fuentes.
- No ocultar el coste de tokens, el tamaño del corpus ni los avisos de auditoría de Graphify.
- No presentar conexiones sorprendentes como descubrimientos confirmados sin evidencia documental.
- No tratar `docs/AGENTS.md` como fuente metodológica; es una instrucción operativa para las herramientas.

## Validación antes de responder

Antes de cerrar una consulta basada en Graphify, comprobar:

- que el grafo corresponde a la versión actual de los documentos;
- que la fuente citada existe y se puede abrir;
- que las relaciones usadas tienen tipo y nivel de confianza explícitos;
- que no se ha confundido una inferencia con un hecho;
- que se ha mantenido la separación entre metodología, propuesta, decisión y estado PCS;
- que la respuesta puede rastrearse desde el resultado del grafo hasta el documento fuente.
