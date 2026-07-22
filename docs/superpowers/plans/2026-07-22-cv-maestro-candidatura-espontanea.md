# CV maestro para candidatura espontánea Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crear un CV maestro de dos páginas y un email modular en español para presentar el perfil de Job-up sin depender de una oferta concreta.

**Architecture:** Los materiales generales vivirán separados de las carpetas de candidaturas por oferta, bajo `presentacion-espontanea/`. El CV integrará Dirección (Management), Administración y Operaciones mediante evidencia factual de la matriz; el email Markdown contendrá tres variantes de destinatario que reutilizan el mismo núcleo factual.

**Tech Stack:** Markdown y YAML en la bóveda; Microsoft Word (`.docx`) y PDF para el CV; las skills `documents:documents` y `pdf:pdf` para crear, renderizar y verificar los documentos.

## Global Constraints

- Usar exclusivamente `boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda.md` como fuente de afirmaciones profesionales.
- Consultar `boveda-entrevista-profesional/busqueda-empleo/datos-privados-candidatura.md` solo para datos de contacto autorizados.
- Redactar en español y limitar el CV a dos páginas.
- Integrar Dirección (Management), Administración y Operaciones sin crear tres CV independientes ni dar prioridad permanente a una sola área.
- Redactar en primera persona las acciones de la persona candidata, por ejemplo: «Conseguí», «Reformulé», «Automaticé» y «Clasifiqué».
- No inferir responsabilidades, métricas, titulaciones, idiomas, tecnologías ni competencias no confirmadas.
- No enviar emails ni compartir documentos sin aprobación humana explícita.
- No modificar el SPEC, los playbooks ni la investigación metodológica de entrevista.

---

### Task 1: Crear el espacio de materiales generales y la plantilla de email

**Files:**
- Create: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/README.md`
- Create: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/email-presentacion.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/README.md`

**Interfaces:**
- Consumes: `datos-core-busqueda.md`, `datos-privados-candidatura.md` y el diseño `docs/superpowers/specs/2026-07-22-cv-maestro-candidatura-espontanea-design.md`.
- Produces: una ubicación estable para el CV maestro y un email reutilizable sin datos personales o afirmaciones inventadas.

- [ ] **Step 1: Crear `presentacion-espontanea/README.md`.**

  Documentar que esta carpeta contiene materiales generales de Job-up, no una candidatura a una oferta. Enumerar los tres artefactos base: `cv-maestro.docx`, `cv-maestro.pdf` y `email-presentacion.md`; añadir que, solo si un destinatario lo solicita, podrán crearse `carta-presentacion.docx` y `carta-presentacion.pdf`. Indicar que todo envío o compartición requiere aprobación humana explícita.

- [ ] **Step 2: Crear `email-presentacion.md` con tres variantes completas.**

  Incluir una sección de núcleo común y tres secciones tituladas `Empresa concreta`, `Intermediario de colocación` y `Contacto personal`. Cada variante debe contener: asunto, saludo, apertura, propuesta de valor de tres a cuatro líneas en primera persona, petición o disponibilidad, cierre y la indicación `Adjunto mi CV`. Mantener los campos de personalización entre corchetes solo para empresa, persona destinataria y motivo de contacto; no usar marcadores para hechos profesionales.

- [ ] **Step 3: Enlazar la carpeta desde el README de Job-up.**

  Añadir un enlace `[[presentacion-espontanea/README|Materiales para candidatura espontánea]]` dentro de `## Trabajo diario`, explicando en una frase que contiene el CV maestro y el email modular no vinculados a una oferta.

- [ ] **Step 4: Verificar contenido y límites.**

  Ejecutar `rg -n 'Empresa concreta|Intermediario de colocación|Contacto personal|Adjunto mi CV|primera persona|enviar|aproba' boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea` y confirmar que existen las tres variantes y el control de aprobación. Ejecutar `git diff --check -- boveda-entrevista-profesional/busqueda-empleo` y confirmar que no hay errores de espacios.

- [ ] **Step 5: Commit.**

  Ejecutar `git add boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/README.md boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/email-presentacion.md boveda-entrevista-profesional/busqueda-empleo/README.md` y `git commit -m "docs: añade materiales de candidatura espontánea"`.

