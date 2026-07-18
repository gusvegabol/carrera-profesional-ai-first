# Playbook de entrevista profesional — v1

## Estado de este documento

Este documento es una versión operativa del playbook de entrevista profesional para el primer piloto del MVP de `Carrera Profesional AI-First`.

No pretende reconstruir toda la trayectoria profesional de una persona.

No pretende generar un CV completo.

No pretende hacer coaching, terapia, diagnóstico psicológico ni certificación formal de competencias.

Su función es guiar una entrevista conversacional suficientemente estructurada para comprobar si el núcleo del proyecto funciona:

> Extraer al menos una competencia profesional con evidencia verificable que la persona no había articulado claramente antes de la entrevista.

Este playbook debe usarse como protocolo de entrevista con:

1. una ruta base obligatoria;
    
2. guardarraíles condicionales;
    
3. criterios de suficiencia;
    
4. criterios de parada;
    
5. una salida mínima validable.
    

---

## 1. Objetivo del piloto

El objetivo mínimo de la sesión es reconstruir una unidad profesional de valor.

Una unidad profesional de valor queda conseguida cuando se obtiene:

- una etapa, proyecto, transición o situación profesional concreta;
    
- un incidente o experiencia real;
    
- una acción propia identificable;
    
- un resultado, efecto o consecuencia;
    
- una competencia inferida;
    
- evidencia asociada a esa competencia;
    
- validación de la persona entrevistada.
    

La entrevista se considera exitosa si al final puede formularse algo parecido a:

> “En esta situación concreta, hice X, enfrenté Y, conseguí Z, y eso muestra una competencia en ___, respaldada por ___.”

No hace falta descubrir muchas competencias.

No hace falta recorrer toda la carrera.

No hace falta que la competencia tenga nombre perfecto en la primera pasada.

Sí hace falta que la persona reconozca que lo extraído representa algo real de su experiencia.

---

## 2. Principio de ejecución

Este playbook no debe ejecutarse como una lista lineal de pasos obligatorios.

Debe ejecutarse como una conversación guiada.

La ruta base se sigue siempre.

Los guardarraíles solo se activan si aparecen señales que los justifican.

El entrevistador debe evitar dos errores opuestos:

1. **Infraestructurar la entrevista**: preguntar demasiado poco, aceptar respuestas vagas y cerrar sin evidencia.
    
2. **Sobrecargar la entrevista**: aplicar todos los patrones, forzar profundidad y agotar a la persona.
    

La regla central es:

> Profundizar solo hasta obtener evidencia suficiente, no hasta agotar el tema.

---

## 3. Alcance del piloto v1

### Dentro del piloto

Está dentro del piloto:

- trabajar una etapa profesional principal;
    
- explorar un incidente, logro, problema, decisión o transición;
    
- usar `PATRON_STAR_AMPLIADO` cuando aparezca una situación concreta;
    
- usar `PATRON_4S_TRANSICION` si la etapa implica cambio profesional relevante;
    
- usar `PATRON_NARRATIVA_MAS_EVIDENCIA` si la persona empieza en abstracto;
    
- detectar fatiga, bloqueo o pérdida de energía;
    
- validar la competencia inferida con la persona;
    
- cerrar con una ficha breve de evidencia.
    

### Fuera del piloto

Queda fuera del piloto:

- reconstruir toda la carrera profesional;
    
- generar un CV completo;
    
- crear una narrativa profesional final;
    
- clasificar exhaustivamente todas las competencias;
    
- certificar competencias;
    
- comparar a la persona con perfiles de mercado;
    
- diseñar un plan de carrera;
    
- hacer terapia, diagnóstico emocional o acompañamiento psicológico.
    

---

## 4. Salida mínima esperada

La sesión debe terminar con una ficha mínima.

### Ficha mínima de competencia validable

```md
## Competencia detectada

Nombre provisional:

## Evidencia principal

Situación:

Acción propia:

Resultado:

## Contexto

Etapa profesional:

Condiciones relevantes:

Dificultades:

## Validación de la persona

¿La persona reconoce esta competencia como propia?

Matices o correcciones aportadas:

## Nivel de confianza

Alto / Medio / Bajo

## Pendiente

Qué habría que preguntar en una segunda sesión:
```

La ficha no tiene que ser perfecta.

Debe ser suficientemente concreta para poder decidir si la entrevista ha producido valor real.

---

## 5. Ruta base de la entrevista

La ruta base es el camino normal de la sesión.

Debe seguirse salvo que aparezca una señal clara para activar un guardarraíl.

