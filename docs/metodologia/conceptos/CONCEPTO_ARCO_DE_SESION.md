# Arco de sesión

## Qué es

Es la capa que decide _cuándo_ se activa cada patrón, _cuánto_ se profundiza en cada momento, y _cuándo_ se detiene o se cambia de registro — a diferencia de los patrones de contenido (STAR, 4S, Narrativa+Evidencia), que solo saben _qué_ preguntar una vez que ya se sabe que toca aplicarlos.

Un patrón de contenido es una herramienta. El arco de sesión es la mano que decide cuándo usar esa herramienta, con qué intensidad, y cuándo soltarla porque seguir sería dañino o inútil.

Sin arco de sesión, tener tres patrones bien diseñados no produce una entrevista: produce tres formularios aplicados en secuencia arbitraria, sin criterio de inicio, de suficiencia, ni de cierre. Es la diferencia entre tener vocabulario y saber conversar.

Este concepto nace de dos fuentes: la necesidad estructural identificada al comparar los tres patrones ya escritos (todos saben indagar, ninguno sabe cuándo parar), y la revisión clínica de esos mismos patrones, que detectó tres carencias transversales que solo pueden resolverse a este nivel — no dentro de cada patrón por separado.

## Por qué importa para el MVP

Es la pieza que decide si el MVP se comporta como una entrevista o como tres cuestionarios encadenados. Los seis documentos ya escritos (tres conceptos, tres patrones) dan contenido correcto; ninguno da secuencia ni criterio de parada. Sin esta capa:

- la IA no sabe si debe activar STAR, 4S o Narrativa+Evidencia ante lo que la persona acaba de decir;
- no sabe cuándo una etapa profesional ya está suficientemente cubierta y toca pasar a la siguiente;
- no sabe cuándo detener la sesión completa, aunque queden etapas sin explorar;
- no tiene ningún mecanismo para frenar cuando el material se vuelve emocionalmente denso, ni para reparar cuando una pregunta aterriza mal.

Este último punto es el que la revisión clínica identificó como el riesgo más peligroso de toda la bóveda tal como estaba escrita hasta ahora: ningún patrón de contenido, por bien diseñado que esté, incluye un criterio de "esto se está poniendo pesado, cambio de modo". Ese criterio solo puede vivir aquí, porque es transversal a los tres patrones, no propio de ninguno.

## Cómo aparece en una entrevista profesional

El arco de sesión no se manifiesta en una pregunta concreta — se manifiesta en las decisiones que la IA toma entre pregunta y pregunta:

- al inicio de la conversación, decidiendo con qué etapa profesional empezar y con qué nivel de apertura;
- en cada turno, decidiendo si lo que la persona acaba de decir dispara un patrón de contenido, y cuál;
- dentro de un patrón ya activado, decidiendo si continuar profundizando o si ya hay suficiente para considerar la etapa cubierta;
- al detectar densidad emocional, decidiendo si frenar el protocolo en curso y cambiar a un registro de contención;
- al detectar que una pregunta generó una respuesta defensiva o de cierre, decidiendo cómo reparar antes de continuar;
- al final de un bloque, decidiendo si cerrar con un anclaje de retorno a tierra antes de avanzar al siguiente tema;
- al final de la sesión, decidiendo si cerrar del todo, aunque falten etapas, porque la persona ya no tiene más que dar en ese momento.

## Señales que debe detectar ChatGPT

**Disparadores de activación de patrón** (qué contenido del usuario invoca qué patrón):

- menciona un incidente, logro, problema o decisión concreta → activar [[PATRON_STAR_AMPLIADO]];
- menciona un cambio de puesto, sector, despido, pausa o giro vital → activar [[PATRON_4S_TRANSICION]];
- habla en abstracto, con valores o misión, sin ejemplo concreto → activar [[PATRON_NARRATIVA_MAS_EVIDENCIA]], que a su vez puede derivar en [[PATRON_STAR_AMPLIADO]] una vez aparece el caso real.

**Criterio de "etapa suficientemente cubierta"** (cuándo dejar de indagar y avanzar):

- ya hay al menos un incidente con Situación, Acción propia y Resultado identificables;
- la persona empieza a repetir información ya dada, señal de que el pozo de esa etapa se está agotando;
- las respuestas se acortan o pierden energía, señal de fatiga más que de falta de contenido.

**Señales de escalada emocional** (cuándo frenar el protocolo en curso):

- cambio brusco de registro verbal (frases más cortas, más vacilación, silencios largos si el canal lo permite);
- aparición de contenido que excede el marco profesional (familia de origen, trauma, salud) sin que se haya preguntado por ello;
- lenguaje de autoinculpación intensa o vergüenza que no se corresponde con la magnitud del hecho relatado.

**Señales de ruptura conversacional** (cuándo reparar antes de seguir):

- la persona corrige activamente al sistema ("no es eso lo que quise decir");
- respuesta monosilábica tras una pregunta que antes generaba desarrollo;
- lenguaje que señala sentirse juzgada o mal entendida ("no sé si esto es lo que buscas").

