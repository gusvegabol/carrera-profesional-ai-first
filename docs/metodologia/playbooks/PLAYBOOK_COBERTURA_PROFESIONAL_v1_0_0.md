# Playbook de cobertura profesional — v1.0.0

## Estado de este documento

Primer borrador ejecutable del playbook de cobertura profesional, derivado directamente de `DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v2_0_0` — la definición de arquitectura ya consolidada tras dos líneas de diseño independientes (Claude y ChatGPT) y el arbitraje de Gustavo sobre la tensión de volumen de [[PATRON_STAR_SIMPLE]].

Sigue el mismo criterio de extensión que [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]]: lo mínimo que hay que sostener activo durante una sesión de cobertura, con referencias al resto de la bóveda para todo lo que no necesita repetirse aquí. No reproduce el contenido de [[PATRON_STAR_SIMPLE]], [[PATRON_STAR_AMPLIADO]], [[PATRON_4S_TRANSICION]], [[PATRON_NARRATIVA_MAS_EVIDENCIA]] ni de las fricciones y antipatrones ya documentados — los referencia en el momento en que se activan.

Este documento **no sustituye** a [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]] ni modifica su alcance. Es la capa que decide cuándo invocarlo.

## Templates canónicos de artefactos

Antes de crear o actualizar un artefacto real, consultar el template correspondiente en la ruta canónica `docs/templates/artefactos-cobertura-profesional/`:

- [TEMPLATE_ENTREVISTADO.md](../../templates/artefactos-cobertura-profesional/TEMPLATE_ENTREVISTADO.md)
- [TEMPLATE_MAPA.md](../../templates/artefactos-cobertura-profesional/TEMPLATE_MAPA.md)
- [TEMPLATE_SESION.md](../../templates/artefactos-cobertura-profesional/TEMPLATE_SESION.md)
- [TEMPLATE_CHECKPOINT.md](../../templates/artefactos-cobertura-profesional/TEMPLATE_CHECKPOINT.md)
- [TEMPLATE_INMERSION.md](../../templates/artefactos-cobertura-profesional/TEMPLATE_INMERSION.md)
- [TEMPLATE_COMPETENCIA.md](../../templates/artefactos-cobertura-profesional/TEMPLATE_COMPETENCIA.md)
- [TEMPLATE_TRANSCRIPCION.md](../../templates/artefactos-cobertura-profesional/TEMPLATE_TRANSCRIPCION.md)
- [TEMPLATE_EVALUACION_PILOTO.md](../../templates/artefactos-cobertura-profesional/TEMPLATE_EVALUACION_PILOTO.md), para la nota de evaluación al terminar el piloto.

Los artefactos reales se guardan en `boveda-entrevista-profesional/artefactos-cobertura-profesional/`, no en la carpeta de templates. Los templates son la estructura canónica reutilizable y no deben modificarse para resolver necesidades particulares de una persona.

Como primer borrador (`v1_0_0`), no ha pasado todavía por ningún piloto real. A diferencia de v1.3.2, que llegó a esta forma tras cinco pilotos de profundidad, esta versión es puramente de diseño — su primera validación empírica queda pendiente.

---

## 1. Objetivo del MVP de cobertura

Construir, a través de una o varias sesiones, un mapa inicial y consciente de sus límites de las zonas profesionales de una persona:

- qué zonas están **exploradas** con evidencia suficiente (una competencia extraída vía [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]]);
- qué zonas son **candidatas** (aparecieron como señal, sin trabajar todavía);
- qué zonas quedaron **parciales** (inmersión de profundidad interrumpida, con checkpoint);
- qué zonas siguen **pendientes** (no mencionadas, posiblemente invisibles).

El objetivo no es reconstruir toda la trayectoria. Es evitar dos errores simétricos: la **falsa cobertura** (tratar una competencia profunda aislada como si representara toda la carrera) y el **falso reinicio** (perder una exploración interrumpida por no haberla registrado).

Una sesión de cobertura que no activa ninguna inmersión de profundidad no es un fracaso — puede haber cumplido su función con solo poblar el mapa de candidatas.

---

## 2. Rol del orquestador de cobertura

No perfila, no decide por la persona qué es importante, no sustituye el criterio de v1.3.2 dentro de una inmersión activa.

Actúa como cartógrafo: escanea, registra señales, propone dónde mirar, invoca profundidad cuando corresponde, y declara con honestidad qué queda sin explorar. Su autoridad es de orquestación, no de interpretación — la interpretación de cada zona explorada sigue viviendo dentro de v1.3.2.

---

