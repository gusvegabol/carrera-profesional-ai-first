---
id: spec-arquitectura-generacion-candidaturas-job-up
titulo: SPEC — Arquitectura modular para generación de candidaturas en Job-up
version: "0.2.5"
estado: borrador_operativo
fecha_version: 2026-08-04
host: carrera-ai
rama: job-up
origen_historico: sesion-20260801-2040-job-up
sustituye: "0.2.0"
---
# SPEC — Arquitectura modular para generación de candidaturas en Job-up

## 1. Propósito

Este documento fija la arquitectura objetivo, el estado real de implantación y el orden de trabajo para rediseñar la generación de candidaturas dentro de `job-up`.

Su finalidad principal es impedir que futuras sesiones de trabajo:

- pierdan decisiones ya tomadas;
- vuelvan a diseñar desde cero partes ya acordadas;
- mezclen análisis, estrategia, redacción y composición documental;
- avancen a una fase sin haber validado la anterior;
- confundan arquitectura futura con funcionalidad ya implementada;
- introduzcan cambios sin dejar trazabilidad;
- utilicen vocabularios de estado ambiguos o contradictorios.

Este SPEC debe actuar como fuente estable de continuidad para esta línea concreta de `job-up`.

No sustituye:

- `estado-actual.md`;
- las sesiones PCS;
- `AGENTS.md`;
- los playbooks específicos;
- los datos core;
- `seguimiento-candidaturas.md`;
- los artefactos concretos de cada candidatura.

---

## 2. Autoridad y relación con PCS

Este SPEC conserva:

- la arquitectura;
- las decisiones de diseño;
- el orden de maduración;
- el estado consolidado de las fases.

La relación entre fuentes queda así:

```text
SPEC
→ arquitectura, decisiones y maduración de esta línea

.pcs/estado/estado-actual.md
→ estado operativo vigente del host

sesión PCS vigente
→ bloque concreto de trabajo actual

AGENTS.md
→ reglas de operación del host

playbooks
→ comportamiento normativo de cada fase

seguimiento-candidaturas.md
→ visión transversal del estado de candidaturas

artefactos de candidatura
→ contenido y estado del caso individual
```

La referencia:

```text
sesion-20260801-2040-job-up
```

es únicamente el origen histórico de esta versión del SPEC.

No debe asumirse que seguirá siendo siempre la sesión PCS activa.

Cuando una futura sesión continúe esta línea:

1. debe leer el SPEC vigente;
2. debe consultar `estado-actual.md`;
3. debe identificar la sesión PCS activa;
4. debe registrar en esa sesión las respuestas de rehidratación;
5. no debe modificar este SPEC solo porque haya cambiado la sesión PCS.

---

## 3. Gobernanza del SPEC

### 3.1 Versionado

El documento usa versionado incremental.

Ejemplo:

```text
0.1.0 → primera arquitectura consolidada
0.2.0 → criterios de cierre y gobernanza
0.2.5 → armonización de estados, responsabilidades y pruebas
0.3.0 → cambio arquitectónico relevante
1.0.0 → arquitectura validada como base operativa
```

### 3.2 Estados del SPEC

Estados permitidos:

- `borrador_operativo`;
- `en_validacion`;
- `vigente`;
- `sustituido`.

### 3.3 Sustitución de versiones

Solo una versión debe actuar como referencia actual.

Cuando una versión sea sustituida debe:

- pasar a `estado: sustituido`;
- indicar `sustituida_por`;
- conservarse por trazabilidad;
- dejar inequívoco que ya no es vigente.

No deben coexistir dos SPEC aparentemente actuales en la misma carpeta.

### 3.4 Decisiones arquitectónicas

Las decisiones de este documento se identifican como:

```text
ARQ-XX
```

para diferenciarlas de decisiones PCS formales.

Estados permitidos para una decisión `ARQ`:

- `vigente`;
- `sustituida`;
- `retirada`.

Si cambia una decisión:

```text
ARQ-XX
estado: sustituida
sustituida_por: ARQ-YY
motivo: ...
```

No se elimina silenciosamente una decisión anterior.

---

## 4. Glosario de estados

Este SPEC maneja varios ejes de estado distintos.

No deben mezclarse.

| Eje | Estados permitidos | Significado |
| --- | --- | --- |
| SPEC | `borrador_operativo`, `en_validacion`, `vigente`, `sustituido` | Madurez del propio SPEC |
| Decisión ARQ | `vigente`, `sustituida`, `retirada` | Vigencia de una decisión arquitectónica |
| Fase | `pendiente`, `diseñada`, `en_prueba`, `validada` | Madurez de una fase |
| Candidatura | definidos por `PLAYBOOK_CANDIDATURA` | Estado operativo de un caso concreto |

Regla:

> Un estado de un eje no puede utilizarse como sinónimo de otro.

Ejemplo:

```text
PLAYBOOK_CANDIDATURA
estado_fase: en_prueba
```

no equivale a:

```text
candidatura CAND-2026-019
estado: pendiente_de_aprobacion
```

---

## 5. Responsabilidad de decisión

En el estado actual del proyecto existe una persona responsable del proyecto.

Le corresponde decidir:

- cuándo una fase pasa a `validada`;
- si hace falta un segundo caso de prueba;
- si un defecto es suficientemente generalizable;
- si una propuesta modifica arquitectura;
- si una decisión `ARQ` se adopta o sustituye;
- si puede avanzarse a la siguiente fase.

La IA puede:

- analizar;
- auditar;
- clasificar;
- proponer;
- señalar inconsistencias;
- recomendar cierre o continuación.

La IA no debe declarar autónomamente una fase como `validada` sin aprobación explícita de la persona responsable.

---

# PARTE I — ARQUITECTURA OBJETIVO

## 6. Principio arquitectónico central

La generación de una candidatura se divide conceptualmente en dos mundos.

### Mundo IA

Incluye:

- análisis;
- interpretación;
- estrategia;
- selección;
- redacción.

### Mundo técnico

Incluye:

- materialización;
- composición;
- conversión;
- formato;
- validación técnica.

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

## 7. Dos puertas de entrada

La arquitectura prevé dos formas de iniciar una candidatura.

### 7.1 Por oferta

```text
oferta
→ PLAYBOOK_ANALISIS_OFERTA
→ analisis-oferta.md
```

Este flujo parte de una oportunidad explícita.

El análisis debe determinar:

- contenido factual de la oferta;
- empresa publicadora;
- empresa contratante cuando sea identificable;
- requisitos;
- prioridades;
- posible problema empresarial;
- encaje factual;
- carencias;
- riesgos;
- argumento competitivo;
- decisión estratégica.

No debe redactar documentos finales.

---

### 7.2 Por empresa objetivo

Arquitectura prevista:

```text
empresa objetivo
→ futuro PLAYBOOK_ANALISIS_EMPRESA_OBJETIVO
→ artefacto de análisis
```

Su finalidad será permitir presentación espontánea o candidatura sin oferta explícita.

Debe analizar:

- actividad;
- contexto;
- posibles necesidades;
- áreas donde el perfil pueda aportar;
- encaje;
- riesgos;
- argumento de aproximación;
- límites factuales.

### Hipótesis pendiente de validar

La arquitectura pretende que esta vía converja posteriormente en:

```text
PLAYBOOK_CANDIDATURA
→ candidatura.md
```

Esta convergencia no está validada.

Antes de darla por definitiva deberá comprobarse que la ficha funciona cuando no existen requisitos explícitos de una oferta.

---

## 8. Ficha común de candidatura

Arquitectura prevista:

```text
análisis de oportunidad
→ PLAYBOOK_CANDIDATURA
→ candidatura.md
```

`candidatura.md` es la ficha viva de la candidatura.

Debe gobernar:

- identidad;
- origen;
- decisión estratégica;
- posicionamiento;
- evidencias prioritarias;
- límites;
- advertencias;
- datos pendientes;
- bloqueos;
- estado;
- artefactos;
- siguiente fase.

