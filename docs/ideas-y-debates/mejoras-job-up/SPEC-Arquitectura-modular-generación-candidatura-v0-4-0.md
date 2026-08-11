---
id: spec-arquitectura-generacion-candidaturas-job-up
titulo: SPEC — Arquitectura modular para generación de candidaturas en Job-up
version: "0.4.0"
estado: borrador_operativo
referencia_de_trabajo: true
fecha_version: 2026-08-04
host: carrera-ai
rama: job-up
origen_historico: sesion-20260801-2040-job-up
sustituye:
  - "0.3.5"
audiencias:
  - humano
  - agente_ia_planificador
---
# SPEC — Arquitectura modular para generación de candidaturas en Job-up

## 1. Propósito

Este documento define la arquitectura de trabajo para la generación modular de candidaturas dentro de `job-up`.

Tiene dos funciones simultáneas:

1. servir de referencia comprensible para una persona;
2. servir como entrada normativa para un agente de IA encargado de elaborar un plan de implementación.

Debe permitir conservar entre sesiones:

- arquitectura;
- decisiones;
- responsabilidades;
- estado real;
- fases pendientes;
- gates abiertos;
- criterios de avance;
- defectos conocidos;
- límites de autonomía;
- siguiente trabajo permitido.

Pregunta principal de continuidad:

> ¿Dónde estamos, qué está demostrado, qué falta demostrar y qué puede hacerse a continuación sin inventar decisiones?

---

# PARTE I — AUDIENCIAS Y REGLAS DE INTERPRETACIÓN

## 2. Audiencias del documento

### 2.1 Persona lectora

Debe poder comprender:

- qué se está construyendo;
- cómo está dividido;
- qué está implementado;
- qué está pendiente;
- qué decisiones ya se tomaron;
- cuál es la siguiente fase;
- qué debe ocurrir antes de avanzar.

No debería necesitar conocer conversaciones anteriores de ChatGPT para entender la arquitectura.

### 2.2 Agente de IA planificador

Debe poder extraer de este documento:

- alcance;
- fuera de alcance;
- estado inicial;
- dependencias;
- precondiciones;
- postcondiciones;
- artefactos;
- gates;
- criterios de aceptación;
- puntos de aprobación humana;
- incertidumbres;
- orden permitido de trabajo.

El agente planificador debe convertir esta SPEC en un **plan de implementación**, no reinterpretar ni rediseñar la arquitectura por iniciativa propia.

---

## 3. Contrato del agente planificador

Si un agente de IA recibe esta SPEC para elaborar un plan, debe aplicar obligatoriamente las siguientes reglas.

### 3.1 Antes de planificar

Debe:

1. leer esta SPEC completa;
2. verificar las reglas vigentes del host;
3. consultar `estado-actual.md`;
4. identificar la sesión PCS vigente;
5. inspeccionar el estado real del repositorio;
6. verificar la existencia de los ficheros que vaya a utilizar;
7. comparar el estado real con el estado declarado en esta SPEC.

No debe asumir que un archivo mencionado como futuro existe físicamente.

---

### 3.2 Su función es planificar, no implementar

Salvo instrucción explícita contraria, el agente:

- no modifica archivos;
- no crea código;
- no crea playbooks;
- no cambia templates;
- no ejecuta migraciones;
- no cambia arquitectura.

Su salida es un plan ejecutable posteriormente.

---

### 3.3 No puede rellenar huecos mediante invención

Si falta información necesaria debe:

1. identificar la carencia;
2. clasificarla como incertidumbre;
3. determinar si bloquea o no el plan;
4. continuar con todo lo que sí pueda determinarse.

No debe inventar:

- rutas;
- schemas;
- contratos;
- estados;
- templates;
- decisiones;
- artefactos;
- reglas de negocio.

---

### 3.4 Debe respetar los gates

Una fase futura puede aparecer en el plan como:

- dependencia;
- hito futuro;
- trabajo fuera de alcance.

No debe descomponerse en tareas implementables mientras su gate anterior no esté aprobado.

Ejemplo:

Permitido:

```text id="jbdha2"
Fase futura:
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA

Dependencia:
GATE-GUION-CV-CONTENIDO aprobado; contrato de la fase diseñado y validado técnicamente
```

No permitido:

```text id="ewtfaw"
Tarea 12: diseñar schema JSON
Tarea 13: modificar generar_candidatura.py
```

si los gates anteriores siguen abiertos.

---

## 4. Jerarquía de autoridad

Cuando dos fuentes parezcan contradictorias, el agente no debe elegir silenciosamente una.

### 4.1 Arquitectura

Este SPEC gobierna:

- separación entre fases;
- relaciones entre fases;
- gates;
- orden de maduración;
- responsabilidades arquitectónicas.

### 4.2 Proceso concreto

El playbook correspondiente gobierna el comportamiento de su fase.

### 4.3 Estructura documental

El template materializa el playbook.

Un template no puede contradecir al playbook que representa.

### 4.4 Factualidad profesional

`datos-core-busqueda.md` es la autoridad factual cuando corresponda según el flujo.

### 4.5 Caso concreto

Los artefactos de una candidatura deben respetar las autoridades anteriores.

### 4.6 Contradicción

Si existe una contradicción real:

```text id="nu83li"
SPEC
vs
PLAYBOOK
vs
TEMPLATE
vs
CASO
```

el agente debe registrarla como defecto.

No debe continuar con tareas cuya corrección dependa de resolver esa contradicción.

---

# PARTE II — TERMINOLOGÍA NORMATIVA

## 5. Glosario

### Arquitectura objetivo

Diseño previsto del sistema completo.

Puede contener elementos todavía no implementados.

### Estado real

Situación comprobable actualmente en el repositorio.

### Fase

Unidad funcional del flujo con responsabilidad propia.

Normalmente está gobernada por un playbook.

### Artefacto

Salida persistente generada o mantenida por una fase.

Ejemplos:

```text id="dn1d3m"
analisis-oferta.md
candidatura.md
guion-adaptacion-cv.md
```

### Vía

Variante de entrada al sistema.

Actualmente:

```text id="qby1qb"
oferta
empresa_objetivo
```

### Traspaso

Transferencia de responsabilidad e información desde una fase hacia otra.

Equivale al concepto técnico de `handoff`.

### Gate

Punto de control formal que determina si un traspaso entre dos fases está suficientemente demostrado para autorizar el avance.

### Precondición

Condición que debe cumplirse antes de ejecutar una fase o tarea.

### Postcondición

Condición que debe ser cierta después de completarla correctamente.

### Caso real

Candidatura existente utilizada como evidencia.

### Caso controlado

Escenario preparado específicamente para probar un comportamiento del sistema.

Puede utilizarse cuando no existe todavía un caso real apropiado.

### Defecto crítico

Defecto que provoca al menos una de estas consecuencias:

- falsificación o pérdida factual;
- contradicción significativa entre artefactos;
- incumplimiento de responsabilidad de fase;
- imposibilidad de realizar el siguiente traspaso sin reconstruir decisiones;
- avance cuando debería existir un bloqueo;
- generación potencial de una candidatura engañosa;
- pérdida de trazabilidad necesaria para auditar el resultado.

### Tesis de candidatura

Razón argumentada por la que tiene sentido competir por una oportunidad.

### Posicionamiento

Ángulo profesional desde el que se decide presentar al candidato.

### Gancho

Idea breve y memorable que concentra el posicionamiento y debe captar la atención inicial del reclutador.

Ejemplo conceptual:

```text id="vjt0w2"
TESIS
Tiene sentido competir porque existe experiencia demostrada
resolviendo problemas de negocio mediante automatización.

POSICIONAMIENTO
Perfil híbrido negocio-operaciones-tecnología.

GANCHO
Convierte problemas operativos en sistemas y automatizaciones
con impacto medible.
```

### Promoción documental

Paso explícito de un documento experimental de `ideas-y-debates` a documentación normativa estable.

### Implementación

Materialización física de una decisión o diseño en:

- archivos;
- código;
- configuración;
- templates;
- estructuras operativas.

---

## 6. Convenciones de identificadores

Los espacios de nombres son independientes.

### Candidaturas

```text id="6qbl0i"
CAND-AAAA-NNN
```

Ejemplo:

```text id="kpbhda"
CAND-2026-019
```

Solo identifica candidaturas.

---

### Decisiones arquitectónicas

```text id="f3j4wb"
ARQ-NN
```

Ejemplo:

```text id="555c1w"
ARQ-07
```

---

### Gates

```text id="d7lmcp"
GATE-<FASE-ORIGEN>-<FASE-DESTINO>
```

Ejemplo actual:

```text id="y51vbf"
GATE-CANDIDATURA-GUION
```

---

### Necesidades candidatas del futuro JSON

```text id="9bhhc7"
JSON-NEC-NNN
```

---

### Incertidumbres

```text id="vxqvre"
INC-NNN
```

Regla:

> Un prefijo no puede reutilizarse para entidades de naturaleza diferente.

