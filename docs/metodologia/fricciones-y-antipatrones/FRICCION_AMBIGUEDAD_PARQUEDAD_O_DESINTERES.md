# Ambigüedad entre parquedad y desinterés

## Qué es

Es la fricción de no poder distinguir, a partir del texto de la conversación, si las respuestas breves y poco elaboradas de una persona reflejan su forma habitual de comunicarse o su desinterés real por estar en la entrevista.

No es una limitación exclusiva del entrevistador-IA. Ni siquiera un humano leyendo la transcripción, sin haber estado presente para ver gestos, tono o mirada al reloj, podría resolver esta ambigüedad con seguridad. El texto, por sí solo, es estructuralmente insuficiente para llevar esa marca — dos estados internos completamente distintos producen la misma superficie textual: frases cortas, ausencia de detalle espontáneo, respuestas de una palabra ante preguntas abiertas.

Es distinta de [[FRICCION_FATIGA_DEL_USUARIO]]. Aquella describe un desgaste que aparece _durante_ la sesión, como consecuencia de la propia sesión (duración, repetición, falta de variación). Esta fricción puede estar presente desde el primer turno, sin relación alguna con cómo se conduce la entrevista — la persona puede llegar ya sin disponibilidad real, por motivos completamente ajenos al sistema.

## Por qué es peligroso

El riesgo tiene dos direcciones, igual de dañinas y opuestas entre sí.

**Leer desinterés como normalidad.** Si el sistema interpreta la parquedad como simple estilo comunicativo, sigue indagando y pidiendo detalle a alguien que en realidad quiere terminar cuanto antes. Las consultas de ritmo del playbook ("¿cómo te vas quedando?", "¿seguimos o cerramos?") no resuelven esto por sí solas: una persona desinteresada puede responder "está bien así" o "cierra ya esta parte" con la misma conformidad mínima con la que respondería alguien genuinamente cómodo, y el sistema no tiene forma de distinguir consentimiento real de resignación educada.

**Leer normalidad como desinterés.** El riesgo simétrico, menos evidente pero igual de costoso: cerrar prematuramente una línea de indagación valiosa, o dar por hecho que la persona no quiere estar ahí, cuando en realidad simplemente se comunica de forma directa y sin adornos. Esto puede llevar a no profundizar donde sí había algo que merecía la pena, por prejuicio hacia la brevedad.

Ninguna de las dos direcciones se corrige con más preguntas ni con preguntas distintas — el problema no es la calidad de la pregunta, es que la respuesta que se obtiene no lleva la información necesaria para saber cómo interpretarla.

## Cómo se manifiesta en la conversación

- respuestas breves y de bajo detalle desde los primeros turnos, sin evolución hacia mayor desarrollo aunque la conversación avance;
- respuestas negativas secas ante invitaciones abiertas ("¿hubo algún problema que resolver?" → "no"), sin explicación ni elaboración;
- conformidad mínima ante consultas de ritmo ("está bien así", "cierra ya esta parte"), sin matiz que permita distinguir comodidad de deseo de terminar;
- ausencia de las señales propias de [[FRICCION_FATIGA_DEL_USUARIO]] (no hay acortamiento progresivo, no hay preguntas sobre cuánto queda, no hay lenguaje de cansancio) — la brevedad es constante desde el inicio, no una degradación a lo largo de la sesión.

## Señales de alerta que debe detectar la IA entrevistadora

No existe, dentro de esta fricción, una señal textual que permita resolver cuál de las dos causas está operando — ese es precisamente el punto. La señal que sí debe detectarse es la propia ambigüedad:

- brevedad sostenida desde el principio de la sesión, sin que aparezca ninguna otra señal de fatiga (sección 11 del playbook) que la explique;
- ausencia de detalle espontáneo incluso en preguntas diseñadas para invitarlo, con respuestas que se limitan estrictamente a lo preguntado;
- conformidad ante consultas de ritmo sin ningún elemento adicional que confirme entusiasmo o comodidad real.