No debe:

- rehacer el análisis;
- redactar CV;
- redactar carta;
- producir el guion;
- sustituir el veredicto.

Debe distinguir:

```text
decisión estratégica
≠
estado operativo
```

---

## 9. Adaptación estratégica

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

Debe decidir:

- relato;
- experiencias prioritarias;
- evidencias;
- elementos a omitir;
- tono;
- riesgos;
- límites;
- tratamiento de carencias;
- foco del CV;
- relación estratégica con la carta.

No debe redactar todavía los textos finales.

---

## 10. Generación única de contenido

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

La decisión arquitectónica es:

> CV, carta y LaTeX no deben convertirse en procesos independientes de redacción.

La redacción debe realizarse una sola vez.

---

## 11. Registro de necesidades futuras de `datos-generacion.json`

No debe diseñarse todavía su schema definitivo.

Durante las pruebas de fases anteriores pueden detectarse necesidades futuras.

Cada necesidad debe registrarse con este formato mínimo:

```text
ID: JSON-NEC-NNN
fase_origen:
caso_origen:
fecha:
necesidad:
motivo:
impacto_previsible:
estado: candidata
```

Ejemplo conceptual:

```text
ID: JSON-NEC-001
fase_origen: PLAYBOOK_GUION_ADAPTACION_CV
caso_origen: CAND-XXXX
necesidad: distinguir evidencias destinadas a CV y carta
motivo: ambas piezas pueden necesitar énfasis distintos
impacto_previsible: estructura futura del JSON
estado: candidata
```

Estas entradas:

- no definen todavía campos del JSON;
- no constituyen contrato;
- sirven para acumular requisitos reales descubiertos durante las pruebas.

---

## 12. Composición documental

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

- no analiza;
- no selecciona estrategia;
- no redacta;
- no corrige semántica;
- no inventa;
- no cambia hechos;
- no modifica silenciosamente contenido.

---

## 13. Veredicto

Arquitectura futura:

```text
documentos finales
→ playbook de veredicto
→ veredicto-final-cv.md
```

El veredicto deberá evaluar:

- integridad factual;
- privacidad;
- coherencia;
- calidad;
- adecuación;
- riesgos;
- posibles defectos.

Los criterios, severidades y umbrales se definirán cuando esta fase pase a diseño.

No se fijan en este SPEC porque todavía no corresponde diseñarla.

Principio futuro:

> El veredicto no parchea directamente un DOCX.

Un defecto de contenido retorna a la capa de contenido.

Un defecto de composición retorna a la capa técnica.

---

## 14. Preparación de entrevista

Fase posterior y condicional.

Arquitectura prevista:

```text
candidatura preparada o enviada
→ playbook específico
→ informe de entrevista
```

No forma parte del núcleo inmediato de rediseño.

---

## 15. Arquitectura objetivo completa

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

La convergencia de esta segunda vía sigue siendo una hipótesis pendiente de validación.

---

# PARTE II — ESTADO REAL DE IMPLANTACIÓN

## 16. Estado canónico de cada fase

Solo se utilizan los estados:

```text
pendiente
diseñada
en_prueba
validada
```

| Fase | Estado |
| --- | --- |
| `PLAYBOOK_ANALISIS_OFERTA` | `en_prueba` |
| `TEMPLATE_ANALISIS_OFERTA_v2` | `en_prueba` |
| ejecución de `analisis-oferta.md` | `en_prueba` |
| `PLAYBOOK_CANDIDATURA` | `en_prueba` |
| `TEMPLATE_CANDIDATURA_v2` | `en_prueba` |
| ejecución de `candidatura.md` | `en_prueba` |
| `PLAYBOOK_GUION_ADAPTACION_CV` | `pendiente` |
| template de guion | `pendiente` |
| ejecución de guion | `pendiente` |
| `PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA` | `pendiente` |
| `datos-generacion.json` | `pendiente` |
| adaptación de `generar_candidatura.py` | `pendiente` |
| adaptación del veredicto | `pendiente` |
| análisis empresa objetivo | `pendiente` |
| preparación entrevista | `pendiente` |

