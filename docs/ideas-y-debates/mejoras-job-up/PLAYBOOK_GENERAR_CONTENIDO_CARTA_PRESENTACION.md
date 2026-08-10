---
id: PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION
tipo: playbook
version: "1.1.0"
estado: en_prueba
alcance: exclusivo_carta_presentacion
entrada_principal: guion-carta-presentacion.md
salida_principal: contenido-carta-presentacion.md
gate_entrada: GATE-GUION-CARTA-CONTENIDO
gate_salida: GATE-CONTENIDO-CARTA-COMPOSICION
---

# PLAYBOOK — Generar contenido de carta de presentación

## 1. Propósito

Este playbook transforma un:

`guion-carta-presentacion.md`

aprobado en el texto semántico final de una carta de presentación:

`contenido-carta-presentacion.md`

La fase convierte decisiones estratégicas y editoriales ya cerradas en una **comunicación profesional real dirigida a un recruiter**.

Esta capa:

- sí redacta la carta;
- sí decide formulaciones concretas;
- sí construye frases y párrafos;
- sí mejora claridad, fluidez, concisión y capacidad comunicativa;

pero:

- no cambia estrategia;
- no introduce evidencia;
- no inventa motivación;
- no decide qué argumentos usar;
- no amplía hechos;
- no decide diseño visual;
- no compone DOCX/PDF.

Principio de responsabilidad:

> **El guion decide qué decir. Esta fase decide cómo decirlo. La composición decidirá cómo presentarlo visualmente.**

---

# 2. Pregunta central

> **¿Cómo convertir fielmente las decisiones del guion en una carta que una persona profesional realmente enviaría a un recruiter, clara, concreta, persuasiva y natural, sin introducir ninguna estrategia, evidencia, motivación, cultura o atribución nueva?**

---

# 3. Resultado esperado

La salida debe poder entregarse directamente a una futura capa de composición sin que dicha capa tenga que:

- reescribir;
- resumir;
- ampliar;
- suavizar;
- corregir tono;
- cambiar argumentos;
- introducir datos;
- eliminar contenido semántico.

Una salida válida es, por tanto, **semánticamente final**.

---

# 4. Flujo

```text
candidatura.md
        ↓
guion-carta-presentacion.md
        ↓
GATE-GUION-CARTA-CONTENIDO
        ↓
PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION
        ↓
contenido-carta-presentacion.md
        ↓
GATE-CONTENIDO-CARTA-COMPOSICION
        ↓
futura composición
```

---

# 5. Autoridades

| Fuente | Autoridad |
| --- | --- |
| `guion-carta-presentacion.md` | Autoridad editorial inmediata |
| `candidatura.md` | Estrategia común de candidatura |
| `datos-core-busqueda.md` | Autoridad factual profesional |
| `analisis-oferta.md` | Contexto y trazabilidad de la oportunidad |
| declaraciones verificadas del usuario | Motivación, preferencias y relación personal |
| fuentes culturales autorizadas | Contexto corporativo permitido |

La redacción debe trabajar principalmente desde el guion.

Las demás fuentes se utilizan para:

- comprobación;
- resolución de referencias;
- control factual.

No pueden utilizarse para seleccionar por cuenta propia material nuevo.

---

# 6. Precondiciones

Antes de redactar deben cumplirse todas:

1. existe `guion-carta-presentacion.md`;
2. su estado es `apto`;
3. `GATE-GUION-CARTA-CONTENIDO` está aprobado humanamente;
4. la candidatura está vigente;
5. `presentada: false`;
6. el destinatario está determinado en el guion;
7. el idioma está determinado;
8. el argumento central está definido;
9. las evidencias narrables están seleccionadas;
10. motivaciones y relaciones personales están clasificadas;
11. las fuentes culturales permitidas están resueltas;
12. las prohibiciones del guion están disponibles.

Si una precondición material falla:

```text
→ no redactar
→ escalar al origen correspondiente
```

---

# 7. Roles obligatorios de la IA

La generación no debe ejecutarse desde una única voz genérica.

La IA debe adoptar secuencialmente tres roles.

---

## 7.1 Rol 1 — Redactor senior de candidaturas laborales

### Misión

Convertir el guion en una carta que una persona profesional realmente podría enviar.

Debe optimizar:

