# Alinear skill Job-up candidatura por oferta — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Alinear `job-up-candidatura-oferta` con la arquitectura documental modular vigente para que sea un orquestador real de CV y carta, sin presentación externa.

**Architecture:** La skill conservará únicamente la coordinación de entradas, sesión, privacidad, orden de fases, comprobación de gates y cierre documental. Cada decisión editorial, generación, composición y veredicto seguirá viviendo en su playbook canónico. El CV consumirá `TEMPLATE_DATOS_GENERACION_CV.json` 1.2 y la carta seguirá una rama independiente.

**Tech Stack:** Markdown, JSON contractual, Python `unittest`, `compileall`, comprobaciones Git.

## Global Constraints

- No ejecutar `job-up-candidatura-oferta` durante esta tarea.
- No crear ni modificar candidaturas reales.
- No generar CV, carta, JSON de candidatura ni abrir gates reales.
- No incluir presentación externa, formularios, credenciales, login ni `presentada: true`.
- Usar exclusivamente `docs/metodologia/playbooks/` y `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/` como rutas operativas.
- Mantener la fotografía del CV por defecto y la carta sin fotografía por defecto.
- Mantener `job-up-inicia-sesion` limitado al ciclo PCS de sesión.

### Task 1: Crear pruebas de contrato para la skill

**Files:**
- Create: `tests/test_job_up_candidatura_oferta_skill.py`
- Read: `.codex/skills/job-up-candidatura-oferta/SKILL.md`

**Interfaces:**
- Consumes: texto de la skill y rutas canónicas existentes.
- Produces: siete regresiones `T-SKILL-01` a `T-SKILL-07` que fallen contra la skill histórica.

- [ ] **Step 1: Write the failing tests**

  Crear una clase `JobUpCandidaturaOfertaSkillTests` con una constante `SKILL_TEXT` y estas comprobaciones:

  ```python
  def test_t_skill_01_no_usa_contrato_conjunto_historico(self):
      self.assertNotIn("TEMPLATE_DATOS_GENERACION_CANDIDATURA.json", self.skill)

  def test_t_skill_02_declara_contrato_cv_12(self):
      self.assertIn("TEMPLATE_DATOS_GENERACION_CV.json", self.skill)
      self.assertIn("1.2", self.skill)

  def test_t_skill_03_separa_fotografia_de_carta(self):
      self.assertIn("carta", self.skill.lower())
      self.assertIn("no se incluye por defecto", self.skill.lower())
      self.assertNotIn("fotografía autorizada por defecto en CV y carta", self.skill.lower())

  def test_t_skill_04_no_orquesta_generacion_conjunta(self):
      self.assertIn("rama CV", self.skill)
      self.assertIn("rama carta", self.skill)
      self.assertNotIn("generación conjunta", self.skill.lower())

  def test_t_skill_05_declara_cierre_documental(self):
      self.assertIn("documentalmente_completa", self.skill)
      self.assertIn("presentada: false", self.skill)

  def test_t_skill_06_excluye_presentacion_externa(self):
      self.assertIn("presentación externa queda fuera", self.skill.lower())
      self.assertNotIn("GATE-CANDIDATURA-PRESENTACION", self.skill)

  def test_t_skill_07_referencias_canonicas_existen(self):
      for playbook in EXPECTED_PLAYBOOKS:
          self.assertIn(playbook, self.skill)
          self.assertTrue((PLAYBOOK_ROOT / playbook).is_file())
      for template in EXPECTED_TEMPLATES:
          self.assertTrue((TEMPLATE_ROOT / template).exists())
  ```

- [ ] **Step 2: Run tests to verify they fail**

  Run: `python -m unittest tests.test_job_up_candidatura_oferta_skill`

  Expected: fallos por la referencia al contrato conjunto, la fotografía compartida, la generación conjunta y la ausencia del cierre `documentalmente_completa`.

### Task 2: Reescribir la skill como orquestador modular

**Files:**
- Modify: `.codex/skills/job-up-candidatura-oferta/SKILL.md`

**Interfaces:**
- Consumes: oferta URL/Markdown/texto, sesión Job-up única y autorización privada específica.
- Produces: expediente documental con ramas CV/carta, gates verificables y estado `documentalmente_completa` cuando corresponda.