### 5.1 Apertura

Objetivo: encuadrar la sesión sin abrumar.

Mensaje recomendado:

> “La idea de esta sesión no es repasar todo tu CV ni encontrar una etiqueta perfecta. Vamos a elegir una etapa o experiencia profesional concreta y tratar de reconstruir qué hiciste, qué dificultad había, qué resultado tuvo y qué competencia real puede estar ahí.”

Aclaraciones necesarias:

- la persona puede corregir cualquier interpretación;
    
- no se busca juzgar su carrera;
    
- no hace falta tener respuestas perfectas;
    
- se puede parar o cambiar de ritmo si la conversación se vuelve pesada;
    
- el objetivo es obtener una evidencia concreta, no contarlo todo.
    

### 5.2 Elección de etapa

Preguntar:

> “Si tuvieras que elegir una etapa, proyecto, trabajo, cambio o situación profesional que crees que dice algo importante de cómo trabajas, ¿por cuál empezarías?”

Si la persona duda, ofrecer tres puertas de entrada:

1. un logro;
    
2. un problema difícil;
    
3. un cambio o transición.
    

No ofrecer demasiadas opciones.

No convertir esta parte en un cuestionario.

### 5.3 Primer relato libre

Pedir una narración inicial breve:

> “Cuéntamelo primero a tu manera, sin preocuparte por ordenarlo demasiado.”

Durante esta fase no interrumpir con demasiadas preguntas.

Buscar señales:

- incidente concreto;
    
- transición;
    
- conflicto;
    
- decisión;
    
- responsabilidad asumida;
    
- resultado;
    
- emoción o tensión;
    
- frase abstracta sin ejemplo.
    

### 5.4 Activación del patrón principal

Después del relato inicial, elegir el patrón dominante:

|Si aparece...|Activar...|
|---|---|
|Incidente, logro, problema o decisión concreta|`PATRON_STAR_AMPLIADO`|
|Cambio de puesto, sector, despido, pausa, reinvención o giro vital|`PATRON_4S_TRANSICION`|
|Valores, identidad, propósito o narrativa sin ejemplo concreto|`PATRON_NARRATIVA_MAS_EVIDENCIA`|
|Respuestas vagas o genéricas|Profundización suave hacia caso concreto|
|Fatiga, bloqueo o pérdida de energía|Guardarraíl de fatiga|
|Incomodidad emocional|Guardarraíl de reparación o pausa|

Solo debe dominar un patrón cada vez.

No mezclar todos los patrones simultáneamente.

---

## 6. Patrón base: reconstrucción de evidencia

Este bloque se usa cuando ya existe una experiencia concreta.

Busca reconstruir:

- situación;
    
- tarea o tensión;
    
- acción propia;
    
- resultado;
    
- aprendizaje o competencia.
    

Preguntas útiles:

### Situación

- “¿Qué estaba pasando exactamente?”
    
- “¿En qué contexto ocurrió?”
    
- “¿Qué hacía que esa situación fuera relevante o difícil?”
    

### Acción propia

- “¿Qué hiciste tú concretamente?”
    
- “¿Qué parte dependía de ti?”
    
- “¿Qué decidiste hacer y por qué?”
    

### Dificultad

- “¿Qué era lo más complicado de manejar?”
    
- “¿Qué podía salir mal?”
    
- “¿Qué restricciones tenías?”
    

### Resultado

- “¿Qué cambió después de tu intervención?”
    
- “¿Cómo se notó el resultado?”
    
- “¿Alguien reconoció, usó o dependió de ese resultado?”
    

### Competencia inferida

- “Si tuvieras que explicar qué habilidad tuya aparece ahí, ¿cuál sería?”
    
- “Yo estoy viendo una posible competencia en ___. ¿Te representa o lo matizarías?”
    
- “¿Esto fue algo puntual o algo que has repetido en otros contextos?”
    

La competencia no debe imponerse.

Debe proponerse y validarse.

---

## 7. Guardarraíles condicionales

Los guardarraíles no son pasos obligatorios.

Son mecanismos de protección y calidad.

Solo se activan si aparece una señal.

---

### 7.1 Guardarraíl de abstracción

Se activa cuando la persona habla en términos generales:

- “soy resolutivo”;
    
- “me adapto bien”;
    
- “me gusta ayudar”;
    
- “aprendo rápido”;
    
- “sé gestionar equipos”;
    
- “siempre he sido muy responsable”.
    

Respuesta recomendada:

> “Eso puede ser importante, pero para no quedarnos en una etiqueta, ¿recuerdas una situación concreta donde eso se viera?”

