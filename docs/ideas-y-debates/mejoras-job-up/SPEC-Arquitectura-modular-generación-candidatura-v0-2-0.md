---
id: spec-arquitectura-generacion-candidaturas-job-up
titulo: SPEC — Arquitectura modular para generación de candidaturas en Job-up
version: "0.2.0"
estado: borrador_operativo
fecha_version: 2026-08-02
host: carrera-ai
rama: job-up
origen_historico: sesion-20260801-2040-job-up
sustituye: "0.1.0"
---
# SPEC — Arquitectura modular para generación de candidaturas en Job-up

## 1. Propósito

Este documento fija la arquitectura objetivo, el estado actual de implantación y el orden de trabajo para rediseñar la generación de candidaturas dentro de `job-up`.

Su finalidad principal es impedir que futuras sesiones de trabajo:

* pierdan decisiones ya tomadas;
* vuelvan a diseñar desde cero partes ya acordadas;
* mezclen análisis, estrategia, redacción y composición documental;
* avancen a una fase sin haber validado suficientemente la anterior;
* confundan arquitectura futura con funcionalidad ya implementada;
* introduzcan cambios sin dejar trazabilidad.

Este SPEC debe actuar como fuente estable de continuidad para esta línea concreta de `job-up`.

No sustituye:

* `estado-actual.md`;
* las sesiones PCS;
* `AGENTS.md`;
* los playbooks específicos;
* los datos core;
* el seguimiento operativo de candidaturas.

---

## 2. Autoridad y relación con PCS

Este SPEC conserva la arquitectura y las decisiones de diseño de esta línea de trabajo.

La relación entre fuentes queda así:

```text
SPEC
→ arquitectura, decisiones y orden de maduración

.pcs/estado/estado-actual.md
→ estado operativo vigente del host

sesión PCS vigente
→ bloque concreto de trabajo actual

AGENTS.md
→ reglas de operación del host

playbooks
→ comportamiento normativo de cada fase

artefactos de candidatura
→ estado y contenido de cada caso concreto
```

La referencia:

```text
sesion-20260801-2040-job-up
```

es el origen histórico de esta versión del SPEC.

No debe asumirse que seguirá siendo siempre la sesión PCS activa.

Cuando una futura sesión continúe esta línea:

1. debe leer el SPEC vigente;
2. debe consultar `estado-actual.md`;
3. debe identificar la sesión PCS activa correspondiente;
4. no debe modificar el SPEC únicamente porque haya cambiado la sesión.

El SPEC se actualiza cuando cambia la arquitectura, una decisión relevante o el estado de maduración de una fase.

---

## 3. Gobernanza del SPEC

### 3.1 Versionado

El documento usa versionado incremental.

Ejemplo:

```text
0.1.0 → primera arquitectura consolidada
0.2.0 → incorporación de criterios de cierre y gobernanza
0.2.1 → corrección menor sin cambio arquitectónico
0.3.0 → modificación relevante de una fase
1.0.0 → arquitectura validada como base operativa
```

### 3.2 Estados

Estados previstos:

* `borrador_operativo`;
* `en_validacion`;
* `vigente`;
* `sustituido`.

### 3.3 Modificación de decisiones

Las decisiones de este documento se identifican como:

```text
ARQ-XX
```

para diferenciarlas de decisiones PCS formales.

Una decisión arquitectónica futura puede:

* mantenerse;
* matizarse;
* sustituirse;
* retirarse.

Cuando una decisión cambie debe registrarse:

```text
ARQ-XX
estado: sustituida
sustituida_por: ARQ-YY
motivo: ...
```

No se elimina silenciosamente una decisión anterior.

---

## 4. Contexto

`job-up` es una rama operativa dentro de `carrera-ai` dedicada a búsqueda de empleo y preparación de candidaturas revisables.

El flujo anterior tendía a mezclar:

* análisis de oportunidad;
* decisión estratégica;
* adaptación del CV;
* selección de evidencias;
* redacción del CV;
* redacción de la carta;
* generación documental;
* validación posterior.

La nueva arquitectura separa estas responsabilidades.

