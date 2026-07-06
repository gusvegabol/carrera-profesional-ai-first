# Definición MVP — Playbook de cobertura profesional (v1.0.2 — síntesis) (Claude)

## Estado de este documento

Síntesis de dos líneas de diseño independientes, producidas sin comunicación directa entre las dos IA, con Gustavo como único nodo de integración:

- [[DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v1]] (ChatGPT) — aporta la taxonomía de zonas, el riesgo de falsa cobertura, y un primer banco de preguntas de apertura y cierre.
- [[DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_1]] (Claude) — aporta la arquitectura multi-sesión, el artefacto de checkpoint, la calibración de tiempo y el protocolo de reanudación.

Ninguna de las dos versiones anteriores queda invalidada por esta — se conservan como registro del proceso. Este documento es la primera versión que intenta sostener ambas capas de problema a la vez: qué debe distinguir una sesión de cobertura por dentro, y cómo sobrevive esa sesión al hecho de repartirse en el tiempo.

Nombre de fichero provisional. Sigue pendiente de que Gustavo decida convención definitiva de versión (esta síntesis podría pasar a ser `v1_1`, `v1_2_IA`, u otro nombre, siguiendo el patrón ya usado en `PLAYBOOK_ENTREVISTA_PROFESIONAL` para versiones de síntesis).

---

## 0. Nota de procedencia

Para no perder trazabilidad de qué idea vino de dónde:

| Elemento | Origen |
|---|---|
| Orquestador multi-sesión, no intra-sesión | Claude |
| Pregunta de calibración de tiempo al abrir | Claude |
| Artefacto de checkpoint fino + protocolo de reanudación (caso A/B, excepción explícita) | Claude |
| Vocabulario de tres — ahora cuatro — zonas (explorada / candidata / parcial / pendiente) | ChatGPT (tres) + Claude (añade "parcial" como estado de inmersión interrumpida) |
| Riesgo de "falsa cobertura" nombrado explícitamente | ChatGPT |
| Banco de preguntas de apertura panorámica | ChatGPT |
| Banco de preguntas de cierre con puerta nueva | ChatGPT, alineado con [[ANTIPATRON_CIERRE_ANCLADO_AL_HILO_UNICO]] (Claude añade la referencia) |
| Estructura de salida mínima con advertencia de límite | ChatGPT |
| Fuera de alcance explícito, estilo v1.3.2 §8 | Claude |

---

## 1. Definición breve

**Cobertura profesional MVP** es la capa de entrevista, repartida en varias sesiones, que permite construir un mapa inicial y consciente de sus límites de las zonas profesionales de una persona: qué está explorado con evidencia suficiente, qué ha aparecido como señal sin desarrollarse todavía, qué inmersión quedó a medias, y qué sigue sin tocar.

Su función no es saberlo todo. Es evitar dos errores simétricos: tratar una competencia profunda aislada como si representara toda la trayectoria (falsa cobertura), y perder el hilo de una exploración interrumpida por no haber quedado registrada (falso reinicio).

---

## 2. Principio de partida: dos capas con dueño distinto

- **[[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]]** sigue siendo el especialista de profundidad: una etapa, una competencia, con evidencia verificable. No cambia nada de su diseño actual.
- **Cobertura** es el orquestador: explora la vida profesional a través de varias sesiones, decide cuándo hay zona fértil, invoca v1.3.2 completo como sub-proceso, y mantiene el mapa de zonas entre sesiones.

La relación es la misma que ya opera dentro de v1.3.2 §9.4 (si aparece X, activa el patrón Y), llevada un nivel arriba: si el escaneo de cobertura encuentra zona fértil, activa v1.3.2 entero.

---

## 3. Vocabulario de zonas

Cuatro estados, no tres ni dos — la fusión de ambas versiones exige distinguir "señal sin trabajar" de "inmersión interrumpida a medias", que son cosas distintas con remedio distinto:

- **Explorada**: pasó por una inmersión completa de v1.3.2, con competencia validada (validación triple, §13 de v1.3.2).
- **Candidata**: apareció como señal durante la conversación (panorámica de apertura, o de pasada dentro de otra inmersión) pero no se ha entrado todavía. Ejemplos de cómo se manifiesta: *"también trabajé en otra empresa, pero fue menos importante"*, *"eso no era mi trabajo principal, pero acabé resolviéndolo yo"*.
- **Parcial**: hubo una inmersión de v1.3.2 activa que se interrumpió antes de cerrar — con checkpoint fino guardado (ver sección 9).
- **Pendiente**: no mencionada, no explorada, posiblemente invisible para la propia persona (trabajo minimizado, etapa no verbalizada, responsabilidad no reconocida como tal).

Candidata y parcial no son intercambiables: una candidata nunca se ha empezado a trabajar (no hay checkpoint que recuperar, solo una señal); una parcial sí tiene una inmersión en curso con estado guardado. Confundirlas llevaría a intentar "reanudar" una candidata como si tuviera un punto exacto de corte que nunca existió.

---

## 4. Riesgo central: falsa cobertura

Aparece cuando una entrevista produce una competencia profunda real y valiosa, y el sistema — o quien lea la salida — actúa como si esa competencia representara suficientemente toda la trayectoria de la persona.

Es la misma raíz empírica que ya documenta [[ANTIPATRON_CIERRE_ANCLADO_AL_HILO_UNICO]] a partir de [[PILOTO_005_ENTREVISTA_REPONEDOR_SUPERMERCADO]]: una sesión puede sentirse completa y satisfactoria desde dentro, con las tres validaciones cumplidas, y aun así dejar fuera una dimensión entera de la competencia objetivo, sin ninguna señal textual que lo delate.

Toda salida de cobertura MVP debe llevar, de forma explícita, una advertencia de límite. Ejemplo de redacción:

> "Hemos explorado con profundidad la etapa X y extraído la competencia Y. Quedan sin explorar las etapas A y B, y han aparecido como candidatas las zonas C y D. Este resultado no debe leerse como mapa completo de la trayectoria."

---

## 5. Arquitectura: orquestador multi-sesión

Decisión explícita, no por defecto: el MVP de cobertura es multi-sesión, no una sesión larga que escanea y profundiza varias veces seguidas.

Razones:

- el tiempo de la entrevista lo marca el humano, no la IA;
- encadenar varias inmersiones completas de v1.3.2 en una sola sesión repetiría, a escala mayor, el riesgo que ya documentan [[FRICCION_FATIGA_DEL_USUARIO]] y [[ANTIPATRON_SECUENCIAS_SIN_PAUSAS]], sin que ningún piloto lo haya probado nunca;
- v1.3.2 §8 ya declara "reconstrucción completa de carrera" fuera de su alcance.

Cada sesión de cobertura contiene, como máximo, una inmersión completa de v1.3.2. El resto del tiempo de sesión es escaneo panorámico, decisión de por dónde seguir, y cierre con puerta nueva.

---

## 6. Apertura de sesión

Toda sesión de cobertura abre con dos movimientos, en este orden:

**a) Calibración de tiempo** (Claude), una sola vez, antes de cualquier otra cosa:

> "¿Cuánto tiempo tienes hoy? Podemos ir a fondo si dispones de un rato largo, o ir con calma sabiendo que seguiremos otro día — tú decides, y puedes parar cuando quieras sin tener que explicarme por qué."

Opcional de responder. Si se declara un tiempo limitado, reduce el peso probatorio de las señales de [[FRICCION_FATIGA_DEL_USUARIO]] mientras estén explicadas por ese tiempo, en vez de leerse automáticamente como fatiga real. No hay vigilancia activa de reloj — el sistema no tiene acceso a timestamp real por mensaje (verificado en sesión de diseño previa) — solo chequeos puntuales en los puntos de transición naturales del playbook.

**b) Apertura panorámica** (ChatGPT), si es la primera sesión o si el mapa tiene zonas pendientes sin señal todavía: preguntas de bajo coste que recorren varias etapas sin profundizar en ninguna, orientadas a poblar el mapa de zonas candidatas antes de decidir dónde entrar. Banco de partida:

- ¿Qué etapas o trabajos ha tenido tu trayectoria hasta ahora, a grandes rasgos?
- ¿Hay algún trabajo o etapa que te parezca menor pero que en realidad ocupó bastante de tu tiempo?
- ¿Hay alguna responsabilidad que asumiste sin que estuviera en tu cargo formal?
- ¿Hay algo que sueles minimizar cuando hablas de tu trabajo?

Esto es un punto de partida, no un criterio cerrado — ver sección 7.

---

## 7. Escaneo de zona fértil (sigue parcialmente abierto)

El banco de preguntas panorámicas de la sección 6b da material bruto, pero no resuelve del todo el criterio operativo que distingue, dentro de una respuesta panorámica, "aquí probablemente hay algo" de "esto fue administrativo, sin mucho que sacar" — el equivalente, para cobertura, de lo que v1.3.2 §9.4 ya resuelve para profundidad activada dentro de un relato.

**Queda como pregunta abierta de este MVP.** Candidato razonable a explorar en una siguiente sesión de diseño: tratar cualquier respuesta panorámica con una acción concreta mencionada, aunque sea de pasada, como candidata por defecto — y dejar que sea la propia persona quien, al ofrecerle elegir entre candidatas, decida cuál merece profundizarse primero. Esto evitaría que el sistema tenga que juzgar fertilidad por sí solo, trasladando la decisión a quien mejor la puede hacer.

---

## 8. Profundización selectiva

A partir del mapa de zonas, se elige una candidata (o se retoma una parcial, ver sección 10) y se invoca [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]] completo, sin modificar nada de su diseño interno. El presupuesto de tiempo declarado en la apertura viaja como contexto heredado; v1.3.2 no vuelve a preguntarlo.

---

## 9. Artefacto de estado de cobertura

Mapa vivo, persistente entre sesiones, con al menos:

- lista de zonas con su estado (explorada / candidata / parcial / pendiente);
- para cada zona explorada: referencia a la ficha mínima de v1.3.2 §14 correspondiente;
- para cada zona parcial: checkpoint fino con el mismo nivel de detalle que v1.3.2 §7 — patrón activo, paso exacto, evidencia clasificada (hecho / interpretación / hipótesis / pendiente), guardarraíles activados, fatiga acumulada hasta el corte;
- para cada zona candidata: la señal textual que la originó y la sesión en que apareció.

**Ubicación**: dentro de la bóveda (`boveda-entrevista-profesional/`), no en `.pcs/`. Carpeta y nombre de fichero concretos siguen pendientes de decisión de Gustavo — no se ha creado ninguna estructura nueva.

---

## 10. Protocolo de reanudación

**Caso A — no había inmersión activa.** Se informa del mapa de zonas actual (explorada / candidata / pendiente) y se pregunta por dónde seguir, incluyendo la opción de abrir una candidata ya detectada.

**Caso B — había una inmersión v1.3.2 interrumpida (zona parcial).**

- Comportamiento por defecto: no se retoma automáticamente en el punto exacto. Se informa con honestidad de que quedó parcial, se mantiene como tal en el mapa, y retomarla se trata como una nueva decisión de cobertura.
- Excepción explícita: si el humano pide continuar desde el punto exacto ("no quiero repetirlo todo"), prevalece — coherente con la jerarquía de v1.3.2 §5. Se hace una recapitulación breve de verificación con lo que el checkpoint tiene guardado, se corrige si hace falta, y se continúa en el siguiente paso del patrón activo. Si el checkpoint no tiene ese nivel de detalle, se dice con honestidad y se ofrece reconstruir brevemente.
- El primer turno tras cualquier reanudación no es información suficiente por sí solo para diagnosticar fatiga o incomodidad — hace falta un segundo turno para confirmar si es patrón o solo el efecto de reengancharse a algo dejado a medias.

---

## 11. Cierre de cobertura: puerta nueva explícita

Antes de cerrar una sesión, movimiento propio y separado de cualquier validación de lo ya trabajado — nunca la misma pregunta que valida transferibilidad, siguiendo exactamente el remedio de [[ANTIPATRON_CIERRE_ANCLADO_AL_HILO_UNICO]]:

> "Antes de cerrar del todo: ¿hay alguna otra parte de tu trabajo, sin relación con esto que hemos hablado, que también muestre algo de cómo trabajas?"