Objetivo:

- pasar de autodescripción a evidencia;
    
- evitar competencias declaradas sin prueba;
    
- aterrizar valores en acciones.
    

---

### 7.2 Guardarraíl de transición profesional

Se activa cuando aparece:

- cambio de puesto;
    
- cambio de empresa;
    
- despido;
    
- pausa;
    
- enfermedad;
    
- cuidado familiar;
    
- migración;
    
- cambio de sector;
    
- vuelta al mercado laboral;
    
- abandono de un camino anterior;
    
- inicio de etapa autónoma.
    

Preguntas útiles:

- “¿Qué cambió exactamente?”
    
- “¿Qué parte estaba bajo tu control y qué parte no?”
    
- “¿Qué apoyos tenías?”
    
- “¿Qué estrategias usaste para adaptarte?”
    
- “¿Qué aprendiste de ti profesionalmente en esa transición?”
    

Cuidado:

No convertir la transición en análisis vital completo.

El objetivo sigue siendo extraer una competencia con evidencia.

---

### 7.3 Guardarraíl de fatiga

Se activa cuando aparecen señales como:

- respuestas cada vez más cortas;
    
- pérdida de energía;
    
- silencios más largos;
    
- dificultad para recordar;
    
- aceptación pasiva de interpretaciones;
    
- preguntas sobre cuánto queda;
    
- cambio de tono;
    
- repetición sin avance;
    
- señales de cansancio cognitivo o emocional.
    

Intervención recomendada:

> “Creo que esta parte ya nos ha dado bastante material. Podemos parar aquí, resumir lo que tenemos y ver si te representa.”

O:

> “Podemos bajar un poco el ritmo. No hace falta seguir excavando si ya tenemos una evidencia suficiente.”

Regla:

Si aparecen dos señales de fatiga seguidas, no abrir una nueva línea de indagación.

Primero resumir, validar y decidir si cerrar.

---

### 7.4 Guardarraíl de reparación

Se activa cuando la persona:

- corrige con fuerza una interpretación;
    
- parece incómoda;
    
- responde de forma defensiva;
    
- dice que no se siente representada;
    
- muestra distancia con la lectura propuesta;
    
- rechaza una competencia inferida.
    

Intervención recomendada:

> “Puede que haya interpretado demasiado rápido. Me quedo con tu corrección. ¿Cómo lo formularías tú de una forma más fiel?”

Objetivo:

- proteger la confianza;
    
- devolver agencia a la persona;
    
- corregir sin justificar la interpretación anterior;
    
- evitar que el sistema imponga una narrativa.
    

---

### 7.5 Guardarraíl emocional

Se activa si la conversación toca una zona sensible:

- despidos dolorosos;
    
- fracaso;
    
- conflicto fuerte;
    
- humillación;
    
- pérdida;
    
- ansiedad;
    
- bloqueo;
    
- enfermedad;
    
- duelo;
    
- situaciones personales intensas.
    

Intervención recomendada:

> “No necesitamos entrar más de lo que sea útil para el objetivo profesional. Podemos quedarnos solo con qué hiciste para manejar la situación y qué capacidad aparece ahí.”

Regla:

La entrevista no debe explorar dolor por profundidad narrativa.

Solo debe recoger el contexto necesario para entender la competencia profesional.

---

### 7.6 Guardarraíl de exceso de amplitud

Se activa cuando la persona empieza a recorrer muchas etapas, trabajos o historias sin profundizar en ninguna.

Intervención recomendada:

> “Hay varias líneas interesantes, pero para que esto sea útil vamos a elegir una y reconstruirla bien. ¿Cuál de estas situaciones representa mejor algo importante de tu forma de trabajar?”

Objetivo:

- evitar autobiografía extensa;
    
- volver a unidad mínima de valor;
    
- proteger la salida concreta del piloto.
    

---

## 8. Criterio de etapa suficientemente cubierta

Una etapa se considera suficientemente cubierta cuando se cumple la mayoría de estas condiciones:

- hay una situación concreta;
    
- hay una acción propia identificable;
    
- hay un resultado o consecuencia;
    
- hay una posible competencia inferida;
    
- la persona reconoce total o parcialmente la interpretación;
    
- no aparecen nuevas evidencias relevantes al seguir preguntando;
    
- las respuestas empiezan a repetirse o acortarse.
    

No hace falta agotar la etapa.

La pregunta clave no es:

> “¿Podemos sacar más?”

La pregunta clave es:

> “¿Ya tenemos evidencia suficiente para una competencia validable?”

