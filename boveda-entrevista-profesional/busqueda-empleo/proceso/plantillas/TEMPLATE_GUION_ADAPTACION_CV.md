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
  - "[ENLACE_A_DATOS_CORE]"
fecha_lectura_fuentes: "[AAAA-MM-DD]"
gate_entrada: GATE-CANDIDATURA-GUION
evaluacion_gate_entrada: "[ENLACE_A_EVALUACION_O_NO_APLICA]"
gate_salida: GATE-GUION-CV-CONTENIDO
---

# Guion de adaptación de CV — [ID_CANDIDATURA]

> Adaptador editorial exclusivo del CV. No sustituye la estrategia de `candidatura.md`, no redacta el CV final y no contiene el estado oficial del gate de salida.

## 1. Entrada validada y trazabilidad

| Elemento | Valor |
| --- | --- |
| Candidatura | [ID_CANDIDATURA] |
| Empresa / puesto | [EMPRESA] — [PUESTO] |
| Idioma del CV | `[CODIGO_IDIOMA]` |
| Autoridad usada para determinar idioma | [INSTRUCCION_EXPLICITA / REQUISITO_OFERTA / IDIOMA_INEQUIVOCO_OFERTA / CV_BASE_AUTORIZADO] |
| Gate de entrada | `GATE-CANDIDATURA-GUION: aprobado` |
| Candidatura de origen | [ENLACE] |
| Análisis de origen | [ENLACE] |
| Fuentes factuales | [ENLACES] |
| Fecha de lectura de fuentes | [AAAA-MM-DD] |
| Sesión | [SESION] |

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

Cada fila usa una referencia local `M-NNN`. Los campos no aplicables deben decir `no_aplica`.

Contrato de campos del mapa: `ref_local`, `contenido`, `tipo`, `evidencia`, `presencia`, `obligatoriedad`, `peso_editorial`, `criterio_objetivo`, `motivo`, `funcion_estrategica`, `seccion_destino`, `orden_en_seccion`, `nivel_detalle`, `limitaciones_redaccion` y `defecto_relacionado`.

| Ref. local | Contenido | Tipo | Evidencia | Presencia | Obligatoriedad | Peso editorial | Criterio objetivo | Motivo | Función estratégica | Sección destino | Orden en sección | Nivel detalle | Limitaciones de redacción | Defecto relacionado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M-001 | [CONTENIDO] | [perfil / titular / competencia / experiencia / cargo / funcion / responsabilidad / logro / resultado / metrica / herramienta / tecnologia / formacion / certificacion / idioma / proyecto / otro] | [ID_EVIDENCIA] | [incluir / omitir] | [obligatoria / opcional] | [alto / medio / bajo / minimo / no_aplica] | [REQUISITO, RESPONSABILIDAD, COMPETENCIA, SEÑAL O ARGUMENTO] | [MOTIVO_O_NO_APLICA] | [sostener_posicionamiento / demostrar_requisito / diferenciar / dar_continuidad / proteger_factualidad / mitigar_riesgo / respaldar_keyword] | [SEC-NN / no_aplica] | [NÚMERO / no_aplica] | [amplio / normal / breve / mencion / no_aplica] | [LÍMITE_O_no_aplica] | [DEF-ARQ-001 / no_aplica] |

### 3.1 Reglas aplicadas al mapa

* `obligatoria` implica `incluir`; `omitir` implica `opcional` y peso `no_aplica`.
* Todo contenido de peso `alto` o `medio` identifica el criterio que ayuda a demostrar.
* Las omisiones no pueden falsear, romper cronología necesaria ni ocultar una carencia relevante.
* El peso y el detalle son dimensiones independientes.
* Si aparece evidencia factual nueva, `defecto_relacionado: DEF-ARQ-001` es obligatorio; la unidad no puede incorporarse al mapa como hecho utilizable.

## 4. Experiencias, logros y contenidos seleccionados

### 4.1 Experiencias de mayor protagonismo

| Experiencia | Evidencia | Qué debe demostrar | Tratamiento |
| --- | --- | --- | --- |
| [EXPERIENCIA] | [ID] | [DEMANDA DEL PUESTO] | [ÉNFASIS, ORDEN Y DETALLE] |

### 4.2 Experiencias secundarias o de continuidad

