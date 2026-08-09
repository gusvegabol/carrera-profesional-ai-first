# Compositor de CV para datos de generación 1.2 — Plan de implantación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Sustituir el generador histórico CV+carta por un flujo CV-only que componga `cv.docx`, `cv.pdf` y `cv.tex` desde `datos-generacion.json` 1.2.

**Architecture:** Un compositor puro transforma `contenido_cv` en un modelo intermedio ordenado. Los renderizadores DOCX y LaTeX consumen ese mismo modelo; el orquestador reutiliza conversión, validación y publicación transaccional.

**Tech Stack:** Python 3, `python-docx`, Pillow, `pypdf`, LibreOffice `soffice.com`, `unittest`.

## Global Constraints

- El contrato activo es CV-only 1.2.
- Los textos visibles se reproducen literalmente.
- Todas las colecciones se ordenan exclusivamente mediante `orden`.
- Solo se publican `cv.docx`, `cv.pdf` y `cv.tex`.
- La carta queda fuera de alcance.
- La fotografía canónica es obligatoria por defecto.
- La excepción sin fotografía no se implementa hasta aprobar su contrato.
- LibreOffice solo se usa para convertir DOCX→PDF, con perfil temporal aislado y sin reintento ante `bootstrap.ini`.
- Toda documentación en español debe revisarse ortográficamente.

---

### Task 1: Contrato ejecutable y modelo intermedio pasivo

**Files:**
- Create: `scripts/job-up/componer_cv.py`
- Create: `tests/test_componer_cv.py`
- Modify: `scripts/job-up/validar_datos_generacion_cv.py`

**Interfaces:**
- Consumes: `dict[str, Any]` ya cargado desde `datos-generacion.json` 1.2.
- Produces: `construir_modelo_cv(documento: dict[str, Any]) -> RenderCV`.

- [ ] Escribir pruebas fallidas con valores literales para orden de encabezado, contactos, secciones, bloques, cabeceras y unidades.
- [ ] Ejecutar `python -m unittest tests.test_componer_cv -v` y confirmar fallos por ausencia de la interfaz.
- [ ] Crear dataclasses inmutables para el árbol `RenderCV` y construirlo solo desde `contenido_cv`.
- [ ] Hacer que el validador 1.2 sea el único gate contractual previo al modelo.
- [ ] Ejecutar las pruebas y confirmar que pasan.
- [ ] Añadir una prueba de independencia que modifique `candidatura`, `control` y archivos externos sin alterar el modelo.

### Task 2: Renderizador LaTeX dinámico

**Files:**
- Modify: `scripts/job-up/componer_cv.py`
- Modify: `tests/test_componer_cv.py`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_CV_FORMATO.tex`

**Interfaces:**
- Consumes: `RenderCV`.
- Produces: `renderizar_latex(modelo: RenderCV) -> str`.

- [ ] Escribir una prueba fallida con secciones variables, viñetas y caracteres especiales.
- [ ] Confirmar que falla porque todavía no existe el renderizador dinámico.
- [ ] Implementar el escape técnico de LaTeX y el renderizado desde el modelo común.
- [ ] Confirmar orden, texto visible y estructura balanceada mediante pruebas.

### Task 3: Renderizador DOCX dinámico con fotografía obligatoria

**Files:**
- Modify: `scripts/job-up/componer_cv.py`
- Modify: `tests/test_componer_cv.py`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_CV_FORMATO.docx`

**Interfaces:**
- Consumes: `RenderCV`, plantilla DOCX y ruta explícita de fotografía canónica.
- Produces: `renderizar_docx(modelo: RenderCV, plantilla: Path, destino: Path, fotografia: Path) -> None`.

- [ ] Escribir pruebas fallidas para estructura dinámica, cantidades variables, viñetas y fotografía incluida.
- [ ] Confirmar los fallos antes de modificar producción.
- [ ] Reutilizar estilos y encabezado de la plantilla, reemplazando el cuerpo fijo por nodos dinámicos.
- [ ] Incorporar únicamente la fotografía recibida explícitamente y validarla.
- [ ] Inspeccionar el OOXML resultante y confirmar que no quedan marcadores.
- [ ] Mantener sin implementar el modo sin fotografía.

