---
id: PLAYBOOK_GUION_ADAPTACION_CV
version: 1.0.1
estado: en_prueba
alcance: exclusivo_cv
entrada: candidatura.md
salida: guion-adaptacion-cv.md
gate_entrada: GATE-CANDIDATURA-GUION
gate_salida: GATE-GUION-CV-CONTENIDO
template: TEMPLATE_GUION_ADAPTACION_CV_v2.md
version_template_esperada: 2.1
diseno_referencia: 2026-08-06-guion-adaptacion-cv-design-v0-3-4.md
---

# Playbook — Guion de adaptación de CV

## 1. Propósito y alcance

Este playbook transforma una estrategia de candidatura ya aprobada en un mapa editorial auditable para un CV concreto.

Produce:

`guion-adaptacion-cv.md`

No:

* produce el CV;
* modifica la estrategia;
* modifica hechos;
* redacta la carta;
* diseña la composición;
* genera formatos finales.

Es un adaptador exclusivo del CV.

`candidatura.md` mantiene la estrategia común.

Una futura carta tendrá su propio adaptador cuando se diseñe.

No se presupone ninguna arquitectura compartida entre ambos artefactos.

---

## 2. Autoridades y límites

| Fuente                   | Autoridad                                                                                      |
| ------------------------ | ---------------------------------------------------------------------------------------------- |
| `candidatura.md`         | Estrategia, posicionamiento, tesis, evidencias prioritarias, carencias, límites y exclusiones. |
| `datos-core-busqueda.md` | Hechos profesionales, cronología y evidencia factual.                                          |
| `analisis-oferta.md`     | Requisitos, señales de selección, contexto de oferta y trazabilidad.                           |

El playbook:

* no investiga externamente;
* no altera hechos;
* no reabre la estrategia;
* no diseña visualmente el CV;
* no genera formatos;
* no escribe carta;
* no genera JSON;
* no presenta candidaturas.

`DEF-ARQ-001` permanece:

```text
estado: abierto
```

Este playbook puede detectar novedades factuales y detener su incorporación local.

No define ni automatiza la propagación arquitectónica de esas novedades.

---

## 3. Precondiciones

Antes de iniciar deben cumplirse todas:

1. `GATE-CANDIDATURA-GUION` está aprobado por decisión humana para el caso.
2. `candidatura.md`, `analisis-oferta.md` y las fuentes factuales son resolubles.
3. No existe bloqueo activo.
4. La candidatura está vigente.
5. `presentada: false`.
6. La fase no contiene una contradicción normativa bloqueante.

Si falla una condición:

```text
PLAYBOOK_GUION_ADAPTACION_CV
→ no inicia
```

Una candidatura presentada solo puede utilizarse en prueba retrospectiva controlada.

No se reescribe su expediente histórico.

---

## 4. Procedimiento normativo — 17 pasos

El orden es obligatorio.

### Paso 1 — Validar precondiciones

Confirmar:

* gate;
* fuentes;
* bloqueo;
* vigencia;
* `presentada: false`.

### Paso 2 — Cargar estrategia heredada

Extraer sin modificar:

* posicionamiento;
* tesis;
* prioridades;
* riesgos;
* carencias;
* exclusiones;
* límites.

### Paso 3 — Resolver fuentes factuales

Leer las referencias autorizadas.

Ante contradicción real:

```text
→ detener decisión afectada
```

No escoger la fuente más conveniente.

### Paso 4 — Determinar `idioma_cv`

El guion debe producir una decisión explícita:

```text
idioma_cv
```

La decisión se obtiene aplicando, por orden:

1. instrucción explícita vigente de la candidatura o de la persona responsable;
2. requisito lingüístico explícito de la oferta;
3. idioma principal inequívoco de la oferta cuando no exista instrucción contraria;
4. idioma de un CV base vigente solo cuando esa regla esté documentada como autoridad del flujo.

Si dos opciones continúan siendo plausibles o existe contradicción:

```text
requiere_revision_origen
```

No se selecciona un idioma silenciosamente.

Valores recomendados:

```text
es
en
de
fr
...
```

preferentemente mediante código BCP 47 o ISO compatible con el flujo.

