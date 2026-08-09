# Guion de adaptación de CV Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implantar el contrato CV-only de `PLAYBOOK_GUION_ADAPTACION_CV`, sincronizar la SPEC y probarlo con `CAND-2026-020` y `CAND-2026-019`.

**Architecture:** La SPEC conserva la arquitectura y el estado de fase; el template fija la estructura de cada guion; el playbook transforma una candidatura válida en ese template. Cada candidatura conserva su propio guion y su evaluación independiente de `GATE-GUION-CV-CONTENIDO`.

**Tech Stack:** Markdown con frontmatter YAML, enlaces Obsidian y pruebas de contrato con `unittest` de Python.

## Global Constraints

- Fuente de diseño vigente: `docs/ideas-y-debates/mejoras-job-up/2026-08-06-guion-adaptacion-cv-design-v0-3-4.md`.
- El guion es exclusivo del CV; carta, JSON, composición, CV final y envío están fuera de alcance.
- `candidatura.md` conserva la estrategia; el guion solo decide adaptación editorial.
- `datos-core-busqueda.md` es autoridad factual; el guion no crea ni modifica hechos.
- Toda evidencia nueva o contradicción factual detiene el caso y exige `datos-core → análisis → candidatura → nueva validación → regeneración completa`.
- `DEF-ARQ-001` permanece abierto y no se resuelve ni se marca como cerrado.
- La aprobación del gate de salida es humana y su estado oficial vive en `evaluacion-gate-guion-cv-contenido.md`, no en el guion.
- Mantener ortografía española, trazabilidad y enlaces resolubles.

---

### Task 1: Sincronizar la SPEC con el contrato aprobado

**ID:** `IMPL-GUI-CV-001`  
**Objetivo:** Eliminar contradicciones entre la SPEC v0.4.0 y el diseño v0.3.4.  
**Justificación:** La sección 34 del diseño exige esta sincronización antes de implementar playbook o template.  
**Precondiciones:** Diseño v0.3.4 autorizado para implementación; `ARQ-22` e `INC-001`–`INC-003` disponibles tras revalidar la numeración.  
**Archivos a leer:** Diseño v0.3.4 y SPEC v0.4.0.  
**Resultado esperado:** SPEC coherente con un adaptador exclusivo de CV, sin cerrar `DEF-ARQ-001`.  
**Criterios de aceptación:** Pipeline CV-only, gate de salida registrado, incertidumbres registradas y fases fuera de alcance pendientes.  
**Verificación:** Prueba `SpecContractTests` y `git diff --check`.  
**Dependencias:** Ninguna.  
**Gate asociado:** `GATE-CANDIDATURA-GUION` ya aprobado; no crea un nuevo gate humano.  
**Aprobación humana:** La instrucción actual autoriza esta implantación.

**Files:**
- Modify: `docs/ideas-y-debates/mejoras-job-up/SPEC-Arquitectura-modular-generación-candidatura-v0-4-0.md`
- Test: `tests/test_playbook_guion_adaptacion_cv.py`

**Consumes:** Diseño v0.3.4, en especial secciones 3, 4, 18, 21 y 34.

**Produces:** Estado `en_prueba` para el playbook; `ARQ-22`; `INC-001` a `INC-003`; pipeline exclusivo CV; gate `GATE-GUION-CV-CONTENIDO`.

- [ ] **Step 1: Escribir la prueba de sincronización normativa**

```python
def test_spec_declares_cv_only_guion_and_preserves_open_defect():
    spec = read("docs/ideas-y-debates/mejoras-job-up/SPEC-Arquitectura-modular-generación-candidatura-v0-4-0.md")
    assert "ARQ-22 — Separación de responsabilidades CV/carta" in spec
    assert "GATE-GUION-CV-CONTENIDO" in spec
    assert "DEF-ARQ-001" in spec and "Estado:** abierto" in spec
    assert "futura generación de contenido del CV" in spec
```

- [ ] **Step 2: Ejecutar la prueba y comprobar que falla**

Run: `python -m unittest discover -s tests -p "test_playbook_guion_adaptacion_cv.py"`

Expected: FAIL porque la SPEC aún carece de `ARQ-22` y del gate de salida.

- [ ] **Step 3: Actualizar la SPEC sin diseñar fases fuera de alcance**

