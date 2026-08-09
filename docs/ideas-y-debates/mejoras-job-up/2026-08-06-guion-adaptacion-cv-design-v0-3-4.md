---
id: design-playbook-guion-adaptacion-cv
titulo: Diseño — PLAYBOOK_GUION_ADAPTACION_CV
version: 0.3.4
sustituye: "0.3.3"
aprobacion_humana_diseno: pendiente
fecha_version: 2026-08-06
host: carrera-ai
rama: job-up
tipo_documento: diseño_de_fase
fase: PLAYBOOK_GUION_ADAPTACION_CV
artefacto_salida: guion-adaptacion-cv.md
gate_entrada: GATE-CANDIDATURA-GUION
gate_salida: GATE-GUION-CV-CONTENIDO
caso_principal: CAND-2026-020
caso_contraste: CAND-2026-019
spec_referencia: SPEC-Arquitectura-modular-generación-candidatura-v0-4-0.md
defectos_relacionados:
  - DEF-ARQ-001
decision_arquitectonica_propuesta_spec:
  - ARQ-22
incertidumbres_propuestas_spec:
  - INC-001
  - INC-002
  - INC-003
audiencias:
  - humano
  - agente_ia_planificador
  - agente_ia_ejecutor
---
# Diseño — `PLAYBOOK_GUION_ADAPTACION_CV`

## 1. Propósito

`PLAYBOOK_GUION_ADAPTACION_CV` transforma la estrategia común ya aprobada de una candidatura en **decisiones editoriales específicas para el CV**.

Produce:

`guion-adaptacion-cv.md`

Ese artefacto debe permitir que una fase posterior pueda generar el contenido del CV sin tener que:

- volver a interpretar la oferta;
- volver a decidir si merece la pena competir;
- reconstruir el posicionamiento;
- reinterpretar carencias;
- seleccionar desde cero qué trayectoria mostrar;
- volver a decidir qué evidencias sostienen el encaje.

El guion:

- no es un borrador de CV;
- no redacta el CV final;
- no diseña visualmente el CV;
- no genera DOCX, PDF o LaTeX;
- no redefine la estrategia;
- no modifica hechos.

Su pregunta central es:

> Dada una estrategia de candidatura ya aprobada, ¿qué parte verdadera de la trayectoria profesional debe mostrar este CV, con qué importancia, para demostrar qué, en qué orden y bajo qué límites?

---

# 2. Posición dentro de la arquitectura

El flujo relevante es:

```text
datos-core-busqueda.md
        ↓
analisis-oferta.md
        ↓
candidatura.md
        ↓
GATE-CANDIDATURA-GUION
        ↓
PLAYBOOK_GUION_ADAPTACION_CV
        ↓
guion-adaptacion-cv.md
        ↓
GATE-GUION-CV-CONTENIDO
        ↓
futura fase de generación de contenido del CV
        ↓
CV
```

Responsabilidades:

```text
candidatura.md
→ estrategia común de candidatura

guion-adaptacion-cv.md
→ adaptación editorial específica del CV
```

`guion-adaptacion-cv.md` no sustituye a `candidatura.md`.

No constituye una segunda fuente estratégica.

---

# 3. Separación de responsabilidades CV/carta

La separación entre CV y carta es una **decisión arquitectónica de este diseño**, no una incertidumbre.

La próxima actualización de la SPEC deberá promoverla como decisión `ARQ`.

Identificador propuesto, sujeto a revalidación de numeración en el momento de actualizar la SPEC:

```text
ARQ-22 — Separación de responsabilidades CV/carta

PLAYBOOK_GUION_ADAPTACION_CV es exclusivo del CV.

candidatura.md conserva la estrategia común de candidatura
para los distintos adaptadores documentales.

La existencia futura de un adaptador específico de carta no modifica
la responsabilidad de PLAYBOOK_GUION_ADAPTACION_CV.

Ninguna interpretación de ARQ-09 — Redacción única puede utilizarse
para exigir que CV y carta compartan este adaptador ni una única fase
de generación de contenido.

El alcance residual de ARQ-09 fuera de esta restricción permanece
pendiente de definición y se registra como INC-003.

Estado de la decisión en este diseño: adoptada.
Estado en la SPEC: pendiente de promoción.
```

La rama concreta de carta continúa deliberadamente sin diseñar.

Ese aplazamiento se registra como `INC-001`.

También permanecen abiertas:

- `INC-002`: semántica futura del gate genérico `GATE-CANDIDATURA-GUION` cuando existan varios adaptadores;
- `INC-003`: alcance residual de `ARQ-09` y de las referencias actuales de la SPEC a generación o convergencia común CV/carta.

Las tres incertidumbres:

- `bloquea_plan: false` para el guion de CV;
- no autorizan a Work a resolverlas silenciosamente;
- deben resolverse en la capa indicada por su registro.

---

# 4. Contrato normativo de fase

Esta sección es la **fuente normativa canónica** del contrato de fase.

Las secciones posteriores desarrollan estos campos, pero no pueden contradecirlos ni introducir responsabilidades nuevas por inferencia.

## OBJETIVO

Traducir una estrategia de candidatura aprobada a un mapa editorial específico del CV, completo, factual, competitivo, trazable y suficientemente determinista para habilitar la fase posterior.

## PRECONDICIONES

- `GATE-CANDIDATURA-GUION: aprobado`;
- `candidatura.md` existente y vigente;
- `analisis-oferta.md` resoluble;
- fuentes factuales autorizadas resolubles;
- ausencia de bloqueo activo;
- para ejecución operativa, `presentada: false`;
- una candidatura presentada solo puede utilizarse en prueba retrospectiva controlada, claramente marcada y sin reescribir su expediente histórico;
- la arquitectura normativa vigente no debe contener una contradicción bloqueante con este diseño una vez aprobado.

## ENTRADAS

Entrada principal:

- `candidatura.md`.

Referencias autorizadas:

- `datos-core-busqueda.md`;
- `analisis-oferta.md`;
- evidencias factuales referenciadas por la candidatura.

No forman parte de las entradas por defecto:

- investigación externa nueva;
- información corporativa no aprobada;
- inferencias no registradas;
- recuerdos de conversaciones sin trazabilidad documental.

## RESPONSABILIDADES

- seleccionar contenido profesional;
- decidir presencia;
- decidir obligatoriedad;
- asignar peso editorial;
- decidir función estratégica;
- ordenar contenido;
- definir nivel de detalle;
- relacionar contenido con criterios de selección;
- asegurar cobertura de prioridades estratégicas;
- trasladar advertencias a límites de redacción;
- definir tratamiento de seniority;
- definir tono editorial del CV;
- construir arquitectura editorial;
- gobernar el primer escaneo;
- limitar duplicación y ruido;
- producir un brief cerrado y derivado.

## FUERA_DE_RESPONSABILIDAD

- cambiar estrategia;
- modificar hechos;
- incorporar evidencia nueva directamente;
- decidir arquitectura de carta;
- resolver `DEF-ARQ-001`;
- resolver el alcance residual de `ARQ-09`;
- redactar CV final;
- diseñar presentación visual;
- generar formatos finales;
- enviar candidatura.

## SALIDA

`guion-adaptacion-cv.md`

## POSTCONDICIONES

La fase siguiente debe conocer de forma explícita:

- qué incluir;
- qué omitir;
- qué conservar obligatoriamente;
- qué priorizar;
- qué minimizar;
- qué demostrar;
- qué evitar;
- qué tono editorial aplicar;
- cómo tratar el seniority;
- qué límites respetar;
- qué estructura narrativa seguir.

No debe necesitar reconstruir la estrategia.

## DEFECTOS_CRITICOS

Son críticos, entre otros:

- invención factual;
- reinterpretación estratégica;
- pérdida de trazabilidad;
- omisión engañosa;
- falsa experiencia;
- alteración engañosa de cronología;
- tratamiento de seniority que falsee trayectoria;
- propagación factual asumida sin contrato arquitectónico;
- pérdida silenciosa de una prioridad estratégica;
- brief que contradiga el cuerpo;
- estado del gate almacenado de forma que convierta el guion en fuente mutable de gobierno del gate;
- aprobación automática del gate por IA;
- avance a una fase posterior aún no diseñada como si ya fuera ejecutable.

`DEF-ARQ-001` permanece como defecto arquitectónico abierto relacionado.

## GATE_SIGUIENTE

`GATE-GUION-CV-CONTENIDO`

## CRITERIOS_DE_ACEPTACION

Los definidos en la sección 19.

---

# 5. Principio de responsabilidad

El guion puede tomar:

> decisiones editoriales.

No puede tomar:

> decisiones estratégicas de candidatura.

Frontera:

```text
candidatura.md
→ qué queremos demostrar y desde qué posicionamiento

guion-adaptacion-cv.md
→ qué contenido verdadero del CV debe hacerlo visible y con qué jerarquía
```

Si para construir el guion resulta necesario cambiar:

- la razón para competir;
- el posicionamiento;
- una evidencia estratégica;
- una afirmación excluida;
- una carencia;
- un riesgo;
- un límite;

el problema pertenece a una fase anterior.

---

# 6. Autoridad de las fuentes

## 6.1 `candidatura.md` — autoridad estratégica

Gobierna:

- decisión estratégica;
- tesis;
- ángulo;
- posicionamiento;
- evidencias prioritarias;
- advertencias;
- carencias;
- afirmaciones excluidas;
- límites;
- bloqueos;
- estado operativo pertinente.

