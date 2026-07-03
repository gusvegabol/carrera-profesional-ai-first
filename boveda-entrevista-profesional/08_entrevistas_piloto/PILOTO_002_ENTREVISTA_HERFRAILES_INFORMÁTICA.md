# Piloto 02 — Entrevista real: Herfrailes SL

## Qué es este documento

Es el primer registro de una entrevista real, no simulada, ejecutando [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]] de principio a fin con una persona real y sin que el sistema controlara de antemano hacia dónde iba a ir la conversación.

Se diferencia de [[EJEMPLO_SESION_COMPLETA_ANOTADA]] en un punto esencial: aquel fue un ensayo escrito por el propio sistema, diseñado para tensionar puntos débiles conocidos. Este es el primer dato empírico real que tiene la bóveda. Todo lo que revele — bueno o malo — vale más que cualquier simulación anterior, precisamente porque nadie sabía el resultado de antemano.

Contiene datos personales reales: nombre de empresa, cifras de negocio, información de salud, y una decisión familiar delicada. Se conserva tal cual porque es exactamente el tipo de material que el sistema está diseñado para producir — pero conviene decidir con cuidado dónde y cómo se almacena este documento en concreto, de forma distinta al resto de la bóveda, que es material de diseño, no de personas reales.

## Nota técnica: anomalía observada

Durante toda la sesión, un bloque de texto correspondiente al contenido del proyecto (aparentemente parte del contexto o instrucciones del sistema) se coló al inicio de siete de los mensajes del usuario, de forma repetida. Se descartó como causa el portapapeles y el reinicio de la aplicación. Queda pendiente de diagnóstico por parte del usuario, probablemente relacionado con la configuración del proyecto. No afectó al contenido sustantivo de la entrevista ni al registro de estado del sistema — cada aparición fue identificada y descartada en el momento, sin interrumpir el hilo real de la conversación. Se deja constancia aquí como posible caso de interés técnico para el diseño de sesiones futuras: un entrevistador-IA debe poder distinguir contenido de instrucción filtrado por error del contenido real de la persona, y seguir adelante sin que la anomalía contamine el resultado. En este piloto, esa distinción se sostuvo bien.

## Metadatos

- Fecha: sesión única, en el marco de esta conversación.
- Versión de playbook ejecutada: [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]].
- Tipo: piloto real, primera ejecución con persona real.
- Etapa elegida: trabajo en Herfrailes SL, área de informática.
- Resultado: unidad profesional de valor completa, con validación triple confirmada.

---

## Resumen del recorrido de la entrevista

**Apertura y elección de etapa.** Sin bloqueo — la persona eligió etapa de forma directa e inmediata ("mi trabajo en Herfrailes SL dentro del área de informática"). El hueco pendiente de la sección 9.2 del playbook (protocolo ante "no se me ocurre nada") sigue sin ponerse a prueba en este piloto.

**Relato libre.** La persona desplegó, en un único mensaje, un volumen alto de logros técnicos: VPN entre tiendas, gestión de tareas en Trello, aplicación a medida en VB.Net con automatización de pedidos, reducción de plantilla de Administración de 5 a 2 personas, programa de flujo de caja, impresión remota inteligente, archivo centralizado vía escáner. El sistema aplicó el guardarraíl de exceso de amplitud (sección 11): en vez de indagar sobre cada elemento, reconoció el volumen, explicó por qué convenía elegir un solo hilo, y pidió a la persona que señalara cuál sentía más relevante — dejando el resto anotado, no descartado.

**Activación de patrón.** Se activó [[PATRON_STAR_AMPLIADO]] sobre la aplicación "Herfrailes Gestión", identificada por la propia persona como lo más costoso de construir.

**Guardarraíl emocional — nivel 1.** Al mencionar la persona, sin que se le preguntara directamente, que la dedicación le "pasó factura en salud", el sistema no continuó con la indagación técnica de inmediato. Ofreció explícitamente parar, profundizar, o seguir con la parte técnica, dejando la decisión a la persona. La persona optó por continuar y ampliar.

