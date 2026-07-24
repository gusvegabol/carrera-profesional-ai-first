# Veredicto final del CV en Job-up — Plan de implantación

> **Para agentes:** SKILL OBLIGATORIA: usar `superpowers:executing-plans` para implantar este plan tarea por tarea. Los pasos usan casillas (`- [ ]`) para su seguimiento.

**Objetivo:** Incorporar un veredicto final reusable que compruebe la integridad del CV, puntúe su calidad en cinco criterios y determine si exige corrección, revisión o queda listo para aprobación humana.

**Arquitectura:** El veredicto es un artefacto Markdown por candidatura, creado después del CV y antes de consolidar su estado. La plantilla define los controles y la escala; el playbook incorpora el orden de ejecución; una instancia real de CAND-2026-004 prueba el flujo y conserva recomendaciones sin modificar automáticamente el CV.

**Tecnología:** Markdown compatible con Obsidian, enlaces wiki y búsquedas `rg` para verificación documental.

## Restricciones globales

- [[datos-core-busqueda]] sigue siendo la única fuente factual profesional.
- La integridad `no_apta` no se compensa con notas altas ni con la media.
- Ningún veredicto autoriza un envío ni sustituye la aprobación humana.
- La investigación contextual es posterior, opcional, requiere autorización por candidatura y muestra las URL propuestas antes de consultar fuentes.
- La escala de calidad usa las cinco notas enteras de 1 a 5 definidas en `docs/superpowers/specs/2026-07-23-veredicto-final-cv-job-up-design.md`.

---

### Tarea 1: Crear la plantilla reusable de veredicto

**Archivos:**

- Crear: `boveda-entrevista-profesional/busqueda-empleo/templates/TEMPLATE_VEREDICTO_FINAL_CV.md`
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/README.md`

**Consume:** la spec aprobada y `TEMPLATE_CANDIDATURA.md`.

**Produce:** una plantilla enlazable, con frontmatter `tipo: veredicto_final_cv`, que todas las carpetas de candidatura pueden copiar.

- [ ] **Paso 1: Crear la plantilla con identificación, integridad y las cinco reglas de calidad.**

  Incluir estos campos de identificación:

  ```markdown
  - **Candidatura:**
  - **Versión de CV evaluada:**
  - **Oferta y fecha de evaluación:**
  - **Fuentes revisadas:** [[datos-core-busqueda]], análisis de oferta y guion de adaptación.
  ```

  Incluir una tabla de integridad con las seis comprobaciones de la spec y una tabla de calidad con estas filas exactas: «Primer escaneo y posicionamiento», «Encaje competitivo», «Cobertura ATS respaldada», «Fuerza de la experiencia» y «Adecuación narrativa». Cada fila debe exigir nota, evidencia, debilidad, mejora prioritaria y límite factual.

- [ ] **Paso 2: Añadir las reglas de decisión y la mejora contextual opcional.**

  Añadir la regla de que `corregir_antes_de_revisar` se aplica con integridad `no_apta` o nota 1/2; `revisar_antes_de_aprobar` cuando todas sean al menos 3 y exista algún 3; y `lista_para_aprobacion_humana` cuando las cinco sean 4/5 e integridad sea `apta`.

  Añadir una sección «Investigación contextual opcional posterior» que obligue a registrar qué se investigaría, URL propuestas, autorización, URL utilizadas y recomendaciones; no debe incluir una consulta ni una URL inventada.

- [ ] **Paso 3: Enlazar la plantilla desde el README de búsqueda de empleo.**

  Añadir una entrada junto a las plantillas existentes:

  ```markdown
  - [[TEMPLATE_VEREDICTO_FINAL_CV]]: revisión final de integridad, calidad y decisión antes de la aprobación humana.
  ```

- [ ] **Paso 4: Verificar la plantilla.**

  Ejecutar:

  ```powershell
  rg -n "Integridad|Primer escaneo|Encaje competitivo|Cobertura ATS|Fuerza de la experiencia|Adecuación narrativa|URL propuestas|lista_para_aprobacion_humana" boveda-entrevista-profesional/busqueda-empleo/templates/TEMPLATE_VEREDICTO_FINAL_CV.md
  ```

  Esperado: al menos una coincidencia para cada control, criterio, URL propuesta y decisión.

### Tarea 2: Integrar el veredicto en el playbook y en la ficha de candidatura

**Archivos:**

- Modificar: `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md`
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/templates/TEMPLATE_CANDIDATURA.md`

