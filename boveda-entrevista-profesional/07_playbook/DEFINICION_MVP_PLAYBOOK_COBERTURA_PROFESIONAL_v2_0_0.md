# Definición MVP — Playbook de cobertura profesional (v2.0.0)
 
## Estado de este documento
 
Este documento es una definición operativa del MVP de cobertura profesional dentro de `Carrera Profesional AI-First`.
 
No es todavía un playbook ejecutable.
 
Su función es fijar la base conceptual y arquitectónica que un futuro [[PLAYBOOK_COBERTURA_PROFESIONAL]] debería implementar.
 
Esta versión `v1.0.4` parte de `DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_3` e incorpora tres ajustes de limpieza y consolidación:
 
- adopta `explorada` como estado canónico, en lugar de `cubierta`;
    
- elimina la antigua sección independiente de activación de profundidad por redundancia con la sección de escaneo y escalado;
    
- refuerza la distinción entre `prevalidación` mediante [[PATRON_STAR_SIMPLE]] y validación profunda mediante [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]].
    
 
El documento se apoya en:
 
- [[CONCEPTO_COBERTURA_PROFESIONAL]];
    
- [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]];
    
- [[PILOTO_005_ENTREVISTA_REPONEDOR_SUPERMERCADO]];
    
- [[ANTIPATRON_CIERRE_ANCLADO_AL_HILO_UNICO]];
    
- [[PATRON_STAR_SIMPLE]];
    
- [[PATRON_STAR_AMPLIADO]];
    
- fricciones y antipatrones ya documentados sobre fatiga, parquedad, secuencias sin pausa y cierre prematuro.
    
 
No sustituye al playbook de profundidad.
 
No modifica el alcance del playbook `v1.3.2`.
 
Define la capa superior que debe decidir qué zonas de la trayectoria se exploran, cuáles quedan pendientes y cuándo debe activarse una inmersión profunda.
 
---
 
## 1. Definición breve
 
**Cobertura profesional MVP** es una capa de entrevista orientada a producir un mapa inicial, no exhaustivo pero consciente de sus límites, de las zonas profesionales exploradas, candidatas, parciales y pendientes de una persona.
 
Su función es evitar que una competencia profunda aislada sea confundida con una comprensión suficiente de toda la trayectoria profesional.
 
Su valor no está en saberlo todo.
 
Su valor está en ordenar lo que ya se sabe, detectar lo que empieza a aparecer, registrar lo que quedó a medias y declarar con claridad lo que todavía no se ha cubierto.
 
---
 
## 2. Principio de partida
 
Cobertura no es una versión ampliada de profundidad.
 
Es una capa distinta.
 
La profundidad responde a:
 
> ¿Podemos extraer una competencia profesional real, valiosa y demostrable a partir de una experiencia concreta?
 
La cobertura responde a:
 
> ¿Sabemos qué parte de la trayectoria profesional estamos viendo, qué parte solo empieza a aparecer y qué parte puede estar quedando fuera?
 
Por tanto:
 
- [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]] sigue siendo el especialista de profundidad;
    
- cobertura actúa como orquestador de trayectoria;
    
- cobertura no profundiza todo;
    
- cobertura decide cuándo merece la pena activar profundidad;
    
- cobertura conserva memoria de lo explorado, lo parcial y lo pendiente.
    
 
La relación entre ambas capas es jerárquica pero no invasiva:
 
```text
Cobertura profesional
→ escanea trayectoria
→ detecta zona fértil
→ invoca profundidad
→ registra resultado
→ decide siguiente zona
```
 
---
 
## 3. Problema que resuelve
 
El playbook de profundidad puede producir una competencia real, valiosa y verificable.
 
Ese resultado es necesario, pero no suficiente para comprender una trayectoria profesional.
 
Una entrevista puede encontrar una unidad profesional muy potente y, aun así, dejar fuera dimensiones importantes de la carrera de una persona.
 
El riesgo principal es la **falsa cobertura**:
 
> creer que una competencia profunda aislada representa suficientemente toda la trayectoria profesional.
 
La cobertura profesional MVP existe para evitar ese salto.
 
No busca reconstruir toda la carrera.
 
No busca detectar todas las competencias.
 
