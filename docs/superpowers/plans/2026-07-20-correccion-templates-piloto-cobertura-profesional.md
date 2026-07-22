# Corrección de templates y artefactos del piloto de cobertura profesional Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Hacer explícita la ubicación canónica de los templates en la documentación operativa y adecuar los artefactos del primer piloto a esos templates sin perder la identificación aprobada ni la transcripción verbatim.

**Architecture:** La ruta canónica de reutilización será `docs/templates/artefactos-cobertura-profesional/`; los artefactos reales permanecerán en `boveda-entrevista-profesional/artefactos-cobertura-profesional/`. Los playbooks y el contrato enlazarán la misma ruta, mientras que cada artefacto conservará el frontmatter y las secciones de su template correspondiente.

**Tech Stack:** Markdown, frontmatter YAML, enlaces Markdown relativos, PowerShell para verificaciones estructurales.

## Global Constraints

- Mantener la convención aprobada del piloto: `ENT-001`, `ENT-001-M01`, zonas con contador propio e intentos `a`, `b`, etc.
- No modificar las plantillas canónicas para resolver necesidades particulares de este caso.
- Mantener la cobertura parcial y sus límites explícitos.
- Mantener la transcripción verbatim como artefacto adicional de auditoría.
- No modificar `.pcs/` ni convertir el resultado experimental en decisión metodológica formal.

---

### Task 1: Documentar la ubicación canónica de los templates

**Files:**
- Modify: `docs/metodologia/playbooks/PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_0.md`
- Modify: `docs/metodologia/playbooks/PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA.md`
- Modify: `docs/superpowers/specs/2026-07-19-preparacion-piloto-cobertura-profesional-design.md`

**Interfaces:**
- Consumes: la ruta vigente `docs/templates/artefactos-cobertura-profesional/` y sus seis templates.
- Produces: instrucciones explícitas y enlazadas para consultar el template antes de crear cada artefacto.

- [ ] **Step 1: Añadir una sección de templates al playbook de cobertura**

Incluir la ruta canónica, un enlace por tipo de artefacto y la regla de uso: consultar el template antes de crear o actualizar un artefacto real; no guardar artefactos dentro de `docs/templates/`.

- [ ] **Step 2: Añadir la referencia de templates al playbook de entrevista**

Incluir la misma ruta como referencia de salida cuando una inmersión produzca artefactos de cobertura, aclarando que el template de inmersión y el de competencia son los documentos canónicos de estructura.

- [ ] **Step 3: Corregir el contrato del piloto**

Sustituir la referencia genérica a “las plantillas existentes” por la ruta exacta y enlaces a los seis templates; indicar que la copia de trabajo, si se necesita, se crea fuera de la carpeta canónica.

- [ ] **Step 4: Verificar las referencias**

Run: `rg -n "docs/templates/artefactos-cobertura-profesional|TEMPLATE_(ENTREVISTADO|MAPA|SESION|CHECKPOINT|INMERSION|COMPETENCIA)" docs/metodologia/playbooks docs/superpowers/specs/2026-07-19-preparacion-piloto-cobertura-profesional-design.md`

Expected: aparecen referencias explícitas en los tres documentos y cada tipo de template está nombrado.

### Task 2: Adecuar los artefactos reales a los templates

**Files:**
- Modify: `boveda-entrevista-profesional/artefactos-cobertura-profesional/entrevistados/ENT-001.md`
- Modify: `boveda-entrevista-profesional/artefactos-cobertura-profesional/mapas/MAPA_ENT-001-M01.md`
- Modify: `boveda-entrevista-profesional/artefactos-cobertura-profesional/sesiones/SESION_COBERTURA_ENT-001-M01_2026-07-20.md`
- Modify: `boveda-entrevista-profesional/artefactos-cobertura-profesional/inmersiones/INMERSION_ENT-001-M01-Z001-a.md`
- Modify: `boveda-entrevista-profesional/artefactos-cobertura-profesional/competencias/COMPETENCIA_ENT-001-M01-Z001-a.md`