Incorporar `ARQ-22`; registrar `INC-001`, `INC-002` e `INC-003`; cambiar el pipeline previsto a CV-only; sustituir la relación estratégica CV/carta por responsabilidades del guion CV; conservar `DEF-ARQ-001` abierto; registrar el gate de salida; y actualizar el estado real a `PLAYBOOK_GUION_ADAPTACION_CV: en_prueba`.

- [ ] **Step 4: Ejecutar la prueba de sincronización**

Run: `python -m unittest discover -s tests -p "test_playbook_guion_adaptacion_cv.py"`

Expected: PASS.

### Task 2: Materializar el template y el playbook

**ID:** `IMPL-GUI-CV-002`  
**Objetivo:** Crear los contratos físicos reutilizables de guion y procedimiento.  
**Justificación:** El diseño exige un template estructurado y un playbook de 16 pasos antes de probar casos.  
**Precondiciones:** `IMPL-GUI-CV-001` completada.  
**Archivos a leer:** Diseño v0.3.4, SPEC sincronizada y `TEMPLATE_CANDIDATURA_v2.md`.  
**Resultado esperado:** Template y playbook CV-only que no almacenan el estado del gate de salida.  
**Criterios de aceptación:** Metadatos, mapa multidimensional, incidencias, retroceso completo y gate separado presentes.  
**Verificación:** Pruebas `TemplateAndPlaybookTests`.  
**Dependencias:** `IMPL-GUI-CV-001`.  
**Gate asociado:** `GATE-GUION-CV-CONTENIDO` definido, aún no evaluado.  
**Aprobación humana:** No adicional.

**Files:**
- Create: `docs/ideas-y-debates/mejoras-job-up/TEMPLATE_GUION_ADAPTACION_CV_v2.md`
- Create: `docs/ideas-y-debates/mejoras-job-up/PLAYBOOK_GUION_ADAPTACION_CV.md`
- Modify: `tests/test_playbook_guion_adaptacion_cv.py`

**Consumes:** SPEC sincronizada y diseño v0.3.4.

**Produces:** Contrato repetible de `guion-adaptacion-cv.md` y procedimiento de 16 pasos con validaciones, retrocesos y gate separado.

- [ ] **Step 1: Escribir las pruebas de contrato del template y playbook**

```python
def test_template_has_required_frontmatter_and_editorial_map():
    template = read(TEMPLATE)
    for key in ("version_diseno:", "fuentes_factuales:", "gate_salida: GATE-GUION-CV-CONTENIDO"):
        assert key in template
    assert "estado_gate_salida:" not in template
    for value in ("incluir", "omitir", "obligatoria", "opcional", "alto", "medio", "bajo", "minimo"):
        assert value in template

def test_playbook_declares_cv_only_execution_and_full_regeneration():
    playbook = read(PLAYBOOK)
    assert "16 pasos" in playbook
    assert "regeneración completa" in playbook
    assert "no redacta la carta" in playbook
    assert "evaluacion-gate-guion-cv-contenido.md" in playbook
```

- [ ] **Step 2: Ejecutar las pruebas y comprobar que fallan**

Run: `python -m unittest discover -s tests -p "test_playbook_guion_adaptacion_cv.py"`

Expected: FAIL porque no existen los dos archivos.

- [ ] **Step 3: Crear `TEMPLATE_GUION_ADAPTACION_CV_v2.md`**

Incluir frontmatter de la sección 21 del diseño; identificación; instrucción editorial; mapa con `M-NNN`, tipo, evidencia, presencia, obligatoriedad, peso, criterio, función, ubicación, orden, detalle y motivo; experiencias/logros; arquitectura; léxico; seniority; tono; advertencias/límites; brief derivado; controles de cobertura, duplicación y primer escaneo. No incluir estado de gate de salida.

- [ ] **Step 4: Crear `PLAYBOOK_GUION_ADAPTACION_CV.md`**

Materializar las precondiciones, autoridad de fuentes, orden normativo de 16 pasos, taxonomía del mapa, protección cronológica, gestión de incidencias, regeneración completa, gate de salida y límites CV-only. Exigir que el estado del gate se escriba únicamente en el artefacto de evaluación.

- [ ] **Step 5: Ejecutar las pruebas de contrato**

Run: `python -m unittest discover -s tests -p "test_playbook_guion_adaptacion_cv.py"`

Expected: PASS.

### Task 3: Probar el caso principal CAND-2026-020

