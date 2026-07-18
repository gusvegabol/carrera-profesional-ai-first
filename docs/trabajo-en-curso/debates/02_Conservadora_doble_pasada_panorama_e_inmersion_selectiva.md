# Idea conservadora - Doble pasada: panorama e inmersión selectiva

## Tesis

La cobertura de toda una vida profesional y la obtención de evidencia conductual son tareas distintas. Intentar lograr ambas con la misma intensidad en cada etapa convierte la entrevista en un interrogatorio o deja la trayectoria en una lista superficial. Esta propuesta las separa en dos pasadas coordinadas:

1. Un **panorama abierto** que registra toda la trayectoria y sus zonas de incertidumbre.
2. Una **inmersión selectiva y breve** en uno o dos episodios con potencial explicativo, usando preguntas conductuales flexibles.

El resultado no pretende certificar competencias. Pretende crear una primera versión útil del perfil: amplia, honesta sobre lo pendiente y suficientemente evidenciada en algunos puntos para comprobar que la IA puede traducir experiencia vivida a valor profesional.

## Problema que resuelve

Una entrevista de cobertura no debe transformarse en una sesión de profundidad sobre cada empleo. El documento de especificación pide reconstruir trayectoria, herramientas, experiencias significativas, uso de IA, preferencias y restricciones; pero también exige que cada competencia tenga evidencia y que la persona pueda validar o rechazar inferencias. [Especificación de Carrera AI](../DOCUMENTO_SPEC_CARRERA_AI.md)

La tensión es real: el barrido completo favorece amplitud, mientras que las técnicas conductuales favorecen detalle. La doble pasada hace visible esa tensión y evita prometer que todas las experiencias tendrán la misma calidad de evidencia.

## Primera pasada: panorama conversacional

La IA invita a recorrer libremente la trayectoria a partir de los recuerdos que la persona elija. Puede proponer categorías de ayuda, pero no una secuencia obligatoria: empleos y actividades, formación, cambios, simultaneidades, interrupciones, proyectos, trabajo informal o familiar, herramientas, responsabilidades y contexto actual.

Su tarea es capturar una ficha ligera por bloque, no obtener STAR completo. Una ficha panorámica contiene: nombre de la etapa según la persona, periodo aproximado, contexto, papel desempeñado, actividades principales, herramientas citadas, cambio o aprendizaje relevante, evidencia mencionada y preguntas pendientes.

La IA debe dejar claro que «no recuerdo» y «no quiero hablar de esto» son respuestas válidas y distintas. También debe poder registrar que un periodo parece relevante pero no desea detallarse ahora.

## Segunda pasada: inmersión que la persona controla

Al finalizar el panorama, la IA ofrece una selección transparente de posibles episodios para profundizar. No elige en secreto ni presenta su elección como diagnóstico: explica qué puede aportar cada opción y la persona escoge, modifica o rechaza la propuesta.

Los criterios posibles son:

- Un episodio que explique una transición entre sectores o funciones.
- Una situación donde hubo responsabilidad, dificultad, decisión o aprendizaje.
- Una experiencia poco formalizada que podría quedar invisible en un CV.
- Un hecho que aclare una herramienta, una práctica de IA o una preferencia actual.

La profundización usa STAR simple: situación, tarea o reto, acción propia y resultado o aprendizaje. Si no hay un resultado cuantificable, se puede recoger una consecuencia observable, una decisión tomada o un aprendizaje reconocido. Si tampoco existe, el episodio conserva valor narrativo, pero no se usa como evidencia fuerte de una competencia.

## Gestión de respuestas no lineales

Las dos pasadas son lógicas de captura, no dos bloques rígidos de conversación. Si durante el panorama la persona cuenta con detalle un episodio importante, la IA puede aprovecharlo como inmersión solo si pide permiso. Si durante una inmersión aparece otra experiencia, la añade al mapa panorámico sin forzar el retorno inmediato.

La IA conserva tres listas visibles o verbalizables: `recogido`, `por explorar` y `pendiente por decisión de la persona`. Esto permite volver a un asunto sin fingir memoria perfecta ni perder una asociación espontánea.

Ejemplo de intervención adecuada: «Lo que cuentas sobre el negocio propio parece explicar también por qué después preferiste entornos más estructurados. Puedo anotarlo como posible conexión y, si quieres, volver luego a cómo era el trabajo autónomo en el día a día.»

## Adaptación de los métodos base a una IA

