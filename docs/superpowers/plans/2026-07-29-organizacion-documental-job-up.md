# Organización documental de Job-up — Plan de implantación

> **Para agentes:** SUBSKILL REQUERIDA: usar `superpowers:subagent-driven-development` (recomendado) o `superpowers:executing-plans` para ejecutar este plan tarea por tarea. Los pasos usan casillas (`- [ ]`) para su seguimiento.

**Objetivo:** Reorganizar Job-up como rama operativa documentada, versionar su playbook, fuentes y plantillas, sustituir la entrada documental duplicada y adaptar sus tres skills sin realizar acciones externas.

**Arquitectura:** `boveda-entrevista-profesional/busqueda-empleo/README.md` será la referencia funcional única, con las capas estables «Modelo mental de Job-up» y «Uso operativo de Job-up». Las fuentes, plantillas y seguimiento se trasladarán a áreas funcionales; el playbook seguirá en `docs/` con una versión vigente de nombre estable y una copia histórica recuperada desde Git. Las skills vivirán en `.codex/skills/`, consumirán las rutas nuevas y aplicarán una compuerta explícita de uso de datos privados.

**Tecnologías:** Markdown con frontmatter YAML, wikilinks de Obsidian, Git, PowerShell y configuración YAML de skills de Codex.

## Restricciones globales

- Mantener ortografía española y revisar explícitamente los documentos redactados o modificados.
- No modificar `docs/DOCUMENTO_SPEC_CARRERA_AI.md`, decisiones PCS, `hosts.yaml` ni el Core de PCS.
- No enviar candidaturas, usar navegadores, conectores o contactos externos.
- No crear un histórico local: solo usar `historico/` y conservar la ruta de procedencia.
- No leer ni usar `.tmp/`.
- Las fuentes y plantillas tendrán versión y estado documental en YAML; las candidaturas y los documentos de sus expedientes no tendrán versionado trazable.
- Los datos privados solo se consultan, copian o incorporan cuando exista autorización aplicable a la candidatura. Puede reutilizarse una autorización escrita en su ficha privada solo para ese mismo expediente.
- Los datos privados no autorizados no se copian ni se propagan; se bloquea únicamente la parte del flujo que los necesita.
- Mantener `allow_implicit_invocation: false` en las tres skills. La activación semántica queda fuera de alcance y se retoma en [[sesion-20260729-1534-activacion-semantica-skills-job-up]].
- `job-up-candidatura-oferta` no crea sesiones PCS; cuando no haya una abierta, solo podrá invocar `job-up-inicia-sesion` después de que la persona usuaria lo confirme explícitamente.
- La investigación de empresas y las relaciones profesionales quedan fuera de esta implantación y se retoman exclusivamente en [[sesion-20260729-1614-investigacion-empresas-relaciones-profesionales]].
- Las sesiones PCS son registros históricos; no reescribir su contenido salvo la nota de trazabilidad ya existente.
- No empezar tareas en worktrees hasta resolver el punto de integración inicial de la Tarea 1.

---

## Cambios incorporados desde el debate de revisión

- Se sustituye la autorización genérica de datos privados por una compuerta de uso aplicable a cada candidatura y reutilizable solo desde su ficha privada.
- El control de versión se extiende a fuentes y plantillas; se excluyen expresamente las candidaturas.
- El README tendrá desde el inicio dos capas con títulos estables para permitir una futura extracción de la arquitectura conceptual.
- La skill de oferta pedirá elegir sesión ante ambigüedad y, si no hay ninguna abierta, solicitará permiso para invocar al launcher de Job-up.
- Investigación y networking no se añaden a la matriz ni al alcance; permanecen como línea PCS pausada.

---

## Mapa de archivos y responsables