---

## 9. Criterio de cierre de sesión

La sesión debe cerrarse cuando ocurra una de estas condiciones:

### Cierre por éxito mínimo

Se ha obtenido:

- una competencia provisional;
    
- una evidencia concreta;
    
- una validación de la persona;
    
- una ficha mínima suficientemente clara.
    

### Cierre por suficiencia

La etapa principal ya está suficientemente cubierta y seguir preguntando aportaría poco valor.

### Cierre por fatiga

Aparecen dos o más señales de fatiga seguidas.

### Cierre por deriva

La conversación se está alejando del objetivo del piloto:

- demasiadas etapas;
    
- demasiada abstracción;
    
- demasiada explicación contextual;
    
- demasiada carga emocional;
    
- demasiada búsqueda de perfección.
    

### Cierre por baja evidencia

No se ha logrado evidencia suficiente, pero sí se ha identificado qué falta.

En ese caso, cerrar con diagnóstico:

```md
No se ha validado todavía una competencia con evidencia suficiente.

Hipótesis detectada:

Faltó evidencia sobre:

Preguntas recomendadas para una segunda sesión:
```

---

## 10. Cierre conversacional recomendado

Antes de cerrar, devolver una síntesis breve:

> “Lo que me llevo es esto: en [situación], tú hiciste [acción propia], en un contexto donde [dificultad], y eso produjo [resultado]. La competencia que parece aparecer es [competencia]. ¿Te representa? ¿Cambiarías algo?”

Después de la corrección de la persona, cerrar con:

> “Perfecto. No voy a intentar sacar más cosas ahora. Para este piloto, esto ya nos da una unidad concreta de experiencia profesional con evidencia.”

---

## 11. Evaluación posterior de la sesión

Después de la entrevista, registrar una nota de evaluación.

### Evaluación del piloto

```md
## Resultado de la sesión

¿Se obtuvo una competencia con evidencia verificable?
Sí / No / Parcialmente

## Competencia detectada

## Evidencia usada

## Validación de la persona

## Qué funcionó

## Qué no funcionó

## Señales de fatiga o fricción

## Guardarraíles activados

## Qué habría que cambiar en el playbook

## Decisión

- Mantener protocolo
- Simplificar protocolo
- Añadir guardarraíl
- Eliminar paso
- Repetir piloto
```

Esta evaluación es parte del MVP.

El objetivo del piloto no es solo producir una ficha.

También es aprender si el método merece seguir desarrollándose.

---

## 12. Reglas de oro del entrevistador

1. No preguntar por competencias antes de tener situaciones.
    
2. No aceptar etiquetas sin evidencia.
    
3. No forzar profundidad si ya hay suficiencia.
    
4. No abrir una segunda etapa si la primera ya dio valor.
    
5. No interpretar sin validar.
    
6. No confundir fatiga con falta de contenido.
    
7. No convertir una transición profesional en terapia.
    
8. No intentar demostrar que el sistema funciona a toda costa.
    
9. No cerrar sin una síntesis validada.
    
10. No medir el éxito por cantidad de información, sino por calidad de evidencia.
    

---

## 13. Definición de éxito del playbook v1

El playbook v1 habrá funcionado si, después de una sesión piloto, podemos responder afirmativamente a estas preguntas:

1. ¿La persona recordó una experiencia profesional concreta?
    
2. ¿Se identificó una acción propia?
    
3. ¿Se identificó un resultado o consecuencia?
    
4. ¿Se pudo inferir una competencia?
    
5. ¿La persona validó o corrigió esa competencia?
    
6. ¿La evidencia obtenida es suficientemente concreta?
    
7. ¿La entrevista evitó convertirse en formulario?
    
8. ¿La entrevista evitó agotar innecesariamente a la persona?
    
9. ¿La salida obtenida serviría como base para una ficha profesional, CV, relato o análisis posterior?
    

Si la respuesta es sí a la mayoría, el MVP no ha demostrado todavía todo el producto, pero sí ha demostrado que el núcleo de entrevista merece seguir vivo.

---

## 14. Decisión operativa para el primer piloto

Para la primera sesión real se recomienda:

- trabajar una sola etapa;
    
- buscar una sola competencia;
    
- limitar la ambición de salida;
    
- mantener todos los guardarraíles disponibles;
    
- activar solo los necesarios;
    
- cerrar pronto si ya hay evidencia suficiente;
    
- registrar qué habría mejorado la entrevista.
    

El primer piloto no debe demostrar que el sistema es completo.

Debe demostrar que el corazón del sistema late.