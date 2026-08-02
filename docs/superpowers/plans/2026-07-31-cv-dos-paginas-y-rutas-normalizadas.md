# CV de dos páginas y rutas normalizadas — Plan de implementación

> **Para agentes:** SUBSKILL OBLIGATORIA: usar `superpowers:executing-plans` para ejecutar este plan tarea por tarea. Los pasos se controlan con casillas.

**Objetivo:** Permitir CV de una o dos páginas, detener únicamente los CV de más de dos páginas con una decisión humana explícita y aceptar rutas de entrada de Windows sin debilitar las rutas canónicas del expediente.

**Arquitectura:** El generador distinguirá entre el límite máximo del CV y el límite de una página de la carta. La normalización se aplicará solo al argumento de entrada del CLI, que puede contener `\\`, mientras que `datos-generacion.json` seguirá exigiendo rutas relativas canónicas con `/`.

**Tecnología:** Python 3, unittest, pypdf, JSON y Markdown.

## Restricciones globales

- El CV admite como máximo 2 páginas; la carta mantiene exactamente 1.
- Un CV de más de 2 páginas se conserva para revisión y no se publica.
- La reanudación exige una decisión humana registrada.
- No se reinician la sesión Job-up, el análisis de la oferta ni la candidatura.
- Las rutas almacenadas en JSON y documentos siguen usando `/`.

---

### Tarea 1: Definir los límites y la normalización mediante pruebas

**Archivos:**
- Modificar: `tests/test_generar_candidatura.py`
- Modificar: `scripts/job-up/generar_candidatura.py`

**Interfaces:**
- Consume: `resolve_input_json(root: Path, value: str) -> Path`.
- Produce: `validate_pdf(path, require_image=False, max_pages=1)` y rutas CLI normalizadas.

- [x] **Paso 1: Escribir las pruebas que fallan**

```python
def test_cli_input_accepts_windows_separators_inside_project(self):
    value = r"boveda-entrevista-profesional\busqueda-empleo\proceso\plantillas\TEMPLATE_DATOS_GENERACION_CANDIDATURA.json"
    self.assertEqual(resolve_input_json(ROOT, value), (ROOT / value.replace("\\", "/")).resolve())

def test_cv_accepts_two_pages_and_rejects_three(self):
    self.assertIsNone(validate_pdf(two_page_pdf, max_pages=2))
    with self.assertRaises(PdfValidationError):
        validate_pdf(three_page_pdf, max_pages=2)
```

- [x] **Paso 2: Ejecutar las pruebas y comprobar que fallan**

Ejecutar:

```text
python -m unittest tests.test_generar_candidatura.GeneratorContractTests.test_cli_input_accepts_windows_separators_inside_project tests.test_generar_candidatura.GeneratorContractTests.test_cv_accepts_two_pages_and_rejects_three
```

Resultado esperado: fallo porque el CLI rechaza `\\` y el validador exige una página exacta.

- [x] **Paso 3: Aplicar la implementación mínima**

```python
normalized = value.replace("\\", "/")
max_pages = 2
if actual_pages > max_pages:
    raise PdfValidationError(path, actual_pages, max_pages)
```

- [x] **Paso 4: Ejecutar las pruebas y comprobar que pasan**

Ejecutar el mismo comando del paso 2.

### Tarea 2: Mantener el bloqueo humano y la publicación coherentes

**Archivos:**
- Modificar: `scripts/job-up/generar_candidatura.py`
- Modificar: `tests/test_generar_candidatura.py`

**Interfaces:**
- Consume: `PdfValidationError.actual_pages` y `PdfValidationError.expected_pages`.
- Produce: `revision-generacion.json` con el máximo de páginas y la ruta del PDF preservado.

- [x] **Paso 1: Escribir una prueba que falle**

```python
def test_generation_review_reports_two_page_limit_for_three_page_cv(self):
    review = preserve_generation_review(..., "cv.pdf", actual_pages=3, expected_pages=2)
    self.assertEqual(review["paginas_esperadas"], 2)
```

- [x] **Paso 2: Ejecutar la prueba y comprobar que falla**

Ejecutar:

```text
python -m unittest tests.test_generar_candidatura.GeneratorContractTests.test_generation_review_reports_two_page_limit_for_three_page_cv
```

- [x] **Paso 3: Implementar el límite por tipo de documento**

El flujo principal debe usar `max_pages=2` solo para `cv.pdf`, `max_pages=1` para `carta-presentacion.pdf` y los mismos límites durante la publicación.

- [x] **Paso 4: Ejecutar la prueba y la batería completa**

Ejecutar:

```text
python -m unittest discover -s tests -p "test_*.py"
```

### Tarea 3: Alinear la skill y la guía con el contrato ejecutable

**Archivos:**
- Modificar: `.codex/skills/job-up-candidatura-oferta/SKILL.md`
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/GUIA_FORMATO_CV_Y_CARTA.md`

**Interfaces:**
- Consume: el límite implementado en el generador.
- Produce: instrucciones inequívocas para CV, carta, rutas y reanudación.

- [x] **Paso 1: Documentar el contrato**

El CV debe indicar «hasta dos páginas»; la carta, «una página». La detención solo se activa si el CV supera dos páginas o la carta supera una. La skill debe mostrar la ruta preservada y esperar la decisión humana.

- [x] **Paso 2: Verificar la redacción**

Ejecutar:

```text
rg -n -i "una página|dos páginas|barras invertidas|revision-generacion" .codex/skills/job-up-candidatura-oferta/SKILL.md boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/GUIA_FORMATO_CV_Y_CARTA.md
```

Corregir cualquier contradicción detectada.

### Tarea 4: Verificación de salida

**Archivos:**
- Verificar: `scripts/job-up/generar_candidatura.py`
- Verificar: `tests/test_generar_candidatura.py`
- Verificar: los documentos de contrato modificados.

- [x] **Paso 1: Ejecutar pruebas y comprobación estática**

```text
python -m unittest discover -s tests -p "test_*.py"
python -m py_compile scripts/job-up/generar_candidatura.py
git diff --check
```

- [x] **Paso 2: Revisar el alcance**

Confirmar que solo se modificaron el generador, sus pruebas, la skill, la guía y este plan; no alterar expedientes ni cambios de terceros.