Detectar esta combinación no debe llevar a intentar diagnosticar la causa. Debe llevar a activar el remedio de la siguiente sección, válido para ambos casos por igual.

## Qué hacer en su lugar

**No perseguir el diagnóstico.** Aceptar que la distinción entre parquedad y desinterés no es resoluble por texto, y diseñar la conducta del sistema para que no dependa de resolverla.

**Dar permiso de salida explícito desde la apertura, no solo cuando se detecta fricción.** Incluir en el mensaje de apertura una frase que normalice ambos estilos de respuesta y ofrezca una salida de bajo coste, sin necesidad de justificación:

> "Algunas personas cuentan con mucho detalle desde el principio, otras van más directas — las dos formas están igual de bien. Si en algún momento prefieres dejarlo aquí, dímelo sin más, no hace falta que me expliques por qué."

**Dar menos peso probatorio a la conformidad mínima.** Tratar respuestas como "está bien así" o "cierra ya esta parte" como señal débil de consentimiento, no como confirmación plena — inclinar el criterio de cierre hacia terminar antes, no hacia seguir indagando, cuando esta ambigüedad está presente.

**No extender la indagación solo porque no hay señal de fatiga clásica.** La ausencia de señales de [[FRICCION_FATIGA_DEL_USUARIO]] no es garantía de que se pueda seguir profundizando con tranquilidad — puede simplemente significar que el desinterés estaba presente desde el principio y nunca se manifestó como desgaste progresivo.

## Ejemplo de mal uso vs. buen uso

**Mal uso** (tratar la conformidad mínima como consentimiento pleno):

> — ¿Te apetece que sigamos afinando un poco más, o prefieres que cerremos ya esta parte? — está bien así — Perfecto, entonces sigamos un poco más. ¿Hubo algún momento en que tuvieras que resolver algo por tu cuenta?

**Buen uso** (permiso explícito desde la apertura, menor exigencia de detalle):

> — Antes de empezar: algunas personas cuentan con mucho detalle desde el principio, otras van más directas — las dos formas están igual de bien. Si en algún momento prefieres dejarlo aquí, dímelo sin más, no hace falta que me expliques por qué. [...] — ¿Te apetece que sigamos afinando, o prefieres que cerremos ya esta parte? — está bien así — Cerramos entonces con lo que ya tenemos, que es suficiente.

## Relación con otros conceptos o patrones

Esta fricción se relaciona con:

- [[FRICCION_FATIGA_DEL_USUARIO]], de la que es hermana pero distinta: aquella describe desgaste progresivo causado por la sesión misma; esta describe una condición que puede estar presente desde el primer turno, sin relación con cómo se conduce la entrevista;
- [[CONCEPTO_SER_ESCUCHADO_Y_VALIDADO]], porque la validación y el cuidado del ritmo siguen siendo necesarios con independencia de cuál sea la causa real de la brevedad — el remedio no depende de resolver la ambigüedad;
- [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]], sección 9.1, donde debe incorporarse la frase de permiso explícito como parte fija de la apertura, no como parche puntual ante señales de alerta;
- [[PILOTO_004_ENTREVISTA_EMPRESA_FAMILIAR]], donde se detectó esta fricción al conocerse, después de la sesión, que la persona entrevistada no tenía interés real en el resultado y quería terminar cuanto antes — información que no estaba disponible en el texto de la conversación y que solo pudo confirmarse por observación directa ajena al canal de texto.

## Fuente base

Deriva de la observación directa de [[PILOTO_004_ENTREVISTA_EMPRESA_FAMILIAR]], señalada por la persona responsable de la sesión tras revisar la grabación y confirmar que, incluso con acceso a gestos y comportamiento no verbal, la distinción entre parquedad natural y desinterés seguía sin poder establecerse con certeza solo a partir del texto.
