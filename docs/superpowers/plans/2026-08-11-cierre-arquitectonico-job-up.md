# Cierre arquitectónico y reorganización documental de Job-up — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Consolidar el flujo documental de Job-up hasta el CV y la carta aprobados, promocionar los contratos maduros a sus ubicaciones canónicas y retirar la presentación automatizada del flujo principal sin añadir funcionalidad nueva.

**Architecture:** Los playbooks operativos vivirán en `docs/metodologia/playbooks/` y los templates de Job-up en `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/`. La generación termina en `candidatura documental completa`; la presentación y la UI de configuración se documentan como líneas futuras separadas. Las instancias de candidatura conservarán artefactos documentales y no usarán el gate de presentación como precondición de cierre.

**Tech Stack:** Markdown/YAML, JSON, Python 3, `unittest`, `python-docx`/OOXML para comprobaciones documentales, PowerShell para movimientos explícitos y `rg` para auditoría de referencias.

## Global Constraints

- Mantener la rama `codex/job-up-validar-presentacion`.
- No crear commit, merge ni PR.
- No iniciar sesión en portales, rellenar formularios, aceptar consentimientos ni presentar `CAND-2026-020`.
- No implementar UI, wizard, servidor local, plugin de navegador ni nuevos campos de configuración.
- No eliminar documentos experimentales sin clasificarlos y conservarlos como histórico o futuro.
- No depender de `docs/ideas-y-debates` para la ejecución normal de ningún playbook, template o script operativo.
- El fin documental es `CV final aprobado + carta final aprobada cuando sea requerida`; `presentada` debe seguir siendo `false`.

---

### Task 1: Inventario y clasificación antes de mover archivos

**Files:**
- Create: `docs/superpowers/plans/2026-08-11-cierre-arquitectonico-job-up.md` (este plan)
- Inspect: `docs/ideas-y-debates/mejoras-job-up/`, `docs/metodologia/playbooks/`, `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/`, `scripts/job-up/`, `tests/`, `.pcs/`

**Interfaces:**
- Consume: nombres de archivos y referencias encontradas con `rg`.
- Produce: matriz de clasificación usada por las tareas 2–4; no se mueve ningún archivo sin destino explícito.

- [ ] **Step 1: Enumerate candidates and current references**

Run:

```powershell
rg --files docs/ideas-y-debates/mejoras-job-up docs/metodologia/playbooks boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas scripts/job-up tests | Sort-Object
rg -n "docs/ideas-y-debates/mejoras-job-up|PLAYBOOK_|TEMPLATE_|GATE-CANDIDATURA-PRESENTACION|paquete-presentacion|presentada" docs boveda-entrevista-profesional scripts tests .pcs
```

Expected: a complete list of active, historical and future artefacts; no move is performed by this step.

- [ ] **Step 2: Record the classification in the working plan**

Classify as `vigente_operativo`:

```text
PLAYBOOK_ANALISIS_OFERTA.md
PLAYBOOK_CANDIDATURA.md
PLAYBOOK_GUION_ADAPTACION_CV.md
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA.md
PLAYBOOK_COMPONER_CV.md (to be documented from the existing compositor contract if absent)
PLAYBOOK_VEREDICTO_FINAL_CV.md
PLAYBOOK_GUION_CARTA_PRESENTACION.md
PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION.md
PLAYBOOK_COMPONER_CARTA_PRESENTACION.md
PLAYBOOK_VEREDICTO_FINAL_CARTA.md
```

Classify as `futura_linea_presentacion`:

```text
PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA.md
TEMPLATE_EVALUACION_PRESENTACION_CANDIDATURA.md
TEMPLATE_VALIDAR_PRESENTACION_CANDIDATURA.md
TEMPLATE_PAQUETE_PRESENTACION.md
evaluacion-presentacion-candidatura.md
paquete-presentacion.md
```

Classify obsolete or historical design versions under `historico/` without deleting them:

```text
2026-08-06-guion-adaptacion-cv-design-*.md
SPEC-Arquitectura-modular-para-generación-de-candidaturas-en-Job-up.md
TEMPLATE_DATOS_GENERACION_CV_v1.json
```

