# Inicio de búsqueda de empleo mediante skill local Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Permitir iniciar una sesión Work de búsqueda de empleo con la invocación explícita `$iniciar-busqueda-empleo`.

**Architecture:** La skill local contiene únicamente el procedimiento reutilizable y sigue la rehidratación PCS sin crear un comando nuevo. El documento de la bóveda contiene el protocolo operativo de esta rama y señala los documentos de trabajo. La skill solo se activa de forma explícita.

**Tech Stack:** Markdown, formato Agent Skills, YAML y PCS 2.0.

## Global Constraints

- Crear la skill únicamente en `.codex/skills/iniciar-busqueda-empleo/`.
- La skill debe activarse solo mediante `$iniciar-busqueda-empleo`.
- No modificar el Core PCS ni la investigación metodológica de entrevista.
- No escribir, enviar candidaturas, usar Chrome ni contactar con terceros durante el inicio.
- Redactar en español y usar wikilinks resolubles para documentos Markdown de la bóveda.
- Mantener el cuerpo de la skill conciso y delegar el detalle operativo en la bóveda.

---

### Task 1: Establecer el caso de prueba basal

**Files:**
- Create: ninguno.

**Interfaces:**
- Consumes: una sesión fresca sin la skill instalada.
- Produces: evidencia de que la invocación literal no inicia por sí sola la rama de búsqueda.

- [ ] **Step 1: Ejecutar el escenario sin skill.**

Pedir a un agente fresco, sin proporcionarle la nueva skill, que responda únicamente a este mensaje:

```text
$iniciar-busqueda-empleo
```

- [ ] **Step 2: Verificar el fallo esperado.**

Registrar como resultado basal que la invocación no puede cargar de forma fiable el estado PCS, el README de búsqueda y el seguimiento de candidaturas sin instrucciones reutilizables. No crear archivos durante esta prueba.

### Task 2: Crear la skill y el punto de entrada operativo

**Files:**
- Create: `.codex/skills/iniciar-busqueda-empleo/SKILL.md`
- Create: `.codex/skills/iniciar-busqueda-empleo/agents/openai.yaml`
- Create: `boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md`

**Interfaces:**
- Consumes: la rehidratación PCS, `README.md` y `seguimiento-candidaturas.md` de la rama de búsqueda.
- Produces: una activación explícita y un protocolo de entrada que termina esperando instrucciones.

- [ ] **Step 1: Inicializar la estructura de skill.**

Ejecutar:

```powershell
python 'C:\Users\gusve\.codex\skills\.system\skill-creator\scripts\init_skill.py' iniciar-busqueda-empleo --path '.codex/skills' --interface display_name='Iniciar búsqueda de empleo' --interface short_description='Abre la rama operativa de empleo' --interface default_prompt='Usa $iniciar-busqueda-empleo para continuar la búsqueda de empleo.'
```

- [ ] **Step 2: Sustituir `SKILL.md` por el procedimiento mínimo.**

```markdown
---
name: iniciar-busqueda-empleo
description: Use when the user explicitly invokes $iniciar-busqueda-empleo in a fresh Work session to start or resume the empleo-search branch of carrera-ai.
---

# Iniciar búsqueda de empleo

## Procedimiento

1. Aplicar el protocolo vigente de `pcs::rehidrata` al host predeterminado, sin crear ni actualizar entidades PCS.
2. Leer `boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md` y seguir su orden de consulta.
3. Responder solo con el ámbito confirmado, el estado breve de candidaturas y acciones relevantes, y el siguiente paso seguro. Esperar instrucciones.

## Límites

- Trabajar solo en la rama operativa de búsqueda de empleo.
- No modificar la investigación de entrevista.
- No realizar escrituras, envíos, navegación en Chrome ni contactos externos por esta invocación.
```

- [ ] **Step 3: Configurar activación explícita.**

Dejar `agents/openai.yaml` con este contenido:

```yaml
interface:
  display_name: "Iniciar búsqueda de empleo"
  short_description: "Abre la rama operativa de empleo"
  default_prompt: "Usa $iniciar-busqueda-empleo para continuar la búsqueda de empleo."
policy:
  allow_implicit_invocation: false
```

- [ ] **Step 4: Crear el protocolo de la bóveda.**

```markdown
# Inicio de sesión Work — búsqueda de empleo

## Ámbito

Esta nota inicia exclusivamente la rama operativa de búsqueda de empleo de Carrera AI. No modifica ni reinterpreta la investigación metodológica de entrevista.

## Consulta inicial

1. Leer [[README]].
2. Leer [[seguimiento-candidaturas]].
3. Consultar [[datos-core-busqueda]] solo cuando la instrucción posterior requiera adaptar, revisar o valorar una candidatura.
4. Consultar [[datos-privados-candidatura]] solo si el usuario autoriza preparar o completar una candidatura concreta.

## Respuesta de inicio

Indicar el estado de las candidaturas y las acciones relevantes, proponer el siguiente paso seguro y esperar instrucciones. No enviar candidaturas, no usar Chrome y no modificar archivos durante el inicio.
```

- [ ] **Step 5: Validar estructura y formato.**

Ejecutar:

```powershell
python 'C:\Users\gusve\.codex\skills\.system\skill-creator\scripts\quick_validate.py' '.codex/skills/iniciar-busqueda-empleo'
git diff --check -- '.codex/skills/iniciar-busqueda-empleo' 'boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md'
```

Esperado: `quick_validate.py` informa de una skill válida y `git diff --check` no devuelve errores.

- [ ] **Step 6: Commit.**

```powershell
git add -- '.codex/skills/iniciar-busqueda-empleo' 'boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md'
git commit -m "feat: añade inicio local de búsqueda de empleo"
```

### Task 3: Verificar la activación y los límites

**Files:**
- Test: `.codex/skills/iniciar-busqueda-empleo/SKILL.md`
- Test: `boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md`

**Interfaces:**
- Consumes: la skill instalada y una sesión Work fresca en la raíz de `carrera-ai`.
- Produces: evidencia de que la activación carga el contexto correcto sin efectos externos.

- [ ] **Step 1: Ejecutar la invocación real.**

En una sesión Work fresca, enviar exactamente:

```text
$iniciar-busqueda-empleo
```

- [ ] **Step 2: Comprobar la salida.**

Verificar que la respuesta:

1. identifica el host `carrera-ai` y mantiene la rama de búsqueda aislada;
2. informa del estado de candidaturas y acciones relevantes de forma breve;
3. no expone datos privados;
4. no declara haber enviado candidaturas, usado Chrome ni modificado archivos; y
5. termina esperando la siguiente instrucción del usuario.

- [ ] **Step 3: Corregir solo si falla un criterio y repetir la prueba.**

Si la salida omite alguno de los cinco criterios, ajustar únicamente el texto de la skill o del punto de entrada que gobierna ese criterio, ejecutar de nuevo `quick_validate.py` y repetir la invocación real.

- [ ] **Step 4: Commit de una corrección, si existiera.**

```powershell
git add -- '.codex/skills/iniciar-busqueda-empleo' 'boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md'
git commit -m "fix: ajusta inicio local de búsqueda de empleo"
```

## Revisión del plan

- Cobertura: las tareas cubren activación explícita, rehidratación PCS, documento operativo, aislamiento de la investigación, ausencia de acciones externas y prueba en sesión fresca.
- Marcadores pendientes: no contiene `TODO`, `TBD` ni pasos sin rutas o criterios verificables.
- Consistencia: la skill delega el detalle en `INICIO_SESION_WORK.md`; este remite al README y al seguimiento sin duplicar el proceso de candidatura.
