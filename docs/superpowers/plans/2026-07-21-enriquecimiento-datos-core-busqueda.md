# Enriquecimiento de Datos Core para Búsqueda de Empleo — Plan de implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Actualizar la matriz factual de búsqueda de empleo para permitir CV específicos por oferta y por perfil profesional.

**Architecture:** Una sola nota de Obsidian conservará los hechos, las evidencias y las condiciones de búsqueda. Los tres perfiles de CV seleccionarán contenido de esa base común, distinguiendo competencias actuales, experiencia histórica y afirmaciones pendientes de contraste.

**Tech Stack:** Markdown, YAML frontmatter y enlaces wiki de Obsidian.

## Global Constraints

- No afirmar titulaciones, nivel profesional de inglés, tecnologías vigentes, cifras o responsabilidades que no estén confirmadas.
- Mantener los tres perfiles disponibles sin prioridad fija.
- No crear CV finales sin una oferta concreta.
- Preservar ortografía española, trazabilidad factual y privacidad.

---

### Task 1: Estructurar la base factual de búsqueda

**Files:**
- Modify: `boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda.md`

**Interfaces:**
- Consumes: la entrevista de esta conversación, `trayectoria_profesional_gustavo_vega_bolanos.md`, `formacion_gustavo_vega_bolanos.md` y `TRANSCRIPCION_ENT-001-M01_2026-07-20.md`.
- Produces: secciones «Posicionamiento», «Perfiles objetivo», «Banco de logros», «Trayectoria», «Competencias y herramientas», «Formación» y «Reglas de adaptación».

- [ ] **Step 1: Reemplazar la estructura inicial por secciones de datos reutilizables.**

  Incluir el posicionamiento: presencial en Gran Canaria, modalidad dependiente del puesto, referencia de 20.000 € brutos anuales a jornada completa y valoración de media jornada según condiciones. Declarar español nativo e inglés básico oral con lectura técnica funcional con apoyo de herramientas.

- [ ] **Step 2: Registrar los tres perfiles sin jerarquía fija.**

  Mantener los perfiles RR. HH. y operaciones, IT y sistemas, y administración, logística y gestión pública. Para cada uno, enumerar competencias y logros de la misma base que se puedan priorizar en una oferta concreta.

- [ ] **Step 3: Crear el banco de logros verificables.**

  Incorporar, como mínimo: automatización de contratación y onboarding en Herfrailes; planificación de vacaciones, permisos, nóminas y jornada; algoritmo de pedidos con reducción del 30 % de caducidades y del 80 % de productos sin venta superior a un mes; algoritmo de adjudicación de plazas docentes; gestión de vivienda pública; sistema de Granintra; automatización fiscal y recaudatoria en Gáldar; y sistemas empresariales iniciales. Distinguir las responsabilidades colegiadas de las individuales.

- [ ] **Step 4: Corregir y completar la trayectoria.**

  Reflejar que Herfrailes tuvo cargo formal de Director Ejecutivo y responsabilidades simultáneas de RR. HH., IT, operaciones, logística y parte de administración. Situar el cierre operativo en octubre de 2024 y marcar como pendiente de conciliación la fecha de enero de 2025 procedente de LinkedIn. Atribuir el algoritmo docente a General de Software de Canarias y el programa de vivienda pública a INERZA.

- [ ] **Step 5: Separar competencias actuales, históricas y transferibles.**

  Registrar como uso actual medio-alto: Notion, ChatGPT, Codex, Work, Ollama, Obsidian, Trello, Office 365, SQL Server, Microsoft Visual Studio, Windows 11, VB.NET y Windows Server. Registrar Linux como básico. Mantener lenguajes, entornos y plataformas anteriores como experiencia histórica, salvo confirmación posterior de vigencia.

- [ ] **Step 6: Corregir la formación.**

  Indicar estudios universitarios no finalizados y no incluir titulación de FP. Incluir el Máster en Inteligencia Artificial con Titulación Universitaria de BIG school, con certificado de la Universidad Isabel I, como formación en curso. Seleccionar cursos complementarios por relevancia y explicar el aprendizaje autodidacta sin convertirlo en credencial.

- [ ] **Step 7: Añadir el protocolo de adaptación por oferta.**

  Establecer que cada CV elegirá un perfil principal, un perfil secundario y de tres a cinco logros del banco. Añadir una lista de comprobación que prohíba inventar métricas, títulos, nivel de idioma, tecnologías actuales o responsabilidades.

### Task 2: Validar contenido, enlaces y precisión

**Files:**
- Modify: `boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda.md`

**Interfaces:**
- Consumes: la nota actualizada de datos core.
- Produces: una matriz coherente y lista para seleccionar información ante una oferta.

- [ ] **Step 1: Revisar las fechas y atribuciones corregidas.**

  Confirmar que la adjudicación de profesorado consta en General de Software de Canarias y que INERZA queda limitada al programa de vivienda pública. Confirmar que octubre de 2024 aparece como cierre operativo de Herfrailes y que enero de 2025 queda marcado para contraste.

- [ ] **Step 2: Revisar ortografía y afirmaciones de nivel.**

  Corregir tildes, errores tipográficos y términos como «LOPDGDD». Eliminar cualquier afirmación que convierta estudios no finalizados, curso en curso, experiencia histórica o inglés básico en una cualificación superior.

- [ ] **Step 3: Comprobar integridad de enlaces y formato Markdown.**

  Ejecutar `rg -n '`[^`]+`|/[^/]+\.md|\[\[\[' boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda.md` y revisar manualmente cualquier coincidencia. Ejecutar `git diff --check` y revisar el diff final del archivo.

- [ ] **Step 4: Confirmar que la nota permite los tres CV.**

  Verificar que cada perfil tiene al menos tres logros seleccionables y que el protocolo de adaptación exige adaptar el contenido a cada oferta antes de redactar un CV.
