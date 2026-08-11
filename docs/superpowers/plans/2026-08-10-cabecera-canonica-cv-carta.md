# Cabecera canónica compartida CV/carta Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Hacer que la composición documental de la carta reutilice la misma cabecera canónica de `datos-generacion.json` que consume el CV, manteniendo intacto `Carta completa consolidada` y dejando el gate humano pendiente de nueva revisión.

**Architecture:** Extraer un helper pequeño (`cabecera_candidatura.py`) que valide y materialice nombre, titular y contacto desde `contenido_cv.encabezado`, incluyendo la autorización de datos privados. `componer_cv.py` y `componer_carta_presentacion.py` consumirán ese helper; la carta separará el cuerpo semántico de la cabecera documental en DOCX y PDF.

**Tech Stack:** Python 3, `python-docx`, `pypdf`, LibreOffice `soffice.com`, YAML/Markdown, `unittest`.

## Global Constraints

- Playbook y template de composición permanecen en versión `1.1.0` y estado `en_prueba`.
- `modo_texto` devuelve exactamente `Carta completa consolidada`, sin cabecera, `.txt` ni artefacto adicional.
- `modo_documento` genera únicamente DOCX, PDF y evaluación, con cabecera canónica compartida y cuerpo inmutable.
- No modificar `contenido-carta-presentacion.md`, `guion-carta-presentacion.md`, `candidatura.md`, los contratos de generación de contenido ni los artefactos CV reales.
- La privacidad se valida contra la autorización de la candidatura y no se recuperan datos por mera existencia en otra fuente.
- El hash SHA-256 del contenido de carta debe coincidir antes y después.
- No aprobar `GATE-CARTA-REVISION-HUMANA`, no diseñar el veredicto final y no abrir `GATE-CANDIDATURA-PRESENTACION`.

---

### Task 1: Helper de cabecera canónica

**Files:**
- Create: `scripts/job-up/cabecera_candidatura.py`
- Test: `tests/test_componer_carta_presentacion.py`
- Test: `tests/test_componer_cv.py`

**Interfaces:**
- `CabeceraCandidatura`: datos visibles `nombre`, `titular`, `contacto`, `origen`, `version`.
- `construir_cabecera_candidatura(payload) -> CabeceraCandidatura`: consume solo `contenido_cv.encabezado` y valida el manifiesto de privacidad del JSON.
- `validar_cabecera_con_autorizacion(cabecera, autorizacion) -> None`: rechaza nombres/contactos no autorizados o tipos divergentes.
- `renderizar_lineas_cabecera(cabecera) -> tuple[str, str, str]`: produce las líneas canónicas para CV/carta.

- [ ] **Step 1: Write failing tests** para que el helper materialice `Gustavo Vega`, el titular y email/teléfono autorizados; rechace LinkedIn no autorizado, nombre divergente y cabecera ausente.
- [ ] **Step 2: Run tests to verify failure** con `python -m unittest tests.test_componer_carta_presentacion tests.test_componer_cv -v`; deben fallar por módulo/helper inexistente.
- [ ] **Step 3: Implement minimal helper** con dataclasses inmutables, validación de `datos-generacion-cv` 1.2 y autorización explícita.
- [ ] **Step 4: Run focused tests** y confirmar que pasan sin modificar `datos-generacion.json`.

### Task 2: Reutilización por el compositor CV

**Files:**
- Modify: `scripts/job-up/componer_cv.py`
- Test: `tests/test_componer_cv.py`

**Interfaces:**
- `construir_modelo_cv` conservará su firma pública, pero obtendrá `RenderEncabezado` desde `construir_cabecera_candidatura`.

- [ ] **Step 1: Add regression test** que compare el modelo CV anterior con el modelo obtenido mediante el helper y verifique nombre, titular, contacto, fotografía y textos sin cambios.
- [ ] **Step 2: Run focused CV tests** y confirmar que la prueba nueva falla antes de integrar el helper.
- [ ] **Step 3: Modify only header construction** en `componer_cv.py`; no cambiar el árbol de secciones ni la plantilla visual.
- [ ] **Step 4: Run `python -m unittest tests.test_componer_cv -v`** y verificar que el CV temporal conserva texto, privacidad y fotografía.

### Task 3: Carta en modo texto y modo documento

**Files:**
- Modify: `scripts/job-up/componer_carta_presentacion.py`
- Test: `tests/test_componer_carta_presentacion.py`

**Interfaces:**
- `extraer_modo_texto(content_path) -> str`: devuelve únicamente `Carta completa consolidada`.
- `construir_cabecera_para_carta(candidate_dir) -> CabeceraCandidatura`: carga el JSON canónico y compara su autorización con `candidatura.md` sin usar el CV como fuente textual.
- `build_docx(letter, header, destination)`: crea una tabla de cabecera canónica y el cuerpo separado.
- `extract_docx_body/header` y `extract_pdf_body/header`: separan ambas capas para auditoría.
- `compose_case` mantendrá sus salidas DOCX/PDF/evaluación y el CLI añadirá `--modo texto|documento`.

- [ ] **Step 1: Add failing T15–T22 tests** para cabecera presente, modo texto intacto, cabecera ausente/divergente, privacidad, equivalencia cuerpo, equivalencia DOCX/PDF y hash inmutable.
- [ ] **Step 2: Run focused tests red** y confirmar que fallan por falta de cabecera compartida o comparaciones separadas.
- [ ] **Step 3: Implement mode routing and shared header**; el cuerpo seguirá procediendo exclusivamente de `Carta completa consolidada`.
- [ ] **Step 4: Replace full-document comparison** with independent body/header comparisons and route unauthorized header data to blocking composition state.
- [ ] **Step 5: Run focused suite green** and inspect generated text mode in memory without creating `.txt`.

### Task 4: Evaluación v1.1.0 y regeneración real

**Files:**
- Modify: `scripts/job-up/componer_carta_presentacion.py`
- Regenerate only: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/carta-presentacion.docx`
- Regenerate only: `.../carta-presentacion.pdf`
- Regenerate only: `.../evaluacion-composicion-carta-presentacion.md`

- [ ] **Step 1: Add evaluation fields** for mode, header origin/version/reuse, header DOCX/PDF equivalence, body integrity, privacy, visual review and the non-blocking `pdf2image` limitation.
- [ ] **Step 2: Run the real composer** after capturing the source hash; do not write any source or candidate strategy file.
- [ ] **Step 3: Verify DOCX OOXML/PDF** for header, authorized data, complete body, order, figures, comments, tracked changes and empty pages.
- [ ] **Step 4: Render and inspect the PDF** and compare the header with the approved CV's name, titular, contact, typography and hierarchy.
- [ ] **Step 5: Recalculate the source hash** and stop if it differs.

### Task 5: Full verification and final state

**Files:**
- Modify: `tests/test_componer_carta_presentacion.py`
- Modify: `tests/test_componer_cv.py`
- Do not modify: all read-only candidate/content/strategy files.

- [ ] **Step 1: Run specific carta suite** and record `X/X`.
- [ ] **Step 2: Run CV compositor regression** and record `X/X`.
- [ ] **Step 3: Run `python -m unittest discover -s tests -v`** and record total.
- [ ] **Step 4: Run `git diff --check` and inspect `git diff --stat`/`git status`** for authorized scope only.
- [ ] **Step 5: Leave human state pending** in regenerated evaluation: `decision_humana: pendiente`, `GATE-CARTA-REVISION-HUMANA` pending new human decision, presentation gate closed.
