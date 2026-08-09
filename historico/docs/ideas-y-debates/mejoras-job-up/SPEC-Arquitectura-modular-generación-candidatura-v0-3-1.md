---
id: spec-arquitectura-generacion-candidaturas-job-up
titulo: SPEC — Arquitectura modular para generación de candidaturas en Job-up
version: "0.3.1"
estado: borrador_operativo
fecha_version: 2026-08-04
host: carrera-ai
rama: job-up
origen_historico: sesion-20260801-2040-job-up
sustituye: "0.2.5"
archivo_canonico_sugerido: SPEC-Arquitectura-modular-generacion-candidatura.md
revisado_por: IA-chatGPT-GPT 5.6 Sol
---
# SPEC — Arquitectura modular para generación de candidaturas en Job-up

## 1. Propósito

Este documento define:

1. la arquitectura objetivo para generar candidaturas en `job-up`;
2. el estado real de implantación de esa arquitectura;
3. las responsabilidades de cada fase;
4. los criterios que permiten avanzar de una fase a otra;
5. el mecanismo de aprendizaje a partir de candidaturas reales;
6. las reglas de continuidad entre sesiones de trabajo.

Su finalidad principal es evitar:

- pérdida de contexto;
- pérdida de decisiones;
- rediseño repetido de cuestiones ya resueltas;
- mezcla de responsabilidades entre fases;
- avance prematuro;
- divergencia entre artefactos;
- ambigüedad sobre qué está diseñado, probado o validado.

Este SPEC debe permitir que una futura sesión pueda responder rápidamente:

> ¿Qué estamos construyendo, qué decisiones siguen vigentes, qué está realmente probado y cuál es el siguiente trabajo permitido?

---

## 2. Alcance

Este SPEC gobierna la arquitectura documental y operativa de generación de candidaturas dentro de `job-up`.

Incluye:

- candidatura por oferta;
- futura candidatura o presentación espontánea a empresa objetivo;
- análisis de oportunidad;
- ficha de candidatura;
- adaptación estratégica;
- generación de contenido;
- composición documental;
- veredicto;
- preparación posterior de entrevista;
- coordinación entre esas fases.

No define en detalle:

- el contenido interno completo de cada playbook;
- el schema definitivo de `datos-generacion.json`;
- el diseño técnico definitivo de `generar_candidatura.py`;
- los criterios definitivos del futuro veredicto;
- el análisis de empresa objetivo todavía no diseñado.

Esos elementos tendrán sus propios contratos cuando corresponda.

---

## 3. Fuentes y niveles de autoridad

Las fuentes tienen responsabilidades diferentes.

### 3.1 Este SPEC

Gobierna:

- arquitectura;
- separación de responsabilidades;
- orden de maduración;
- decisiones arquitectónicas;
- gates entre fases;
- criterios generales de validación.

### 3.2 `estado-actual.md`

Gobierna:

- continuidad operativa vigente del host;
- sesión relacionada;
- situación actual del proyecto.

### 3.3 Sesión PCS vigente

Registra:

- bloque de trabajo actual;
- pruebas realizadas;
- incidencias;
- decisiones de sesión;
- siguiente gesto.

### 3.4 `AGENTS.md`

Gobierna las reglas operativas aplicables al host.

### 3.5 Playbooks

Cada playbook es autoridad sobre el proceso concreto que gobierna.

### 3.6 Templates

Materializan el contrato documental definido por el playbook correspondiente.

### 3.7 `datos-core-busqueda.md`

Es la autoridad factual sobre trayectoria profesional cuando así lo establezca el flujo vigente.

### 3.8 `seguimiento-candidaturas.md`

Mantiene la visión transversal del conjunto de candidaturas.

### 3.9 `candidatura.md`

Gobierna el ciclo de vida del caso individual.

Principio:

> Ninguna de estas fuentes debe absorber silenciosamente la responsabilidad de otra.

---

## 4. Gobernanza del propio SPEC

### 4.1 Fuente vigente

Debe existir una única versión identificable como actual.

La estrategia recomendada es:

```text
docs/.../SPEC-Arquitectura-modular-generacion-candidatura.md
```

con la versión declarada en el frontmatter.

Las versiones sustituidas deben:

- marcarse como `sustituido`; o
- trasladarse a una ubicación histórica inequívoca.

No deben coexistir varias versiones aparentemente vigentes.

### 4.2 Versionado

Criterio orientativo:

```text
0.x.y → arquitectura todavía en maduración
1.0.0 → arquitectura aceptada como base operativa estable
```

### 4.3 Estados del SPEC

Valores permitidos:

- `borrador_operativo`;
- `en_validacion`;
- `vigente`;
- `sustituido`.

### 4.4 Decisiones arquitectónicas

Se identifican mediante:

```text
ARQ-XX
```

Estados permitidos:

- `vigente`;
- `sustituida`;
- `retirada`.

Una decisión sustituida no se borra.

Debe indicar:

```text
sustituida_por:
motivo:
```

---

## 5. Modelo de estados

Este sistema utiliza varios ejes independientes.

| Eje | Estados |
| --- | --- |
| SPEC | `borrador_operativo`, `en_validacion`, `vigente`, `sustituido` |
| Decisión ARQ | `vigente`, `sustituida`, `retirada` |
| Fase + vía | `pendiente`, `diseñada`, `en_prueba`, `validada` |
| Gate | `pendiente`, `aprobado`, `bloqueado` |
| Candidatura | los definidos por `PLAYBOOK_CANDIDATURA` |

No deben mezclarse.

Ejemplo:

```text
PLAYBOOK_CANDIDATURA [oferta]
estado_fase: en_prueba
```

puede producir:

```text
CAND-2026-019
estado: pendiente_de_aprobacion
```

sin contradicción.

---

## 6. Unidad real de validación

La unidad de validación no es únicamente una fase.

Es:

> **fase + vía de entrada + gate que se quiere superar**

Ejemplo:

```text
PLAYBOOK_CANDIDATURA
vía: oferta
gate: salida_hacia_guion
```

Esto permite validar el flujo por oferta sin tener que esperar a que esté diseñada la futura vía por empresa objetivo.

También evita bloquear trabajo útil por funcionalidades futuras todavía inexistentes.

---

## 7. Responsabilidad humana

La IA puede:

- analizar;
- auditar;
- ejecutar checklists;
- detectar incoherencias;
- proponer clasificaciones;
- recomendar cambios;
- recomendar aprobar o bloquear un gate.

La persona responsable del proyecto decide finalmente:

- aprobación de un gate;
- validación de una fase;
- necesidad de nuevas pruebas;
- adopción de una decisión `ARQ`;
- modificación de arquitectura;
- autorización de acciones externas;
- uso de datos privados cuando corresponda.

La futura skill directora tampoco podrá apropiarse de estas decisiones salvo que exista autorización explícita para ello.

---

# PARTE I — PRINCIPIOS DE DISEÑO

## 8. Arquitectura modular

`job-up` no debe depender de una única skill monolítica que:

- analiza;
- decide;
- redacta;
- maqueta;
- corrige;
- valida;

todo dentro de una única ejecución opaca.

La arquitectura objetivo separa responsabilidades mediante:

```text
playbook
→ artefacto
→ gate
→ siguiente playbook
```

Cada artefacto constituye un contrato de comunicación entre fases.

---

## 9. Separación entre inteligencia y composición

La arquitectura distingue dos capas.

### Capa de inteligencia

Responsable de:

- análisis;
- razonamiento;
- estrategia;
- selección factual;
- redacción.

### Capa de composición

Responsable de:

- estructura documental;
- estilos;
- formato;
- DOCX;
- PDF;
- LaTeX;
- conversiones;
- validación técnica.

La frontera futura será:

```text
datos-generacion.json
```

Principio:

> La composición no debe reinterpretar el contenido.

---

## 10. Corrección por capa

Cuando la arquitectura esté implantada:

### Fallo de contenido

Ejemplos:

- posicionamiento débil;
- logro mal seleccionado;
- frase engañosa;
- omisión estratégica;
- incoherencia entre CV y carta.

Debe corregirse en:

```text
fase de generación de contenido
→ datos-generacion.json
```

### Fallo de composición

Ejemplos:

- salto de página;
- márgenes;
- estilos;
- tipografía;
- estructura DOCX;
- conversión PDF.

Debe corregirse en:

```text
template
o
generar_candidatura.py
```

No debe parchearse manualmente un documento final para resolver un problema de contenido estructural.

---

## 11. Principios transversales de calidad

Toda fase debe preservar estos principios.

### 11.1 Integridad factual

No inventar ni exagerar:

- experiencia;
- formación;
- tecnologías;
- responsabilidades;
- métricas;
- seniority;
- resultados.

### 11.2 Formación no equivale a experiencia

La formación puede demostrar actualización o conocimiento.

No debe transformarse en experiencia profesional inexistente.

### 11.3 Automatización no equivale a IA

Algoritmos, scripts, programación, integraciones, automatizaciones o analítica no deben presentarse automáticamente como experiencia profesional en Inteligencia Artificial.