- claridad;
- naturalidad;
- concreción;
- economía de lenguaje;
- fuerza argumental;
- fluidez;
- capacidad de generar interés;
- voz del candidato.

### Pregunta central

> **¿Cómo diría una persona profesional esta idea ante un recruiter para resultar clara y convincente utilizando únicamente lo autorizado por el guion?**

### Debe evitar especialmente

- lenguaje de auditoría;
- lenguaje de expediente;
- formulaciones defensivas;
- frases que expliquen restricciones internas;
- burocracia;
- abstracción innecesaria;
- estructuras artificialmente perfectas;
- clichés de carta de presentación;
- grandilocuencia;
- servilismo;
- entusiasmo inventado.

Este rol redacta la primera versión.

---

## 7.2 Rol 2 — Recruiter senior receptor de la carta

### Misión

Leer la carta como destinatario real, no como autor ni como auditor técnico.

Debe imaginar que recibe esta carta junto a muchas candidaturas.

### Pregunta central

> **Si recibiera esta carta hoy, ¿me ayuda realmente a entender por qué merece la pena considerar al candidato o percibo el mecanismo que ha generado el texto?**

Debe evaluar:

- relevancia inmediata;
- comprensión del encaje;
- evidencia;
- utilidad de cada párrafo;
- capacidad de mantener interés;
- complementariedad con el CV;
- naturalidad;
- personalización;
- concisión;
- credibilidad;
- ausencia de lenguaje artificial.

Este rol puede exigir una nueva redacción.

No puede introducir hechos ni estrategia.

---

## 7.3 Rol 3 — Auditor senior de factualidad y contrato

### Misión

Evitar que la mejora comunicativa de los dos roles anteriores amplíe indebidamente los hechos.

### Pregunta central

> **¿Cada afirmación profesional final permanece dentro del significado, alcance y autoridad concedidos por el guion y sus fuentes factuales?**

Debe detectar:

- evidencia nueva;
- alcance ampliado;
- métricas alteradas;
- responsabilidades infladas;
- seniority inflado;
- tecnologías no acreditadas;
- formación convertida en titulación;
- transferibilidad presentada como experiencia literal;
- motivaciones fabricadas;
- cultura transformada en atributo personal;
- empresa anónima convertida en conocida.

Si mejorar una frase obliga a inventar:

```text
→ no mejorar así
```

---

# 8. Orden obligatorio de ejecución

La secuencia será:

```text
ROL 1 — Redactor
        ↓
primera redacción
        ↓
ROL 2 — Recruiter
        ↓
crítica comunicativa
        ↓
revisión editorial si procede
        ↓
ROL 3 — Auditor
        ↓
control factual y contractual
        ↓
ajustes solo si no cambian estrategia
        ↓
segunda lectura como recruiter
        ↓
contenido final
```

La auditoría factual no debe convertir nuevamente la carta en lenguaje defensivo.

---

# 9. Principio de fidelidad al guion

La fase puede:

- redactar;
- parafrasear;
- condensar;
- fusionar ideas;
- dividir frases;
- cambiar sintaxis;
- eliminar redundancias;
- mejorar transiciones;
- adaptar orden local cuando el guion lo permita.

No puede:

- crear argumentos;
- seleccionar nueva evidencia;
- crear motivación;
- añadir cultura;
- alterar carencias;
- cambiar destinatario;
- cambiar posicionamiento;
- reconsiderar competitividad general.

---

# 10. Regla de no expansión semántica

Toda afirmación profesional visible debe poder responder:

> **¿Qué decisión `A-NNN` del guion autoriza esta afirmación?**

Las únicas excepciones son elementos funcionales:

- saludo;
- transición;
- cortesía;
- despedida;
- conexión gramatical.

Una frase profesional no trazable no puede permanecer.

---

# 11. Guardarraíl fundamental — Restricción no equivale a contenido

Una restricción del guion:

> **regula lo que puede escribirse, pero no constituye por sí misma algo que deba decirse al recruiter.**

Ejemplo interno:

```text
No presentar cuadres de caja como tesorería.
```

Esto NO autoriza una carta como:

```text
Mi experiencia se limita a realizar cuadres de caja.
```

Debe formularse positivamente el hecho verdadero:

```text
Realizaba cuadres de caja...
```

