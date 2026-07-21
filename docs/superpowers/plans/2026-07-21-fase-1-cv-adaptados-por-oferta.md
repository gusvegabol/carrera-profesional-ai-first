# Fase 1 — CV adaptados por oferta Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Habilitar un flujo trazable que convierta el texto de una oferta en un CV y una carta adaptados en DOCX y PDF, sin modificar la investigación de entrevista.

**Architecture:** La fase 1 se apoya en `datos-core-busqueda.md` como fuente factual y añade una ficha privada, un registro de seguimiento y plantillas de análisis y candidatura. Un playbook conecta esos artefactos: analiza la oferta, selecciona evidencia, genera los documentos y registra el resultado; la validación final usa una oferta real aportada por la persona responsable.

**Tech Stack:** Markdown y YAML para la bóveda; Microsoft Word (`.docx`) y PDF para los entregables; las skills `documents:documents` y `pdf:pdf` para crear y verificar documentos cuando se ejecute una candidatura real.

## Global Constraints

- La rama consume `boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda.md` como fuente factual profesional.
- No modifica el SPEC, los playbooks ni los criterios de validación de la entrevista.
- No infiere responsabilidades, titulaciones, niveles de idioma, tecnologías vigentes ni métricas no confirmadas.
- No envía candidaturas en fase 1.
- La información de contacto se almacena fuera de la matriz profesional.
- Cada candidatura genera DOCX editable y PDF, además de una entrada de seguimiento.
- La validación de extremo a extremo se realiza solo con una oferta real que aporte la persona responsable.

---

### Task 1: Crear los registros privados y de seguimiento

**Files:**
- Create: `boveda-entrevista-profesional/busqueda-empleo/datos-privados-candidatura.md`
- Create: `boveda-entrevista-profesional/busqueda-empleo/seguimiento-candidaturas.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda.md`

**Interfaces:**
- Consumes: la separación de datos definida en `docs/superpowers/specs/2026-07-21-proceso-cv-adaptados-oferta-design.md`.
- Produces: una ficha privada sin datos inventados y un registro de estados compatible con una candidatura identificada como `CAND-YYYY-NNN`.

- [ ] **Step 1: Crear la ficha privada como plantilla vacía.**

  Incluir únicamente campos vacíos para nombre completo, correo, teléfono, localidad, enlace profesional, disponibilidad y consentimiento de uso para candidaturas. Añadir una regla visible: estos datos no se copian a `datos-core-busqueda.md` ni se usan fuera de una candidatura aprobada.

- [ ] **Step 2: Crear el registro de seguimiento.**

  Incluir una tabla con las columnas: `id_candidatura`, `fecha`, `empresa`, `puesto`, `enlace`, `perfil_principal`, `encaje`, `estado`, `cv_docx`, `cv_pdf`, `carta_docx`, `carta_pdf`, `motivo_bloqueo` y `observaciones`. Definir los estados permitidos: `preparada`, `pendiente_de_aprobacion`, `aprobada`, `enviada`, `detenida`, `duplicada` y `fallida`.

- [ ] **Step 3: Enlazar el uso de ambos registros desde la matriz.**

  Añadir al protocolo de adaptación de `datos-core-busqueda.md` una referencia a la ficha privada y al seguimiento, indicando que la matriz sigue siendo exclusivamente factual y profesional.

- [ ] **Step 4: Verificar separación y formato.**

  Ejecutar `rg -n 'correo|teléfono|dirección|credencial|contraseña' boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda.md` y confirmar que no devuelve datos personales. Ejecutar `git diff --check -- boveda-entrevista-profesional/busqueda-empleo` y revisar el diff.

- [ ] **Step 5: Commit.**

  Ejecutar `git add boveda-entrevista-profesional/busqueda-empleo/datos-privados-candidatura.md boveda-entrevista-profesional/busqueda-empleo/seguimiento-candidaturas.md boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda.md` y `git commit -m "docs: añade registros de candidatura"`.

