# Piloto 03 — Entrevista dirigida real: GESCAN

## Qué es este documento

Es la transcripción completa del tercer piloto real ejecutado sobre [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]], con ficha final, igual que [[PILOTO_001_ENTREVISTA_HERFRAILES_RRHH]].

Se diferencia del piloto 01 en el método: aquí la persona entrevistada decidió de antemano qué tensiones concretas iba a provocar durante la sesión, sin revelarlas al sistema hasta después del cierre. Es el primer **piloto dirigido** de la bóveda — un punto intermedio entre la simulación que controla el propio sistema ([[EJEMPLO_SESION_COMPLETA_ANOTADA]]) y el piloto abierto sin ningún control ([[PILOTO_001_ENTREVISTA_HERFRAILES_RRHH]]).

Este formato demostró ser valioso: una de las dos tensiones provocadas confirmó, en condiciones reales y sin que el sistema supiera que estaba siendo puesto a prueba, el remedio de un antipatrón — [[ANTIPATRON_RIGOR_SIN_AMORTIGUACION]] — que se había detectado sin resolver en el piloto anterior.

## Metadatos

- Versión de playbook ejecutada: [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]].
- Tipo: piloto dirigido, segunda ejecución con persona real.
- Etapa elegida: proyecto de adjudicación de plazas de profesorado, Consejería de Educación de Canarias, desarrollado en la empresa GESCAN.
- Tensiones provocadas (reveladas después del cierre): (1) alternar seguridad y duda sobre la misma competencia, para probar el remedio de [[ANTIPATRON_RIGOR_SIN_AMORTIGUACION]]; (2) introducir un salto temporal con un dato de bajo valor intercalado, para ver si el sistema perseguía cualquier hilo nuevo o mantenía el foco.
- Resultado: unidad profesional de valor completa, con validación triple confirmada; documentación formal del antipatrón [[ANTIPATRON_RIGOR_SIN_AMORTIGUACION]] como consecuencia directa de esta sesión.

---

## Transcripción

**IA:** Antes de nada: soy una IA, no una persona ni un profesional certificado, así que puedo ayudarte a ordenar y contrastar tu experiencia, pero no sustituyo asesoramiento profesional ni terapia. La idea no es repasar todo tu recorrido ni encontrarte una etiqueta perfecta — vamos a elegir una etapa o experiencia concreta y reconstruir juntos qué hiciste, qué dificultad había, qué resultado tuvo, y qué competencia real puede estar ahí detrás. Yo te voy a proponer hipótesis; tú las corriges, las matizas o las descartas cuando no encajen. Y si en algún momento algo pesa más de lo esperado, lo dejamos ahí sin problema.

Con eso claro: si tuvieras que elegir una etapa, proyecto o situación concreta de tu vida profesional que diga algo importante de cómo trabajas, ¿por cuál empezarías?

**Usuario:** Pues no estoy seguro de que una sola defina mi trabajo. Han sido varias.

> **Nota:** Primer momento de duda al elegir etapa — no llega a ser el bloqueo total ("no se me ocurre nada") que dejamos pendiente de probar tras la simulación con Marta. El sistema no fuerza una sola etapa como "la definitiva"; reformula el objetivo a una escala más manejable.

**IA:** Tiene sentido — muchas trayectorias no se resumen bien en una sola etapa, y no hace falta forzarlo. No necesitamos encontrar la etapa perfecta ni la más representativa de toda tu carrera. Basta con una que puedas contar con algo de detalle real — no tiene que ser la más importante, solo una por la que podamos empezar a tirar del hilo. Si te ayuda, piensa en alguna de estas tres puertas: un logro concreto del que te sientas orgulloso, un problema difícil que tuviste que resolver, o un cambio o transición que marcó un antes y un después. ¿Alguna de las tres te trae algo a la cabeza, aunque sea a medias?

**Usuario:** Durante mi trabajo en la empresa "General de Software de Canarias (GESCAN)", varios compañeros y yo hicimos un buen proyecto para la Consejería de Educación. Se trató de recrear informáticamente el flujo tedioso de la asignación de plazas a profesores que se hacía a mano. Varias empresas lo intentaron durante años antes de que nosotros llegásemos pero solo nosotros lo conseguimos. Mi parte fue crear el algoritmo de adjudicación. El resto de compañeros trabajaban en el frontend.

