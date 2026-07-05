# Playbook de entrevista profesional — Borrador v0

## Estado de este documento

Es un primer borrador, no la versión consolidada que prevé [[idea-central]] para [[PLAYBOOK_ENTREVISTA_PROFESIONAL]]. Su función es traducir en reglas operativas concretas lo que hasta ahora vive como criterio conceptual en [[CONCEPTO_ARCO_DE_SESION]], apoyándose en los tres patrones y en el antipatrón [[ANTIPATRON_SECUENCIAS_SIN_PAUSAS]] ya documentados.

Corresponde al alcance mínimo necesario para pilotar el MVP definido en conversaciones previas: validar si la entrevista profesional profunda es el mejor método para extraer al menos una competencia con evidencia verificable que el usuario no había articulado antes de empezar.

## 1. Objetivo de esta sesión de entrevista

Extraer, mediante conversación guiada, al menos una etapa profesional reconstruida con:

- un incidente con Situación, Acción propia y Resultado identificables (vía [[PATRON_STAR_AMPLIADO]]);
- evidencia verificable asociada a ese incidente;
- una competencia inferida que la persona no había nombrado explícitamente antes de la entrevista.

Todo lo demás que ocurra en la sesión —narrativa de sentido, exploración de transición, validación emocional— está al servicio de este objetivo, no lo sustituye.

## 2. Alcance del MVP

**Dentro:**

- [[PATRON_STAR_AMPLIADO]], [[PATRON_4S_TRANSICION]], [[PATRON_NARRATIVA_MAS_EVIDENCIA]];
- movimientos de reflejo/validación entre fases sensibles;
- protocolo de escalada emocional y de reparación de ruptura (definidos en las secciones 5 y 6);
- cierre con anclaje de retorno a tierra.

**Fuera, reservado para versiones posteriores:**

- CCI / My Career Story Workbook completo (héroes, película, lema, recuerdos tempranos);
- Pictorial Narratives con componente visual;
- DACUM invertido como patrón independiente (por ahora, cubierto parcialmente por la fase de Tarea de STAR ampliado);
- rúbrica de calidad de entrevista formal y protocolo de validación con el usuario, que requieren datos del piloto para diseñarse con criterio.

## 3. Fases de la sesión

1. **Apertura.** Encuadre breve, sin proyección identitaria (se deja fuera del MVP el bloque CCI/MCS). Se pide a la persona que elija una etapa profesional por la que empezar.
2. **Cuerpo — por cada etapa elegida.** Se aplica el patrón que corresponda según los disparadores de la sección 4, con las pausas de reflejo obligatorias de la sección 5.
3. **Transición entre etapas.** Antes de abrir una nueva etapa, se ofrece la posibilidad de detenerse o continuar (ver movimientos de transición en [[CONCEPTO_ARCO_DE_SESION]]).
4. **Cierre de sesión.** Se aplica cuando se cumple el criterio de la sección 7.

## 4. Tabla de disparadores de activación

| La persona menciona...                                   | Patrón que se activa                                                     |
| -------------------------------------------------------- | ------------------------------------------------------------------------ |
| Un incidente, logro, problema o decisión concreta        | [[PATRON_STAR_AMPLIADO]]                                                 |
| Un cambio de puesto, sector, despido, pausa o giro vital | [[PATRON_4S_TRANSICION]]                                                 |
| Valores, misión o identidad, sin ejemplo concreto        | [[PATRON_NARRATIVA_MAS_EVIDENCIA]] (deriva a STAR ampliado en su paso 2) |

Regla de desempate: si un mismo turno contiene señales de más de un disparador, se prioriza el que esté más cerca de un hecho concreto y verificable sobre el que esté más cerca de una declaración abstracta. Ante la duda, se empieza por Narrativa+Evidencia, que ya contempla el descenso hacia STAR.

## 5. Reglas de pausa y reflejo (aplican a los tres patrones)

- Después de la fase de mayor carga de cada patrón (Acción en STAR, Estrategias en 4S, el paso de evidencia en Narrativa+Evidencia), insertar un movimiento de reflejo antes de continuar a la siguiente fase.
- Nunca encadenar dos incidentes STAR distintos sin al menos un movimiento de transición entre ambos.
- Nunca cerrar un bloque de 4S pasando directamente de "Estrategias" a "Plan" sin un anclaje de retorno a tierra intermedio.

