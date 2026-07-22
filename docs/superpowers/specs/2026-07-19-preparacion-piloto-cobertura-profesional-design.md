# Preparación del piloto real de cobertura profesional

> Documento de diseño y contrato provisional. No adopta la doble pasada como método formal ni sustituye las decisiones PCS pendientes.

## Propósito

Preparar una prueba real y controlada de la arquitectura de doble pasada para comprobar si la cobertura panorámica y la inmersión selectiva producen un mapa profesional útil, honesto y revisable por la persona entrevistada.

La prueba usará como capa de orquestación el [Playbook de cobertura profesional v1.0.0](../../metodologia/playbooks/PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_0.md) y, cuando se active una inmersión, el [Playbook de entrevista profesional v1.3.2](../../metodologia/playbooks/PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA.md).

## Estado y límites

- La doble pasada se probará como orientación experimental, no como metodología adoptada.
- La prueba no certificará competencias ni validará correspondencias ESCO.
- El mapa resultante será parcial por definición y deberá declarar sus límites.
- La persona entrevistada conservará control sobre el ritmo, la selección de zonas, las correcciones y la información que se incorpore a la salida.
- El piloto no intentará validar simultáneamente toda la arquitectura futura de producto, visualizaciones, automatización o clasificación.

## Pregunta principal

¿Puede una secuencia de panorámica abierta, selección consciente de una o dos zonas, prevalidación ligera e inmersión profunda producir un mapa inicial razonable de la trayectoria profesional sin crear falsa cobertura ni una carga conversacional excesiva?

## Preguntas secundarias

1. ¿La panorámica descubre zonas relevantes que no aparecerían mediante entrevistas de profundidad aisladas?
2. ¿La persona entiende y acepta la selección de una zona para profundizar?
3. ¿El mapa distingue de forma útil entre zonas exploradas, candidatas, parciales y pendientes?
4. ¿La combinación de cobertura v1.0.0 y profundidad v1.3.2 evita inferencias no respaldadas?
5. ¿Los registros permiten revisar, corregir y reanudar el trabajo sin inventar contexto?

## Secuencia provisional

### Antes de la primera sesión

1. Explicar el propósito experimental, los límites y el control de la persona.
2. Confirmar qué información puede conservarse y qué información debe excluirse.
3. Crear el registro del entrevistado y un mapa inicial vacío.
4. Confirmar la convención de identificadores específica del piloto.
5. Preparar una copia de trabajo de las plantillas, sin modificar las plantillas canónicas mientras la convención siga en debate.

Los templates canónicos se encuentran en `docs/templates/artefactos-cobertura-profesional/`:

- [TEMPLATE_ENTREVISTADO.md](../../templates/artefactos-cobertura-profesional/TEMPLATE_ENTREVISTADO.md)
- [TEMPLATE_MAPA.md](../../templates/artefactos-cobertura-profesional/TEMPLATE_MAPA.md)
- [TEMPLATE_SESION.md](../../templates/artefactos-cobertura-profesional/TEMPLATE_SESION.md)
- [TEMPLATE_CHECKPOINT.md](../../templates/artefactos-cobertura-profesional/TEMPLATE_CHECKPOINT.md)
- [TEMPLATE_INMERSION.md](../../templates/artefactos-cobertura-profesional/TEMPLATE_INMERSION.md)
- [TEMPLATE_COMPETENCIA.md](../../templates/artefactos-cobertura-profesional/TEMPLATE_COMPETENCIA.md)
- [TEMPLATE_TRANSCRIPCION.md](../../templates/artefactos-cobertura-profesional/TEMPLATE_TRANSCRIPCION.md)
- [TEMPLATE_EVALUACION_PILOTO.md](../../templates/artefactos-cobertura-profesional/TEMPLATE_EVALUACION_PILOTO.md)

Los artefactos creados a partir de ellos se guardan en `boveda-entrevista-profesional/artefactos-cobertura-profesional/`; la carpeta de templates no debe contener registros de personas ni resultados de entrevistas.

### Durante cada sesión

1. Registrar el tiempo que la persona declara tener y su permiso para detenerse.
2. Recuperar el mapa previo, si existe, y declarar sus límites.
3. Realizar la panorámica abierta sin forzar una cronología.
4. Registrar las zonas candidatas sin convertirlas en competencias.
5. Pedir a la persona que seleccione la zona que desea mirar con más detalle.
6. Aplicar `PATRON_STAR_SIMPLE` a una o dos candidatas como máximo.
7. Activar como máximo una inmersión completa con el playbook v1.3.2.
8. Crear o actualizar el mapa, la sesión, la inmersión, el checkpoint o la competencia que corresponda.
9. Cerrar separando hechos, evidencias, inferencias, límites y zonas pendientes.

### Después de cada sesión