El guion no puede sustituir ni modificar estas decisiones.

---

## 6.2 `datos-core-busqueda.md` — autoridad factual

Gobierna la factualidad profesional.

Puede aportar:

- experiencias;
- cargos;
- fechas;
- responsabilidades;
- funciones;
- logros;
- resultados;
- métricas;
- herramientas;
- tecnologías;
- formación;
- certificaciones;
- competencias demostradas;
- cronología;
- otros hechos profesionales autorizados.

Que un dato exista en el core no implica que deba aparecer en el CV.

El guion decide su tratamiento editorial.

---

## 6.3 `analisis-oferta.md` — contexto y trazabilidad

Puede utilizarse para:

- requisitos;
- responsabilidades;
- señales de selección;
- contexto de la oferta;
- relación entre requisitos y evidencias;
- comprobación de trazabilidad.

No puede emplearse para reabrir silenciosamente la estrategia ya fijada en `candidatura.md`.

---

## 6.4 Investigación externa

El guion no inicia investigación externa por sí mismo.

Si una investigación corporativa o sectorial ya fue aprobada, validada y propagada a las fuentes autorizadas del caso, podrá consumir sus efectos.

No puede incorporar directamente información externa nueva para:

- cambiar el tono;
- introducir palabras clave;
- reinterpretar la empresa;
- modificar posicionamiento.

---

## 6.5 Conflicto entre autoridades

Ante una contradicción real entre:

```text
datos-core-busqueda.md
vs
analisis-oferta.md
vs
candidatura.md
```

el guion debe:

1. detener la decisión afectada;
2. identificar qué autoridad debe resolverla;
3. registrar la incidencia;
4. no escoger la interpretación más conveniente.

---

# 7. Validación de precondiciones

La lista normativa de precondiciones es exclusivamente la de la sección 4.

Esta sección define cómo se valida.

El agente debe comprobar:

1. existencia del gate de entrada;
2. decisión humana `aprobado`;
3. existencia y legibilidad de `candidatura.md`;
4. resolución del análisis y fuentes factuales;
5. ausencia de bloqueo;
6. estado `presentada`;
7. vigencia operativa de la candidatura.

Si falla una precondición obligatoria:

```text
PLAYBOOK_GUION_ADAPTACION_CV
→ no inicia
```

La aprobación del gate de entrada no autoriza:

- generar el CV;
- generar la carta;
- presentar la candidatura;
- alterar el estado a `presentada`.

---

# 8. Qué puede decidir

Esta sección desarrolla `RESPONSABILIDADES` sin ampliar su alcance.

El playbook puede:

- construir el universo candidato de contenido;
- seleccionar contenido;
- omitir contenido;
- definir obligatoriedad;
- asignar peso editorial;
- definir función estratégica;
- jerarquizar experiencias;
- jerarquizar logros;
- jerarquizar competencias;
- seleccionar evidencia de apertura;
- decidir ubicación editorial;
- decidir orden;
- decidir nivel de detalle;
- relacionar contenido con necesidades de selección;
- asegurar cobertura estratégica;
- reducir ruido;
- gestionar sobrecualificación mediante énfasis honesto;
- definir tratamiento editorial del seniority;
- definir tono editorial;
- trasladar advertencias a restricciones;
- clasificar léxico;
- construir el brief derivado.

---

# 9. Qué no puede decidir

Esta sección desarrolla `FUERA_DE_RESPONSABILIDAD` sin ampliarlo.

No puede:

- modificar hechos;
- crear experiencia;
- inventar métricas;
- inventar responsabilidades;
- alterar fechas;
- modificar requisitos de la oferta;
- cambiar la decisión estratégica;
- cambiar la tesis;
- cambiar el posicionamiento;
- eliminar carencias mediante edición;
- convertir formación en experiencia;
- convertir transferibilidad en experiencia literal;
- convertir automatización en IA;
- atribuir tecnologías no acreditadas;
- modificar cargos históricos;
- ocultar deliberadamente hechos necesarios para interpretar correctamente la trayectoria;
- degradar seniority histórico para aparentar mejor encaje;
- inflar seniority para aparentar más experiencia;
- redactar el CV definitivo;
- redactar la carta;
- diseñar formato visual;
- producir DOCX, PDF o LaTeX;
- diseñar la futura infraestructura CV/carta;
- presentar la candidatura.

---

# 10. Orden normativo de ejecución

El agente debe operar en este orden:

```text
1. validar precondiciones
2. cargar estrategia heredada
3. resolver fuentes factuales
4. construir universo candidato de contenido
5. decidir presencia
6. decidir obligatoriedad
7. asignar peso editorial y función estratégica
8. vincular contenido con criterio objetivo
9. verificar cobertura de prioridades estratégicas
10. decidir ubicación, orden y nivel de detalle
11. construir arquitectura narrativa
12. definir seniority, tono, léxico y límites
13. generar brief derivado
14. ejecutar control de primer escaneo
15. ejecutar control de coherencia
16. evaluar gate de salida
```

No debe invertir pasos cuando ello suponga tomar una decisión antes de disponer de la información que la gobierna.

Este orden constituye un **algoritmo normativo de fase**, no una sugerencia.

---

# 11. Universo candidato de contenido

El playbook no debe recorrer indiscriminadamente toda la trayectoria y generar una decisión para cada dato existente.

El universo candidato contiene material que cumpla al menos una de estas condiciones:

1. está señalado estratégicamente por `candidatura.md`;
2. posee relevancia plausible para un requisito o señal de selección;
3. es necesario para mantener coherencia factual;
4. es necesario para mantener coherencia cronológica;
5. puede afectar materialmente a la percepción profesional;
6. contiene una advertencia o límite que debe controlarse.

Puede incluir:

- perfil profesional;
- titular;
- competencias;
- experiencias;
- cargos;
- funciones;
- responsabilidades;
- logros;
- resultados;
- métricas;
- herramientas;
- tecnologías;
- formación;
- certificaciones;
- idiomas;
- proyectos;
- otros contenidos profesionales relevantes.

El playbook no está obligado a utilizar todas las categorías.

Una unidad entra en el universo candidato para ser **evaluada**, no para ser incluida automáticamente.

---

# 12. Contrato de `guion-adaptacion-cv.md`

## 12.1 Identificación y trazabilidad

Debe registrar:

- candidatura;
- empresa;
- puesto;
- fecha;
- sesión;
- `candidatura.md` de origen;
- análisis de origen;
- fuentes factuales utilizadas;
- fecha de lectura de fuentes;
- gate de entrada;
- referencia a la evaluación del gate de entrada cuando exista;
- gate de salida aplicable.

Objetivo:

> poder identificar inequívocamente qué estado estratégico y factual produjo el guion.

El guion **no almacena el estado oficial mutable del gate de salida**.

Ese estado pertenece al artefacto específico de evaluación y decisión del gate.

---

## 12.2 Instrucción editorial del CV

Debe expresar:

- posicionamiento heredado;
- mensaje profesional principal;
- gancho;
- objetivo del CV;
- tratamiento de seniority;
- tono editorial;
- percepción que debe provocar;
- percepción que debe evitar cuando proceda.

### 12.2.1 Tratamiento de seniority

Debe distinguir:

```text
seniority_historico
seniority_objetivo
tratamiento_editorial
```

`seniority_historico` describe únicamente lo respaldado por la trayectoria.

`seniority_objetivo` describe el nivel real del puesto al que se opta.

`tratamiento_editorial` decide cómo presentar el primero frente al segundo.

Puede:

- modular prominencia;
- priorizar evidencia funcional;
- reducir contenido directivo irrelevante;
- destacar proximidad real al trabajo objetivo.

No puede:

- alterar cargos;
- degradar responsabilidades históricas;
- inventar un nivel inferior;
- ocultar hechos necesarios para entender la trayectoria.

### 12.2.2 Tono editorial

El guion debe fijar de uno a tres descriptores operativos de tono.

Ejemplos conceptuales:

```text
directo
concreto
operativo
técnico
ejecutivo
didáctico
sobrio
```

No existe un enum obligatorio global.

Los descriptores deben justificarse por:

- tipo de puesto;
- posicionamiento heredado;
- naturaleza de la evidencia;
- convenciones ya respaldadas por las fuentes del caso.

El tono no autoriza:

- lenguaje corporativo inventado;
- claims promocionales sin evidencia;
- exageración;
- investigación externa no aprobada.

Ejemplo conceptual:

```text
Posicionamiento:
Profesional de operaciones de supermercados con experiencia
demostrada en previsión, stock, organización y mejora de procesos.

Gancho:
Experiencia práctica resolviendo problemas reales de operación
mediante previsión, organización, seguimiento y mejora.

Seniority:
Mantener cargos históricos; reducir protagonismo directivo
y priorizar evidencia operativa real.

Tono:
Directo, concreto y operativo.

Percepción a evitar:
Perfil excesivamente corporativo y alejado de la operación diaria.
```

Son instrucciones editoriales.

No son frases destinadas a copiarse literalmente.

---

## 12.3 Mapa de edición

El mapa es el núcleo operativo del guion.

Cada unidad considerada debe poseer una referencia local única dentro del artefacto.

Formato recomendado:

```text
M-001
M-002
M-003
...
```

`M-NNN` es una referencia interna del guion.

No constituye un nuevo espacio de identificadores global del proyecto.

---

### 12.3.1 Tipo de contenido

Valores preferentes:

```text
perfil
titular
competencia
experiencia
cargo
funcion
responsabilidad
logro
resultado
metrica
herramienta
tecnologia
formacion
certificacion
idioma
proyecto
otro
```

`otro` requiere descripción explícita.

---

### 12.3.2 Presencia

Valores:

```text
incluir
omitir
```

#### `incluir`

El contenido forma parte de este CV.

#### `omitir`

El contenido no aparece.

Solo es admisible cuando la omisión:

- no falsifica;
- no rompe una cronología necesaria;
- no oculta una carencia que deba permanecer visible;
- no produce interpretación engañosa;
- no elimina contexto imprescindible.

---

### 12.3.3 Obligatoriedad

Valores:

```text
obligatoria
opcional
```

#### `obligatoria`

El contenido debe conservarse por:

- continuidad cronológica;
- coherencia factual;
- prevención de interpretación engañosa;
- necesidad estratégica explícita;
- requisito contractual del futuro CV.

#### `opcional`

Su inclusión depende de utilidad editorial.

Reglas:

```text
obligatoriedad: obligatoria
→ presencia: incluir

presencia: omitir
→ obligatoriedad: opcional
```

Obligatoriedad no determina peso.

---

### 12.3.4 Peso editorial

Para contenido incluido:

```text
alto
medio
bajo
minimo
```

#### `alto`

Sostiene directamente el posicionamiento o un criterio central de selección.

#### `medio`

Aporta evidencia relevante pero secundaria.

#### `bajo`

Debe aparecer resumido.

#### `minimo`

Solo mantiene contexto, continuidad o información imprescindible.

Para contenido omitido:

```text
peso_editorial: no_aplica
```

Es válida esta combinación:

```text
presencia: incluir
obligatoriedad: obligatoria
peso_editorial: minimo
```

---

### 12.3.5 Jerarquía para decidir peso

El agente debe aplicar esta prioridad:

1. relevancia para la estrategia heredada;
2. relevancia para requisitos o señales de selección;
3. fuerza y credibilidad de la evidencia factual;
4. capacidad de diferenciación;
5. utilidad para el primer escaneo;
6. especificidad del efecto o resultado.

Una métrica acreditada aumenta la fuerza probatoria, pero no sustituye a la relevancia.

Cuando dos contenidos tengan relevancia, credibilidad y fuerza de evidencia comparables, podrá preferirse el que aporte:

- resultado cuantificable;
- efecto verificable más específico;
- evidencia más fácil de defender en entrevista.

No debe preferirse una métrica débil o irrelevante frente a una evidencia cualitativa claramente más pertinente.

Nunca se inventan cifras para aumentar peso editorial.

---

### 12.3.6 Criterio objetivo

Todo contenido con peso `alto` o `medio` debe identificar qué ayuda a demostrar.

Puede ser:

- requisito explícito;
- responsabilidad del puesto;
- competencia;
- señal de selección;
- argumento estratégico heredado.

Ejemplo:

```text
contenido: previsión y pedidos
evidencia: HER-03
criterio_objetivo: disponibilidad / pedidos / inventario
presencia: incluir
obligatoriedad: opcional
peso_editorial: alto
```

No es necesario recrear la matriz completa de análisis.

---

### 12.3.7 Función estratégica

Valores preferentes, compatibles entre sí:

```text
sostener_posicionamiento
demostrar_requisito
diferenciar
dar_continuidad
proteger_factualidad
mitigar_riesgo
respaldar_keyword
```

Una unidad puede cumplir más de una función.

`funcion_estrategica` no reemplaza a `criterio_objetivo`.

---

### 12.3.8 Ubicación editorial

Cada contenido incluido debe indicar cuando proceda:

```text
seccion_destino
orden_en_seccion
nivel_detalle
```

`seccion_destino` referencia una sección definida en la arquitectura editorial del propio guion.

Las secciones pueden identificarse localmente como:

```text
SEC-01
SEC-02
SEC-03
...
```

`SEC-NN` es referencia local, no identificador global.

`orden_en_seccion` es numérico y solo ordena elementos dentro de la misma sección.

`nivel_detalle` utiliza:

```text
amplio
normal
breve
mencion
```

Definición:

- `amplio`: requiere desarrollo suficiente para sostener una evidencia prioritaria;
- `normal`: desarrollo estándar;
- `breve`: presencia resumida;
- `mencion`: mínima presencia necesaria para continuidad o contexto.

Para contenido omitido:

```text
seccion_destino: no_aplica
orden_en_seccion: no_aplica
nivel_detalle: no_aplica
```

Peso editorial y nivel de detalle son dimensiones relacionadas pero no equivalentes.

Una unidad obligatoria con peso `minimo` puede requerir `nivel_detalle: mencion`.

---

### 12.3.9 Motivo y restricciones

`motivo` es obligatorio cuando:

- `presencia: omitir`;
- `obligatoriedad: obligatoria`;
- `peso_editorial: alto`;
- `peso_editorial: medio`.

`limitaciones_redaccion` es obligatorio cuando:

- existe advertencia;
- existe uso condicionado;
- existe riesgo de sobreafirmación;
- existe una exclusión relacionada.

---

### 12.3.10 Campos mínimos del mapa

Cada unidad considerada debe registrar:

```text
ref_local
contenido
tipo
evidencia
presencia
obligatoriedad
peso_editorial
criterio_objetivo
motivo
funcion_estrategica
seccion_destino
orden_en_seccion
nivel_detalle
limitaciones_redaccion
```

Los campos no aplicables deben aparecer como:

```text
no_aplica
```

No deben omitirse silenciosamente.

`evidencia` puede contener una o varias referencias factuales.

---

## 12.4 Contenido profesional seleccionado

El guion debe determinar qué material sostiene el CV.

Puede incluir:

- perfil;
- competencias;
- experiencia;
- responsabilidades;
- funciones;
- logros;
- métricas;
- herramientas;
- tecnologías;
- formación;
- certificaciones;
- idiomas;
- proyectos.

Para experiencias debe distinguir cuando proceda:

- experiencia con mayor protagonismo;
- experiencia secundaria;
- experiencia necesaria para continuidad;
- contenido a minimizar;
- logros prioritarios;
- evidencias de impacto.

Una competencia genérica no debe desplazar una evidencia concreta que la demuestre.

Cuando se incluya una competencia relevante, debe existir:

- evidencia factual;
- o una relación heredada explícita desde la estrategia de candidatura.

No debe redactar todavía frases finales.

---

## 12.5 Cronología y relevancia

Adaptar no significa reorganizar libremente la trayectoria.

El guion puede decidir:

- peso;
- detalle;
- logros destacados;
- contenidos utilizados en el perfil;
- prominencia relativa.

Debe preservar una trayectoria comprensible y honesta.

**Contenido de apertura** significa:

> evidencia que debe dominar la percepción inicial.

No significa:

> colocar automáticamente una experiencia antigua antes de la más reciente.

Una alteración posterior de la estructura cronológica requerirá que el formato de CV aplicable lo autorice expresamente.

---

## 12.6 Arquitectura editorial y presupuesto de contenido

El guion puede decidir:

- orden funcional de secciones;
- objetivo de cada sección;
- identificador local de cada sección;
- qué debe dominar la primera lectura;
- distribución relativa de profundidad;
- qué contenido debe comprimirse;
- qué contenido solo mantiene continuidad;
- progresión narrativa.

Debe además considerar cualquier restricción documental ya vigente en el flujo, por ejemplo un límite máximo de extensión.

Puede traducir esa restricción a:

- mayor o menor compresión;
- número relativo de evidencias;
- reducción de contenido secundario;
- prioridad de secciones.

No puede decidir todavía:

- paginación exacta;
- columnas;
- tipografía;
- tamaños;
- colores;
- márgenes;
- recursos gráficos.

Si existe tensión entre cobertura estratégica y límite documental:

1. preservar contenido obligatorio;
2. preservar evidencia de peso alto;
3. reducir o eliminar contenido de peso bajo;
4. evitar comprimir una evidencia hasta volverla ininteligible;
5. registrar cualquier conflicto que no pueda resolverse editorialmente.

---

## 12.7 Léxico respaldado

Debe clasificar términos relevantes en tres grupos.

### Utilizables

Existe respaldo factual suficiente.

### Uso condicionado

Solo pueden emplearse:

- con alcance limitado;
- en contexto concreto;
- sin extender su significado.

### Prohibidos

No deben utilizarse porque:

- exceden evidencia;
- alteran seniority;
- convierten transferibilidad en experiencia;
- contradicen exclusiones;
- generan una impresión falsa.

Reglas:

> La optimización para ATS nunca autoriza afirmaciones falsas.

> La cobertura de palabras clave no debe producir keyword stuffing ni desplazar evidencia profesional más fuerte.

---

## 12.8 Carencias, advertencias y límites

Cada riesgo relevante debe transformarse en una instrucción editorial.

Formato:

```text
elemento:
riesgo:
tratamiento:
permitido:
prohibido:
```

Ejemplo:

```text
elemento:
FP no finalizada

riesgo:
presentarla como titulación terminada

tratamiento:
no utilizarla como credencial terminada

permitido:
formación realmente acreditada

prohibido:
presentar título de Técnico Administrativo
```

---

## 12.9 Control de primer escaneo

El guion debe controlar explícitamente la **previsión editorial** de la lectura inicial del recruiter.

No sustituye la validación posterior del CV materializado.

Sin depender de diseño visual debe procurar que puedan percibirse rápidamente:

1. qué perfil profesional se presenta;
2. por qué puede encajar;
3. cuáles son sus dos o tres señales de evidencia más fuertes;
4. qué capacidad merece atención inmediata.

El primer escaneo no debe quedar dominado por:

- información secundaria;
- contenido irrelevante;
- credenciales débiles;
- trayectoria que incremente innecesariamente la percepción de sobrecualificación;
- keywords no sustentadas.

Pregunta de control:

> Si un recruiter dedica inicialmente pocos segundos al contenido que este guion hará dominante, ¿recibe primero las señales correctas?

Debe poder responder afirmativamente a estas comprobaciones:

- el tipo de perfil se identifica sin reconstruir toda la trayectoria;
- el encaje principal resulta visible;
- aparecen dos o tres señales fuertes y respaldadas;
- ninguna credencial secundaria, keyword o cargo histórico desplaza injustificadamente el mensaje principal;
- cuando exista riesgo de sobrecualificación, la primera lectura mantiene proximidad real al trabajo objetivo sin falsificar seniority ni trayectoria.

---

## 12.10 Control de cobertura estratégica

Toda prioridad estratégica de `candidatura.md` debe terminar en una de estas situaciones:

```text
cubierta
no_requiere_presencia_directa
no_cubierta_justificada
bloqueo
```

### `cubierta`

Existe al menos una unidad incluida que la representa de manera suficiente.

### `no_requiere_presencia_directa`

La prioridad gobierna el relato pero no necesita aparecer como contenido independiente.

### `no_cubierta_justificada`

Existe una razón editorial explícita para no representarla.

No puede utilizarse para ocultar falta de evidencia.

### `bloqueo`

La prioridad no puede trasladarse al CV sin:

- inventar;
- contradecir fuentes;
- cambiar estrategia;
- o resolver una incidencia aguas arriba.

El guion debe registrar un resumen de cobertura que permita comprobar que ninguna prioridad estratégica desapareció silenciosamente.

---

## 12.11 Control de duplicación

La misma evidencia puede aparecer en distintos niveles de abstracción, por ejemplo:

```text
perfil
→ experiencia
→ logro
```

solo cuando cada aparición cumple una función distinta.

Debe evitarse repetir la misma afirmación sin añadir valor.

Regla:

> Reforzar una evidencia no equivale a duplicarla literalmente.

El guion debe reducir:

- reiteraciones;
- listas de competencias que repiten logros;
- keywords redundantes;
- responsabilidades que duplican resultados;
- frases de perfil que repiten de forma literal la experiencia.

---

## 12.12 Brief cerrado para generación

El guion debe terminar con un brief compacto.

Debe resumir:

- objetivo;
- posicionamiento;
- gancho;
- seniority;
- tono;
- contenidos prioritarios;
- evidencias prioritarias;
- cobertura estratégica;
- arquitectura narrativa;
- contenidos a minimizar;
- restricciones;
- léxico;
- riesgos.

### 12.12.1 Autoridad del brief

El brief es una **síntesis derivada**.

No constituye otra fuente de autoridad.

No puede:

- crear decisiones;
- modificar decisiones;
- eliminar restricciones;
- reinterpretar posicionamiento;
- cambiar seniority;
- cambiar tono sin respaldo;
- cambiar presencia;
- cambiar obligatoriedad;
- cambiar peso;
- alterar cobertura.

En caso de discrepancia:

```text
cuerpo detallado del guion
> brief
```

La discrepancia debe corregirse antes del gate.

---

# 13. Tratamiento de incidencias y relación con `DEF-ARQ-001`

## 13.1 Regla arquitectónica previa

`DEF-ARQ-001 — Propagación de cambios factuales` permanece:

```text
clasificacion: ARQUITECTURA
estado: abierto
```

Este diseño **no lo cierra**.

En particular, este playbook no debe presentarse como el contrato arquitectónico general de propagación de nueva evidencia factual.

La responsabilidad local de esta fase se limita a:

1. detectar que existe una novedad factual relevante;
2. impedir su incorporación directa;
3. invalidar o bloquear su propia salida cuando proceda;
4. remitir la situación a la arquitectura de propagación.

Mientras `DEF-ARQ-001` permanezca abierto:

> Work no puede inventar un mecanismo automático de propagación entre `datos-core-busqueda.md`, análisis, candidatura, guiones u otros artefactos derivados.

---

## 13.2 Alcance histórico

La problemática de propagación afecta a candidaturas:

```text
presentada: false
```

Una candidatura ya presentada conserva carácter histórico.

Una evidencia descubierta posteriormente no autoriza a reescribir retroactivamente los artefactos históricos de una candidatura presentada.

---

## 13.3 Corrección editorial local

Si:

- los hechos no cambian;
- la estrategia no cambia;
- el posicionamiento no cambia;
- las exclusiones no cambian;

pero una decisión editorial es incorrecta, puede corregirse localmente.

Ejemplos:

- peso incorrecto;
- orden incorrecto;
- detalle excesivo;
- cobertura incompleta por error editorial;
- contenido incluido que debería omitirse.

Resultado:

```text
requiere_correccion
```

No activa `DEF-ARQ-001`.

---

## 13.4 Evidencia insuficiente

Si una afirmación deseada carece de respaldo:

```text
no se inventa
```

Puede:

- eliminarse;
- limitarse;
- sustituirse por una formulación sustentada;

si ello no altera la estrategia.

Si la insuficiencia pone en duda:

- posicionamiento;
- evidencia prioritaria;
- encaje;
- tesis;
- afirmación estratégica;

el guion debe detener la decisión y remitir aguas arriba.

Resultado:

```text
requiere_revision_origen
```

cuando la estrategia de origen debe ser reconsiderada.

---

## 13.5 Evidencia factual nueva

Si aparece un hecho profesional nuevo que podría modificar:

- análisis;
- encaje;
- evidencia;
- riesgos;
- estrategia;
- posicionamiento;

el guion no puede incorporarlo directamente.

Resultado local:

```text
requiere_actualizacion_factual
```

Debe registrar:

```text
defecto_relacionado: DEF-ARQ-001
```

El recorrido conceptual esperado continúa siendo:

```text
datos-core-busqueda.md
        ↓
analisis-oferta.md
        ↓
candidatura.md
        ↓
validación correspondiente
        ↓
nuevo guion
```

Este esquema expresa **dependencias lógicas**, no un contrato operativo completo de propagación.

La forma verificable de realizar esa propagación pertenece a `DEF-ARQ-001`.

---

## 13.6 Evidencia contradictoria

Si aparece una contradicción entre autoridades:

```text
guion
→ detenido
```

Resultado:

```text
requiere_revision_origen
```

No debe decidir qué fuente conviene conservar.

---

## 13.7 Bloqueo operativo

Debe producir:

```text
bloqueado
```

cuando una condición impide evaluar válidamente el guion y no puede resolverse mediante una corrección editorial local.

Ejemplos:

- fuente obligatoria inaccesible;
- gate de entrada no aprobado;
- candidatura no apta para ejecución;
- dependencia obligatoria inexistente;
- contradicción arquitectónica que impide determinar qué contrato aplicar.

---

## 13.8 Invalidación por cambios aguas arriba

Si cambia materialmente:

- `candidatura.md`;
- evidencia factual utilizada;
- análisis relevante;
- posicionamiento;
- exclusiones;
- evidencias prioritarias;

el guion puede perder validez.

La evaluación vigente de:

```text
GATE-GUION-CV-CONTENIDO
```

deja de considerarse suficiente y debe volver a:

```text
pendiente
```

siempre que el modelo de gobierno vigente permita registrar esa transición.

Si el cambio afecta hechos o estrategia:

> el guion deberá regenerarse una vez que la propagación aguas arriba haya quedado válidamente resuelta.

Esta regla local de invalidación no resuelve `DEF-ARQ-001`.

---

# 14. Control de coherencia previo al gate

Este control es interno al playbook.

No sustituye los criterios formales de aceptación de la sección 19.

Antes de evaluar el gate debe comprobarse:

- [ ] gate de entrada aprobado;
- [ ] fuentes resolubles;
- [ ] ausencia de bloqueo;
- [ ] estrategia no reabierta;
- [ ] todo hecho usado tiene respaldo;
- [ ] universo candidato acotado;
- [ ] todas las prioridades estratégicas tienen estado de cobertura;
- [ ] toda unidad relevante tiene tratamiento;
- [ ] presencia, obligatoriedad y peso son independientes;
- [ ] peso sigue la jerarquía definida;
- [ ] contenido prioritario sostiene posicionamiento;
- [ ] contenido prioritario se vincula a criterios objetivos;
- [ ] seniority está tratado explícitamente;
- [ ] tono está definido y respaldado;
- [ ] omisiones no deforman trayectoria;
- [ ] cronología sigue siendo comprensible;
- [ ] exclusiones están protegidas;
- [ ] advertencias se traducen en restricciones;
- [ ] no existen hechos inventados;
- [ ] no existe keyword stuffing;
- [ ] duplicaciones injustificadas han sido eliminadas;
- [ ] previsión de primer escaneo es satisfactoria;
- [ ] brief coincide con el cuerpo;
- [ ] no se ha redactado el CV final;
- [ ] no se ha diseñado la carta;
- [ ] fase posterior no necesita reinterpretar estrategia;
- [ ] cualquier incidencia factual nueva se relaciona correctamente con `DEF-ARQ-001`.

---

# 15. Gate de salida

El gate se denomina:

```text
GATE-GUION-CV-CONTENIDO
```