La intención final es disponer de una skill directora de orquesta que coordine procesos especializados.

La skill directora no debe concentrar toda la lógica en un único prompt.

---

# PARTE I — ARQUITECTURA OBJETIVO

## 5. Principio arquitectónico central

La generación de candidatura se divide conceptualmente en dos mundos.

### Mundo IA

Incluye:

* análisis;
* interpretación;
* estrategia;
* selección;
* redacción.

### Mundo técnico

Incluye:

* materialización;
* composición;
* conversión;
* formato;
* validación técnica.

La frontera futura será:

```text
datos-generacion.json
```

Arquitectura objetivo:

```text
razonamiento y redacción
→ datos-generacion.json
→ composición determinista
→ documentos finales
```

Regla arquitectónica:

> Los errores de contenido deben corregirse en la fase que genera el contenido o en su representación estructurada.

> Los errores de composición deben corregirse en templates o código de composición.

Esta regla pertenece a la arquitectura objetivo.

Todavía no está plenamente implantada.

---

## 6. Dos puertas de entrada

La arquitectura prevé dos formas de iniciar una candidatura.

### 6.1 Por oferta

```text
oferta
→ PLAYBOOK_ANALISIS_OFERTA
→ analisis-oferta.md
```

Este flujo parte de una oportunidad explícita.

El análisis debe determinar:

* contenido factual de la oferta;
* empresa publicadora;
* empresa contratante cuando sea identificable;
* requisitos;
* prioridades;
* posible problema empresarial;
* encaje factual;
* carencias;
* riesgos;
* argumento competitivo;
* decisión estratégica.

No debe redactar los documentos finales.

---

### 6.2 Por empresa objetivo

Arquitectura prevista:

```text
empresa objetivo
→ futuro PLAYBOOK_ANALISIS_EMPRESA_OBJETIVO
→ artefacto de análisis
```

Su finalidad será permitir presentación espontánea o candidatura sin oferta explícita.

Debe investigar:

* actividad;
* contexto;
* necesidades razonablemente inferibles;
* posibles áreas de aportación;
* encaje;
* riesgos;
* argumento de aproximación;
* límites factuales.

### Hipótesis pendiente de validar

La arquitectura **pretende** que esta vía converja posteriormente en `candidatura.md`.

Esta convergencia todavía no se considera validada.

Antes de declararla definitiva deberá comprobarse que `PLAYBOOK_CANDIDATURA` y su template funcionan también con una oportunidad sin requisitos explícitos de oferta.

---

## 7. Ficha común de candidatura

Arquitectura prevista:

```text
análisis de oportunidad
→ PLAYBOOK_CANDIDATURA
→ candidatura.md
```

`candidatura.md` es la ficha viva de la candidatura.

Debe gobernar:

* identidad;
* origen;
* decisión estratégica;
* posicionamiento;
* evidencias prioritarias;
* límites;
* advertencias;
* datos pendientes;
* bloqueos;
* estado;
* artefactos;
* siguiente fase.

No debe:

* rehacer el análisis;
* redactar CV;
* redactar carta;
* producir el guion;
* sustituir el veredicto.

Debe distinguir:

```text
decisión estratégica
≠
estado operativo
```

---

## 8. Adaptación estratégica

Arquitectura prevista:

```text
PLAYBOOK_GUION_ADAPTACION_CV
→ guion-adaptacion-cv.md
```

Esta fase transforma:

```text
análisis
+ candidatura.md
+ datos core
```

en una estrategia concreta de adaptación.

Debe decidir, entre otros:

* relato;
* experiencias a priorizar;
* evidencias;
* elementos a omitir;
* tono;
* riesgos;
* límites;
* tratamiento de carencias;
* foco del CV;
* relación estratégica con la carta.

No debe redactar todavía los documentos finales.

---

## 9. Generación única de contenido

Arquitectura futura:

```text
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
→ datos-generacion.json
```

Esta fase se diseñará después de validar las anteriores.

Consumirá previsiblemente:

