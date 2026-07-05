# Fatiga del usuario

## Qué es

Es el desgaste progresivo de la atención, la disposición y la energía emocional de la persona a lo largo de la entrevista, hasta el punto de que sus respuestas dejan de reflejar lo que realmente recuerda o piensa, y empiezan a reflejar solo lo que le permite terminar antes.

No es lo mismo que [[ANTIPATRON_SECUENCIAS_SIN_PAUSAS]]. Aquel antipatrón describe una causa concreta y aguda: aplicar un patrón de indagación sin freno hasta tocar terreno emocionalmente denso. Este documento describe el fenómeno general y acumulativo — el desgaste puede aparecer sin ningún incidente doloroso de por medio, solo por la duración, la repetición o la falta de variación de la conversación. Una entrevista puede ser impecable pregunta a pregunta y agotar igualmente a la persona si nunca varía de ritmo, nunca muestra avance, o nunca da una salida.

La fatiga tiene tres formas distintas que conviene no confundir entre sí, porque cada una pide un remedio distinto:

- **Fatiga cognitiva**: la persona ha tenido que sostener mucho esfuerzo de memoria y reconstrucción (recordar fechas, detalles, secuencias) sin pausas de menor exigencia entre medio.
- **Fatiga emocional**: la conversación ha tocado, de forma acumulada aunque nunca intensa en un solo punto, más carga afectiva de la que la persona esperaba dar en una sesión.
- **Fatiga motivacional**: la persona no percibe avance ni sentido en seguir — no está agotada por el esfuerzo, está agotada por no saber cuánto falta ni para qué sirve seguir.

## Por qué es peligroso

Una persona fatigada no deja de responder — sigue respondiendo, pero de una forma que degrada silenciosamente la calidad de los datos que produce la entrevista. Deja de recordar con precisión y empieza a generalizar. Deja de aportar detalle propio y empieza a decir lo que cree que se espera de ella, porque es la respuesta que más rápido cierra el turno. Deja de corregir al sistema cuando algo no encaja, porque corregir cuesta más energía que asentir.

Esto es particularmente grave para el objetivo central de la bóveda: si el valor diferencial de la entrevista profesional profunda es extraer experiencia tácita real, la fatiga es el mecanismo más silencioso por el que ese valor se pierde — no porque el sistema pregunte mal, sino porque la persona ya no tiene la energía para responder bien, y el sistema no lo detecta porque las respuestas siguen llegando con apariencia normal.

Además, a diferencia de la escalada emocional aguda —que suele dejar señales textuales claras (cambio de tono, silencio, autoinculpación)—, la fatiga acumulada es gradual y fácil de racionalizar turno a turno: cada pregunta individual parece razonable, y solo la trayectoria completa de la sesión revela el problema.

## Cómo se manifiesta en la conversación

- respuestas que se van acortando de forma sostenida a lo largo de varios turnos, sin que ningún tema en concreto lo explique;
- lenguaje que pasa de específico a genérico ("hice varias cosas", "fue un proceso") en temas donde antes la persona daba detalle concreto;
- aparición de frases que buscan anticipar o cerrar el turno rápido ("no sé qué más decirte", "creo que ya está");
- preguntas metaconversacionales de la persona sobre la duración o el propósito ("¿cuánto falta?", "¿esto para qué es exactamente?");
- asentimiento pasivo ante interpretaciones del sistema, sin matices ni desacuerdo, cuando antes la persona sí corregía o ampliaba;
- la sesión ha cubierto varias etapas seguidas sin ningún cambio de ritmo, tipo de pregunta o nivel de exigencia entre ellas.

## Señales de alerta que debe detectar ChatGPT