| Entrega | Worktree sugerido | Archivos principales | Dependencias |
| --- | --- | --- | --- |
| Preintegración | coordinador | árbol de trabajo y rama base | ninguna |
| Playbook versionado | `codex/job-up-playbook-versioning` | `docs/metodologia/playbooks/`, `historico/docs/metodologia/playbooks/` | preintegración |
| Estructura, versiones y README | `codex/job-up-documentation` | `boveda-entrevista-profesional/busqueda-empleo/`, `historico/boveda-entrevista-profesional/busqueda-empleo/` | preintegración |
| Skills renombradas | `codex/job-up-skills-existing` | `.codex/skills/job-up-inicia-sesion/`, `.codex/skills/job-up-genera-cv-empresa/` | estructura y README integrados |
| Skill de oferta | `codex/job-up-skill-offer` | `.codex/skills/job-up-candidatura-oferta/` | estructura, README y playbook integrados |
| Integración y validación | `codex/job-up-integration` | enlaces y referencias afectadas | todas las entregas anteriores |

Las entregas de playbook y estructura pueden ejecutarse en paralelo desde la misma rama base limpia. Las de skills se ejecutarán después de integrar la estructura; la nueva skill también requiere que el nombre estable del playbook ya esté integrado.

### Tarea 1: Fijar una base segura de integración

**Archivos:**

- Revisar: los archivos modificados que muestre `git status --short`.
- Crear: una rama base de integración, solo después de preservar los cambios locales autorizados.

**Consume:** la especificación aprobada `docs/superpowers/specs/2026-07-29-organizacion-documental-job-up-design.md`.

**Produce:** una referencia Git limpia y conocida desde la que crear todos los worktrees; un inventario de cambios locales que no se deben sobrescribir.

- [x] **Paso 1: Inventariar los cambios locales antes de crear worktrees.**

  Ejecutar:

  ```powershell
  git status --short
  git diff -- boveda-entrevista-profesional/busqueda-empleo docs/superpowers/specs .pcs/sesiones
  ```

  Clasificar cada cambio como «parte de esta implantación», «ajeno» o «pendiente de decisión». En particular, revisar los cambios actuales en `README.md`, `INICIO_SESION_WORK.md`, `seguimiento-candidaturas.md` y `TEMPLATE_ANALISIS_OFERTA.md` antes de tocar esas rutas.

- [x] **Paso 2: Resolver la base con la persona responsable.**

  Si todos los cambios pertenecen a la implantación, crear un commit de preparación limitado a esos cambios. Si alguno es ajeno o incompleto, no usarlo como base de los worktrees: conservarlo en el árbol principal y crear los worktrees desde el último commit común. No iniciar ningún movimiento sobre un archivo clasificado como «pendiente de decisión».


- [x] **Paso 3: Confirmar que la especificación es el contrato vigente antes de usarla.**

  Comprobar que el flujo de `job-up-candidatura-oferta` termina en los pasos
  `9.`, `10.` y `11.`, que recoge la reutilización limitada de autorizaciones
  privadas y que no incorpora investigación ni networking al alcance. Si falta
  cualquiera de esos requisitos, no crear worktrees y pedir revisión humana.

- [x] **Paso 4: Crear la rama y los worktrees independientes desde la misma referencia.**

  Crear desde la base limpia los worktrees de las Tareas 2 y 3, que pueden
  ejecutarse en paralelo. Crear los worktrees de las Tareas 4 y 5 solo después
  de integrar sus dependencias: la Tarea 4 parte de la estructura de la Tarea
  3 y la Tarea 5 parte de las Tareas 2 y 3. Antes de empezar, comprobar en cada
  worktree independiente:

  ```powershell
  git rev-parse HEAD
  git status --short
  ```

  Resultado esperado: el mismo SHA base y un árbol limpio en cada worktree.

- [x] **Paso 5: Confirmar la preparación.**

  Registrar el SHA base y la clasificación de los cambios locales en el comentario de coordinación de la tarea. No crear decisiones PCS ni modificar el estado PCS.

### Tarea 2: Versionar el playbook de candidatura por oferta

**Worktree:** `codex/job-up-playbook-versioning`.

**Archivos:**