---

# PARTE III — GOBERNANZA

## 7. Fuentes y responsabilidades

### Este SPEC

Gobierna:

- arquitectura;
- gates;
- responsabilidades;
- orden de maduración;
- decisiones `ARQ`.

### `estado-actual.md`

Gobierna la continuidad operativa vigente.

### Sesión PCS

Registra el bloque de trabajo concreto.

### `AGENTS.md`

Gobierna las reglas operativas del host.

### Playbooks

Gobiernan procesos concretos.

### Templates

Materializan los contratos documentales.

### `datos-core-busqueda.md`

Fuente factual profesional cuando el flujo lo utilice.

### `seguimiento-candidaturas.md`

Visión transversal del conjunto.

### `candidatura.md`

Gobierno del caso individual.

---

## 8. Estados

### SPEC

```text id="lbfj3d"
borrador_operativo
en_validacion
vigente
sustituido
```

### Decisiones `ARQ`

```text id="rzu16j"
vigente
sustituida
retirada
```

### Fase + vía

```text id="5gmveo"
pendiente
diseñada
en_prueba
validada
```

### Gate

```text id="vf3sja"
pendiente
aprobado
bloqueado
```

### Candidatura

Los definidos por `PLAYBOOK_CANDIDATURA`.

No deben mezclarse estos ejes.

---

## 9. Gate no equivale a validación completa

La aprobación de un gate valida únicamente el traspaso que protege.

No implica necesariamente que la fase de origen esté completamente validada.

Es válida esta situación:

```text id="lq2awf"
PLAYBOOK_CANDIDATURA [oferta]
estado_fase: en_prueba

GATE-CANDIDATURA-GUION
estado: aprobado
```

Esto significa:

> El traspaso hacia el guion funciona, aunque existan otros comportamientos de `candidatura.md` todavía en prueba.

---

## 10. Responsabilidad humana

La IA puede:

- evaluar;
- comparar;
- clasificar;
- proponer;
- ejecutar pruebas;
- recomendar gates.

La persona responsable decide:

- aprobación de un gate;
- validación de fase;
- adopción de una decisión `ARQ`;
- modificación arquitectónica;
- promoción documental;
- autorización externa;
- uso de datos privados cuando corresponda.

---

# PARTE IV — PRINCIPIOS DEL SISTEMA

## 11. Arquitectura modular

El sistema no debe concentrar en una única skill:

- análisis;
- estrategia;
- redacción;
- composición;
- validación.

Patrón:

```text id="asrdy2"
PLAYBOOK
→ ARTEFACTO
→ GATE
→ SIGUIENTE PLAYBOOK
```

---

## 12. Inteligencia frente a composición

### Inteligencia

Responsable de:

- análisis;
- interpretación;
- selección;
- estrategia;
- redacción.

### Composición

Responsable de:

- formato;
- estilos;
- DOCX;
- PDF;
- LaTeX;
- transformación técnica.

Frontera futura:

```text id="v65cnl"
datos-generacion.json
```

En la rama arquitectónica actualmente diseñada, esta frontera corresponde exclusivamente al contenido del CV. No
implica un artefacto, schema ni traspaso común con la carta de presentación, cuya rama independiente ya está diseñada y se prueba por separado.

---

## 13. Corrección por capa

Contenido:

```text id="egkbvk"
→ fase de inteligencia responsable
```

Composición:

```text id="v4nzfm"
→ template o script
```

Regla:

> No se parchean documentos finales para corregir errores cuyo origen pertenece a una fase anterior.

---

## 14. Principios factuales

### No invención

No inventar:

- experiencia;
- formación;
- tecnologías;
- responsabilidades;
- resultados;
- métricas;
- seniority.

### Formación no equivale a experiencia

### Automatización no equivale a IA

### Inferencia no equivale a hecho

### Transferibilidad no equivale a experiencia literal

---

## 15. Principio competitivo

Una candidatura correcta no es necesariamente una candidatura competitiva.

Dentro de los límites factuales, debe buscarse:

- máxima relevancia;
- diferenciación;
- claridad;
- credibilidad;
- fuerza de evidencia;
- capacidad de generar entrevista.

La prudencia factual no debe convertir el perfil en invisible.

---

# PARTE V — VÍAS DE ENTRADA

## 16. Vía oferta

Entrada:

```text id="8ej73u"
oferta
```

Primera fase:

```text id="4krnve"
PLAYBOOK_ANALISIS_OFERTA
→ analisis-oferta.md
```

Debe producir una interpretación factual y estratégica de la oportunidad.

---

## 17. Vía empresa objetivo

Entrada futura:

```text id="s9z19o"
empresa objetivo
```

Arquitectura prevista:

```text id="vc5bhn"
PLAYBOOK_ANALISIS_EMPRESA_OBJETIVO
→ artefacto de análisis
```

La compatibilidad posterior con:

```text id="7wqh42"
PLAYBOOK_CANDIDATURA
```

es una hipótesis pendiente.

Tampoco se ha definido todavía qué paquete documental final necesitará esta vía.

No debe asumirse que será idéntico al flujo por oferta.

---

# PARTE VI — FLUJO OBJETIVO POR OFERTA

## 18. Pipeline

```text id="pubzf5"
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
GATE-GUION-CV-CONTENIDO
↓
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
↓
datos-generacion.json
↓
PLAYBOOK_COMPONER_CV
↓
cv.docx / cv.pdf / cv.tex
↓
GATE-VEREDICTO-CV
↓
PLAYBOOK_GUION_CARTA_PRESENTACION (si la candidatura requiere carta)
↓
guion-carta-presentacion.md
↓
PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION
↓
contenido-carta-presentacion.md
↓
PLAYBOOK_COMPONER_CARTA_PRESENTACION
↓
carta-presentacion.docx / carta-presentacion.pdf
↓
GATE-VEREDICTO-CARTA
↓
CANDIDATURA DOCUMENTALMENTE COMPLETA

La presentación externa automatizada y la UI inicial de configuración quedan
fuera de este flujo y se documentan como líneas futuras independientes.
```

---

## 19. Contrato conceptual de fases

| Fase | Responsabilidad | Salida |
| --- | --- | --- |
| Análisis | Entender oportunidad y encaje | `analisis-oferta.md` |
| Candidatura | Gobernar estrategia heredada y ciclo de vida | `candidatura.md` |
| Guion CV | Traducir estrategia común a decisiones editoriales exclusivas del CV | `guion-adaptacion-cv.md` |
| Contenido CV | Redactar el contenido final del CV a partir de `guion-adaptacion-cv.md` aprobado | `datos-generacion.json` |
| Carta de presentación | Adaptar la estrategia común a una carta mediante su módulo independiente cuando se requiera | `guion-carta-presentacion.md` y sus artefactos posteriores |
| Composición y veredicto CV | Fases CV-only diseñadas e implantadas | `GATE-VEREDICTO-CV` |
| Cierre documental | Confirmar CV y carta aprobados cuando corresponda | candidatura documentalmente completa |
| Entrevista | Preparar defensa posterior | informe |

---

# PARTE VII — CONTRATOS DE FASE

## 20. Patrón obligatorio

Toda fase que pase de `pendiente` a `diseñada` debe definir:

```text id="3xl7kn"
OBJETIVO
PRECONDICIONES
ENTRADAS
RESPONSABILIDADES
FUERA_DE_RESPONSABILIDAD
SALIDA
POSTCONDICIONES
DEFECTOS_CRITICOS
GATE_SIGUIENTE
CRITERIOS_DE_ACEPTACION
```

Un agente planificador debe comprobar que este contrato existe antes de diseñar tareas de implementación.

---

## 21. Fase actual — Candidatura

### Objetivo

Crear y mantener:

```text id="bxee09"
candidatura.md
```

como ficha viva del caso.

### Precondiciones

Para vía oferta debe existir:

```text id="embsvn"
analisis-oferta.md
```

con decisión estratégica suficiente.

### Entradas

- análisis;
- identificación de candidatura;
- datos operativos necesarios.

### Responsabilidades

Debe conservar:

- identidad;
- origen;
- decisión;
- tesis;
- posicionamiento;
- gancho cuando exista;
- evidencias prioritarias;
- riesgos;
- límites;
- afirmaciones excluidas;
- pendientes;
- bloqueos;
- estado;
- artefactos;
- siguiente fase.

### Fuera de responsabilidad

No debe:

- rehacer el análisis;
- redactar CV;
- redactar carta;
- diseñar el guion;
- realizar veredicto.

### Salida

```text id="29wytv"
candidatura.md
```

### Postcondiciones

La ficha debe permitir entender:

- por qué competir;
- cómo competir;
- con qué evidencia;
- con qué riesgos;
- con qué límites;
- cuál es el estado operativo.

### Gate siguiente

```text id="w43jhs"
GATE-CANDIDATURA-GUION
```

---

# PARTE VIII — GATE ACTUAL

## 22. Definición de `GATE-CANDIDATURA-GUION`