- [ ] **Step 1: Sustituir el contrato histórico por la secuencia modular**

  La skill debe describir únicamente:

  ```text
  oferta
  → análisis de oferta
  → candidatura
  → guion CV
  → contenido CV
  → composición CV
  → veredicto CV
  → guion carta cuando proceda
  → contenido carta
  → composición carta
  → veredicto carta
  → documentalmente_completa
  ```

  Debe enlazar los playbooks canónicos por nombre exacto, indicar que cada gate humano bloquea el avance cuando corresponde y remitir a los playbooks para las reglas detalladas.

- [ ] **Step 2: Declarar el contrato CV-only 1.2 y la rama de carta**

  Incluir `TEMPLATE_DATOS_GENERACION_CV.json` con versión `1.2`, `PLAYBOOK_COMPONER_CV` y las salidas `cv.docx`, `cv.pdf` y `cv.tex`. La carta debe usar `PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION`, `PLAYBOOK_COMPONER_CARTA_PRESENTACION` y `PLAYBOOK_VEREDICTO_FINAL_CARTA` de forma independiente.

- [ ] **Step 3: Declarar fotografía y cierre documental**

  Documentar la política CV/carta separada, la independencia de `presentada` y la regla `CV aprobado + carta aprobada cuando sea requerida = documentalmente_completa`.

- [ ] **Step 4: Eliminar lógica duplicada y presentación externa**

  Retirar detalles de composición, conversión, slots, generación conjunta y envío. Mantener solo precondiciones, delegación, comprobación de salida y detenciones seguras.

- [ ] **Step 5: Ejecutar las pruebas de skill**

  Run: `python -m unittest tests.test_job_up_candidatura_oferta_skill`

  Expected: `7/7` correctos.

### Task 3: Actualizar PCS y verificar documentación directa

**Files:**
- Modify: `.pcs/estado/estado-actual.md`
- Modify: `.pcs/sesiones/sesion-20260805-1757-job-up.md`
- Read: `.codex/skills/job-up-inicia-sesion/SKILL.md`
- Read: `boveda-entrevista-profesional/busqueda-empleo/README.md`

**Interfaces:**
- Consumes: resultado de auditoría y pruebas de las tareas 1–2.
- Produces: registro PCS de la causa, corrección, pruebas y E2E pendiente.

- [ ] **Step 1: Confirmar que `job-up-inicia-sesion` no requiere cambios**

  Verificar que solo gestiona ciclo PCS y no contiene contrato de generación, presentación o fotografía. Si no hay inconsistencia, no modificarlo.

- [ ] **Step 2: Registrar la corrección en PCS**

  Añadir a la sesión y al estado operativo que el bloqueo E2E provenía de la skill desalineada, que se corrigió el contrato y que la prueba real sigue pendiente. No abrir sesión nueva.

### Task 4: Verificación final sin ejecutar E2E

**Files:**
- Verify: `.codex/skills/job-up-candidatura-oferta/SKILL.md`
- Verify: `tests/test_job_up_candidatura_oferta_skill.py`

- [ ] **Step 1: Ejecutar tests Job-up**

  Run: `python -m unittest tests.test_job_up_candidatura_oferta_skill tests.test_componer_cv tests.test_componer_carta_presentacion tests.test_veredicto_final_cv tests.test_veredicto_final_carta tests.test_candidatura_documental_completa tests.test_fotografia_cv_carta`

- [ ] **Step 2: Ejecutar suite completa**

  Run: `python -m unittest discover -s tests -p 'test*.py'`

- [ ] **Step 3: Ejecutar comprobaciones técnicas**

  Run: `python -m compileall -q scripts/job-up tests`

  Run: `git diff --check`

- [ ] **Step 4: Buscar referencias históricas en la skill**

  Run: `rg -n -i "TEMPLATE_DATOS_GENERACION_CANDIDATURA|schema 1\.0|fotograf[ií]a.*CV y carta|generaci[oó]n conjunta|GATE-CANDIDATURA-PRESENTACION" .codex/skills/job-up-candidatura-oferta/SKILL.md`

  Expected: sin coincidencias operativas.

- [ ] **Step 5: Confirmar que no se ejecutó la skill ni se creó una candidatura**

  Revisar `git status --short` y las carpetas de `boveda-entrevista-profesional/busqueda-empleo/candidaturas/`. No debe aparecer ningún nuevo expediente creado por esta tarea.