### Task 2: Seleccionar y validar la evidencia del CV maestro

**Files:**
- Create: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/seleccion-factual.md`
- Read: `boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda.md`
- Read when contact details are needed: `boveda-entrevista-profesional/busqueda-empleo/datos-privados-candidatura.md`

**Interfaces:**
- Consumes: la matriz factual y, únicamente para el encabezado, los datos de contacto autorizados.
- Produces: un guion rastreable con el titular, resumen, áreas de contribución, experiencias, logros seleccionados y afirmaciones descartadas que alimentará el CV y el email.

- [ ] **Step 1: Leer la matriz factual y extraer evidencia.**

  Registrar en `seleccion-factual.md` los hechos disponibles para Dirección (Management), Administración y Operaciones. Para cada hecho elegido, anotar su sección de origen en `datos-core-busqueda.md` y su uso previsto: titular, resumen, área de contribución, experiencia o email.

- [ ] **Step 2: Definir la identidad profesional integrada.**

  Redactar un titular y un resumen de valor que conecten las tres áreas sin indicar que son tres perfiles independientes. Seleccionar experiencia y logros suficientes para ocupar dos páginas; expresar las acciones de la persona candidata en primera persona y excluir las que no tengan evidencia verificable.

- [ ] **Step 3: Preparar los límites factuales.**

  Crear una tabla `Afirmación descartada | Motivo` que recoja cualquier métrica, responsabilidad, titulación, idioma, tecnología o dato de contacto no confirmado. Si la evidencia no alcanza para sostener una de las tres áreas, detener la tarea y solicitar una precisión a la persona responsable antes de producir el CV.

- [ ] **Step 4: Verificar la selección.**

  Ejecutar `rg -n 'Dirección|Management|Administración|Operaciones|primera persona|Afirmación descartada' boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/seleccion-factual.md` y revisar que las tres áreas y la tabla de exclusiones están presentes. Comparar cada afirmación final con su sección de origen en `datos-core-busqueda.md`.

- [ ] **Step 5: Commit.**

  Ejecutar `git add boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/seleccion-factual.md` y `git commit -m "docs: selecciona evidencia para CV maestro"`.

### Task 3: Producir el CV maestro editable y su PDF

**Files:**
- Create: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/cv-maestro.docx`
- Create: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/cv-maestro.pdf`
- Read: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/seleccion-factual.md`

**Interfaces:**
- Consumes: el guion factual validado de `seleccion-factual.md`.
- Produces: un CV maestro editable de dos páginas y un PDF visualmente verificado, listo para revisión humana pero no para envío automático.

- [ ] **Step 1: Cargar las instrucciones de creación documental.**

  Leer la skill `documents:documents` completa antes de crear el DOCX y seguir su procedimiento de renderizado y verificación. Leer la skill `pdf:pdf` completa antes de generar o inspeccionar el PDF.

- [ ] **Step 2: Crear `cv-maestro.docx`.**

  Aplicar la estructura exacta: encabezado con datos autorizados, titular integrado, resumen de valor, áreas de contribución, experiencia cronológica, competencias o herramientas confirmadas, formación e idiomas confirmados. Mantener las acciones en primera persona y eliminar cualquier afirmación recogida como descartada en `seleccion-factual.md`.

- [ ] **Step 3: Generar y renderizar `cv-maestro.pdf`.**

  Exportar el DOCX a PDF. Renderizar las dos páginas y comprobar que no hay texto cortado, bloques solapados, viudas visuales, elementos fuera de margen ni tercera página. Si el contenido supera dos páginas, acortar el resumen o eliminar detalles redundantes sin eliminar las tres áreas profesionales.

- [ ] **Step 4: Verificar rigor y presentación.**

  Revisar el DOCX y el PDF contra `seleccion-factual.md`. Confirmar que cada verbo de acción de la persona candidata está en primera persona, que Dirección (Management), Administración y Operaciones son visibles y que no se añadieron hechos no rastreables. Solicitar la revisión humana de la persona responsable antes de compartir el documento.