`GATE-CANDIDATURA-GUION` es el punto de control que determina si `candidatura.md` transmite información suficientemente:

- completa;
- factual;
- estratégica;
- compacta;
- trazable;
- accionable;

para iniciar `PLAYBOOK_GUION_ADAPTACION_CV` sin reconstruir la estrategia anterior.

```text id="ml84ia"
origen:
PLAYBOOK_CANDIDATURA
→ candidatura.md

gate:
GATE-CANDIDATURA-GUION

destino:
PLAYBOOK_GUION_ADAPTACION_CV
```

Estado actual:

```text id="9gz78w"
aprobado
```

Caso base:

```text id="ew27lr"
CAND-2026-019
```

---

## 23. Criterios de `GATE-CANDIDATURA-GUION`

### Responsabilidad

- [ ] La ficha gobierna el caso.
- [ ] No rehace el análisis.
- [ ] No invade fases posteriores.

### Trazabilidad

- [ ] Origen identificado.
- [ ] Análisis de origen identificado.
- [ ] Decisión estratégica conservada.
- [ ] Evidencias trazables.
- [ ] Límites trazables.

### Estado

- [ ] Decisión y estado operativo están separados.
- [ ] Advertencias y bloqueos están separados.
- [ ] `presentada` representa un hecho.
- [ ] Siguiente fase identificada.

### Economía

- [ ] No duplica matrices completas.
- [ ] No duplica contenido futuro.
- [ ] Contiene suficiente contexto para gobernar.

### Calidad competitiva

- [ ] Existe tesis de candidatura.
- [ ] Existe posicionamiento.
- [ ] Existe o puede identificarse un gancho.
- [ ] Las evidencias respaldan el posicionamiento.
- [ ] Los riesgos no destruyen innecesariamente la fuerza del relato.
- [ ] Las afirmaciones prohibidas están claras.

### Traspaso

El futuro guion debe poder saber:

- qué relato desarrollar;
- qué experiencia priorizar;
- qué evidencia utilizar;
- qué riesgos gestionar;
- qué afirmaciones evitar;

sin volver a decidir:

> ¿Por qué estamos compitiendo?

---

## 24. Cobertura necesaria

### Continuación normal

Caso disponible:

```text id="qxfncx"
CAND-2026-019
```

Cubre:

```text id="zy4t1m"
preparar_con_advertencias
```

### Bloqueo

Debe comprobarse:

```text id="y4pkl5"
pedir_datos_adicionales_antes_de_redactar
→ candidatura detenida
→ no avanzar al guion
```

Puede usarse un caso controlado.

### No recomendada

Debe comprobarse:

```text id="z5u7ei"
no_recomendada
→ no iniciar producción documental normal
```

---

## 25. Resultado del gate

### Aprobado

```text id="tpfdfj"
GATE-CANDIDATURA-GUION: aprobado
```

Autoriza comenzar el diseño de:

```text id="kg2mfz"
PLAYBOOK_GUION_ADAPTACION_CV
```

### Bloqueado

Debe registrarse:

```text id="obp2lz"
id:
descripcion:
clasificacion:
criticidad:
evidencia:
impacto:
correccion_necesaria:
```

---

# PARTE IX — ESTADO REAL

## 26. Vía oferta

| Unidad | Estado |
| --- | --- |
| `PLAYBOOK_ANALISIS_OFERTA` | `en_prueba` |
| `TEMPLATE_ANALISIS_OFERTA` | `vigente` en `busqueda-empleo/proceso/plantillas` |
| `analisis-oferta.md` | `en_prueba` |
| `PLAYBOOK_CANDIDATURA` | `en_prueba` |
| `TEMPLATE_CANDIDATURA` | `vigente` en `busqueda-empleo/proceso/plantillas` |
| `candidatura.md` | `en_prueba` |
| `GATE-CANDIDATURA-GUION` | `aprobado` |
| `PLAYBOOK_GUION_ADAPTACION_CV` | `en_prueba` (candidata a validada) |
| `GATE-GUION-CV-CONTENIDO` | `aprobado` para CAND-2026-019 y CAND-2026-020 |
| `PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA` | `en_prueba`: validado técnicamente en fixtures y en CAND-2026-019/CAND-2026-020 |
| `datos-generacion.json` | `generado y validado técnicamente` para CAND-2026-019 y CAND-2026-020 |
| `GATE-CONTENIDO-CV-COMPOSICION` | `aprobado` para CAND-2026-019 y CAND-2026-020 |
| composición basada en JSON | `implantada y verificada técnicamente` en CAND-2026-019 y CAND-2026-020 |
| `PLAYBOOK_VEREDICTO_FINAL_CV` | `implantado y verificado técnicamente` |
| revisión humana CV | `completada` para CAND-2026-019 y CAND-2026-020 |
| veredictos actuales | `completados`: ASIC `no_competitivo`; Lidl `apto_para_presentacion` |
| `GATE-VEREDICTO-CV` | Lidl `aprobado`; ASIC `bloqueado` (2026-08-09) |
| `PLAYBOOK_GUION_CARTA_PRESENTACION` | Probado; CAND-2026-020 queda `apto` con la rama de carta cerrada |
| `PLAYBOOK_VEREDICTO_FINAL_CARTA` | `en_prueba`; CAND-2026-020 `APTA`, valor incremental medio, inclusión recomendada |
| `GATE-VEREDICTO-CARTA` | `aprobado` humanamente el 2026-08-10 para CAND-2026-020 |
| `PLAYBOOK_COMPONER_CV` | `vigente`; composición determinista desde el JSON 1.2 |
| `CAND-2026-020` | `documentalmente_completa`; CV y carta aprobados, `presentada: false` |
| presentación automatizada | `fuera_de_alcance_actual`; documentada como línea futura |

---

## 27. Vía empresa objetivo

| Unidad | Estado |
| --- | --- |
| análisis específico | `pendiente` |
| compatibilidad con `candidatura.md` | `pendiente` |
| canal de presentación | `pendiente` |
| paquete documental | `pendiente` |

---

# PARTE X — SIGUIENTE FASE

## 28. `PLAYBOOK_GUION_ADAPTACION_CV`

La fase entra en prueba después de:

```text id="m99zq2"
GATE-CANDIDATURA-GUION: aprobado
```

Objetivo:

> Convertir la estrategia común aprobada de `candidatura.md` en decisiones editoriales concretas y exclusivas para el CV.

Debe definir:

- instrucción editorial de CV;
- experiencia de apertura;
- logros prioritarios;
- evidencias;
- seniority;
- énfasis;
- omisiones;
- carencias;
- tono;
- palabras clave respaldadas;
- arquitectura de contenido;
- límites de redacción;
- brief de generación futuro para el CV.

No debe redactar todavía el contenido final, diseñar la carta de presentación, alterar la estrategia común, crear hechos,
diseñar JSON, composición, veredicto o envío.

El estado oficial de su gate de salida se registra por candidatura en
`evaluacion-gate-guion-cv-contenido.md`. La aprobación humana del gate no vive en el guion.

---

# PARTE XI — FASES FUTURAS

## 29. Generación de contenido del CV

```text id="zboik5"
GATE-GUION-CV-CONTENIDO
→
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
→ datos-generacion.json
```

`PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA` conserva su identificador arquitectónico histórico. En la rama actualmente
diseñada su alcance es exclusivamente el contenido del CV.

Su entrada será un `guion-adaptacion-cv.md` que haya superado `GATE-GUION-CV-CONTENIDO`. Su salida arquitectónica será
`datos-generacion.json`, que contendrá únicamente el contenido y los datos necesarios para el CV dentro de este flujo.
No contiene carta, no genera carta ni presupone campos, artefactos o una fase común CV/carta.

El contrato detallado del playbook y el schema físico de `datos-generacion.json` ya están diseñados, implantados y
validados técnicamente. La persona responsable aprobó los dos `GATE-CONTENIDO-CV-COMPOSICION` el 2026-08-07.
La composición CV-only ya está implantada y ejecutada en CAND-2026-020 y CAND-2026-019; las revisiones humanas se
registraron el 2026-08-08 y permitieron completar ambos veredictos actuales.

---

## 30. Necesidades candidatas del JSON

Formato:

```text id="5sh795"
ID: JSON-NEC-NNN
fase_origen:
caso_origen:
fecha:
necesidad:
motivo:
impacto_previsible:
estado: candidata
```

No forman parte todavía del schema.

---

## 31. Composición

Arquitectura futura por oferta:

```text id="wejhet"
datos-generacion.json
→ futura composición del CV
```

Salida objetivo:

```text id="ht7nfu"
cv.docx
cv.pdf
cv.tex
```

La composición del CV consume contenido ya decidido y redactado, sin reinterpretar estrategia. El flujo activo usa
`generar_candidatura.py` como orquestador técnico sobre el contrato JSON 1.2 y delega la representación en el modelo
intermedio pasivo compartido por DOCX y LaTeX.

