# Veredicto final del CV — Plan de implantación

> **Para agentes:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task.

**Goal:** Implantar la revisión humana posterior a composición, el veredicto final CV-only con huella de versión y el `GATE-VEREDICTO-CV-PRESENTACION` sin automatizar la aprobación ni el envío.

**Architecture:** La revisión humana se persiste en `revision-humana-cv.md` y contiene la decisión humana y la huella SHA-256 del `cv.pdf`. Un validador técnico comprueba precondiciones, huella y precedencia; el veredicto Markdown aplica dos roles, integridad, fidelidad, seis criterios recruiter y diagnóstico competitivo. La candidatura conserva el veredicto como recomendación y el gate como decisión humana separada.

**Tech Stack:** Markdown/Obsidian, Python estándar (`hashlib`, `json`, `re`, `pathlib`), `unittest`, `python-docx` y Poppler para verificaciones físicas del PDF.

## Global Constraints

- El compositor CV-only 1.2 permanece sin cambios salvo defecto imprescindible.
- `revision-humana-cv.md` solo es válida para la huella exacta del `cv.pdf` revisado.
- Una regeneración material invalida revisión y veredicto anteriores.
- El veredicto no redacta, parchea, cambia estrategia, crea hechos, genera carta, aprueba gates ni envía candidaturas.
- `presentada: false` es precondición obligatoria.
- La media de criterios es informativa y nunca gobierna el resultado.
- La fotografía sigue incluida por defecto y la privacidad debe coincidir con `autorizacion_datos_cv`.

---

### Task 1: Especificar los contratos documentales vigentes

**Files:**
- Modify: `docs/ideas-y-debates/mejoras-job-up/PLAYBOOK_VEREDICTO_FINAL_CV.md`
- Modify: `docs/ideas-y-debates/mejoras-job-up/TEMPLATE_VEREDICTO_FINAL_CV.md`
- Modify: `docs/ideas-y-debates/mejoras-job-up/TEMPLATE_REVISION_HUMANA_CV.md`
- Test: `tests/test_veredicto_final_cv.py`

**Interfaces:**
- Produce `PLAYBOOK_VEREDICTO_FINAL_CV` versión `1.0.1`, el template de veredicto versión `1.0.1` y el template reusable de revisión humana.
- El template de revisión debe conservar exactamente `decision`, `cv_revisado`, `huella_cv`, `fecha` y `decidido_por`.

- [ ] **Step 1: Write the failing contract test**

  Crear pruebas que exijan frontmatter/versiones, `revision-humana-cv.md`, `GATE-VEREDICTO-CV-PRESENTACION`, roles A/B, seis criterios, cinco salidas globales, clasificación corregible/no corregible y regla de huella.

- [ ] **Step 2: Run the contract test and verify it fails**

  Run: `python -m unittest tests.test_veredicto_final_cv -v`

  Expected: FAIL porque el playbook actual no tiene frontmatter normativo ni declara todos los contratos.

- [ ] **Step 3: Update the playbook and templates**

  Añadir frontmatter normativo y documentar precondiciones, revisión humana, comparación SHA-256, invalidación, roles, capas, criterios C1–C6, precedencia, gate humano y no envío.

- [ ] **Step 4: Run the contract test and verify it passes**

  Run: `python -m unittest tests.test_veredicto_final_cv -v`

  Expected: PASS.

### Task 2: Implementar validador técnico de revisión, huella y resultado

**Files:**
- Create: `scripts/job-up/verificar_veredicto_final_cv.py`
- Test: `tests/test_verificador_veredicto_final_cv.py`

**Interfaces:**
- `calcular_huella(path: Path) -> str` devuelve SHA-256 hexadecimal del archivo.
- `resultado_global(integridad: str, fidelidad: str, puntuaciones: list[int], competitividad: str | None = None) -> str` aplica la precedencia aprobada.
- `validar_revision_humana(revision_path: Path, pdf_path: Path) -> dict[str, str]` bloquea ausencia, decisión no aprobada o huella discordante.
- `validar_precondiciones(candidatura_dir: Path) -> list[str]` devuelve bloqueos identificables sin modificar archivos.

- [ ] **Step 1: Write failing tests for hash identity and precedence**

  Cubrir revisión aprobada con huella correcta, revisión de versión anterior, revisión sin huella, decisión `requiere_correccion`, las cinco salidas y `presentada: true`.

- [ ] **Step 2: Run tests and verify expected failures**

  Run: `python -m unittest tests.test_verificador_veredicto_final_cv -v`

  Expected: FAIL porque el módulo y sus funciones aún no existen.