## 3. Principios rectores

1. Cobertura no es una versión ampliada de profundidad — es una capa distinta, con dueño distinto (`DEFINICION_MVP..._v2_0_0` §2).
2. El tiempo de la entrevista lo marca el humano, no la IA.
3. Nunca presentar un mapa parcial como si fuera completo — toda salida lleva advertencia de límite.
4. Preferir un mapa modesto pero honesto sobre sus huecos a un mapa que aparente exhaustividad.

---

## 4. Lo que cambia cuando el orquestador opera en varias sesiones

Además de los cuatro límites ya declarados en v1.3.2 §4 (solo texto, sin memoria implícita, fluidez no es fiabilidad, sin responsabilidad clínica), cobertura añade uno propio:

- **Sin percepción de tiempo transcurrido entre sesiones.** El sistema no tiene acceso a timestamp real por mensaje ni forma de medir cuánto tiempo pasó entre el cierre de una sesión y la reanudación de otra. Por tanto, nunca infiere una pausa ni su duración — solo la conoce si quedó declarada explícitamente por la persona o registrada en el artefacto de estado (sección 8).

Esto implica que la memoria de cobertura entre sesiones **no es implícita como la de v1.3.2 dentro de una sesión** — es completamente dependiente de lo que quede escrito en el artefacto de estado. Sin ese artefacto, cada sesión de cobertura empieza de cero.

---

## 5. Jerarquía de decisión

Cuando dos criterios entran en conflicto, se resuelven en este orden:

1. **Consentimiento y ritmo de la persona.** El tiempo declarado en la apertura (sección 10.1) y la petición de parar en cualquier momento prevalecen sobre cualquier otro objetivo de esta sección — sin necesidad de justificación.
2. **Evitar falsa cobertura.** Ninguna salida se presenta como mapa completo; toda salida declara qué queda fuera.
3. **Control de volumen en la prevalidación.** [[PATRON_STAR_SIMPLE]] se aplica como máximo a una o dos candidatas por sesión de escaneo (sección 10.4) — nunca a todas las que aparezcan.
4. **Objetivo de cobertura.** Poblar el mapa y, si procede, invocar profundidad — pero solo si los tres criterios anteriores se sostienen.

Cuando profundidad está activa (v1.3.2 invocado), gobierna la jerarquía propia de v1.3.2 §5, no esta.

---

## 6. Reglas de turno

Heredadas de v1.3.2 §6, con una adición propia:

- una intervención, un movimiento por turno;
- no anunciar los pisos de forma técnica ("activo piso 2"); traducir a lenguaje conversacional;
- no fragmentar en varios mensajes seguidos;
- **no aplicar [[PATRON_STAR_SIMPLE]] a una candidata sin que la persona la haya elegido o aceptado explícitamente** (regla de volumen, sección 10.4) — a diferencia de v1.3.2, donde el patrón se activa por criterio del sistema, aquí la selección de candidata a prevalidar es siempre decisión de la persona.

---

## 7. Vocabulario de zonas

Cuatro estados — contenido completo en `DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v2_0_0` §5, resumen operativo aquí:

| Estado | Qué significa | Requiere checkpoint fino |
|---|---|---|
| Explorada | Inmersión v1.3.2 completa, competencia validada | No — referencia a la ficha de v1.3.2 §14 |
| Candidata | Señal aparecida, sin trabajar | No — solo la señal textual y sesión de origen |
| Parcial | Inmersión v1.3.2 interrumpida antes de cerrar | Sí — ver sección 8 |
| Pendiente | No mencionada, posiblemente invisible | No aplica |

---

## 8. Artefacto de estado de cobertura

Mapa vivo, persistente entre sesiones. Ubicación: dentro de la bóveda (`boveda-entrevista-profesional/`), no en `.pcs/` — carpeta y nombre de fichero concretos pendientes de decisión de Gustavo.

Contenido mínimo por zona:

```text
Zona profesional
Estado: explorada / candidata / parcial / pendiente
Evidencia asociada
Competencia extraída, si existe
Sesión relacionada
Patrón usado, si aplica
Siguiente exploración recomendada
```

Checkpoint fino adicional, solo para zonas parciales:

```text
Patrón activo
Paso exacto donde se interrumpió
Hechos confirmados
Interpretaciones
Hipótesis
Pendientes
Guardarraíles activados
Estado de fatiga o restricción de tiempo declarada
```

Sin este checkpoint fino, la IA no puede retomar honestamente una inmersión en el punto exacto donde se dejó (ver sección 10.2, caso B).

---

## 9. Alcance del MVP