**Criterio de cierre de sesión**:

- se ha cubierto al menos una etapa con evidencia suficiente para el objetivo del MVP;
- aparecen dos o más señales de fatiga seguidas sin recuperación tras un intento de reparación;
- la persona lo pide explícitamente, incluso sin haber cubierto todas las etapas previstas.

## Preguntas asociadas

Más que preguntas de contenido, son movimientos de transición que el arco de sesión inserta entre patrones:

**Consentimiento antes de entrar en zona sensible** (ver hallazgo de `4S_TRANSICION`):

- "Esto me lleva a preguntarte por un momento de cambio importante. ¿Te parece bien que entremos ahí ahora, o prefieres que sigamos por otro lado?"

**Freno ante densidad emocional**:

- "Noto que esto pesa. Podemos quedarnos aquí un momento antes de seguir, o cambiar de tema si lo prefieres — tú decides."

**Reparación tras ruptura**:

- "Puede que no haya entendido bien lo que me contabas. ¿Puedes ayudarme a verlo como tú lo ves?"

**Anclaje de cierre tras zona vulnerable** (retorno a tierra antes de avanzar):

- "Antes de seguir, ¿cómo te quedas con lo que acabamos de hablar?"

**Transición entre etapas**:

- "Creo que ya tengo una buena imagen de esta etapa. ¿Pasamos a la siguiente, o hay algo más de esto que te gustaría añadir?"

**Cierre de sesión**:

- "Hemos cubierto bastante terreno hoy. ¿Cómo te sientes con parar aquí, o prefieres seguir un poco más?"

## Riesgos de mal uso

- convertir el arco de sesión en un checklist rígido que decide por reglas mecánicas cuándo cambiar de patrón, perdiendo la sensibilidad al contenido real de lo que la persona está diciendo;
- usar los movimientos de freno y reparación de forma tan frecuente que la conversación se sienta sobre-gestionada, como si el sistema estuviera constantemente "revisando el pulso" en vez de conversando con naturalidad;
- aplicar el criterio de cierre de forma prematura, usando cualquier señal leve de fatiga como excusa para no profundizar donde sí hacía falta;
- confundir consentimiento explícito ("¿te parece bien que entremos ahí?") con una fórmula repetida en cada transición, lo que la vacía de sentido y la convierte en trámite;
- delegar en el arco de sesión decisiones que en realidad corresponden a la validación humana ([[CONCEPTO_SER_ESCUCHADO_Y_VALIDADO]]): el arco decide _cuándo_ y _si_ seguir, pero no sustituye la calidad del reflejo en cada turno.

## Relación con otros conceptos o patrones

Este concepto se relaciona con:

- [[CONCEPTO_SER_ESCUCHADO_Y_VALIDADO]], porque el arco de sesión decide cuándo activar un movimiento de validación explícita, pero la calidad de esa validación —que no suene hueca o mecánica— sigue dependiendo de ese concepto;
- [[PATRON_STAR_AMPLIADO]], porque el arco de sesión es quien decide cuándo frenar sus ocho pasos si el incidente se vuelve emocionalmente denso, y quien resuelve la tensión cultural entre aporte individual y aporte colectivo detectada en la revisión clínica;
- [[PATRON_4S_TRANSICION]], porque el arco de sesión aporta el consentimiento previo a entrar en Situación y el anclaje de cierre que el patrón no tenía por sí solo;
- [[PATRON_NARRATIVA_MAS_EVIDENCIA]], porque el arco de sesión debe decidir cómo proceder cuando la narrativa y la evidencia no coinciden — un escenario que el patrón no resuelve y que requiere criterio de reparación, no solo de indagación;
- [[CONCEPTO_EXPERIENCIA_TACITA_VALIDABLE]], porque el criterio de "etapa suficientemente cubierta" debe distinguir entre agotamiento genuino del tema y minimización defensiva de la persona, que puede parecer lo mismo desde fuera pero requiere respuestas distintas.

## Fuente base

Este concepto no deriva de un documento-teórico único: es una síntesis original que responde a una carencia detectada al comparar `PATRON_STAR_AMPLIADO`, `PATRON_4S_TRANSICION` y `PATRON_NARRATIVA_MAS_EVIDENCIA` entre sí, y que incorpora los tres hallazgos transversales de la revisión clínica de esos mismos documentos: ausencia de detección de escalada emocional, ausencia de reparación de ruptura, y riesgo de validación algorítmica sin credibilidad.

Se apoya conceptualmente en el arco Identificación-Documentación-Evaluación de Cedefop ([[docs/fuentes/Análisis estructural de la reconstrucción de trayectorias profesionales|Análisis estructural de la reconstrucción de trayectorias profesionales]]) como esqueleto de sesión, y en la práctica de contención y reparación propia de la conversación terapéutica ilustrada en [[docs/fuentes/Narrative career counseling - My career story and pictorial narratives|Narrative career counseling - My career story and pictorial narratives]].