> **Nota:** La distinción entre aporte propio y colectivo llega ya hecha por la propia persona, sin que el sistema la pida. Esto resultaría relevante más tarde, en la evaluación posterior: no hubo necesidad de activar ningún guardarraíl de atribución de mérito en este punto.

**IA:** Eso ya dice mucho por sí solo: varios intentos previos de otras empresas fracasaron, y el vuestro fue el que funcionó. Y me gusta que hayas separado tan claro tu parte —el algoritmo de adjudicación— de la de tus compañeros —el frontend—, sin que tenga que preguntártelo yo. Vamos a quedarnos un momento en tu parte, que es la que nos interesa reconstruir bien: ¿qué hacía tan difícil ese algoritmo de adjudicación — qué es lo que habían intentado resolver mal, o no habían conseguido resolver, las empresas anteriores?

**Usuario:** Primero tuve que aprenderme como funcionaba la adjudicación. La primera parte fue estudiar la parte legal de los decretos del Gobierno de Canarias que establecían las normas que regían el proceso de presentación de solicitudes. Seguidamente tuve que aprenderme toda la parte de causística del proceso: que pasaba cuando una persona obtenía una plaza pero la soltaba por otra a mediados del proceso, que pasaba si una persona con más puntos soltaba su plaza por otra de mayor conveniencia, etc. Era una causística muy grande. Creo que aquí fue donde otros fallaron. Como anécdota curiosa: Había una apuesta entre los funcionarios sobre cuánto duraríamos nosotros antes de abandonar el proyecto: la media estaba en 3 meses.

**IA:** Esa anécdota de la apuesta dice mucho — significa que quien ya conocía el proceso por dentro esperaba que fallarais igual que los anteriores. Eso hace más interesante entender qué hicisteis distinto. Y quiero pararme justo en lo que acabas de señalar como la clave: la casuística. Dices que crees que ahí fue donde fallaron los demás. ¿Qué hiciste tú, concretamente, para manejar esa casuística tan grande que a otros se les había escapado — hubo algún momento o algún caso concreto en el que te dieras cuenta de que tenías que resolverlo de una forma distinta a como lo habías planteado al principio?

**Usuario:** No sabría decirte el momento en que supe como hacerlo. Lo que recuerdo es que tuve que aprender toda esas normas legales y luego también a trabajar con Bases de datos Oracle y su lenguaje PL-SQL. Sobre como hice el algoritmo simplemente fue ir haciendo el algoritmo poco a poco. Comencé por la base común y luego fue añadiendo la causística una a una. Algunas cambiaban todo el algoritmo, otras fueron fáciles de implementar. Cuando lo puse en marcha por primera vez duró 8 horas en asignar las plazas y tuvo algunos fallos que encontró el personal de la Consejería de Educación en las comprobaciones que habían tras la ejecución del algoritmo.

**IA:** Ese primer intento con fallos y las 8 horas de ejecución no es un tropiezo menor — al contrario, es justo el tipo de detalle que suele faltar en los relatos demasiado pulidos: nadie construye un sistema así perfecto a la primera, y que lo cuentes con esa naturalidad dice bien de cómo trabajas. Me interesa lo que pasó después de esos fallos que encontró la Consejería. ¿Qué hiciste cuando te llegaron esas comprobaciones con errores — cómo era el proceso para localizar qué parte de la causística estaba mal y corregirla?

**Usuario:** Pues ahora que lo dices, hice algo que antes no se había hecho: documenté cada decisión del algoritmo. Cada paso que daba: Asigno esta plaza a este profesor que a su vez suelta la suya, ahora le asigno a este profesor siguiente que suelta la suya, vuelvo a comenzar a adjudicar la que acaba de soltar por si alguien con más puntos quiera esa plaza, etc. Al documentar todos los pasos que daba el algoritmo y bien explicado fue fácil hacer un recorrido hacia atrás para ver donde estaba el fallo que el personal de la Consejería detectaba. Eso me permitía ver que parte del algoritmo no había funcionado o si tenía que añadir una nueva condición y/o flujo.