- Crear: `historico/docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md`.
- Crear: `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md`.
- Eliminar tras verificar la migración: `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md`.
- Revisar: `docs/VERSIONADO_CARRERA_AI.md`, `docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md` y las referencias al nombre anterior.

**Consume:** el contenido exacto del commit `071f9d846e30ce4526c00713b9cf418e48e55ed6` y el contenido actual del playbook.

**Produce:** playbook vigente `1.1.0` con nombre estable y copia histórica fiel `1.0.0`.

- [x] **Paso 1: Recuperar la versión histórica sin mezclar mejoras posteriores.**

  Obtener el archivo original desde Git con:

  ```powershell
  git show 071f9d846e30ce4526c00713b9cf418e48e55ed6:docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md
  ```

  Crear `historico/docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md` con ese contenido y anteponer este frontmatter YAML:

  ```yaml
  ---
  id: playbook-candidatura-por-oferta
  tipo: playbook
  version: "1.0.0"
  estado: retirada
  fecha_version: 2026-07-21
  fecha_retiro: 2026-07-29
  sustituida_por: "1.1.0"
  ---
  ```

- [x] **Paso 2: Crear el playbook vigente con nombre estable.**

  Copiar el contenido actual a `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md` y anteponer:

  ```yaml
  ---
  id: playbook-candidatura-por-oferta
  tipo: playbook
  version: "1.1.0"
  estado: vigente
  fecha_version: 2026-07-29
  version_anterior: "1.0.0"
  sustituye: PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0
  ---
  ```

  Ajustar el título visible para no presentar `v1.0.0` como versión vigente. No cambiar las reglas metodológicas del cuerpo.

- [x] **Paso 3: Retirar el archivo vigente con versión en el nombre.**

  Eliminar `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md` solo después de que existan las dos copias nuevas y se hayan comprobado sus YAML.

- [x] **Paso 4: Comprobar exactitud e integridad.**

  Ejecutar:

  ```powershell
  $rutaHistorica = 'historico/docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md'
  $contenidoHistorico = [System.IO.File]::ReadAllText((Resolve-Path $rutaHistorica))
  $cuerpoHistorico = [regex]::Replace($contenidoHistorico, '(?s)\A---\r?\n.*?\r?\n---\r?\n', '')
  $cuerpoEsperado = (git show 071f9d846e30ce4526c00713b9cf418e48e55ed6:docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md) -join "`n"
  if ($cuerpoHistorico.Replace("`r`n", "`n") -ne $cuerpoEsperado.Replace("`r`n", "`n")) { throw 'El cuerpo histórico no coincide con el commit de creación.' }
  ```

  Resultado esperado: el comando termina sin excepción. Verificar además que ambos YAML contienen `version`, `estado` y la relación de sustitución correcta.

- [x] **Paso 5: Revisar y comprometer.**

  Revisar ortografía española, `git diff --check` y el inventario de referencias al nombre antiguo. Crear un commit aislado:

  ```powershell
  git add docs/metodologia/playbooks historico/docs/metodologia/playbooks
  git commit -m "docs: versionar playbook de candidatura por oferta"
  ```

### Tarea 3: Migrar la estructura operativa y escribir el README canónico

**Worktree:** `codex/job-up-documentation`.

**Archivos:**

- Crear: `boveda-entrevista-profesional/busqueda-empleo/fuentes/`.
- Crear: `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/`.
- Crear: `boveda-entrevista-profesional/busqueda-empleo/seguimiento/`.
- Crear: `historico/boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md`.
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/README.md`.
- Mover: `datos-core-busqueda.md`, `datos-privados-candidatura.md`, `templates/`, `seguimiento-candidaturas.md` y `INICIO_SESION_WORK.md`.
- Modificar tras el movimiento: el frontmatter de las dos fuentes y de las cuatro plantillas para establecer su control de versión documental.
- Revisar y modificar si contienen rutas relativas: documentos en `candidaturas/`, `presentacion-espontanea/`, plantillas y README de candidaturas.