Expected: every file has one classification and one intended destination.

---

### Task 2: Promote mature playbooks to the canonical playbook directory

**Files:**
- Move from `docs/ideas-y-debates/mejoras-job-up/` to `docs/metodologia/playbooks/`: the nine mature playbooks listed in Task 1.
- Create: `docs/metodologia/playbooks/PLAYBOOK_COMPONER_CV.md` only if no existing canonical file is found; derive its contract from `scripts/job-up/componer_cv.py`, `scripts/job-up/generar_candidatura.py` and `tests/test_componer_cv.py`.
- Modify: all moved playbooks to replace relative references to the old ideas directory with canonical template links.

**Interfaces:**
- Consumes: existing playbook contracts and the implementation/test behaviour already present.
- Produces: one canonical operational copy per playbook; no normal execution path points to `docs/ideas-y-debates`.

- [ ] **Step 1: Create a recoverable target directory check**

Run:

```powershell
New-Item -ItemType Directory -Force 'docs/metodologia/playbooks' | Out-Null
```

Expected: the existing canonical playbook directory remains intact.

- [ ] **Step 2: Move only mature playbooks with explicit paths**

Use `Move-Item -LiteralPath` for each mature file, preserving names and refusing to overwrite an existing target. Do not move `PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA.md`.

Expected: the source file is absent from the active ideas folder and the target exists in `docs/metodologia/playbooks/`.

- [ ] **Step 3: Document the missing CV composition contract from existing behaviour**

If `PLAYBOOK_COMPONER_CV.md` is absent, create a concise playbook with:

```yaml
id: PLAYBOOK_COMPONER_CV
estado: vigente
entrada_principal: datos-generacion.json
salidas:
  - cv.docx
  - cv.pdf
  - cv.tex
gate_entrada: GATE-CONTENIDO-CV-COMPOSICION
gate_salida: GATE-VEREDICTO-CV
```

The body must state that the compositor is deterministic, consumes only the JSON contract, includes the approved photograph by default, produces the three CV artefacts and does not read candidature strategy or presentation state to choose content.

Expected: the canonical flow has a named composition playbook without changing runtime behaviour.

- [ ] **Step 4: Update playbook references and validate paths**

Run:

```powershell
rg -n "docs/ideas-y-debates/mejoras-job-up|TEMPLATE_[A-Z_]+" docs/metodologia/playbooks
```

Expected: all template references resolve to `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/` or to a documented external contract.

---

### Task 3: Promote mature templates and isolate presentation artefacts

**Files:**
- Move mature templates from `docs/ideas-y-debates/mejoras-job-up/` to `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/`.
- Move presentation templates to `docs/ideas-y-debates/mejoras-job-up/futuro/presentacion/`.
- Move the candidate-local `evaluacion-presentacion-candidatura.md` and `paquete-presentacion.md` to the mirrored `historico/` path.
- Modify: promoted templates to use canonical frontmatter and links.

**Interfaces:**
- Consumes: current template versions and the existing target templates in `proceso/plantillas/`.
- Produces: one active template per contract and an explicit future/presentation archive.

- [ ] **Step 1: Resolve canonical template names before moving**

Use these canonical names, preserving the mature contract versions:

```text
TEMPLATE_ANALISIS_OFERTA.md
TEMPLATE_CANDIDATURA.md
TEMPLATE_GUION_ADAPTACION_CV.md
TEMPLATE_DATOS_GENERACION_CV.json
TEMPLATE_CONTENIDO_CARTA_PRESENTACION.md
TEMPLATE_COMPOSICION_CARTA_PRESENTACION.md
TEMPLATE_GUION_CARTA_PRESENTACION.md
TEMPLATE_REVISION_HUMANA_CV.md
TEMPLATE_VEREDICTO_FINAL_CV.md
TEMPLATE_VEREDICTO_FINAL_CARTA.md
```

Expected: `v2`, `v1_FINAL` and historical suffixes are removed from the active path only; the source versions remain recoverable under `historico/` when they are not the promoted copy.