---

## 17. Significado de los estados de fase

### `pendiente`

No existe todavía un diseño suficiente.

### `diseñada`

Existe:

- playbook;
- contrato;
- template si procede;
- criterios de prueba.

Pero todavía no ha demostrado funcionamiento suficiente.

### `en_prueba`

La fase se ejecuta sobre casos reales o controlados.

Se registran:

- defectos;
- ambigüedades;
- fricciones;
- cambios necesarios.

### `validada`

La fase ha superado sus criterios explícitos de cierre y la persona responsable ha aprobado su cierre.

---

# PARTE III — CRITERIOS DE CIERRE

## 18. Regla general de cierre

Ninguna fase se declara validada únicamente porque:

- exista un documento;
- produzca una salida;
- una ejecución no dé error;
- un caso parezca correcto.

Una fase se valida cuando:

1. existe contrato claro;
2. existe prueba relevante;
3. se han ejecutado sus controles;
4. los defectos detectados se han resuelto o documentado;
5. no existen bloqueos estructurales conocidos;
6. puede alimentar la fase siguiente sin obligarla a reconstruir decisiones anteriores;
7. la persona responsable aprueba explícitamente el cierre.

---

## 19. Criterios de cierre de `candidatura.md`

La fase actual es:

```text
PLAYBOOK_CANDIDATURA
→ candidatura.md
```

Estado:

```text
en_prueba
```

Debe comprobarse:

### Responsabilidad

- [ ] `candidatura.md` gobierna el ciclo de vida.
- [ ] No repite el análisis completo.
- [ ] No redacta documentos posteriores.
- [ ] No vuelve a decidir silenciosamente el encaje.

### Trazabilidad

- [ ] El origen está identificado.
- [ ] El artefacto de análisis está identificado.
- [ ] La decisión estratégica procede del análisis.
- [ ] Las evidencias mantienen trazabilidad.
- [ ] Las afirmaciones excluidas mantienen su origen.

### Estado

- [ ] Decisión estratégica y estado operativo son independientes.
- [ ] `presentada` representa un hecho real.
- [ ] Los bloqueos afectan correctamente al estado.
- [ ] La siguiente fase está identificada.

### Economía documental

- [ ] No replica matrices o razonamientos completos del análisis.
- [ ] No duplica contenido de fases posteriores.
- [ ] Mantiene suficiente información para gobernar sin reconstruir toda la oportunidad.

### Artefactos

- [ ] El inventario representa documentos reales o previstos.
- [ ] Los estados son coherentes.
- [ ] Los enlaces existentes funcionan.

### Prueba actual

- [ ] `CAND-2026-019` ha sido revisada completamente contra este contrato.
- [ ] Los defectos encontrados han sido clasificados.
- [ ] Las correcciones generalizables se han aplicado.
- [ ] No quedan defectos estructurales conocidos.

---

## 20. Matriz mínima de cobertura antes de cerrar `candidatura.md`

`CAND-2026-019` no debe considerarse automáticamente suficiente.

Antes de validar la fase debe comprobarse qué dimensiones estructurales ha cubierto.

| Dimensión | Caso actual cubierto | ¿Necesita contraste? |
| --- | --- | --- |
| Origen por oferta | sí | no por sí sola |
| Empresa publicadora ≠ contratante | sí | puede requerirse oferta directa |
| Decisión `preparar_con_advertencias` | sí | puede requerirse otra decisión |
| Bloqueos activos | no | revisar necesidad |
| Estado `detenida` | no | revisar necesidad |
| Puesto tecnológico/directivo | sí | puede requerirse otro tipo de puesto |
| Advertencias relevantes | sí | cubierto parcialmente |
| Datos pendientes | sí | cubierto parcialmente |
| Artefactos posteriores existentes | sí | cubierto |
| Presentada `false` | sí | no prueba transición a enviada |