`idioma_cv` es una decisión editorial del documento.

No modifica la estrategia de candidatura.

### Paso 5 — Construir el universo candidato

Incluir únicamente contenido:

* señalado estratégicamente;
* plausible para selección;
* necesario para cronología;
* necesario para factualidad;
* sujeto a advertencia.

### Paso 6 — Decidir presencia

Valores:

```text
incluir
omitir
```

Una omisión no puede:

* falsear;
* romper cronología necesaria;
* ocultar una carencia relevante.

### Paso 7 — Decidir obligatoriedad

Valores:

```text
obligatoria
opcional
```

Reglas:

```text
obligatoria
→ incluir

omitir
→ opcional
```

### Paso 8 — Asignar peso editorial y función estratégica

Peso:

```text
alto
medio
bajo
minimo
no_aplica
```

Registrar una o varias funciones estratégicas.

### Paso 9 — Vincular contenido con criterio objetivo

Todo contenido con peso `alto` o `medio` debe identificar qué ayuda a demostrar:

* requisito;
* responsabilidad;
* competencia;
* señal de selección;
* argumento heredado.

### Paso 10 — Verificar cobertura estratégica

Para cada prioridad:

```text
cubierta
no_requiere_presencia_directa
no_cubierta_justificada
bloqueo
```

### Paso 11 — Decidir ubicación, orden y nivel de detalle

Cada unidad incluida debe vincularse cuando proceda a:

```text
SEC-NN
orden_en_seccion
amplio | normal | breve | mencion
```

### Paso 12 — Construir arquitectura narrativa

Definir:

* secciones;
* progresión;
* presupuesto editorial;
* contenido a comprimir.

No decidir:

* tipografía;
* columnas;
* márgenes;
* paginación exacta.

### Paso 13 — Definir seniority, tono, léxico y límites

Mantener:

* cargos históricos;
* responsabilidades reales;
* cronología.

Definir:

* seniority editorial;
* tono;
* léxico utilizable;
* léxico condicionado;
* léxico prohibido;
* límites de redacción.

### Paso 14 — Generar brief derivado

Resumir el cuerpo.

No:

* crear;
* modificar;
* eliminar decisiones.

### Paso 15 — Ejecutar control de primer escaneo

Comprobar que aparecen primero:

* perfil;
* encaje;
* dos o tres señales fuertes;

antes que:

* ruido;
* credenciales secundarias;
* sobrecualificación.

### Paso 16 — Ejecutar control de coherencia

Revisar:

* idioma;
* trazabilidad;
* cronología;
* cobertura;
* duplicación;
* restricciones;
* ausencia de redacción final.

### Paso 17 — Evaluar gate de salida

Crear o actualizar únicamente:

```text
evaluacion-gate-guion-cv-contenido.md
```

El estado oficial del gate nunca vive en el guion.

---

## 5. Taxonomía y reglas del mapa editorial

Cada unidad utiliza:

```text
M-NNN
```