```text
análisis de oportunidad
+ candidatura.md
+ guion-adaptacion-cv.md
+ datos-core-busqueda.md
+ datos privados autorizados
```

Producirá el contenido final estructurado para CV y carta.

La decisión arquitectónica es:

> CV, carta y LaTeX no deben convertirse en tres procesos independientes de redacción.

La redacción debe realizarse una sola vez.

---

## 10. Necesidades futuras detectadas para `datos-generacion.json`

No debe diseñarse todavía su schema definitivo.

Sí se mantendrá una lista de requisitos descubiertos durante las fases anteriores.

Esta lista no constituye contrato.

Estado inicial:

* deberá permitir generar CV;
* deberá permitir generar carta;
* deberá permitir generar LaTeX;
* deberá distinguir datos de contenido y metadatos;
* deberá mantener trazabilidad suficiente;
* deberá impedir divergencias entre formatos.

Cada prueba de `candidatura.md` o `guion-adaptacion-cv.md` podrá añadir aquí necesidades futuras.

No deben crearse campos definitivos antes de diseñar la fase de generación.

---

## 11. Composición documental

Arquitectura futura:

```text
datos-generacion.json
→ generar_candidatura.py
→ documentos
```

Documentos previstos:

```text
cv.docx
cv.pdf
cv.tex
carta-presentacion.docx
carta-presentacion.pdf
```

El compositor:

* no analiza;
* no selecciona estrategia;
* no redacta;
* no corrige semántica;
* no inventa;
* no cambia hechos;
* no modifica silenciosamente el contenido.

---

## 12. Veredicto

Arquitectura futura:

```text
documentos finales
→ playbook de veredicto
→ veredicto-final-cv.md
```

El veredicto deberá evaluar al menos:

* integridad factual;
* privacidad;
* coherencia;
* calidad;
* adecuación;
* riesgos;
* posibles defectos.

Los criterios concretos, severidades y umbrales deberán definirse cuando se revise esta fase.

No se fijan en este SPEC porque todavía no corresponde diseñarla.

Principio futuro:

> El veredicto no parchea directamente un DOCX.

Un defecto de contenido debe retornar a la fase de contenido.

Un defecto de composición debe retornar a la capa técnica.

---

## 13. Preparación de entrevista

Fase posterior y condicional.

Arquitectura prevista:

```text
candidatura preparada o enviada
→ playbook específico
→ informe de entrevista
```

No forma parte del núcleo inmediato de rediseño.

---

## 14. Arquitectura objetivo completa

### Por oferta

```text
oferta
→ PLAYBOOK_ANALISIS_OFERTA
→ analisis-oferta.md
→ PLAYBOOK_CANDIDATURA
→ candidatura.md
→ PLAYBOOK_GUION_ADAPTACION_CV
→ guion-adaptacion-cv.md
→ PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
→ datos-generacion.json
→ generar_candidatura.py
→ cv + carta
→ veredicto
→ entrevista si procede
```

### Por empresa objetivo

```text
empresa objetivo
→ futuro PLAYBOOK_ANALISIS_EMPRESA_OBJETIVO
→ artefacto de análisis
→ posible convergencia en PLAYBOOK_CANDIDATURA
→ candidatura.md
→ resto del flujo común
```

La convergencia de la segunda vía es todavía una hipótesis arquitectónica.

---

# PARTE II — ESTADO REAL DE IMPLANTACIÓN

## 15. Estado de cada fase

| Fase                                     | Estado actual          |
| ---------------------------------------- | ---------------------- |
| `PLAYBOOK_ANALISIS_OFERTA`               | avanzado               |
| `TEMPLATE_ANALISIS_OFERTA_v2`            | avanzado               |
| prueba de `analisis-oferta.md`           | realizada parcialmente |
| `PLAYBOOK_CANDIDATURA`                   | diseñado               |
| `TEMPLATE_CANDIDATURA_v2`                | diseñado               |
| prueba de `candidatura.md`               | en validación          |
| `PLAYBOOK_GUION_ADAPTACION_CV`           | pendiente              |
| template de guion                        | pendiente              |
| prueba de guion                          | pendiente              |
| `PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA` | futuro                 |
| `datos-generacion.json`                  | futuro                 |
| adaptación de `generar_candidatura.py`   | futura                 |
| adaptación del veredicto                 | futura                 |
| análisis empresa objetivo                | futuro                 |
| preparación entrevista                   | futura                 |