No busca producir un perfil definitivo.
 
Busca responder de forma prudente:
 
> ¿Qué zonas profesionales hemos explorado, qué zonas aparecen como candidatas, qué zonas quedaron parciales y qué zonas siguen pendientes o invisibles?
 
---
 
## 4. Arquitectura MVP: orquestador multi-sesión
 
La cobertura profesional MVP debe entenderse como un **orquestador multi-sesión**, no como una única entrevista larga.
 
La entrevista profesional completa de una persona no debería depender de una sesión extensa en la que se intenta escanear, profundizar y cerrar toda la trayectoria.
 
El tiempo de la entrevista lo marca el humano, no la IA.
 
Por tanto, el MVP debe asumir que la cobertura se construye por ciclos.
 
Cada sesión de cobertura puede contener, como máximo:
 
1. apertura y calibración;
    
2. revisión del mapa de cobertura existente;
    
3. escaneo ligero de una o varias zonas;
    
4. decisión de si existe una zona fértil;
    
5. una inmersión profunda completa como máximo;
    
6. cierre de cobertura y actualización del mapa.
    
 
Queda fuera de este MVP encadenar varias inmersiones completas de profundidad en una sola sesión.
 
Si en el futuro se quisiera permitir más de una inmersión profunda por sesión, eso exigiría una revisión explícita de esta definición.
 
No debe introducirse como extensión silenciosa.
 
---
 
## 5. Zonas del mapa de cobertura
 
El mapa de cobertura debe distinguir, como mínimo, cuatro tipos de zonas:
 
- `explorada`;
    
- `candidata`;
    
- `parcial`;
    
- `pendiente`.
    
 
Estos cuatro estados no son etiquetas decorativas. Indican qué tipo de trabajo se ha hecho, qué puede afirmarse y qué debe ocurrir después.
 
### 5.1. Zonas exploradas
 
Son áreas de la trayectoria donde ya existe evidencia suficiente.
 
Normalmente han pasado por una inmersión de profundidad completa o por una validación suficientemente sólida.
 
Pueden incluir:
 
- una competencia extraída;
    
- una etapa profesional analizada;
    
- una responsabilidad reconstruida;
    
- una tensión laboral entendida;
    
- una decisión profesional explicada;
    
- una forma de actuar demostrada con evidencia.
    
 
Una zona explorada permite decir:
 
> Aquí podemos afirmar algo con cierta seguridad.
 
### 5.2. Zonas candidatas
 
Son áreas que han aparecido durante la conversación, pero todavía no han sido trabajadas con suficiente profundidad.
 
Funcionan como puertas posibles.
 
Pueden aparecer en frases como:
 
- “también trabajé en otra empresa, pero eso fue menos importante”;
    
- “aprendí mucho en esa época, aunque no sé explicarlo”;
    
- “eso no era mi trabajo principal, pero acabé resolviéndolo yo”;
    
- “hubo una etapa rara entre un empleo y otro”;
    
- “eso no tiene mucho mérito, pero lo hacía siempre”;
    
- “no sé si eso cuenta como competencia”.
    
 
Una zona candidata no debe tratarse todavía como competencia validada.
 
Debe registrarse como posible línea futura de exploración.
 
### 5.3. Zonas parciales
 
Son zonas donde ya hubo algún trabajo, pero no existe cierre suficiente.
 
Pueden darse por varios motivos:
 
- la sesión terminó antes de completar la inmersión;
    
- se inició una exploración pero no llegó a evidencia;
    
- hubo señales interesantes, pero faltó tiempo;
    
- se aplicó una prevalidación rápida, pero no una inmersión completa;
    
- el humano decidió pausar o cambiar de zona.
    
 
La zona parcial exige memoria más fina que una simple etiqueta.
 
Debe conservar, cuando proceda:
 
- qué se estaba explorando;
    
- qué patrón estaba activo;
    
- qué evidencia quedó como hecho;
    
- qué quedó como interpretación;
    
- qué quedó como hipótesis;
    
- qué quedó pendiente;
    
- qué guardarraíles se activaron;
    
- qué señales de fatiga, parquedad o restricción de tiempo aparecieron.
    
 
### 5.4. Zonas pendientes
 