- [ ] **Step 5: Commit.**

  Ejecutar `git add boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/cv-maestro.docx boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/cv-maestro.pdf` y `git commit -m "docs: crea CV maestro de Job-up"`.

### Task 4: Completar y validar el email modular

**Files:**
- Modify: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/email-presentacion.md`
- Read: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/seleccion-factual.md`

**Interfaces:**
- Consumes: la evidencia seleccionada y el CV maestro aprobado para revisión.
- Produces: tres emails listos para personalizar, con el mismo núcleo factual que el CV y conversión directa a carta formal cuando sea solicitada.

- [ ] **Step 1: Sustituir el núcleo genérico por evidencia seleccionada.**

  Redactar el bloque común con tres o cuatro líneas en primera persona que resuman Dirección (Management), Administración y Operaciones. Usar únicamente afirmaciones incluidas en `seleccion-factual.md`.

- [ ] **Step 2: Completar las tres variantes.**

  Para `Empresa concreta`, dejar personalizables el nombre de la empresa, el destinatario y el motivo de contacto. Para `Intermediario de colocación`, pedir consideración para oportunidades compatibles. Para `Contacto personal`, pedir difusión o una conexión pertinente sin presuponer que la persona conoce una vacante.

- [ ] **Step 3: Documentar la conversión a carta formal.**

  Añadir una sección `Conversión a carta formal` que indique: conservar el núcleo factual, sustituir el asunto por fecha y destinatario, usar saludo formal, mantener el cierre y copiar el contenido a un DOCX solo si se solicita. Prohibir añadir hechos durante la conversión.

- [ ] **Step 4: Verificar las variantes.**

  Ejecutar `rg -n 'Empresa concreta|Intermediario de colocación|Contacto personal|Conversión a carta formal|Conseguí|Reformulé|Automaticé|Clasifiqué' boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/email-presentacion.md`. Confirmar que cada variante incluye asunto, saludo, propuesta de valor, cierre y `Adjunto mi CV`, y revisar que no se ha incluido una afirmación ausente de `seleccion-factual.md`.

- [ ] **Step 5: Commit.**

  Ejecutar `git add boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/email-presentacion.md` y `git commit -m "docs: completa email modular de Job-up"`.

### Task 5: Revisión de aceptación y entrega para aprobación humana

**Files:**
- Modify: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/README.md`
- Read: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/cv-maestro.docx`
- Read: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/cv-maestro.pdf`
- Read: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/email-presentacion.md`
- Read: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/seleccion-factual.md`

**Interfaces:**
- Consumes: los cuatro materiales generales terminados.
- Produces: una lista de comprobación con resultado explícito y materiales presentados para aprobación humana; no produce envíos ni inscripciones.

- [ ] **Step 1: Añadir lista de aceptación en el README.**

  Añadir una sección `## Revisión antes de compartir` con estas casillas: CV en español y dos páginas; tres áreas visibles; verbos de acción en primera persona; afirmaciones rastreables; tres variantes de email; datos de contacto autorizados; revisión humana realizada; aprobación explícita antes de compartir.

- [ ] **Step 2: Ejecutar la revisión documental y visual.**

  Revisar el contenido del DOCX, el PDF renderizado, el email y `seleccion-factual.md` contra cada casilla. Marcar solo las condiciones verificadas y dejar sin marcar `aprobación explícita antes de compartir` hasta recibirla de la persona responsable.

- [ ] **Step 3: Comprobar el alcance de entrega.**

  Ejecutar `rg -n -i 'enviad[oa]|correo enviado|inscripción realizada' boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea` y confirmar que no se registra ningún envío. Ejecutar `git diff --check -- boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea`.

- [ ] **Step 4: Presentar los materiales para aprobación humana.**

  Entregar las rutas del CV DOCX, CV PDF y email Markdown. Informar de que los tres materiales están preparados para revisión y que ninguna variante se enviará hasta recibir una instrucción explícita.

- [ ] **Step 5: Commit.**

  Ejecutar `git add boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/README.md` y `git commit -m "docs: verifica materiales de candidatura espontánea"`.