### Task 2: Crear las plantillas de análisis y de candidatura

**Files:**
- Create: `boveda-entrevista-profesional/busqueda-empleo/templates/TEMPLATE_ANALISIS_OFERTA.md`
- Create: `boveda-entrevista-profesional/busqueda-empleo/templates/TEMPLATE_CANDIDATURA.md`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/README.md`

**Interfaces:**
- Consumes: el texto de una oferta y las evidencias identificadas en `datos-core-busqueda.md`.
- Produces: un análisis factual de oferta y una carpeta `candidaturas/CAND-YYYY-NNN-slug/` con cuatro documentos de salida.

- [ ] **Step 1: Crear la plantilla de análisis de oferta.**

  Incluir campos para texto fuente, empresa, puesto, tipo de oferta, salario, modalidad, zona geográfica, jornada, contrato, funciones, requisitos, perfil principal, perfil secundario, nivel de encaje, logros seleccionados, afirmaciones excluidas y dudas que bloquean la generación.

- [ ] **Step 2: Crear la plantilla de candidatura.**

  Incluir identificador `CAND-YYYY-NNN`, enlace al análisis, perfil seleccionado, lista de tres a cinco logros utilizados, lista de afirmaciones descartadas, estado, rutas de los cuatro documentos, fecha de preparación y revisión humana requerida antes de cualquier envío.

- [ ] **Step 3: Definir el contenido de la carpeta de candidatura.**

  En `candidaturas/README.md`, establecer que cada carpeta contiene exactamente `cv.docx`, `cv.pdf`, `carta-presentacion.docx` y `carta-presentacion.pdf`, además del análisis Markdown y la ficha de candidatura. Prohibir guardar credenciales o datos no necesarios.

- [ ] **Step 4: Verificar trazabilidad.**

  Ejecutar `rg -n 'perfil principal|perfil secundario|logros|afirmaciones|revisión humana' boveda-entrevista-profesional/busqueda-empleo/templates` y confirmar que ambos templates incluyen los campos requeridos.

- [ ] **Step 5: Commit.**

  Ejecutar `git add boveda-entrevista-profesional/busqueda-empleo/templates boveda-entrevista-profesional/busqueda-empleo/candidaturas/README.md` y `git commit -m "docs: define plantillas de candidatura"`.

### Task 3: Documentar el playbook operativo de fase 1

**Files:**
- Create: `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md`
- Modify: `.pcs/acciones/ACC-20260721-1651-001-activar-rama-operativa-busqueda-empleo-fase-1.md`

**Interfaces:**
- Consumes: la matriz factual, la ficha privada, el registro de seguimiento y las dos plantillas.
- Produces: instrucciones operativas que convierten una oferta en documentos revisables y una acción PCS actualizada con el progreso.

- [ ] **Step 1: Escribir las reglas de entrada y descarte.**

  Establecer que la entrada es el texto completo de una oferta. Clasificar como `fuerte`, `parcial` o `sin_encaje`; descartar automáticamente solo `sin_encaje`. Mostrar salario, modalidad, zona, jornada y contrato sin excluir automáticamente por esos campos.

- [ ] **Step 2: Escribir el procedimiento de selección factual.**

  Exigir un perfil principal, uno secundario y de tres a cinco logros del banco. Exigir que toda frase del CV y de la carta se pueda rastrear a la matriz, y que las decisiones colegiadas, estudios no finalizados, nivel de idiomas y tecnología histórica mantengan sus límites.

- [ ] **Step 3: Escribir el procedimiento de producción documental.**

  Indicar que la generación usa la skill `documents:documents` para crear DOCX y la skill `pdf:pdf` para exportar y verificar PDF. Incluir el orden fijo: preparar texto, revisión factual, crear DOCX, exportar PDF, comprobar visualmente ambos, registrar rutas y marcar la candidatura como `pendiente_de_aprobacion`.

- [ ] **Step 4: Escribir los bloqueos y la revisión humana.**

  Detener la producción cuando falte información factual, una oferta exija una capacidad no documentada, exista contradicción de fechas o la información privada no esté autorizada. La fase 1 termina en documentos preparados; no incluye envío.

- [ ] **Step 5: Actualizar la acción PCS.**

  Cambiar el próximo paso de la acción a «ejecutar una prueba con una oferta real» cuando el playbook y las plantillas estén creados. Mantener el estado `en_curso` hasta completar la prueba de extremo a extremo.

- [ ] **Step 6: Verificar enlaces y límites.**

  Ejecutar `rg -n 'enviar candidaturas|sin aprobación|sin_encaje|pendiente_de_aprobacion|DOCX|PDF' docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md` y revisar que el playbook no autoriza envíos.

- [ ] **Step 7: Commit.**

  Ejecutar `git add docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md .pcs/acciones/ACC-20260721-1651-001-activar-rama-operativa-busqueda-empleo-fase-1.md` y `git commit -m "docs: define playbook de candidatura por oferta"`.

### Task 4: Validar el flujo con una oferta real

**Files:**
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-YYYY-NNN-slug/analisis-oferta.md`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-YYYY-NNN-slug/candidatura.md`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-YYYY-NNN-slug/cv.docx`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-YYYY-NNN-slug/cv.pdf`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-YYYY-NNN-slug/carta-presentacion.docx`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-YYYY-NNN-slug/carta-presentacion.pdf`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/seguimiento-candidaturas.md`
- Modify: `.pcs/acciones/ACC-20260721-1651-001-activar-rama-operativa-busqueda-empleo-fase-1.md`