Lectura:

```text
GATE-
ORIGEN: GUION-CV
DESTINO: CONTENIDO
```

El origen identifica inequívocamente la rama.

No es necesario repetir `CV` en el destino.

La futura rama de carta podría aplicar un patrón simétrico:

```text
GATE-GUION-CARTA-CONTENIDO
```

solo si su futuro diseño lo aprueba.

El gate de entrada `GATE-CANDIDATURA-GUION` conserva su nombre vigente.

Este diseño:

- no lo renombra;
- no presupone su futura semántica multiadaptador.

La cuestión queda en `INC-002`.

---

# 16. Qué valida el gate

`GATE-GUION-CV-CONTENIDO` valida únicamente que:

> `guion-adaptacion-cv.md` constituye una entrada suficientemente completa, factual, competitiva, estratégica, trazable y determinista para habilitar el siguiente paso arquitectónico de la rama CV.

No valida:

- CV final;
- resultado visual;
- ATS final;
- carta;
- maquetación;
- candidatura completa;
- envío.

---

# 17. Gate aprobado y fase siguiente

Mientras la futura generación de contenido del CV no esté diseñada:

```text
GATE-GUION-CV-CONTENIDO: aprobado
```

autoriza:

> comenzar el diseño de la siguiente fase.

No autoriza:

> ejecutarla.

Patrón:

```text
fase
→ artefacto
→ gate
→ diseño autorizado de siguiente fase
```

Una vez que la siguiente fase exista y haya sido aprobada por su propio proceso, su ejecución se regirá por su contrato, no por este documento.

---

# 18. Evaluación y decisión humana

La IA puede evaluar.

La aprobación oficial sigue siendo humana.

Debe distinguirse entre:

```text
contrato del gate
evaluación de una candidatura
decisión humana
estado de fase
```

`GATE-GUION-CV-CONTENIDO` define el tipo de traspaso.

Cada candidatura genera su propia evaluación.

Por tanto:

- aprobar `CAND-2026-020` no aprueba otros casos;
- validar la fase no elimina gates individuales futuros;
- estado de fase y estado de gate son ejes distintos.

---

## 18.1 Resultado de evaluación

Valores:

```text
apto
requiere_correccion
requiere_revision_origen
requiere_actualizacion_factual
bloqueado
```

---

## 18.2 Regla determinista de resultado

### `apto`

Solo cuando:

- todas las precondiciones se cumplen;
- todos los criterios de aceptación se cumplen;
- no existe incidencia pendiente.

### `requiere_correccion`

Cuando el defecto es local al guion y no obliga a cambiar hechos ni estrategia.

Ejemplos:

- peso;
- orden;
- cobertura editorial;
- duplicación;
- tono;
- nivel de detalle;
- brief inconsistente.

### `requiere_revision_origen`

Cuando resolver el problema exige revisar una autoridad aguas arriba.

Ejemplos:

- contradicción entre fuentes;
- insuficiencia que pone en duda estrategia;
- posicionamiento no sostenible.

### `requiere_actualizacion_factual`

Cuando existe nueva evidencia factual relevante que debe incorporarse mediante el contrato arquitectónico de propagación.

### `bloqueado`

Cuando no es posible realizar una evaluación válida.

Ejemplos:

- fuente obligatoria inaccesible;
- gate de entrada no aprobado;
- precondición obligatoria incumplida;
- contradicción arquitectónica bloqueante.

Regla:

> Si concurren varios resultados, prevalece el que obligue a retroceder más lejos en la arquitectura.

Orden de precedencia:

```text
bloqueado
requiere_actualizacion_factual
requiere_revision_origen
requiere_correccion
apto
```

La precedencia no sustituye el registro de todas las incidencias detectadas.

---

## 18.3 Recomendación IA

Valores:

```text
aprobar
no_aprobar
```

Regla:

```text
resultado_evaluacion: apto
→ recomendacion_ia: aprobar

cualquier otro resultado
→ recomendacion_ia: no_aprobar
```

---

## 18.4 Decisión humana

Valores:

```text
pendiente
aprobado
bloqueado
```

La persona responsable puede decidir de forma distinta a la recomendación de IA, pero la discrepancia debe quedar registrada.

Ejemplo:

```text
resultado_evaluacion: apto
recomendacion_ia: aprobar
decision_humana: pendiente
estado_gate: pendiente
```

Tras aprobación:

```text
resultado_evaluacion: apto
recomendacion_ia: aprobar
decision_humana: aprobado
estado_gate: aprobado
```

---

## 18.5 Artefacto de evaluación del gate

La evaluación debe persistirse en un artefacto separado.

Nombre previsto para el caso:

```text
evaluacion-gate-guion-cv-contenido.md
```

Campos mínimos:

```yaml
id:
tipo: evaluacion_gate
candidatura:
gate: GATE-GUION-CV-CONTENIDO
guion_evaluado:
fecha_evaluacion:
resultado_evaluacion:
recomendacion_ia:
decision_humana:
estado_gate:
fecha_decision_humana:
sesion:
```

El guion no es la autoridad del estado del gate.

El artefacto de evaluación sí registra:

- evaluación;
- recomendación;
- decisión;
- estado oficial del gate para esa candidatura.

---

# 19. Criterios de aceptación

Para recomendar aprobación deben cumplirse todos:

- [ ] gate de entrada aprobado;
- [ ] ausencia de bloqueo;
- [ ] posicionamiento heredado intacto;
- [ ] instrucción editorial clara;
- [ ] seniority tratado explícitamente;
- [ ] tono editorial explícito y respaldado;
- [ ] universo candidato razonable;
- [ ] mapa de edición completo;
- [ ] presencia separada de obligatoriedad;
- [ ] obligatoriedad separada de peso;
- [ ] campos no aplicables marcados como `no_aplica`;
- [ ] contenido principal vinculado a criterios objetivos;
- [ ] experiencias y logros prioritarios identificados;
- [ ] prioridades estratégicas con cobertura controlada;
- [ ] selección trazable;
- [ ] omisiones materiales justificadas;
- [ ] ninguna omisión induce a error;
- [ ] cronología comprensible;
- [ ] exclusiones protegidas;
- [ ] léxico respaldado;
- [ ] ausencia de keyword stuffing;
- [ ] duplicación injustificada controlada;
- [ ] ausencia de hechos nuevos incorporados sin propagación;
- [ ] incidencias factuales nuevas relacionadas con `DEF-ARQ-001`;
- [ ] previsión de primer escaneo competitiva;
- [ ] brief coherente;
- [ ] ausencia de redacción final del CV;
- [ ] ausencia de diseño de carta;
- [ ] siguiente fase capaz de operar sin reconstruir estrategia.

---

# 20. Postcondiciones

Con gate aprobado debe existir evidencia de que:

1. `guion-adaptacion-cv.md` está completo;
2. coincide con `candidatura.md`;
3. mantiene trazabilidad factual;
4. las decisiones editoriales están cerradas;
5. la futura fase sabe:
   - qué incluir;
   - qué omitir;
   - qué conservar;
   - qué priorizar;
   - qué minimizar;
   - qué demostrar;
   - qué evitar;
   - qué tono aplicar;
   - cómo tratar seniority;
   - qué estructura seguir;
6. todas las prioridades estratégicas poseen estado de cobertura;
7. el posicionamiento no requiere reinterpretación;
8. no existe contenido final del CV;
9. cualquier problema factual nuevo ha sido detenido y remitido correctamente;
10. existe artefacto separado de evaluación del gate cuando se haya evaluado.

---

# 21. Metadatos mínimos del artefacto

El futuro template deberá incluir frontmatter estructurado.

Mínimo:

```yaml
id:
tipo: guion_adaptacion_cv
version_diseno:
version_playbook:
version_template:
candidatura:
empresa:
puesto:
fecha_generacion:
sesion:
candidatura_origen:
analisis_origen:
fuentes_factuales:
fecha_lectura_fuentes:
gate_entrada:
evaluacion_gate_entrada:
gate_salida: GATE-GUION-CV-CONTENIDO
```

No debe contener:

```yaml
estado_gate_salida:
```

como fuente normativa del estado oficial.

Motivo:

> la decisión del gate ocurre después de generar y evaluar el guion y pertenece a su artefacto específico de evaluación.

`fecha_lectura_fuentes` aporta trazabilidad temporal mínima.

No constituye por sí sola:

- versionado;
- detección automática de cambios;
- solución de `DEF-ARQ-001`.

Si el repositorio dispone de identificadores de versión o revisión verificables, podrán reutilizarse.

No debe inventarse infraestructura nueva para obtenerlos.

---

# 22. Prueba principal — `CAND-2026-020`

Caso:

```text
CAND-2026-020
Lidl Supermercados SAU
Responsable de turno Tienda 40h Tamaraceite
```

Es adecuado porque obliga a adaptar una trayectoria amplia hacia un puesto operativo.

---

## 22.1 Contenido a priorizar

La prueba debe demostrar capacidad para priorizar:

- operación de supermercados;
- previsión;
- pedidos;
- stock;
- rotación;
- mermas;
- disponibilidad;
- organización del trabajo;
- seguimiento de tareas;
- cuadres de caja;
- mejora de procesos.

---

## 22.2 Sobrecualificación y seniority

Debe:

- conservar cargos reales;
- conservar continuidad;
- registrar explícitamente tratamiento de seniority;
- reducir protagonismo de contenido directivo irrelevante;
- aumentar evidencia operativa;
- impedir que la primera percepción sea la de un perfil alejado de tienda.

