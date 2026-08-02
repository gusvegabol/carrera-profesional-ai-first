---
id: [ID_CANDIDATURA]
tipo: candidatura
tipo_origen: [oferta / empresa_objetivo]
empresa: [EMPRESA]
puesto_objetivo: [PUESTO_O_AMBITO_OBJETIVO]
decision_estrategica: [DECISION]
estado: [en_preparacion / detenida / pendiente_de_aprobacion / aprobada / enviada / rechazada / duplicada / fallida]
presentada: false
fecha_creacion: [AAAA-MM-DD]
sesion_relacionada: [SESION_O_NO_ASIGNADA]
---
# Ficha de candidatura — [ID_CANDIDATURA]

> Esta ficha gobierna el ciclo de vida de la candidatura. No sustituye el análisis de origen ni los artefactos posteriores.

## 1. Identificación y origen

* **Identificador:** `[ID_CANDIDATURA]`
* **Tipo de origen:** `[oferta / empresa_objetivo]`
* **Empresa:** [EMPRESA]
* **Puesto o ámbito objetivo:** [PUESTO_O_AMBITO]
* **Fecha de creación:** [AAAA-MM-DD]
* **Sesión relacionada:** [SESION_O_NO_ASIGNADA]
* **Artefacto de análisis de origen:** [ENLACE]
* **Decisión estratégica heredada:** `[DECISION]`

## 2. Decisión y estrategia heredada

### 2.1 Justificación compacta

[SÍNTESIS_DE_POR_QUE_SE_CONTINUA_O_BAJO_QUE_CONDICIONES]

### 2.2 Ángulo de candidatura

[ARGUMENTO_COMPETITIVO_COMPACTO]

### 2.3 Posicionamiento

* **Principal:** [POSICIONAMIENTO]
* **Secundario:** [POSICIONAMIENTO_O_NO_APLICA]
* **A evitar:** [ENFOQUES_A_EVITAR]

## 3. Evidencias y límites

### 3.1 Evidencias prioritarias

| Evidencia      | Función en la candidatura                      |
| -------------- | ---------------------------------------------- |
| [ID_EVIDENCIA] | [POR_QUE_DEBE_ALIMENTAR_LAS_FASES_POSTERIORES] |

> No existe un número fijo de evidencias. Incluir únicamente las necesarias para sostener la estrategia.

### 3.2 Afirmaciones excluidas

| Afirmación que no debe aparecer | Motivo   | Alternativa permitida     |
| ------------------------------- | -------- | ------------------------- |
| [AFIRMACION]                    | [MOTIVO] | [ALTERNATIVA_O_NO_APLICA] |

## 4. Advertencias, datos pendientes y bloqueos

### 4.1 Advertencias activas

| Advertencia   | Tratamiento             |
| ------------- | ----------------------- |
| [ADVERTENCIA] | [COMO_DEBE_GESTIONARSE] |

Si no existen:

`ninguna`

### 4.2 Datos pendientes

| Dato   | Estado                                                | Impacto                         |
| ------ | ----------------------------------------------------- | ------------------------------- |
| [DATO] | [pendiente / confirmado / descartado / no_disponible] | [NO_BLOQUEANTE / FASE_AFECTADA] |

Si no existen:

`ninguno`

### 4.3 Bloqueos activos

| Bloqueo   | Fase afectada | Resolución necesaria |
| --------- | ------------- | -------------------- |
| [BLOQUEO] | [FASE]        | [RESOLUCION]         |

Si no existen:

`ninguno`

> Si existe un bloqueo activo que impida continuar, el estado de la candidatura debe ser `detenida`.

## 5. Estado operativo

* **Estado actual:** `[ESTADO]`
* **Presentada:** `[true / false]`
* **Última actualización:** [AAAA-MM-DD]
* **Próxima fase prevista:** [FASE]
* **Motivo del estado actual:** [EXPLICACION_COMPACTA]

### 5.1 Veredicto documental

* **Veredicto disponible:** [sí / no]
* **Enlace:** [ENLACE_O_NO_DISPONIBLE]
* **Decisión del veredicto:** [DECISION_O_NO_DISPONIBLE]

> La decisión del veredicto no sustituye la decisión estratégica de la candidatura.

## 6. Artefactos de la candidatura

| Artefacto                    | Estado                                                                                  | Enlace o ruta        |
| ---------------------------- | --------------------------------------------------------------------------------------- | -------------------- |
| Análisis de origen           | [completado]                                                                            | [ENLACE]             |
| Guion de adaptación del CV   | [no_iniciado / en_preparacion / completado / requiere_revision / bloqueado / no_aplica] | [ENLACE_O_PENDIENTE] |
| CV DOCX                      | [ESTADO]                                                                                | [RUTA_O_PENDIENTE]   |
| CV PDF                       | [ESTADO]                                                                                | [RUTA_O_PENDIENTE]   |
| CV TEX                       | [ESTADO]                                                                                | [RUTA_O_PENDIENTE]   |
| Carta DOCX                   | [ESTADO]                                                                                | [RUTA_O_PENDIENTE]   |
| Carta PDF                    | [ESTADO]                                                                                | [RUTA_O_PENDIENTE]   |
| Veredicto final del CV       | [ESTADO]                                                                                | [ENLACE_O_PENDIENTE] |
| Informe empresa / entrevista | [ESTADO / no_aplica]                                                                    | [ENLACE_O_PENDIENTE] |

> Añadir nuevos artefactos operativos si aparecen. No incluir capturas ni archivos internos de control.

## 7. Control de coherencia

* [ ] La decisión estratégica coincide con el artefacto de análisis de origen.
* [ ] La ficha no vuelve a analizar la oferta o empresa.
* [ ] Las evidencias mantienen trazabilidad factual.
* [ ] No existe un número fijo artificial de evidencias.
* [ ] Las afirmaciones excluidas permanecen visibles para las fases posteriores.
* [ ] Advertencias, datos pendientes y bloqueos están diferenciados.
* [ ] Todo bloqueo activo está reflejado en el estado.
* [ ] `presentada` refleja un hecho real y no una inferencia.
* [ ] El índice de artefactos refleja únicamente documentos realmente existentes o pendientes.
* [ ] Los enlaces existentes no están rotos.
* [ ] La ficha no duplica contenido completo de análisis, guion, CV, carta o veredicto.
* [ ] La próxima fase está claramente identificada.
