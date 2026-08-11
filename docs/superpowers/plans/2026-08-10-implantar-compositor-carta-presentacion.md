# Compositor de carta de presentación — Plan de implantación

> **Para agentes de implementación:** ejecutar este plan respetando la frontera semántica cerrada y sin diseñar el veredicto final de carta.

**Objetivo:** convertir determinísticamente la sección `Carta completa consolidada` aprobada de CAND-2026-020 en `carta-presentacion.docx`, `carta-presentacion.pdf` y una evaluación auditable, demostrando equivalencia textual y calidad de render.

**Arquitectura:** un extractor obtiene exclusivamente la sección autorizada; un compositor `python-docx` aplica un diseño de carta sobrio y genera DOCX; LibreOffice convierte ese mismo DOCX a PDF; un auditor extrae y normaliza texto de fuente, DOCX y PDF, comprueba orden, cifras, privacidad y render, y genera el registro de composición. La fase nunca consulta otras fuentes para decidir contenido.

**Tecnologías:** Python, `python-docx`, `pypdf`, Pillow, LibreOffice `soffice.com`, `pdftoppm`/renderizador documental.

## Restricciones globales

- Entrada única: `contenido-carta-presentacion.md` → `Carta completa consolidada`.
- Precondiciones: contenido `apto`, gate de composición aprobado humanamente, `presentada: false`.
- Estados: `apta`, `requiere_correccion_composicion`, `requiere_revision_contenido`, `bloqueada`.
- No modificar semántica, orden, cifras, firma, saludo, cierre ni datos personales.
- No diseñar ni implementar veredicto final de carta ni presentación externa.
- Entregables exclusivos: DOCX, PDF y evaluación de composición.

## Tareas

### Tarea 1: Contrato y precondiciones

**Archivos:**
- Modificar: `docs/ideas-y-debates/mejoras-job-up/PLAYBOOK_COMPONER_CARTA_PRESENTACION.md` (estado `en_prueba`).
- Modificar: `docs/ideas-y-debates/mejoras-job-up/TEMPLATE_COMPOSICION_CARTA_PRESENTACION.md` (estado `en_prueba`).
- Test: `tests/test_componer_carta_presentacion.py`.

- [ ] Verificar que el playbook/template contienen los contratos completos y normalizar solo su estado provisional.
- [ ] Definir fixtures sintéticos para gates, contenido no apto, omisión, adición, cifra, orden, privacidad y diferencias tipográficas.
- [ ] Ejecutar la prueba específica en rojo antes de implementar el compositor.

### Tarea 2: Extracción y compositor DOCX/PDF

**Archivos:**
- Crear: `scripts/job-up/componer_carta_presentacion.py`.
- Test: `tests/test_componer_carta_presentacion.py`.

- [ ] Implementar extracción determinista de `## 16. Carta completa consolidada` hasta el siguiente encabezado de nivel 2.
- [ ] Validar frontmatter, gate, `estado_contenido`, candidatura y `presentada` antes de generar.
- [ ] Crear DOCX con tipografía sobria, márgenes legibles, contacto autorizado y párrafos en el orden fuente.
- [ ] Convertir el DOCX a PDF con `soffice.com`, perfil temporal aislado y sin reintento ante `bootstrap.ini`.
- [ ] Exponer funciones reutilizables para extraer texto DOCX/PDF, normalizar equivalencias y auditar salidas.

### Tarea 3: Auditoría y registro

**Archivos:**
- Modificar: `scripts/job-up/componer_carta_presentacion.py`.
- Crear: `evaluacion-composicion-carta-presentacion.md` en la candidatura.
- Test: `tests/test_componer_carta_presentacion.py`.

- [ ] Comprobar fuente=DOCX=PDF, orden, cifras `30 %` y `80 %`, privacidad y ausencia de marcadores/comentarios/revisión.
- [ ] Clasificar incidencias según precedencia y no corregir semántica.
- [ ] Rellenar el template con hashes, configuración visual, resultados, incidencias y recomendación del gate con decisión humana pendiente.

### Tarea 4: Caso real y QA visual

**Archivos:**
- Crear: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/carta-presentacion.docx`.
- Crear: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/carta-presentacion.pdf`.
- Crear: `.../evaluacion-composicion-carta-presentacion.md`.
- Modificar: `.../candidatura.md` para inventariar los artefactos y mantener `presentada: false`.

- [ ] Ejecutar el compositor una sola vez sobre la fuente aprobada.
- [ ] Renderizar el DOCX a PNG/PDF y revisar todas las páginas; comprobar que no hay cortes, superposiciones ni página vacía.
- [ ] Ejecutar tests específicos, suite completa y `git diff --check`.
- [ ] Actualizar PCS con el resultado sin abrir el veredicto final de carta ni el gate de presentación.
