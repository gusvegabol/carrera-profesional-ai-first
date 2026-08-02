# Preservar negrita de cabeceras del CV Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Mantener la negrita de todo el valor que sustituye cada marcador `[EXPERIENCIA N CABECERA]` en el CV generado.

**Architecture:** El reemplazo de marcadores conservará la propiedad de formato del marcador completo cuando el texto sustituido sea más largo que el marcador. Las descripciones conservarán su formato normal y el separador no cambiará.

**Tech Stack:** Python, python-docx, unittest.

## Global Constraints

- Modificar únicamente el reemplazo de formato y su prueba de regresión.
- Mantener la compatibilidad con marcadores divididos en varios runs.
- No alterar la validación, las rutas ni la generación de PDF.

---

### Task 1: Reemplazo de marcadores con formato de cabecera preservado

**Files:**

- Modify: `scripts/job-up/generar_candidatura.py`
- Modify: `tests/test_generar_candidatura.py`

**Interfaces:**

- Consumes: `_replace_docx_paragraph(paragraph, values)` y `_set_paragraph_text(paragraph, text)`.
- Produces: un párrafo DOCX en el que el texto de una cabecera de experiencia conserva negrita completa y la descripción no hereda esa negrita.

- [x] **Step 1: Escribir la prueba que falla**

```python
def test_docx_preserves_full_bold_experience_header_after_long_replacement(self):
    # Generar un CV con una cabecera más larga que el marcador y comprobar que
    # todos sus runs tienen bold=True, mientras la descripción tiene bold=False.
```

- [x] **Step 2: Ejecutar la prueba y verificar el fallo**

Run: `python -m unittest tests.test_generar_candidatura.GeneratorContractTests.test_docx_preserves_full_bold_experience_header_after_long_replacement`

Expected: fallo porque la porción de cabecera que excede el marcador hereda el formato normal de la descripción.

- [x] **Step 3: Implementar el cambio mínimo**

```python
# Al sustituir un marcador de cabecera de experiencia, aplicar a todos los
# caracteres del valor el rPr del primer carácter del marcador, no el estilo
# posicional que sigue al marcador.
```

- [x] **Step 4: Ejecutar la prueba de regresión y la batería completa**

Run: `python -m unittest tests.test_generar_candidatura`

Expected: todas las pruebas pasan.

- [x] **Step 5: Regenerar el CV afectado y revisar el formato**

Run: `python scripts/job-up/generar_candidatura.py <datos-generacion.json>`

Expected: los cinco artefactos se regeneran y las cabeceras completas de experiencia aparecen en negrita.