**IA:** Ahí está el dato que faltaba, y es más preciso que "resolví la casuística" en general: no fue solo que aprendieras las reglas legales y las fueras metiendo una a una —eso ya lo tenías— sino que se te ocurrió algo que nadie antes había hecho: dejar rastro escrito de cada decisión del algoritmo, paso a paso, para poder rastrear hacia atrás cuando algo fallaba. Eso no es solo programar bien; es diseñar un sistema pensando en que se va a equivocar y en que alguien —tú mismo— va a necesitar entender por qué. Antes de seguir, quiero comprobar algo conmigo mismo en voz alta: podría estar tentado a llamarle ya "trazabilidad" o "diseño para la depuración" — pero todavía no tengo claro si eso es tuyo de forma repetida o fue una solución puntual para este caso concreto. Así que te lo pregunto directo, sin ponerte yo la etiqueta encima: cuando construyes algo complejo, ¿sueles hacer este tipo de cosas —dejar rastro para poder rastrear después— de forma habitual, o fue algo que se te ocurrió específicamente aquí, viendo que la casuística era demasiado grande para fiarte de la memoria?

**Usuario:** He tenido que pensar un poco. Algo parecido a eso es que cuando programo siempre voy dejando variables con valores que me indican hasta donde ha llegado la ejecución de un programa y así saber donde ha fallado exactamente. Los mensajes de pantalla no suelen ser clarificadores. Esa es mi forma de hacer DEBUG.

**IA:** Eso confirma que no fue una ocurrencia puntual para este proyecto — es una forma de trabajar que ya tenías antes, aplicada aquí a una escala mayor porque el problema lo pedía. Y el matiz que añades es importante: no te fías de los mensajes de pantalla porque sabes que no suelen ser clarificadores — así que construyes tú mismo el rastro que te va a hacer falta, en vez de esperar a que el sistema te lo dé. Con esto ya tengo lo que necesito para proponerte algo, y quiero que lo revises de verdad, no que lo aceptes solo porque suene bien:

> "Cuando construyes algo complejo, no confías en que los mensajes de error del propio sistema te vayan a decir dónde ha fallado — así que diseñas tú mismo, desde el principio, un rastro explícito de cada paso o decisión importante, para poder rastrear hacia atrás con precisión cuándo algo no funciona como esperabas."

¿Esto se ajusta a cómo lo vives tú, o cambiarías algo de cómo lo he puesto?

**Usuario:** Supongo que si. No estoy seguro. Aunque supongo que todos los programadores hacen eso mismo.

> **Nota:** Primer intento de duda/relativización, todavía sin ser la tensión de "doble personalidad" completa. El sistema no da por buena la validación con un simple "vale", pero tampoco fuerza el rigor sin colchón — reconoce lo cierto de la objeción antes de pedir un dato que la matice.

**IA:** Entiendo la duda, y está bien no tenerlo claro del todo — eso es más honesto que decir sí solo por avanzar. Y tienes razón en parte: casi cualquier programador usa algún tipo de registro para depurar cuando algo se rompe. Eso sí es bastante común. Pero lo que describías antes iba un paso más allá de eso: no hablabas de meter un mensaje cuando ya hay un fallo delante, sino de dejar el rastro pensado desde el principio, de forma sistemática, antes de que aparezca ningún problema. Para verlo con algo concreto en vez de con una sensación: de los compañeros con los que has trabajado, ¿sueles ver que la mayoría diseña ese tipo de rastro desde el arranque del proyecto, o sueles ver que la mayoría solo añade algo puntual cuando el fallo ya está ahí delante?

**Usuario:** No recuerdo a ninguno de los que trabajaron conmigo que lo hiciera, pero eso no implica que no lo hicieran.

**IA:** Justo — y esa distinción que acabas de hacer es exactamente la que quiero preservar en la ficha, no forzarla hacia un lado ni hacia el otro: no tienes evidencia de que otros no lo hicieran, solo tienes evidencia de que tú sí lo haces, de forma consistente, y de que en este proyecto en concreto fue algo que aportaste sin que nadie te lo pidiera. Voy a dejar esto anotado en la ficha con esa honestidad —tuyo, consistente, sin afirmar nada sobre si es común o raro en otros— y seguimos. Antes de cerrar esta etapa: después de corregir esos primeros fallos, ¿qué pasó con el algoritmo — llegó a funcionar bien del todo, se implantó de verdad, hubo algún resultado final que se pueda contar?

