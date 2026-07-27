# Candidatura espontánea a Randstad Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crear y verificar la candidatura `CAND-2026-006` para presentar a Gustavo a Randstad en procesos de intermediación de Dirección y Operaciones.

**Architecture:** La candidatura vivirá en una carpeta propia dentro de `boveda-entrevista-profesional/busqueda-empleo/candidaturas/`. La ficha, el análisis, el guion y el veredicto serán Markdown trazable; el CV y la carta serán DOCX y PDF generados con la identidad documental vigente y revisados visualmente.

**Tech Stack:** Markdown/Obsidian, Python-docx mediante las dependencias del workspace, LibreOffice para conversión/renderizado, `render_docx.py` para verificación visual y los datos factuales de `datos-core-busqueda.md`.

## Global Constraints

- Perfil principal: Dirección/Management.
- Perfiles secundarios: Operaciones; Administración; mejora de procesos; Informática aplicada y automatización.
- La candidatura será espontánea y no responderá a una oferta concreta.
- El CV representará los grandes hitos acreditados de Herfrailes S. L. sin convertirlos en un inventario ilegible.
- No se presentarán decisiones colegiadas, funciones de CENCOSU, experiencia independiente 2024–actualidad ni estudios no finalizados como hechos distintos de los documentados.
- Para `CAND-2026-006` están autorizados nombre completo, email, teléfono, fotografía y enlace profesional.
- No se enviará ni compartirá ningún documento sin aprobación humana explícita.
- La ficha deberá inventariar todos los documentos creados en la carpeta.

---

### Task 1: Crear la estructura y la trazabilidad de CAND-2026-006

**Files:**
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-006-randstad-presentacion-espontanea/candidatura.md`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-006-randstad-presentacion-espontanea/analisis-oferta.md`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-006-randstad-presentacion-espontanea/guion-adaptacion-cv.md`

- [ ] Crear la ficha con estado `pendiente_de_aprobacion`, empresa Randstad, modalidad `presentación espontánea` y perfiles principal/secundarios definidos.
- [ ] Documentar que Randstad es el destinatario de una presentación para intermediación y que no existe una oferta concreta asociada.
- [ ] Crear el análisis con encaje, propuesta de valor, palabras clave respaldadas, logros seleccionados, límites de atribución y ausencia de requisitos de una oferta concreta.
- [ ] Crear el guion con el titular, resumen, narrativa, selección de logros de Herfrailes, dimensión informática secundaria y control antiarrastre.
- [ ] Inventariar provisionalmente los documentos previstos y actualizar la ficha después de cada creación.

### Task 2: Generar el CV de dos páginas con datos autorizados

**Files:**
- Create: `tools/generate_randstad_spontaneous.py`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-006-randstad-presentacion-espontanea/cv.docx`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-006-randstad-presentacion-espontanea/cv.pdf`
- Read: `boveda-entrevista-profesional/busqueda-empleo/datos-privados-candidatura.md`
- Read: `boveda-entrevista-profesional/busqueda-empleo/foto-perfil.png`
- Read: `boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda.md`

- [ ] Generar el encabezado con nombre completo, email, teléfono, enlace profesional y fotografía autorizados.
- [ ] Redactar el perfil directivo con Operaciones como eje y Administración, mejora de procesos e Informática aplicada como secundarios.
- [ ] Incluir los hitos HER-01, HER-02, HER-03, HER-04, HER-05, HER-07, HER-08 y HER-09 en formulaciones compactas, manteniendo cifras y límites de atribución.
- [ ] Incluir experiencia informática histórica de Granintra, GSC e INERZA sin presentarla como dominio tecnológico actual.
- [ ] Incluir formación en curso, estudios no finalizados correctamente etiquetados y herramientas actuales permitidas.
- [ ] Convertir el DOCX a PDF y confirmar que el CV tiene exactamente dos páginas.

### Task 3: Crear la carta/email de presentación espontánea

**Files:**
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-006-randstad-presentacion-espontanea/carta-presentacion.docx`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-006-randstad-presentacion-espontanea/carta-presentacion.pdf`

- [ ] Explicar que el contacto se dirige a Randstad para ser considerado en procesos de intermediación, no como respuesta a una vacante concreta.
- [ ] Presentar el eje de Dirección/Operaciones y conectar los hitos de Herfrailes con mejora de procesos, sistemas, logística y gestión transversal.
- [ ] Mencionar de forma secundaria la dimensión informática aplicada: automatización, VB.NET/API de Trello, sistemas empresariales y análisis de datos.
- [ ] Incorporar nombre completo, email, teléfono, foto y enlace profesional solo conforme a la autorización de `CAND-2026-006`.
- [ ] Mantener una extensión breve, profesional y accionable para remisión a una persona consultora de selección.
- [ ] Convertir el DOCX a PDF y revisar visualmente ambas salidas.

### Task 4: Emitir el veredicto y cerrar la consistencia documental

**Files:**
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-006-randstad-presentacion-espontanea/veredicto-final-cv.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-006-randstad-presentacion-espontanea/candidatura.md`

- [ ] Comprobar integridad factual y privacidad de CV y carta antes de puntuar calidad.
- [ ] Puntuar primer escaneo, encaje competitivo, cobertura ATS respaldada, fuerza de la experiencia y adecuación narrativa.
- [ ] Marcar la candidatura como `pendiente_de_aprobacion` hasta la revisión humana explícita.
- [ ] Completar el inventario de documentos de la ficha y registrar el veredicto.

### Task 5: Actualizar Job-up y verificar el resultado final

**Files:**
- Modify: `boveda-entrevista-profesional/busqueda-empleo/seguimiento-candidaturas.md`
- Modify: `.pcs/estado/estado-actual.md`
- Modify: `.pcs/sesiones/sesion-20260724-2004-candidaturas-job-up.md`

- [ ] Añadir `CAND-2026-006` al seguimiento global con estado `pendiente_de_aprobacion`.
- [ ] Actualizar el estado vivo con la nueva candidatura espontánea y su alcance.
- [ ] Registrar el trabajo en la sesión PCS abierta de candidaturas nuevas y antiguas.
- [ ] Ejecutar comprobaciones de enlaces/archivos, extracción de texto del DOCX/PDF, número de páginas y ausencia de afirmaciones prohibidas.
- [ ] Renderizar e inspeccionar todas las páginas del CV y la carta antes de afirmar que los documentos están listos.