### 11.4 Encaje funcional no equivale a dominio tecnológico literal

Una persona puede haber resuelto problemas equivalentes utilizando otras tecnologías.

Debe conservarse esa diferencia.

### 11.5 Inferencia no equivale a hecho

Una interpretación estratégica debe permanecer identificable como interpretación.

### 11.6 Relevancia antes que volumen

Una candidatura no mejora por incluir más trayectoria.

Debe incluir aquello que ayuda a responder:

> ¿Por qué debería entrevistar a esta persona para esta oportunidad?

### 11.7 Credibilidad antes que coincidencia artificial

No se debe mejorar la aparente cobertura de una oferta sacrificando credibilidad.

### 11.8 El objetivo es conseguir entrevista

CV, carta y demás piezas no deben intentar contar toda la trayectoria.

Deben producir una candidatura:

- comprensible;
- relevante;
- creíble;
- suficientemente diferencial;
- defendible en entrevista.

---

# PARTE II — DOS VÍAS DE ENTRADA

## 12. Vía A — Candidatura por oferta

Entrada:

```text
oferta
```

Proceso:

```text
PLAYBOOK_ANALISIS_OFERTA
→ analisis-oferta.md
```

Debe determinar:

- contenido factual;
- empresa publicadora;
- empresa contratante cuando sea identificable;
- requisitos;
- prioridades;
- problema empresarial probable;
- encaje;
- carencias;
- riesgos;
- posicionamiento;
- decisión estratégica.

El análisis no redacta documentos finales.

---

## 13. Vía B — Empresa objetivo sin oferta

Entrada:

```text
empresa objetivo
```

Proceso futuro:

```text
PLAYBOOK_ANALISIS_EMPRESA_OBJETIVO
→ artefacto de análisis correspondiente
```

Debe permitir valorar una presentación espontánea a una empresa aunque no exista oferta concreta.

### 13.1 Hipótesis de convergencia

La arquitectura pretende que posteriormente pueda utilizar:

```text
PLAYBOOK_CANDIDATURA
→ candidatura.md
```

Pero esta convergencia no está validada.

### 13.2 Hipótesis de salida

Tampoco debe asumirse todavía que la vía espontánea generará exactamente:

```text
cv.docx
cv.pdf
cv.tex
carta-presentacion.docx
carta-presentacion.pdf
```

El canal real podría requerir:

- CV;
- texto para formulario web;
- email de presentación;
- carta;
- combinación de varios formatos.

Por tanto:

> La vía empresa objetivo puede compartir arquitectura estratégica sin que necesariamente comparta todos los artefactos finales.

Esto deberá decidirse cuando esa vía se diseñe.

---

# PARTE III — ARQUITECTURA OBJETIVO POR OFERTA

## 14. Flujo objetivo

```text
oferta
↓
PLAYBOOK_ANALISIS_OFERTA
↓
analisis-oferta.md
↓
PLAYBOOK_CANDIDATURA
↓
candidatura.md
↓
PLAYBOOK_GUION_ADAPTACION_CV
↓
guion-adaptacion-cv.md
↓
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
↓
datos-generacion.json
↓
generar_candidatura.py
↓
cv.docx
cv.pdf
cv.tex
carta-presentacion.docx
carta-presentacion.pdf
↓
veredicto-final-cv.md
↓
aprobación humana
↓
envío
↓
preparación de entrevista, cuando proceda
```

---

## 15. Contrato conceptual de las fases

| Fase | Responsabilidad principal | Salida | No debe hacer |
| --- | --- | --- | --- |
| Análisis | Entender oportunidad y encaje | `analisis-oferta.md` | Redactar CV/carta |
| Candidatura | Gobernar decisión y ciclo de vida | `candidatura.md` | Rehacer análisis |
| Guion | Traducir estrategia a adaptación | `guion-adaptacion-cv.md` | Redactar documentos finales |
| Generación de contenido | Redactar contenido final estructurado | `datos-generacion.json` | Maquetar |
| Composición | Materializar formatos | documentos finales | Analizar o redactar |
| Veredicto | Evaluar candidatura generada | `veredicto-final-cv.md` | Parchear documentos |
| Entrevista | Preparar defensa y conversación | informe correspondiente | Alterar silenciosamente candidatura |

---

# PARTE IV — ESTADO REAL

## 16. Estado actual por vía

### Vía por oferta