1. Revisar el registro con la persona entrevistada.
2. Registrar correcciones, rechazos, omisiones voluntarias y dudas.
3. Actualizar la advertencia de límite del mapa.
4. Registrar incidencias del modelo o del flujo sin convertirlas automáticamente en cambios metodológicos.

## Artefactos mínimos

El piloto necesita estos artefactos, todos dentro del área de evidencias o trabajo experimental, no en `.pcs/`:

- un registro de entrevistado;
- un mapa de cobertura vivo;
- una sesión por encuentro;
- un checkpoint solo si una inmersión queda parcial;
- una inmersión por activación de profundidad;
- una competencia solo cuando la evidencia lo justifique;
- una transcripción verbatim por sesión, para permitir la auditoría turno a turno;
- una nota de evaluación del piloto al terminar.

Los ocho templates canónicos anteriores cubren estos tipos. El template de competencia incluye las validaciones factual, de competencia y de valor profesional. El template de transcripción conserva los turnos literales de la sesión. El template de evaluación estructura la nota consolidada del piloto y sus incidencias. La nomenclatura de fichero contiene dos variantes históricas (`ZONA_<n>` y una propuesta basada en identificadores de entrevistado, mapa, zona e intento). Para esta prueba se deberá escoger una sola convención antes de crear el primer artefacto; esa elección no se considerará adopción global.

## Criterios de evaluación

### Cobertura

- La persona identifica zonas relevantes que aparecen en el mapa.
- El mapa hace visibles zonas pendientes o poco exploradas.
- La salida no presenta una zona profunda como representación de toda la trayectoria.

### Evidencia y prudencia

- Cada competencia propuesta remite a una inmersión y a evidencia concreta.
- Las inferencias mantienen alcance, calidad y límites.
- La persona puede aceptar, corregir, rechazar o dejar pendiente una formulación.

### Experiencia y control

- La persona entiende por qué se propone profundizar en una zona.
- Puede cambiar de zona o detenerse sin justificar la decisión.
- La carga y el ritmo son aceptables para la persona.

### Continuidad

- Una zona parcial queda registrada sin aparentar estar explorada.
- La reanudación informa de lo que se sabe y de lo que no se sabe.
- El sistema no infiere duración de pausas ni completa silencios con suposiciones.

### Utilidad de salida

- La persona considera útil el mapa inicial.
- La salida diferencia hechos, evidencias, inferencias y pendientes.
- El resultado permite decidir qué explorar después.

## Evidencias que deben recogerse

Por cada sesión se conservarán:

- zonas mencionadas y estado asignado;
- candidatas prevalidadas y motivo de selección;
- activación o no de inmersión;
- correcciones y rechazos de la persona;
- señales de carga, confusión o pérdida de control;
- incidencias del modelo;
- límites reconocidos al cierre.

No se interpretará una formulación aceptada sin corrección como prueba suficiente de validez; la fluidez o el asentimiento pueden ocultar errores.

## Riesgos y respuestas previstas

| Riesgo | Respuesta provisional |
| --- | --- |
| Colapsar responsabilidades distintas en una sola zona | Preguntar si cada responsabilidad merece exploración independiente antes de profundizar. |
| Filtrar vocabulario interno | Usar lenguaje natural con la persona y reservar `zona`, `mapa`, `checkpoint` e `inmersión` para los registros. |
| Generalizar una tarea al resto de una etapa | Exigir evidencia específica antes de formular una competencia sobre otra responsabilidad. |
| Confundir mapa parcial con cobertura completa | Mantener una advertencia de límite visible en cada cierre. |
| Perder una inmersión interrumpida | Crear checkpoint antes de cerrar una zona parcial. |
| Fallo de generación del modelo | Detener la elaboración de conclusiones, registrar la incidencia y revisar con la persona qué parte sigue siendo fiable. |

## Condiciones de salida del piloto

El piloto podrá cerrarse cuando exista suficiente material para responder a la pregunta principal y la persona haya revisado la salida. El cierre deberá indicar una de estas conclusiones:

- la arquitectura es suficientemente útil para un siguiente piloto;
- la arquitectura requiere cambios concretos antes de repetir la prueba;
- la arquitectura no aporta valor suficiente en su forma actual.

Ninguna de estas conclusiones convierte por sí sola la propuesta en metodología formal; esa decisión requiere una revisión posterior.

## Decisiones que requieren al responsable

Antes de crear el primer artefacto real, quedan pendientes de autorización humana:

1. autorizar la ejecución experimental del piloto;
2. identificar a la persona participante o confirmar que el primer caso será el propio responsable;
3. aprobar el alcance de conservación y exclusión de datos;
4. escoger la convención de identificadores del piloto;
5. confirmar quién revisará la salida y con qué criterio se considerará útil.

## Siguiente gesto

Una vez autorizados esos cinco puntos, se puede preparar el paquete concreto del primer caso y abrir la primera sesión de cobertura. Hasta entonces, este documento funciona como protocolo de preparación y no como registro de una entrevista real.