**ID:** `IMPL-GUI-CV-003`  
**Objetivo:** Generar y evaluar el primer guion conforme al contrato, sin producir un CV.  
**Justificación:** `CAND-2026-020` es la prueba principal definida en el diseño.  
**Precondiciones:** `IMPL-GUI-CV-002` completada; `GATE-CANDIDATURA-GUION` aprobado; candidatura no presentada y sin bloqueo activo.  
**Archivos a leer:** Candidatura, análisis, datos core, playbook y template.  
**Resultado esperado:** Guion y evaluación separados, con decisión humana de salida pendiente.  
**Criterios de aceptación:** Cobertura Lidl, límites de FP/caja/compras respetados y trazabilidad factual íntegra.  
**Verificación:** Prueba `CandidateGuideTests.test_lidl_guion_preserves_limits_and_covers_strategy`.  
**Dependencias:** `IMPL-GUI-CV-002`.  
**Gate asociado:** `GATE-GUION-CV-CONTENIDO`.  
**Aprobación humana:** Requerida posteriormente para aprobar o bloquear el gate de salida; no se infiere.

**Files:**
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/guion-adaptacion-cv.md`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/evaluacion-gate-guion-cv-contenido.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/candidatura.md`
- Modify: `tests/test_playbook_guion_adaptacion_cv.py`

**Consumes:** `CAND-2026-020/candidatura.md`, su análisis y `datos-core-busqueda.md`.

**Produces:** Guion CV factualmente trazable y evaluación `apto` con recomendación IA, pero decisión humana pendiente.

- [ ] **Step 1: Escribir la prueba del caso Lidl**

```python
def test_lidl_guion_preserves_limits_and_covers_strategy():
    guide = read(LIDL_GUIDE)
    evaluation = read(LIDL_EVALUATION)
    for evidence in ("HER-03", "HER-07", "HER-04", "HER-08", "HER-10"):
        assert evidence in guide
    assert "FP de Técnico Administrativo" in guide
    assert "tesorería" in guide and "no afirmar" in guide
    assert "compras centralizadas" in guide
    assert "decision_humana: pendiente" in evaluation
    assert "estado_gate: pendiente" in evaluation
```

- [ ] **Step 2: Ejecutar la prueba y comprobar que falla**

Run: `python -m unittest discover -s tests -p "test_playbook_guion_adaptacion_cv.py"`

Expected: FAIL porque no existe el guion ni la evaluación.

- [ ] **Step 3: Crear guion y evaluación de CAND-2026-020**

Aplicar el mapa editorial a operación de supermercados, previsión, pedidos, stock, rotación, merma, caja, equipos y mejora de procesos. Mantener los cargos históricos; reducir el peso de dirección generalista; impedir equivalencia de FP, tesorería, compras corporativas y negociación posterior no acreditada. Evaluar todos los criterios de aceptación, con `resultado_evaluacion: apto`, `recomendacion_ia: aprobar`, `decision_humana: pendiente` y `estado_gate: pendiente`.

- [ ] **Step 4: Actualizar el índice de candidatura**

Cambiar la siguiente fase a guion, registrar el enlace y estado del guion/evaluación, y eliminar referencias ya obsoletas al gate anterior pendiente. No modificar `presentada: false` ni marcar la candidatura como aprobada o enviada.

- [ ] **Step 5: Ejecutar la prueba del caso Lidl**

Run: `python -m unittest discover -s tests -p "test_playbook_guion_adaptacion_cv.py"`

Expected: PASS.

### Task 4: Preparar y someter a gate de entrada CAND-2026-019

**ID:** `IMPL-GUI-CV-004`  
**Objetivo:** Migrar la ficha histórica mínima de `CAND-2026-019` al contrato actual y emitir evidencia para `GATE-CANDIDATURA-GUION`.  
**Justificación:** El playbook no puede iniciar este caso sin gate de entrada individual aprobado.  
**Precondiciones:** `IMPL-GUI-CV-002` completada; la candidatura no está presentada y sus fuentes son resolubles.  
**Archivos a leer:** Ficha, análisis, datos core, evaluación de CAND-2026-020 y template de candidatura.  
**Resultado esperado:** Ficha compatible con la arquitectura actual y evaluación de gate de entrada con recomendación IA, decisión humana pendiente.  
**Criterios de aceptación:** Estrategia y límites heredados, artefactos antiguos declarados históricos, sin declaración automática de aprobación.  
**Verificación:** Prueba `CandidateEntryGateTests`.  
**Dependencias:** `IMPL-GUI-CV-002`.  
**Gate asociado:** `GATE-CANDIDATURA-GUION`.  
**Aprobación humana:** Obligatoria antes de `IMPL-GUI-CV-005`; el plan no puede suplirla.