| Unidad | Estado |
| --- | --- |
| `PLAYBOOK_ANALISIS_OFERTA` | `en_prueba` |
| `TEMPLATE_ANALISIS_OFERTA_v2` | `en_prueba` |
| `analisis-oferta.md` | `en_prueba` |
| `PLAYBOOK_CANDIDATURA` | `en_prueba` |
| `TEMPLATE_CANDIDATURA_v2` | `en_prueba` |
| `candidatura.md` | `en_prueba` |
| Gate candidatura → guion | `pendiente` |
| `PLAYBOOK_GUION_ADAPTACION_CV` | `pendiente` |
| `PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA` | `pendiente` |
| `datos-generacion.json` | `pendiente` |
| nueva composición basada en JSON | `pendiente` |
| veredicto adaptado a nueva arquitectura | `pendiente` |

### Vía empresa objetivo

| Unidad | Estado |
| --- | --- |
| análisis específico | `pendiente` |
| compatibilidad con `candidatura.md` | `pendiente` |
| artefactos finales | `pendiente` |
| canal de presentación | `pendiente` |

---

# PARTE V — GATES Y VALIDACIÓN

## 17. Por qué existen gates

Una fase puede tener responsabilidades más amplias que las necesarias para alimentar inmediatamente a la siguiente.

Ejemplo:

`candidatura.md` también mantiene el ciclo de vida posterior:

- aprobación;
- envío;
- rechazo;
- actualización de artefactos.

No es necesario esperar a que una candidatura real complete todo ese ciclo para comprobar si `candidatura.md` es capaz de alimentar correctamente a `PLAYBOOK_GUION_ADAPTACION_CV`.

Por ello se distinguen:

### Madurez global de fase

```text
pendiente
→ diseñada
→ en_prueba
→ validada
```

### Gate de handoff

```text
pendiente
→ aprobado
o
bloqueado
```

Regla:

> Puede avanzarse a la siguiente fase cuando esté aprobado el gate que protege ese handoff, aunque existan aspectos posteriores del ciclo de vida aún en prueba.

---

## 18. Regla general de aprobación de gate

Un gate puede aprobarse cuando:

1. la salida de la fase anterior cumple su contrato relevante;
2. no existen defectos críticos abiertos;
3. la información necesaria para la fase siguiente está presente;
4. la fase siguiente no necesita reconstruir decisiones que deberían venir resueltas;
5. las limitaciones conocidas están explícitas;
6. las pruebas cubren los comportamientos estructurales necesarios;
7. existe aprobación humana.

---

# PARTE VI — GATE ACTUAL: `candidatura.md → guion`

## 19. Identificación

```text
ID: CAND-O1
vía: oferta
origen: PLAYBOOK_CANDIDATURA
destino: PLAYBOOK_GUION_ADAPTACION_CV
estado: pendiente
caso_base: CAND-2026-019
```

Objetivo:

> Determinar si `candidatura.md` entrega a la fase de adaptación estratégica una representación suficientemente completa, compacta, factual y accionable de la candidatura.

---

## 20. Criterios documentales de CAND-O1

### Separación de responsabilidades

- [ ] No vuelve a analizar la oferta.
- [ ] No reproduce matrices completas de análisis.
- [ ] No redacta CV.
- [ ] No redacta carta.
- [ ] No realiza el trabajo del guion.

### Trazabilidad

- [ ] Identifica candidatura.
- [ ] Identifica tipo de origen.
- [ ] Identifica análisis de origen.
- [ ] Conserva decisión estratégica.
- [ ] Conserva evidencias prioritarias.
- [ ] Conserva límites y afirmaciones excluidas.

### Estado

- [ ] Decisión estratégica y estado operativo están separados.
- [ ] `presentada` representa un hecho real.
- [ ] Advertencias, datos pendientes y bloqueos están diferenciados.
- [ ] Los bloqueos producen el comportamiento previsto.
- [ ] La próxima fase está identificada.

### Economía

- [ ] No replica documentos anteriores.
- [ ] No se convierte en una ficha sobredimensionada.
- [ ] Permite comprender la candidatura sin reconstruir todo el análisis.

### Artefactos

- [ ] Registra artefactos existentes.
- [ ] Registra artefactos pendientes.
- [ ] Sus estados son coherentes.
- [ ] Sus referencias permiten localizarlos.

---

## 21. Criterios de selección y empleabilidad de CAND-O1

Desde la perspectiva de un reclutador y coach, la ficha debe permitir responder claramente:

### 21.1 Por qué competir

- [ ] Existe una tesis concreta de candidatura.
- [ ] Esa tesis está respaldada por evidencias.
- [ ] No depende de exagerar experiencia o formación.

### 21.2 Por qué podrían descartarnos

- [ ] Las principales carencias son visibles.
- [ ] Los riesgos de sobrecualificación o infracualificación relevantes están visibles.
- [ ] Las incompatibilidades importantes no quedan escondidas.