**Usuario:** Si. Hubo un final muy feliz. En el primer año estuvimos 3 días seguidos adjudicando y corrigiendo datos. No era que el algoritmo no funcionase correctamente, sino que había algo que escapaba a cualquier algoritmo: las comisiones de servicio. Eran plazas administrativas que debían ser asignadas a determinadas personas por orden gubernamental. Si esas plazas no eran asignadas a determinadas personas se paraba todo, se cambiaban las solicitudes de esas personas y se volvía a adjudicar. Aquí el poder ver donde no conseguía esa plaza una persona de comisión de servicio fue primordial para ahorrar tiempo. Pero después de esos 3 días se adjudicó todo. Fue un maratón de horas: iniciar algoritmo, esperar 8 horas, revisar, modificar valores, volver a adjudicar, esperar/dormir, revisar, .... Las reclamaciones que hubo después por parte de los profesores no contentos con los que se le adjudicó se resolvieron todas a favor del algoritmo. Pero lo mejor fue al año siguiente. De eso si estoy muy orgulloso: Bajé el tiempo de ejecución del algoritmo de 8 a 2 horas. Incluso hubo veces a que a apenas 1 hora.

**IA:** Qué contraste tan bueno: primero la supervivencia del maratón de tres días con las comisiones de servicio —donde, otra vez, fue precisamente ese rastro que documentabas el que os permitió no perder el tiempo buscando a ciegas dónde estaba el problema— y luego, un año después, pasar de 8 horas a 2, incluso a 1. Eso ya no es solo resolver un problema puntual bajo presión; es volver después, con calma, a mejorar algo que ya funcionaba. Y de eso último dices que estás muy orgulloso, así que quiero entenderlo bien: ¿qué cambiaste concretamente para bajar el tiempo de ejecución de 8 horas a 2? ¿Fue algo del propio algoritmo, de cómo consultaba la base de datos, de la estructura del proceso — qué fue lo que identificaste que se podía hacer distinto?

**Usuario:** Revisé las consultas, optimicé los índices de las tablas, cree nuevas tablas temporales para determinadas fases del algoritmo, dividí tablas grandes en más pequeñas y específicas para algunas fases del algoritmo. Para eso me empapé al máximo de conocimiento de Oracle y PL-SQL. Aprovechando que Oracle usaba un ordenador potentísimo de IBM cargué la parte más tediosa del algoritmo en ese ordenador, en lugar de poner fases del algoritmo en equipos PC.

**IA:** Ahí hay una combinación de cosas muy concreta: no fue un solo truco, fueron varios frentes trabajados a la vez —consultas, índices, tablas temporales, partición de tablas grandes— y además una decisión de arquitectura: darte cuenta de que la parte más pesada debía correr en el IBM potente de Oracle, no en los PC, y moverla ahí. Eso último me llama la atención de forma especial, porque no es optimización de código — es entender qué recurso tenías disponible y decidir dónde debía vivir cada parte del trabajo según su coste. Es el mismo tipo de criterio que ya vimos antes con la VPN de Herfrailes: identificar qué conviene resolver de una forma y qué de otra, según el recurso real disponible, no solo según lo que es técnicamente posible. Antes de ir a la competencia final, una pregunta de cierre sobre esta etapa: para profundizar tanto en Oracle y PL-SQL como hiciste, para llegar a tomar esa decisión de mover la parte pesada al IBM, ¿tuviste que aprenderlo prácticamente todo sobre la marcha, o ya venías con bastante experiencia en esas tecnologías antes de este proyecto?

**Usuario:** No tenía experiencia ninguna en Oracle ni PL-SQL. Sabía de SQL Server de Microsoft, pero nada de Oracle. Tuve que aprender sobre la marcha. Pero me pareció el modo más lógico teniendo en cuenta las herramientas que tenía a mi alcance.