Banco adicional de preguntas de cierre (ChatGPT), útiles para poblar zonas candidatas nuevas antes de terminar:

- ¿Qué parte de tu trayectoria no hemos tocado hoy?
- ¿Hay alguna etapa que no hemos explorado porque parecía menos interesante?
- ¿Qué quedaría injustamente fuera si cerráramos aquí?

---

## 12. Salida mínima esperada

1. **Competencia extraída** (si la hubo esta sesión): nombre, evidencia, zona de procedencia — ficha mínima de v1.3.2 §14.
2. **Mapa de zonas actualizado**: explorada / candidata / parcial / pendiente.
3. **Advertencia de límite** (sección 4): qué no debe concluirse todavía a partir de lo explorado hasta ahora.
4. **Siguiente exploración recomendada**, si la hay, con motivo breve de por qué esa zona parece relevante.
5. **Checkpoint fino**, si la sesión cerró con una inmersión a medias.

---

## 13. Qué queda explícitamente fuera de este MVP

- criterio operativo cerrado de "zona fértil" en el escaneo panorámico (sección 7 — solo heurística de partida);
- más de una inmersión completa de v1.3.2 por sesión;
- vigilancia activa de tiempo real transcurrido (no hay timestamp fiable disponible);
- comportamiento ante desaparición silenciosa sin parada señalizada;
- formato de fichero cerrado y ubicación exacta del artefacto de estado (sección 9);
- reconstrucción completa de carrera o certificación de perfil — el mapa es inicial y razonable, no exhaustivo, siguiendo el propio [[CONCEPTO_COBERTURA_PROFESIONAL]].

---

## 14. Fricción nueva identificada, pendiente de documentar formalmente

Brevedad o ritmo acelerado motivado por una restricción de tiempo conocida de antemano por el humano, que sin declaración explícita puede leerse erróneamente como fatiga desde el inicio — distinta de [[FRICCION_FATIGA_DEL_USUARIO]] (desgaste acumulado) y de [[FRICCION_AMBIGUEDAD_PARQUEDAD_O_DESINTERES]] (brevedad sin causa determinable). El remedio ya está incorporado en la sección 6a. Queda pendiente, si Gustavo lo autoriza, redactarla como documento propio en `05_fricciones_y_antipatrones/`.

---

## 15. Preguntas abiertas que ninguna de las dos versiones anteriores resuelve

- Criterio cerrado de zona fértil en el escaneo (sección 7).
- Qué ocurre si, durante una inmersión de profundidad ya activada, aparece una señal candidata de otra zona distinta — ¿se anota para después sin interrumpir, o se ofrece elegir en el momento? Ninguna de las dos versiones lo trató.
- Cuántas candidatas o pendientes puede sostener el mapa antes de que mostrarlo completo al humano sea, en sí mismo, una fuente de fatiga motivacional (ver [[FRICCION_FATIGA_DEL_USUARIO]], tercera forma).

---

## 16. Relación con otros documentos de la bóveda

- [[CONCEPTO_COBERTURA_PROFESIONAL]] — definición conceptual de la que este documento es la arquitectura.
- [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]] — especialista de profundidad invocado, sin modificar.
- [[ANTIPATRON_CIERRE_ANCLADO_AL_HILO_UNICO]] — origen empírico del riesgo de falsa cobertura y del remedio de puerta nueva.
- [[CONCEPTO_ARCO_DE_SESION]] — orquestación dentro de una sesión; este documento extiende su lógica al nivel entre sesiones.
- [[FRICCION_FATIGA_DEL_USUARIO]], [[FRICCION_AMBIGUEDAD_PARQUEDAD_O_DESINTERES]], [[ANTIPATRON_SECUENCIAS_SIN_PAUSAS]] — umbral de activación modificado por el tiempo declarado, sin cambio en su contenido propio.
- [[DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v1]] y `..._v1_0_1` — las dos versiones fuente de esta síntesis.

## Fuente base

Síntesis elaborada por Claude a partir de [[DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v1]] (ChatGPT) y [[DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_1]] (Claude), por instrucción directa de Gustavo, 2026-07-06.