La composición de carta sigue fuera de esta rama de composición del CV. Su módulo de guion ya está diseñado y probado por separado; la redacción y composición final requieren sus propios gates.

La composición CV-only implantada consume `contenido_cv` 1.2 mediante un modelo intermedio pasivo. DOCX y LaTeX
consumen ese mismo modelo; el texto se conserva literalmente y las colecciones se ordenan exclusivamente por
`orden`. El orquestador publica solo `cv.docx`, `cv.pdf` y `cv.tex`, conserva fotografía por defecto y reutiliza
resolución segura de rutas, bloqueo, conversión aislada, validación, publicación transaccional, restauración y logging.

La política de fotografía es específica por artefacto: el CV incluye fotografía
por defecto salvo exclusión humana expresa; la carta no incluye fotografía por
defecto y solo podría incorporarla mediante una decisión o configuración
humana expresa específica. La identidad visual compartida —nombre, título,
contacto autorizado, lenguaje visual y cabecera coherente— no obliga a duplicar
la fotografía. La autorización de disponer de una fotografía y la autorización
editorial para mostrarla son capas distintas.

Los datos privados no se solicitan ni se infieren durante la composición. Al iniciar cada candidatura, la persona
responsable debe resolver `autorizacion_datos_cv` para nombre, apellido 1, apellido 2, email, teléfono, LinkedIn,
ubicación y fotografía. La fase de contenido copia únicamente los campos autorizados desde
`datos-privados-candidatura.md`, mantiene trazabilidad independiente para nombre y apellidos y materializa la
decisión en `control.datos_privados`. Una autorización pendiente o una discordancia entre autorización y contenido
bloquea el generador.

La evidencia de implantación está documentada en
`docs/superpowers/specs/2026-08-08-compositor-cv-datos-generacion-1-2-design.md`, en
`scripts/job-up/componer_cv.py` y en las pruebas de compositor y generador CV-only.

### 31.1 Revisión humana y veredicto final del CV

La fase posterior a composición queda fijada así:

```text
cv.docx / cv.pdf / cv.tex
→ revisión humana del PDF
→ revision-humana-cv.md
→ PLAYBOOK_VEREDICTO_FINAL_CV v1.0.1
→ veredicto-final-cv.md
→ GATE-VEREDICTO-CV
```

`revision-humana-cv.md` es una decisión humana separada que identifica la
candidatura, el PDF revisado, su huella SHA-256, fecha, persona responsable y
`aprobado_para_veredicto` o `requiere_correccion`. El veredicto no se ejecuta si
falta la revisión, si la decisión requiere corrección o si la huella no coincide.

`PLAYBOOK_VEREDICTO_FINAL_CV` aplica dos roles: recruiter senior + coach de
carrera y auditor senior del flujo agentic. Evalúa integridad, fidelidad,
calidad recruiter mediante C1–C6, diagnóstico competitivo y enrutamiento por
capa. Sus salidas únicas son `bloqueado_por_integridad`,
`requiere_correccion_de_flujo`, `no_competitivo`,
`revisar_antes_de_presentar` y `apto_para_presentacion`, con la precedencia
documentada en el playbook. La media de puntuaciones nunca gobierna el resultado.

El veredicto solo recomienda `aprobar` o `no_aprobar` para `GATE-VEREDICTO-CV`.
Este gate valida exclusivamente el CV y no autoriza carta, email, formulario,
paquete de candidatura ni envío. La decisión del gate sigue siendo humana.
Una regeneración material invalida la revisión y el veredicto anteriores y
exige repetir la secuencia completa.

### 31.2 Cierre documental y presentación fuera de alcance

La aprobación de `GATE-VEREDICTO-CV` da paso a la rama independiente de carta
cuando la candidatura la requiere. La candidatura documental termina cuando
existen el CV final aprobado y la carta final aprobada cuando corresponda.

```text
GATE-VEREDICTO-CV
        ↓
PLAYBOOK_GUION_CARTA_PRESENTACION (si procede)
        ↓
PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION
        ↓
PLAYBOOK_COMPONER_CARTA_PRESENTACION
        ↓
GATE-VEREDICTO-CARTA
        ↓
CANDIDATURA DOCUMENTALMENTE COMPLETA
```

`GATE-CANDIDATURA-PRESENTACION`, `paquete-presentacion.md` y la validación de
canal no son precondiciones del cierre documental. La presentación externa,
incluidos portales, cuentas, formularios, credenciales, consentimientos y
envíos, queda fuera de esta arquitectura. `presentada` solo puede cambiar de
`false` a `true` tras una acción humana real y su evidencia, bajo un contrato
futuro independiente.

### 31.3 Veredicto final independiente de la carta

La carta mantiene una fase de veredicto propia, posterior a la composición y
a la aprobación humana de su representación:

```text
carta-presentacion.docx / carta-presentacion.pdf
→ GATE-CARTA-REVISION-HUMANA = aprobado
→ PLAYBOOK_VEREDICTO_FINAL_CARTA v1.0.0
→ veredicto-final-carta.md
→ GATE-VEREDICTO-CARTA
```

`PLAYBOOK_VEREDICTO_FINAL_CARTA` trabaja exclusivamente sobre la carta y
separa la calidad de la conveniencia de incluirla en el paquete. Usa tres
roles independientes —recruiter, responsable editorial/documental y auditor de
coherencia— y una síntesis determinista sin votación. Sus resultados son
`APTA`, `APTA_CON_RESERVAS` y `NO_APTA`; el valor incremental frente al CV y la
recomendación de inclusión se registran por separado.

`GATE-VEREDICTO-CARTA` requiere decisión humana y no se aprueba
automáticamente. `APTA` y `APTA_CON_RESERVAS` lo dejan en `pendiente`; `NO_APTA`
lo deja `bloqueado` hasta corregir en la fase responsable, propagar y repetir
el veredicto. Este gate no abre `GATE-CANDIDATURA-PRESENTACION` ni autoriza
presentación externa.

---

## 32. Veredicto

Debe evaluar en el futuro:

- factualidad;
- credibilidad;
- posicionamiento;
- primer escaneo;
- narrativa;
- coherencia;
- evidencia;
- privacidad;
- adecuación.

El veredicto final de carta queda definido por `PLAYBOOK_VEREDICTO_FINAL_CARTA`
v1.0.0, en prueba. La severidad se clasifica como `bloqueante`,
`reserva_relevante`, `reserva_menor` u `observacion`; la precedencia es
determinista y no utiliza puntuaciones ni mayoría.

---

# PARTE XII — DEFECTOS E INCERTIDUMBRES

## 33. Taxonomía de defectos

```text id="onzn1m"
CASO
PLAYBOOK
TEMPLATE
DATOS_CORE
ARQUITECTURA
COMPOSICION
```

Un defecto puede pertenecer a varias categorías.

---

### 33.1 Defectos arquitectónicos abiertos

#### DEF-ARQ-001 — Propagación de cambios factuales

- **Clasificación:** `ARQUITECTURA`.
- **Estado:** abierto.
- **Alcance:** únicamente candidaturas con `presentada: false`. Las candidaturas enviadas o presentadas conservan su carácter histórico y no se reescriben por evidencia descubierta posteriormente.
- **Problema:** la arquitectura no define todavía un contrato verificable para propagar una nueva evidencia factual desde `datos-core-busqueda.md` hacia los artefactos derivados de candidaturas no presentadas.
- **Evidencia:** `DEF-CAND-020-001` y `DEF-CAND-020-002`, registrados en la evaluación de `GATE-CANDIDATURA-GUION` de `CAND-2026-020`.
- **Impacto:** un análisis, una ficha de candidatura o una fase posterior pueden conservar una formulación obsoleta, omitir evidencia nueva o exigir reconstruir la estrategia desde un artefacto anterior.
- **Resolución necesaria:** definir el disparador de revisión, la localización de candidaturas afectadas, el orden de propagación (`datos-core` → análisis de origen → `candidatura.md` → fases posteriores), los estados de revisión y la verificación previa a reanudar el flujo.
- **Límite actual:** hasta que se resuelva, cualquier cambio factual relevante requiere una revisión manual de los expedientes no presentados que utilicen esa evidencia.

#### DEF-ARQ-002 — Frontera entre validación del CV y presentación de la candidatura

- **Clasificación:** `ARQUITECTURA`.
- **Estado:** resuelto en diseño e implantación; el paquete y la presentación quedan fuera del flujo vigente.
- **Alcance:** candidaturas con `presentada: false` que hayan superado la composición y el veredicto del CV.
- **Problema:** `GATE-VEREDICTO-CV-PRESENTACION` podía interpretarse como autorización de la candidatura completa aunque la carta, el email, el formulario, el canal y el paquete documental no estuvieran definidos.
- **Evidencia:** CAND-2026-020 tenía el CV validado y el gate aprobado, pero no disponía de carta, email de presentación ni paquete contractual del canal Indeed.
- **Resolución:** el gate activo pasa a llamarse `GATE-VEREDICTO-CV` y queda limitado al CV. El cierre vigente es documental: CV y carta finales aprobados cuando corresponda. No se exige `paquete-presentacion.md` ni `GATE-CANDIDATURA-PRESENTACION`; la presentación externa siempre la realiza la persona responsable.
- **Impacto operativo:** CAND-2026-020 permanece `documentalmente_completa` con `presentada: false`; CAND-2026-019 permanece `detenida` por su gate CV bloqueado.
- **Límite:** email, formularios y credenciales no forman parte del flujo vigente ni se ejecutan automáticamente.