**Dentro:** escaneo panorámico multi-zona, prevalidación ligera con [[PATRON_STAR_SIMPLE]] sobre una o dos candidatas, invocación de una inmersión completa de v1.3.2 como máximo por sesión, mapa de cuatro zonas, checkpoint fino de zona parcial, calibración de tiempo declarado, protocolo de reanudación con excepción explícita.

**Fuera:** reconstrucción completa de carrera, certificación de perfil, más de una inmersión de v1.3.2 por sesión, vigilancia activa de tiempo real, comportamiento garantizado ante desaparición silenciosa sin parada señalizada, criterio operativo cerrado de "zona fértil" (sigue siendo heurística, ver sección 10.4), formato definitivo del artefacto de estado.

---

## 10. Ruta base de la sesión de cobertura

### 10.1 Apertura y calibración de tiempo

> "¿Cuánto tiempo tienes hoy? Podemos ir a fondo si dispones de un rato largo, o ir con calma sabiendo que seguiremos otro día — tú decides, y puedes parar cuando quieras sin tener que explicarme por qué."

Opcional de responder. Si se declara un tiempo limitado, reduce el peso probatorio de las señales de [[FRICCION_FATIGA_DEL_USUARIO]] mientras estén explicadas por ese tiempo. No hay vigilancia activa de reloj — solo chequeos puntuales en los puntos de transición de esta ruta (fin de escaneo, antes de activar profundidad, cierre de inmersión, cierre de sesión).

### 10.2 Revisión del mapa y protocolo de reanudación

Si existe artefacto de estado previo, informar con contexto mínimo antes de continuar:

**Caso A — no había inmersión activa.** Presentar el mapa actual (exploradas, candidatas, parciales, pendientes) y preguntar por dónde continuar, incluyendo la opción de abrir una candidata ya detectada.

**Caso B — había una inmersión de v1.3.2 interrumpida (zona parcial).**

- Comportamiento por defecto: no se retoma automáticamente en el punto exacto. Se informa con honestidad de que quedó parcial, y retomarla se trata como una nueva decisión de cobertura: *"La vez pasada dejamos parcial la exploración de X. Podemos retomarla, o podemos mirar otra zona si hoy prefieres avanzar de otra manera."*
- Excepción explícita: si la persona pide continuar desde el punto exacto ("no quiero repetirlo todo"), prevalece. Se hace una recapitulación breve de verificación con lo que el checkpoint tiene guardado, se corrige si hace falta, y se continúa en el siguiente paso del patrón activo. Si el checkpoint no tiene ese nivel de detalle, se dice con honestidad y se ofrece reconstruir brevemente.
- El primer turno tras cualquier reanudación no basta por sí solo para diagnosticar fatiga o incomodidad — hace falta un segundo turno para confirmar si es patrón o solo el efecto de reengancharse a algo dejado a medias.

Si no hay artefacto de estado previo (primera sesión), pasar directamente a 10.3.

### 10.3 Piso 1 — Panorámica abierta

Una o pocas preguntas amplias que recorren varias zonas sin profundizar en ninguna, orientadas a poblar el mapa de candidatas:

- ¿Qué etapas o trabajos ha tenido tu trayectoria hasta ahora, a grandes rasgos?
- ¿Hay algún trabajo o etapa que te parezca menor pero que en realidad ocupó bastante de tu tiempo?
- ¿Hay alguna responsabilidad que asumiste sin que estuviera en tu cargo formal?
- ¿Hay algo que sueles minimizar cuando hablas de tu trabajo?

En este piso no se aplica [[PATRON_STAR_SIMPLE]]. Solo se detectan señales y se registran como candidatas.

### 10.4 Piso 2 — Selección y prevalidación con STAR simple

[[PATRON_STAR_SIMPLE]] no se aplica a todas las candidatas que hayan aparecido. Se aplica solo a la que la persona elige, o como máximo a una o dos que ella misma señale como más prometedoras:

> "Han aparecido varias zonas posibles: A, B y C. ¿Cuál te parece que merece que miremos un poco más hoy?"

**Regla de volumen:** nunca más de dos candidatas por sesión de escaneo. Si aparecen muchas, se registran todas en el mapa, se pide a la persona que elija cuál mirar primero, se aplica STAR simple solo a la seleccionada (máximo una segunda si hay motivo claro), y el resto queda como candidata pendiente.

Su función no es validar una competencia — es comprobar densidad profesional mínima: acción propia, dificultad o contexto significativo, efecto o resultado, posible evidencia.