**Consume:** la arquitectura, matriz de artefactos y reglas de trazabilidad de la especificación.

**Produce:** estructura funcional coherente, README único de Job-up, fuentes y plantillas con versión documental, y documento de inicio conservado solo como histórico.

- [x] **Paso 1: Mover los artefactos sin alterar su contenido sustantivo.**

  Aplicar este mapa exacto:

  ```text
  datos-core-busqueda.md              -> fuentes/datos-core-busqueda.md
  datos-privados-candidatura.md       -> fuentes/datos-privados-candidatura.md
  templates/*                         -> proceso/plantillas/*
  seguimiento-candidaturas.md         -> seguimiento/seguimiento-candidaturas.md
  INICIO_SESION_WORK.md               -> historico/boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md
  ```

  Preservar historial con `git mv` cuando el origen y destino estén versionados. No mover `candidaturas/`, `presentacion-espontanea/`, certificados ni archivos de CV.

- [x] **Paso 2: Marcar la pieza histórica correctamente.**

  En la copia histórica de `INICIO_SESION_WORK.md`, añadir un frontmatter YAML que indique que está retirada y que fue sustituida por el README y `job-up-inicia-sesion`. Mantener íntegro el contenido histórico; no convertirlo en una guía activa.

- [x] **Paso 3: Establecer el control de versión de fuentes y plantillas.**

  Añadir o completar el frontmatter YAML de estos seis documentos trasladados:

  ```text
  fuentes/datos-core-busqueda.md
  fuentes/datos-privados-candidatura.md
  proceso/plantillas/TEMPLATE_ANALISIS_OFERTA.md
  proceso/plantillas/TEMPLATE_CANDIDATURA.md
  proceso/plantillas/TEMPLATE_GUION_ADAPTACION_CV.md
  proceso/plantillas/TEMPLATE_VEREDICTO_FINAL_CV.md
  ```

  Cada documento debe conservar su `id`, `tipo` y estado funcional existente,
  y añadir `version: "1.0.0"` y `fecha_version: 2026-07-29`. Las plantillas
  que aún no tengan identificador usarán, respectivamente,
  `template-analisis-oferta`, `template-candidatura`,
  `template-guion-adaptacion-cv` y `template-veredicto-final-cv`, con
  `estado: vigente`. No añadir campos de versión a ninguna carpeta ni archivo
  dentro de `candidaturas/`. Conservar las autorizaciones ya delimitadas por
  candidatura dentro de `fuentes/datos-privados-candidatura.md`; no copiar sus
  valores a los expedientes ni convertirlas en autorizaciones globales.

- [x] **Paso 4: Reescribir el README como referencia funcional única.**

  Estructurarlo con dos secciones principales y este contenido mínimo:

  ```text
  1. Modelo mental de Job-up
     - definición, misión, alcance y exclusiones
     - límites de evidencia factual, privacidad y aprobación humana
     - arquitectura de la rama
  2. Uso operativo de Job-up
     - cómo empezar y qué skill corresponde a cada entrada
     - mapa de carpetas y enlaces canónicos
     - flujo desde entrada de oferta hasta pendiente de aprobación
     - matriz de artefactos para oferta y presentación espontánea
     - trazabilidad, histórico y enlaces a PCS y playbook
  ```

  Usar como títulos reales «Modelo mental de Job-up» y «Uso operativo de
  Job-up». Incluir explícitamente las tres modalidades de entrada de una
  oferta: URL accesible, fichero Markdown de estructura libre o texto pegado.
  Indicar la compuerta de datos privados: autorización específica, reutilizable
  solo desde la ficha privada de la misma candidatura, sin copiar ni propagar
  datos no autorizados. Explicar que, si no existe sesión abierta, la skill de
  oferta pedirá permiso antes de invocar `job-up-inicia-sesion`.