### 21.3 Cómo debemos competir

- [ ] El posicionamiento principal es claro.
- [ ] Está claro qué debe dominar el relato.
- [ ] Está claro qué debe quedar en segundo plano.
- [ ] Está claro qué no debe afirmarse.

### 21.4 Qué debe recibir el guion

La fase posterior debe poder saber:

- qué experiencia priorizar;
- qué evidencias utilizar;
- qué riesgos gestionar;
- qué límites respetar;
- qué narrativa desarrollar.

Sin volver a decidir desde cero:

> “¿Por qué nos presentamos a esta oferta?”

---

## 22. Criterio crítico de handoff

El gate CAND-O1 no se considera aprobado si `PLAYBOOK_GUION_ADAPTACION_CV` necesita releer el análisis completo para reconstruir:

- argumento competitivo;
- posicionamiento;
- evidencias prioritarias;
- afirmaciones prohibidas;
- advertencias;
- bloqueos.

Puede consultar el análisis para detalle o trazabilidad.

No debe necesitarlo para rehacer la estrategia básica.

---

# PARTE VII — COBERTURA DE PRUEBA

## 23. Caso base

Caso actual:

```text
CAND-2026-019
```

Cubre:

- origen por oferta;
- empresa publicadora distinta de empresa contratante;
- decisión `preparar_con_advertencias`;
- numerosas advertencias;
- datos pendientes;
- ausencia de bloqueo;
- candidatura con artefactos posteriores existentes;
- estado `pendiente_de_aprobacion`;
- `presentada: false`.

---

## 24. Comportamientos estructurales no cubiertos

CAND-2026-019 no demuestra:

- comportamiento con bloqueo activo;
- decisión `pedir_datos_adicionales_antes_de_redactar`;
- creación normal con decisión `preparar_candidatura`;
- comportamiento ante `no_recomendada`;
- empresa publicadora igual a contratante;
- vía empresa objetivo;
- transición real a `enviada`.

No todos estos huecos bloquean CAND-O1.

---

## 25. Cobertura mínima obligatoria para CAND-O1

Antes de aprobar el gate deben estar probados:

### Obligatorio A — continuación normal

Una candidatura capaz de avanzar.

Puede ser:

- `preparar_candidatura`; o
- `preparar_con_advertencias`.

`CAND-2026-019` cubre este comportamiento.

### Obligatorio B — bloqueo

Debe comprobarse:

```text
pedir_datos_adicionales_antes_de_redactar
→ candidatura.md
→ estado: detenida
→ no avanza al guion
```

Puede probarse mediante:

- caso real; o
- fixture/caso controlado.

No es necesario crear artificialmente una candidatura real solo para probar el mecanismo.

### Obligatorio C — no recomendada

Debe comprobarse a nivel de playbook/orquestación que:

```text
no_recomendada
```

no inicia producción documental normal.

No es necesario generar una `candidatura.md` completa para demostrarlo.

---

## 26. Coberturas que no bloquean CAND-O1

No es obligatorio probar todavía:

- empresa objetivo;
- transición a enviada;
- transición a rechazada;
- todos los posibles tipos de puesto;
- todas las combinaciones de empresa publicadora/contratante.

Esos comportamientos podrán formar parte de validaciones posteriores.

---

## 27. Decisión de gate

Después de las pruebas, el gate termina en una de dos situaciones.

### `aprobado`

La salida de candidatura puede alimentar el diseño y prueba del guion.

### `bloqueado`

Existe al menos un defecto que impide confiar en el handoff.

Debe registrarse:

```text
defecto:
clasificacion:
impacto:
correccion_necesaria:
```

---

# PARTE VIII — SIGUIENTE FASE

## 28. `PLAYBOOK_GUION_ADAPTACION_CV`

Solo debe entrar en diseño operativo después de aprobar CAND-O1.

Objetivo conceptual:

> Convertir la estrategia de candidatura en instrucciones concretas de adaptación.

Debe recibir:

```text
analisis-oferta.md
+ candidatura.md
+ datos-core-busqueda.md
```

y producir:

```text
guion-adaptacion-cv.md
```

---

## 29. Responsabilidad prevista del guion

Debe determinar:

- narrativa profesional;
- selección de experiencias;
- jerarquía de evidencias;
- tratamiento del seniority;
- tratamiento de carencias;
- palabras clave utilizables;
- énfasis;
- omisiones deliberadas;
- tono;
- orientación del CV;
- relación estratégica entre CV y carta.

No debe producir todavía la redacción final de ambos documentos.

---

## 30. Criterio de calidad futuro del guion