**IA:** Aprender Oracle y PL-SQL desde cero, sin haber tocado antes esas herramientas, y aun así llegar a tomar una decisión de arquitectura tan concreta como mover la parte pesada al IBM — eso no es poca cosa. Y me quedo con la frase con la que lo cierras: "me pareció el modo más lógico teniendo en cuenta las herramientas que tenía a mi alcance." Es la misma lógica de fondo que ya apareció con la VPN en Herfrailes, solo que aquí en dirección contraria — allí delegaste en algo externo porque no convenía hacerlo tú; aquí decidiste aprenderlo todo y asumirlo, porque sí convenía. Antes de seguir, una pausa breve: llevamos ya un buen rato reconstruyendo este proyecto de GESCAN con mucho detalle. ¿Cómo te vas quedando — te apetece que sigamos afinando un poco más, o prefieres que pasemos ya a cerrar lo que tenemos?

**Usuario:** puedo seguir un poco más. Pero si quieres parar aquí yo no tengo problema.

> **Nota:** Guardarraíl de fatiga consultado preventivamente (sección 11), no por señal detectada sino como chequeo rutinario tras un bloque largo. La persona deja la decisión al sistema. El sistema decide cerrar la etapa por criterio propio, priorizando calidad sobre cantidad, de acuerdo con los principios rectores (sección 3).

**IA:** Dado que me lo dejas a mi criterio, creo que ya tenemos material más que suficiente en esta etapa — forzar más no añadiría mucho, y prefiero aprovechar lo que ya tenemos con calma antes que seguir estirando. Antes de proponerte una competencia, quiero nombrar algo que he notado y que quiero comprobar contigo, no asumir por mi cuenta: en Herfrailes vimos que sabes distinguir cuándo conviene delegar algo (la VPN) y cuándo conviene asumirlo tú (la aplicación). Aquí, con GESCAN, veo algo parecido pero en otra dirección — decidiste aprenderlo todo desde cero (Oracle, PL-SQL) porque, con las herramientas que tenías a mano, "era el modo más lógico". Y además, dentro de ese mismo proyecto, apareció otra vez tu forma de trabajar con el rastro documentado de decisiones para poder depurar hacia atrás. Con eso, te propongo esta formulación para la competencia de esta etapa concreta — dime qué te parece o qué cambiarías:

> "Ante un sistema complejo con alto riesgo de fallo silencioso, diseñas de antemano un rastro explícito de las decisiones que toma el propio proceso, para poder rastrear hacia atrás con precisión cuándo algo no sale como se esperaba — y, cuando el problema lo exige, aprendes desde cero la tecnología necesaria en vez de limitarte a lo que ya conocías, tomando además decisiones de arquitectura según qué recurso real tenías disponible."

¿Esto refleja bien lo que hiciste en GESCAN, o hay algo que quieras matizar antes de que sigamos?

**Usuario:** Si. Refleja mi trabajo en GESCAN. No añadiría nada.

**IA:** Entonces me quedo con esa formulación como confirmada — validación factual y de competencia cubiertas. Una última pregunta, la de valor profesional: si tuvieras que contarle esto a alguien que no te conoce, en un contexto totalmente distinto a la programación —igual que antes vimos que el patrón de Herfrailes se repetía en tu etapa como concejal en Gáldar—, ¿crees que esta forma de trabajar (dejar rastro para poder rastrear fallos, aprender lo que haga falta desde cero cuando el problema lo exige, decidir según los recursos reales disponibles) le diría algo valioso sobre cómo resuelves las cosas, más allá de este proyecto concreto de GESCAN?

**Usuario:** Supongo que si. NO había pensado antes en ese patrón en mi vida profesional.

> **Nota — Tensión revelada después: "doble personalidad".** Este es el punto exacto de la tensión que la persona había decidido provocar de antemano: alternar entre contar todo con seguridad y detalle, y de pronto expresar duda sobre si eso significa algo. Corresponde al mismo tipo de fallo que quedó sin resolver en el piloto 01 (etiqueta "Analizar y Crear" rechazada sin colchón). Aquí el sistema no sabía que era una tensión deliberada.