No puede:

- falsear cargos;
- degradar responsabilidades históricas;
- inventar una trayectoria operativa distinta;
- presentar seniority ficticiamente inferior.

---

## 22.3 Formación

Debe impedir:

- presentar FP no finalizada como titulación;
- crear equivalencias inexistentes.

---

## 22.4 Caja

`HER-10` puede respaldar:

- cuadres de caja;
- mejora mediante Excel.

No puede respaldar:

- tesorería;
- banca;
- pagos;
- gestión financiera integral.

---

## 22.5 Compras y proveedores

Puede utilizar hechos acreditados sobre:

- pedidos;
- proveedores directos;
- negociación limitada;
- sistemas acreditados.

No puede convertirlos en:

- política central de compras;
- negociación corporativa;
- funciones financieras;
- responsabilidades no acreditadas.

---

## 22.6 Resultado esperado del control de cobertura

La prueba debe demostrar que las prioridades estratégicas relevantes de `candidatura.md`:

- aparecen representadas;
- o poseen justificación explícita para no requerir presencia directa.

No debe aceptarse un guion que sea factual pero haya perdido una prioridad estratégica por selección editorial defectuosa.

---

# 23. Estado del caso antes de probar

Antes de generar el guion debe verificarse:

```text
GATE-CANDIDATURA-GUION: aprobado
```

Además:

- la siguiente fase debe apuntar al guion;
- el índice de artefactos debe reflejar el estado vigente;
- no deben sobrevivir instrucciones anteriores al gate aprobado;
- `presentada: false`;
- las referencias de origen deben resolver al estado utilizado para la prueba.

No debe probarse la fase utilizando un artefacto operativamente obsoleto.

---

# 24. Prueba de generalidad

`CAND-2026-020` es el primer caso.

`CAND-2026-019` es el caso posterior de contraste.

El contraste debe probar problemas distintos:

- perfil tecnológico;
- transferibilidad funcional;
- carencias de stack;
- formación no coincidente;
- riesgo de sobreafirmación;
- posicionamiento distinto;
- uso de léxico técnico sin convertir familiaridad en experiencia;
- tratamiento de seniority en un contexto diferente al operativo de tienda.

La progresión queda definida literalmente:

```text
CAND-2026-020 superado
→ PLAYBOOK_GUION_ADAPTACION_CV: en_prueba

CAND-2026-020 + CAND-2026-019 superados
→ PLAYBOOK_GUION_ADAPTACION_CV: candidata a validada
```

Superar únicamente `CAND-2026-020` permite:

- continuar implementación;
- continuar pruebas;
- mantener fase `en_prueba`.

No permite declarar:

```text
validada
```

Solo después de superar ambos casos puede proponerse validación humana.

`candidata a validada` no es un nuevo estado formal.

Estados oficiales:

```text
pendiente
diseñada
en_prueba
validada
```

La validación de fase no sustituye la evaluación individual del gate de cada candidatura posterior.

---

# 25. Regla de generalización

El playbook y su template no deben codificar reglas específicas de:

- Lidl;
- supermercados;
- `CAND-2026-020`;
- `CAND-2026-019`.

Debe comprobarse que son genéricos:

- ejes editoriales;
- universo candidato;
- tipos de contenido;
- jerarquización;
- seniority;
- tono;
- cobertura estratégica;
- retrocesos;
- primer escaneo;
- sobrecualificación;
- relación con factualidad.

Principio:

> El caso valida el contrato. El caso no define el contrato.

---

# 26. Entregables y orden de implantación tras aprobación

La aprobación humana de este diseño autoriza **planificación**, no cambios físicos.

Work deberá producir primero un plan de implementación.

El plan debe separar cuatro bloques.

## 26.1 Bloque A — Sincronización normativa

Antes de implementar físicamente el playbook debe planificarse la sincronización mínima de la SPEC definida en la sección 34.

Objetivo:

> eliminar contradicciones normativas entre la SPEC vigente y el diseño aprobado.

Este bloque no resuelve `DEF-ARQ-001` ni las incertidumbres diferidas más allá de lo expresamente decidido aquí.

---

## 26.2 Bloque B — Implementación de fase

Debe conducir como mínimo a:

```text
PLAYBOOK_GUION_ADAPTACION_CV.md
TEMPLATE_GUION_ADAPTACION_CV_v2.md
```

También debe contemplar:

- metadatos definidos;
- mapa editorial estructurado;
- controles;
- semántica de incidencias;
- contrato del gate.

---

## 26.3 Bloque C — Prueba principal

Debe contemplar:

- sincronización previa de `CAND-2026-020`;
- actualización de su índice de artefactos;
- generación de `guion-adaptacion-cv.md`;
- control de coherencia;
- evaluación del gate en `evaluacion-gate-guion-cv-contenido.md`;
- decisión humana;
- actualización del estado de fase cuando corresponda.

---

## 26.4 Bloque D — Generalidad

Debe contemplar posteriormente:

- prueba con `CAND-2026-019`;
- evaluación individual del gate;
- contraste entre resultados;
- propuesta de validación de fase si ambos casos son superados.

---

# 27. Responsabilidad de Work

Esta sección es normativa para cualquier agente que reciba este diseño.

## 27.1 Rol

Work actúa como:

> planificador e implementador de un diseño previamente aprobado.

No actúa como diseñador autónomo de esta fase.

Existen dos autorizaciones separadas:

1. **aprobación humana de este diseño** → autoriza elaborar el plan;
2. **aprobación humana del plan + instrucción explícita de ejecución** → autoriza implementar las tareas aprobadas.

La aprobación del diseño no autoriza cambios físicos.

---

## 27.2 Secuencia obligatoria

```text
diseño aprobado
        ↓
verificación de estado real
        ↓
plan de implementación
        ↓
revisión y aprobación del plan
        ↓
instrucción explícita de ejecución
        ↓
sincronización normativa mínima de SPEC
        ↓
implementación del playbook y template
        ↓
preparación CAND-2026-020
        ↓
prueba
        ↓
evaluación del gate
        ↓
decisión humana
        ↓
posterior contraste CAND-2026-019
```

---

## 27.3 Antes de planificar

Work debe:

1. leer la SPEC vigente;
2. leer este diseño completo;
3. consultar `estado-actual.md`;
4. identificar la sesión PCS vigente;
5. inspeccionar el repositorio real;
6. comprobar existencia de artefactos;
7. comprobar `CAND-2026-020`;
8. comprobar `CAND-2026-019` cuando proceda;
9. verificar gates;
10. verificar el estado vigente de `DEF-ARQ-001`;
11. revalidar numeración disponible de `ARQ` e `INC`;
12. identificar discrepancias entre diseño y repositorio.

---

## 27.4 Qué puede hacer al planificar

Puede:

- localizar rutas reales;
- identificar archivos a crear;
- identificar archivos a actualizar;
- descomponer implementación;
- ordenar tareas;
- proponer pruebas;
- proponer verificaciones;
- señalar dependencias;
- señalar incertidumbres;
- señalar contradicciones.

---

## 27.5 Qué no puede hacer al planificar

No puede:

- rediseñar este contrato;
- cambiar responsabilidades;
- modificar el gate;
- fusionar CV y carta;
- cerrar `DEF-ARQ-001`;
- inventar el contrato de propagación factual;
- diseñar la rama de carta;
- resolver el alcance residual de `ARQ-09`;
- resolver `INC-001`, `INC-002` o `INC-003` por iniciativa propia;
- diseñar prematuramente JSON;
- diseñar el generador final;
- ampliar alcance;
- sustituir estados;
- introducir nuevas taxonomías;
- tratar una inferencia como decisión aprobada.

---

## 27.6 Reglas sobre `DEF-ARQ-001`

Mientras siga abierto:

Work puede implementar únicamente la reacción local definida por este diseño:

- detección;
- bloqueo;
- invalidación local;
- referencia al defecto.

Work no puede implementar por iniciativa propia:

- cascadas automáticas;
- propagación transversal;
- actualización automática de artefactos aguas abajo;
- cierre del defecto.

Si una tarea requiere alguno de esos comportamientos:

```text
STOP
→ devolver la tarea a arquitectura
```

---

## 27.7 Reglas sobre la carta y `ARQ-09`

Work puede aplicar la restricción ya decidida:

> este playbook es exclusivamente CV.

No puede resolver:

- playbook de carta;
- template de carta;
- gate de carta;
- generación de carta;
- infraestructura compartida;
- alcance residual de `ARQ-09`.

La sincronización de la SPEC sí debe dejar explícito que `ARQ-09` **no puede utilizarse para forzar una fase común CV/carta en contradicción con ARQ-22**.

Eso no equivale a resolver su significado residual.

---

## 27.8 Criterios de parada

Work debe detener la tarea afectada cuando:

- el repositorio contradiga una autoridad normativa;
- falte una decisión imprescindible;
- una tarea dependa de cerrar `DEF-ARQ-001`;
- sea necesario modificar una decisión de este diseño;
- aparezca incertidumbre bloqueante;
- se necesite diseñar una fase futura no autorizada;
- exista ambigüedad factual irresoluble.

Debe continuar con las tareas independientes válidas.

---

## 27.9 Salida mínima del plan

Cada tarea seguirá el esquema canónico de la SPEC:

```text
ID
titulo
objetivo
justificacion
precondiciones
archivos_a_leer
archivos_afectados
accion
resultado_esperado
criterios_de_aceptacion
verificacion
dependencias
gate_asociado
aprobacion_humana
```

