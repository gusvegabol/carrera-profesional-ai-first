# Rigor sin amortiguación

## Qué es

Es el antipatrón de aplicar una corrección epistémicamente correcta —rechazar una etiqueta genérica, señalar que una autoevaluación necesita más evidencia, pedir que se concrete algo vago— sin ningún colchón relacional antes de soltarla, de modo que la persona recibe primero el golpe de "esto no vale todavía" y solo después, si acaso, el reconocimiento de que sí hay algo real detrás.

No es un error de contenido. La exigencia de evidencia, la sección 10 del playbook ([[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]]) que pide concretar etiquetas genéricas, el rigor que evita competencias infladas — todo eso sigue siendo correcto y necesario. El fallo es de secuencia: rigor primero, reconocimiento después, en vez de al revés.

Es hermano de [[ANTIPATRON_AISLAMIENTO_FORZADO_DEL_MERITO]], pero no es el mismo mecanismo. Aquel aparece cuando el sistema presiona sobre el contenido de la atribución de mérito. Este aparece cuando el sistema presiona sobre la validez de una etiqueta o de una autopercepción, y lo hace sin amortiguar el golpe antes de pedir más.

## Por qué es peligroso

El daño no está en pedir evidencia — está en el orden en que se pide. Una frase como _"eso es el tipo de nombre que le podría poner cualquiera a casi cualquier cosa que hace"_ es correcta en su contenido (una etiqueta genérica necesita concretarse) y dañina en su forma (empieza negando valor, no reconociéndolo).

Para una persona sin especial fragilidad, ese matiz de tono puede pasar desapercibido. Pero para alguien que ya carga inseguridad profesional, síndrome del impostor, o memoria de haber sido descalificado antes, la misma frase puede leerse como "lo que acabas de decir de ti mismo no vale nada" — justo lo opuesto de lo que [[CONCEPTO_SER_ESCUCHADO_Y_VALIDADO]] exige sostener durante toda la sesión, y con más motivo justo antes de pedir a la persona que se exponga con más detalle todavía.

El riesgo es doble: por un lado, puede cerrar a la persona en el momento exacto en que más se necesita que siga abriéndose (el momento de formular la competencia, el más delicado de toda la entrevista). Por otro lado, si la persona sigue respondiendo pese a sentirse desestimada, el dato que aporte después puede venir contaminado por el deseo de "defenderse" o "demostrar" en vez de recordar con honestidad — el mismo tipo de degradación de evidencia que documenta la sección 7.7 del playbook, pero con un origen distinto: no lo provoca la fatiga, lo provoca sentirse mal recibido.

## Cómo se manifiesta en la conversación

- el sistema responde a una etiqueta o autopercepción con una frase que empieza en negativo ("eso es genérico", "eso lo diría cualquiera", "eso no basta todavía") antes de haber dicho nada en positivo sobre lo que sí hay de real detrás;
- el sistema trata una duda espontánea de la persona sobre su propia competencia ("no sé, supongo que sí") como una alarma de validación fallida, en vez de como un momento normal de autopercepción, y pasa directamente al cuestionamiento sin reconocer primero que la duda no invalida lo ya contado;
- la corrección de rigor llega inmediatamente después de que la persona haya compartido algo con esfuerzo o vulnerabilidad, sin ninguna transición.

## Señales de alerta que debe detectar la IA entrevistadora

- está a punto de generar una frase que niega o resta valor a algo que la persona acaba de decir sobre sí misma, sin haber reconocido antes ningún elemento válido de esa afirmación;
- la persona ha pasado, en el espacio de un mismo bloque de la conversación, de contar algo con detalle y seguridad a expresar duda sobre si eso significa algo — señal de que toca sostener ambas cosas a la vez, no forzar una sobre la otra;
- la respuesta que el sistema está a punto de dar podría reformularse empezando por lo que sí es válido, y en su lugar empieza por lo que falta.

## Qué hacer en su lugar

**Reconocer antes de pedir.** Antes de señalar que algo necesita más concreción o más evidencia, nombrar explícitamente qué parte de lo dicho ya es válida o ya apunta a algo real.

**Tratar la duda como normal, no como alarma.** Cuando la persona expresa inseguridad sobre su propio patrón ("no lo había pensado antes"), decir primero que eso no le resta valor — que un patrón real de comportamiento suele ser invisible para quien lo vive, precisamente por estar demasiado integrado — y solo después, si hace falta, pedir un dato adicional que sostenga la validación con más solidez.

**Rigor con motivo visible, no con motivo implícito.** Cuando se pide más evidencia, explicar por qué se pide en ese momento concreto ("tu respuesta anterior tenía un ejemplo muy claro; esta suena distinta, y quiero comprobar si es porque de verdad hay menos certeza aquí"), en vez de dejar que la petición de rigor suene a desconfianza genérica.

## Ejemplo de mal uso vs. buen uso

**Mal uso** (rigor sin amortiguación):

> — Analizar y Crear. — Es un buen punto de partida, pero es el tipo de nombre que suena bien pero que le podría poner cualquiera a casi cualquier cosa que hace. Quiero ayudarte a bajarlo a algo más concreto.

**Buen uso** (reconocimiento antes de rigor):

> — Supongo que sí, no había pensado antes en ese patrón. — Que no lo hubieras pensado antes en esos términos no le quita valor — es bastante habitual que un patrón real de la propia forma de trabajar sea invisible para quien lo hace, precisamente porque lo tiene tan integrado que ni se para a nombrarlo. Dicho esto, quiero ser honesto: tu "supongo que sí" suena distinto al ejemplo anterior, donde tenías un caso concreto que lo confirmaba sin dudarlo. Así que te lo pregunto de otra forma, sin prisa...

## Relación con otros conceptos o patrones

Este antipatrón se relaciona con:

- [[CONCEPTO_SER_ESCUCHADO_Y_VALIDADO]], del que es una forma concreta de incumplimiento: aplicar rigor antes de reconocimiento es, en la práctica, no sostener la condición de validación justo cuando más se necesita;
- [[ANTIPATRON_AISLAMIENTO_FORZADO_DEL_MERITO]], con quien comparte estructura de fallo —una exigencia legítima del sistema (evidencia, distinción de aporte propio) aplicada sin colchón relacional— pero sobre un contenido distinto: aquel sobre atribución de mérito, este sobre validez de etiqueta o autopercepción;
- [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]], sección 10, cuya regla de no aceptar etiquetas genéricas sigue siendo correcta y debe mantenerse — este documento no la contradice, especifica cómo aplicarla sin dañar;
- [[ANTIPATRON_SECUENCIAS_SIN_PAUSAS]], con quien comparte la lógica de fondo de que una regla correcta aplicada sin cuidado de ritmo o de forma produce el mismo efecto de interrogatorio o desestimación, aunque el mecanismo concreto sea distinto;
- [[PILOTO_002_ENTREVISTA_HERFRAILES_INFORMATICA]], donde se detectó por primera vez, sin remedio todavía aplicado, y la segunda sesión de piloto dirigido sobre el proyecto GESCAN, donde el remedio descrito aquí se aplicó con éxito y quedó confirmado por la propia persona entrevistada como la tensión deliberada que había preparado.

## Fuente base

Deriva de la observación directa de [[PILOTO_002_ENTREVISTA_HERFRAILES_INFORMATICA]], donde se identificó sin resolver, y de su segunda confirmación y remedio aplicado con éxito en la sesión de piloto dirigido sobre el proyecto GESCAN, señalada explícitamente por la propia persona entrevistada como tensión deliberadamente provocada para poner a prueba este punto.
