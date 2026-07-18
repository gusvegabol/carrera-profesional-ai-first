# Definición MVP — Playbook de cobertura profesional (v1.0.1) (Claude)

## Estado de este documento

Primera definición operativa del MVP de cobertura profesional, construida en sesión de trabajo con Claude, a partir de [[CONCEPTO_COBERTURA_PROFESIONAL]] y de la experiencia empírica de [[PILOTO_005_ENTREVISTA_REPONEDOR_SUPERMERCADO]] y [[ANTIPATRON_CIERRE_ANCLADO_AL_HILO_UNICO]].

Existe en paralelo una definición de MVP generada por ChatGPT, a partir de una conversación distinta. Este documento no intenta reconciliarse con aquella ni sustituirla — es la línea de diseño trabajada específicamente con Claude, como parte del experimento deliberado de mantener ambas IA sin comunicación directa entre sí, con Gustavo como único nodo de integración. La comparación y eventual síntesis entre ambas es una decisión pendiente que corresponde solo a Gustavo.

Este documento no es un playbook ejecutable todavía — es la definición de alcance y arquitectura que un futuro `PLAYBOOK_COBERTURA_PROFESIONAL` debería implementar, siguiendo el mismo criterio de progresión que ya se usó con profundidad: concepto → patrón/arquitectura → playbook operativo.

---

## 1. Principio de partida

Cobertura no es una versión ampliada de profundidad. Es una capa distinta, con dueño distinto:

- **[[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]]** sigue siendo el especialista de profundidad: una etapa, una competencia, con evidencia verificable. No cambia nada de su diseño actual.
- **Cobertura** es el orquestador: explora la vida profesional del usuario a través de varias sesiones, decide cuándo hay una zona fértil, y en ese momento invoca v1.3.2 completo como sub-proceso.

La relación es la misma que ya existe dentro de v1.3.2 §9.4 (si aparece X, activa el patrón Y), llevada un nivel arriba: si el escaneo de cobertura encuentra zona fértil, activa v1.3.2 entero.

---

## 2. Arquitectura: orquestador multi-sesión, no intra-sesión

Decisión explícita, no por defecto: el MVP de cobertura es **multi-sesión**, no una sesión larga que escanea y profundiza varias veces seguidas.

Razones:

- el tiempo de la entrevista lo marca el humano, no la IA — nadie se sienta dos o cuatro horas seguidas a contar toda su vida profesional;
- encadenar varias inmersiones completas de v1.3.2 en una sola sesión repetiría, a escala mayor, exactamente el riesgo que ya documentan [[FRICCION_FATIGA_DEL_USUARIO]] y [[ANTIPATRON_SECUENCIAS_SIN_PAUSAS]], sin que ningún piloto lo haya probado nunca;
- v1.3.2 §8 ya declara "reconstrucción completa de carrera" fuera de su alcance — forzar varias inmersiones seguidas en una sesión violaría esa frontera ya decidida.

Cada sesión de cobertura puede, por tanto, contener como máximo una inmersión completa de v1.3.2. El resto del tiempo de sesión es escaneo, decisión de por dónde seguir, y cierre.

**Queda fuera de este MVP** (siguiendo el mismo criterio de v1.3.2 §8): diseñar un criterio de fatiga acumulada entre varias inmersiones dentro de una misma sesión. Si en el futuro se decide permitir más de una inmersión por sesión, eso exige una revisión explícita de esta definición, no una extensión silenciosa.

---

## 3. Escaneo de zona fértil

Antes de invocar v1.3.2, cobertura necesita un mecanismo propio, más ligero que cualquiera de los tres patrones existentes, para recorrer varias etapas o experiencias sin profundizar todavía, y distinguir "aquí probablemente hay algo" de "esto fue administrativo, sin mucho que sacar".

**Esto queda como pregunta abierta de este MVP.** No se ha definido todavía el criterio operativo de "zona fértil" al nivel de escaneo — es el equivalente, para cobertura, de lo que v1.3.2 §9.4 ya resuelve para profundidad. Se deja pendiente de una siguiente sesión de diseño, posiblemente como un cuarto patrón de la bóveda (`04_patrones_de_preguntas/`) o como sección propia de un futuro playbook de cobertura.

---

## 4. Artefacto de estado de cobertura

Cobertura necesita un mapa vivo, persistente entre sesiones, que registre qué zonas de la trayectoria están:

- **cubiertas** (ya pasaron por una inmersión completa de v1.3.2, con competencia validada);
- **parciales** (hubo escaneo o incluso una inmersión interrumpida, sin cierre completo);
- **pendientes** (no exploradas todavía).

**Ubicación**: dentro del host anfitrión `carrera-ai`, en la bóveda (`boveda-entrevista-profesional/`), no en `.pcs/` — siguiendo la distinción que ya opera en el proyecto entre memoria operativa de PCS sobre el host y la verdad del propio proyecto anfitrión. La carpeta y el nombre de fichero concretos quedan pendientes de que Gustavo los decida; no se ha creado ninguna estructura nueva todavía.

**Contenido mínimo necesario** (sin diseño de formato cerrado todavía):

- mapa de zonas con su estado (cubierta / parcial / pendiente);
- si hay una inmersión de v1.3.2 interrumpida: su checkpoint fino, con el mismo nivel de detalle que v1.3.2 §7 ya usa para su propio registro de estado — patrón activo, paso exacto dentro del patrón, evidencia ya clasificada (hecho / interpretación / hipótesis / pendiente), guardarraíles ya activados, fatiga acumulada hasta el corte.

La diferencia de granularidad entre "mapa de zonas" y "checkpoint fino" no es opcional: sin el checkpoint fino, no es posible atender la petición legítima del humano de retomar una inmersión exactamente donde se dejó (ver sección 6).

---

## 5. Apertura de sesión de cobertura

Toda sesión de cobertura, tanto la primera como cualquier reanudación, abre con una única pregunta de calibración de tiempo, antes de cualquier otra cosa:

> "¿Cuánto tiempo tienes hoy? Podemos ir a fondo si dispones de un rato largo, o ir con calma sabiendo que seguiremos otro día — tú decides, y puedes parar cuando quieras sin tener que explicarme por qué."

Esta pregunta:

- se hace una sola vez, al nivel de cobertura — no se repite dentro de una inmersión de v1.3.2 activada en la misma sesión; el presupuesto de tiempo declarado viaja como contexto heredado hacia el sub-proceso;
- es opcional de responder: si el humano no la contesta o prefiere no decirlo, el sistema se comporta igual que hoy, sin ese dato;
- si se responde con un tiempo limitado, reduce el peso probatorio de las señales de [[FRICCION_FATIGA_DEL_USUARIO]] (respuestas que se acortan, preguntas sobre cuánto queda) mientras estén explicadas por el tiempo declarado, en vez de leerse automáticamente como fatiga real.

**Limitación explícita, ya verificada en esta sesión de diseño**: el sistema no tiene acceso a timestamp real por mensaje ni forma de medir cuánto tiempo transcurre entre turnos. Por tanto, no hay vigilancia activa de reloj ni cierre proactivo automático al acercarse un límite. El mecanismo válido es el chequeo puntual, con ligereza, en los puntos de transición que ya existen de forma natural en el playbook (cierre de etapa, cambio de patrón, fin de una inmersión) — nunca un cálculo de tiempo restante que el sistema no puede sostener con honestidad.

---

## 6. Protocolo de reanudación

Al retomar una sesión de cobertura, el sistema informa primero con contexto mínimo del estado guardado, y distingue dos casos:

### Caso A — no había inmersión de v1.3.2 activa

La sesión anterior se cerró entre zonas, o durante escaneo. Se informa del mapa de zonas actual y se pregunta por dónde seguir. No hay checkpoint fino que recuperar.

### Caso B — había una inmersión de v1.3.2 interrumpida a medias

Aquí el comportamiento por defecto y la excepción explícita son distintos, y ambos deben quedar disponibles:

**Comportamiento por defecto**: la inmersión no se retoma automáticamente en el punto exacto del corte. Se informa con honestidad de que quedó parcial ("la vez pasada nos quedamos a medias en X"), se registra en el mapa de zonas como *parcial*, y retomarla o no se trata como una nueva decisión de cobertura ("¿quieres seguir explorando esto, o prefieres que veamos otra zona hoy?").

**Excepción explícita**: si el humano pide directamente continuar desde el punto exacto donde se dejó ("quiero retomarlo pero desde donde lo dejamos, no quiero repetirlo todo"), eso prevalece — es una instrucción directa y consciente, coherente con la jerarquía de decisión de v1.3.2 §5 (consentimiento de la persona por encima de cualquier otro criterio). En ese caso:

1. la IA hace una recapitulación breve de verificación antes de continuar — no un reinicio, una sola confirmación corta de lo que el checkpoint tiene guardado (situación, tarea, y lo último clasificado como hecho vs. lo que quedaba como hipótesis), invitando a corregir si algo no coincide con el recuerdo del humano;
2. si se confirma, se continúa exactamente en el siguiente paso del patrón activo guardado, sin pedir que se cuente de nuevo desde el principio;
3. si el checkpoint guardado no tiene ese nivel de detalle (por ejemplo, por quedar registrado antes de que este protocolo existiera), la IA lo dice con honestidad y ofrece reconstruir brevemente antes de seguir, en vez de fingir una precisión que no tiene.

**Nota sobre el primer turno tras cualquier reanudación**: incluso siguiendo la excepción explícita, el primer turno tras retomar merece el mismo cuidado que cualquier reencuentro. Si la respuesta llega distinta en tono o extensión, un solo turno no es información suficiente para diagnosticar fatiga, incomodidad, o cualquier otra cosa — hace falta un segundo turno para confirmar si es patrón o es solo el efecto natural de reengancharse a algo que quedó a medias.

---

## 7. Qué queda explícitamente fuera de este MVP

Siguiendo el mismo criterio de frontera que usa v1.3.2 en su §8:

- criterio operativo de "zona fértil" para el escaneo (sección 3 — pendiente de diseño);
- más de una inmersión completa de v1.3.2 por sesión;
- vigilancia activa de tiempo real transcurrido (no hay acceso a timestamp fiable);
- comportamiento ante desaparición silenciosa del humano sin parada señalizada — el MVP garantiza buen comportamiento ante parada explícita; ante cierre de ventana sin aviso, el sistema hace lo que pueda con lo último escrito en el hilo, sin garantía;
- formato de fichero cerrado para el artefacto de estado de cobertura, y su ubicación exacta dentro de la bóveda (sección 4 — pendiente de decisión de Gustavo);
- reconstrucción completa de carrera o certificación de perfil profesional — cobertura MVP produce un mapa inicial razonable, no una reconstrucción total, siguiendo el propio criterio ya escrito en [[CONCEPTO_COBERTURA_PROFESIONAL]].

---

## 8. Fricción nueva identificada, pendiente de documentar formalmente

Esta sesión de diseño identificó una tercera causa de brevedad en las respuestas, distinta de las dos ya documentadas:

- [[FRICCION_FATIGA_DEL_USUARIO]]: desgaste que se acumula durante la sesión.
- [[FRICCION_AMBIGUEDAD_PARQUEDAD_O_DESINTERES]]: brevedad presente desde el primer turno, sin causa determinable por texto.
- **Nueva, sin nombre ni fichero propio todavía**: brevedad o ritmo acelerado motivado por una restricción de tiempo conocida de antemano por el humano, que sin declaración explícita puede leerse erróneamente como fatiga desde el inicio.

El remedio de esta sesión (pregunta de calibración de tiempo al abrir, sección 5) ya resuelve el caso práctico. Queda pendiente, si Gustavo lo autoriza, redactar esta fricción como documento propio en `05_fricciones_y_antipatrones/`, con la misma estructura que las otras dos. No se ha creado ese fichero en esta sesión.

---

## 9. Relación con otros documentos de la bóveda

Este documento se apoya en, y no duplica:

- [[CONCEPTO_COBERTURA_PROFESIONAL]] — la definición conceptual de la que este documento es la primera traducción hacia arquitectura;
- [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]] — el especialista de profundidad que cobertura invoca sin modificarlo;
- [[CONCEPTO_ARCO_DE_SESION]] — el criterio de orquestación dentro de una sesión, del que este documento extiende la lógica al nivel entre sesiones;
- [[ANTIPATRON_CIERRE_ANCLADO_AL_HILO_UNICO]] — el hallazgo empírico que motivó separar "validar lo construido" de "abrir puerta nueva", y que dio origen a esta línea de trabajo;
- [[FRICCION_FATIGA_DEL_USUARIO]], [[FRICCION_AMBIGUEDAD_PARQUEDAD_O_DESINTERES]], [[ANTIPATRON_SECUENCIAS_SIN_PAUSAS]] — antipatrones y fricciones existentes cuyo umbral de activación se ve modificado por el tiempo declarado (sección 5), sin que su contenido propio cambie.

## Fuente base

Deriva de sesión de trabajo con Claude, 2026-07-06, a partir de la relectura de [[CONCEPTO_COBERTURA_PROFESIONAL]], [[estado-actual]] y la sesión abierta `sesion-20260705-concepto-cobertura-profesional-carrera-ai`.