**Interfaces:**
- Consumes: una oferta real pegada por la persona responsable y los artefactos creados en las tareas 1–3.
- Produces: una candidatura preparada, no enviada, y evidencia de que el flujo puede reutilizarse.

- [ ] **Step 1: Solicitar una oferta real.**

  Pedir el texto completo de la oferta y no fabricar una oferta de prueba. Asignar el siguiente identificador disponible `CAND-YYYY-NNN` y un slug derivado del puesto y la empresa.

- [ ] **Step 2: Completar el análisis de oferta.**

  Extraer todos los campos de `TEMPLATE_ANALISIS_OFERTA.md`, clasificar el encaje y seleccionar el perfil, los logros y las afirmaciones excluidas. Si aparece un vacío factual, detenerse y formular una pregunta de entrevista.

- [ ] **Step 3: Crear los documentos con verificación visual.**

  Usar `documents:documents` para generar los dos DOCX y `pdf:pdf` para exportar, renderizar y revisar los dos PDF. Confirmar que los cuatro documentos contienen solo afirmaciones rastreables hasta la matriz y que el diseño se lee correctamente.

- [ ] **Step 4: Registrar sin enviar.**

  Crear `candidatura.md`, insertar una fila en `seguimiento-candidaturas.md` con estado `pendiente_de_aprobacion` y enlazar los cuatro archivos. No abrir ni completar formularios externos.

- [ ] **Step 5: Verificar el criterio de cierre.**

  Confirmar que existen los cuatro documentos, que el análisis enlaza a la matriz, que el registro no duplica una candidatura previa y que no se ha producido ningún envío. Mostrar la candidatura a la persona responsable para revisión.

- [ ] **Step 6: Actualizar la acción PCS y commit.**

  Si la persona responsable valida los documentos y la trazabilidad, marcar la acción `completada`, registrar la evidencia de cierre y ejecutar `git add boveda-entrevista-profesional/busqueda-empleo/candidaturas boveda-entrevista-profesional/busqueda-empleo/seguimiento-candidaturas.md .pcs/acciones/ACC-20260721-1651-001-activar-rama-operativa-busqueda-empleo-fase-1.md` seguido de `git commit -m "docs: valida fase 1 de candidatura por oferta"`.
