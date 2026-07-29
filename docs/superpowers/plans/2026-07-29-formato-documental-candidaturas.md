# Formato documental de candidaturas Job-up — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Crear plantillas visuales coherentes para CV y carta, documentar su correspondencia con el guion de adaptación y eliminar improvisaciones previsibles de las dos skills de Job-up.

**Architecture:** La plantilla DOCX será la referencia visual reutilizable; una guía Markdown será el contrato semántico que conecta cada campo del guion con el CV y la carta. Las dos skills consumirán ese contrato y producirán siempre el mismo conjunto de artefactos, con revisión factual, estructural y visual antes de `pendiente_de_aprobacion`.

**Tech Stack:** DOCX basado en `python-docx`, validación OOXML con `python-docx`, PDF generado y renderizado con las dependencias documentales disponibles, Markdown, YAML frontmatter y Git.

## Global Constraints

- Basar la identidad visual en `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-010-acciona-administrativo/cv.docx`.
- Usar Calibri; 14/12/11/10,5 pt; `#1F2937` y `#5B6573`.
- Justificar el contenido del CV y de la carta; mantener alineación funcional solo en encabezados, contacto, saludos, títulos y firma.
- Mantener CV y carta en una página cuando la legibilidad lo permita; esta plantilla fija una página como objetivo operativo.
- Incorporar fotografía siempre, salvo exclusión expresa de la persona responsable en la invocación de la skill.
- Mantener texto seleccionable, encabezados estándar y viñetas; no usar tablas ni columnas para el contenido operativo.
- No ampliar hechos, métricas, herramientas, titulaciones ni datos privados más allá de las fuentes y autorización de cada candidatura.
- No enviar candidaturas, emails ni documentos; la salida es siempre revisión y aprobación humana.

---

### Task 1: Crear la guía semántica común

**Files:**
- Create: `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/GUIA_FORMATO_CV_Y_CARTA.md`

**Interfaces:**
- Consumes: `TEMPLATE_GUION_ADAPTACION_CV.md`, `TEMPLATE_CANDIDATURA.md`, el playbook vigente y el CV base de CAND-2026-010.
- Produces: reglas de correspondencia para las plantillas y las skills.

- [ ] Documentar la tabla `guion → CV → carta` con titular, perfil, competencias, experiencia, valor diferencial, sobrecualificación, límites y datos privados.
- [ ] Documentar el contrato visual: Calibri, tamaños, colores, justificación, una página y fotografía obligatoria salvo exclusión expresa.
- [ ] Documentar los nombres exactos de los artefactos: `cv.docx`, `cv.pdf`, `cv.tex`, `carta-presentacion.docx`, `carta-presentacion.pdf`.
- [ ] Añadir una lista de controles contra improvisación: afirmaciones, logros, requisitos, experiencia histórica, herramientas, tono, contacto, foto, páginas y llamada a la acción.
- [ ] Revisar ortografía española y enlaces internos antes de continuar.

### Task 2: Crear la plantilla visual de CV

**Files:**
- Create: `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_CV_FORMATO.docx`
- Create: `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_CV_FORMATO.md`

**Interfaces:**
- Consumes: CAND-2026-010 `cv.docx` como referencia visual y `GUIA_FORMATO_CV_Y_CARTA.md` como contrato semántico.
- Produces: plantilla DOCX sin datos personales reutilizables y guía específica de uso.

- [ ] Conservar del documento base la estructura del encabezado de dos celdas, la jerarquía de estilos, los colores, la justificación y la reserva de fotografía.
- [ ] Sustituir todos los datos personales y hechos de CAND-2026-010 por marcadores explícitos: `[NOMBRE]`, `[TITULAR]`, `[EMAIL]`, `[TELÉFONO]`, `[FOTOGRAFÍA]`, `[PERFIL PROFESIONAL]`, `[PROPUESTA DE VALOR]`, `[EXPERIENCIA]`, `[COMPETENCIAS]`, `[FORMACIÓN]` e `[INFORMACIÓN ADICIONAL]`.
- [ ] Mantener una fotografía de marcador o un espacio claramente identificable, sin reutilizar la fotografía personal de CAND-2026-010.
- [ ] Crear la guía Markdown con el orden de sustitución y la relación de cada marcador con el guion.
- [ ] Validar que la plantilla no contiene nombres, emails, teléfonos, LinkedIn, empresas, métricas ni logros de la candidatura base.

### Task 3: Crear la plantilla visual de carta

**Files:**
- Create: `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_CARTA_PRESENTACION_FORMATO.docx`
- Create: `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_CARTA_PRESENTACION_FORMATO.md`

**Interfaces:**
- Consumes: estructura visual de CAND-2026-010, `GUIA_FORMATO_CV_Y_CARTA.md` y `email-presentacion.md` para el registro formal.
- Produces: plantilla DOCX de una página y reglas de contenido para cartas.