manteniendo internamente la prohibición de llamarlo tesorería.

Regla bloqueante:

> **Está prohibido trasladar automáticamente guardarraíles, advertencias, límites de atribución o controles internos al texto visible.**

---

# 12. Guardarraíl de afirmación positiva

Cuando un hecho puede expresarse correctamente de forma afirmativa, debe preferirse la formulación positiva.

Patrones de riesgo:

```text
sin convertir...
sin afirmar...
sin presentar...
sin atribuir...
mi experiencia se limita a...
aunque no...
no debe confundirse con...
```

Estos patrones activan revisión obligatoria.

La IA debe preguntar:

> **¿Esta negación aporta información útil al recruiter o simplemente explica una falsedad que el sistema ha evitado?**

Si únicamente documenta una precaución interna:

```text
→ eliminar del texto visible
```

Esto no implica prohibir todas las negaciones.

Una negación puede permanecer cuando tenga auténtico valor comunicativo.

---

# 13. Guardarraíl de voz del candidato

Toda frase visible debe superar:

> **¿Es plausible que el propio candidato dijera esta frase espontáneamente en una conversación profesional con el recruiter?**

Ejemplo no válido:

```text
La disponibilidad para turnos rotativos está confirmada.
```

Ejemplo válido:

```text
Tengo disponibilidad para trabajar en turnos rotativos.
```

La carta debe hablar con voz del candidato.

No con voz de:

- auditor;
- analista;
- sistema;
- evaluador;
- expediente;
- playbook.

---

# 14. Guardarraíl contra lenguaje metaanalítico

La carta no debe describir el proceso interno utilizado para construirla.

Patrones que requieren revisión:

```text
la oferta describe...
el contexto de la oferta...
según el análisis...
la evidencia demuestra...
esta experiencia conecta con la necesidad...
está confirmado...
el candidato...
la candidatura...
se ha identificado...
```

No son cadenas absolutamente prohibidas en cualquier contexto.

Son **indicadores de voz analítica**.

Si la frase explica cómo el sistema interpreta la candidatura en lugar de comunicar directamente al recruiter:

```text
→ reescribir
```

La carta habla:

```text
del candidato
a la empresa/recruiter
sobre la oportunidad
```

No habla:

```text
del análisis de la candidatura
```

---

# 15. Guardarraíl de utilidad frase por frase

Toda oración visible debe justificar su existencia.

Valores válidos:

```text
entiende_encaje
obtiene_evidencia
entiende_valor
entiende_motivacion_real
obtiene_contexto_relevante
entiende_disponibilidad
facilita_continuidad
```

Valor no válido:

```text
demuestra_que_el_sistema_no_ha_inventado
```

Si una frase solo sirve para demostrar prudencia del sistema:

```text
→ eliminar o reformular
```

---

# 16. Guardarraíl de comunicación positiva

La carta debe explicar principalmente:

```text
qué ha hecho
qué sabe hacer
qué puede aportar
por qué es relevante
```

No debe construirse principalmente alrededor de:

```text
qué no hizo
qué no sabe
qué no puede afirmar
qué interpretación debe evitarse
```

Las limitaciones siguen siendo obligatorias, pero funcionan como fronteras invisibles.

---

# 17. Guardarraíl anti-segundo-CV

Pregunta obligatoria:

> **¿La carta explica por qué las evidencias importan para esta oportunidad o simplemente vuelve a enumerarlas?**

Si la carta se limita a repetir:

- puestos;
- cronología;
- competencias;
- herramientas;
- tareas;
- métricas;

sin construir significado:

```text
estado_contenido: requiere_correccion
```

Preferencia argumental:

```text
necesidad relevante
+
evidencia seleccionada
+
valor transferible
```

---

# 18. Guardarraíl anti-genericidad

Pregunta:

> **¿Esta carta podría enviarse prácticamente a otra empresa cambiando únicamente el nombre y el puesto?**

Si la respuesta es `sí`:

```text
estado_contenido: requiere_correccion
```

La especificidad puede provenir de:

- necesidades concretas del puesto;
- selección de evidencias;
- contexto funcional;
- empresa;
- cultura autorizada;
- modelo operativo;
- destinatario.

No es obligatorio utilizar todos.

---

# 19. Guardarraíl anti-IA