- [ ] **Step 2: Move mature templates without overwriting existing canonical files**

Compare the source and target contents. Promote the source only when it is the newer accepted contract; otherwise update the target using `apply_patch` and archive the source. Keep `TEMPLATE_CV_FORMATO.*`, `TEMPLATE_CARTA_PRESENTACION_FORMATO.*` and `GUIA_FORMATO_CV_Y_CARTA.md` in their existing canonical directory.

Expected: the canonical template directory contains the complete operational set.

- [ ] **Step 3: Isolate future presentation templates**

Create `docs/ideas-y-debates/mejoras-job-up/futuro/presentacion/` and move:

```text
PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA.md
TEMPLATE_EVALUACION_PRESENTACION_CANDIDATURA.md
TEMPLATE_VALIDAR_PRESENTACION_CANDIDATURA.md
TEMPLATE_PAQUETE_PRESENTACION.md
```

Move the candidate-local presentation evaluation and package to:

```text
historico/boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/
```

Expected: presentation material remains auditable but is no longer an active dependency.

- [ ] **Step 4: Audit duplicate active templates**

Run:

```powershell
rg --files docs/metodologia/playbooks boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas docs/ideas-y-debates/mejoras-job-up/futuro | Sort-Object
```

Expected: each contract has one active template and future presentation templates are clearly separated.

---

### Task 4: Close the main contract at documentary completion

**Files:**
- Modify: `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md`
- Modify: `docs/ideas-y-debates/mejoras-job-up/SPEC-Arquitectura-modular-generación-candidatura-v0-4-0.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/candidatura.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/README.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/README.md`

**Interfaces:**
- Consumes: canonical playbooks/templates from Tasks 2–3.
- Produces: a single documented terminal state `documentalmente_completa` independent of presentation.

- [ ] **Step 1: Replace presentation as a completion precondition**

Change the active flow to:

```text
CV final aprobado
+ carta final aprobada cuando sea requerida
→ candidatura documental completa
→ FIN DEL ALCANCE ACTUAL
```

Retain `presentada: false` as a fact field. Remove active instructions that require opening or evaluating `GATE-CANDIDATURA-PRESENTACION` to close the candidate.

Expected: no current playbook or candidate state says presentation is required for documentary completion.

- [ ] **Step 2: Add explicit future lines without implementing them**

Document separately in the SPEC and README:

```text
Línea futura A — entorno inicial de preguntas/configuración.
Línea futura B — presentación automatizada asistida por IA.
```

Expected: future scope is visible but has no active gate, script, UI or field.

- [ ] **Step 3: Set CAND-2026-020 to documentary completion**

Update frontmatter and status text to:

```yaml
estado: documentalmente_completa
paquete_presentacion: fuera_de_alcance_actual
gate_candidatura_presentacion: no_aplica_en_esta_fase
presentada: false
```

State that CV and letter have approved final verdicts and that no external presentation occurred.

Expected: CAND-2026-020 meets the prompt's final state without a presentation gate.

- [ ] **Step 4: Update candidature README and Job-up README flow**

Replace the current step that opens `GATE-CANDIDATURA-PRESENTACION` with the documentary completion step. Keep presentation as a future/manual responsibility outside this architecture.

Expected: a new reader can discover where the current flow ends and what is excluded.

---

### Task 5: Remove live runtime dependencies on presentation and old paths

**Files:**
- Modify: `scripts/job-up/generar_candidatura.py`
- Modify: `scripts/job-up/componer_cv.py`
- Modify: `scripts/job-up/componer_carta_presentacion.py`
- Modify: `scripts/job-up/verificar_paquete_presentacion.py` only if it remains as a future validator; otherwise move its documentation dependency to future scope.
- Modify: `scripts/job-up/verificar_veredicto_final_cv.py`
- Modify: `scripts/job-up/verificar_veredicto_final_carta.py`
- Modify: all tests that import or assert old template paths.

**Interfaces:**
- Consumes: canonical template directory and candidate-local artefacts.
- Produces: normal execution independent of ideas documents and presentation state.