- [ ] **Step 3: Implement the minimal validator**

  Usar solo biblioteca estándar; leer los campos YAML simples del artefacto Markdown mediante expresiones regulares y no aceptar una revisión genérica.

- [ ] **Step 4: Run focused tests**

  Run: `python -m unittest tests.test_verificador_veredicto_final_cv -v`

  Expected: PASS.

### Task 3: Crear instancias de revisión humana y veredicto para CAND-2026-019/020

**Files:**
- Create: `docs/ideas-y-debates/mejoras-job-up/TEMPLATE_REVISION_HUMANA_CV.md` instance copies only as candidate-local `revision-humana-cv.md`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-019-asic-consultores-responsable-automatizacion-ia/revision-humana-cv.md`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-019-asic-consultores-responsable-automatizacion-ia/veredicto-final-cv.md`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/revision-humana-cv.md`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/veredicto-final-cv.md`
- Modify: both candidate `candidatura.md`

**Interfaces:**
- Both review instances use the current PDF SHA-256, `decision: aprobado_para_veredicto`, and `decidido_por: persona_responsable` as the explicit human decision recorded for this test run.
- Lidl veredict: integridad/fidelidad apta, C1–C6 scored with evidence, `apto_para_presentacion` only if supported; ASIC must preserve unsupported IA/Power Platform/degree gaps and may be `no_competitivo`.
- Both gate decisions remain `pendiente`; the veredict only recommends `aprobar` or `no_aprobar`.

- [ ] **Step 1: Compute current PDF hashes and page counts**

  Use Python `hashlib` and `pdfinfo.exe`; record values in both reviews and veredicts.

- [ ] **Step 2: Create human review instances**

  Record the PDF reviewed, generation date, page count, visual checks and the exact decision block. This is a persisted human decision, not an AI approval.

- [ ] **Step 3: Create two complete veredicts**

  Fill all six criteria, integrity/fidelity, privacy, competitive diagnosis, owner layer, global result, regeneration need, recommendation and pending gate decision. Do not reuse the historical ASIC veredict.

- [ ] **Step 4: Update candidate operational state**

  Replace stale “diseño de la composición” text with “revisión humana del CV → veredicto final”. Mark ASIC’s old veredict as `historico_flujo_anterior` and mark both new veredicts as current-but-gate-pending.

### Task 4: Integrar SPEC, playbook operativo, índices y PCS

**Files:**
- Modify: `docs/ideas-y-debates/mejoras-job-up/SPEC-Arquitectura-modular-generación-candidatura-v0-4-0.md`
- Modify: `docs/ideas-y-debates/mejoras-job-up/PLAYBOOK_CANDIDATURA.md`
- Modify: `.pcs/estado/estado-actual.md`
- Modify: `.pcs/sesiones/sesion-20260805-1757-job-up.md`

- [ ] **Step 1: Document the post-composition phase and gate**

  Add the new artifacts, result vocabulary, identity rule, invalidation rule and real 019/020 status without changing the upstream architecture.

- [ ] **Step 2: Integrate the operational playbook**

  Require human review before veredict, preserve `presentada: false`, and keep gate approval outside automation.

- [ ] **Step 3: Update PCS continuity**

  Record implementation, test results, candidate outcomes and remaining human gate decision.

### Task 5: Add physical acceptance and negative-flow tests

**Files:**
- Modify: `tests/test_veredicto_final_cv.py`
- Modify: `tests/test_verificador_veredicto_final_cv.py`

- [ ] **Step 1: Add five outcome fixtures**

  Assert private-data violation → `bloqueado_por_integridad`; composition omission → `requiere_correccion_de_flujo`; material unsupported gaps → `no_competitivo`; correctable visual defect → `revisar_antes_de_presentar`; complete viable CV → `apto_para_presentacion`.

- [ ] **Step 2: Add DEF-VER-001 sequence tests**

  Assert v1 review+veredict allowed, v2 PDF with v1 review blocked, missing hash blocked, correction decision blocked, and v2 PDF with v2 review allowed.

- [ ] **Step 3: Run full verification**

  Run: `python -m unittest discover -s tests -v`

  Expected: all tests PASS; then run `git diff --check` and verify it returns no errors.

---

## Self-review

- The plan covers the approved post-composition boundary, human review, hash identity, six recruiter criteria, all five outputs, both roles, candidate instances, SPEC/PCS integration and negative tests.
- It leaves the composer, carta and submission outside scope.
- It does not use the mean as a gate and does not reuse the historical ASIC veredict.