Son áreas de la trayectoria que no han sido exploradas o que podrían haber quedado invisibles.
 
Pueden incluir:
 
- etapas profesionales no mencionadas;
    
- trabajos minimizados;
    
- aprendizajes no verbalizados;
    
- responsabilidades invisibles;
    
- transiciones no exploradas;
    
- conflictos evitados;
    
- fracasos o cambios de rumbo no tratados;
    
- competencias que no emergen porque la conversación se ancló a otro hilo fértil.
    
 
Las zonas pendientes son importantes porque delimitan la ignorancia del sistema.
 
La cobertura profesional MVP no solo debe decir qué sabe.
 
También debe decir qué no sabe todavía.
 
---
 
## 6. Artefacto de estado de cobertura
 
La cobertura profesional necesita un artefacto persistente entre sesiones.
 
Ese artefacto no debe vivir en `.pcs/`, porque no es memoria operativa de PCS.
 
Debe vivir dentro de la documentación propia del proyecto anfitrión, previsiblemente en la bóveda de entrevista profesional.
 
Su ubicación exacta queda pendiente de decisión documental.
 
El artefacto debe registrar, como mínimo:
 
```text
Zona profesional
Estado: explorada / candidata / parcial / pendiente
Evidencia asociada
Competencia extraída, si existe
Sesión o piloto relacionado
Patrón usado, si aplica
Riesgos o límites
Siguiente exploración recomendada
```
 
Cuando exista una inmersión interrumpida, el artefacto debe poder registrar un checkpoint fino:
 
```text
Zona activa
Patrón activo
Paso exacto donde se interrumpió
Hechos confirmados
Interpretaciones
Hipótesis
Pendientes
Guardarraíles activados
Estado de fatiga o restricción de tiempo
Instrucción de reanudación
```
 
Sin este checkpoint fino, la IA no puede retomar honestamente una inmersión en el punto exacto donde se dejó.
 
---
 
## 7. Apertura de sesión de cobertura
 
Toda sesión de cobertura debe abrir con una calibración ligera de disponibilidad y ritmo.
 
La pregunta base puede ser:
 
> ¿Cuánto tiempo tienes hoy? Podemos ir a fondo si dispones de un rato largo, o ir con calma sabiendo que seguiremos otro día. Tú decides, y puedes parar cuando quieras sin tener que explicarme por qué.
 
Esta pregunta tiene varias funciones:
 
- reconoce que el tiempo lo gobierna el humano;
    
- evita interpretar automáticamente la brevedad como fatiga o desinterés;
    
- permite decidir si conviene escanear, profundizar o solo reanudar;
    
- prepara una salida limpia si la sesión debe ser breve.
    
 
La respuesta es opcional.
 
Si la persona no responde o no quiere concretar tiempo, el sistema continúa sin ese dato.
 
La IA no debe fingir control de tiempo real.
 
Si no dispone de timestamps fiables ni puede medir duración entre turnos, no debe calcular cuánto tiempo queda.
 
Solo puede hacer chequeos ligeros en puntos naturales:
 
- cambio de zona;
    
- cierre de escaneo;
    
- antes de activar profundidad;
    
- cierre de inmersión;
    
- cierre de sesión.
    
 
---
 
## 8. Escaneo de zona fértil y control de volumen
 
Antes de invocar el playbook de profundidad, cobertura opera en tres pisos, no en dos.
 
Esta sección resuelve una tensión de diseño importante: [[PATRON_STAR_SIMPLE]] sirve como herramienta ligera de prevalidación, pero no debe aplicarse indiscriminadamente a todas las zonas candidatas, porque entonces la fase de escaneo puede convertirse en una entrevista larga disfrazada.
 
### Piso 1 — Panorámica abierta
 
La sesión comienza con una o pocas preguntas amplias que recorren varias zonas profesionales a la vez.
 
Su función es poblar el mapa de candidatas sin profundizar todavía en ninguna.
 
Ejemplos:
 
> ¿Qué etapas o trabajos ha tenido tu trayectoria hasta ahora, a grandes rasgos?
 
> ¿Hay algún trabajo o etapa que te parezca menor pero que en realidad ocupó bastante de tu tiempo?
 
