# Cierre anclado al hilo único

## Qué es

Es el antipatrón de formular la pregunta de cierre de una entrevista de forma que valida la transferibilidad de la competencia ya construida y, al mismo tiempo, se espera que esa misma pregunta invite a abrir una puerta hacia otra competencia distinta — cuando en realidad una pregunta no puede cumplir las dos funciones a la vez sin decirlo explícitamente.

La pregunta de cierre habitual (*"¿esto tendría valor si tuvieras que explicarlo fuera?"*) usa el demostrativo "esto" para referirse al hilo que ya se ha construido durante toda la sesión. Eso ancla a la persona entrevistada al contenido ya trabajado, en el peor momento posible para pedirle que salte a un recuerdo distinto: justo cuando está cerrando mentalmente el tema.

## Por qué es peligroso

El daño es invisible desde dentro de la propia sesión. No hay ninguna señal textual de que se está dejando fuera contenido real — la sesión se siente completa, bien cerrada, con las tres validaciones cumplidas. El propio entrevistador puede evaluar el piloto como "satisfactorio" con toda razón, porque dentro de su objetivo (una competencia, con evidencia, validada) lo fue.

Esto quedó confirmado con datos, no solo con sospecha teórica: en un ejercicio de entrevista sobre un personaje con una verdad de fondo escrita de antemano, la competencia objetivo tenía dos componentes —detección de patrones de consumo, y transmisión informal de ese criterio a compañeros nuevos—. La entrevista capturó el primero con gran fidelidad y nunca llegó a mencionar el segundo en ningún momento de la sesión. No fue un fallo de ejecución de las preguntas individuales, que fueron buenas una a una. Fue que el diseño de la sesión nunca tuvo la cobertura como criterio de decisión — solo la profundidad en el hilo que apareciera primero.

## Cómo se manifiesta en la conversación

- la pregunta de cierre usa un demostrativo que apunta al contenido ya construido ("esto", "esta forma de trabajar") sin ninguna cláusula que invite explícitamente a un contenido distinto;
- la sesión completa gira alrededor de un único hilo desde que aparece la primera anécdota fuerte, sin que en ningún punto se ofrezca deliberadamente una puerta hacia otro tipo de experiencia;
- el cierre se siente satisfactorio y completo desde dentro de la conversación, sin ninguna sensación de vacío que alerte de que algo se quedó fuera.

## Señales de alerta que debe detectar la IA entrevistadora

No hay una señal textual que delate este antipatrón mientras ocurre — es, en ese sentido, hermano de [[FRICCION_AMBIGUEDAD_PARQUEDAD_O_DESINTERES]]: el problema no se nota desde dentro de la sesión. La señal que sí se puede vigilar es estructural, no conversacional: si la sesión ha girado en torno a un único hilo desde el primer tercio de la conversación, sin que se haya ofrecido ninguna puerta alternativa antes del cierre, hay riesgo de este antipatrón con independencia de cómo se sienta la conversación.

## Qué hacer en su lugar

**Separar la pregunta de validación de la pregunta de puerta nueva.** No esperar que una sola pregunta de cierre haga las dos cosas. Primero validar la transferibilidad de lo ya construido; después, en un turno explícitamente distinto, abrir una invitación limpia:

> "Antes de cerrar del todo: ¿hay alguna otra parte de tu trabajo, sin relación con esto que hemos hablado, que también muestre algo de cómo trabajas?"

**No asumir cobertura por defecto.** Una sesión centrada en profundidad (el modo por defecto de este playbook) no produce cobertura como efecto secundario. Si el objetivo de una sesión concreta es cobertura, debe declararse como tal desde el diseño, no esperarse de una pregunta de cierre bien intencionada.

## Ejemplo de mal uso vs. buen uso

**Mal uso** (cierre que mezcla validación y puerta nueva en una sola pregunta):
> — ¿Te parece que esto tendría valor si mañana tuvieras que explicar tu trabajo a alguien de fuera?
> — Sí, creo que sí... nunca lo había pensado como algo que se pudiera contar en una entrevista.
> *(la sesión cierra aquí, sin que ninguna otra faceta de la persona llegue a mencionarse)*

**Buen uso** (validación y puerta nueva como dos movimientos distintos):
> — ¿Te parece que esto tendría valor si mañana tuvieras que explicar tu trabajo a alguien de fuera?
> — Sí, creo que sí.
> — Antes de cerrar del todo: ¿hay alguna otra parte de tu trabajo, sin relación con esto, que también muestre algo de cómo trabajas?

## Relación con otros conceptos o patrones

Este antipatrón se relaciona con:

- [[FRICCION_AMBIGUEDAD_PARQUEDAD_O_DESINTERES]], con quien comparte la propiedad de ser invisible desde dentro de la propia sesión — ninguno de los dos deja rastro textual de que algo falla;
- [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]], sección 13 (cierre conversacional y validación triple), donde debería incorporarse la separación explícita entre validación de transferibilidad y puerta nueva;
- [[CONCEPTO_ARCO_DE_SESION]], porque decidir si una sesión persigue profundidad o cobertura es exactamente el tipo de criterio de orquestación que ese concepto debería regular, y que hoy no distingue entre ambos modos.

## Fuente base

Deriva de la comparación directa entre la transcripción de [[PILOTO_005_ENTREVISTA_REPONEDOR_SUPERMERCADO]] y la verdad de fondo del personaje entrevistado, escrita antes de la sesión y no conocida por el modelo que la condujo, que reveló la ausencia completa de uno de los dos componentes de la competencia objetivo.