Campos:

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
defecto_relacionado
```

Tipos preferentes:

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

## 5.1 Prioridad para decidir peso

Orden:

1. estrategia heredada;
2. requisitos o señales;
3. fuerza factual;
4. diferenciación;
5. primer escaneo;
6. especificidad del resultado.

Una métrica respaldada refuerza evidencia.

No reemplaza relevancia.

---

## 5.2 Campos no aplicables

Para contenido omitido:

```text
seccion_destino: no_aplica
orden_en_seccion: no_aplica
nivel_detalle: no_aplica
peso_editorial: no_aplica
```

El motivo es obligatorio para:

* omisiones;
* obligaciones;
* peso alto;
* peso medio.

Las limitaciones son obligatorias ante:

* advertencia;
* uso condicionado;
* riesgo de sobreafirmación.

---

## 6. Cronología, seniority y presupuesto

La adaptación puede modular:

* protagonismo;
* detalle;
* evidencia de apertura.

Debe preservar una trayectoria comprensible.

No altera:

* cargos;
* fechas;
* responsabilidades.

La evidencia de apertura domina la percepción inicial.

No obliga a alterar el orden cronológico.

Ante tensión de extensión, preservar por este orden:

1. contenido obligatorio;
2. evidencia de peso alto;
3. evidencia diferencial;
4. peso medio;
5. peso bajo;
6. peso mínimo.

Si la tensión no puede resolverse editorialmente:

```text
requiere_revision_origen
```

No se toma una decisión visual.

---

## 7. Léxico, carencias y restricciones

Clasificación:

```text
utilizable
uso_condicionado
prohibido
```

La cobertura de palabras clave no permite:

* keyword stuffing;
* afirmaciones falsas.

Toda carencia, advertencia, exclusión o riesgo se traduce a:

```text
elemento
riesgo
tratamiento
permitido
prohibido
```

El playbook no puede convertir:

* formación en experiencia;
* transferibilidad en experiencia literal;
* automatización en IA.

---

## 8. Incidencias, retroceso y regeneración

| Situación                                                                      | Resultado                        | Acción                                            |
| ------------------------------------------------------------------------------ | -------------------------------- | ------------------------------------------------- |
| Error editorial local sin cambio de hechos ni estrategia                       | `requiere_correccion`            | Corregir el guion.                                |
| Insuficiencia o contradicción entre autoridades que afecta estrategia          | `requiere_revision_origen`       | Detener y remitir a autoridad de origen.          |
| Idioma no determinable inequívocamente                                         | `requiere_revision_origen`       | Obtener decisión antes de producir el guion apto. |
| Evidencia factual nueva relevante                                              | `requiere_actualizacion_factual` | Registrar `DEF-ARQ-001`; no incorporar el hecho.  |
| Fuente inaccesible, gate no aprobado o contradicción arquitectónica bloqueante | `bloqueado`                      | No generar ni evaluar válidamente.                |

Ante evidencia factual nueva o contradicción:

```text
datos-core-busqueda.md
        ↓
analisis-oferta.md
        ↓
candidatura.md
        ↓
nueva validación
        ↓