- [ ] Crear encabezado con nombre, contacto y fotografía, manteniendo el contrato visual del CV.
- [ ] Crear marcadores para `[DESTINATARIO]`, `[FECHA]`, `[ASUNTO]`, `[SALUDO]`, `[APERTURA]`, `[EVIDENCIA 1]`, `[EVIDENCIA 2]`, `[ENCAJE]`, `[CIERRE]` y `[FIRMA]`.
- [ ] Mantener el cuerpo justificado, el tratamiento formal cuando el destinatario sea empresa y una extensión de una página.
- [ ] Prohibir que la carta introduzca logros, herramientas, requisitos cumplidos o hechos de empresa no presentes en el guion y el análisis.
- [ ] Validar que no contiene datos personales ni hechos de CAND-2026-010.

### Task 4: Alinear el guion de adaptación

**Files:**
- Modify: `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_GUION_ADAPTACION_CV.md`

**Interfaces:**
- Consumes: `GUIA_FORMATO_CV_Y_CARTA.md`.
- Produces: guion compatible con CV y carta.

- [ ] Cambiar la regla visual para permitir fotografía obligatoria salvo exclusión expresa.
- [ ] Añadir que el guion gobierna simultáneamente CV, CV LaTeX y carta.
- [ ] Añadir el límite de justificación, una página, Calibri, tamaños y colores como contrato de salida.
- [ ] Añadir controles para que la carta no amplíe la selección factual del CV.

**También modificar:** `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md`, para que no conserve reglas antiguas incompatibles con la fotografía obligatoria y la justificación del contenido.

### Task 5: Endurecer `job-up-candidatura-oferta`

**Files:**
- Modify: `.codex/skills/job-up-candidatura-oferta/SKILL.md`

**Interfaces:**
- Consumes: `GUIA_FORMATO_CV_Y_CARTA.md`, `TEMPLATE_CV_FORMATO.docx`, `TEMPLATE_CARTA_PRESENTACION_FORMATO.docx` y el guion actualizado.
- Produces: paquete de candidatura con formato, contenido y verificación coherentes.

- [ ] Añadir al flujo la lectura del contrato documental antes de generar CV o carta.
- [ ] Exigir fotografía por defecto y permitir excluirla solo por instrucción expresa de la persona responsable.
- [ ] Exigir justificación del contenido del CV y de la carta.
- [ ] Exigir que titular, perfil, competencias, experiencia, logros, valor diferencial y sobrecualificación procedan del guion.
- [ ] Exigir los cinco nombres de archivo y el índice completo de candidatura.
- [ ] Añadir controles de improvisación y detener solo los documentos afectados cuando falte autorización privada.
- [ ] Reforzar la validación estructural DOCX, PDF visual, coherencia CV/carta/LaTeX y ausencia de datos no autorizados.

### Task 6: Endurecer `job-up-genera-cv-empresa`

**Files:**
- Modify: `.codex/skills/job-up-genera-cv-empresa/SKILL.md`

**Interfaces:**
- Consumes: `GUIA_FORMATO_CV_Y_CARTA.md`, `TEMPLATE_CV_FORMATO.docx`, `TEMPLATE_CARTA_PRESENTACION_FORMATO.docx`, `email-presentacion.md` y `seleccion-factual.md`.
- Produces: CV y email espontáneo coherentes y revisables.

- [ ] Exigir que el CV espontáneo use la misma plantilla visual y fotografía por defecto.
- [ ] Exigir que el email use únicamente hechos comprobados, puntos de encaje marcados como hipótesis y módulos seleccionados explícitamente.
- [ ] Prohibir que el email o el CV improvisen cultura, necesidades, destinatario, proyectos, herramientas o logros.
- [ ] Añadir control de tono, tratamiento, llamada a la acción y correspondencia con el CV.
- [ ] Mantener el estado de revisión y aprobación humana sin envío.

**También revisar:** `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/email-presentacion.md`, únicamente para hacer explícita la selección de módulos, el origen factual y la llamada a la acción, sin cambiar su finalidad.

### Task 7: Verificar y consolidar

**Files:**
- Verify: las plantillas, el guion, ambas skills y los documentos generados.

- [ ] Abrir la plantilla DOCX con `python-docx` y verificar marcadores, fuente, tamaños, colores, justificación, imagen de marcador y ausencia de datos personales.
- [ ] Renderizar la plantilla CV y carta a PDF con el motor disponible y revisar visualmente cada página.
- [ ] Ejecutar búsquedas de marcadores sin correspondencia y de datos heredados de CAND-2026-010.
- [ ] Comprobar que las dos skills referencian los nombres reales de las plantillas y de la guía.
- [ ] Ejecutar `git diff --check` y comprobar que el árbol contiene únicamente cambios de esta iniciativa.
- [ ] Actualizar la sesión PCS activa con los artefactos creados y verificaciones realizadas.
- [ ] Crear un commit único con el formato documental y las reglas de las skills.