Puede añadirse:

```text
riesgo_o_incidencia
```

como anotación complementaria opcional.

No se convierte en un campo obligatorio adicional.

Debe distinguir:

- archivos a crear;
- archivos a modificar;
- archivos solo de lectura;
- artefactos de prueba;
- actualizaciones de gobernanza.

---

## 27.10 Prohibición de implementación silenciosa

Si Work encuentra una mejora no contemplada:

1. la registra;
2. determina si es local o arquitectónica;
3. no la introduce silenciosamente;
4. devuelve a diseño cualquier decisión arquitectónica.

Principio:

> Work materializa el contrato; no completa sus huecos mediante diseño implícito.

---

# 28. Fuera de alcance arquitectónico

No forma parte de este bloque:

- redacción final del CV;
- maquetación;
- DOCX;
- PDF;
- LaTeX;
- carta;
- playbook de carta;
- template de carta;
- gate de carta;
- artefacto estratégico de carta;
- generación de carta;
- `datos-generacion.json`;
- adaptación del generador;
- nuevo veredicto final;
- envío;
- contacto externo;
- resolución de `DEF-ARQ-001`;
- definición residual de `ARQ-09`.

---

# 29. Criterio de cierre del diseño

El diseño puede aprobarse cuando exista decisión humana explícita sobre:

- [ ] responsabilidad CV-only;
- [ ] separación CV/carta;
- [ ] precedencia de ARQ-22 frente a cualquier lectura incompatible de ARQ-09;
- [ ] alcance residual de ARQ-09 registrado como incertidumbre;
- [ ] rama de carta como incertidumbre no bloqueante;
- [ ] contrato de fase de diez campos;
- [ ] autoridad estratégica;
- [ ] autoridad factual;
- [ ] papel del análisis;
- [ ] ausencia de investigación externa autónoma;
- [ ] orden normativo de 16 pasos;
- [ ] universo candidato;
- [ ] tipos de contenido;
- [ ] presencia / obligatoriedad / peso;
- [ ] jerarquía para asignar peso;
- [ ] criterio objetivo;
- [ ] función estratégica;
- [ ] ubicación y nivel de detalle;
- [ ] tratamiento de seniority;
- [ ] tono editorial;
- [ ] presupuesto editorial;
- [ ] protección cronológica;
- [ ] control de cobertura estratégica;
- [ ] control de duplicación;
- [ ] previsión de primer escaneo;
- [ ] autoridad derivada del brief;
- [ ] tratamiento de incidencias;
- [ ] relación con `DEF-ARQ-001`;
- [ ] ausencia de cierre local de `DEF-ARQ-001`;
- [ ] invalidación local sin inventar propagación;
- [ ] gate `GATE-GUION-CV-CONTENIDO`;
- [ ] gate evaluado por candidatura;
- [ ] artefacto separado de evaluación del gate;
- [ ] evaluación determinista;
- [ ] IA separada de aprobación humana;
- [ ] `CAND-2026-020` como prueba principal;
- [ ] `CAND-2026-019` como contraste;
- [ ] progresión `en_prueba → candidata a validada`;
- [ ] sincronización normativa de SPEC antes de implementación;
- [ ] autorización para planificar separada de autorización para implementar;
- [ ] responsabilidad y límites de Work.

Una vez aprobado:

> el siguiente paso será elaborar en Work un plan de implementación contra este contrato.

---

# 30. Decisiones consolidadas

Las decisiones `D-NN` son locales a este diseño.

Solo se promueven a `ARQ-NN` cuando afectan a la arquitectura general de `job-up`.

## D-01 — Adaptador exclusivo de CV

`PLAYBOOK_GUION_ADAPTACION_CV` gobierna únicamente el CV.

## D-02 — Estrategia común única

`candidatura.md` conserva la estrategia común.

## D-03 — Separación CV/carta decidida

La separación debe promoverse a decisión arquitectónica general.

## D-04 — Precedencia frente a `ARQ-09`

Una lectura de `ARQ-09` que obligue a fusionar CV y carta queda desplazada por la separación adoptada.

Su alcance residual permanece abierto.

## D-05 — Rama de carta diferida

Su arquitectura específica queda como incertidumbre no bloqueante.

## D-06 — Factualidad externa

El guion selecciona hechos; no los crea.

## D-07 — Contrato de fase explícito

La fase satisface los diez campos normativos de la SPEC.

## D-08 — Ejecución secuencial

El playbook sigue un orden normativo de dieciséis pasos.

## D-09 — Universo candidato acotado

No se barre indiscriminadamente todo el core.

## D-10 — Mapa multidimensional

Se separan:

```text
presencia
obligatoriedad
peso_editorial
```

## D-11 — Tipos y campos normalizados

El mapa utiliza una taxonomía preferente y semántica explícita para campos operativos.

## D-12 — Relevancia trazable

El contenido prioritario se relaciona con criterio objetivo y función estratégica.

## D-13 — Métrica como refuerzo

Una métrica acreditada refuerza evidencia comparable, pero no sustituye relevancia.

## D-14 — Seniority explícito

El guion debe decidir cómo tratar seniority sin modificar trayectoria histórica.

## D-15 — Tono editorial explícito

El tono forma parte de la instrucción editorial, no de la redacción final.

## D-16 — Primer escaneo gobernado

La adaptación debe prever la lectura inicial del recruiter.

## D-17 — Cobertura estratégica obligatoria

Ninguna prioridad de `candidatura.md` puede desaparecer silenciosamente.

## D-18 — Duplicación controlada

La misma evidencia solo se reutiliza cuando cada aparición cumple función diferente.

## D-19 — Cronología protegida

La relevancia no justifica una representación engañosa de la trayectoria.

## D-20 — Presupuesto editorial

El guion gestiona compresión relativa, pero no decide maquetación ni paginación exacta.

## D-21 — Brief derivado

El brief resume; no gobierna.

## D-22 — Corrección proporcional

Errores editoriales locales se corrigen localmente.

## D-23 — `DEF-ARQ-001` permanece abierto

El guion no resuelve propagación factual general.

## D-24 — Cambio material puede invalidar

La evaluación anterior del gate puede dejar de ser suficiente.

## D-25 — Gate legible

```text
GATE-GUION-CV-CONTENIDO
```

## D-26 — Estado del gate separado del guion

El guion referencia el gate.

El estado oficial vive en el artefacto de evaluación.

## D-27 — Evaluación determinista

Los tipos de incidencia producen resultados definidos.

## D-28 — IA evalúa, humano aprueba

La aprobación oficial no es automática.

## D-29 — Gate evaluado por candidatura

Validar la fase no aprueba automáticamente casos futuros.

## D-30 — Gate habilita diseño posterior

Mientras la siguiente fase no exista, no autoriza su ejecución.

## D-31 — Validación progresiva

```text
CAND-2026-020
→ en_prueba

CAND-2026-020 + CAND-2026-019
→ candidata a validada
```

## D-32 — Autorizaciones separadas

Diseño aprobado autoriza plan.

Plan aprobado + instrucción explícita autoriza ejecución.

## D-33 — SPEC se sincroniza antes de implementar

La implementación física del playbook no comienza bajo una SPEC contradictoria.

## D-34 — Work implementa, no rediseña

Los huecos arquitectónicos regresan a la capa de diseño.

---

# 31. Resumen operativo

```text
candidatura.md
        ↓
estrategia aprobada
        ↓
PLAYBOOK_GUION_ADAPTACION_CV
        ↓
universo candidato
        ↓
presencia
obligatoriedad
peso
función estratégica
criterio objetivo
cobertura
ubicación
orden
detalle
seniority
tono
léxico
límites
        ↓
guion-adaptacion-cv.md
        ↓
control de cobertura
control de duplicación
previsión de primer escaneo
control factual
control estratégico
        ↓
¿incidencia?
        │
        ├─ no
        │    ↓
        │  resultado: apto
        │    ↓
        │  recomendación IA
        │    ↓
        │  decisión humana por candidatura
        │    ↓
        │  evaluacion-gate-guion-cv-contenido.md
        │    ↓
        │  GATE-GUION-CV-CONTENIDO
        │
        └─ sí
             ↓
          clasificar incidencia
             ↓
          requiere_correccion
          requiere_revision_origen
          requiere_actualizacion_factual
          bloqueado
```

---

# 32. Registro formal de incertidumbres

Los identificadores son propuestas para la próxima actualización de la SPEC.

La numeración debe revalidarse antes de escribir.

## `INC-001` — Rama específica de carta pendiente de diseño

```text
ID: INC-001

elemento:
Arquitectura posterior de adaptación y generación
de la carta de presentación.

motivo:
La separación de responsabilidades CV/carta está decidida,
pero no es necesario diseñar la rama de carta para implementar
y probar PLAYBOOK_GUION_ADAPTACION_CV.

impacto:
Quedan deliberadamente sin decidir:
- playbook de adaptación de carta;
- template;
- gate;
- artefacto estratégico;
- fase de generación de contenido;
- infraestructura compartida o separada con CV;
- relación técnica entre ambas ramas.

bloquea_plan: false

resolucion_necesaria:
Antes de iniciar el diseño de la rama específica de carta
o de una infraestructura común CV/carta.
```

---

## `INC-002` — Semántica futura de `GATE-CANDIDATURA-GUION`