- [x] **Paso 5: Actualizar todas las rutas afectadas.**

  Localizar referencias mediante:

  ```powershell
  rg -n "datos-core-busqueda|datos-privados-candidatura|seguimiento-candidaturas|TEMPLATE_|INICIO_SESION_WORK" boveda-entrevista-profesional .codex docs
  ```

  Corregir rutas Markdown relativas para que apunten a `fuentes/`, `proceso/plantillas/` y `seguimiento/`. Los wikilinks simples pueden mantener el nombre visible cuando sigan resolviendo de forma unívoca; convertirlos a ruta relativa solo si hay ambigüedad.

- [x] **Paso 6: Verificar la documentación trasladada y sus metadatos.**

  Comprobar que no existen los cuatro orígenes operativos antiguos y que existen los cinco destinos previstos:

  ```powershell
  Test-Path boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda.md
  Test-Path boveda-entrevista-profesional/busqueda-empleo/fuentes/datos-core-busqueda.md
  Test-Path boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_ANALISIS_OFERTA.md
  Test-Path boveda-entrevista-profesional/busqueda-empleo/seguimiento/seguimiento-candidaturas.md
  Test-Path historico/boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md
  ```

  Resultado esperado: el primer comando devuelve `False`; los cuatro restantes, `True`.

  Comprobar además que las seis fuentes y plantillas indicadas contienen
  `id`, `tipo`, `version: "1.0.0"` y `fecha_version: 2026-07-29`, y que no hay
  coincidencias de `version:` dentro de `candidaturas/`.

- [x] **Paso 7: Revisar y comprometer.**

  Revisar ortografía, ejecutar `git diff --check` y crear un commit aislado:

  ```powershell
  git add boveda-entrevista-profesional/busqueda-empleo historico/boveda-entrevista-profesional/busqueda-empleo
  git commit -m "docs: reorganizar documentación operativa de Job-up"
  ```

### Tarea 4: Renombrar y adaptar las skills existentes

**Worktree:** `codex/job-up-skills-existing`, creado desde la rama que ya contenga la Tarea 3.

**Archivos:**

- Crear mediante `git mv`: `.codex/skills/job-up-inicia-sesion/SKILL.md` y `agents/openai.yaml`.
- Crear mediante `git mv`: `.codex/skills/job-up-genera-cv-empresa/SKILL.md` y `agents/openai.yaml`.
- Eliminar tras verificar: los directorios `.codex/skills/empleo-inicio-busqueda/` y `.codex/skills/empleo-genera-cv-empresa/`.
- Modificar: `.codex/skills/README.md` si enumera o describe las skills.

**Consume:** las rutas de la Tarea 3 y las reglas de sesión ya presentes en `empleo-inicio-busqueda`.

**Produce:** dos skills de Job-up con nombres, metadatos y rutas coherentes.

- [x] **Paso 1: Renombrar sin perder archivos de configuración.**

  Usar `git mv` para que cada `SKILL.md` conserve su archivo `agents/openai.yaml` asociado. No dejar directorios duplicados con los nombres antiguos.

- [x] **Paso 2: Adaptar `job-up-inicia-sesion`.**

  Cambiar el frontmatter `name` y la descripción para referirse a `job-up-inicia-sesion`. Sustituir la lectura de `INICIO_SESION_WORK.md` por la del README canónico y sus rutas nuevas: seguimiento en `seguimiento/` y fuentes en `fuentes/`. Mantener la secuencia PCS actual: validar, cerrar sesiones Job-up previas cuando corresponda, crear una sesión nueva y actualizar únicamente la traza Job-up del estado.

- [x] **Paso 3: Adaptar `job-up-genera-cv-empresa`.**

  Cambiar el frontmatter `name`, el título y las rutas de `datos-core-busqueda.md` y los materiales de presentación espontánea. Mantener sus límites: investigación pública verificable, datos privados restringidos, ninguna comunicación externa y resultado pendiente de aprobación humana. Antes de usar datos privados, exigir una autorización aplicable a esa candidatura; aceptar una autorización escrita en la ficha privada solo cuando identifica el mismo expediente. No copiar ni propagar datos no autorizados y continuar únicamente las partes que no los requieran.