**Files:**
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-019-asic-consultores-responsable-automatizacion-ia/candidatura.md`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-019-asic-consultores-responsable-automatizacion-ia/evaluacion-gate-candidatura-guion.md`
- Modify: `tests/test_playbook_guion_adaptacion_cv.py`

- [ ] **Step 1: Escribir la prueba de gate de entrada de ASIC**

```python
def test_asic_has_entry_gate_evidence_without_automatic_approval():
    evaluation = read(ASIC_ENTRY_EVALUATION)
    assert "gate: GATE-CANDIDATURA-GUION" in evaluation
    assert "recomendacion_ia: aprobar" in evaluation
    assert "decision_humana: pendiente" in evaluation
    assert "estado_gate: pendiente" in evaluation
```

- [ ] **Step 2: Ejecutar la prueba y comprobar que falla**

Run: `python -m unittest discover -s tests -p "test_playbook_guion_adaptacion_cv.py"`

Expected: FAIL porque falta la evaluación de entrada.

- [ ] **Step 3: Sincronizar ficha y crear evaluación de entrada**

Migrar la ficha al modelo actual sin reescribir CV/carta heredados; declarar esos documentos como históricos del flujo anterior; crear evaluación con recomendación IA basada en el análisis y decisión humana pendiente.

- [ ] **Step 4: Ejecutar la prueba de gate de entrada**

Run: `python -m unittest discover -s tests -p "test_playbook_guion_adaptacion_cv.py"`

Expected: PASS, pero el caso queda detenido a la espera de aprobación humana del gate de entrada.

### Task 5: Contrastar la generalidad con CAND-2026-019

**ID:** `IMPL-GUI-CV-005`  
**Objetivo:** Regenerar el guion de ASIC y evaluar su gate de salida bajo el contrato nuevo.  
**Justificación:** Es el contraste obligatorio para proponer la validación de fase.  
**Precondiciones:** `IMPL-GUI-CV-004` completada y decisión humana `GATE-CANDIDATURA-GUION: aprobado` registrada para CAND-2026-019.  
**Archivos a leer:** Candidatura ASIC sincronizada, análisis, datos core, playbook y template.  
**Resultado esperado:** Guion tecnológico trazable y evaluación de salida pendiente de decisión humana.  
**Criterios de aceptación:** No transforma transferibilidad en experiencia IA o de stack; conserva límites, seniority y cronología.  
**Verificación:** Prueba `CandidateGuideTests.test_asic_guion_does_not_turn_transferability_into_ia_or_stack_experience`.  
**Dependencias:** `IMPL-GUI-CV-004` y decisión humana de entrada.  
**Gate asociado:** `GATE-GUION-CV-CONTENIDO`.  
**Aprobación humana:** Requerida para el gate de entrada y, posteriormente, para el gate de salida.

**Files:**
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-019-asic-consultores-responsable-automatizacion-ia/guion-adaptacion-cv.md`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-019-asic-consultores-responsable-automatizacion-ia/evaluacion-gate-guion-cv-contenido.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-019-asic-consultores-responsable-automatizacion-ia/candidatura.md`
- Modify: `tests/test_playbook_guion_adaptacion_cv.py`

**Consumes:** Candidatura y análisis existentes de ASIC, con documentación previa que debe preservarse como histórica.

**Produces:** Guion compatible con el nuevo contrato sin reescribir ni volver a generar CV/carta ya existentes; prueba de generalidad y evaluación pendiente de decisión humana.

- [ ] **Step 1: Escribir la prueba de contraste tecnológico**

```python
def test_asic_guion_does_not_turn_transferability_into_ia_or_stack_experience():
    guide = read(ASIC_GUIDE)
    for evidence in ("HER-01", "HER-03", "HER-07", "HER-08", "GSC-01"):
        assert evidence in guide
    for limit in ("Power Automate", "Dynamics 365 Business Central", "Salesforce", "experiencia profesional en IA"):
        assert limit in guide
    assert "no afirmar" in guide
    assert "decision_humana: pendiente" in read(ASIC_EVALUATION)
```

- [ ] **Step 2: Ejecutar la prueba y comprobar que falla**

Run: `python -m unittest tests.test_playbook_guion_adaptacion_cv.CandidateGuideTests.test_asic_guion_does_not_turn_transferability_into_ia_or_stack_experience`

