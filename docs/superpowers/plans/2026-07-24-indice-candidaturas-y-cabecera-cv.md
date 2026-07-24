# Índice de candidaturas y cabecera de CV Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Hacer que cada ficha `candidatura.md` inventaríe todos los artefactos operativos de su carpeta y fijar en el generador de CV la cabecera centrada con espacio reservado antes de «Perfil profesional».

**Architecture:** La ficha de candidatura será el índice legible de los documentos preparados para una oferta. El playbook y su plantilla convertirán esa actualización en un requisito de creación y de mantenimiento. El generador compartido de CV conservará la pauta visual de la candidatura Pro a Pro —incluido su párrafo espaciador— sin regenerar ni sobrescribir el CV de referencia editado por el usuario.

**Tech Stack:** Markdown con wikilinks de Obsidian; Python 3 y `python-docx`; DOCX existente como referencia visual.

## Global Constraints

- Trabajar sobre los cambios ya existentes: no descartar ni sobrescribir ajustes manuales del usuario.
- Documentación en español de España y con revisión ortográfica final.
- Listar en la ficha los artefactos de candidatura (Markdown, DOCX y PDF), no las capturas PNG ni otros controles visuales internos.
- Una ficha se actualiza al crear la candidatura y cada vez que se incorpora un artefacto nuevo a su carpeta.
- El encabezado de todo CV generado contiene nombre, titular y contacto centrados, seguido de un párrafo espaciador que conserve el mismo espacio de separación validado en el CV de Pro a Pro antes de «Perfil profesional».
- No se realizarán `git add`, commits ni regeneraciones que puedan sobrescribir el CV de referencia.

---

### Task 1: Auditar los artefactos e indexar las candidaturas existentes

**Files:**
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-001-evershine-investments-administrativo/candidatura.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-002-islas-natura-07-tecnico-administrativo/candidatura.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-003-randstad-auxiliar-administrativo-prl/candidatura.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-004-globaenergy-auxiliar-administrativo-back-office/candidatura.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-005-proapro-tecnico-distribucion-logistica/candidatura.md`
- Test: inventario generado mediante `Get-ChildItem` y comprobación de enlaces mediante `rg`.

**Interfaces:**
- Consumes: el contenido real de cada carpeta `CAND-2026-*`.
- Produces: una sección `## Documentos de la candidatura` con los enlaces a todos los artefactos operativos existentes.

- [x] **Step 1: Inventariar los archivos relevantes de cada carpeta.**

  Ejecutar:

  ```powershell
  Get-ChildItem 'boveda-entrevista-profesional/busqueda-empleo/candidaturas' -Directory |
    ForEach-Object { Get-ChildItem $_.FullName -File | Where-Object { $_.Extension -in '.md', '.docx', '.pdf' } }
  ```

  Esperado: lista de artefactos Markdown, DOCX y PDF para CAND-2026-001 a CAND-2026-005, sin capturas PNG.

- [x] **Step 2: Reemplazar o completar el índice documental de cada ficha.**

  Normalizar las cinco fichas a la estructura exacta siguiente, conservando solo enlaces a archivos que realmente existan:

  ```markdown
  ## Documentos de la candidatura

  ### Análisis y preparación

  - [[analisis-oferta|Análisis de la oferta]]
  - [[guion-adaptacion-cv|Guion de adaptación del CV]]
  - [[veredicto-final-cv|Veredicto final del CV]]
  - [[informe-empresa-entrevista|Informe de empresa y preparación de entrevista]]

  ### Documentos para revisión y envío

  - [[cv.docx|CV (DOCX)]]
  - [[cv.pdf|CV (PDF)]]
  - [[carta-presentacion.docx|Carta de presentación (DOCX)]]
  - [[carta-presentacion.pdf|Carta de presentación (PDF)]]
  ```

  No incluir enlaces muertos ni enlazar la propia ficha `candidatura.md`.

- [x] **Step 3: Verificar la cobertura de enlaces.**

  Ejecutar:

  ```powershell
  rg -n "^## Documentos de la candidatura|^\- \[\[" boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-*/candidatura.md
  ```

  Esperado: las cinco fichas incluyen la sección y cada artefacto operativo inventariado figura una sola vez en ella.

### Task 2: Convertir el índice documental en una regla del flujo

**Files:**
- Modify: `boveda-entrevista-profesional/busqueda-empleo/templates/TEMPLATE_CANDIDATURA.md`
- Modify: `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md`
- Test: búsqueda textual de la obligación de creación y actualización posterior.

**Interfaces:**
- Consumes: patrón documental validado en Task 1.
- Produces: una plantilla y un playbook que obligan a mantener el índice de la ficha sincronizado con los artefactos.

- [x] **Step 1: Convertir la plantilla en un índice completo.**

  Sustituir el bloque de cuatro rutas sueltas por `## Documentos de la candidatura`, con dos grupos: `### Análisis y preparación` y `### Documentos para revisión y envío`. Incluir enlaces de plantilla para análisis, guion, veredicto, informe de empresa cuando exista, CV DOCX/PDF y carta DOCX/PDF.

- [x] **Step 2: Añadir la obligación operativa al playbook.**

  En «6. Producción documental», añadir un paso que exija actualizar `candidatura.md` al crear cada artefacto y volver a actualizarlo cuando se añada o sustituya cualquier documento posterior. El paso debe exigir enumerar todos los artefactos operativos existentes, no solo CV y carta.