---

## 34. Incertidumbres

Cuando un agente no pueda verificar algo necesario debe registrar:

```text id="bzw5lv"
ID: INC-NNN
elemento:
motivo:
impacto:
bloquea_plan: true|false
resolucion_necesaria:
```

Una incertidumbre no debe rellenarse mediante suposición.

### `INC-001` — Rama específica de carta diseñada y en prueba

```text
ID: INC-001
elemento: Arquitectura posterior de adaptación y generación de la carta de presentación.
motivo: ARQ-22 separa el adaptador de CV de la carta y exigía un módulo, guion y gate propios.
impacto: El paquete mínimo sigue incompleto hasta generar y revisar la carta, pero ya no falta el diseño del módulo.
bloquea_plan: true para GATE-CANDIDATURA-PRESENTACION; false para el CV-only.
resolucion_necesaria: Mantener la prueba del módulo, registrar la interacción humana y ejecutar la redacción posterior.
estado: resuelto_para_diseño; en_prueba
artefactos: PLAYBOOK_GUION_CARTA_PRESENTACION, TEMPLATE_GUION_CARTA_PRESENTACION.md, guion-carta-presentacion.md, GATE-GUION-CARTA-CONTENIDO
```

### `INC-002` — Semántica de `GATE-CANDIDATURA-GUION` para adaptadores adicionales

```text
ID: INC-002
elemento: Semántica y posible especialización por rama de GATE-CANDIDATURA-GUION.
motivo: El gate estaba probado inicialmente como entrada del adaptador de CV y la rama de carta necesitaba una decisión explícita sobre su reutilización.
impacto: Un gate de entrada específico de carta no existe ni debe inventarse sin una necesidad independiente.
bloquea_plan: false
resolucion_necesaria: Resuelto en la prueba del módulo de carta: `GATE-CANDIDATURA-GUION` es la entrada común para adaptadores documentales; cada rama conserva su gate de salida propio.
estado: resuelto_en_prueba
```

### `INC-003` — Alcance residual de `ARQ-09` y generación común

```text
ID: INC-003
elemento: Alcance residual de ARQ-09 — Redacción única y de las referencias previas a generación común CV/carta.
motivo: ARQ-22 impide interpretar ARQ-09 como obligación de una fase común CV/carta, pero el significado residual de ARQ-09 sigue sin definirse.
impacto: No se puede diseñar todavía una arquitectura de generación común. No bloquea el diseño de la fase de contenido exclusiva de CV.
bloquea_plan: false
resolucion_necesaria: Decidir el alcance residual de ARQ-09 antes de diseñar una infraestructura común CV/carta o la rama de carta.
```

### `INC-004` — Excepción contractual para omitir fotografía del CV

```text
ID: INC-004
elemento: Decisión inicial de exclusión de fotografía del CV y transporte determinista hasta el compositor CV-only.
motivo: La inclusión por defecto estaba decidida, pero faltaba un registro persistente de la decisión de datos privados y su transporte determinista hacia el compositor.
impacto: La inclusión predeterminada del CV queda resuelta y se aplica. La excepción sin fotografía del CV sigue bloqueada hasta que exista una decisión expresa registrada y aprobada para una candidatura concreta. La carta tiene una política independiente: sin fotografía por defecto.
bloquea_plan: true para la excepción sin fotografía del CV; false para la composición CV con fotografía y para la carta sin fotografía.
resolucion_necesaria: Resuelto el vacío del CV mediante `autorizacion_datos_cv.fotografia` en `candidatura.md`, materializado en `control.datos_privados` del JSON 1.2. El compositor CV exige actualmente `fotografia: incluir`; el compositor de carta no renderiza fotografía. No se implementan omisiones heurísticas ni inclusiones de fotografía en carta sin decisión específica.
```

---

## 35. Regla de generalización

Antes de modificar normativa:

1. detectar problema;
2. recopilar evidencia;
3. determinar si es específico;
4. identificar autoridad afectada;
5. cambiar únicamente esa capa.

Principio:

> Un caso puede descubrir un problema. No crea automáticamente una regla.

---

# PARTE XIII — CONTINUIDAD

## 36. Rehidratación mínima

Toda sesión o agente debe recuperar:

```text id="wc7sgf"
host
rama
SPEC referencia
estado-actual.md
sesión PCS vigente
vía actual
fase actual
estado_fase
gate_actual
estado_gate
casos_probados
defectos_abiertos
incertidumbres
siguiente_accion
```

---

## 37. Registro PCS recomendado

```text id="j0lydc"
via_actual:
fase_actual:
estado_fase:
gate_actual:
estado_gate:
casos_probados:
defectos_abiertos:
incertidumbres:
decisiones:
siguiente_accion:
```

---

# PARTE XIV — CONTRATO DE SALIDA DEL AGENTE PLANIFICADOR

## 38. Estructura mínima del plan

Un plan generado a partir de este SPEC debe contener:

### 38.1 Contexto verificado

- host;
- rama;
- estado actual;
- archivos existentes;
- discrepancias detectadas.

### 38.2 Objetivo

Qué cambio debe conseguir el plan.

### 38.3 Alcance

Qué incluye.

### 38.4 Fuera de alcance

Qué no debe tocar.

### 38.5 Precondiciones globales

Qué debe ser cierto antes de ejecutar.

### 38.6 Gates

Qué gates están abiertos y cuáles condicionan tareas.

### 38.7 Fases del plan

Ordenadas por dependencias.

### 38.8 Aprobaciones humanas

Puntos donde la ejecución debe detenerse.

### 38.9 Incertidumbres

Todas las `INC-NNN`.

### 38.10 Riesgos

Riesgos técnicos, documentales y funcionales.

### 38.11 Criterio de finalización

Qué evidencia permite considerar terminado el plan.

### 38.12 Trabajo futuro

Elementos conocidos pero fuera del alcance actual.

---

## 39. Estructura mínima de una tarea

Cada tarea implementable debe incluir:

```text id="1qodnd"
ID:
titulo:
objetivo:
justificacion:
precondiciones:
archivos_a_leer:
archivos_afectados:
accion:
resultado_esperado:
criterios_de_aceptacion:
verificacion:
dependencias:
gate_asociado:
aprobacion_humana:
```

No todas las tareas requieren modificación física de archivos.

---

## 40. Reglas de planificación

El agente debe:

- ordenar por dependencia, no por conveniencia;
- reutilizar artefactos existentes;
- minimizar cambios simultáneos;
- evitar rediseñar fases posteriores;
- distinguir corrección de implementación;
- incluir pruebas;
- incluir rollback o recuperación cuando sea relevante;
- señalar cualquier tarea que requiera decisión humana.

---

## 41. Regla de verificación del repositorio

Antes de proponer una tarea física:

> comprobar primero qué existe realmente.

Ejemplo:

Si la arquitectura dice:

```text id="f6sl8u"
adaptar generar_candidatura.py
```

el agente debe primero localizar:

```text id="1fvxzk"
generar_candidatura.py
```

y estudiar:

- responsabilidad actual;
- entradas;
- salidas;
- dependencias;
- pruebas existentes;

antes de decidir qué significa “adaptar”.

---

# PARTE XV — DECISIONES ARQUITECTÓNICAS

## 42. Registro vigente

### ARQ-01 — Arquitectura modular

Estado: `vigente`.

### ARQ-02 — Separación entre análisis y redacción

Estado: `vigente`.

### ARQ-03 — `candidatura.md` como ficha viva

Estado: `vigente`.

### ARQ-04 — Dos vías de entrada

Estado: `vigente`.

### ARQ-05 — Convergencia de empresa objetivo no asumida

Estado: `vigente`.

### ARQ-06 — Paquete documental espontáneo no definido

Estado: `vigente`.

### ARQ-07 — Guion antes de redacción final

Estado: `vigente`.

### ARQ-08 — Posicionamiento competitivo como requisito

Estado: `vigente`.

### ARQ-09 — Redacción única

Estado: `vigente`.

Su alcance residual no autoriza una fase de contenido común CV/carta; permanece delimitado por `INC-003`.

### ARQ-10 — JSON como frontera futura

Estado: `vigente`.

En la rama actualmente diseñada se interpreta como `contenido final del CV → datos-generacion.json → composición del
CV`; no convierte el JSON en artefacto común de CV/carta.

### ARQ-11 — Composición determinista

Estado: `vigente`.

