# README de búsqueda de empleo Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crear un índice navegable para la rama operativa de búsqueda de empleo.

**Architecture:** El README vive en la raíz de la rama operativa y se organiza por propósito, uso diario y trazabilidad. Enlaza las notas de la bóveda con wikilinks y los documentos externos a la bóveda con rutas Markdown relativas.

**Tech Stack:** Markdown y Obsidian.

## Global Constraints

- No modificar la investigación metodológica de entrevista.
- Usar wikilinks para documentos Markdown de la bóveda.
- No exponer datos privados en el README.
- Incluir únicamente enlaces existentes.

---

### Task 1: Crear el índice de la rama operativa

**Files:**
- Create: `boveda-entrevista-profesional/busqueda-empleo/README.md`

**Interfaces:**
- Consumes: los artefactos existentes de búsqueda de empleo, PCS, diseño, planificación y candidatura.
- Produces: una puerta de entrada para continuar la rama sin consultar la investigación de entrevista.

- [ ] **Step 1: Escribir propósito y límites.**

Declarar que la carpeta es la rama operativa de búsqueda de empleo dentro de Carrera AI, separada de la investigación de entrevista, y que su función es preparar candidaturas trazables con aprobación humana antes de cualquier envío.

- [ ] **Step 2: Enlazar documentos de uso diario.**

Incluir wikilinks a `[[datos-core-busqueda]]`, `[[datos-privados-candidatura]]`, `[[seguimiento-candidaturas]]`, `[[TEMPLATE_ANALISIS_OFERTA]]`, `[[TEMPLATE_CANDIDATURA]]`, `[[PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0]]` y `[[candidaturas/README]]`.

- [ ] **Step 3: Enlazar trazabilidad y planificación.**

Añadir rutas Markdown relativas a la sesión PCS, decisión, acción completada, tres especificaciones y dos planes. Incluir wikilinks a `[[analisis-oferta]]` y `[[candidatura]]`, más las rutas de los cuatro archivos de `CAND-2026-001`.

- [ ] **Step 4: Verificar enlaces y alcance.**

Ejecutar:

```powershell
rg -n '`[^`]+`|/[^/]+\.md|\[\[|datos privados|correo|teléfono' boveda-entrevista-profesional/busqueda-empleo/README.md
git diff --check -- boveda-entrevista-profesional/busqueda-empleo/README.md
```

Esperado: los enlaces de la bóveda usan wikilinks, las rutas externas existen y el README no contiene datos privados.

- [ ] **Step 5: Commit.**

```powershell
git add boveda-entrevista-profesional/busqueda-empleo/README.md
git commit -m "docs: añade índice de búsqueda de empleo"
```