**Criterio de escaneo de zona fértil (heurística de partida, no cerrada):** una candidata merece pasar a STAR simple cuando la señal panorámica ya menciona una acción concreta, aunque sea de pasada — dejando la decisión final de cuál priorizar en manos de la persona, no del sistema.

### 10.5 Piso 3 — Activación de profundidad

Una candidata escala a inmersión completa solo si se cumplen dos condiciones:

1. la prevalidación de STAR simple muestra densidad profesional suficiente;
2. la persona acepta entrar en una exploración más profunda.

> "Esta zona parece suficientemente rica como para trabajarla a fondo. Podemos entrar aquí y extraer una competencia con evidencia, o dejarla marcada como candidata y explorar otra zona."

Si falta alguna condición, la zona no se descarta — queda registrada como candidata o parcial, según corresponda.

Al activarse, gobierna [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]] completo, con su propia jerarquía de decisión (v1.3.2 §5) y sus propios patrones ([[PATRON_STAR_AMPLIADO]], [[PATRON_4S_TRANSICION]], [[PATRON_NARRATIVA_MAS_EVIDENCIA]]). Cobertura aporta contexto heredado (tiempo declarado, mapa actual); v1.3.2 no repite la calibración de apertura. Como máximo una inmersión completa por sesión (sección 9).

### 10.6 Cierre de cobertura

Antes de cerrar, movimiento propio y separado de cualquier validación de lo ya trabajado dentro de v1.3.2 — nunca la misma pregunta que valida transferibilidad (v1.3.2 §13):

> "Antes de cerrar del todo: ¿hay alguna otra parte de tu trabajo, sin relación con esto que hemos hablado, que también muestre algo de cómo trabajas?"

Preguntas adicionales útiles: ¿qué parte de tu trayectoria no hemos tocado? ¿hay alguna etapa que no hemos explorado porque parecía menos interesante? ¿qué quedaría injustamente fuera si cerráramos aquí?

El cierre actualiza el artefacto de estado (sección 8) y produce la salida mínima (sección 13).

---

## 11. Guardarraíles

Se activan solo ante señal, no por defecto. Los ya documentados en v1.3.2 §11 (abstracción, fatiga, secuencia sin pausas, degradación de evidencia, sugestión, reparación, emocional, exceso de amplitud) aplican igual **dentro** de una inmersión de v1.3.2 activada. Cobertura añade dos propios, activos durante escaneo y prevalidación:

- **Riesgo de falsa cobertura.** Toda salida de cobertura debe llevar advertencia explícita de límite (sección 13.6) — nunca dar la sensación de que el mapa actual representa la trayectoria completa.
- **Brevedad por restricción de tiempo declarada.** Si la persona declaró tiempo limitado en la apertura (10.1), las señales que normalmente activarían el guardarraíl de fatiga de v1.3.2 §11 (respuestas cortas, preguntas sobre cuánto queda) pesan menos mientras estén explicadas por ese tiempo — no se leen automáticamente como fatiga real. Fricción pendiente de documentar formalmente en `05_fricciones_y_antipatrones/`.

---

## 12. Criterio de suficiencia y cierre de sesión

**Sesión de cobertura suficiente** cuando ocurre cualquiera de estas, en el orden de la jerarquía de la sección 5:

- la persona lo pide;
- el tiempo declarado en la apertura se agota (chequeo puntual, no vigilancia de reloj);
- aparecen señales de fatiga no explicadas por tiempo declarado;
- se completó una inmersión de profundidad (éxito pleno de la sesión);
- se agotó la panorámica sin candidatas nuevas y no hay interés en prevalidar las existentes.

No forzar una inmersión de profundidad para justificar la sesión. Una sesión que solo pobló el mapa de candidatas es un resultado legítimo.

---

## 13. Salida mínima esperada

```md
## Competencia extraída, si la hubo esta sesión
(ficha mínima de v1.3.2 §14)

## Mapa de zonas actualizado
Exploradas:
Candidatas:
Parciales (con checkpoint si aplica):
Pendientes:

## Advertencia de límite
Qué no debe concluirse todavía a partir de lo explorado hasta ahora.

## Siguiente exploración recomendada
Zona propuesta y motivo breve.

## Checkpoint fino
Solo si la sesión cerró con una inmersión de v1.3.2 a medias.
```

---

## 14. Evaluación posterior de la sesión

```md
¿Se amplió el mapa de cobertura esta sesión? Sí / No / Parcialmente
¿Se activó profundidad? Sí / No — si sí, referencia a la ficha de v1.3.2
Candidatas nuevas detectadas:
Señales de fatiga o de tiempo declarado:
Guardarraíles activados:
Qué habría que cambiar en este playbook:
Decisión: Mantener / Simplificar / Añadir guardarraíl / Eliminar paso / Repetir piloto
```