nuevo guion
```

Tras sincronizarse el origen se exige regeneración completa.

No se parchean decisiones editoriales anteriores.

Una modificación material de:

* candidatura;
* análisis;
* evidencias prioritarias;
* posicionamiento;
* exclusiones;

puede invalidar el guion.

Esta reacción local no resuelve `DEF-ARQ-001`.

Toda incidencia se registra de forma estructurada.

Se registran todas, incluso si la precedencia determina un único resultado global.

---

## 9. Control previo al gate

Antes de evaluar comprobar:

* [ ] gate de entrada aprobado;
* [ ] fuentes resolubles;
* [ ] ausencia de bloqueo;
* [ ] estrategia intacta;
* [ ] `idioma_cv` determinado explícitamente;
* [ ] respaldo factual;
* [ ] mapa completo;
* [ ] cobertura estratégica;
* [ ] seniority explícito;
* [ ] tono explícito;
* [ ] léxico y límites explícitos;
* [ ] cronología honesta;
* [ ] omisiones no engañosas;
* [ ] duplicación controlada;
* [ ] primer escaneo competitivo;
* [ ] brief coherente;
* [ ] ausencia de CV final;
* [ ] ausencia de carta.

---

## 10. Gate de salida separado

Gate:

```text
GATE-GUION-CV-CONTENIDO
```

Valida que el guion permite generar contenido del CV sin reconstruir estrategia.

No valida:

* CV final;
* maquetación;
* ATS final;
* carta;
* envío.

Evaluación:

```text
evaluacion-gate-guion-cv-contenido.md
```

Campos:

```text
id
tipo
candidatura
gate
guion_evaluado
fecha_evaluacion
resultado_evaluacion
recomendacion_ia
decision_humana
estado_gate
fecha_decision_humana
sesion
```

Resultados:

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

La IA recomienda `aprobar` solo para `apto`.

La decisión humana y estado del gate:

```text
pendiente
aprobado
bloqueado
```

La aprobación del gate autoriza diseñar la fase posterior.

No autoriza ejecutarla mientras no exista su contrato.

---

## 11. Salida y comprobación final

La salida es:

```text
guion-adaptacion-cv.md
```

creada desde:

```text
TEMPLATE_GUION_ADAPTACION_CV_v2.md
version_template: 2.1
```

Debe contener:

* idioma del CV;
* referencias factuales;
* mapa completo;
* arquitectura editorial;
* controles;
* brief derivado.

Debe poder alimentar la generación de contenido sin:

* reabrir estrategia;
* volver a decidir idioma;
* inventar hechos.

---

# ARCHIVO 2 — `TEMPLATE_GUION_ADAPTACION_CV_v2.md`

---

id: "[ID_GUIÓN]"
tipo: guion_adaptacion_cv
version_diseno: 0.3.4
version_playbook: 1.0.1
version_template: 2.1
candidatura: "[ID_CANDIDATURA]"
empresa: "[EMPRESA]"
puesto: "[PUESTO]"
idioma_cv: "[CODIGO_IDIOMA]"
fecha_generacion: "[AAAA-MM-DD]"
sesion: "[SESION_O_NO_ASIGNADA]"
candidatura_origen: "[ENLACE_A_CANDIDATURA]"
analisis_origen: "[ENLACE_A_ANALISIS]"
fuentes_factuales:

* "[ENLACE_A_DATOS_CORE]"
  fecha_lectura_fuentes: "[AAAA-MM-DD]"
  gate_entrada: GATE-CANDIDATURA-GUION
  evaluacion_gate_entrada: "[ENLACE_A_EVALUACION_O_NO_APLICA]"
  gate_salida: GATE-GUION-CV-CONTENIDO

---

# Guion de adaptación de CV — [ID_CANDIDATURA]

> Adaptador editorial exclusivo del CV. No sustituye la estrategia de `candidatura.md`, no redacta el CV final y no contiene el estado oficial del gate de salida.

## 1. Entrada validada y trazabilidad

| Elemento                               | Valor                                                                                      |
| -------------------------------------- | ------------------------------------------------------------------------------------------ |
| Candidatura                            | [ID_CANDIDATURA]                                                                           |
| Empresa / puesto                       | [EMPRESA] — [PUESTO]                                                                       |
| Idioma del CV                          | `[CODIGO_IDIOMA]`                                                                          |
| Autoridad usada para determinar idioma | [INSTRUCCION_EXPLICITA / REQUISITO_OFERTA / IDIOMA_INEQUIVOCO_OFERTA / CV_BASE_AUTORIZADO] |
| Gate de entrada                        | `GATE-CANDIDATURA-GUION: aprobado`                                                         |
| Candidatura de origen                  | [ENLACE]                                                                                   |
| Análisis de origen                     | [ENLACE]                                                                                   |
| Fuentes factuales                      | [ENLACES]                                                                                  |
| Fecha de lectura de fuentes            | [AAAA-MM-DD]                                                                               |
| Sesión                                 | [SESION]                                                                                   |

## 2. Instrucción editorial heredada

* **Posicionamiento heredado:** [SIN REJUSTIFICARLO].
* **Mensaje profesional principal:** [MENSAJE].
* **Gancho heredado:** [GANCHO_O_NO_APLICA].
* **Objetivo del CV:** [OBJETIVO DE SELECCIÓN].
* **Idioma del CV:** [CODIGO_IDIOMA].
* **Percepción a provocar:** [PERCEPCIÓN].
* **Percepción a evitar:** [PERCEPCIÓN_O_NO_APLICA].

### 2.1 Seniority

* **Seniority histórico:** [HECHOS RESPALDADOS].
* **Seniority objetivo:** [NIVEL REAL DEL PUESTO].
* **Tratamiento editorial:** [CÓMO MODULAR EL ÉNFASIS SIN ALTERAR CARGOS, RESPONSABILIDADES NI CRONOLOGÍA].

### 2.2 Tono editorial

* **Descriptores:** [UNO A TRES DESCRIPTORES].
* **Justificación factual y estratégica:** [JUSTIFICACIÓN].

## 3. Mapa de edición

Cada fila usa una referencia local `M-NNN`.

Los campos no aplicables deben decir:

```text
no_aplica
```

Contrato:

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
defecto_relacionado
```