Después de la evaluación se elige explícitamente:

```text
A. CAND-2026-019 ofrece cobertura suficiente
B. Hace falta un segundo caso por oferta
C. Hace falta otro tipo de prueba antes de validar completamente
```

La elección debe justificarse por dimensiones de cobertura, no por comodidad.

---

## 21. Criterios futuros para `PLAYBOOK_GUION_ADAPTACION_CV`

Cuando se diseñe esta fase, deberán fijarse criterios explícitos antes de probarla.

Como mínimo deberá demostrar que:

- consume correctamente análisis y candidatura;
- no repite el análisis;
- convierte estrategia en instrucciones operativas;
- selecciona evidencias;
- conserva límites;
- no redacta prematuramente textos finales;
- produce una salida suficiente para alimentar la futura fase de contenido.

---

# PARTE IV — APRENDIZAJE Y RETROALIMENTACIÓN

## 22. Clasificación de defectos

Toda prueba debe clasificar cada problema.

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

### PLAYBOOK

Problema de reglas, razonamiento o contrato.

### TEMPLATE

Problema de estructura documental.

### DATOS_CORE

La fase necesita información factual inexistente o mal estructurada.

### ARQUITECTURA

El problema revela una mala separación de responsabilidades o fases.

### COMPOSICION

Problema técnico de generación o formato.

---

## 23. Resolución de clasificación dudosa

La IA puede proponer una clasificación.

Si existen dudas entre:

```text
CASO vs PLAYBOOK
PLAYBOOK vs ARQUITECTURA
TEMPLATE vs ARQUITECTURA
DATOS_CORE vs CASO
```

la clasificación final corresponde a la persona responsable.

La decisión debe registrarse en la sesión PCS de trabajo cuando tenga impacto generalizable.

---

## 24. Aprendizaje entre candidaturas

Las candidaturas no deben ser islas independientes.

Cuando una incidencia aparezca en varios casos debe evaluarse si revela un patrón.

Ejemplos:

- carencia factual repetida;
- ambigüedad frecuente;
- campo necesario no previsto;
- riesgo recurrente;
- dato core insuficiente;
- límite de arquitectura.

Regla:

> Un caso descubre un problema. La repetición puede demostrar una necesidad estructural.

No se modifica automáticamente un documento normativo por una incidencia aislada.

---

## 25. Retroalimentación hacia documentos de autoridad

Cuando un problema sea generalizable:

```text
hecho profesional faltante
→ datos-core-busqueda.md

regla de análisis
→ PLAYBOOK_ANALISIS_OFERTA

regla de candidatura
→ PLAYBOOK_CANDIDATURA

estructura de ficha
→ TEMPLATE_CANDIDATURA_v2

límite entre fases
→ este SPEC

problema transversal de seguimiento
→ seguimiento-candidaturas.md o gobernanza correspondiente
```

---

# PARTE V — REGLAS TRANSVERSALES

## 26. Principios factuales comunes

### No invención

No atribuir información profesional no acreditada.

### Formación no equivale a experiencia

La formación o actualización no debe presentarse como experiencia profesional.

### Automatización no equivale a IA

Algoritmos, automatización, programación, integraciones o análisis de datos no deben convertirse automáticamente en experiencia profesional en IA.

### Inferencia no equivale a hecho

Una interpretación debe mantenerse diferenciada de información factual.

### Tecnología transferible no equivale a experiencia literal

El encaje funcional no permite afirmar dominio de una tecnología no acreditada.

---

## 27. Redundancia temporal de reglas

Durante la transición se admite que estas reglas aparezcan también en playbooks concretos.

La redundancia debe revisarse cuando ocurra cualquiera de estos disparadores:

1. una regla transversal necesite modificarse;
2. existan versiones divergentes en dos documentos;
3. una misma modificación deba aplicarse manualmente a más de un playbook;
4. la duplicación empiece a generar inconsistencias.