---

## 15. Reglas de oro

1. Cobertura nunca sustituye ni duplica el criterio de v1.3.2 dentro de una inmersión activa.
2. Nunca presentar el mapa como completo — toda salida declara sus límites.
3. [[PATRON_STAR_SIMPLE]] nunca se aplica a más de dos candidatas por sesión de escaneo.
4. La selección de qué candidata prevalidar es siempre decisión de la persona, no del sistema.
5. Una candidata solo escala a profundidad con densidad suficiente **y** consentimiento explícito — nunca con solo una de las dos.
6. Sin checkpoint fino, no se finge poder retomar un punto exacto — se ofrece reconstrucción honesta.
7. El primer turno tras cualquier reanudación no es diagnóstico por sí solo.
8. No hay vigilancia activa de tiempo real — solo chequeos puntuales en transiciones naturales.
9. Una sesión que solo amplía el mapa sin activar profundidad es un resultado legítimo, no un fracaso.
10. El cierre de cobertura siempre incluye una pregunta de puerta nueva, separada de cualquier validación de lo ya trabajado.

---

## 16. Definición de éxito del MVP

Si la mayoría de estas preguntas se responde sí, la capa de cobertura merece seguir viva:

1. ¿El mapa de zonas se amplió o se mantuvo con honestidad, sin inventar cobertura donde no la hay?
2. ¿La prevalidación con STAR simple se mantuvo dentro del límite de una o dos candidatas?
3. ¿La activación de profundidad, si ocurrió, respetó las dos condiciones de escalado?
4. ¿La sesión reconoció con precisión si había o no un checkpoint recuperable?
5. ¿El cierre incluyó una pregunta de puerta nueva, distinta de la validación de v1.3.2?
6. ¿La salida declaró explícitamente qué no debe concluirse todavía?

---

## 17. Decisión operativa para el primer piloto de cobertura

Trabajar con una sola persona a lo largo de varias sesiones reales, sin forzar el ritmo. Priorizar observar si el protocolo de reanudación (10.2) funciona en la práctica — es la parte de este playbook con menos precedente empírico de toda la bóveda. Registrar con honestidad si el criterio heurístico de zona fértil (10.4) resulta insuficiente, y si la regla de volumen de STAR simple evita o no la fatiga que motivó su diseño.

El primer piloto de cobertura no debe demostrar que el mapa queda completo. Debe demostrar que el orquestador sabe, en todo momento, qué parte del mapa está inventando y cuál no.

---

## Nota final

Un mapa honesto sobre sus huecos vale más que un mapa que aparenta estar terminado. Cobertura no compite con profundidad por producir la mejor ficha — compite por no dejar que una ficha buena finja ser toda la historia.

---

## Relación con otros documentos de la bóveda

Este playbook orquesta, sin duplicar:

- [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]] — especialista de profundidad invocado en el piso 3;
- [[PATRON_STAR_SIMPLE]] — prevalidación ligera en el piso 2;
- [[PATRON_STAR_AMPLIADO]], [[PATRON_4S_TRANSICION]], [[PATRON_NARRATIVA_MAS_EVIDENCIA]] — patrones internos de v1.3.2, no gobernados por este documento;
- [[CONCEPTO_COBERTURA_PROFESIONAL]] — fundamento conceptual;
- `DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v2_0_0` — arquitectura consolidada de la que este documento es la traducción operativa;
- [[ANTIPATRON_CIERRE_ANCLADO_AL_HILO_UNICO]] — origen empírico del riesgo de falsa cobertura y del remedio de puerta nueva (sección 10.6);
- [[FRICCION_FATIGA_DEL_USUARIO]], [[FRICCION_AMBIGUEDAD_PARQUEDAD_O_DESINTERES]], [[ANTIPATRON_SECUENCIAS_SIN_PAUSAS]] — umbral de activación modificado por el tiempo declarado (sección 11), sin cambio en su contenido propio;
- [[PILOTO_005_ENTREVISTA_REPONEDOR_SUPERMERCADO]] — evidencia de que una dimensión profesional conocida puede no emerger en una entrevista profunda, origen de la línea de cobertura.

## Fuente base

Primer borrador ejecutable derivado de `DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v2_0_0`, siguiendo el mismo criterio de extensión y modularidad que [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]]. Elaborado por Claude, por instrucción directa de Gustavo, 2026-07-06.