### Task 4: Orquestador CV-only y publicación de tres artefactos

**Files:**
- Modify: `scripts/job-up/generar_candidatura.py`
- Modify: `tests/test_generar_candidatura.py`

**Interfaces:**
- Consumes: ruta a `datos-generacion.json` 1.2.
- Produces: `cv.docx`, `cv.pdf`, `cv.tex` y manifiesto técnico.

- [ ] Reemplazar en pruebas la integración de cinco artefactos por una expectativa literal de tres.
- [ ] Confirmar que las pruebas fallan contra el generador histórico.
- [ ] Derivar la carpeta de candidatura desde la ubicación segura del JSON y comprobar el identificador.
- [ ] Conectar validador, modelo, renderizadores, conversión y validaciones.
- [ ] Parametrizar publicación, restauración y manifiesto para las tres salidas.
- [ ] Retirar del flujo activo toda generación o validación de carta.
- [ ] Confirmar que el manifiesto declara fotografía incluida.
- [ ] Ejecutar las pruebas del orquestador y corregir únicamente los fallos del nuevo contrato.

### Task 5: Pruebas negativas y de independencia

**Files:**
- Modify: `tests/test_componer_cv.py`
- Modify: `tests/test_generar_candidatura.py`
- Reuse: `tests/fixtures/datos-generacion-cv/`

**Interfaces:**
- Consumes: fixtures positivos y negativos del contrato 1.2.
- Produces: evidencia de rechazo y de independencia semántica.

- [ ] Probar rutas externas, identificador discordante, fotografía ausente o inválida y JSON no válido.
- [ ] Probar que no se crea ningún artefacto de carta.
- [ ] Probar que cambios en candidatura, guion, análisis, datos-core y seguimiento no alteran los documentos generados.
- [ ] Probar rollback después de una publicación parcial de tres salidas.
- [ ] Ejecutar toda la batería `tests` y registrar el resultado.

### Task 6: Casos reales y comprobación visual

**Files:**
- Consume: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/datos-generacion.json`
- Consume: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-019-asic-consultores-responsable-automatizacion-ia/datos-generacion.json`
- Produce in each candidate folder: `cv.docx`, `cv.pdf`, `cv.tex`

**Interfaces:**
- Consumes: los dos JSON productivos aprobados.
- Produces: tres artefactos por candidatura.

- [ ] Generar CAND-2026-020 y verificar estructura, literalidad, orden y fotografía.
- [ ] Generar CAND-2026-019 y repetir las mismas comprobaciones.
- [ ] Renderizar los PDF a imágenes con una herramienta distinta de LibreOffice y revisar legibilidad, cortes, fotografía y máximo de dos páginas.
- [ ] Comparar el texto extraído de ambos formatos con el modelo intermedio.

### Task 7: Sincronización documental y PCS

**Files:**
- Modify: `docs/ideas-y-debates/mejoras-job-up/SPEC-Arquitectura-modular-generación-candidatura-v0-4-0.md`
- Modify: `.pcs/estado/estado-actual.md`
- Modify: `.pcs/sesiones/sesion-20260805-1757-job-up.md`
- Modify if required: candidate inventories in `candidatura.md`

**Interfaces:**
- Consumes: evidencia técnica y resultados reales.
- Produces: estado documental trazable y vacío contractual de fotografía registrado.

- [ ] Registrar el compositor CV-only implantado y sus resultados, sin declarar resuelta la excepción sin fotografía.
- [ ] Registrar la propuesta contractual mínima `incluir_fotografia`, expresamente pendiente de aprobación.
- [ ] Actualizar inventarios solo con artefactos realmente creados.
- [ ] Revisar ortografía, enlaces y coherencia de estados.
- [ ] Ejecutar una verificación final completa y preparar el informe solicitado.