- [x] **Paso 4: Actualizar los metadatos de las dos skills.**

  En ambos `agents/openai.yaml`, establecer nombres visibles y descripciones consistentes con Job-up, actualizar `default_prompt` para usar el nombre nuevo y conservar:

  ```yaml
  policy:
    allow_implicit_invocation: false
  ```

- [x] **Paso 5: Ejecutar pruebas documentales de regresión.**

  Ejecutar:

  ```powershell
  rg -n "empleo-inicio-busqueda|empleo-genera-cv-empresa|INICIO_SESION_WORK.md|busqueda-empleo/datos-core-busqueda.md" .codex/skills
  ```

  Resultado esperado: ninguna coincidencia operativa; solo se admitirán menciones históricas justificadas fuera de `.codex/skills`.

- [x] **Paso 6: Revisar y comprometer.**

  Revisar ortografía, `git diff --check` y crear:

  ```powershell
  git add .codex/skills
  git commit -m "feat: adaptar skills de entrada de Job-up"
  ```

### Tarea 5: Crear la skill de candidatura por oferta

**Worktree:** `codex/job-up-skill-offer`, creado desde la rama que ya integre las Tareas 2 y 3.

**Archivos:**

- Crear: `.codex/skills/job-up-candidatura-oferta/SKILL.md`.
- Crear: `.codex/skills/job-up-candidatura-oferta/agents/openai.yaml`.
- Modificar: `.codex/skills/README.md` si actúa como índice de skills.

**Consume:** `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md`, la matriz del README de Job-up y las rutas creadas en la Tarea 3.

**Produce:** una skill explícita que inicia el flujo de candidatura por oferta desde URL, Markdown o texto, sin abrir sesiones por sí misma.

- [x] **Paso 1: Escribir una prueba de comportamiento en Markdown.**

  Crear `docs/superpowers/tests/2026-07-29-job-up-candidatura-oferta.md` con esta tabla de casos y resultado esperado:

  | Entrada | Estado de sesión | Resultado esperado |
  | --- | --- | --- |
  | URL accesible | una sesión Job-up abierta | extraer contenido, registrar URL y continuar el flujo |
  | URL inaccesible + Markdown | una sesión Job-up abierta | usar Markdown, registrar contenido aportado y continuar |
  | Texto pegado | una sesión Job-up abierta | extraer datos disponibles y pedir solo faltantes esenciales |
  | Cualquiera | ninguna sesión Job-up abierta | informar y preguntar si desea ejecutar `job-up-inicia-sesion`; sin respuesta afirmativa, detenerse |
  | Cualquiera | ninguna sesión + respuesta afirmativa | invocar `job-up-inicia-sesion`, comprobar una única sesión creada y continuar |
  | Cualquiera | varias sesiones Job-up abiertas | pedir que la persona usuaria seleccione una sesión; no elegir por inferencia |
  | Cualquiera | una sesión Job-up abierta + autorización privada aplicable | usar solo los datos autorizados para ese expediente |
  | Cualquiera | una sesión Job-up abierta + autorización ausente o ambigua | no copiar ni propagar datos privados; bloquear solo los documentos que los requieran |

- [x] **Paso 2: Redactar la skill con el contrato de entrada.**

  Usar este frontmatter mínimo:

  ```yaml
  ---
  name: job-up-candidatura-oferta
  description: Use when the user explicitly provides a job offer by accessible URL, Markdown file, or pasted text and wants to prepare a traceable Job-up application.
  ---
  ```

  Definir las tres modalidades y exigir contenido suficiente de la oferta; no imponer plantilla a Markdown ni texto.