> ¿Hay alguna responsabilidad que asumiste sin que estuviera en tu cargo formal?
 
En este piso no se aplica todavía `STAR_SIMPLE`.
 
Solo se detectan señales.
 
### Piso 2 — Selección y [[PATRON_STAR_SIMPLE]]
 
[[PATRON_STAR_SIMPLE]] no se aplica a todas las candidatas que hayan aparecido en la panorámica.
 
Se aplica solo a:
 
- la candidata que la propia persona elige;
    
- o, como máximo, una o dos candidatas que parezcan más prometedoras por señal textual clara o por elección explícita de la persona.
    
 
Ejemplo de selección:
 
> Han aparecido varias zonas posibles: A, B y C. ¿Cuál te parece que merece que miremos un poco más hoy?
 
También puede formularse así:
 
> De estas líneas, ¿cuál crees que dice más de cómo trabajas?
 
Este filtro evita que la prevalidación se convierta en una entrevista larga disfrazada.
 
Sin esta restricción, cinco candidatas multiplicadas por cuatro preguntas de `STAR_SIMPLE` producirían veinte preguntas antes de activar siquiera profundidad. Eso reproduce el mismo riesgo de fatiga que cobertura pretende evitar, solo que desplazado a la fase de escaneo.
 
La función de `STAR_SIMPLE` en cobertura no es validar una competencia.
 
Su función es comprobar si una candidata tiene densidad profesional mínima:
 
- acción propia;
    
- dificultad o contexto significativo;
    
- efecto o resultado;
    
- posible evidencia.
    
 
### Piso 3 — `STAR_AMPLIADO` / `v1.3.2`
 
Si una candidata supera la prevalidación ligera y la persona acepta entrar a fondo, entonces se activa [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]].
 
En ese momento deja de gobernar `STAR_SIMPLE`.
 
Pasa a gobernar la profundidad, con [[PATRON_STAR_AMPLIADO]] cuando corresponda.
 
La activación de profundidad debe ser explícita. La IA debe poder decir algo equivalente a:
 
> Esta zona parece suficientemente rica como para trabajarla a fondo. Podemos entrar aquí y extraer una competencia con evidencia, o dejarla marcada como candidata y explorar otra zona.
 
La persona decide si quiere entrar.
 
### Regla de volumen
 
[[PATRON_STAR_SIMPLE]] se aplica como máximo a una o dos candidatas por sesión de escaneo.
 
Nunca se aplica a todas las candidatas que aparezcan en la panorámica.
 
Si aparecen muchas candidatas, la cobertura debe:
 
1. registrarlas en el mapa;
    
2. pedir a la persona que elija cuál mirar primero;
    
3. aplicar `STAR_SIMPLE` solo a la seleccionada, o a una segunda como máximo si hay motivo claro;
    
4. dejar el resto como candidatas pendientes.
    
 
### Regla de escalado
 
Una candidata puede escalar de `STAR_SIMPLE` a `STAR_AMPLIADO` / `v1.3.2` solo si se cumplen dos condiciones:
 
1. La prevalidación muestra densidad profesional suficiente: acción propia, dificultad, efecto y posible evidencia.
    
2. La persona acepta entrar en una exploración más profunda.
    
 
Si falta una de esas dos condiciones, la zona no se descarta necesariamente.
 
Debe quedar registrada como candidata o parcial, según corresponda.
 
---
 
## 9. Protocolo de reanudación
 
Al retomar cobertura, el sistema debe informar primero del estado guardado.
 
Debe hacerlo con contexto mínimo, no con una recapitulación pesada.
 
Hay dos casos principales.
 
### Caso A — no había inmersión profunda activa
 
La sesión anterior quedó entre zonas, durante escaneo o después de un cierre limpio.
 
En ese caso, la IA debe presentar el mapa actual:
 
- zonas exploradas;
    
- zonas candidatas;
    
- zonas parciales, si existen;
    
- zonas pendientes;
    
- siguiente exploración recomendada.
    
 
Después debe preguntar por dónde continuar.
 
### Caso B — había una inmersión profunda interrumpida
 
La sesión anterior quedó dentro de una inmersión de profundidad.
 