En ese momento deberá decidirse una fuente normativa única o una estrategia explícita de herencia.

---

# PARTE VI — NOMENCLATURA Y TRAZABILIDAD

## 28. Identificador de candidatura

Cada candidatura mantiene un ID estable:

```text
CAND-AAAA-NNN
```

Todos sus artefactos deben poder relacionarse inequívocamente con ese identificador.

---

## 29. Seguimiento transversal

Existe:

```text
seguimiento-candidaturas.md
```

Su función es ofrecer visión transversal del estado de las candidaturas.

No sustituye:

```text
candidatura.md
```

que gobierna el caso individual.

Por ahora no se crea un nuevo índice maestro.

Solo deberá reconsiderarse si ambos documentos dejan de cubrir adecuadamente la trazabilidad.

---

## 30. Convención de nombres

Debe evitarse depender de variaciones arbitrarias de:

- mayúsculas;
- minúsculas;
- sufijos;
- versiones;
- nombres inconsistentes.

Principio:

> El ID de candidatura es la clave lógica; el nombre de archivo es una representación.

La convención definitiva de nombres deberá fijarse antes de escalar ampliamente el nuevo flujo.

---

# PARTE VII — ORDEN DE TRABAJO

## 31. Prioridad actual

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

Objetivo:

> determinar si puede declararse `validada`.

---

## 32. Secuencia vigente

```text
1. Revisar PLAYBOOK_CANDIDATURA
2. Revisar TEMPLATE_CANDIDATURA_v2
3. Auditar candidatura_CAND-2026-019_v2
4. Aplicar criterios de cierre
5. Registrar defectos
6. Clasificar defectos
7. Resolver los generalizables
8. Repetir la prueba
9. Evaluar matriz de cobertura
10. Decidir A / B / C
11. Obtener aprobación humana del cierre
12. Si se valida, diseñar PLAYBOOK_GUION_ADAPTACION_CV
```

---

## 33. Regla de avance

Una fase siguiente puede discutirse conceptualmente.

No debe diseñarse en profundidad ni implementarse hasta que sus entradas sean suficientemente estables.

Regla:

> Arquitectura futura puede anticiparse.  
> Diseño operativo debe respetar el orden de maduración.

---

# PARTE VIII — SKILL DIRECTORA

## 34. Papel futuro

La skill principal de `job-up` deberá actuar como directora de orquesta.

Responsabilidades previstas:

1. identificar origen;
2. activar análisis;
3. generar o actualizar candidatura;
4. activar adaptación;
5. activar generación de contenido;
6. activar composición;
7. activar veredicto;
8. actualizar estados;
9. detenerse ante decisiones que requieran aprobación humana.

La skill directora:

- coordina;
- comprueba precondiciones;
- transmite artefactos;
- controla estados.

No debe absorber toda la lógica de los playbooks.

---

## 35. Límite de autonomía

La futura skill directora no podrá decidir autónomamente:

- que una fase metodológica queda validada;
- que una decisión ARQ cambia;
- que una carencia factual puede ignorarse;
- que una candidatura debe enviarse;
- que un dato privado puede utilizarse sin autorización.

Estas decisiones requieren la gobernanza correspondiente y, cuando proceda, aprobación humana explícita.

---

# PARTE IX — CONTINUIDAD ENTRE SESIONES

## 36. Rehidratación mínima obligatoria

Una futura sesión debe recuperar:

```text
host: carrera-ai
rama: job-up
SPEC vigente
estado-actual.md
sesión PCS vigente
fase actual
estado de fase
último artefacto probado
defectos abiertos
criterio de cierre pendiente
```

---

## 37. Preguntas obligatorias al retomar

La sesión debe poder responder:

1. ¿Qué fase está activa?
2. ¿Cuál es su estado canónico?
3. ¿Qué artefacto se está probando?
4. ¿Qué criterios faltan?
5. ¿Qué defectos siguen abiertos?
6. ¿Qué decisiones ARQ siguen vigentes?
7. ¿Cuál es la siguiente fase permitida?
8. ¿Se ha modificado el estado desde la sesión anterior?