- [ ] **Step 1: Locate every runtime path assumption**

Run:

```powershell
rg -n "ideas-y-debates|TEMPLATE_ROOT|proceso/plantillas|GATE-CANDIDATURA-PRESENTACION|paquete-presentacion" scripts tests
```

Expected: every match is assigned either to active documentary flow or to a future validator.

- [ ] **Step 2: Point active generators to the canonical template directory**

Set the active root in each generator to:

```python
TEMPLATE_ROOT = Path("boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas")
```

Resolve it relative to the repository root and preserve secure path validation. Do not make generators read presentation files.

Expected: CV and letter generation work with canonical templates only.

- [ ] **Step 3: Make presentation validator non-blocking for the active closure**

If retained, `verificar_paquete_presentacion.py` must be clearly marked future-only and must not be imported by the active candidate completion path. No script may set `presentada: true`.

Expected: presentation code is isolated and cannot block document completion.

- [ ] **Step 4: Add route regression tests**

Add tests that fail if an active script imports `docs/ideas-y-debates` or requires `GATE-CANDIDATURA-PRESENTACION` for CV/carta generation.

Expected: route independence is mechanically enforced.

---

### Task 6: Add contract tests for documentary completion

**Files:**
- Create: `tests/test_candidatura_documental_completa.py`
- Modify: `tests/test_veredicto_final_cv.py`
- Modify: `tests/test_veredicto_final_carta.py`
- Modify: `tests/test_verificador_paquete_presentacion.py` if it remains future-only.

**Interfaces:**
- Consumes: candidate frontmatter, CV/carta verdict fixtures and optional-letter configuration.
- Produces: deterministic assertions for T01–T10 from the prompt.

- [ ] **Step 1: Write failing tests for T01–T05**

Cover:

```python
def test_cv_and_required_letter_approved_complete(): ...
def test_required_letter_not_approved_incomplete(): ...
def test_letter_not_required_can_complete(): ...
def test_document_complete_does_not_set_presented_true(): ...
def test_missing_presentation_gate_does_not_block_document_complete(): ...
```

Expected: the current presentation-dependent model fails at least the completion tests.

- [ ] **Step 2: Write failing tests for T06–T10**

Cover canonical-path independence, future presentation isolation, valid references and the complete `CAND-2026-020` case.

Expected: each test names the path or state it protects and fails before the contract edits.

- [ ] **Step 3: Implement the smallest contract helpers and assertions**

Use existing parsing helpers where available. Do not add a new runtime service. The completion predicate must be pure and return `True` only when all required approved artefacts exist.

Expected: tests pass without introducing new external actions.

- [ ] **Step 4: Run the focused suite**

Run:

```powershell
python -m unittest tests.test_candidatura_documental_completa tests.test_componer_cv tests.test_componer_carta_presentacion tests.test_veredicto_final_cv tests.test_veredicto_final_carta
```

Expected: PASS.

---

### Task 7: Update the canonical flow index and inventories

**Files:**
- Modify: `boveda-entrevista-profesional/busqueda-empleo/README.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/README.md`
- Modify: `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md`
- Create or modify: `docs/metodologia/playbooks/README_JOB_UP.md`

**Interfaces:**
- Consumes: final canonical paths and flow from Tasks 2–6.
- Produces: discoverable index of playbooks, templates, scripts, artefacts, historical and future documents.

- [ ] **Step 1: Create the canonical flow reference**

Document this exact outline in `README_JOB_UP.md`:

```text
OFERTA → ANÁLISIS → CANDIDATURA
→ CV (guion → contenido → composición → revisión/veredicto)
→ CARTA opcional según contrato (guion → contenido → composición → revisión/veredicto)
→ CANDIDATURA DOCUMENTAL COMPLETA
→ FIN DEL ALCANCE ACTUAL
```

State that external presentation and UI/configuration are future lines.

- [ ] **Step 2: Add inventories**

List canonical playbooks, templates, scripts and candidate artefacts; link future presentation material and historical paths explicitly.