El guion deberá conseguir que la futura fase de redacción no necesite volver a decidir:

- qué perfil estamos presentando;
- por qué;
- con qué evidencias;
- frente a qué riesgos;
- con qué límites.

---

# PARTE IX — GENERACIÓN ÚNICA DE CONTENIDO

## 31. Arquitectura futura

Después del guion:

```text
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
→ datos-generacion.json
```

Consumirá previsiblemente:

```text
analisis-oferta.md
candidatura.md
guion-adaptacion-cv.md
datos-core-busqueda.md
datos privados autorizados
```

La redacción de:

- CV;
- carta;
- bloques destinados a LaTeX;

debe realizarse una sola vez.

---

## 32. Registro de necesidades futuras del JSON

No se diseña todavía su schema.

Sí se registran requisitos descubiertos durante las pruebas.

Formato:

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

Las entradas `JSON-NEC-*`:

- son observaciones;
- no son campos definitivos;
- no comprometen el schema;
- sirven para evitar pérdida de aprendizaje.

---

# PARTE X — COMPOSICIÓN Y VEREDICTO

## 33. Composición futura

Para la vía por oferta:

```text
datos-generacion.json
→ generar_candidatura.py
```

produce previsiblemente:

```text
cv.docx
cv.pdf
cv.tex
carta-presentacion.docx
carta-presentacion.pdf
```

El compositor no:

- analiza;
- decide;
- redacta;
- corrige contenido.

---

## 34. Veredicto futuro

El veredicto evaluará los documentos generados.

Entre otros aspectos deberá revisar:

- integridad factual;
- credibilidad;
- coherencia;
- fuerza en primera lectura;
- adecuación;
- narrativa;
- cobertura relevante;
- calidad documental.

Los criterios, niveles de severidad y umbrales se diseñarán cuando esa fase pase a `diseñada`.

No corresponde fijarlos todavía.

---

# PARTE XI — APRENDIZAJE

## 35. Taxonomía de defectos

Todo problema detectado debe clasificarse.

### `CASO`

Particular del caso analizado.

### `PLAYBOOK`

Defecto de proceso o razonamiento normativo.

### `TEMPLATE`

Defecto de estructura del artefacto.

### `DATOS_CORE`

Información factual ausente, insuficiente o mal representada.

### `ARQUITECTURA`

Fallo en límites o responsabilidades entre fases.

### `COMPOSICION`

Problema técnico de generación documental.

---

## 36. Clasificaciones múltiples

Un defecto puede afectar a varias capas.

Ejemplo:

```text
datos faltantes
→ DATOS_CORE

pero el playbook los supone obligatorios sin tratamiento alternativo
→ PLAYBOOK
```

Cuando haya duda, la IA propone y la persona responsable decide.

---

## 37. Aprendizaje entre candidaturas

No debe modificarse una regla general automáticamente porque falle un caso.

Debe preguntarse:

1. ¿Es específico del caso?
2. ¿Puede repetirse?
3. ¿Afecta al contrato?
4. ¿Qué documento tiene autoridad para resolverlo?

Principio:

> Los casos generan evidencia; la arquitectura se modifica cuando la evidencia demuestra una necesidad generalizable.

---

## 38. Destino de mejoras generalizables

```text
hecho profesional
→ datos-core-busqueda.md

razonamiento de análisis
→ PLAYBOOK_ANALISIS_OFERTA

gobierno de candidatura
→ PLAYBOOK_CANDIDATURA

estructura de candidatura
→ TEMPLATE_CANDIDATURA_v2

separación entre fases
→ este SPEC

seguimiento transversal
→ seguimiento-candidaturas.md

composición
→ template visual / script
```

---

## 39. Redundancia de reglas

Durante la transición se admite que determinadas reglas factuales aparezcan en varios playbooks.

Debe revisarse esa redundancia cuando:

1. una regla necesite modificarse;
2. aparezcan formulaciones divergentes;
3. una misma modificación deba repetirse manualmente;
4. existan dudas sobre qué documento es autoridad.

En ese momento deberá decidirse explícitamente la fuente normativa adecuada.

---

# PARTE XII — TRAZABILIDAD

## 40. Identificador de candidatura

Formato:

```text
CAND-AAAA-NNN
```

Es la clave lógica del caso.

Todos sus artefactos deben poder vincularse inequívocamente con ese ID.

---

## 41. Nombres de archivo

Los nombres no deben ser la única fuente de identidad.

Debe reducirse progresivamente la deriva entre:

- mayúsculas;
- minúsculas;
- sufijos;
- versiones;
- nombres alternativos.

