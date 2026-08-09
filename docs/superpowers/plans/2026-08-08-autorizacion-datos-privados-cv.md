# Autorización de datos privados por candidatura — Plan de implantación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans (recommended). Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Hacer explícita, auditable y determinista la selección de datos privados que pueden aparecer en cada CV y regenerar Lidl y ASIC con nombre, apellido 1, email y teléfono autorizados.

**Architecture:** `datos-privados-candidatura.md` conserva los valores factuales privados. `datos-core-busqueda.md` los referencia separando nombre, apellido 1 y apellido 2. Cada `candidatura.md` registra la autorización por campo. El contenido 1.2 materializa únicamente los campos autorizados y el compositor continúa consumiendo solo el JSON.

**Tech Stack:** Markdown/YAML, JSON 1.2, Python 3, `unittest`, `python-docx`, LibreOffice `soffice.com` para DOCX→PDF.

## Global Constraints

- La autoridad para autorizar datos privados es la persona responsable de la candidatura.
- Los valores factuales no se inventan ni se copian desde un CV generado; proceden de `datos-privados-candidatura.md`.
- `nombre`, `apellido_1` y `apellido_2` son datos independientes.
- Para esta regeneración se autorizan `nombre`, `apellido_1`, `email` y `telefono`.
- `apellido_2`, `linkedin` y `ubicacion` no se incorporan al CV de esta regeneración.
- La fotografía continúa incluida por defecto según la decisión vigente.
- Las candidaturas presentadas no se modifican; Lidl y ASIC tienen `presentada: false`.
- El compositor no consulta fuentes privadas: recibe los contactos ya materializados en `datos-generacion.json`.
- No se genera carta.

---

### Task 1: Fuente factual separada y autorización por candidatura

**Files:**
- Modify: `boveda-entrevista-profesional/busqueda-empleo/fuentes/datos-core-busqueda.md`
- Modify: `docs/ideas-y-debates/mejoras-job-up/TEMPLATE_CANDIDATURA_v2.md`
- Modify: `docs/ideas-y-debates/mejoras-job-up/PLAYBOOK_CANDIDATURA.md`
- Modify: both candidate `candidatura.md`

**Interfaces:**
- Consumes: `datos-privados-candidatura.md` and the human authorization in this request.
- Produces: `autorizacion_datos_cv` with `incluir|omitir|pendiente` for each private field.

- [ ] Add separate factual rows for `Nombre`, `Apellido 1`, `Apellido 2`, email, phone and LinkedIn to the core, without duplicating secret values.
- [ ] Add the authorization block to the candidate template with explicit default `pendiente`, date and authority.
- [ ] Add the mandatory start-of-candidacy question and the rule that any `pendiente` blocks CV generation.
- [ ] Record the approved matrix in CAND-2026-020 and CAND-2026-019: name/include, surname 1/include, surname 2/omit, email/include, phone/include, LinkedIn/omit, location/omit, photo/include.

### Task 2: Contract and validation of private data

**Files:**
- Modify: `docs/ideas-y-debates/mejoras-job-up/TEMPLATE_DATOS_GENERACION_CV_v1_FINAL.json`
- Modify: `docs/ideas-y-debates/mejoras-job-up/PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA.md`
- Modify: `scripts/job-up/validar_datos_generacion_cv.py`
- Modify: `tests/test_validacion_datos_generacion_cv.py`

**Interfaces:**
- Consumes: candidate authorization and factual source references.
- Produces: auditable `control.datos_privados` and rejection of unauthorized materialization.

- [ ] Add the non-visible audit block with authorized, omitted and source-reference fields.
- [ ] Require separate identity references for name, surname 1 and surname 2 when present.
- [ ] Add failing tests for an omitted field materialized in contact and for a pending field.
- [ ] Implement the minimum validator checks and run the focused tests.

### Task 3: Propagate authorized values into both JSON productives

**Files:**
- Modify: both candidate `datos-generacion.json`
- Modify: both candidate content evaluations if their status text says the old contract is active

**Interfaces:**
- Consumes: authorized values and factual refs.
- Produces: contact units for name components, email and phone only, plus the existing default photo policy.

- [ ] Materialize name, surname 1, email and phone with separate factual traceability.
- [ ] Exclude surname 2, LinkedIn and location from visible content.
- [ ] Preserve all existing professional content and gate metadata.
- [ ] Validate each JSON against its CV guide and the updated validator.

### Task 4: Regenerate the two CVs

**Files:**
- Replace outputs in both candidate folders: `cv.docx`, `cv.pdf`, `cv.tex`
- Update: both `manifest-generacion-cv.json`

**Interfaces:**
- Consumes: updated JSON 1.2.
- Produces: three CV artifacts per candidate with authorized private data and photo.

- [ ] Run the generator for Lidl and verify only the authorized fields appear.
- [ ] Run the generator for ASIC and verify only the authorized fields appear.
- [ ] Confirm no carta artifact is created or changed.

### Task 5: Tests, visual verification and PCS synchronization

**Files:**
- Modify: `tests/test_componer_cv.py`
- Modify: `tests/test_generar_cv_1_2.py`
- Modify: `docs/ideas-y-debates/mejoras-job-up/SPEC-Arquitectura-modular-generación-candidatura-v0-4-0.md`
- Modify: `.pcs/estado/estado-actual.md`
- Modify: `.pcs/sesiones/sesion-20260805-1757-job-up.md`

**Interfaces:**
- Consumes: generated artifacts and test evidence.
- Produces: final audit trail and open/closed status for the privacy defect.

- [ ] Add a regression test asserting the model renders authorized email and phone and omits unauthorized LinkedIn/location.
- [ ] Run the complete test suite.
- [ ] Extract PDF text and render both PDFs to images; verify one page, photo, authorized contacts and no unauthorized contacts.
- [ ] Register the privacy authorization rule in the SPEC, resolve the contact-data defect and keep the letter branch separate.
- [ ] Update PCS state and session with results and the next human review step.