Expected: a new reader can locate each category without searching ideas documents.

- [ ] **Step 3: Validate links in the index**

Run the repository link/reference checker from Task 9 and fix each missing target before proceeding.

Expected: no broken canonical links.

---

### Task 8: Synchronize SPEC, candidate state and PCS

**Files:**
- Modify: `docs/ideas-y-debates/mejoras-job-up/SPEC-Arquitectura-modular-generación-candidatura-v0-4-0.md`
- Modify: `.pcs/estado/estado-actual.md`
- Modify: `.pcs/sesiones/sesion-20260805-1757-job-up.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/seguimiento/seguimiento-candidaturas.md`

**Interfaces:**
- Consumes: final flow and validation results.
- Produces: one live PCS record distinguishing current documentary completion from future presentation work.

- [ ] **Step 1: Rewrite SPEC pipeline/status sections**

Set the active terminal state to documentary completion and move the presentation validator to a clearly labelled future line. Keep the UI line separate and unimplemented. Update gates only where the existing contract requires it; do not invent a new presentation gate.

- [ ] **Step 2: Synchronize CAND-2026-020 in PCS and tracking**

Record:

```yaml
estado: documentalmente_completa
presentada: false
cv: aprobado
carta: aprobada
presentacion: fuera_de_alcance_actual
```

Keep `CAND-2026-019` blocked and do not rewrite already-presented historical candidates.

- [ ] **Step 3: Register the two future lines**

Record the configuration-question environment and supervised/automated presentation as separate future work, with no active action opened and no new session.

- [ ] **Step 4: Record branch and no-integration constraint**

Add that the work remains on `codex/job-up-validar-presentacion` without commit, merge or PR until human pending items and real-flow validation are resolved.

Expected: PCS tells a future agent exactly where the current phase ends and what remains external.

---

### Task 9: Run structural, route and end-to-end validation

**Files:**
- Inspect all active Markdown, JSON, Python and candidate artefacts.
- Modify only files with a verified broken reference or failing contract assertion.

**Interfaces:**
- Consumes: all outputs of Tasks 2–8.
- Produces: auditable validation report in the final response and PCS status.

- [ ] **Step 1: Check syntax and whitespace**

Run:

```powershell
python -m compileall scripts/job-up tests
git diff --check
```

Expected: no syntax errors and no whitespace errors.

- [ ] **Step 2: Check broken references and old dependencies**

Run:

```powershell
rg -n "docs/ideas-y-debates/mejoras-job-up/(PLAYBOOK|TEMPLATE)|GATE-CANDIDATURA-PRESENTACION|paquete-presentacion" docs/metodologia/playbooks boveda-entrevista-profesional/busqueda-empleo scripts/job-up tests
```

Expected: only explicitly future/experimental references remain; none are required by the active flow.

- [ ] **Step 3: Run focused and complete tests**

Run:

```powershell
python -u -m unittest discover -s tests -p 'test*.py'
```

Expected: all tests pass.

- [ ] **Step 4: Verify CAND-2026-020 end to end**

Check that the candidate folder contains the approved CV and letter artefacts, the final verdicts are approved, the candidate is documentary complete and `presentada` remains `false`. Do not open a browser or submit anything.

- [ ] **Step 5: Produce the final inventory and stop**

Report moved files, archived/future files, updated references, tests, remaining dependency scans and the next future line. Do not commit, merge, open a PR or implement the next line.

---

## Completion checklist

- [ ] Alcance cerrado en generación documental.
- [ ] Presentación automatizada fuera del flujo principal.
- [ ] UI/configuración fuera del flujo principal.
- [ ] Playbooks y templates maduros en rutas definitivas.
- [ ] Documentos experimentales clasificados y conservados.
- [ ] Referencias y scripts actualizados.
- [ ] SPEC, README, índices y PCS sincronizados.
- [ ] CAND-2026-020 documentalmente completa con `presentada: false`.
- [ ] Pruebas específicas, suite completa, sintaxis y `git diff --check` pasan.
- [ ] Rama conservada sin commit, merge ni PR.