La convención definitiva se decidirá antes de escalar ampliamente la arquitectura.

---

## 42. Seguimiento transversal frente a ficha individual

```text
seguimiento-candidaturas.md
```

responde:

> ¿Qué está ocurriendo con el conjunto de candidaturas?

```text
candidatura.md
```

responde:

> ¿Qué está ocurriendo con esta candidatura concreta?

No debe crearse otro índice maestro mientras estas dos piezas cubran adecuadamente ambas necesidades.

---

# PARTE XIII — CONTINUIDAD ENTRE SESIONES

## 43. Rehidratación mínima

Toda nueva sesión sobre esta línea debe localizar:

```text
host
rama
SPEC vigente
estado-actual.md
sesión PCS vigente
vía de trabajo
fase actual
gate actual
último caso probado
defectos abiertos
siguiente acción permitida
```

---

## 44. Preguntas que la rehidratación debe responder

1. ¿Qué vía estamos desarrollando?
2. ¿Qué fase está activa?
3. ¿Cuál es su estado?
4. ¿Qué gate está abierto?
5. ¿Qué artefacto se está probando?
6. ¿Qué comportamientos faltan por probar?
7. ¿Qué defectos siguen abiertos?
8. ¿Qué decisiones ARQ están vigentes?
9. ¿Qué debe ocurrir para poder avanzar?

---

## 45. Registro en PCS

Cuando sea relevante para continuidad, la sesión PCS debe dejar constancia de:

```text
via_actual:
fase_actual:
estado_fase:
gate_actual:
estado_gate:
casos_probados:
defectos_abiertos:
decisiones_tomadas:
siguiente_accion:
```

No es necesario modificar este SPEC en cada sesión.

---

## 46. Cuándo modificar el SPEC

Debe modificarse cuando ocurra al menos uno de estos eventos:

- cambia arquitectura;
- cambia responsabilidad de una fase;
- cambia un gate;
- se adopta o sustituye una decisión ARQ;
- cambia el modelo de validación;
- una prueba demuestra una necesidad arquitectónica generalizable;
- cambia el alcance previsto de una vía.

No debe modificarse para registrar incidencias particulares de una candidatura.

---

# PARTE XIV — DECISIONES ARQUITECTÓNICAS VIGENTES

## 47. Registro

### ARQ-01 — Arquitectura modular

La candidatura se divide en fases especializadas.

Estado: `vigente`.

### ARQ-02 — Separación entre análisis y redacción

El análisis no redacta documentos finales.

Estado: `vigente`.

### ARQ-03 — `candidatura.md` como ficha viva

Gobierna decisión, estado y artefactos sin sustituir análisis o documentos posteriores.

Estado: `vigente`.

### ARQ-04 — Dos vías de entrada

Se pretende soportar:

- oferta;
- empresa objetivo.

Estado: `vigente`.

La segunda vía sigue sin validar.

### ARQ-05 — Convergencia no asumida

La compatibilidad completa de `candidatura.md` con empresa objetivo es una hipótesis pendiente.

Estado: `vigente`.

### ARQ-06 — Artefactos finales de empresa objetivo no definidos

No se presume que una presentación espontánea produzca exactamente el mismo paquete documental que una candidatura por oferta.

Estado: `vigente`.

### ARQ-07 — Guion antes de redacción final

Debe existir adaptación estratégica explícita antes de generar contenido final.

Estado: `vigente`.

### ARQ-08 — Redacción única

CV, carta y LaTeX deben derivar de una misma generación estructurada de contenido.

Estado: `vigente`.

### ARQ-09 — JSON como futura frontera

`datos-generacion.json` separará redacción y composición.

Estado: `vigente`.

Implementación: `pendiente`.

### ARQ-10 — Composición determinista

El compositor no analiza ni redacta.

Estado: `vigente`.

### ARQ-11 — Corrección por capa

Contenido y composición se corrigen en capas distintas.

Estado: `vigente`.

### ARQ-12 — Gates de handoff

El avance entre fases depende de gates explícitos.

Estado: `vigente`.

### ARQ-13 — Validación por vía

Una fase puede validarse o superar gates para una vía sin esperar a que las otras vías estén diseñadas.

Estado: `vigente`.

### ARQ-14 — Cierre humano

La aprobación final de gates y fases corresponde a la persona responsable.

Estado: `vigente`.

### ARQ-15 — Aprendizaje transversal

Los casos pueden modificar playbooks, templates, datos core o arquitectura cuando revelen problemas generalizables.

Estado: `vigente`.

### ARQ-16 — Única fuente vigente del SPEC

Debe ser inequívoco cuál es la versión actual.

