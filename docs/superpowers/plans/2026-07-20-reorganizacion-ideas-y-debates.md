# Reorganización de ideas y debates — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Sustituir la carpeta temática demasiado específica por un contenedor general de ideas y debates, con subcarpetas por tema y referencias activas actualizadas.

**Architecture:** La nueva raíz será `docs/ideas-y-debates/`. Los documentos actuales se separarán en `cobertura-profesional/` e `investigacion-github/`. Las referencias históricas que describan la ubicación original de un documento se conservarán como trazabilidad; las referencias operativas y de navegación apuntarán a la nueva ubicación.

**Tech Stack:** Markdown, HTML, enlaces Markdown y enlaces Obsidian cuando el destino sea una nota de la bóveda.

## Global Constraints

- No modificar el contenido funcional de los documentos movidos.
- Mantener sus nombres de fichero.
- No eliminar la carpeta antigua hasta verificar que está vacía y que las referencias activas apuntan a la nueva estructura.
- No modificar `.pcs/estado/estado-actual.md` porque la reorganización documental no cambia el estado operativo del proyecto.
- Conservar las referencias en planes históricos cuando expresen la ruta original de creación, salvo que queden como enlaces rotos operativos.

---

### Task 1: Preparar y mover los documentos

**Files:**
- Create: `docs/ideas-y-debates/cobertura-profesional/`
- Create: `docs/ideas-y-debates/investigacion-github/`
- Move: `docs/Ideas debate - como afrontar entrevista cobertura profesional/06_Presentacion_propuesta_recomendada.html` → `docs/ideas-y-debates/cobertura-profesional/06_Presentacion_propuesta_recomendada.html`
- Move: `docs/Ideas debate - como afrontar entrevista cobertura profesional/INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md` → `docs/ideas-y-debates/investigacion-github/INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md`

- [ ] **Step 1: Confirmar los dos archivos objetivo**

Verificar que ambos existen y que la carpeta antigua solo contiene esos documentos antes de moverlos.

- [ ] **Step 2: Crear la nueva estructura**

Crear las dos subcarpetas dentro de `docs/ideas-y-debates/`.

- [ ] **Step 3: Mover los documentos**

Mover los dos archivos a sus subcarpetas temáticas, sin reescribir su contenido.

### Task 2: Actualizar referencias activas

**Files:**
- Modify: `README.md`
- Modify: `docs/superpowers/specs/2026-07-12-presentacion-propuesta-entrevista-design.md`
- Modify: `.pcs/sesiones/sesion-20260720-1242-investigacion-github-carrera-ai-first.md`

- [ ] **Step 1: Actualizar navegación del README**

Sustituir la ruta antigua de la presentación por `docs/ideas-y-debates/cobertura-profesional/06_Presentacion_propuesta_recomendada.html` y añadir la ruta de la investigación de GitHub.

- [ ] **Step 2: Actualizar la especificación de la presentación**

Cambiar las rutas de creación y referencia de la presentación a la nueva subcarpeta.

- [ ] **Step 3: Actualizar la sesión PCS de investigación**

Cambiar el documento origen a `docs/ideas-y-debates/investigacion-github/INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md`.

### Task 3: Verificar navegación y trazabilidad

**Files:**
- Verify: `docs/ideas-y-debates/`
- Verify: referencias en `README.md`, la especificación y la sesión PCS.

- [ ] **Step 1: Comprobar archivos y carpeta antigua**

Expected: ambos documentos existen en sus destinos y la carpeta antigua queda vacía.

- [ ] **Step 2: Buscar referencias activas a la ruta antigua**

Run: `rg -n "Ideas debate - como afrontar entrevista cobertura profesional|INVESTIGACION_GITHUB_CARRERA_AI_FIRST|06_Presentacion_propuesta_recomendada" README.md docs .pcs/sesiones`

Expected: las referencias operativas usan `docs/ideas-y-debates/`; las menciones históricas quedan identificables como rutas de origen de planes o mapas.

- [ ] **Step 3: Verificar formato y enlaces**

Run: `git diff --check -- README.md docs/superpowers/specs/2026-07-12-presentacion-propuesta-entrevista-design.md .pcs/sesiones/sesion-20260720-1242-investigacion-github-carrera-ai-first`

Expected: sin errores de whitespace y con destinos locales existentes.