La futura composición del CV debe consumir contenido ya decidido y redactado, sin reinterpretar la estrategia. Su
contrato continúa pendiente de diseño.

### ARQ-12 — Corrección por capa

Estado: `vigente`.

### ARQ-13 — Gates explícitos

Estado: `vigente`.

### ARQ-14 — Validación independiente por vía

Estado: `vigente`.

### ARQ-15 — Gate no equivale a validación completa

Estado: `vigente`.

### ARQ-16 — Aprobación humana

Estado: `vigente`.

### ARQ-17 — Aprendizaje transversal

Estado: `vigente`.

### ARQ-18 — Identificadores inequívocos

Estado: `vigente`.

### ARQ-19 — Verificación antes de planificación

El estado real del repositorio debe comprobarse antes de planificar cambios físicos.

Estado: `vigente`.

### ARQ-20 — Incertidumbre explícita

El agente no completa huecos mediante invención.

Estado: `vigente`.

### ARQ-21 — Planificación limitada por gates

No se convierten fases bloqueadas en tareas implementables.

Estado: `vigente`.

### ARQ-22 — Separación de responsabilidades CV/carta

`PLAYBOOK_GUION_ADAPTACION_CV` es exclusivo del CV. `candidatura.md` conserva la estrategia común para los distintos
adaptadores documentales. La carta de presentación utiliza un módulo independiente de guion, contenido y revisión.

Esta decisión prevalece sobre cualquier interpretación incompatible de ARQ-09 — Redacción única: ARQ-09 no puede
utilizarse para imponer un guion ni una fase de generación común CV/carta.

Estado: `vigente`.

### ARQ-24 — Política de fotografía específica por artefacto

La fotografía se gobierna por artefacto y no por una regla visual común:

```text
CV:
fotografía incluida por defecto, salvo exclusión humana expresa.

Carta:
sin fotografía por defecto; inclusión solo mediante decisión o configuración
humana expresa específica para esa carta.
```

La autorización de uso de la fotografía para el CV no implica autorización
editorial para mostrarla en la carta. La identidad visual compartida no obliga a
duplicar la fotografía. La futura configuración podrá representar decisiones
separadas para CV y carta, pero no se implementa en esta fase.

Estado: `vigente`.

### ARQ-23 — Paquete mínimo y presentación manual

Toda candidatura por oferta debe producir como mínimo un CV y una carta de
presentación, cada uno gobernado por su módulo y revisión propios. La
presentación en Indeed, LinkedIn, Lidl, Mercadona u otros portales la realiza
siempre la persona responsable. Job-up no autentica, introduce credenciales,
completa formularios, carga documentos ni envía candidaturas como parte del
flujo general.

Los requisitos adicionales del canal se registran cuando se conocen, pero no
pueden impedir la generación del paquete mínimo ni convertir la automatización
del portal en una dependencia del flujo.

Estado: `vigente`.

---

# PARTE XVI — TRABAJO ACTUAL

## 43. Situación

```text id="p2gpjn"
via_actual: oferta

fase_completada:
PLAYBOOK_VEREDICTO_FINAL_CV
→ veredicto-final-cv.md
→ PLAYBOOK_VEREDICTO_FINAL_CARTA
→ veredicto-final-carta.md

estado_fase_completada: implantada y verificada; CAND-2026-020 aprobado y CAND-2026-019 bloqueado en su gate CV

gate_completado:
GATE-VEREDICTO-CV

estado_gate: Lidl aprobado; ASIC bloqueado (2026-08-09)

fase_siguiente:
cerrar documentalmente CAND-2026-020 y mantener la presentación fuera de alcance

estado_fase_siguiente: `documentalmente_completa`; `presentada: false`; no se ha enviado la candidatura

caso_base:
CAND-2026-020
```

---

## 44. Próximo trabajo autorizado

La validación de entrada se completó con `CAND-2026-020`, un caso controlado de bloqueo y un caso controlado `no_recomendada`. La persona responsable aprobó explícitamente `GATE-CANDIDATURA-GUION` el 2026-08-05 para Lidl y el 2026-08-06 para ASIC. Tras regenerar los guiones conforme al contrato 1.0.1/2.1, ambos `GATE-GUION-CV-CONTENIDO` fueron reevaluados técnicamente y aprobados expresamente por la persona responsable el 2026-08-07.

El contrato de `PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA` y su plantilla 1.2 se validaron técnicamente mediante fixtures aislados. Los gates aprobados autorizaron la ejecución productiva para Lidl y ASIC. La composición CV-only se implantó y se ejecutó en ambos casos: generó `cv.docx`, `cv.pdf` y `cv.tex`, con fotografía incluida, una página y cobertura literal de los textos del JSON. Las revisiones humanas se registraron y los veredictos se completaron: Lidl `apto_para_presentacion` y ASIC `no_competitivo`. La rama de carta de CAND-2026-020 está compuesta, revisada humanamente y evaluada por `PLAYBOOK_VEREDICTO_FINAL_CARTA` v1.0.0 con resultado `APTA`, valor incremental `medio` y recomendación `incluir`; `GATE-VEREDICTO-CARTA` fue aprobado humanamente el 2026-08-10. CAND-2026-020 queda documentalmente completa y `presentada` permanece en `false`; los artefactos de presentación se conservan como línea futura.

---

## 45. Siguiente transición permitida

CAND-2026-020 ha alcanzado el cierre documental. No se abre ninguna fase de
presentación en este flujo. CAND-2026-019 permanece detenida por gate CV
bloqueado. La aprobación de un gate no equivale a un envío automático.

El gate de entrada ya satisfecho para la composición fue:

```text id="ivz6vq"
GATE-GUION-CV-CONTENIDO: aprobado
```

autoriza la ejecución productiva de:

```text id="q75fb4"
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
```

---

## 46. Trabajo todavía fuera de alcance

No debe planificarse todavía como implementación hasta que exista y se apruebe su contrato:

```text id="3iu8j1"
PLAYBOOK_ANALISIS_EMPRESA_OBJETIVO
presentación automatizada y validación de canales externos
entorno inicial de preguntas y configuración
decisiones separadas de fotografía por artefacto mediante futura configuración
```

Puede aparecer únicamente como:

- dependencia futura;
- riesgo;
- necesidad detectada;
- hito posterior.

---

# PARTE XVII — PROMOCIÓN DOCUMENTAL

## 47. Criterios

Un documento puede proponerse para promoción cuando:

1. tiene responsabilidad inequívoca;
2. no contiene términos esenciales sin definir;
3. no depende de contexto conversacional para entenderse;
4. sus entradas y salidas están claras;
5. ha sido probado cuando corresponda;
6. no tiene defectos críticos abiertos;
7. no contradice decisiones `ARQ`;
8. un agente puede utilizarlo sin inventar decisiones;
9. se conoce su futura autoridad y ubicación.

---

# PARTE XVIII — RESUMEN EJECUTIVO

## 48. Arquitectura objetivo

```text id="rkjclj"
analisis-oferta.md
↓
candidatura.md
↓
GATE-CANDIDATURA-GUION
↓
guion-adaptacion-cv.md
↓
GATE-GUION-CV-CONTENIDO
↓
datos-generacion.json
↓
composición CV-only
↓
GATE-VEREDICTO-CV
↘
PLAYBOOK_GUION_CARTA_PRESENTACION
↓
guion-carta-presentacion.md → carta revisada
↓
PLAYBOOK_VEREDICTO_FINAL_CARTA
↓
veredicto-final-carta.md → GATE-VEREDICTO-CARTA
↓
CANDIDATURA DOCUMENTALMENTE COMPLETA
```

---

## 49. Estado actual

```text id="467hma"
PLAYBOOK_CANDIDATURA [oferta]
→ en_prueba

GATE-CANDIDATURA-GUION
→ aprobado

PLAYBOOK_GUION_ADAPTACION_CV
→ en_prueba (candidata a validada)

GATE-GUION-CV-CONTENIDO
→ aprobado

PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
→ en_prueba (contenido productivo generado y validado técnicamente)

GATE-CONTENIDO-CV-COMPOSICION
→ aprobado para CAND-2026-019 y CAND-2026-020

PLAYBOOK_VEREDICTO_FINAL_CV
→ implantado y verificado técnicamente

GATE-VEREDICTO-CV
→ Lidl aprobado; ASIC bloqueado

PLAYBOOK_GUION_CARTA_PRESENTACION
→ probado; CAND-2026-020 apto y con gate de contenido aprobado; carta revisada humanamente

PLAYBOOK_VEREDICTO_FINAL_CARTA
→ en_prueba; CAND-2026-020 `APTA`, valor incremental `medio`, recomendación `incluir`

GATE-VEREDICTO-CARTA
→ aprobado humanamente el 2026-08-10 para CAND-2026-020

CAND-2026-020
→ documentalmente completa; `presentada: false`

PRESENTACIÓN AUTOMATIZADA / UI DE CONFIGURACIÓN
→ fuera de alcance; líneas futuras independientes
```

---

## 50. Regla principal para humanos