```text
ID: INC-002

elemento:
Semántica y posible especialización por rama
del gate GATE-CANDIDATURA-GUION.

motivo:
El gate fue aprobado cuando el guion de CV era la única rama diseñada.
La existencia futura de otros adaptadores plantea si debe seguir siendo
un gate común o existir un gate específico por rama.

impacto:
No afecta al guion de CV actual, pero puede afectar a futuros adaptadores.

bloquea_plan: false

resolucion_necesaria:
Antes de diseñar un segundo adaptador que consuma candidatura.md.
```

---

## `INC-003` — Alcance residual de `ARQ-09` y generación común

```text
ID: INC-003

elemento:
Alcance residual de ARQ-09 — Redacción única y de las referencias
actuales de la SPEC a generación común CV/carta.

motivo:
ARQ-22 establece ya que el guion de CV es exclusivo y que ninguna
lectura de ARQ-09 puede forzar una fase común CV/carta.

Sigue pendiente decidir qué significado residual conserva ARQ-09
y cómo será la futura arquitectura de generación.

impacto:
No bloquea PLAYBOOK_GUION_ADAPTACION_CV.

La SPEC debe dejar de utilizar ARQ-09 para inferir una obligación
de convergencia CV/carta.

bloquea_plan: false

resolucion_necesaria:
Antes de diseñar la futura fase de generación de contenido
o una infraestructura común CV/carta.
```

Ninguna incertidumbre autoriza a Work a elegir silenciosamente una solución.

---

# 33. Relación con defectos arquitectónicos abiertos

## `DEF-ARQ-001` — Propagación de cambios factuales

Estado heredado:

```text
clasificacion: ARQUITECTURA
estado: abierto
```

Este diseño:

- lo reconoce;
- lo referencia;
- evita contradecirlo;
- define la reacción local del guion.

Este diseño no:

- lo resuelve;
- lo cierra;
- define toda la propagación;
- autoriza implementación transversal.

Criterio de compatibilidad:

> `PLAYBOOK_GUION_ADAPTACION_CV` debe ser implementable sin que Work tenga que inventar la solución de `DEF-ARQ-001`.

Si esto deja de ser posible:

```text
bloqueo arquitectónico
→ regresar a diseño
```

---

# 34. Contrato mínimo de sincronización de la SPEC

Una vez este diseño sea aprobado y antes de implementar físicamente el playbook, el plan de Work debe contemplar una actualización acotada de la SPEC.

Work no decide el contenido de esa actualización.

Debe materializar las decisiones ya fijadas aquí.

## 34.1 Promover `ARQ-22`

Tras revalidar numeración, incorporar la decisión:

```text
Separación de responsabilidades CV/carta.
PLAYBOOK_GUION_ADAPTACION_CV es exclusivo del CV.
candidatura.md permanece como estrategia común.
```

Debe constar que cualquier lectura incompatible de `ARQ-09` queda subordinada a esta decisión.

---

## 34.2 Registrar incertidumbres

Incorporar formalmente, con numeración revalidada:

- rama de carta;
- semántica futura de `GATE-CANDIDATURA-GUION`;
- alcance residual de `ARQ-09` / generación común.

No resolverlas.

---

## 34.3 Actualizar el pipeline vigente

La SPEC no debe seguir presentando como hecho decidido que:

```text
guion-adaptacion-cv.md
→ una única generación común
→ CV + carta
```

cuando esa convergencia está sin diseñar.

La arquitectura normativa debe representar únicamente lo decidido:

```text
candidatura.md
        ↓
PLAYBOOK_GUION_ADAPTACION_CV
        ↓
guion-adaptacion-cv.md
        ↓
GATE-GUION-CV-CONTENIDO
        ↓
futura generación de contenido del CV
```

y registrar la rama de carta como pendiente.

---

## 34.4 Actualizar el contrato previsto del guion

La SPEC debe dejar de exigir al guion de CV una:

```text
relación estratégica CV/carta
```

Debe recoger en su lugar las responsabilidades aprobadas en este diseño, al menos:

- narrativa;
- gancho;
- seniority;
- tono;
- evidencia;
- énfasis;
- omisiones;
- carencias;
- palabras clave respaldadas;
- adaptación exclusiva de CV.

---

## 34.5 Registrar el gate de salida

Incorporar:

```text
GATE-GUION-CV-CONTENIDO
```

sin renombrar por ahora:

```text
GATE-CANDIDATURA-GUION
```

La futura semántica de este último permanece en `INC-002`.

---

## 34.6 Mantener `DEF-ARQ-001` abierto

La sincronización de la SPEC no debe:

- cerrarlo;
- introducir un contrato general de propagación;
- inferir automatizaciones aguas arriba o aguas abajo.

---

## 34.7 No diseñar fases futuras

La actualización de la SPEC puede:

- corregir arquitectura ya decidida;
- marcar fases pendientes;
- registrar incertidumbres.

No puede aprovecharse para diseñar:

- contenido final;
- JSON;
- composición;
- carta;
- generadores.

---

# 35. Principios finales

## Principio editorial

> El guion decide qué historia profesional debe hacer visible el CV y qué evidencia debe sostenerla, pero no redacta todavía el documento final.

## Principio estratégico

> La estrategia pertenece a `candidatura.md`; el guion no puede reinventarla para obtener un CV aparentemente mejor.

## Principio factual

> Lo que mejora el encaje mediante falsificación no es adaptación.

## Principio competitivo

> La seguridad factual no debe producir un CV débil: dentro de los hechos acreditados debe seleccionarse y jerarquizarse la evidencia con máxima capacidad de generar entrevista.

## Principio de selección

> El CV debe funcionar tanto bajo lectura completa como bajo el primer escaneo de un recruiter.

## Principio de cobertura

> Una adaptación no es correcta si conserva todos los hechos pero pierde silenciosamente una prioridad estratégica.

## Principio de seniority

> Adaptar el énfasis no autoriza a reescribir el nivel histórico de responsabilidad.

## Principio arquitectónico

> Un playbook local no debe apropiarse de la resolución de un defecto arquitectónico abierto.

## Principio de gobierno del gate

> El guion produce contenido editorial; el artefacto de evaluación gobierna el estado del gate.

## Principio agentic

> Una decisión que el agente tenga que adivinar es una decisión que el contrato todavía no ha especificado suficientemente.

## Principio de implementación

> Work materializa decisiones aprobadas; las incertidumbres y defectos arquitectónicos regresan a la capa que tiene autoridad para resolverlos.

---

# Changelog

## 0.3.4 — 2026-08-06

Versión final de diseño obtenida mediante revisión consolidada de `0.3.2` y `0.3.3` con tres roles: arquitecto senior de documentación y workflows agentic, recruiter senior + coach de carrera y AI workflow engineer.

Cambios principales:

- Se mantiene la referencia cruzada de precondiciones introducida en `0.3.3`, pero la sección 4 queda declarada como fuente normativa canónica para evitar divergencia entre listas duplicadas.
- Se incorpora explícitamente `tono` y tratamiento de `seniority`, requeridos por el contrato previsto de la fase y necesarios para adaptación competitiva.
- Se fija la precedencia de la separación CV/carta frente a cualquier interpretación incompatible de `ARQ-09`, manteniendo solo su alcance residual como `INC-003`.
- Se añade ausencia de investigación externa autónoma como frontera de autoridad.
- El orden normativo pasa a 16 pasos incorporando control de cobertura estratégica.
- Se normaliza el mapa editorial con referencias locales, tipos de contenido, función estratégica, ubicación, orden y niveles de detalle.
- Se define una jerarquía explícita para asignar peso editorial.
- Se mantiene la métrica como refuerzo o desempate, nunca como sustituto automático de relevancia.
- Se incorpora un control formal de cobertura estratégica para impedir pérdida silenciosa de prioridades de `candidatura.md`.
- Se incorpora control de duplicación de evidencia y keywords.
- Se añade gestión de presupuesto editorial sin invadir decisiones visuales ni de paginación.
- El primer escaneo queda definido como previsión editorial, diferenciándolo de la validación posterior del CV materializado.
- Se amplía el tratamiento de incidencias con `bloqueado` y una clasificación más determinista.
- Se define una regla de precedencia cuando concurren varias incidencias.
- Se elimina `estado_gate_salida` del contrato del guion como fuente normativa mutable.
- Se define un artefacto independiente `evaluacion-gate-guion-cv-contenido.md` para evaluación, recomendación, decisión humana y estado oficial del gate.
- Se añaden `version_diseno`, `version_playbook` y `version_template` a la trazabilidad del guion.
- Se refuerza `CAND-2026-020` con controles de seniority y cobertura.
- Se amplía el contraste de `CAND-2026-019` a tratamiento de vocabulario técnico y seniority.
- La implantación se divide en sincronización normativa, implementación, prueba principal y contraste de generalidad.
- Se exige sincronizar la SPEC antes de implementar físicamente el playbook, evitando que Work opere contra dos autoridades contradictorias.
- Se define de forma explícita el contrato mínimo de esa sincronización.
- `DEF-ARQ-001` permanece abierto y fuera del alcance de esta implementación.

## 0.3.3 — 2026-08-06

- Añadió referencia cruzada desde precondiciones operativas al contrato canónico de la sección 4.
- No introdujo otros cambios sustantivos sobre `0.3.2`.

## 0.3.2 — 2026-08-06

- Consolidó frontmatter estructurado, separación CV/carta, incertidumbres formales, relación con `DEF-ARQ-001`, gate por candidatura, Work como implementador no diseñador y validación progresiva con `CAND-2026-020` y `CAND-2026-019`.