No basta con afirmar que el texto «suena natural».

El recruiter debe comprobar explícitamente:

- abstracciones innecesarias;
- conectores mecánicos;
- repetición de estructuras;
- frases excesivamente simétricas;
- lenguaje corporativo genérico;
- elogios vacíos;
- clichés;
- exceso de adjetivos;
- reformulación literal de la oferta;
- lenguaje excesivamente pulido;
- párrafos de tamaño artificialmente uniforme;
- conclusión intercambiable;
- introducción intercambiable;
- explicaciones que una persona no consideraría necesario dar;
- formulaciones propias de análisis o evaluación.

Principio:

> **Preferir lenguaje concreto y directo sobre lenguaje conceptual cuando ambos expresen el mismo significado.**

---

# 20. Guardarraíl de primera lectura recruiter

La carta debe superar un primer escaneo rápido.

Tras leer apertura y primeras líneas debe resultar reconocible:

1. para qué posición escribe;
2. cuál es el núcleo de su encaje;
3. por qué merece seguir leyendo.

Si esto requiere interpretar varios párrafos:

```text
→ requiere_correccion
```

---

# 21. Apertura

Debe:

- identificar la oportunidad;
- entrar rápidamente en materia;
- presentar encaje sin lenguaje analítico;
- evitar fórmulas burocráticas;
- evitar entusiasmo no acreditado.

Evitar como patrón por defecto:

```text
Por medio de la presente...
Tengo el placer de...
Me complace enormemente...
Desde siempre...
```

No son prohibiciones lingüísticas absolutas; requieren justificación real.

---

# 22. Argumentación

Cada párrafo debe cumplir una función clara.

Preferencia:

```text
evidencia
→ significado
→ relación con la oportunidad
```

La carta no necesita explicar exhaustivamente toda la candidatura.

Debe seleccionar pocas evidencias de alto valor ya autorizadas por el guion.

---

# 23. Evidencias

Solo pueden utilizarse las seleccionadas en el guion.

Se puede cambiar su formulación.

No puede cambiarse:

- alcance;
- métrica;
- responsabilidad;
- contexto;
- titularidad;
- seniority;
- dominio tecnológico;
- resultado.

La atribución colectiva debe conservarse cuando corresponda.

---

# 24. Motivación

Solo puede presentarse como motivación personal aquello que haya sido declarado o autorizado como tal.

Si:

```text
motivacion_usuario: ninguna
```

la carta debe funcionar sin emoción inventada.

Puede utilizar razones profesionales factuales.

Ejemplo permitido:

```text
Mi experiencia en operaciones de supermercado resulta directamente aplicable a...
```

No convertirlo en:

```text
Me apasiona el retail...
```

---

# 25. Cultura

La cultura autorizada puede:

- contextualizar;
- mostrar conocimiento de la empresa;
- relacionarse con procesos o condiciones de incorporación;
- apoyar la transición hacia procedimientos específicos.

No puede transformarse en:

```text
comparto sus valores
me identifico con su cultura
su filosofía encaja conmigo
me atrae especialmente...
```

salvo declaración personal autorizada.

La cultura de empresa:

```text
≠
atributo del candidato
```

---

# 26. Empresa anónima

Si el empleador real no está identificado:

- no inferirlo;
- no buscar pistas para adivinarlo;
- no usar cultura del intermediario como cultura del empleador;
- no redactar como si se conociera la empresa;
- personalizar mediante puesto, funciones, sector y necesidades conocidas.

---

# 27. ATS y recruiter IA

Prioridad:

```text
factualidad
>
utilidad recruiter
>
argumentación
>
naturalidad
>
compatibilidad ATS/IA
```

El vocabulario autorizado debe integrarse de forma natural.

No:

- keyword stuffing;
- listas disfrazadas de párrafo;
- repetición artificial del cargo;
- introducción de keywords sin respaldo.

---

# 28. Longitud

Debe respetarse el rango definido en el guion.

Si puede expresarse lo mismo con menos palabras:

```text
preferir versión más breve
```

No rellenar espacio.

Una página completa no constituye objetivo.

---

# 29. Tono

Debe respetar el guion.

Como norma general:

- profesional;
- humano;
- directo;
- sobrio;
- seguro;
- específico.

Evitar:

- arrogancia;
- servilismo;
- grandilocuencia;
- exceso de entusiasmo;
- lenguaje corporativo vacío;
- frialdad administrativa.

---

# 30. Saludo y destinatario

No inventar:

- nombre;
- género;
- cargo;
- departamento;
- tratamiento;

si no están acreditados.

Utilizar fórmula profesional genérica cuando corresponda.

---

# 31. Cierre

Debe facilitar continuidad.

Puede:

- expresar disponibilidad;
- proponer conversación;
- ofrecer ampliación de información.

No debe:

- presionar;
- prometer;
- suplicar;
- introducir motivación nueva;
- cerrar con clichés grandilocuentes.

---

# 32. Privacidad

Solo incorporar datos personales autorizados para la candidatura.

No trasladar automáticamente todos los datos del CV.

La decisión visual sobre datos de contacto pertenece a composición.

---

# 33. Salida

`contenido-carta-presentacion.md` debe contener:

## A. Metadatos y controles

- candidatura;
- empresa;
- puesto;
- idioma;
- versiones;
- fuentes;
- trazabilidad;
- controles;
- incidencias;
- estado.

## B. Carta completa consolidada

Texto semántico final.

No contiene decisiones de:

- tipografía;
- tamaños;
- colores;
- márgenes;
- saltos de página;
- estilos DOCX;
- LaTeX;
- posición gráfica.

---

# 34. Trazabilidad

Cada bloque semántico debe registrar:

```yaml
bloque: B-NN
funcion:
refs_guion:
  - A-NNN
```

No es necesario etiquetar cada frase si la trazabilidad del bloque es inequívoca.

---

# 35. Autocontrol obligatorio del Redactor

Antes de entregar al Recruiter:

- [ ] he escrito con voz de candidato;
- [ ] no he introducido hechos;
- [ ] no he convertido restricciones en contenido;
- [ ] he preferido afirmaciones positivas;
- [ ] no he explicado cautelas internas;
- [ ] no he convertido la carta en un CV;
- [ ] no he fabricado emoción;
- [ ] no he convertido cultura en afinidad;
- [ ] la carta tiene una tesis reconocible;
- [ ] cada párrafo aporta algo.

---

# 36. Control obligatorio del Recruiter

Debe responder:

### R1. Primer escaneo

¿Entiendo rápidamente puesto y encaje?

`si | no`

### R2. Utilidad

¿Cada párrafo me ayuda a evaluar al candidato?

`si | no`

### R3. Voz real

¿Parece escrito por el candidato y no por un sistema?

`si | no`

### R4. Segundo CV

`interpreta_y_conecta | repite_cv`

### R5. Genericidad

¿Podría enviarse casi igual a otra empresa?

`si | no`

### R6. Lenguaje defensivo

¿Expone restricciones internas?

`si | no`

### R7. Lenguaje metaanalítico

¿Habla del análisis en lugar de hablar al recruiter?

`si | no`

### R8. Artificialidad IA

¿Hay señales materiales de texto generado?

`si | no`

Cualquier fallo material:

```text
→ regresar al Rol 1
```

---

# 37. Control obligatorio del Auditor

Debe verificar:

- [ ] todas las afirmaciones profesionales trazables;
- [ ] métricas exactas;
- [ ] responsabilidades no ampliadas;
- [ ] seniority correcto;
- [ ] formación correcta;
- [ ] herramientas correctas;
- [ ] resultados correctos;
- [ ] atribuciones colectivas conservadas;
- [ ] motivaciones autorizadas;
- [ ] cultura utilizada correctamente;
- [ ] empresa/intermediario correctamente tratados;
- [ ] privacidad conforme.

Un fallo factual no puede resolverse inventando una formulación.

---

# 38. Segunda lectura recruiter

Tras auditoría factual debe ejecutarse de nuevo una lectura recruiter.

Motivo:

> **La corrección factual no puede degradar la carta hasta convertirla en texto defensivo o administrativo.**

Si ocurre:

```text
→ reformular manteniendo la misma frontera factual
```

---

# 39. Incidencias

Tipos:

```text
editorial
factual
trazabilidad
origen
privacidad
arquitectura
```

Si aparece nueva evidencia:

```text
→ no incorporar
→ requiere_actualizacion_factual
```