> No avanzar porque el documento parezca correcto. Avanzar cuando exista evidencia suficiente de que el traspaso funciona.

---

## 51. Regla principal para agentes

> Verificar antes de asumir. Planificar solo aquello que los gates actuales permiten. Registrar incertidumbre en lugar de inventar.

---

## 52. Regla de calidad profesional

> Una candidatura debe ser simultáneamente verdadera, relevante, competitiva y defendible en entrevista.

---

## 53. Regla arquitectónica

> El contenido se corrige en la capa que produce contenido. La composición se corrige en la capa técnica.

---

## 54. Cierre arquitectónico documental — 2026-08-11

Esta sección fija el estado vigente de la arquitectura y prevalece sobre los
registros históricos anteriores que describían la presentación como fase de
cierre.

### Fin del alcance actual

```text
oferta
→ análisis
→ candidatura
→ CV (guion → contenido → composición → revisión/veredicto)
→ carta, si la candidatura la requiere
   (guion → contenido → composición → revisión/veredicto)
→ candidatura documentalmente completa
→ fin del alcance actual
```

La candidatura documentalmente completa exige el CV final aprobado y la carta
final aprobada cuando sea requerida. No exige `paquete-presentacion.md`,
`GATE-CANDIDATURA-PRESENTACION` ni evaluación de un portal. `presentada` sigue
siendo un hecho externo y permanece en `false` hasta que la persona responsable
realice una presentación real bajo un contrato futuro.

### Ubicaciones canónicas

- Playbooks operativos: `docs/metodologia/playbooks/`.
- Templates operativos de Job-up:
  `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/`.
- Scripts: `scripts/job-up/`.
- Diseños y contratos experimentales: `docs/ideas-y-debates/mejoras-job-up/`.
- Presentación futura: `docs/ideas-y-debates/mejoras-job-up/futuro/presentacion/`.

### Líneas futuras separadas

1. Entorno inicial de preguntas/configuración: descubrir opciones, aplicar
   defaults y persistir decisiones; no se implementan UI, wizard ni campos
   nuevos en esta fase.
2. Presentación automatizada asistida por IA: navegación supervisada,
   formularios y envío bajo contrato específico; no se implementa en el flujo
   vigente.

### Caso de referencia

`CAND-2026-020` queda `documentalmente_completa`, con CV y carta aprobados y
`presentada: false`. `CAND-2026-019` continúa detenida por su gate CV
bloqueado. No se abre una sesión PCS nueva ni se realiza integración Git en este
cierre.

### Política de fotografía — cierre contractual 2026-08-11

La decisión arquitectónica vigente distingue la representación de fotografía
por artefacto:

```text
CV:
fotografía incluida por defecto, salvo exclusión humana expresa.

Carta:
sin fotografía por defecto; inclusión solo mediante decisión o configuración
humana expresa específica para esa carta.
```

La autorización `control.datos_privados.autorizacion.fotografia = incluir`
confirma que la fotografía está disponible y autorizada para el CV; no implica
mostrarla automáticamente en la carta. La identidad visual compartida no
obliga a duplicar la fotografía. La carta actual de CAND-2026-020, sin
fotografía, es conforme y conserva su veredicto `APTA`, su gate aprobado y el
estado `documentalmente_completa`.

---

## 55. Reglas consolidadas tras la prueba E2E de CAND-2026-021 — 2026-08-11

Estas reglas forman parte del contrato vigente y no son un registro de
incidencias:

1. **Fotografía del CV:** la fotografía es un recurso técnico privado incluido
   por defecto. La ausencia de mención no genera pregunta, pendiente ni
   bloqueo; solo una exclusión humana expresa cambia el valor a `omitir`. La
   carta mantiene su política independiente sin fotografía por defecto.
2. **Datos reutilizables y decisiones:** los hechos profesionales reutilizables
   (como `vehículo propio`) se conservan en Data Core; las preferencias
   generales (como la movilidad territorial) se distinguen de la decisión
   concreta de una oferta. Un requisito relevante sin evidencia se resuelve
   antes de `GATE-CANDIDATURA-GUION`.
3. **Contexto corporativo:** tras identificar la empresa, el contexto cultural
   útil se localiza o solicita antes de cerrar decisiones afectadas. Es contexto
   con procedencia, nunca evidencia ni afinidad personal del candidato.
4. **Transiciones:** gate aprobado + siguiente acción determinista + ausencia
   de dato, decisión, revisión humana o acción irreversible implica continuidad
   automática al siguiente playbook. Las excepciones se detienen y registran.
5. **Composición de carta:** las líneas físicas consecutivas no vacías del
   Markdown forman un único párrafo semántico; la línea vacía separa párrafos.
   No se generan saltos manuales de Word por hard wrapping. Fecha y asunto se
   derivan solo de datos confirmados y la jerarquía vigente es nombre 18 pt,
   titular 11 pt, contacto 10,5 pt y cuerpo 11 pt justificado.
6. **Inspección visual:** `render_generado` y `render_inspeccionado` son estados
   distintos. No se declara `revision_visual: ejecutada` sin evidencia de
   inspección real de los PNG/renderizados. La comprobación automática no
   sustituye la revisión humana.
7. **Cierre:** la aprobación de CV y carta deja la candidatura
   `documentalmente_completa` con `presentada: false` y sin módulo activo
   posterior. La presentación externa y sus artefactos siguen en la línea
   futura, bajo responsabilidad de la persona usuaria.

---

# Changelog

## Separación contractual de fotografía CV/carta — 2026-08-11

- se formaliza `ARQ-24` para separar la política de fotografía por artefacto;
- el CV mantiene fotografía por defecto salvo exclusión humana expresa;
- la carta queda sin fotografía por defecto y sin renderizado automático;
- se alinean el playbook operativo, la guía de formato y la plantilla de carta;
- no se modifica el compositor de carta ni se regenera CAND-2026-020.

## Cierre arquitectónico y reorganización documental — 2026-08-11

- se cierra el alcance vigente en la generación y validación de artefactos
  documentales;
- se promocionan los playbooks y templates maduros a sus ubicaciones canónicas;
- se reclasifican los artefactos de presentación como línea futura/experimental;
- CAND-2026-020 pasa a `documentalmente_completa` con `presentada: false`;
- se documentan por separado las líneas futuras de configuración y presentación
  automatizada;
- no se implementan UI, navegador, formularios, credenciales ni envíos.

## Registro histórico: validación operativa de presentación — 2026-08-11

- se incorporan `PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA` y
  `TEMPLATE_EVALUACION_PRESENTACION_CANDIDATURA`, ambos v1.0.0 en `en_prueba`;
- se abre `GATE-CANDIDATURA-PRESENTACION` en `pendiente` para CAND-2026-020 el 2026-08-11;
- la primera evaluación real resulta `APTA_CON_PENDIENTES_HUMANOS` por cuenta,
  credenciales, preferencias de privacidad y campos obligatorios del portal;
- `presentada` permanece en `false` y no se realiza ningún envío.

## Aprobación humana del veredicto final de carta — 2026-08-10

- se registró `GATE-VEREDICTO-CARTA` como `aprobado`, con decisión humana
  aprobada y fecha 2026-08-10;
- se mantuvieron `APTA`, el valor incremental `medio` y la recomendación
  `incluir`;
- la rama documental de carta queda cerrada y el paquete pasa a
  `listo_para_gate`;
- `GATE-CANDIDATURA-PRESENTACION` continúa sin abrir y no se ha realizado
  ningún envío.

## Corrección de propagación y regeneración del veredicto de carta — 2026-08-10

- se propagó a la evaluación directa la decisión humana ya existente de
  `GATE-CARTA-REVISION-HUMANA` (`aprobado`, 2026-08-10);
- se regeneró completamente `veredicto-final-carta.md` para CAND-2026-020;
- el caso obtuvo `APTA`, valor incremental `medio`, recomendación `incluir` y
  `GATE-VEREDICTO-CARTA` `pendiente` de decisión humana;
- `GATE-CANDIDATURA-PRESENTACION` continúa cerrado y no se ha realizado ningún
  envío.

## Veredicto final independiente de carta — 2026-08-10

- se incorpora `PLAYBOOK_VEREDICTO_FINAL_CARTA` v1.0.0 y
  `TEMPLATE_VEREDICTO_FINAL_CARTA`, ambos en `en_prueba`;
- se formaliza `GATE-VEREDICTO-CARTA`, separado de la revisión humana y del
  gate de presentación;
- se intenta probar CAND-2026-020, pero la fuente directa de la revisión humana
  sigue en `pendiente` mientras los resúmenes declaran `aprobado`; el caso
  queda bloqueado y no emite resultado competitivo;
- el gate completo sigue sin abrirse y `presentada` permanece en `false`.

## 0.4.0 — 2026-08-04

Revisión orientada simultáneamente a lectura humana y planificación por agentes de IA.

Cambios principales:

- se añade contrato explícito del agente planificador;
- se define que la salida esperada es un plan y no implementación;
- se obliga a verificar el repositorio antes de planificar cambios;
- se añade jerarquía de autoridad entre SPEC, playbooks, templates y fuentes factuales;
- se introduce política explícita de contradicciones;
- se introduce política de incertidumbre `INC-NNN`;
- se añade glosario normativo;
- se distinguen tesis, posicionamiento y gancho;
- se sustituye definitivamente `CAND-O1` por `GATE-CANDIDATURA-GUION`;
- se establece convención formal de identificadores;
- se prohíbe reutilizar el prefijo `CAND` para otras entidades;
- se aclara que gate aprobado no implica fase completamente validada;
- se incorpora patrón obligatorio de contrato de fase;
- se introducen precondiciones y postcondiciones;
- se formaliza el contrato de salida del agente planificador;
- se formaliza la estructura mínima de cada tarea;
- se prohíbe convertir fases bloqueadas por gates en tareas de implementación;
- se refuerzan los criterios de promoción documental;
- se mantiene `GATE-CANDIDATURA-GUION` como único gate operativo inmediato;
- se mantiene `PLAYBOOK_GUION_ADAPTACION_CV` como siguiente fase permitida.

## Sincronización de contrato CV — 2026-08-06

- se incorpora ARQ-22 para separar responsabilidades de CV y carta;
- se registran INC-001, INC-002 e INC-003 sin resolverlas por anticipación;
- el pipeline del guion queda limitado al CV y registra `GATE-GUION-CV-CONTENIDO`;
- `PLAYBOOK_GUION_ADAPTACION_CV` pasa a `en_prueba`; tras los casos completos `CAND-2026-020` y `CAND-2026-019`, su implantación queda **candidata a validada**. La regeneración posterior conforme al contrato 1.0.1/2.1 exigió una nueva decisión humana de ambos `GATE-GUION-CV-CONTENIDO`, aprobados el 2026-08-07;
- `DEF-ARQ-001` se mantiene abierto sin modificar su resolución necesaria.

## Corrección de frontera de contenido CV — 2026-08-06

- se aclara que `PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA` tiene alcance exclusivamente CV en la arquitectura actual;
- se fija `datos-generacion.json` como salida estructurada del contenido del CV y frontera con su futura composición;
- se elimina la inferencia de que el mismo JSON o la misma fase producen la carta;
- se corrige la composición para mantener la carta bajo `INC-001`;
- el validador distingue el metadato normativo `GATE-CONTENIDO-CV-COMPOSICION`, exigido por la plantilla, del contenido visible del CV: la prohibición de carta o composición se aplica a los textos que consumirá el CV, no al nombre del gate de salida.
- la plantilla declara `refs_guion` en cada uso de léxico condicionado, porque el validador exige trazabilidad completa entre el término, la decisión editorial y el contenido materializado.
- el contrato detallado del playbook y la plantilla JSON 1.2 se validan técnicamente mediante casos positivos, negativos y un compositor pasivo; se generan y validan los dos JSON productivos de Lidl y ASIC, cuyos `GATE-CONTENIDO-CV-COMPOSICION` fueron aprobados el 2026-08-07; la composición CV-only se ejecuta el 2026-08-08 con tres artefactos por caso.
- el veredicto final CV-only se sitúa después de la composición y exige revisión humana con huella antes de evaluar; no se reutiliza el veredicto histórico de CAND-2026-019.

## Sincronización de composición CV-only — 2026-08-08

- se documenta y aprueba para implantación la alternativa 3: adaptación del generador histórico reutilizando su infraestructura técnica;
- se crea un modelo intermedio pasivo común para DOCX y LaTeX, alimentado exclusivamente por `contenido_cv` 1.2;
- el generador activo deja de producir carta y publica solo `cv.docx`, `cv.pdf` y `cv.tex`;
- se verifican los casos reales CAND-2026-020 y CAND-2026-019, con textos completos, orden declarado, fotografía incluida y una página por CV;
- la fotografía queda incluida por defecto por decisión humana;
- `INC-004` queda resuelto en su vacío contractual: `candidatura.md` ya registra `autorizacion_datos_cv.fotografia` y el JSON 1.2 transporta la decisión. La inclusión por defecto está implantada; la omisión continúa bloqueada salvo decisión expresa y aprobada;
- se incorpora el contrato de datos privados para ambos casos: nombre y apellido 1 incluidos; apellido 2, LinkedIn y ubicación omitidos; email y teléfono incluidos;
- se regeneran CAND-2026-020 y CAND-2026-019 con datos privados autorizados, fotografía incluida, una página por CV y sin envío externo;
- la revisión humana de los artefactos generados quedó completada; el módulo independiente de carta permanece pendiente.

## Sincronización del veredicto final CV — 2026-08-08

- se promueve `PLAYBOOK_VEREDICTO_FINAL_CV` a versión 1.0.1 y se incorporan
  `TEMPLATE_VEREDICTO_FINAL_CV` y `TEMPLATE_REVISION_HUMANA_CV` como contratos
  vigentes;
- se implementa la validación técnica de huella SHA-256, precondiciones,
  privacidad y precedencia de resultados en `scripts/job-up/verificar_veredicto_final_cv.py`;
- el veredicto histórico de CAND-2026-019 se conserva bajo `historico/` y no se
  reutiliza para el CV actual;
- las revisiones humanas de CAND-2026-019 y CAND-2026-020 se registran con
  `aprobado_para_veredicto` y huellas SHA-256 coincidentes;
- los veredictos actuales quedan completados: ASIC `no_competitivo` con
  recomendación `no_aprobar`, y Lidl `apto_para_presentacion` con recomendación
  `aprobar`;
- el gate CV, entonces denominado `GATE-VEREDICTO-CV-PRESENTACION`, de
  CAND-2026-020 queda `aprobado` y el de CAND-2026-019 queda `bloqueado`, ambos
  por decisión humana del 2026-08-09; la denominación queda deprecada por
  `DEF-ARQ-002`;
- no se ha realizado ningún envío.

## Sincronización de la frontera CV → candidatura completa — 2026-08-09

- se registra `DEF-ARQ-002` por la ambigüedad entre validar el CV y autorizar la
  presentación de la candidatura completa;
- `GATE-VEREDICTO-CV` sustituye como denominación activa a
  `GATE-VEREDICTO-CV-PRESENTACION` y queda limitado al CV;
- se define `paquete-presentacion.md` como inventario del canal y de los
  artefactos requeridos;
- se introduce `GATE-CANDIDATURA-PRESENTACION` como gate independiente para el
  paquete completo;
- `scripts/job-up/verificar_paquete_presentacion.py` valida de forma determinista
  el paquete incompleto y la evidencia mínima de un envío real;
- CAND-2026-020 conserva su CV aprobado, pero vuelve a `en_preparacion` porque
  todavía no tiene carta ni paquete mínimo completo; email y formularios quedan
  bajo responsabilidad de la persona responsable;
- CAND-2026-019 permanece detenida por su gate CV bloqueado;
- no se ha realizado ningún envío ni se ha cambiado `presentada` a `true`.

## Sincronización del paquete mínimo y presentación manual — 2026-08-09

- se incorpora `ARQ-23`: toda candidatura debe producir como mínimo CV y carta;
- la carta mantiene módulo, guion, revisión y gate propios, separados del CV;
- los formularios, credenciales y pasos específicos de Indeed, LinkedIn, Lidl,
  Mercadona u otros portales quedan bajo responsabilidad de la persona
  responsable y fuera de la automatización general;
- `GATE-CANDIDATURA-PRESENTACION` pasa a validar la existencia y revisión del
  paquete mínimo, no la ejecución de un formulario externo;
- la transición a `presentada: true` requiere evidencia aportada después de que
  la persona responsable realice manualmente la presentación;
- CAND-2026-020 queda pendiente del diseño y generación de su carta, no de la
  auditoría del formulario de Lidl.

## Prueba del módulo de guion de carta — 2026-08-09

- se completa el diseño de `PLAYBOOK_GUION_CARTA_PRESENTACION` y
  `TEMPLATE_GUION_CARTA_PRESENTACION.md`, manteniendo la estrategia común en
  `candidatura.md` y la separación respecto del CV;
- se generan y evalúan `guion-carta-presentacion.md` y
  `evaluacion-gate-guion-carta-contenido.md` para CAND-2026-020;
- el contrato supera las pruebas T1–T9, incluido el caso sintético de empresa
  anónima, y queda `apto_para_implantacion`;
- CAND-2026-020 queda `apto`: el usuario declaró que no tiene motivación
  personal ni relación previa con Lidl y autorizó consultar la URL oficial de
  empleo, que fue leída el 2026-08-09;
- la carta final, su composición y el gate de candidatura completa permanecen
  pendientes de la siguiente fase y de la revisión humana.
- se resuelve `INC-002` en la prueba: la carta reutiliza el gate de entrada común
  `GATE-CANDIDATURA-GUION` y no se crea un gate de entrada específico no definido.