BEI y STAR aportan disciplina para pedir hechos, acciones y resultados; no autorizan a la IA a comportarse como evaluador humano. Por ello, la IA debe:

- Formular una pregunta a la vez y permitir respuestas en el lenguaje de la persona.
- Distinguir entre una síntesis propia y palabras atribuidas al entrevistado.
- Pedir confirmación antes de convertir un episodio en competencia candidata.
- Conservar evidencia contraria o límites: «lo hice una vez», «con ayuda», «en ese contexto concreto».
- No inferir nivel de dominio, intención o credibilidad por la calidad retórica de la respuesta.

El enfoque también separa identificación y documentación de evaluación. CEDEFOP describe esas fases como partes distintas de la validación de aprendizajes no formales e informales; Carrera AI puede apoyar las primeras sin declarar certificación. [CEDEFOP](https://www.cedefop.europa.eu/en/tools/validation-non-formal-informal-learning) [Guías de RPL](<../../fuentes/Recognition of Prior Learning_Guidelines RPLpdf.md>)

## Datos y trazabilidad

La primera pasada genera la estructura de trayectoria y preguntas pendientes. La segunda añade a uno o dos episodios: cita o resumen validado, situación, acciones atribuidas a la persona, resultado o aprendizaje, evidencia disponible, herramientas, competencia candidata, límites y confianza.

Una competencia no explorada en profundidad puede seguir apareciendo como `candidata con evidencia inicial`, pero no debe recibir el mismo nivel que una competencia respaldada por un episodio contrastado. ESCO se aplica después sobre conceptos internos ya revisados; la clasificación europea relaciona ocupaciones con conocimientos, habilidades y competencias, pero no demuestra por sí misma la capacidad individual de una persona. [ESCO: ocupaciones](https://esco.ec.europa.eu/en/classification/occupation_main)

## Ventajas debatibles

- Es un diseño operativo sencillo para un primer MVP y fácil de comparar entre entrevistas.
- Protege la cobertura: cada etapa puede existir aunque no se profundice en ella.
- Protege la evidencia: evita que una lista de tareas se convierta automáticamente en una lista de competencias.
- Reduce la presión sobre el entrevistado al concentrar el detalle en pocos episodios elegidos.

## Riesgos y mitigaciones

El riesgo principal es que la segunda pasada privilegie experiencias con relato fácil y deje sin valor trabajos rutinarios, manuales o poco verbalizados. La mitigación es ofrecer criterios alternativos de selección, incluido «experiencia que suele infravalorarse», y permitir evidencia documental, resultados observables o demostraciones futuras.

Otro riesgo es que la IA use STAR como un formulario. La mitigación es admitir respuestas parciales, no pedir todas las dimensiones si ya existe evidencia suficiente y etiquetar claramente las dimensiones no exploradas.

## Hipótesis para un piloto

Estas son propuestas de medición para debatir:

- Cobertura: porcentaje de etapas que la persona reconoce como incluidas, aunque estén pendientes de detalle.
- Profundidad: número de episodios con acción propia y resultado o aprendizaje claramente diferenciados.
- Prudencia: número de competencias presentadas como candidatas frente a competencias validadas.
- Equidad narrativa: distribución de la inmersión entre empleos formales, trabajo autónomo, actividades informales y transiciones.
- Experiencia: percepción de que la persona eligió qué contar y qué profundizar.

## Decisiones para debatir

1. ¿Debe la segunda pasada ocurrir en la misma sesión o ser una invitación posterior?
2. ¿Uno o dos episodios son suficientes para validar utilidad sin convertir el MVP en profundidad encubierta?
3. ¿Qué tipo de evidencia puede reforzar un episodio con poca capacidad de relato verbal?
4. ¿La IA puede sugerir episodios por posible valor o debe esperar siempre una selección espontánea?

## Fuentes de apoyo

- [DOCUMENTO_SPEC_CARRERA_AI.md](../DOCUMENTO_SPEC_CARRERA_AI.md)
- [What is BEI Synergogy](<../../fuentes/What_is_BEI_Synergogy.md>)
- [Skills pillar](<../../fuentes/Skills pillar.md>)
- [How SFIA works](<../../fuentes/How SFIA works - Levels of responsibility and skills.md>)
- [CEDEFOP, información sobre validación](https://www.cedefop.europa.eu/en/tools/validation-non-formal-informal-learning)
- [ESCO, clasificación de ocupaciones](https://esco.ec.europa.eu/en/classification/occupation_main)