---

## 16. Estados de maduración de una fase

Cada fase debe usar estos estados:

```text
pendiente
→ diseñada
→ en_prueba
→ validada
```

### Pendiente

No existe todavía un diseño suficiente.

### Diseñada

Existe:

* playbook;
* contrato;
* template si procede;
* criterios de prueba.

Pero aún no se considera demostrada.

### En prueba

La fase está siendo ejecutada sobre casos reales o controlados.

Se registran:

* defectos;
* ambigüedades;
* fricciones;
* cambios necesarios.

### Validada

La fase ha superado explícitamente sus criterios de cierre.

Solo entonces debe considerarse estable para alimentar la fase siguiente.

---

# PARTE III — CRITERIOS DE CIERRE

## 17. Regla general de cierre

Ninguna fase se declara validada únicamente porque:

* el documento exista;
* haya producido una salida;
* una ejecución no haya dado error;
* un único caso parezca correcto.

Una fase se valida cuando:

1. existe contrato suficientemente claro;
2. existe al menos una prueba relevante;
3. se han ejecutado sus controles;
4. los defectos encontrados se han corregido o documentado;
5. no existen bloqueos conocidos que invaliden su uso;
6. puede alimentar la fase siguiente sin obligarla a reconstruir decisiones anteriores.

Cuando una fase requiera más de un tipo de caso para demostrar generalidad, debe indicarse explícitamente.

---

## 18. Criterios de cierre actuales de `candidatura.md`

La fase actual es:

```text
PLAYBOOK_CANDIDATURA
→ candidatura.md
```

Estado:

```text
en_prueba
```

Antes de declararla validada debe comprobarse al menos:

### Responsabilidad

* [ ] `candidatura.md` gobierna el ciclo de vida.
* [ ] No repite el análisis completo.
* [ ] No redacta documentos posteriores.
* [ ] No vuelve a decidir silenciosamente el encaje.

### Trazabilidad

* [ ] El origen está identificado.
* [ ] El artefacto de análisis está identificado.
* [ ] La decisión estratégica procede del análisis.
* [ ] Las evidencias mantienen trazabilidad.
* [ ] Las afirmaciones excluidas mantienen su origen.

### Estado

* [ ] Decisión estratégica y estado operativo son independientes.
* [ ] `presentada` representa un hecho real.
* [ ] Los bloqueos afectan correctamente al estado.
* [ ] La siguiente fase está identificada.

### Economía documental

* [ ] No replica matrices o razonamientos del análisis.
* [ ] No duplica el contenido de futuros artefactos.
* [ ] Mantiene suficiente información para gobernar sin tener que reconstruir toda la oportunidad.

### Artefactos

* [ ] El inventario representa documentos reales o previstos.
* [ ] Los estados son coherentes.
* [ ] Los enlaces existentes funcionan.

### Prueba

* [ ] `CAND-2026-019` ha sido revisada completamente contra este contrato.
* [ ] Los defectos encontrados han sido clasificados.
* [ ] Las correcciones generalizables se han aplicado al playbook/template.
* [ ] No quedan defectos estructurales conocidos.

Después de esta prueba deberá decidirse si se necesita un segundo caso antes de cerrar definitivamente la fase.

---

## 19. Prueba de generalidad de `candidatura.md`

La arquitectura no impone automáticamente un número fijo de pruebas.

Sin embargo, debe comprobarse si CAND-2026-019 es suficiente para validar el modelo.

Después de evaluarla se tomará una decisión explícita:

```text
A. caso suficiente para validar
B. necesita segundo caso por oferta
C. necesita prueba de otro tipo de origen antes de validar completamente
```

Si se elige un segundo caso, debe aportar variedad real.

Ejemplos posibles:

* empresa publicadora = empresa contratante;
* puesto administrativo frente a tecnológico;
* candidatura con bloqueos;
* candidatura con decisión distinta de `preparar_con_advertencias`.

No se debe probar un segundo caso únicamente para “cumplir un número”.

---

## 20. Cierre futuro de `PLAYBOOK_GUION_ADAPTACION_CV`

Cuando se diseñe esta fase deberá crearse también su criterio de validación antes de declararla cerrada.

Como mínimo deberá demostrar que:

* consume correctamente análisis y candidatura;
* no vuelve a realizar el análisis;
* convierte estrategia en instrucciones operativas;
* selecciona evidencias;
* conserva límites;
* no redacta prematuramente los textos finales;
* produce una salida suficiente para alimentar la fase de contenido.

Los criterios definitivos se fijarán durante su diseño.

---

# PARTE IV — APRENDIZAJE Y RETROALIMENTACIÓN

## 21. Clasificación de defectos encontrados

Toda prueba debe clasificar cada problema detectado.

Categorías:

```text
CASO
PLAYBOOK
TEMPLATE
DATOS_CORE
ARQUITECTURA
COMPOSICION
```

### CASO

Problema particular de una candidatura.

No requiere necesariamente cambios normativos.

### PLAYBOOK

Problema en reglas, razonamiento o contrato de la fase.

Debe revisarse el playbook.

### TEMPLATE

Problema de estructura documental.

Debe revisarse el template.

### DATOS_CORE

La fase necesita información factual que no está disponible o está mal estructurada.

Debe estudiarse su incorporación o tratamiento.

### ARQUITECTURA

El problema demuestra que las responsabilidades o límites entre fases son incorrectos.

Debe revisarse este SPEC.

### COMPOSICION

Problema técnico de generación o formato.

Pertenece a templates visuales o código.

---

## 22. Aprendizaje entre candidaturas

Las candidaturas no deben ser islas independientes.

Cuando una misma incidencia aparezca en varios casos, debe evaluarse si revela un patrón.

Ejemplos:

* carencia factual repetida;
* ambigüedad frecuente;
* campo necesario no previsto;
* riesgo recurrente;
* regla mal definida;
* dato core sistemáticamente insuficiente.

Regla:

> Un caso descubre el problema. La repetición puede revelar una necesidad estructural.

No se actualiza automáticamente un documento normativo por una incidencia aislada.

Debe evaluarse primero su generalidad.

---

## 23. Retroalimentación hacia documentos superiores

Cuando una prueba revele un problema generalizable, debe decidirse qué documento es autoridad para resolverlo.

Ejemplos:

```text
hecho profesional faltante
→ datos-core-busqueda.md

regla de análisis
→ PLAYBOOK_ANALISIS_OFERTA

regla de candidatura
→ PLAYBOOK_CANDIDATURA

estructura de ficha
→ TEMPLATE_CANDIDATURA

límite entre fases
→ este SPEC
```

Esto evita introducir la misma corrección en varios lugares sin fuente clara.

---

# PARTE V — REGLAS TRANSVERSALES

## 24. Reglas factuales comunes

Las siguientes reglas afectan transversalmente a todas las fases.

### No invención

No atribuir información profesional no acreditada.

### Formación no equivale a experiencia

La formación o actualización no debe presentarse como experiencia profesional.

### Automatización no equivale a IA

Algoritmos, automatización, programación, integraciones o análisis de datos no deben convertirse automáticamente en experiencia profesional en Inteligencia Artificial.

### Inferencia no equivale a hecho

Una interpretación debe mantenerse diferenciada de información factual.

### Tecnología transferible no equivale a experiencia literal

El encaje funcional con una necesidad no permite afirmar dominio de una tecnología no acreditada.

Este SPEC declara estas reglas como principios transversales.

Los playbooks pueden desarrollarlas de forma específica, pero no contradecirlas sin modificar previamente la arquitectura o justificar expresamente la excepción.

---

## 25. Fuente única y repetición de reglas

No es necesario eliminar inmediatamente reglas repetidas en los playbooks existentes.

Durante la transición se admite redundancia si ayuda a la seguridad.