Expected: FAIL porque falta la evaluación y el guion heredado no sigue el contrato actual.

- [ ] **Step 3: Regenerar el guion de CAND-2026-019 y crear la evaluación**

Reemplazar solo el guion por uno conforme al nuevo template; mantener los artefactos CV/carta heredados como históricos sin modificarlos. Priorizar automatización, procesos, datos, algoritmos, integración e impacto; limitar IA y stack Microsoft a formulaciones acreditadas; tratar seniority directivo sin falsearlo. Registrar evaluación `apto`, recomendación IA de aprobar y decisión humana pendiente.

- [ ] **Step 4: Actualizar el índice de candidatura sin reescribir el historial documental**

Enlazar el nuevo guion y evaluación; dejar explícito que CV/carta existentes pertenecen al flujo anterior y no fueron regenerados por esta prueba.

- [ ] **Step 5: Ejecutar la prueba de contraste**

Run: `python -m unittest tests.test_playbook_guion_adaptacion_cv.CandidateGuideTests.test_asic_guion_does_not_turn_transferability_into_ia_or_stack_experience`

Expected: PASS.

### Task 6: Verificación integrada y actualización de continuidad

**ID:** `IMPL-GUI-CV-006`  
**Objetivo:** Consolidar evidencia, estado de fase y continuidad PCS sin declarar aprobaciones humanas inexistentes.  
**Justificación:** La fase solo puede ser candidata a validada tras dos pruebas completas; el estado vivo debe reflejar los gates individuales.  
**Precondiciones:** `IMPL-GUI-CV-003` y `IMPL-GUI-CV-005` completadas.  
**Archivos a leer:** SPEC, playbook, template, ambos guiones/evaluaciones y documentos PCS.  
**Resultado esperado:** Fase en prueba o candidata a validada según evidencia, sin CV/carta nuevos ni envío.  
**Criterios de aceptación:** Dos evaluaciones, trazabilidad, pruebas y estado PCS coherente.  
**Verificación:** Pruebas integradas, regresión existente, enlaces y `git diff --check`.  
**Dependencias:** `IMPL-GUI-CV-003` y `IMPL-GUI-CV-005`.  
**Gate asociado:** Ambos gates individuales de salida.  
**Aprobación humana:** Necesaria para validar formalmente la fase, no para registrar el resultado técnico.

**Files:**
- Modify: `.pcs/estado/estado-actual.md`
- Modify: `.pcs/sesiones/sesion-20260805-1757-job-up.md`
- Modify: `tests/test_playbook_guion_adaptacion_cv.py`

**Consumes:** SPEC sincronizada, playbook/template y ambos casos evaluados.

**Produces:** Evidencia de implementación completa, fase `candidata a validada` sin declarar validación humana, y continuidad PCS exacta.

- [ ] **Step 1: Escribir la prueba integrada**

```python
def test_full_contract_has_two_cases_and_no_out_of_scope_generation():
    for candidate in (LIDL_DIR, ASIC_DIR):
        assert (candidate / "guion-adaptacion-cv.md").is_file()
        assert (candidate / "evaluacion-gate-guion-cv-contenido.md").is_file()
    assert "candidata a validada" in read(SPEC)
    assert "decision_humana: pendiente" in read(LIDL_EVALUATION)
    assert "decision_humana: pendiente" in read(ASIC_EVALUATION)
```

- [ ] **Step 2: Ejecutar la prueba y comprobar que falla o queda incompleta**

Run: `python -m unittest tests.test_playbook_guion_adaptacion_cv`

Expected: FAIL hasta que estén completos los dos casos y la continuidad.

- [ ] **Step 3: Actualizar estado PCS y sesión**

Registrar que la implantación está completa y probada con dos casos; que el playbook es `candidata a validada`; que ambos gates individuales están pendientes de decisión humana; y que no se autoriza la generación ni el envío.

- [ ] **Step 4: Ejecutar pruebas integradas y regresión existente**

Run: `python -m unittest tests.test_playbook_guion_adaptacion_cv tests.test_generar_candidatura`

Expected: PASS.

- [ ] **Step 5: Revisar enlaces, diffs y ortografía**

Run: `git diff --check` y un comprobador de enlaces Markdown/Wikilink de los nuevos documentos.

Expected: ningún enlace roto, ningún error de formato ni modificación de CV/carta/DOCX/PDF/LaTeX.
