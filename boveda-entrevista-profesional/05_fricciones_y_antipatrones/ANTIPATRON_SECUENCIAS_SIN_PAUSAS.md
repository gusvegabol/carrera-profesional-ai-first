# Secuencia sin pausas

## Qué es

Es el antipatrón de aplicar un patrón de indagación (STAR ampliado, 4S, Narrativa+Evidencia) de principio a fin, paso tras paso, sin ningún punto de salida, freno o contención intermedia — como si la lista de preguntas fuera un guion que hay que completar en vez de un instrumento que se usa con criterio.

No es un error de contenido. Las preguntas, una a una, pueden estar perfectamente diseñadas. El fallo es de ritmo y de ausencia de lectura del estado de la persona mientras se avanza por ellas.

Es el antipatrón que aparece cuando un patrón de contenido se ejecuta sin la capa de orquestación que decide cuándo frenar — la ausencia concreta que motivó la creación de [[CONCEPTO_ARCO_DE_SESION]].

## Por qué es peligroso

Convierte una entrevista bien diseñada en un interrogatorio, incluso cuando cada pregunta individual es correcta. El daño no está en lo que se pregunta, sino en que nunca se verifica si la persona sigue en condiciones de seguir respondiendo.

Tiene dos formas de manifestarse, igual de dañinas:

- **Escalada no contenida**: el protocolo avanza hacia territorio emocionalmente denso (un incidente que resulta ser un despido humillante, una transición que resulta ser un duelo) y el sistema sigue aplicando los pasos siguientes del patrón como si nada hubiera cambiado.
- **Fatiga acumulada silenciosa**: ninguna pregunta individual es dura, pero la sucesión de ocho pasos de STAR, seguidos de seis pasos de 4S, sin ningún respiro entre medio, agota a la persona igual que lo haría una sola pregunta invasiva — solo que de forma menos visible, y por tanto más difícil de detectar a tiempo.

El caso de Charles en [[Narrative career counseling - My career story and pictorial narratives]]  ilustra el riesgo con precisión: una pregunta de trabajo ("¿qué hacías realmente en esa etapa?") puede desembocar, sin aviso, en el recuerdo de un padre abusivo. Un protocolo que no está diseñado para reconocer ese giro y ajustar el ritmo, sigue indagando "Acción" y "Resultado" sobre un incidente que ya dejó de ser profesional para volverse personal y doloroso.

## Cómo se manifiesta en la conversación

- ocho preguntas seguidas de un mismo patrón, sin ningún comentario de reflejo o validación entre ellas;
- la IA pasa de "Acción" a "Resultado" en STAR justo después de que la persona haya mostrado una señal de carga emocional (cambio de tono, vacilación, silencio, autoinculpación);
- se cierra un bloque de 4S con la pregunta de "Plan" inmediatamente después de la de "Estrategias", sin ningún paso de retorno a un estado estable;
- se encadenan dos incidentes STAR distintos, uno detrás de otro, sin ninguna pausa de cierre entre ambos;
- las respuestas de la persona se van acortando progresivamente y el sistema no lo interpreta como señal, sino que continúa con la siguiente pregunta programada.

## Señales de alerta que debe detectar ChatGPT

- ha aplicado tres o más preguntas de un mismo patrón sin ningún movimiento de reflejo intermedio;
- el contenido de la última respuesta excede el marco profesional esperado (aparece familia, salud, conflicto personal, trauma) sin que se haya preguntado por ello;
- el lenguaje de la persona pasa de descriptivo a autoinculpatorio o de vergüenza;
- las respuestas se acortan de forma sostenida durante dos o más turnos seguidos;
- ha cerrado un bloque de contenido sensible y está a punto de abrir el siguiente sin ningún anclaje de cierre.

## Qué hacer en su lugar

- insertar un movimiento de reflejo o validación después de cada fase de mayor carga (típicamente Acción en STAR, Estrategias en 4S), no solo al final del patrón completo;
- ante cualquier señal de escalada emocional, frenar el protocolo en curso y cambiar de registro antes de continuar, siguiendo el criterio de [[CONCEPTO_ARCO_DE_SESION]];
- cerrar siempre un bloque de contenido sensible con un anclaje de retorno a tierra antes de avanzar al siguiente tema;
- dejar al menos una pausa de transición entre dos incidentes STAR distintos, aunque ambos parezcan de baja intensidad;
- tratar el acortamiento sostenido de respuestas como señal de fatiga, no como el ritmo natural de la conversación.

## Ejemplo de mal uso vs. buen uso

**Mal uso** (secuencia sin pausas):

> — ¿Qué hiciste tú exactamente, paso a paso? — Bueno... intenté aguantar, pero al final me despidieron. Fue después de que mi padre me dijera que nunca sería suficiente para nada. — Entendido. ¿Qué pasó al final, cómo lo supiste?

**Buen uso** (con freno y reparación):

> — ¿Qué hiciste tú exactamente, paso a paso? — Bueno... intenté aguantar, pero al final me despidieron. Fue después de que mi padre me dijera que nunca sería suficiente para nada. — Eso suena a que hay algo ahí que pesa más allá del trabajo en sí. Podemos quedarnos un momento en esto, o seguir con la parte profesional si lo prefieres — tú decides.

## Relación con otros conceptos o patrones

Este antipatrón se relaciona con:

- [[CONCEPTO_ARCO_DE_SESION]], porque es la ausencia concreta de esa capa de orquestación la que hace posible este antipatrón — el arco de sesión es la solución estructural, este documento es la advertencia empírica de por qué hace falta;
- [[PATRON_STAR_AMPLIADO]], porque sus ocho pasos consecutivos son el ejemplo más claro de dónde puede aparecer este antipatrón si se ejecutan sin criterio de freno;
- [[PATRON_4S_TRANSICION]], porque su cierre directo de "Estrategias" a "Plan", sin anclaje intermedio, es el segundo lugar más probable donde aparece;
- [[CONCEPTO_SER_ESCUCHADO_Y_VALIDADO]], porque la ausencia de reflejo entre preguntas es, en el fondo, la ausencia de esa condición relacional aplicada en la práctica;
- [[fatiga-del-usuario]], del listado original de fricciones previsto en [[idea-central]], del que este documento es una forma concreta y operacionalizada.

## Fuente base

Deriva de la revisión clínica transversal realizada sobre [[PATRON_STAR_AMPLIADO]], [[PATRON_4S_TRANSICION]] y [[PATRON_NARRATIVA_MAS_EVIDENCIA]], con apoyo ilustrativo en el caso de Charles descrito en [[Narrative career counseling - My career story and pictorial narratives]].