Si falta una decisión del guion:

```text
→ no decidir localmente
→ requiere_revision_origen
```

---

# 40. Estados

```text
apto
requiere_correccion
requiere_revision_origen
requiere_actualizacion_factual
bloqueado
```

Precedencia:

```text
bloqueado
>
requiere_actualizacion_factual
>
requiere_revision_origen
>
requiere_correccion
>
apto
```

---

# 41. Condiciones de `apto`

Solo puede declararse `apto` si:

1. factualidad superada;
2. trazabilidad superada;
3. fidelidad al guion superada;
4. primer escaneo recruiter superado;
5. lenguaje defensivo ausente;
6. lenguaje metaanalítico ausente;
7. voz del candidato superada;
8. segundo CV descartado;
9. genericidad descartada;
10. naturalidad superada;
11. anti-IA superado;
12. cultura conforme;
13. motivación conforme;
14. ATS/IA natural;
15. privacidad conforme;
16. longitud conforme.

---

# 42. Gate de salida

`GATE-CONTENIDO-CARTA-COMPOSICION`

Pregunta:

> **¿El contenido final expresa fielmente el guion y funciona como una carta profesional real, factual, concreta, natural y útil para el recruiter, de manera que pueda pasar a composición sin ninguna decisión semántica adicional?**

La IA:

```text
recomienda aprobar
|
recomienda no_aprobar
```

La IA no aprueba humanamente el gate.

---

# 43. Casos de prueba mínimos

## T1 — Sin motivación personal

Debe generar una carta válida sin fabricar emoción.

## T2 — Cultura autorizada

Debe utilizarla como contexto sin atribuir afinidad.

## T3 — Evidencia no seleccionada

No puede incorporarse aunque exista en datos-core.

## T4 — Segundo CV

Debe detectarse.

## T5 — Keyword no autorizada

Debe rechazarse.

## T6 — Frase no trazable

Debe corregirse o escalarse.

## T7 — Carta genérica

Debe detectarse.

## T8 — Entusiasmo inventado

Debe detectarse.

## T9 — Longitud incorrecta

Debe corregirse.

## T10 — Empresa anónima

Debe funcionar sin inventar identidad.

## T11 — Nueva evidencia

Debe devolverse al flujo factual.

## T12 — Expansión semántica

Debe detectarse.

## T13 — Restricción convertida en contenido

Entrada conceptual:

```text
no presentar cuadres de caja como tesorería
```

La carta no puede producir lenguaje como:

```text
mi experiencia se limita...
```

Debe afirmar positivamente el hecho permitido.

## T14 — Voz de auditor

Texto como:

```text
la disponibilidad está confirmada
```

debe detectarse como voz incorrecta cuando pueda expresarse naturalmente en primera persona.

## T15 — Lenguaje metaanalítico

Texto que describe el análisis o el «contexto de la oferta» debe activarse para revisión cuando no aporta valor recruiter.

## T16 — Precaución interna visible

Una frase cuya única función sea demostrar que no se inventó un hecho debe eliminarse.

## T17 — Anti-IA

Debe detectar párrafos artificialmente simétricos, abstracción excesiva o clichés materiales.

## T18 — Regresión tras auditoría factual

Una corrección factual no debe volver defensivo el texto.

---

# 44. Regla de aprendizaje de pruebas

Cuando una prueba real detecte un defecto:

1. determinar si es específico del caso o generalizable;
2. si es generalizable, convertirlo en regla del playbook;
3. reflejarlo en el template;
4. añadir test cuando sea automatizable;
5. regenerar el caso desde el contrato actualizado.

Principio:

> **Una corrección generalizable no debe quedarse como memoria informal de una candidatura concreta.**

---

# 45. Principio final

> **La carta final debe ocultar la maquinaria que garantiza su rigor.**

El recruiter debe recibir:

- hechos correctos;
- selección relevante;
- argumento comprensible;
- lenguaje humano;
- comunicación profesional.

No debe recibir:

- nuestros guardarraíles;
- nuestras cautelas;
- nuestra auditoría;
- nuestro análisis interno;
- nuestra arquitectura.

La mejor prueba de este playbook no es que la carta demuestre que el sistema fue prudente.

La mejor prueba es que **parezca una buena carta profesional y siga siendo rigurosamente cierta**.