**Interfaces:**
- Consumes: los seis templates de `docs/templates/artefactos-cobertura-profesional/`.
- Produces: artefactos con frontmatter, encabezados, referencias y estados compatibles con sus templates.

- [ ] **Step 1: Normalizar el entrevistado**

Usar `tipo: entrevistado`, `id_entrevistado`, `alias` y `fecha_creacion`; conservar el alcance y la autorización de conservación como contenido adicional del caso.

- [ ] **Step 2: Normalizar el mapa**

Usar `tipo: mapa`, `id_mapa`, `id_entrevistado`, `fecha_creacion`, `fecha_actualizacion`, `estado: activo` y `fecha_cierre:`; reorganizar las zonas con estado, señal de origen, sesión, inmersión y competencia.

- [ ] **Step 3: Normalizar la sesión**

Usar los campos del template de sesión, completar calibración, panorámica, selección, activación, hilos abiertos, cierre y guardarraíles; usar `motivo_cierre: limite_tiempo_declarado`.

- [ ] **Step 4: Normalizar la inmersión**

Usar `tipo: inmersion`, identificadores del template, `id_competencia`, `fecha_creacion` y `resultado: competencia_validada`; incluir la ficha mínima completa de situación, acción, resultado, contexto, validaciones, calidad y límites.

- [ ] **Step 5: Normalizar la competencia**

Usar todos los campos del template, incluido `id_inmersion`, `fecha_creacion` y `calidad_evidencia: fuerte`; conservar la formulación observable, versión humana y límite.

- [ ] **Step 6: Verificar que no se cree checkpoint**

Confirmar que la ausencia de checkpoint es correcta porque la inmersión terminó y no quedó parcial; no crear un documento vacío.

### Task 3: Verificar coherencia y emitir el informe final

**Files:**
- Verify: los cinco artefactos normalizados y la transcripción.
- Verify: `docs/templates/artefactos-cobertura-profesional/`.

**Interfaces:**
- Consumes: cambios de Tasks 1 y 2.
- Produces: evidencia de que la documentación apunta a la ruta correcta, los artefactos siguen los templates y quedan identificados los elementos adicionales necesarios.

- [ ] **Step 1: Comparar campos YAML**

Run: `rg -n "^(tipo|id_|alias|fecha_|estado|motivo_cierre|resultado|calidad_evidencia):" docs/templates/artefactos-cobertura-profesional boveda-entrevista-profesional/artefactos-cobertura-profesional`

Expected: cada artefacto usa los campos canónicos de su template y no conserva los nombres incompatibles anteriores.

- [ ] **Step 2: Comprobar enlaces de artefactos**

Run: `rg -n "MAPA_ENT-001-M01|SESION_COBERTURA_ENT-001-M01_2026-07-20|INMERSION_ENT-001-M01-Z001-a|COMPETENCIA_ENT-001-M01-Z001-a|TRANSCRIPCION_ENT-001-M01_2026-07-20" boveda-entrevista-profesional/artefactos-cobertura-profesional`

Expected: las referencias apuntan a los nombres reales y la transcripción está enlazada desde la sesión y la inmersión.

- [ ] **Step 3: Revisar ortografía española y diff**

Run: `git diff --check -- docs/metodologia/playbooks docs/superpowers/specs/2026-07-19-preparacion-piloto-cobertura-profesional-design.md boveda-entrevista-profesional/artefactos-cobertura-profesional`

Expected: sin errores de espacios o formato; revisar manualmente tildes, eñes y signos de puntuación en los documentos modificados.

- [ ] **Step 4: Preparar el informe final**

Informar de los archivos corregidos y señalar expresamente que la transcripción verbatim es necesaria para auditoría pero no tiene template canónico propio; indicar también cualquier campo adicional que se haya conservado y por qué.