Estado: `vigente`.

---

# PARTE XV — TRABAJO ACTUAL

## 48. Situación

Vía:

```text
oferta
```

Fase:

```text
PLAYBOOK_CANDIDATURA
→ candidatura.md
```

Estado:

```text
en_prueba
```

Gate:

```text
CAND-O1
```

Estado del gate:

```text
pendiente
```

Caso base:

```text
CAND-2026-019
```

---

## 49. Próximo trabajo permitido

El próximo trabajo debe ser:

1. auditar `PLAYBOOK_CANDIDATURA`;
2. auditar `TEMPLATE_CANDIDATURA_v2`;
3. auditar `candidatura_CAND-2026-019_v2`;
4. aplicar los criterios CAND-O1;
5. registrar defectos;
6. clasificarlos;
7. corregir los generalizables;
8. repetir la prueba;
9. comprobar el comportamiento bloqueado;
10. comprobar el comportamiento `no_recomendada`;
11. decidir humanamente si CAND-O1 se aprueba.

---

## 50. Transición autorizada

Solo tras:

```text
CAND-O1: aprobado
```

se pasa a:

```text
diseño de PLAYBOOK_GUION_ADAPTACION_CV
```

---

## 51. Transiciones todavía no autorizadas

No corresponde todavía diseñar en profundidad:

```text
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
datos-generacion.json
nuevo generar_candidatura.py
nuevo veredicto
PLAYBOOK_ANALISIS_EMPRESA_OBJETIVO
```

Pueden registrarse necesidades o decisiones conceptuales cuando aparezcan.

No deben convertirse todavía en foco de implementación.

---

# 52. Resumen ejecutivo

La arquitectura objetivo por oferta es:

```text
analisis-oferta.md
→ candidatura.md
→ guion-adaptacion-cv.md
→ datos-generacion.json
→ composición determinista
→ documentos finales
→ veredicto
→ aprobación humana
→ envío
→ entrevista cuando proceda
```

La vía por empresa objetivo sigue siendo una línea futura y no se presume idéntica a la candidatura por oferta.

El estado actual es:

```text
PLAYBOOK_CANDIDATURA [oferta]
→ en_prueba

Gate CAND-O1
→ pendiente

PLAYBOOK_GUION_ADAPTACION_CV
→ pendiente
```

La prioridad inmediata no es diseñar más arquitectura.

Es demostrar que `candidatura.md` puede entregar al futuro guion una candidatura:

- factual;
- estratégica;
- compacta;
- trazable;
- creíble;
- accionable;
- consciente de sus riesgos.

El criterio fundamental es:

> La fase siguiente puede consultar el análisis para obtener detalle, pero no debe necesitar rehacer la estrategia que `candidatura.md` tenía la responsabilidad de conservar.

Regla de avance:

> No se avanza porque un documento “parezca bueno”.  
> Se avanza cuando el handoff necesario ha demostrado funcionar y su gate ha sido aprobado.

Regla de selección:

> La candidatura debe maximizar relevancia y credibilidad, no coincidencia artificial.

Regla arquitectónica:

> El contenido se corrige en la capa de contenido.  
> La composición se corrige en la capa de composición.

---

## Changelog

### 0.3.1 — 2026-08-04

- Se reorganiza el SPEC para reducir repetición y separar arquitectura, implantación y gates.
- Se introduce la unidad de validación `fase + vía + gate`.
- Se diferencia madurez global de fase y autorización de handoff.
- Se crea el gate `CAND-O1` para `candidatura.md → guion-adaptacion-cv.md`.
- Se definen criterios documentales y de selección para CAND-O1.
- Se establecen pruebas mínimas de continuación, bloqueo y `no_recomendada`.
- Se evita exigir el ciclo de vida completo de una candidatura para poder diseñar la siguiente fase.
- Se mantiene `PLAYBOOK_CANDIDATURA [oferta]` en `en_prueba`.
- Se mantiene `PLAYBOOK_GUION_ADAPTACION_CV` como siguiente fase permitida.
- Se rebaja explícitamente la simetría entre candidatura por oferta y empresa objetivo.
- Se deja sin definir el paquete documental final de la vía espontánea.
- Se refuerzan relevancia, credibilidad y capacidad de conseguir entrevista como criterios transversales.
- Se mantiene el registro `JSON-NEC-*` sin adelantar el schema.
- Se refuerza la responsabilidad humana sobre gates y validaciones.
- Se establece una única versión canónica del SPEC como objetivo de gobernanza.
- Se conserva la clasificación de defectos y el aprendizaje entre candidaturas.
- Se sustituye la versión `0.2.5`.