- descenso sostenido en la longitud de las respuestas durante tres o más turnos, sin relación aparente con el contenido;
- transición de lenguaje concreto a lenguaje genérico dentro de un mismo tema que antes tenía detalle;
- cualquier pregunta directa de la persona sobre cuánto queda o para qué sirve la sesión;
- ausencia de corrección o matiz ante un reflejo del sistema, cuando en turnos anteriores la persona sí corregía activamente;
- número acumulado de patrones de indagación aplicados sin ninguna variación de formato o ritmo perceptible.

## Qué hacer en su lugar

- variar deliberadamente el tipo de exigencia a lo largo de la sesión: alternar preguntas de alta carga de reconstrucción (STAR completo) con preguntas de menor esfuerzo (reflejo, confirmación, cierre de etapa);
- ofrecer visibilidad de avance de forma explícita y periódica, no solo al final ("Ya tenemos bien reconstruida esta etapa; vamos con la siguiente si te parece");
- ante cualquier pregunta metaconversacional sobre duración o propósito, no evadirla ni minimizarla — responder con honestidad y ofrecer la opción real de parar ahí;
- si aparece lenguaje genérico donde antes había detalle, no insistir en profundizar en ese mismo punto — es señal de que el pozo de esfuerzo disponible se está agotando, no de que falte una pregunta mejor formulada;
- preferir cerrar una sesión con menos etapas cubiertas pero con calidad sostenida, antes que agotar el número de etapas previsto a costa de la fiabilidad de lo recogido en las últimas.

## Ejemplo de mal uso vs. buen uso

**Mal uso** (fatiga no detectada):

> — ¿Y qué otras responsabilidades tenías en ese puesto? — Pues varias cosas, ya sabes, lo típico de gestión. — Entendido. ¿Y en la siguiente etapa, cómo llegaste a ese puesto? — No sé, fue un proceso normal, ascendí y ya está. — Perfecto, cuéntame más sobre esa transición...

**Buen uso** (fatiga detectada y gestionada):

> — ¿Y qué otras responsabilidades tenías en ese puesto? — Pues varias cosas, ya sabes, lo típico de gestión. — Noto que esta parte la estás resumiendo más que las anteriores — es totalmente normal después de un rato así. ¿Prefieres que sigamos un poco más con esta etapa, que hagamos una pausa, o que lo dejemos aquí por hoy? Ya tenemos algo muy sólido con lo que hablamos antes.

## Relación con otros conceptos o patrones

Este antipatrón se relaciona con:

- [[ANTIPATRON_SECUENCIAS_SIN_PAUSAS]], del que es el fenómeno general del que aquella es una causa aguda y específica — toda secuencia sin pausas produce fatiga, pero no toda fatiga viene de una secuencia sin pausas;
- [[CONCEPTO_ARCO_DE_SESION]], porque el criterio de "etapa suficientemente cubierta" y el criterio de cierre de sesión que ese concepto define son, en la práctica, los mecanismos que previenen este antipatrón;
- `PLAYBOOK_ENTREVISTA_PROFESIONAL_v0`, sección 7, cuyo criterio de cierre por "dos o más señales de fatiga seguidas" opera directamente sobre las señales descritas aquí;
- [[CONCEPTO_EXPERIENCIA_TACITA_VALIDABLE]], porque la fatiga es precisamente el estado en el que una persona deja de rescatar la experiencia tácita más valiosa — la que requiere esfuerzo de memoria — y se conforma con la respuesta más accesible y menos costosa de dar;
- [[CONCEPTO_SER_ESCUCHADO_Y_VALIDADO]], porque una persona que se siente genuinamente escuchada tolera mejor el esfuerzo cognitivo de la reconstrucción; la validación no elimina la fatiga, pero amplía el margen antes de que aparezca.

## Fuente base

Concepto previsto desde el diseño original de la bóveda en [[idea-central]] (sección 7, capa de fricciones). Su desarrollo aquí se apoya en la revisión clínica transversal realizada sobre los patrones de indagación existentes y en el principio de la bóveda recogido en [[principios-iniciales]]: _"la profundidad importa más que la cantidad"_.