- [x] **Paso 3: Implementar el flujo y las detenciones obligatorias.**

  Documentar, en este orden: identificar procedencia; extraer contenido disponible; registrar URL o material aportado y fecha; pedir solo datos esenciales ausentes; resolver una única sesión abierta; pedir selección humana si existen varias; si no existe ninguna, solicitar permiso para invocar `job-up-inicia-sesion` y comprobar la sesión creada; crear el análisis dentro del expediente; aplicar el playbook vigente y la matriz del README; comprobar la autorización privada aplicable; producir el paquete en `pendiente_de_aprobacion`; actualizar ficha y seguimiento. Declarar la detención obligatoria cuando no haya confirmación para invocar el launcher, la selección de sesión siga ambigua, falten datos esenciales imposibles de obtener o exista contradicción factual.

- [x] **Paso 4: Añadir límites explícitos.**

  Incluir que la skill no abre ni cierra directamente sesiones PCS, no usa el contenido de una URL inaccesible si no se facilita por Markdown o texto, no inventa datos, no envía candidaturas ni realiza contactos. La entrega de una oferta no es autorización para crear sesión ni usar datos privados. Una respuesta afirmativa explícita a la propuesta de ejecutar `job-up-inicia-sesion` autoriza únicamente esa invocación delegada; no autoriza datos privados ni acciones externas.

- [x] **Paso 5: Crear la configuración de descubrimiento.**

  Crear `agents/openai.yaml` con un nombre visible, descripción breve y prompt por defecto que invoquen `job-up-candidatura-oferta`, y con:

  ```yaml
  policy:
    allow_implicit_invocation: false
  ```

- [x] **Paso 6: Verificar contra los seis casos.**

  Revisar línea por línea la skill contra la tabla de la prueba; cada resultado debe tener una instrucción inequívoca en el documento. Ejecutar `git diff --check` y buscar la ruta del playbook antiguo:

  ```powershell
  rg -n "PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0|INICIO_SESION_WORK" .codex/skills/job-up-candidatura-oferta
  ```

  Resultado esperado: cero coincidencias.

- [x] **Paso 7: Revisar y comprometer.**

  Revisar ortografía española y crear:

  ```powershell
  git add .codex/skills/job-up-candidatura-oferta docs/superpowers/tests/2026-07-29-job-up-candidatura-oferta.md
  git commit -m "feat: añadir skill de candidatura por oferta"
  ```

### Tarea 6: Integrar las entregas y validar el sistema completo

**Worktree:** `codex/job-up-integration`.

**Archivos:**

- Modificar: referencias afectadas por los movimientos en todo el repositorio.
- Revisar: README, playbook, histórico, las tres skills, plantillas, seguimiento y expedientes de candidatura.
- No modificar: decisiones PCS, Core PCS, SPEC de Carrera AI ni archivos binarios de candidaturas.

**Consume:** los commits de las Tareas 2 a 5.

**Produce:** rama de integración con enlaces válidos, rutas coherentes y verificación documentada.

- [x] **Paso 1: Integrar en el orden de dependencias.**

  Aplicar los commits en este orden: Tarea 2, Tarea 3, Tarea 4 y Tarea 5. Resolver un conflicto solo comparando el cambio con la especificación aprobada; si afecta a un archivo clasificado como «pendiente de decisión» en la Tarea 1, detenerse y pedir intervención humana.

- [x] **Paso 2: Sustituir referencias al playbook y a rutas antiguas.**

  Ejecutar:

  ```powershell
  rg -n "PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0|empleo-inicio-busqueda|empleo-genera-cv-empresa|INICIO_SESION_WORK.md|busqueda-empleo/(datos-core-busqueda|datos-privados-candidatura|seguimiento-candidaturas|templates/)" --glob '!historico/**' --glob '!.pcs/**' --glob '!.superpowers/**' --glob '!docs/superpowers/specs/**' --glob '!docs/superpowers/plans/**' --glob '!docs/ideas-y-debates/**' .
  ```

  Actualizar cada coincidencia operativa para usar el playbook sin versión en el nombre, los nombres nuevos de skills o la ruta funcional nueva. Mantener las referencias históricas en `.pcs/`, `.superpowers/`, `historico/` y documentos de diseño, así como `sustituye: PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0` en el YAML del playbook vigente.