En ese caso, el comportamiento por defecto es no reanudar automáticamente en el punto exacto.
 
La IA debe decir algo como:
 
> La vez pasada dejamos parcial la exploración de X. Podemos retomarla, o podemos mirar otra zona si hoy prefieres avanzar de otra manera.
 
Si la persona pide explícitamente continuar desde donde se dejó, esa instrucción prevalece.
 
Entonces la IA debe:
 
1. hacer una recapitulación breve de verificación;
    
2. distinguir hechos, interpretaciones, hipótesis y pendientes;
    
3. invitar a corregir;
    
4. continuar desde el siguiente paso guardado;
    
5. no pedir que la persona cuente todo desde el principio.
    
 
Si el checkpoint no tiene suficiente detalle, la IA debe decirlo con honestidad y ofrecer una reconstrucción breve antes de seguir.
 
No debe fingir precisión.
 
---
 
## 10. Cierre de cobertura
 
Antes de cerrar una sesión, cobertura debe volver a abrir el mapa.
 
El objetivo es evitar el cierre anclado al hilo único.
 
Preguntas útiles:
 
- ¿Qué parte de tu trayectoria no hemos tocado?
    
- ¿Hay algún trabajo o etapa que parezca menor pero diga mucho de ti?
    
- ¿Hay algo profesionalmente importante que esta conversación no permitiría ver?
    
- ¿Qué quedaría injustamente fuera si cerráramos tu perfil solo con lo hablado?
    
- ¿Hay alguna responsabilidad que tiendes a minimizar pero que otros sí valorarían?
    
- ¿Hay alguna etapa que no hemos explorado porque parecía menos interesante?
    
 
El cierre debe producir una actualización del mapa:
 
- qué quedó explorado;
    
- qué quedó candidato;
    
- qué quedó parcial;
    
- qué quedó pendiente;
    
- qué no debe concluirse todavía;
    
- cuál sería el siguiente paso razonable.
    
 
---
 
## 11. Salida mínima esperada
 
Una salida MVP de cobertura profesional debe contener, como mínimo:
 
### 11.1. Competencia profunda extraída, si existe
 
- Nombre provisional o definitivo.
    
- Evidencia asociada.
    
- Zona de trayectoria de la que procede.
    
- Nivel de seguridad.
    
 
### 11.2. Zona explorada
 
- Qué parte de la trayectoria se trabajó con suficiente profundidad.
    
- Qué puede afirmarse razonablemente.
    
 
### 11.3. Zonas candidatas
 
- Señales aparecidas durante la conversación.
    
- Posibles líneas futuras de entrevista.
    
- Motivo por el que parecen relevantes.
    
 
### 11.4. Zonas parciales
 
- Qué quedó iniciado pero no cerrado.
    
- Qué checkpoint existe.
    
- Qué haría falta para retomarlo.
    
 
### 11.5. Zonas pendientes
 
- Partes de la trayectoria no exploradas.
    
- Áreas invisibles o insuficientemente tratadas.
    
- Riesgos de omisión.
    
 
### 11.6. Advertencia de límite
 
- Qué no debe concluirse todavía.
    
- Riesgo de falsa cobertura.
    
- Alcance real del mapa generado.
    
 
### 11.7. Siguiente exploración recomendada
 
- Qué zona convendría abrir después.
    
- Por qué esa zona parece relevante.
    
- Si conviene escaneo, [[PATRON_STAR_SIMPLE]] o inmersión profunda.
    
 
---
 
## 12. Criterio mínimo de éxito MVP
 
La cobertura profesional MVP funciona si, al terminar una sesión o ciclo mínimo de exploración, el sistema puede afirmar:
 
> Hemos extraído o situado al menos una unidad profesional significativa, sabemos de qué zona de trayectoria procede, hemos detectado otras zonas candidatas o parciales y podemos declarar explícitamente qué queda pendiente o no cubierto.
 
La cobertura no fracasa por no saberlo todo.
 
Fracasa si produce una salida que parece total cuando solo ha explorado una parte.
 
---
 
## 13. Qué queda fuera de este MVP
 
Queda fuera de esta versión:
 
- reconstrucción completa de carrera;
    