| Ref. local | Contenido   | Tipo                                                                                                                                                                                               | Evidencia      | Presencia          | Obligatoriedad           | Peso editorial                             | Criterio objetivo                                            | Motivo               | Función estratégica                                                                                                                          | Sección destino      | Orden en sección     | Nivel detalle                                   | Limitaciones de redacción | Defecto relacionado       |
| ---------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------ | ------------------------ | ------------------------------------------ | ------------------------------------------------------------ | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | -------------------- | ----------------------------------------------- | ------------------------- | ------------------------- |
| M-001      | [CONTENIDO] | [perfil / titular / competencia / experiencia / cargo / funcion / responsabilidad / logro / resultado / metrica / herramienta / tecnologia / formacion / certificacion / idioma / proyecto / otro] | [ID_EVIDENCIA] | [incluir / omitir] | [obligatoria / opcional] | [alto / medio / bajo / minimo / no_aplica] | [REQUISITO, RESPONSABILIDAD, COMPETENCIA, SEÑAL O ARGUMENTO] | [MOTIVO_O_NO_APLICA] | [sostener_posicionamiento / demostrar_requisito / diferenciar / dar_continuidad / proteger_factualidad / mitigar_riesgo / respaldar_keyword] | [SEC-NN / no_aplica] | [NÚMERO / no_aplica] | [amplio / normal / breve / mencion / no_aplica] | [LÍMITE_O_no_aplica]      | [DEF-ARQ-001 / no_aplica] |

### 3.1 Reglas aplicadas al mapa

* `obligatoria` implica `incluir`.
* `omitir` implica `opcional`.
* `omitir` implica peso `no_aplica`.
* Todo contenido de peso `alto` o `medio` identifica criterio objetivo.
* Las omisiones no pueden falsear ni romper cronología necesaria.
* Peso y detalle son dimensiones independientes.
* Si aparece evidencia factual nueva, `defecto_relacionado: DEF-ARQ-001` es obligatorio y la unidad no se convierte en hecho utilizable.

## 4. Experiencias, logros y contenidos seleccionados

### 4.1 Experiencias de mayor protagonismo

| Experiencia   | Evidencia | Qué debe demostrar   | Tratamiento                |
| ------------- | --------- | -------------------- | -------------------------- |
| [EXPERIENCIA] | [ID]      | [DEMANDA DEL PUESTO] | [ÉNFASIS, ORDEN Y DETALLE] |

### 4.2 Experiencias secundarias o de continuidad

| Experiencia   | Evidencia | Función   | Tratamiento                      |
| ------------- | --------- | --------- | -------------------------------- |
| [EXPERIENCIA] | [ID]      | [FUNCIÓN] | [RESUMIR, MENCIONAR O CONSERVAR] |

### 4.3 Logros y evidencias de impacto utilizables

| Logro o evidencia | Referencia factual | Uso permitido | Límite               |
| ----------------- | ------------------ | ------------- | -------------------- |
| [LOGRO]           | [ID]               | [USO]         | [LÍMITE_O_no_aplica] |

## 5. Arquitectura editorial y presupuesto de contenido

| Sección | Objetivo   | Contenido dominante | Profundidad relativa  | Restricciones   |
| ------- | ---------- | ------------------- | --------------------- | --------------- |
| SEC-01  | [OBJETIVO] | [CONTENIDOS]        | [ALTA / MEDIA / BAJA] | [RESTRICCIONES] |

* **Progresión narrativa:** [PROGRESIÓN].
* **Contenido que debe comprimirse:** [CONTENIDO].
* **Límite documental aplicable:** [LÍMITE_O_NO_DISPONIBLE].

## 6. Léxico respaldado

### 6.1 Utilizable

| Término   | Evidencia factual | Uso        |
| --------- | ----------------- | ---------- |
| [TÉRMINO] | [ID]              | [CONTEXTO] |

### 6.2 Uso condicionado

| Término   | Alcance permitido | Prohibición asociada |
| --------- | ----------------- | -------------------- |
| [TÉRMINO] | [ALCANCE]         | [LÍMITE]             |

### 6.3 Prohibido

| Término o afirmación | Motivo   | Alternativa permitida     |
| -------------------- | -------- | ------------------------- |
| [TÉRMINO]            | [MOTIVO] | [ALTERNATIVA_O_NO_APLICA] |