Sin embargo:

> las reglas transversales deben interpretarse conforme a este SPEC y las reglas específicas conforme al playbook de cada fase.

Si una regla transversal cambia, deberá comprobarse qué playbooks afectados necesitan actualización.

---

# PARTE VI — NOMENCLATURA Y TRAZABILIDAD

## 26. Identificador de candidatura

Cada candidatura debe mantener un identificador estable:

```text
CAND-AAAA-NNN
```

Todos sus artefactos deben poder relacionarse inequívocamente con ese ID.

---

## 27. Convención de artefactos

Debe evitarse depender de variaciones arbitrarias de mayúsculas, sufijos o versiones en nombres finales.

Principio:

> El identificador de candidatura es la clave lógica; el nombre de archivo es una representación.

La convención definitiva de nombres debe revisarse antes de escalar la nueva arquitectura a producción.

No se crea por ahora un nuevo índice maestro si `seguimiento-candidaturas.md` y `candidatura.md` pueden cubrir esa función.

Primero debe comprobarse si existe una necesidad real adicional.

---

# PARTE VII — ORDEN DE TRABAJO

## 28. Prioridad actual

El trabajo actual no está en:

```text
datos-generacion.json
```

ni en:

```text
generar_candidatura.py
```

ni en:

```text
PLAYBOOK_ANALISIS_EMPRESA_OBJETIVO
```

La fase actual es:

```text
PLAYBOOK_CANDIDATURA
→ candidatura.md
```

Objetivo inmediato:

> determinar si esta fase puede declararse validada.

---

## 29. Secuencia de trabajo vigente

Orden:

```text
1. Validar PLAYBOOK_CANDIDATURA
2. Validar TEMPLATE_CANDIDATURA_v2
3. Revisar candidatura CAND-2026-019 contra criterios explícitos
4. Registrar defectos
5. Clasificar defectos
6. Corregir problemas generalizables
7. Decidir si hace falta segundo caso
8. Declarar la fase validada o mantenerla en prueba
9. Diseñar PLAYBOOK_GUION_ADAPTACION_CV
10. Diseñar su template si procede
11. Definir sus criterios de cierre
12. Probarlo
13. Solo después pasar a generación de contenido
```

---

## 30. Regla de avance

Una fase siguiente puede discutirse conceptualmente.

No debe diseñarse en profundidad ni implementarse hasta que sus entradas sean suficientemente estables.

Regla:

> Arquitectura futura puede anticiparse.
> Diseño operativo debe respetar el orden de maduración.

---

# PARTE VIII — SKILL DIRECTORA

## 31. Papel futuro

La skill principal de `job-up` deberá convertirse en directora de orquesta.

Responsabilidades previstas:

1. identificar origen;
2. activar análisis correspondiente;
3. generar o actualizar candidatura;
4. activar adaptación;
5. activar generación de contenido;
6. activar composición;
7. activar veredicto;
8. actualizar estados;
9. detenerse en puntos de aprobación humana.

La skill directora:

* coordina;
* comprueba precondiciones;
* transmite artefactos;
* controla estados.

No debe absorber internamente toda la lógica de los playbooks.

---

## 32. Estado actual de la skill directora

Todavía no debe considerarse definida en su forma final.

Faltan fases esenciales:

* validación de candidatura;
* guion de adaptación;
* generación estructurada de contenido.

Su arquitectura se mantiene como objetivo, no como tarea inmediata.

---

# PARTE IX — CONTINUIDAD ENTRE SESIONES

## 33. Rehidratación mínima obligatoria

Una futura sesión sobre esta línea debe recuperar:

```text
host: carrera-ai
rama: job-up
SPEC vigente
estado-actual.md
sesión PCS vigente
fase actual de maduración
último artefacto probado
criterio de cierre pendiente
```

---

## 34. Preguntas obligatorias al retomar

La sesión debe poder responder:

1. ¿Qué fase está activa?
2. ¿En qué estado de maduración está?
3. ¿Qué artefacto se está validando?
4. ¿Qué criterios de cierre quedan pendientes?
5. ¿Qué defectos están abiertos?
6. ¿Cuál es la siguiente fase permitida?
7. ¿Qué decisiones arquitectónicas no deben reabrirse sin motivo?

---

## 35. Cierre de una sesión de trabajo

Antes de finalizar un bloque debe quedar registrado:

* fase trabajada;
* estado anterior;
* estado resultante;
* pruebas realizadas;
* defectos encontrados;
* defectos resueltos;
* decisiones tomadas;
* documentos afectados;
* criterios pendientes;
* siguiente acción recomendada.

Esto puede registrarse en la sesión PCS correspondiente.

El SPEC solo debe modificarse cuando cambie algo estructural o el estado consolidado de maduración.

---

# PARTE X — DECISIONES ARQUITECTÓNICAS

## 36. Registro vigente

### ARQ-01 — Arquitectura modular

La candidatura se divide en fases especializadas.

Estado: vigente.

---

### ARQ-02 — Separación entre análisis y redacción

El análisis no redacta documentos finales.

Estado: vigente.

---

### ARQ-03 — `candidatura.md` como ficha viva

Gobierna el ciclo de vida y no sustituye otros artefactos.

Estado: en validación.

---

### ARQ-04 — Dos puertas de entrada

Se pretende soportar:

* oferta;
* empresa objetivo.

Estado: vigente como arquitectura objetivo.

La convergencia completa todavía no está validada.

---

### ARQ-05 — Guion antes de contenido final

Debe existir una fase explícita de adaptación estratégica antes de redactar contenido final.

Estado: vigente.

---

### ARQ-06 — Redacción única

CV, carta y LaTeX deben derivar de una única generación estructurada de contenido.

Estado: arquitectura objetivo.

---

### ARQ-07 — JSON como frontera

`datos-generacion.json` será la frontera futura entre redacción y composición.

Estado: arquitectura objetivo; contrato todavía no diseñado.

---

### ARQ-08 — Composición determinista

El compositor no analiza ni redacta.

Estado: arquitectura objetivo.

---

### ARQ-09 — Corrección por capa

Contenido y composición se corrigen en capas distintas.

Estado: arquitectura objetivo.

---

### ARQ-10 — No saltar fases

No se diseña operativamente una fase dependiente mientras sus entradas principales sigan inestables.

Estado: vigente.

---

### ARQ-11 — Cierre verificable

Una fase no se considera validada por intuición; debe superar criterios explícitos.

Estado: vigente.

---

### ARQ-12 — Aprendizaje transversal

Las pruebas de candidaturas deben poder producir mejoras en playbooks, templates, datos core o arquitectura cuando el problema sea generalizable.

Estado: vigente.

---

# PARTE XI — ARTEFACTOS

## 37. Existentes

```text
PLAYBOOK_ANALISIS_OFERTA.md
TEMPLATE_ANALISIS_OFERTA_v2.md
analisis-oferta-cand-2026-019.md

PLAYBOOK_CANDIDATURA.md
TEMPLATE_CANDIDATURA_v2.md
candidatura_CAND-2026-019_v2.md
```

---

## 38. Pendientes

```text
PLAYBOOK_GUION_ADAPTACION_CV.md
TEMPLATE_GUION_ADAPTACION_CV.md, si resulta necesario

PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA.md
datos-generacion.json
schema/template del JSON

adaptación de generar_candidatura.py
adaptación del veredicto

PLAYBOOK_ANALISIS_EMPRESA_OBJETIVO.md
artefacto/template correspondiente

playbook de preparación de entrevista
```

No todos estos artefactos son tareas próximas.

---

# PARTE XII — RIESGOS

## 39. Riesgos principales

### R1 — Volver al monolito

Mezclar todas las fases en una skill.

### R2 — Saltar fases

Diseñar una fase antes de estabilizar sus entradas.

### R3 — Confundir arquitectura objetivo con implantación real

Dar por existente algo que solo está previsto.

### R4 — Redacción duplicada

Redactar CV, carta y LaTeX independientemente.

### R5 — Parcheo de documentos finales