- [x] **Paso 3: Comprobar los enlaces Markdown locales modificados.**

  Para cada enlace Markdown relativo que haya cambiado, resolver la ruta desde el directorio del archivo que lo contiene y comprobar que el destino existe. Para cada wikilink modificado, comprobar que solo exista un archivo activo con ese nombre. Corregir los enlaces rotos sin cambiar el contenido factual de candidaturas existentes.

- [x] **Paso 4: Verificar contratos de las skills.**

  Ejecutar:

  ```powershell
  rg -n "^name: job-up-|allow_implicit_invocation: false|INICIO_SESION_WORK" .codex/skills/job-up-*/SKILL.md .codex/skills/job-up-*/agents/openai.yaml
  ```

  Resultado esperado: tres nombres `job-up-*`, tres políticas explícitas en `false` y cero referencias activas al documento histórico de inicio. Revisar además que las dos skills que pueden consultar datos privados exigen autorización aplicable a la candidatura y que la skill de oferta no elige sesiones ambiguas ni crea directamente una sesión PCS.

- [x] **Paso 5: Ejecutar la comprobación final de estructura y contenido.**

  Verificar que el README contiene las secciones «Modelo mental», «Uso operativo», «Matriz de artefactos», las tres skills y las tres modalidades de entrada. Confirmar que el playbook vigente declara `1.1.0`, el histórico declara `1.0.0` y que el único archivo vigente del playbook no lleva versión en el nombre.

  Verificar que las seis fuentes y plantillas establecidas en la Tarea 3 tienen
  YAML de versión, que ningún expediente bajo `candidaturas/` contiene ese
  control de versión y que el README excluye expresamente investigación de
  empresas y networking de la primera implantación.

- [x] **Paso 6: Revisar cambios locales y completar el cierre técnico.**

  Repetir `git status --short` y comparar con el inventario de la Tarea 1. Confirmar que ningún cambio ajeno se ha incluido. Ejecutar `git diff --check`, revisar ortografía española de los documentos alterados y crear el commit de integración solo si no quedan conflictos ni enlaces rotos:

  ```powershell
  git add -A
  git commit -m "docs: integrar la organización funcional de Job-up"
  ```

## Auditoría de cobertura de la especificación

| Requisito aprobado | Tarea que lo implementa |
| --- | --- |
| README como referencia única con dos capas | Tarea 3 |
| Estructura `fuentes/`, `proceso/plantillas/`, `seguimiento/` | Tarea 3 |
| Versionado de fuentes y plantillas, sin versionado de candidaturas | Tarea 3 y validación Tarea 6 |
| Histórico global y conservación de `INICIO_SESION_WORK.md` | Tarea 3 |
| Matriz de artefactos, compuerta de privacidad y reutilización limitada de autorización | Tareas 3, 4 y 5; validación Tarea 6 |
| Playbook vigente 1.1.0 y original 1.0.0 histórico | Tarea 2 |
| Renombrado de las dos skills existentes | Tarea 4 |
| Nueva skill de oferta con URL, Markdown y texto | Tarea 5 |
| Selección humana ante sesiones ambiguas y derivación confirmada al launcher cuando no exista sesión abierta | Tarea 5 y validación Tarea 6 |
| Invocación explícita; activación semántica diferida | Tareas 4, 5 y 6 |
| Investigación y networking fuera de alcance y trazados en sesión pausada | Restricciones globales y validación Tarea 6 |
| Enlaces, trazabilidad y preservación de cambios ajenos | Tareas 1 y 6 |

## Criterio de aceptación final

La integración estará lista para revisión humana cuando cada tarea tenga su commit verificable, los enlaces modificados resuelvan, las rutas antiguas no aparezcan en uso operativo, los documentos históricos estén exclusivamente bajo `historico/`, las tres skills usen los nombres y políticas aprobados y no se haya realizado ninguna acción externa ni cambio de gobernanza PCS.