---

## 38. Registro de esas respuestas

Las respuestas de rehidratación deben quedar registradas en la sesión PCS correspondiente cuando sean relevantes para continuidad.

Como mínimo:

```text
fase_actual:
estado_fase:
artefacto_en_prueba:
defectos_abiertos:
criterios_pendientes:
siguiente_paso:
```

No es necesario modificar el SPEC por cada rehidratación.

---

## 39. Cierre de una sesión de trabajo

Antes de finalizar un bloque debe quedar registrado:

- fase trabajada;
- estado anterior;
- estado resultante;
- pruebas realizadas;
- defectos encontrados;
- clasificación;
- defectos resueltos;
- decisiones tomadas;
- documentos afectados;
- criterios pendientes;
- siguiente acción recomendada.

---

# PARTE X — DECISIONES ARQUITECTÓNICAS

## 40. Registro vigente

### ARQ-01 — Arquitectura modular

La candidatura se divide en fases especializadas.

Estado: `vigente`.

### ARQ-02 — Separación entre análisis y redacción

El análisis no redacta documentos finales.

Estado: `vigente`.

### ARQ-03 — `candidatura.md` como ficha viva

Gobierna el ciclo de vida y no sustituye otros artefactos.

Estado: `vigente`.

La fase que implementa esta decisión está actualmente `en_prueba`.

### ARQ-04 — Dos puertas de entrada

Se pretende soportar:

- oferta;
- empresa objetivo.

Estado: `vigente`.

La convergencia común todavía no está validada.

### ARQ-05 — Guion antes de contenido final

Debe existir una fase explícita de adaptación estratégica antes de redactar contenido final.

Estado: `vigente`.

### ARQ-06 — Redacción única

CV, carta y LaTeX deben derivar de una única generación estructurada.

Estado: `vigente`.

Su implementación todavía está `pendiente`.

### ARQ-07 — JSON como frontera

`datos-generacion.json` será la frontera entre redacción y composición.

Estado: `vigente`.

Su diseño está `pendiente`.

### ARQ-08 — Composición determinista

El compositor no analiza ni redacta.

Estado: `vigente`.

### ARQ-09 — Corrección por capa

Contenido y composición se corrigen en capas distintas.

Estado: `vigente`.

### ARQ-10 — No saltar fases

No se diseña operativamente una fase dependiente mientras sus entradas principales sigan inestables.

Estado: `vigente`.

### ARQ-11 — Cierre verificable

Una fase necesita criterios explícitos y aprobación de cierre.

Estado: `vigente`.

### ARQ-12 — Aprendizaje transversal

Los casos reales pueden producir mejoras normativas cuando el problema sea generalizable.

Estado: `vigente`.

### ARQ-13 — Responsabilidad humana de cierre

La validación final de una fase corresponde a la persona responsable.

Estado: `vigente`.

---

# PARTE XI — ARTEFACTOS

## 41. Existentes

### Arquitectura y continuidad

```text
SPEC — Arquitectura modular para generación de candidaturas en Job-up
seguimiento-candidaturas.md
```

### Análisis de oferta

```text
PLAYBOOK_ANALISIS_OFERTA.md
TEMPLATE_ANALISIS_OFERTA_v2.md
analisis-oferta-cand-2026-019.md
```

### Candidatura

```text
PLAYBOOK_CANDIDATURA.md
TEMPLATE_CANDIDATURA_v2.md
candidatura_CAND-2026-019_v2.md
```

---

## 42. Pendientes

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

No todos son trabajos próximos.

---

# PARTE XII — RIESGOS

## 43. Riesgos principales

### R1 — Volver al monolito

Mezclar todas las fases en una skill.

### R2 — Saltar fases

Diseñar una fase antes de estabilizar sus entradas.

### R3 — Confundir arquitectura objetivo con implantación

Dar por existente algo que solo está previsto.