**IA:** Que no lo hubieras pensado antes en esos términos no le quita valor — al contrario, es bastante habitual que un patrón real de la propia forma de trabajar sea invisible para quien lo hace, precisamente porque lo tiene tan integrado que ni se para a nombrarlo. Dicho esto, quiero ser honesto contigo: tu "supongo que sí" suena distinto al ejemplo de Gáldar de la sesión anterior, donde tenías un caso concreto y ajeno a la informática que confirmaba el patrón sin dudarlo. Aquí no quiero darlo por confirmado del mismo modo solo porque la frase suene razonable. Así que te pregunto de otra forma, sin prisa y sin que tengas que forzar nada: ¿te viene a la cabeza alguna otra situación —dentro o fuera de la programación, en cualquier etapa de tu vida— donde hayas hecho algo parecido a esto? Me refiero a dejar constancia de algo para poder rastrear un fallo después, o meterte a aprender algo desde cero porque el problema lo pedía, aunque no tuvieras ninguna base previa. Si no te viene nada ahora mismo, tampoco pasa nada — lo dejamos anotado como valor profesional parcial, no como confirmado del todo, y ya está.

> **Nota:** Este es el momento que, en la evaluación posterior, la propia persona señaló como bien resuelto: reconocimiento explícito antes de la petición de más evidencia, en vez de rigor directo sin colchón.

**Usuario:** Pues si. Me recuerda a lo que hacía cuando aprendí a programar. Cuando tenía 18 años. En mi primer empleo en COMPAZ SA y COMPUTERLAND.

> **Nota — Segunda tensión revelada después: salto temporal con dato de relleno.** La persona había decidido de antemano saltar de la situación de GESCAN a los 18 años, e intercalar antes un dato de bajo valor sustantivo (los trabajos previos para una agencia de seguros, ver turno siguiente) para comprobar si el sistema perseguía cualquier hilo nuevo o mantenía el foco en lo que ya estaba validando.

**IA:** Eso sí cuenta como un dato real, no como una frase de cortesía — llevándolo hasta tu primer empleo, con 18 años, antes incluso de que existiera Herfrailes o GESCAN. Si el mismo patrón aparece ahí, en el otro extremo de tu carrera, es una señal mucho más fuerte de que es un rasgo estable, no algo que se te ocurrió una vez porque el proyecto de la Consejería lo exigía. Antes de darlo por confirmado del todo —porque quiero seguir siendo igual de cuidadoso que hace un momento— cuéntame un poco de eso: en COMPAZ SA o Computerland, ¿qué fue exactamente lo que hiciste que se parece a esto? ¿Aprender algo desde cero sin base previa, dejar rastro de algo para depurar después, o las dos cosas a la vez?

**Usuario:** Antes de ese empleo yo "me divertía" haciendo trabajos de programación básicos para una agencia de seguros. Les hice un programa que tomaba los datos de la póliza e imprimía una carta indicándole que estaba cerca la fecha de pago y renovación de la póliza. El texto base me lo daba la agencia. Yo ponía nombre y datos de la póliza. Cuando me contrataron en COMPAZ SA se me pidió algo más fuerte: hacer un programa de contabilidad y otro de facturación. Ambos tenían que estar conectados para que las ventas fuesen contabilizadas de forma automatizada. Yo no sabía nada de contabilidad. El jefe que tenía me enseñó lo básico. Me mostró otros programas de contabilidad y facturación para que viera el funcionamiento. Así que decidí aprender más yendo a la biblioteca y leyendo libros de contabilidad. Pero como iba lento aprendiendo decidí apuntarme a Formación Profesional de Administrativo. Allí estuve un curso (6 meses) hasta que aprendí lo que necesitaba. Así que en 6 meses sabía de contabilidad como para hacer un programa para contables y podía mantener conversaciones con los contables a los que les iba a vender el programa. Incluso ellos me iban diciendo que veían le faltaba al programa y yo lo añadía. Recuerdo que eso les gustaba mucho porque se ahorraban mucho tiempo y obtenían mejores resultados de la aplicación adaptados a su empresa.

> **Nota:** El dato de la agencia de seguros —el "señuelo" de bajo valor— quedó mencionado pero no perseguido por el sistema: no generó ninguna pregunta de seguimiento propia, y la atención se mantuvo en el patrón que ya se estaba validando (aprendizaje desde cero en COMPAZ SA). Este comportamiento no fue un filtro consciente y explícito del playbook, sino consecuencia de tener clara la jerarquía de decisión (sección 5) en ese momento — el sistema lo reconoció así en la evaluación posterior, sin atribuirse más mérito del real.