**Consume:** `TEMPLATE_VEREDICTO_FINAL_CV.md` de la tarea 1.

**Produce:** un flujo que exige el veredicto antes del estado `pendiente_de_aprobacion` y una ficha que registra la versión evaluada y la decisión.

- [ ] **Paso 1: Añadir el veredicto a los artefactos de entrada del playbook.**

  Bajo «Entradas y artefactos de trabajo», incorporar [[TEMPLATE_VEREDICTO_FINAL_CV]] como artefacto que documenta la revisión de integridad, calidad y decisión antes de la aprobación humana.

- [ ] **Paso 2: Insertar el paso de veredicto en producción documental.**

  Después de crear los DOCX y PDF y de comprobarlos visualmente, el playbook debe exigir:

  ```markdown
  Completar el veredicto final del CV: comprobar integridad, puntuar los cinco criterios, registrar evidencia y mejoras, calcular la decisión sin usar la media como puerta y corregir el CV si la decisión es `corregir_antes_de_revisar`.
  ```

  Reordenar los pasos posteriores para que el registro de rutas y el estado `pendiente_de_aprobacion` ocurran solo después del veredicto.

- [ ] **Paso 3: Actualizar controles de revisión y lista final.**

  Incluir casillas que confirmen que la integridad fue `apta`, que existe el archivo de veredicto, que las notas 1/2 se corrigieron antes de aprobar y que la investigación contextual, si existe, fue autorizada y conserva sus URL.

- [ ] **Paso 4: Ampliar TEMPLATE_CANDIDATURA.**

  Añadir en «Identificación y trazabilidad» los campos:

  ```markdown
  - **Enlace al veredicto final del CV:**
  - **Versión de CV evaluada:**
  - **Decisión de veredicto:** `corregir_antes_de_revisar` | `revisar_antes_de_aprobar` | `lista_para_aprobacion_humana`
  ```

  Añadir en «Control antes del envío» una casilla que obligue a comprobar el veredicto y sus incidencias de integridad.

- [ ] **Paso 5: Verificar la integración.**

  Ejecutar:

  ```powershell
  rg -n "TEMPLATE_VEREDICTO_FINAL_CV|integridad|corregir_antes_de_revisar|veredicto final" docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md boveda-entrevista-profesional/busqueda-empleo/templates/TEMPLATE_CANDIDATURA.md
  ```

  Esperado: coincidencias en ambos archivos y una secuencia donde el veredicto precede al estado final de candidatura.

### Tarea 3: Aplicar el veredicto a CAND-2026-004 como prueba de aceptación

**Archivos:**

