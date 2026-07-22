# Template de evaluación del piloto de cobertura profesional — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crear el template canónico de evaluación del piloto y adecuar la evaluación real existente a ese template.

**Architecture:** El template vivirá junto a los demás templates en `docs/templates/artefactos-cobertura-profesional/`. La nota real seguirá viviendo en `boveda-entrevista-profesional/artefactos-cobertura-profesional/evaluaciones/` y conservará los resultados concretos de la primera prueba.

**Tech Stack:** Markdown, frontmatter YAML, tablas Markdown y enlaces relativos.

## Global Constraints

- Mantener la matriz como instrumento de evaluación y no duplicarla como decisión metodológica.
- Mantener la evaluación como evidencia experimental, no como adopción formal de la doble pasada.
- Registrar incidencias con fecha, parte afectada, impacto, corrección y cambio propuesto.
- Mantener ortografía española y enlaces locales funcionales.

---

### Task 1: Crear el template canónico de evaluación

**Files:**
- Create: `docs/templates/artefactos-cobertura-profesional/TEMPLATE_EVALUACION_PILOTO.md`

- [ ] **Step 1: Definir frontmatter y referencias**

Incluir `tipo`, identificadores de evaluación, persona, mapa, sesión, fecha, resultado y estado, además de enlaces a la matriz y a las evidencias.

- [ ] **Step 2: Reproducir la estructura evaluable**

Incluir las secciones A–F de la matriz, una tabla de resultado/evidencia por criterio, la sección G de incidencias y fallos, incidencias que no constituyen fallo, conclusión experimental y siguiente paso.

### Task 2: Adecuar la evaluación real y documentar el template

**Files:**
- Modify: `boveda-entrevista-profesional/artefactos-cobertura-profesional/evaluaciones/EVALUACION_PILOTO_ENT-001-M01_2026-07-20.md`
- Modify: `docs/metodologia/playbooks/PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_0.md`
- Modify: `docs/superpowers/specs/2026-07-19-preparacion-piloto-cobertura-profesional-design.md`

- [ ] **Step 1: Añadir referencia al template en la evaluación real**

Enlazar el template canónico y mantener el contenido específico de `ENT-001`.

- [ ] **Step 2: Añadir el octavo template al inventario operativo**

Incluir `TEMPLATE_EVALUACION_PILOTO.md` en la lista canónica del playbook de cobertura y del contrato.

### Task 3: Verificar estructura y enlaces

**Files:**
- Verify: los templates, la evaluación real, el playbook y el contrato.

- [ ] **Step 1: Comprobar secciones y frontmatter**

Run: `rg -n "TEMPLATE_EVALUACION_PILOTO|## A\. Cobertura|## G\. Incidencias y fallos|resultado:|id_evaluacion:" docs/templates/artefactos-cobertura-profesional boveda-entrevista-profesional/artefactos-cobertura-profesional/evaluaciones docs/metodologia/playbooks docs/superpowers/specs/2026-07-19-preparacion-piloto-cobertura-profesional-design.md`

Expected: el template y la evaluación real contienen los campos y secciones requeridos y las referencias aparecen en la documentación operativa.

- [ ] **Step 2: Verificar enlaces y formato**

Run: `git diff --check -- docs/templates docs/metodologia/playbooks docs/superpowers/specs/2026-07-19-preparacion-piloto-cobertura-profesional-design.md boveda-entrevista-profesional/artefactos-cobertura-profesional/evaluaciones`

Expected: sin errores de whitespace y con destinos locales existentes.