Esta sección operacionaliza directamente el antipatrón [[ANTIPATRON_SECUENCIAS_SIN_PAUSAS]]: cada regla aquí listada es la corrección de una de las formas de fallo documentadas allí.

## 6. Protocolo de escalada emocional y reparación

**Activación del protocolo de escalada** ante cualquiera de estas señales:

- cambio brusco de registro verbal (frases más cortas, vacilación, silencios);
- contenido que excede el marco profesional (familia, salud, trauma) sin haber sido preguntado;
- lenguaje de autoinculpación o vergüenza desproporcionado al hecho relatado.

Acción: frenar el patrón en curso, ofrecer explícitamente la opción de quedarse en el tema o cambiar ("Podemos quedarnos aquí un momento, o seguir con la parte profesional si lo prefieres"), y no retomar el protocolo de indagación hasta obtener una respuesta clara de la persona.

**Activación del protocolo de reparación** ante cualquiera de estas señales:

- la persona corrige activamente al sistema;
- respuesta monosilábica tras una pregunta que antes generaba desarrollo;
- lenguaje que señala sentirse mal entendida.

Acción: pausar la indagación, reconocer explícitamente la posible desconexión ("Puede que no haya entendido bien lo que me contabas — ¿puedes ayudarme a verlo como tú lo ves?"), y esperar a que la persona restablezca el hilo antes de continuar con el patrón activo.

## 7. Criterio de suficiencia y cierre

**Una etapa se considera suficientemente cubierta cuando:**

- existe al menos un incidente con Situación, Acción propia y Resultado identificables;
- la persona empieza a repetir información ya dada;
- las respuestas pierden energía o se acortan de forma sostenida.

**La sesión completa se cierra cuando:**

- se ha cubierto al menos una etapa con evidencia suficiente para el objetivo de la sección 1;
- aparecen dos o más señales de fatiga seguidas, incluso tras un intento de reparación;
- la persona lo pide explícitamente, en cualquier momento, con independencia de cuánto se haya cubierto.

Todo cierre de sesión debe incluir un anclaje de retorno a tierra final, no solo una despedida funcional.

## 8. Discrepancia entre narrativa y evidencia

Cuando la historia que cuenta la persona y la evidencia concreta que aporta después no coinciden (riesgo identificado en la revisión clínica de [[PATRON_NARRATIVA_MAS_EVIDENCIA]]), no se señala la discrepancia como corrección ni se le pide a la persona que la resuelva en el momento. Se registra la tensión tal cual aparece, y se ofrece a la persona la oportunidad de ampliar si lo desea ("Cuentas esto como algo que salió bien — al mismo tiempo, lo que describes tiene también su parte más difícil. ¿Cómo lo ves tú?"). El objetivo es dejar espacio, no confrontar.

## 9. Pendiente para la siguiente iteración

- diseño de la rúbrica de calidad de entrevista, una vez existan sesiones piloto que analizar;
- protocolo de validación del usuario sobre el resultado final (plantilla de ficha de etapa);
- decisión sobre si incorporar CCI/MCS como bloque opcional de apertura en sesiones más largas;
- revisión de este borrador contra las primeras transcripciones reales del piloto.

## Relación con otros conceptos o patrones

Este documento opera sobre:

- [[CONCEPTO_ARCO_DE_SESION]], del que es la traducción operativa en reglas ejecutables;
- [[ANTIPATRON_SECUENCIAS_SIN_PAUSAS]], cuyas correcciones se incorporan directamente en la sección 5;
- [[PATRON_STAR_AMPLIADO]], [[PATRON_4S_TRANSICION]], [[PATRON_NARRATIVA_MAS_EVIDENCIA]], cuyo momento de activación y límites de aplicación quedan aquí fijados;
- [[CONCEPTO_SER_ESCUCHADO_Y_VALIDADO]], cuya condición relacional sostiene todos los movimientos de reflejo y reparación descritos.

## Fuente base

Síntesis operativa derivada de [[CONCEPTO_ARCO_DE_SESION]] y de la revisión clínica transversal de los tres patrones existentes, con apoyo en [[Análisis estructural de la reconstrucción de trayectorias profesionales]] y [[Narrative career counseling - My career story and pictorial narratives]].