- Crear: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-004-globaenergy-auxiliar-administrativo-back-office/veredicto-final-cv.md`
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-004-globaenergy-auxiliar-administrativo-back-office/candidatura.md`
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/seguimiento-candidaturas.md`

**Consume:** el CV, análisis de oferta y guion de CAND-2026-004; la autorización de datos en `datos-privados-candidatura.md`.

**Produce:** una instancia real y verificable del veredicto, con recomendaciones centradas en mejorar la redacción de la experiencia sin añadir hechos.

- [ ] **Paso 1: Registrar integridad `apta`.**

  Documentar que el CV no contiene experiencia municipal ni actividad independiente, utiliza solo los datos privados autorizados, mantiene la FP como no finalizada y no afirma experiencia directa en energía, CRM ni atención telefónica específica.

- [ ] **Paso 2: Puntuar las cinco reglas con evidencia y límites factuales.**

  Registrar estas notas iniciales para la versión actual del CV:

  | Criterio | Nota | Motivo mínimo |
  | --- | --- | --- |
  | Primer escaneo y posicionamiento | 4 | Titular específico y perfil administrativo claros. |
  | Encaje competitivo | 3 | El enfoque es pertinente, pero la experiencia puede relacionarse más directamente con back office, expedientes y seguimiento. |
  | Cobertura ATS respaldada | 4 | Incluye back office, documentación, expedientes, Excel y bases de datos; omite CRM y energía por falta de evidencia. |
  | Fuerza de la experiencia | 3 | Las contribuciones son creíbles, pero algunos puntos siguen siendo amplios y pueden concretar mejor contexto y resultado. |
  | Adecuación narrativa | 4 | El tono reduce la lectura directiva sin falsear cargos. |

  Para las dos notas de 3, proponer mejoras concretas sin inventar contratos energéticos, CRM, atención telefónica ni resultados adicionales.

- [ ] **Paso 3: Registrar decisión y opción de investigación contextual.**

  Calcular media `3,6`, establecer `revisar_antes_de_aprobar` y dejar la investigación contextual sin iniciar: indicar que se ofrecerá al usuario antes de cualquier consulta y que todavía no hay URL propuestas ni autorización para investigarlas.

- [ ] **Paso 4: Corregir la ficha de candidatura y el seguimiento.**

  Sustituir en `candidatura.md` la frase «No autorizados todavía para esta candidatura» por el alcance autorizado real. Añadir enlace al veredicto, versión evaluada `cv.docx` y decisión `revisar_antes_de_aprobar`.

  En la observación de CAND-2026-004 de [[seguimiento-candidaturas]], añadir «veredicto final: revisar antes de aprobar; media 3,6; integridad apta» sin cambiar el estado formal `pendiente_de_aprobacion`.

- [ ] **Paso 5: Verificar la instancia contra las reglas.**

  Ejecutar:

  ```powershell
  rg -n "Integridad.*apta|Primer escaneo.*4|Encaje competitivo.*3|Cobertura ATS.*4|Fuerza de la experiencia.*3|Adecuación narrativa.*4|3,6|revisar_antes_de_aprobar|CRM|energía" boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-004-globaenergy-auxiliar-administrativo-back-office/veredicto-final-cv.md
  ```

  Esperado: las cinco notas, la media, la decisión, la integridad y los límites de CRM/energía aparecen explícitamente.

### Tarea 4: Actualizar la continuidad de Job-up y comprobar la implantación completa

**Archivos:**

- Modificar: `.pcs/sesiones/sesion-20260722-1131-job-up.md`
- Modificar: `.pcs/estado/estado-actual.md`

**Consume:** los artefactos y la prueba de aceptación de las tareas 1 a 3.

**Produce:** memoria operativa que identifica el veredicto como control de calidad de Job-up y registra CAND-2026-004 como primera aplicación.

- [ ] **Paso 1: Registrar el cambio en la sesión Job-up.**

  Añadir un bloque que relacione los cinco criterios, la puerta de integridad, la investigación contextual opcional con URL y autorización, y el resultado de CAND-2026-004.

- [ ] **Paso 2: Actualizar el estado vivo.**

  Incluir en la rama Job-up que el flujo ya posee un veredicto final con integridad, calidad 1–5 y decisión. Mantener que la aprobación humana y el envío siguen separados.

- [ ] **Paso 3: Ejecutar comprobación de completitud.**

  Ejecutar:

  ```powershell
  rg -n "TEMPLATE_VEREDICTO_FINAL_CV|veredicto-final-cv|revisar_antes_de_aprobar|investigación contextual" boveda-entrevista-profesional/busqueda-empleo docs/metodologia/playbooks .pcs
  git diff --check
  ```

  Esperado: plantilla, playbook, instancia de CAND-2026-004 y trazabilidad PCS localizados; `git diff --check` sin salida.

- [ ] **Paso 4: Revisión de aceptación.**

  Confirmar manualmente que los seis criterios de aceptación de la spec se pueden asociar a: plantilla, playbook, regla de decisión, instancia de CAND-2026-004, sección de investigación opcional y estado PCS actualizado.