- certificación de perfil profesional;
    
- mapa exhaustivo de competencias;
    
- taxonomía definitiva;
    
- más de una inmersión profunda completa por sesión;
    
- vigilancia activa de tiempo real;
    
- comportamiento garantizado ante desaparición silenciosa del humano;
    
- criterio cerrado de zona fértil;
    
- formato definitivo del artefacto de estado de cobertura;
    
- automatización de la cobertura;
    
- integración técnica con bases de datos o dashboards;
    
- conversión de cobertura en playbook ejecutable final.
    
 
El MVP produce un mapa inicial razonable, no una reconstrucción total.
 
---
 
## 14. Fricciones y antipatrones relacionados
 
Esta definición debe tener en cuenta, como mínimo:
 
- [[ANTIPATRON_CIERRE_ANCLADO_AL_HILO_UNICO]];
    
- `FRICCION_FATIGA_DEL_USUARIO`;
    
- `FRICCION_AMBIGUEDAD_PARQUEDAD_O_DESINTERES`;
    
- `ANTIPATRON_SECUENCIAS_SIN_PAUSAS`;
    
- la nueva fricción candidata de brevedad o aceleración por restricción de tiempo conocida por el humano.
    
 
La calibración inicial de tiempo ayuda a no leer como fatiga lo que quizá es simplemente límite de disponibilidad.
 
La existencia de zonas candidatas, parciales y pendientes ayuda a no cerrar la trayectoria sobre una sola competencia profunda.
 
---
 
## 15. Relación con otros documentos de la bóveda
 
Este documento se apoya en:
 
- [[CONCEPTO_COBERTURA_PROFESIONAL]]: definición conceptual de cobertura profesional.
    
- [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]]: especialista de profundidad que cobertura puede invocar.
    
- [[PATRON_STAR_SIMPLE]]: patrón ligero para capturar incidentes básicos y prevalidar zonas candidatas.
    
- [[PATRON_STAR_AMPLIADO]]: patrón de profundidad que se activa dentro de `v1.3.2` cuando una zona ya merece inmersión.
    
- [[CONCEPTO_ARCO_DE_SESION]]: criterio de orquestación dentro de una sesión.
    
- [[ANTIPATRON_CIERRE_ANCLADO_AL_HILO_UNICO]]: riesgo empírico que motiva la capa de cobertura.
    
- [[PILOTO_005_ENTREVISTA_REPONEDOR_SUPERMERCADO]]: evidencia de que una dimensión profesional conocida puede no emerger en una entrevista profunda.
    
- fricciones y antipatrones relacionados con fatiga, parquedad, secuencias sin pausa y límites de disponibilidad.
    
 
Este documento no duplica esos materiales.
 
Los usa como base para definir la arquitectura mínima de cobertura MVP.
 
---
 
## 16. Formulación operativa final
 
La cobertura profesional MVP es la capa de entrevista que permite construir, a través de una o varias sesiones, un mapa inicial y no exhaustivo de las zonas profesionales exploradas, candidatas, parciales y pendientes de una persona.
 
Su función es evitar que una competencia profunda aislada sea confundida con una comprensión suficiente de toda la trayectoria.
 
Opera como orquestador:
 
```text
mapa → escaneo → zona candidata → prevalidación ligera → profundidad si procede → actualización del mapa → siguiente zona
```
 
Su éxito no consiste en cerrar la carrera profesional de la persona.
 
Consiste en saber qué parte se ha trabajado, qué parte empieza a aparecer, qué parte quedó a medias y qué parte todavía no se puede afirmar.
 
---
 
## 17. Estado y uso previsto
 
Este documento debe tratarse como definición MVP integrada para el futuro playbook de cobertura profesional.
 
No debe tratarse como playbook operativo final.
 
Puede servir como base para derivar posteriormente:
 
- un patrón de preguntas de cobertura;
    
- un criterio operativo de zona fértil;
    
- una plantilla de mapa de cobertura;
    
- un protocolo de actualización del artefacto de estado de cobertura;
    
- una futura versión `PLAYBOOK_COBERTURA_PROFESIONAL_v1`.
    
 
Hasta que exista ese playbook, cobertura debe seguir tratándose como capa en diseño.