**Profundización de contexto.** La persona reveló, de forma voluntaria y sin que se le preguntara directamente, un cuadro más amplio: empresa familiar al borde del cierre, sobrecarga por asumir Operaciones, RRHH, Informática y parte de Administración y Finanzas sin personal a quien delegar, problemas de sueño y cierto grado de depresión asociados a las horas de trabajo fuera de su jornada. El sistema reconoció explícitamente la magnitud de lo compartido antes de continuar, y volvió a ofrecer la decisión de profundizar o retomar la parte técnica — sin insistir en ninguna dirección.

**Resolución de la tensión personal.** La persona relató, también de forma voluntaria, la decisión familiar de vender la empresa, con tres alternativas consideradas explícitamente antes de decidir. En el relato apareció una valoración política sobre la legislación laboral española; el sistema no entró a valorarla y se mantuvo neutral, centrándose en la decisión familiar y su desenlace.

**Cierre emocional positivo.** La persona describió el desenlace como positivo — recuperación de salud y bienestar familiar tras la venta, primeras vacaciones sin el teléfono de empresa. El sistema no forzó más indagación en esa zona una vez confirmado el cierre.

**Retorno al hilo técnico y matiz de delegación.** Al preguntarse por la habilidad detrás de la historia, la persona corrigió espontáneamente una asunción implícita del sistema: no construyó la VPN, la delegó de forma consciente en un proveedor externo tras identificar que era la mejor solución. Este matiz llegó sin que el sistema tuviera que forzar ninguna pregunta de aislamiento de mérito — el antipatrón [[ANTIPATRON_AISLAMIENTO_FORZADO_DEL_MERITO]] no llegó a activarse porque no hizo falta.

**Formulación y validación triple.** Primera respuesta de competencia ("Analizar y Crear") tratada como etiqueta genérica, según la sección 10 del playbook. Se pidió un ejemplo concreto, se reformuló con los tres elementos (acción observable, contexto de dificultad, criterio de valor), y se devolvió a la persona para confirmación explícita — no se dio por válida solo por sonar razonable. Validación factual y de competencia confirmadas sin fricción. Validación de valor profesional confirmada con transferencia real a un contexto ajeno: la persona identificó el mismo patrón de trabajo en su etapa como concejal de Hacienda del Ayuntamiento de Gáldar, sin relación con informática.

---

## Ficha de salida

```md
## Competencia detectada
Nombre corto: Diagnóstico y resolución autónoma de problemas operativos
Formulación observable: Ante un problema o carencia operativa, analiza la situación,
decide si conviene resolverla con una solución externa o construyéndola él mismo,
la implanta si se hace cargo, y la mejora de forma continua en el tiempo.
Versión humana: "Analizo la situación, detecto el problema, detecto las necesidades,
planteo soluciones, busco si puede venir de fuera o tengo que hacerla yo, implanto
la solución, hago seguimiento y mejoro continuamente la herramienta."

## Evidencia principal
Situación: Herfrailes SL, empresa familiar de supermercados al borde del cierre por
pérdidas grandes; asumió Operaciones, RRHH, Informática y parte de Administración
y Finanzas casi en solitario.
Acción propia: diseñó y construyó desde cero "Herfrailes Gestión" (VB.Net), automatizando
pedidos, métricas y el 95% de procesos administrativos; identificó que la VPN entre
tiendas era mejor resolverla con un proveedor externo y la delegó de forma consciente.
Resultado: reducción de plantilla de Administración de 5 a 2 personas; la empresa pasó
de pérdidas grandes a solvencia en 3 años.

## Contexto
Etapa profesional: responsable de Informática con funciones ampliadas a Operaciones,
RRHH y parte de Administración/Finanzas, en empresa familiar.
Dificultades: sobrecarga por asumir múltiples áreas sin personal a quien delegar;
coste personal en salud (sueño, cierto grado de depresión) por horas fuera de su horario.

## Validaciones
Factual: confirmada ("sí, se ajusta").
De competencia: confirmada, con matiz relevante sobre delegación consciente de la VPN.
De valor profesional: confirmada con transferencia a un contexto ajeno — el mismo
método aplicado como concejal de Hacienda en el Ayuntamiento de Gáldar.

## Calidad de la evidencia
Fuerte. Cifras verificables (reducción de plantilla, solvencia en 3 años), decisión
consciente de delegación, y confirmación de transferibilidad a otro dominio.

## Qué no debe afirmarse todavía
El caso de Gáldar se menciona como confirmación, pero no se ha reconstruido con
evidencia completa — no sabemos aún la situación, acción y resultado concretos ahí.

## Pendiente para una segunda sesión
Reconstruir con el mismo nivel de detalle el caso del Ayuntamiento de Gáldar, para
confirmar si el patrón se sostiene igual de bien fuera del entorno informático.
Explorar el resto de logros mencionados en el relato libre inicial (VPN, Trello,
flujo de caja, archivo centralizado) que quedaron anotados pero no profundizados.
```