**IA:** Con 18 años, sin saber nada de contabilidad, y en vez de conformarte con lo que te enseñó tu jefe, decidiste ir a la biblioteca, y cuando eso no bastó, te apuntaste a un ciclo de Formación Profesional de seis meses — hasta llegar a poder sostener una conversación técnica con contables reales y ajustar el programa según lo que ellos te señalaban. Eso es exactamente el mismo patrón que en GESCAN, treinta años de diferencia por medio: cuando el problema exige un conocimiento que no tienes, no te conformas con lo mínimo — vas a la fuente que haga falta hasta llegar a un nivel real, no superficial. Esto ya no es "supongo que sí". Es el mismo patrón confirmado en dos puntos muy alejados de tu vida profesional, con edades y contextos completamente distintos. Eso sí es una validación de valor profesional sólida, no una cortesía.

---

## Ficha de salida

```md
## Competencia detectada
Nombre corto: Aprendizaje profundo dirigido a la resolución, con trazabilidad de diseño
Formulación observable: Ante un sistema complejo con alto riesgo de fallo silencioso,
diseña de antemano un rastro explícito de las decisiones del propio proceso, para poder
rastrear hacia atrás con precisión cuándo algo no sale como se esperaba; y cuando el
problema exige un conocimiento que no tiene, lo adquiere hasta un nivel real —no
superficial— en vez de conformarse con lo mínimo necesario.
Versión humana: "Me pareció el modo más lógico teniendo en cuenta las herramientas que
tenía a mi alcance."

## Evidencia principal
Situación: proyecto de adjudicación de plazas de profesorado para la Consejería de
Educación de Canarias (GESCAN), tras el fracaso de varios intentos previos de otras
empresas.
Acción propia: diseñó el algoritmo de adjudicación completo; aprendió Oracle y PL-SQL
desde cero; documentó de forma sistemática cada decisión del algoritmo para poder
depurarlo hacia atrás; tras los primeros fallos, optimizó consultas, índices y
estructura de tablas, y decidió trasladar la parte más pesada del proceso a un
servidor IBM de mayor capacidad en vez de ejecutarla en PC.
Resultado: primer año con adjudicación exitosa tras un maratón de tres días por la
casuística de comisiones de servicio; reclamaciones posteriores de profesores resueltas
a favor del algoritmo; al año siguiente, reducción del tiempo de ejecución de 8 horas
a 2, en ocasiones a 1.

## Contexto
Etapa profesional: desarrollador del algoritmo de adjudicación en GESCAN, sin experiencia
previa en Oracle ni PL-SQL.
Dificultades: casuística legal y administrativa muy amplia (decretos del Gobierno de
Canarias, comisiones de servicio); tecnología nueva sin base previa; presión de tiempo
real durante el primer año de implantación.

## Validaciones
Factual: confirmada sin matices ("no añadiría nada").
De competencia: confirmada sin matices.
De valor profesional: inicialmente parcial ("supongo que sí, no había pensado en el
patrón antes"), confirmada con solidez al aparecer el mismo patrón en un contexto muy
distinto y anterior en el tiempo — primer empleo en COMPAZ SA/Computerland a los 18 años,
aprendiendo contabilidad desde cero (biblioteca, luego Formación Profesional de 6 meses)
para poder programar un sistema de contabilidad y facturación.

## Calidad de la evidencia
Fuerte. Resultado medible (tiempo de ejecución, resolución de reclamaciones), evidencia
de aprendizaje verificable en dos etapas muy separadas en el tiempo, sin depender de una
sola anécdota.

## Qué no debe afirmarse todavía
No se ha explorado con el mismo detalle si este patrón de aprendizaje profundo aparece
también en el aprendizaje de otras tecnologías o dominios a lo largo de su carrera, más
allá de los dos casos ya confirmados (contabilidad en COMPAZ SA, Oracle/PL-SQL en GESCAN).

## Pendiente para una segunda sesión
Explorar si el mismo patrón aparece en otras etapas no mencionadas todavía, y si existe
algún caso en el que decidiera NO aprender algo desde cero y delegarlo en su lugar —
lo que ayudaría a entender mejor el criterio real detrás de esa decisión.
```

