# AGENTS — Memoria operativa PCS

## Propósito

Esta carpeta contiene la memoria operativa local del host `carrera-ai` dentro del Project Continuity System (PCS).

Estas instrucciones regulan cómo consultar e interpretar el contenido de `.pcs/`. Complementan el [`AGENTS.md` raíz](../AGENTS.md), que mantiene las reglas generales del repositorio, y no sustituyen el contrato canónico ni las entidades del PCS Core.

## Jerarquía de fuentes

Para rehidratar el estado del proyecto o responder sobre continuidad PCS, respetar esta precedencia:

1. `estado/estado-actual.md`: situación operativa vigente, foco, riesgos, próximos pasos y decisiones relevantes.
2. `decisiones/`: determinaciones formales vigentes, con su alcance, impacto y criterios de revisión.
3. `sesiones/`: contexto histórico, razonamiento, trazabilidad y preguntas abiertas de cada línea de trabajo.

Una sesión puede explicar por qué se llegó a una determinación, pero no sustituye al estado actual ni declara por sí sola una decisión vigente.

## Tipos de información

- **Estado vivo:** se consulta en `estado/estado-actual.md`. Resume el presente operativo y no debe deducirse únicamente de la sesión más reciente.
- **Decisión normativa:** se consulta en `decisiones/`. Solo una decisión con estado `vigente` debe tratarse como aplicable actualmente.
- **Contexto histórico:** se consulta en `sesiones/`. Puede contener alternativas descartadas, hipótesis, decisiones candidatas o información que ya no esté vigente.

Cuando exista contradicción, señalarla y resolverla consultando la fuente de mayor autoridad. No convertir un resumen histórico en estado o normativa.

## Rehidratación recomendada

Para una rehidratación PCS:

1. Aplicar primero el `AGENTS.md` raíz y estas instrucciones específicas.
2. Leer `estado/estado-actual.md`.
3. Consultar las decisiones vigentes relevantes.
4. Abrir la sesión activa o las sesiones relacionadas que el estado indique.
5. Confirmar en las fuentes originales cualquier afirmación que vaya a orientar una acción o decisión.

No cargar todas las sesiones por defecto. Tampoco asumir que la sesión modificada más recientemente representa el estado vivo.

## Actualización y trazabilidad

Cuando se cree o modifique un estado, una decisión o una sesión:

- utilizar la entidad y la plantilla canónicas correspondientes;
- mantener enlaces entre la sesión, las decisiones, las acciones y el estado afectados;
- actualizar `estado/estado-actual.md` cuando cambie el presente operativo;
- conservar las referencias históricas como tales, sin presentarlas como instrucciones vigentes.

## Exclusiones y privacidad

- No leer, recorrer, indexar, resumir, modificar ni utilizar `.tmp/` salvo autorización expresa del usuario.
- No enviar el contenido de `.pcs/` a servicios externos ni ejecutar integraciones de publicación sin autorización explícita.
- Limitar el contexto recuperado a lo necesario para la tarea.
- Tratar la información de continuidad del proyecto como información operativa que puede contener datos sensibles.

## Límites de gobernanza

- El PCS Core y su contrato canónico mantienen la autoridad normativa común.
- Este documento no modifica `hosts/hosts.yaml`, el PCS Core ni las entidades canónicas.
- No crear ni actualizar una sesión, acción, decisión o estado a partir de una inferencia sin evidencia suficiente.
- No tratar una sesión histórica como una decisión PCS ni como evidencia suficiente para cambiar el SPEC, el playbook o la metodología.

## Validación antes de responder

Antes de cerrar una respuesta sobre continuidad PCS, comprobar:

- que `estado/estado-actual.md` se ha consultado para las afirmaciones de presente;
- que las decisiones citadas existen y su estado es compatible con la afirmación;
- que las sesiones utilizadas son pertinentes y se presentan como contexto histórico;
- que la fuente citada existe y puede abrirse;
- que no se ha leído `.tmp/` ni se ha confundido una fuente histórica con una instrucción vigente.