Modificar contenido directamente en DOCX/PDF.

### R6 — Duplicar fuentes de verdad

Crear índices o registros innecesarios.

### R7 — Deriva de nomenclatura

Perder relación inequívoca entre candidatura y artefactos.

### R8 — Pérdida de decisiones

No actualizar SPEC o sesión PCS cuando se adopta una decisión relevante.

### R9 — Caso único convertido en regla

Generalizar una solución a partir de una sola candidatura sin evaluarla.

### R10 — Sobre-especificar fases futuras

Diseñar en detalle JSON, composición o veredicto mientras la fase actual sigue abierta.

---

# PARTE XIII — PRÓXIMO TRABAJO

## 40. Objetivo inmediato

No crear todavía un nuevo playbook.

Primero:

> validar o refutar que `PLAYBOOK_CANDIDATURA + TEMPLATE_CANDIDATURA_v2` producen una ficha adecuada.

Caso inicial:

```text
CAND-2026-019
```

---

## 41. Procedimiento inmediato

1. Leer `PLAYBOOK_CANDIDATURA.md`.
2. Leer `TEMPLATE_CANDIDATURA_v2.md`.
3. Leer `candidatura_CAND-2026-019_v2.md`.
4. Aplicar los criterios de cierre de este SPEC.
5. Registrar cualquier defecto.
6. Clasificar cada defecto.
7. Determinar cuáles son particulares y cuáles generalizables.
8. Corregir playbook/template si procede.
9. Repetir la prueba.
10. Decidir si CAND-2026-019 es suficiente.
11. Si no lo es, seleccionar un segundo caso que aporte contraste real.
12. Declarar la fase:

* `validada`; o
* `en_prueba`.

Solo después:

```text
PLAYBOOK_GUION_ADAPTACION_CV
```

---

# 42. Resumen ejecutivo

La arquitectura objetivo de `job-up` es:

```text
análisis de oportunidad
→ candidatura.md
→ guion-adaptacion-cv.md
→ datos-generacion.json
→ composición determinista
→ documentos finales
→ veredicto
→ entrevista si procede
```

Pero esa arquitectura objetivo no describe el estado real de implantación.

El punto actual es:

```text
PLAYBOOK_ANALISIS_OFERTA
→ avanzado

PLAYBOOK_CANDIDATURA
→ diseñado
→ EN PRUEBA

PLAYBOOK_GUION_ADAPTACION_CV
→ siguiente fase

resto
→ arquitectura futura
```

La prioridad actual no es avanzar.

Es demostrar que la fase actual puede cerrarse con criterios verificables.

La siguiente transición permitida es:

```text
candidatura.md validada
→ diseñar PLAYBOOK_GUION_ADAPTACION_CV
```

No:

```text
candidatura.md todavía incierta
→ diseñar datos-generacion.json
```

La regla operativa principal de esta versión del SPEC es:

> No avanzar por intuición.
> Cada fase debe tener criterios explícitos de cierre y evidencias suficientes para declararla validada.

Y la regla arquitectónica de largo plazo permanece:

> El contenido se corrige en la capa de contenido.
> La maquetación se corrige en la capa de composición.

---

## Changelog

### 0.2.0 — 2026-08-02

* Se separa arquitectura objetivo de estado real de implantación.
* Se introducen estados de maduración por fase.
* Se añaden criterios explícitos de cierre.
* Se fija `candidatura.md` como fase actual en validación.
* Se evita asumir que CAND-2026-019 basta por sí sola.
* Se rebaja la convergencia de empresa objetivo a hipótesis pendiente de validar.
* Se introduce gobernanza y versionado del SPEC.
* Se diferencia `ARQ-*` de decisiones PCS.
* Se define la relación entre SPEC, PCS, estado y sesiones.
* Se incorpora aprendizaje entre candidaturas.
* Se incorpora clasificación de defectos.
* Se añade lista no contractual de necesidades futuras del JSON.
* Se reduce el compromiso prematuro sobre fases futuras.
* Se establece como siguiente trabajo la validación formal de `candidatura.md`.