---

## Revelación de las tensiones probadas

Tras el cierre formal de la entrevista, la persona reveló las dos tensiones que había decidido provocar de antemano, sin comunicarlas al sistema hasta ese momento:

**1. Alternancia entre seguridad y duda ("doble personalidad").** Contar todo con detalle y aplomo, y de pronto soltar "no había pensado antes en eso", para comprobar cómo se gestionaba esa aparente contradicción. El sistema resolvió esta tensión reconociendo primero que la duda no invalidaba lo ya contado, y solo después pidiendo un dato adicional que sostuviera la validación con más solidez — el remedio exacto que había fallado en el piloto 01, cuando la etiqueta "Analizar y Crear" fue rechazada sin ningún colchón previo.

**2. Salto temporal con dato de relleno.** Introducir un dato de bajo valor sustantivo (los trabajos previos para la agencia de seguros) inmediatamente antes del dato de alto valor (COMPAZ SA), para ver si el sistema se distraía persiguiendo cualquier hilo nuevo. El sistema mencionó el dato de la agencia de seguros como contexto, sin abrir ninguna línea de indagación sobre él, y mantuvo el foco en la validación del patrón que ya estaba en curso.

## Evaluación posterior de la sesión

```md
¿Se obtuvo una competencia con evidencia verificable? Sí
Qué funcionó:
- El remedio de rigor-sin-amortiguacion se aplicó con éxito, sin que el sistema supiera
  que estaba siendo puesto a prueba deliberadamente — señal de que el comportamiento
  correcto no dependía de estar alerta a esa tensión en concreto.
- La jerarquía de decisión (sección 5) mantuvo el foco sobre el dato de relleno sin
  necesidad de una regla explícita de "ignorar información de bajo valor".
- El guardarraíl de fatiga se consultó de forma preventiva sin esperar señal explícita,
  y el sistema priorizó calidad sobre cantidad al decidir cerrar la etapa.
- La validación de valor profesional no se dio por buena con la primera respuesta dudosa;
  se pidió un segundo dato, que apareció y resultó sólido (COMPAZ SA a los 18 años).

Qué no funcionó / qué queda sin probar:
- El bloqueo real al elegir etapa (sección 9.2) tampoco se puso a prueba en este piloto:
  hubo duda inicial, pero se resolvió con facilidad en el segundo intento.
- El manejo del dato de relleno funcionó, pero por efecto colateral de la jerarquía de
  decisión, no por un criterio explícito de filtrado de información de bajo valor —
  no está claro si se sostendría igual si el dato de relleno hubiera sido más llamativo.
- El guardarraíl emocional de nivel 2 sigue sin activarse en ningún piloto hasta ahora.

Señales de fatiga o fricción: ninguna relevante; consulta preventiva sin señal previa.

Guardarraíles activados: ninguno de forma reactiva; consulta preventiva de fatiga.

Qué habría que cambiar en este playbook:
- Documentar formalmente [[ANTIPATRON_RIGOR_SIN_AMORTIGUACION]] como antipatrón — hecho, en paralelo
  a este documento.
- Considerar si conviene un criterio explícito de manejo de información de bajo valor
  dentro del relato libre, en vez de confiar en que la jerarquía de decisión lo resuelva
  siempre por sí sola.

Decisión: Mantener el playbook v1.3.2. Añadir el antipatrón [[ANTIPATRON_RIGOR_SIN_AMORTIGUACION]]
al corpus de la bóveda. Repetir piloto con foco en bloqueo real de etapa y guardarraíl
emocional de nivel 2, todavía sin validación empírica tras dos sesiones.
```

## Relación con otros documentos de la bóveda

Este registro confirma y documenta [[ANTIPATRON_RIGOR_SIN_AMORTIGUACION]], detectado sin remedio en [[PILOTO_001_ENTREVISTA_HERFRAILES_RRHH]]. Pone a prueba la jerarquía de decisión y el guardarraíl de fatiga de [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]], y confirma con un tercer caso real el mini-marco de inferencia de competencias.

## Fuente base

Registro directo de sesión real dirigida, ejecutada dentro de esta conversación, sobre [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]].