- [x] **Step 3: Añadir comprobaciones de cierre.**

  En «7. Revisión humana y salida de fase 1» y «8. Lista de control final», exigir que el índice de `candidatura.md` coincida con la carpeta y que no haya enlaces a archivos inexistentes.

- [x] **Step 4: Verificar las dos condiciones temporales.**

  Ejecutar:

  ```powershell
  rg -n -i "crear.*artefacto|añada|sustituya|índice.*document" boveda-entrevista-profesional/busqueda-empleo/templates/TEMPLATE_CANDIDATURA.md docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md
  ```

  Esperado: existe una instrucción explícita tanto para la creación inicial como para la incorporación posterior de documentos.

### Task 3: Fijar la cabecera reutilizable del CV

**Files:**
- Modify: `tools/generate_adapted_cvs.py:54-120`
- Test: inspección con `python-docx` de la referencia Pro a Pro y comprobación estática de los parámetros del generador.

**Interfaces:**
- Consumes: los valores de alineación y espaciado de los primeros párrafos de `CAND-2026-005-proapro-tecnico-distribucion-logistica/cv.docx`.
- Produces: `build(path, config)` con una cabecera de tres líneas centradas y un párrafo espaciador explícito antes de `heading(doc, "Perfil profesional")`.

- [x] **Step 1: Medir la referencia sin modificarla.**

  Ejecutar un script de solo lectura con `python-docx` que muestre para los seis primeros párrafos: texto, alineación, `space_before`, `space_after` y tamaño de fuente.

  Esperado: nombre, titular y contacto centrados, con espaciados de 0, 1 y 5 pt respectivamente; a continuación, un párrafo vacío con 6 pt antes y 2 pt después, y el encabezado de perfil con 6 pt antes y 2 pt después.

- [x] **Step 2: Declarar constantes de diseño en el generador.**

  Junto a las constantes tipográficas, definir valores con nombre para `HEADER_ALIGNMENT = WD_ALIGN_PARAGRAPH.CENTER`, `HEADER_SPACER_BEFORE_PT = 6.0` y `HEADER_SPACER_AFTER_PT = 2.0`. No codificar el hueco como números sin nombre en la llamada a `paragraph`.

- [x] **Step 3: Aplicar el patrón a las tres líneas de cabecera.**

  Sustituir las alineaciones izquierdas de nombre, titular y contacto por `HEADER_ALIGNMENT`. Mantener sus espacios posteriores de 0, 1 y 5 pt e insertar `paragraph(doc, "", before=HEADER_SPACER_BEFORE_PT, after=HEADER_SPACER_AFTER_PT, align=WD_ALIGN_PARAGRAPH.LEFT)` antes de la llamada a `heading(doc, "Perfil profesional")`.

- [x] **Step 4: Verificar el origen y preservar el documento de referencia.**

  Ejecutar:

  ```powershell
  rg -n -C 2 "HEADER_ALIGNMENT|HEADER_SPACER_|Perfil profesional" tools/generate_adapted_cvs.py
  ```

  Esperado: las tres líneas de cabecera usan la constante de centrado y el párrafo vacío reserva el hueco con constantes nombradas. No ejecutar el generador sobre CAND-2026-005 ni modificar su `cv.docx`.

### Task 4: Revisión final de integridad documental

**Files:**
- Modify: `docs/superpowers/plans/2026-07-24-indice-candidaturas-y-cabecera-cv.md` (marcar tareas realizadas).
- Test: revisión ortográfica y comprobación final de inventario.

**Interfaces:**
- Consumes: resultados de Tasks 1 a 3.
- Produces: artefactos sincronizados y reglas de mantenimiento verificadas.

- [x] **Step 1: Comprobar enlaces locales de las cinco fichas.**

  Ejecutar una comprobación de solo lectura que extraiga los destinos de los wikilinks y confirme que existe el archivo con extensión explícita o el Markdown correspondiente dentro de la misma carpeta.

  Esperado: cero enlaces documentales rotos.

- [x] **Step 2: Revisar ortografía española.**

  Revisar manualmente los nuevos textos de plantilla, playbook y fichas, corrigiendo tildes, concordancia y signos de puntuación.

- [x] **Step 3: Registrar el resultado en este plan.**

Resultado: los cinco índices documentales coinciden con los archivos operativos de sus carpetas y no tienen enlaces rotos. Se conservaron fuera del índice las capturas PNG de control visual. El CV de Pro a Pro no se regeneró ni modificó durante la validación.

  Marcar todas las casillas completadas solo tras obtener las verificaciones esperadas y anotar cualquier excepción real.

## Self-Review

- Cobertura: Task 1 satisface la actualización de todas las candidaturas existentes; Task 2 fija la regla para creación y documentos posteriores; Task 3 reproduce la cabecera y reserva el hueco para la fotografía; Task 4 verifica enlaces y ortografía.
- Sin marcadores pendientes: no contiene `TODO`, `TBD`, «similar a» ni instrucciones sin rutas, comandos o contenido operativo.
- Consistencia: la única interfaz de generación afectada es `build(path, config)` y usa las mismas constantes declaradas en Task 3.