## 7. Carencias, advertencias y límites de redacción

| Elemento   | Riesgo   | Tratamiento editorial | Permitido   | Prohibido   |
| ---------- | -------- | --------------------- | ----------- | ----------- |
| [ELEMENTO] | [RIESGO] | [TRATAMIENTO]         | [PERMITIDO] | [PROHIBIDO] |

## 8. Control editorial

### 8.1 Cobertura estratégica

| Prioridad de `candidatura.md` | Estado                                                                         | Mapa relacionado | Justificación   |
| ----------------------------- | ------------------------------------------------------------------------------ | ---------------- | --------------- |
| [PRIORIDAD]                   | [cubierta / no_requiere_presencia_directa / no_cubierta_justificada / bloqueo] | [M-NNN]          | [JUSTIFICACIÓN] |

### 8.2 Duplicación

| Evidencia | Apariciones permitidas | Función distinta de cada aparición | Acción                          |
| --------- | ---------------------- | ---------------------------------- | ------------------------------- |
| [ID]      | [UBICACIONES]          | [FUNCIONES]                        | [MANTENER / REDUCIR / ELIMINAR] |

### 8.3 Previsión de primer escaneo

* **Perfil identificable de inmediato:** [SÍ / NO Y EVIDENCIA].
* **Dos o tres señales fuertes visibles:** [SEÑALES].
* **Riesgo de sobrecualificación controlado:** [TRATAMIENTO].
* **Credenciales o keywords que no deben dominar:** [ELEMENTOS].

## 9. Brief cerrado para la futura generación de contenido del CV

* **Idioma del CV:** [CODIGO_IDIOMA].
* **Objetivo y posicionamiento:** [SÍNTESIS DERIVADA].
* **Gancho, seniority y tono:** [SÍNTESIS DERIVADA].
* **Contenidos y evidencias prioritarias:** [M-NNN].
* **Arquitectura y contenido a minimizar:** [SÍNTESIS DERIVADA].
* **Léxico, restricciones y riesgos:** [SÍNTESIS DERIVADA].

> Este brief resume el cuerpo del guion. En caso de discrepancia prevalece el cuerpo detallado y la discrepancia debe corregirse antes de la evaluación.

## 10. Incidencias e invalidación

| Incidencia             | Clasificación                            | Defecto relacionado       | Resultado requerido                                                                                       | Acción   |
| ---------------------- | ---------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------- | -------- |
| [INCIDENCIA_O_NINGUNA] | [editorial / origen / factual / bloqueo] | [DEF-ARQ-001 / no_aplica] | [requiere_correccion / requiere_revision_origen / requiere_actualizacion_factual / bloqueado / no_aplica] | [ACCIÓN] |

> Si surge evidencia factual nueva o contradictoria, no se parchea este guion: debe resolverse aguas arriba y producirse una regeneración completa desde la `candidatura.md` sincronizada. `DEF-ARQ-001` continúa abierto.

> Se registran todas las incidencias detectadas aunque la precedencia del gate determine un único resultado global.

## 11. Control de coherencia previo a evaluación

* [ ] Gate de entrada aprobado y fuentes resolubles.
* [ ] No hay bloqueo activo ni hechos nuevos incorporados directamente.
* [ ] `idioma_cv` está determinado y posee autoridad explícita.
* [ ] El mapa contiene todos los campos obligatorios.
* [ ] Las prioridades estratégicas tienen cobertura.
* [ ] Seniority, tono, léxico, carencias y exclusiones están tratados.
* [ ] No hay omisiones engañosas.
* [ ] No hay duplicaciones injustificadas.
* [ ] No hay carta.
* [ ] No hay redacción final del CV.
* [ ] El brief coincide con el cuerpo detallado.

## 12. Referencia a la evaluación del gate de salida

* **Artefacto de evaluación:** `evaluacion-gate-guion-cv-contenido.md`.
* **Regla:** evaluación, recomendación, decisión humana y estado oficial de `GATE-GUION-CV-CONTENIDO` se registran exclusivamente en ese artefacto separado.
