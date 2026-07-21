# Voz narrativa de candidaturas Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Impedir que las candidaturas copien verbos en tercera persona desde la matriz factual.

**Architecture:** [[datos-core-busqueda]] conserva su función de fuente factual en tercera persona. El playbook añade una transformación de voz y una lista de control que distingue las acciones de la persona candidata de las acciones de otros sujetos.

**Tech Stack:** Markdown y wikilinks de Obsidian.

## Global Constraints

- No modificar [[datos-core-busqueda]].
- Mantener la trazabilidad factual de cada frase.
- Redactar las acciones de la persona candidata en primera persona.
- Mantener tercera persona solo si el sujeto es distinto de la persona candidata.
- No autorizar envíos de candidaturas.

---

### Task 1: Añadir transformación y validación de voz

**Files:**
- Modify: `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md`

**Interfaces:**
- Consumes: [[datos-core-busqueda]] como fuente factual en tercera persona.
- Produces: una regla de redacción aplicable antes de generar CV y carta.

- [ ] **Step 1: Añadir la regla de transformación en «Selección factual».**

Insertar después de los límites factuales este bloque:

```markdown
### Transformación de voz narrativa

[[datos-core-busqueda]] registra los hechos en tercera persona y no se copia literalmente en los documentos de candidatura.

- Redactar en primera persona cada acción cuyo sujeto sea la persona candidata: «Diseñé», «Automaticé», «Clasifiqué».
- Mantener la tercera persona cuando el sujeto sea distinto, por ejemplo: «el personal pasó a recibir…» o «las decisiones correspondían al Consejo de Dirección».
- Cambiar únicamente la voz gramatical; no ampliar responsabilidades, métricas, titulaciones, tecnologías ni resultados.
```

- [ ] **Step 2: Añadir el control previo a la producción.**

Insertar como primer paso de «Producción documental»:

```markdown
1. Revisar cada logro seleccionado: identificar su sujeto, usar primera persona si la acción corresponde a la persona candidata y conservar tercera persona solo para otros sujetos.
```

Renumerar los pasos posteriores de esa sección.

- [ ] **Step 3: Añadir la comprobación a la lista final.**

Insertar este elemento antes de la comprobación de bloqueo:

```markdown
- [ ] Los verbos de acción de la persona candidata están en primera persona; la tercera persona solo describe a otros sujetos.
```

- [ ] **Step 4: Verificar alcance y redacción.**

Ejecutar:

```powershell
rg -n 'Transformación de voz|primera persona|tercera persona|No se copia literalmente|No autoriza enviar' docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md
git diff --check -- docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md
```

Esperado: las cinco expresiones aparecen en el playbook y no hay errores de formato.

- [ ] **Step 5: Commit.**

```powershell
git add docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md
git commit -m "docs: exige primera persona en candidaturas"
```