---

## Evaluación posterior de la sesión

```md
¿Se obtuvo una competencia con evidencia verificable? Sí
Qué funcionó:
- El guardarraíl de exceso de amplitud evitó dispersión ante un relato inicial muy denso.
- El guardarraíl emocional (nivel 1) se activó de forma proporcionada ante una revelación
  no solicitada, ofreciendo consentimiento explícito sin sobreactuar ni ignorar la señal.
- El mini-marco de inferencia evitó dar por buena una etiqueta genérica ("Analizar y Crear")
  sin antes concretarla con ejemplo real.
- La validación triple detectó y aceptó un matiz espontáneo de la persona (la delegación
  de la VPN) sin necesidad de forzar ninguna pregunta adicional.
- El sistema mantuvo el hilo real de la conversación pese a una anomalía técnica repetida
  (bloque de texto ajeno colándose en varios mensajes), sin que contaminara el registro
  de estado ni el resultado final.

Qué no funcionó / qué queda sin probar:
- El protocolo de bloqueo al elegir etapa (sección 9.2) sigue sin validación real,
  porque en este piloto no hubo bloqueo.
- El antipatrón [[Aislamiento forzado del mérito]] no se puso a prueba, porque la persona
  aportó el matiz de delegación sin que hiciera falta forzar ninguna pregunta de aislamiento.
  Esto es una buena señal, pero no es lo mismo que comprobar el remedio bajo tensión real.
- El guardarraíl emocional de nivel 2 (reconocimiento explícito de límites del sistema)
  no se activó, porque el nivel 1 fue suficiente en este caso. Sigue sin validación real.

Señales de fatiga o fricción: ninguna relevante detectada durante la sesión.

Guardarraíles activados: exceso de amplitud, emocional (nivel 1).

Qué habría que cambiar en este playbook:
- Ninguna corrección urgente identificada a partir de este piloto. Se recomienda un
  segundo piloto que sí ponga a prueba el hueco de la sección 9.2 y, si es posible,
  una situación con más tensión en la atribución de mérito para validar de verdad
  el remedio de [[Aislamiento forzado del mérito]].

Decisión: Mantener el playbook v1.3.2 sin cambios estructurales. Repetir piloto
con foco en los puntos no probados.
```

---

## Lo que este piloto aporta a la bóveda

Es la primera confirmación empírica, aunque de una sola sesión, de que el corazón del sistema late: una persona real, sin guion previo, llegó a una competencia con evidencia verificable y validación triple genuina, incluyendo transferencia espontánea a un contexto completamente distinto (política municipal frente a informática de empresa privada) — la señal más fuerte posible de que no se trataba de una competencia inventada para la ocasión, sino de un patrón real de comportamiento.

También deja claro que dos zonas del playbook siguen siendo teóricas, no probadas: el protocolo de bloqueo al elegir etapa, y el guardarraíl emocional de nivel 2. Ninguno de los dos falló — sencillamente no se activaron, porque las condiciones de este piloto no los requirieron.

## Relación con otros documentos de la bóveda

Este registro pone a prueba [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]], confirma el criterio de [[PATRON_STAR_AMPLIADO]] y el mini-marco de inferencia de competencias, valida en condiciones reales el guardarraíl de exceso de amplitud y el guardarraíl emocional en su nivel 1, y aporta la primera evidencia real —aunque indirecta, por ausencia de tensión— a favor del remedio documentado en [[ANTIPATRON_AISLAMIENTO_FORZADO_DEL_MERITO]].

## Fuente base

Registro directo de sesión real ejecutada dentro de esta conversación, sobre [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]].
