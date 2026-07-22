# Incorporación de elementos adicionales al piloto de cobertura profesional — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Incorporar en los templates los elementos necesarios detectados durante el primer piloto real y dejar trazabilidad de la prueba y sus correcciones en la sesión PCS abierta de cobertura profesional.

**Architecture:** Los templates canónicos de `docs/templates/artefactos-cobertura-profesional/` serán la fuente reutilizable para entrevistado, mapa, sesión, checkpoint, inmersión, competencia y transcripción. Los artefactos reales seguirán viviendo en `boveda-entrevista-profesional/artefactos-cobertura-profesional/`, y la sesión PCS abierta conservará la historia de la prueba y de la corrección sin convertirse en estado vivo.

**Tech Stack:** Markdown, frontmatter YAML, enlaces Markdown relativos y verificaciones PowerShell.

## Global Constraints

- Mantener la convención del piloto: `ENT-001`, `ENT-001-M01`, zonas `Z001`, intentos `a`, `b`, etc.
- No borrar ni reescribir la historia previa de la sesión PCS; añadir una actualización fechada.
- No crear un checkpoint cuando la inmersión ha terminado; registrar explícitamente que no aplica.
- Mantener la transcripción verbatim como artefacto auditable.
- Mantener la separación entre orientación experimental y metodología adoptada.

---

### Task 1: Ampliar los templates canónicos

**Files:**
- Modify: `docs/templates/artefactos-cobertura-profesional/TEMPLATE_ENTREVISTADO.md`
- Modify: `docs/templates/artefactos-cobertura-profesional/TEMPLATE_MAPA.md`
- Modify: `docs/templates/artefactos-cobertura-profesional/TEMPLATE_SESION.md`
- Modify: `docs/templates/artefactos-cobertura-profesional/TEMPLATE_INMERSION.md`
- Modify: `docs/templates/artefactos-cobertura-profesional/TEMPLATE_COMPETENCIA.md`
- Create: `docs/templates/artefactos-cobertura-profesional/TEMPLATE_TRANSCRIPCION.md`

**Interfaces:**
- Consumes: las necesidades observadas en el piloto real y los requisitos de los playbooks.
- Produces: templates que permiten crear futuros artefactos sin perder transcripción, validación, alcance, conservación ni la convención de identificadores.

- [ ] **Step 1: Añadir contexto aprobado al template de entrevistado**

Añadir campos opcionales `alcance_aprobado` y `conservacion_aprobada`, más secciones de alcance y conservación que puedan completarse sin recoger datos adicionales no autorizados.

- [ ] **Step 2: Hacer explícitos zona, intento y referencias reales en mapa, sesión e inmersión**

Actualizar los placeholders para usar `id_zona`, nombres de fichero con intento (`...-Z001-a.md`) y un enlace de transcripción verbatim. Indicar que el checkpoint es `no aplica` cuando la inmersión termina.

- [ ] **Step 3: Añadir validaciones a competencia**

Añadir una sección `## Validaciones` con validación factual, de competencia y de valor profesional, y conservar `id_inmersion` como vínculo de trazabilidad.

- [ ] **Step 4: Crear template canónico de transcripción**

Crear `TEMPLATE_TRANSCRIPCION.md` con frontmatter para entrevistado, mapa, sesión, fecha y estado, y un formato de turnos literales sin sustituir el artefacto de sesión, inmersión o competencia.

- [ ] **Step 5: Verificar que cada elemento adicional está representado**

Run: `rg -n "alcance_aprobado|conservacion_aprobada|id_zona|intento|Transcripción verbatim|## Validaciones|TEMPLATE_TRANSCRIPCION" docs/templates/artefactos-cobertura-profesional`

Expected: cada elemento aparece en el template responsable y existe el nuevo template de transcripción.

### Task 2: Alinear la documentación operativa con los nuevos templates

**Files:**
- Modify: `docs/metodologia/playbooks/PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_0.md`
- Modify: `docs/metodologia/playbooks/PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA.md`
- Modify: `docs/superpowers/specs/2026-07-19-preparacion-piloto-cobertura-profesional-design.md`

**Interfaces:**
- Consumes: los templates ampliados de Task 1.
- Produces: instrucciones que obligan a usar la transcripción y las nuevas piezas de trazabilidad.

- [ ] **Step 1: Enlazar el template de transcripción en los dos playbooks**

Indicar que cada sesión real debe conservar una transcripción verbatim y enlazar `TEMPLATE_TRANSCRIPCION.md` junto con los demás templates.

- [ ] **Step 2: Actualizar el contrato del piloto**

Incluir la transcripción como artefacto mínimo de auditoría y señalar que el template de competencia contiene las tres validaciones.

- [ ] **Step 3: Verificar referencias**

Run: `rg -n "TEMPLATE_TRANSCRIPCION|transcripción verbatim|tres validaciones|alcance_aprobado|conservacion_aprobada" docs/metodologia/playbooks docs/superpowers/specs/2026-07-19-preparacion-piloto-cobertura-profesional-design.md`

Expected: la documentación operativa menciona los nuevos elementos y su ruta canónica.

### Task 3: Registrar la prueba real y las correcciones en la sesión PCS abierta

**Files:**
- Modify: `.pcs/sesiones/sesion-20260705-concepto-cobertura-profesional-carrera-ai.md`

**Interfaces:**
- Consumes: los artefactos `ENT-001` del piloto y la corrección de templates.
- Produces: una actualización histórica de la sesión abierta, sin cerrar la sesión ni usarla como estado vivo.

- [ ] **Step 1: Añadir actualización de la prueba real**

Registrar fecha, autorización, participante, alcance mínimo, conservación, convención de identificadores, zonas detectadas, zona profundizada y resultado.

- [ ] **Step 2: Añadir correcciones realizadas**

Registrar que la primera materialización no siguió los templates por una resolución errónea de ruta; documentar la normalización posterior, la creación de la transcripción y la ampliación de templates.

- [ ] **Step 3: Registrar el no-checkpoint**

Dejar constancia de que la inmersión terminó y por eso no se creó checkpoint, sin presentarlo como omisión.

### Task 4: Verificar el conjunto completo

**Files:**
- Verify: `docs/templates/artefactos-cobertura-profesional/`
- Verify: `docs/metodologia/playbooks/`
- Verify: `docs/superpowers/specs/2026-07-19-preparacion-piloto-cobertura-profesional-design.md`
- Verify: `.pcs/sesiones/sesion-20260705-concepto-cobertura-profesional-carrera-ai.md`

- [ ] **Step 1: Comprobar templates y referencias locales**

Run: `rg -n "TEMPLATE_TRANSCRIPCION|alcance_aprobado|conservacion_aprobada|id_zona|## Validaciones|no aplica" docs/templates/artefactos-cobertura-profesional docs/metodologia/playbooks docs/superpowers/specs/2026-07-19-preparacion-piloto-cobertura-profesional-design.md .pcs/sesiones/sesion-20260705-concepto-cobertura-profesional-carrera-ai.md`

Expected: no falta ningún elemento requerido.

- [ ] **Step 2: Revisar enlaces y formato**

Run: `git diff --check -- docs/templates docs/metodologia/playbooks docs/superpowers/specs/2026-07-19-preparacion-piloto-cobertura-profesional-design.md .pcs/sesiones/sesion-20260705-concepto-cobertura-profesional-carrera-ai.md`

Expected: sin errores de whitespace; comprobar manualmente ortografía española y destino de enlaces Markdown.