| Experiencia | Evidencia | Función | Tratamiento |
| --- | --- | --- | --- |
| [EXPERIENCIA] | [ID] | [FUNCIÓN] | [RESUMIR, MENCIONAR O CONSERVAR] |

### 4.3 Logros y evidencias de impacto utilizables

| Logro o evidencia | Referencia factual | Uso permitido | Límite |
| --- | --- | --- | --- |
| [LOGRO] | [ID] | [USO] | [LÍMITE_O_no_aplica] |

## 5. Arquitectura editorial y presupuesto de contenido

| Sección | Objetivo | Contenido dominante | Profundidad relativa | Restricciones |
| --- | --- | --- | --- | --- |
| SEC-01 | [OBJETIVO] | [CONTENIDOS] | [ALTA / MEDIA / BAJA] | [RESTRICCIONES] |

* **Progresión narrativa:** [PROGRESIÓN].
* **Contenido que debe comprimirse:** [CONTENIDO].
* **Límite documental aplicable:** [LÍMITE_O_NO_DISPONIBLE].

## 6. Léxico respaldado

### 6.1 Utilizable

| Término | Evidencia factual | Uso |
| --- | --- | --- |
| [TÉRMINO] | [ID] | [CONTEXTO] |

### 6.2 Uso condicionado

| Término | Alcance permitido | Prohibición asociada |
| --- | --- | --- |
| [TÉRMINO] | [ALCANCE] | [LÍMITE] |

### 6.3 Prohibido

| Término o afirmación | Motivo | Alternativa permitida |
| --- | --- | --- |
| [TÉRMINO] | [MOTIVO] | [ALTERNATIVA_O_NO_APLICA] |

## 7. Carencias, advertencias y límites de redacción

| Elemento | Riesgo | Tratamiento editorial | Permitido | Prohibido |
| --- | --- | --- | --- | --- |
| [ELEMENTO] | [RIESGO] | [TRATAMIENTO] | [PERMITIDO] | [PROHIBIDO] |

## 8. Control editorial

### 8.1 Cobertura estratégica

| Prioridad de `candidatura.md` | Estado | Mapa relacionado | Justificación |
| --- | --- | --- | --- |
| [PRIORIDAD] | [cubierta / no_requiere_presencia_directa / no_cubierta_justificada / bloqueo] | [M-NNN] | [JUSTIFICACIÓN] |

### 8.2 Duplicación

| Evidencia | Apariciones permitidas | Función distinta de cada aparición | Acción |
| --- | --- | --- | --- |
| [ID] | [UBICACIONES] | [FUNCIONES] | [MANTENER / REDUCIR / ELIMINAR] |

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

| Incidencia | Clasificación | Defecto relacionado | Resultado requerido | Acción |
| --- | --- | --- | --- | --- |
| [INCIDENCIA_O_NINGUNA] | [editorial / origen / factual / bloqueo] | [DEF-ARQ-001 / no_aplica] | [requiere_correccion / requiere_revision_origen / requiere_actualizacion_factual / bloqueado / no_aplica] | [ACCIÓN] |

> Si surge evidencia factual nueva o contradictoria, no se parchea este guion: debe resolverse aguas arriba y producirse una **regeneración completa** desde la `candidatura.md` sincronizada. `DEF-ARQ-001` continúa abierto.

> Se registran todas las incidencias detectadas, aunque la precedencia del gate determine un único resultado global.

## 11. Control de coherencia previo a evaluación

* [ ] Gate de entrada aprobado y fuentes resolubles.
* [ ] No hay bloqueo activo ni hechos nuevos incorporados directamente.
* [ ] `idioma_cv` está determinado y posee autoridad explícita.
* [ ] El mapa contiene todos los campos obligatorios y las prioridades estratégicas tienen cobertura.
* [ ] Seniority, tono, léxico, carencias y exclusiones están tratados.
* [ ] No hay omisiones engañosas, duplicaciones injustificadas, carta ni redacción final del CV.
* [ ] El brief coincide con el cuerpo detallado.

## 12. Referencia a la evaluación del gate de salida

* **Artefacto de evaluación:** `evaluacion-gate-guion-cv-contenido.md`.
* **Regla:** la evaluación, recomendación, decisión humana y estado oficial de `GATE-GUION-CV-CONTENIDO` se registran exclusivamente en ese artefacto separado.