### R4 — Redacción duplicada

Redactar CV, carta y LaTeX independientemente.

### R5 — Parcheo de documentos finales

Modificar contenido directamente en documentos compuestos.

### R6 — Duplicar fuentes de verdad

Crear índices o registros innecesarios.

### R7 — Deriva de nomenclatura

Perder relación inequívoca entre candidatura y artefactos.

### R8 — Pérdida de decisiones

No registrar cambios relevantes.

### R9 — Caso único convertido en regla

Generalizar demasiado pronto.

### R10 — Sobre-especificar fases futuras

Diseñar JSON, composición o veredicto mientras la fase actual sigue abierta.

### R11 — Ambigüedad de estados

Usar vocabularios de estado distintos para el mismo eje.

### R12 — Dos SPEC aparentemente vigentes

Mantener versiones antiguas sin marcar como sustituidas.

---

# PARTE XIII — PRÓXIMO TRABAJO

## 44. Objetivo inmediato

No crear todavía un nuevo playbook.

Primero:

> validar o refutar que `PLAYBOOK_CANDIDATURA + TEMPLATE_CANDIDATURA_v2` producen una ficha adecuada.

Caso inicial:

```text
CAND-2026-019
```

---

## 45. Procedimiento inmediato

1. Leer `PLAYBOOK_CANDIDATURA.md`.
2. Leer `TEMPLATE_CANDIDATURA_v2.md`.
3. Leer `candidatura_CAND-2026-019_v2.md`.
4. Aplicar la checklist de cierre.
5. Registrar defectos.
6. Clasificarlos.
7. Corregir los generalizables.
8. Repetir la prueba.
9. Aplicar la matriz de cobertura.
10. Decidir A, B o C.
11. Obtener decisión humana sobre cierre.
12. Si queda `validada`, pasar a:

```text
PLAYBOOK_GUION_ADAPTACION_CV
```

---

# 46. Resumen ejecutivo

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

El estado real es:

```text
PLAYBOOK_ANALISIS_OFERTA
→ en_prueba

PLAYBOOK_CANDIDATURA
→ en_prueba

PLAYBOOK_GUION_ADAPTACION_CV
→ pendiente

resto
→ pendiente
```

La prioridad actual es demostrar si la fase:

```text
PLAYBOOK_CANDIDATURA
→ candidatura.md
```

puede pasar de:

```text
en_prueba
```

a:

```text
validada
```

La transición siguiente permitida será:

```text
candidatura.md validada
→ diseñar PLAYBOOK_GUION_ADAPTACION_CV
```

No:

```text
candidatura.md todavía incierta
→ diseñar datos-generacion.json
```

Regla operativa:

> No avanzar por intuición. Cada fase necesita criterios explícitos, cobertura suficiente y aprobación humana de cierre.

Regla arquitectónica de largo plazo:

> El contenido se corrige en la capa de contenido.  
> La maquetación se corrige en la capa de composición.

---

## Changelog

### 0.2.5 — 2026-08-04

- Se unifica el vocabulario canónico de estados de fase.
- Se elimina `en validación` como estado alternativo de fase.
- Se añade glosario de ejes de estado.
- Se explicita la responsabilidad humana de cierre.
- Se incorpora matriz mínima de cobertura para decidir si hace falta un segundo caso.
- Se formaliza el registro `JSON-NEC-*` de necesidades futuras del JSON.
- Se incorpora `seguimiento-candidaturas.md` como artefacto contextual existente.
- Se establece que versiones anteriores del SPEC deben marcarse como sustituidas.
- Se define dónde registrar la rehidratación entre sesiones.
- Se incorpora disparador para resolver la redundancia temporal de reglas factuales.
- Se armoniza `ARQ-03` con el estado de fase `en_prueba`.
- Se refuerza la separación entre estado de decisión, fase, SPEC y candidatura.
- Se mantiene `candidatura.md` como fase actual y `PLAYBOOK_GUION_ADAPTACION_CV` como siguiente fase permitida.