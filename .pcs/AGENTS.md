# AGENTS — Memoria operativa PCS y grafo Graphify

## Propósito

Esta carpeta contiene la memoria operativa local del host `carrera-ai` dentro del Project Continuity System (PCS).

Estas instrucciones regulan cómo consultar e interpretar el contenido de `.pcs/` y cómo utilizar, si se crea, un grafo Graphify específico de este corpus. Complementan el [`AGENTS.md` raíz](../AGENTS.md), que mantiene las reglas generales del repositorio, y no sustituyen el contrato canónico ni las entidades del PCS Core.

La política de Graphify para `docs/` es independiente y está documentada en [`docs/AGENTS.md`](../docs/AGENTS.md). Este documento no amplía ni modifica el corpus autorizado para `docs/`.

## Jerarquía de fuentes

Para rehidratar el estado del proyecto o responder sobre continuidad PCS, respetar esta precedencia:

1. `estado/estado-actual.md`: situación operativa vigente, foco, riesgos, próximos pasos y decisiones relevantes.
2. `decisiones/`: determinaciones formales vigentes, con su alcance, impacto y criterios de revisión.
3. `sesiones/`: contexto histórico, razonamiento, trazabilidad y preguntas abiertas de cada línea de trabajo.
4. `graphify-out/`: índice derivado para localizar documentos y relaciones; nunca fuente normativa.

Una sesión puede explicar por qué se llegó a una determinación, pero no sustituye al estado actual ni declara por sí sola una decisión vigente. Una relación del grafo tampoco altera la precedencia documental.

## Tipos de información

- **Estado vivo:** se consulta en `estado/estado-actual.md`. Resume el presente operativo y no debe deducirse únicamente de la sesión más reciente.
- **Decisión normativa:** se consulta en `decisiones/`. Solo una decisión con estado `vigente` debe tratarse como aplicable actualmente.
- **Contexto histórico:** se consulta en `sesiones/`. Puede contener alternativas descartadas, hipótesis, decisiones candidatas o información que ya no esté vigente.
- **Índice derivado:** se consulta en `graphify-out/`, si existe. Sirve para encontrar fuentes, no para reemplazarlas.

Cuando exista contradicción, señalarla y resolverla consultando la fuente de mayor autoridad. No convertir un resumen histórico ni una inferencia del grafo en estado o normativa.

## Uso de Graphify en `.pcs/`

Si se ejecuta Graphify sobre `.pcs/`, debe tratarse como un corpus separado de `docs/` y de `boveda-entrevista-profesional/`. No se debe generar un grafo conjunto mezclando esos corpus, porque tienen finalidades y autoridades documentales diferentes.

La salida esperada, si se configura, es `graphify-out/` dentro de `.pcs/`. Sus archivos son regenerables y derivados. No deben editarse manualmente ni utilizarse como fuente de verdad.

Graphify debe utilizarse para:

- localizar sesiones relacionadas con una decisión o un tema;
- descubrir relaciones de trazabilidad entre estado, decisiones y sesiones;
- seleccionar qué documentos históricos merece la pena abrir;
- realizar consultas dirigidas con un presupuesto de contexto limitado.

Graphify no debe utilizarse para:

- decidir cuál es el estado vivo del proyecto sin leer `estado/estado-actual.md`;
- declarar vigente una decisión;
- crear acciones, decisiones, requisitos o cambios de estado;
- sustituir la lectura de la fuente cuando se afirme algo concreto;
- mezclar automáticamente la memoria PCS con otros corpus del repositorio.

## Interpretación de relaciones

Conservar las etiquetas de confianza que proporcione Graphify:

- `EXTRACTED`: relación explícita en una fuente.
- `INFERRED`: relación razonable propuesta por la herramienta, pendiente de confirmación en la fuente.
- `AMBIGUOUS`: relación incierta que debe mantenerse como tal hasta resolverla documentalmente.

Toda afirmación basada en `INFERRED` o `AMBIGUOUS` debe verificarse abriendo el documento de origen. Incluso una relación `EXTRACTED` debe interpretarse dentro del documento y de su estado de vigencia.

## Rehidratación recomendada

Para una rehidratación PCS:

1. Aplicar primero el `AGENTS.md` raíz y estas instrucciones específicas.
2. Leer `estado/estado-actual.md`.
3. Consultar las decisiones vigentes relevantes.
4. Abrir la sesión activa o las sesiones relacionadas que el estado indique.
5. Utilizar Graphify, si existe, para localizar contexto histórico adicional y reducir lecturas innecesarias.
6. Confirmar en las fuentes originales cualquier afirmación que vaya a orientar una acción o decisión.

No cargar todas las sesiones por defecto. Tampoco asumir que la sesión modificada más recientemente representa el estado vivo.

## Actualización y trazabilidad

Cuando se cree o modifique un estado, una decisión o una sesión:

- actualizar el grafo PCS cuando exista y la ejecución esté autorizada;
- preferir una actualización incremental para cambios documentales ordinarios;
- reservar una regeneración completa para cambios estructurales o cuando el grafo no exista;
- revisar el informe, las fuentes detectadas, las relaciones usadas y el coste de tokens;
- confirmar que el grafo no ha indexado su propia salida;
- corregir la fuente original y regenerar el grafo, nunca editar manualmente sus artefactos.

Si el grafo no está actualizado, declararlo antes de utilizarlo. La existencia de `graphify-out/` no demuestra que refleje la versión actual de `.pcs/`.

## Exclusiones y privacidad

- No leer, recorrer, indexar, resumir, modificar ni utilizar `.tmp/` salvo autorización expresa del usuario.
- Excluir `graphify-out/` y los archivos de configuración de Graphify del propio corpus cuando se configure su ejecución.
- No enviar el contenido de `.pcs/` a servicios externos ni ejecutar integraciones de publicación sin autorización explícita.
- Limitar el contexto recuperado a lo necesario para la tarea.
- Tratar la información de continuidad del proyecto como información operativa que puede contener datos sensibles.

## Límites de gobernanza

- El PCS Core y su contrato canónico mantienen la autoridad normativa común.
- Este documento no modifica `hosts/hosts.yaml`, el PCS Core ni las entidades canónicas.
- No crear ni actualizar una sesión, acción, decisión o estado solo porque Graphify sugiera una relación.
- No tratar el grafo como una decisión PCS ni como evidencia suficiente para cambiar el SPEC, el playbook o la metodología.
- Las reglas de corpus de `docs/` siguen perteneciendo a `docs/AGENTS.md` y a la decisión PCS que las formaliza.

## Validación antes de responder

Antes de cerrar una respuesta basada en el grafo PCS, comprobar:

- que `estado/estado-actual.md` se ha consultado para las afirmaciones de presente;
- que las decisiones citadas existen y su estado es compatible con la afirmación;
- que las sesiones utilizadas son pertinentes y se presentan como contexto histórico;
- que las relaciones `INFERRED` y `AMBIGUOUS` han sido verificadas o se mantienen explícitamente como incertidumbre;
- que la fuente citada existe y puede abrirse;
- que no se ha leído `.tmp/` ni se ha confundido una salida derivada con una fuente normativa;
- que el coste y el alcance del contexto recuperado son proporcionales a la pregunta.
