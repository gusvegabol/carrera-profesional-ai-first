# Actualizar inicio de búsqueda de empleo para gestionar sesiones PCS — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Actualizar `$empleo-inicio-busqueda` para que cada invocación cree una nueva sesión PCS de Job-up con la fecha y hora de invocación, cierre las sesiones Job-up anteriores que sigan abiertas y actualice la trazabilidad del estado vivo antes de continuar con la rehidratación operativa.

**Architecture:** La skill local seguirá siendo el punto de entrada explícito de Job-up y no se convertirá en un comando `pcs::` ni modificará el Core PCS. Antes de leer el estado de candidaturas, ejecutará un ciclo de sesión PCS delimitado: resolver timestamp, localizar sesiones Job-up activas, cerrar las anteriores, crear la nueva sesión desde la plantilla canónica y actualizar `estado-actual.md`. El flujo debe preparar y validar todos los cambios antes de escribir para evitar cierres parciales.

**Tech Stack:** Markdown, YAML frontmatter, Agent Skills, PowerShell para validaciones locales y PCS 2.0.

## Estado de ejecución

- [x] Task 1: Actualizar el diseño funcional y fijar el contrato de sesión.
- [x] Task 2: Crear el fixture y ejecutar la prueba RED de ciclo de sesiones.
- [x] Task 3: Actualizar la skill y el punto de entrada Job-up.
- [x] Task 4: Ejecutar GREEN y cerrar los huecos de interpretación.
- [x] Task 5: Verificación final y entrega del plan ejecutado.

## Nota breve de cierre

- Minor diferido 1: el fixture de Task 2 queda con cinco archivos porque el quinto caso concreto de sesión incompleta es necesario para cubrir el escenario 3.
- Minor diferido 2: la reejecución GREEN del CLI externo en Task 4 no pudo llegar a un estado funcional por límites de cuenta y entorno; la evidencia fresca de subagente y las comprobaciones aisladas del fixture quedan registradas.

## Global Constraints

- La activación seguirá siendo exclusivamente `$empleo-inicio-busqueda`.
- No se registrará ningún comando nuevo en PCS Core.
- Las sesiones se crearán con el patrón `sesion-YYYYMMDD-HHMM-slug.md` y se usará un sufijo si existe colisión en el mismo minuto.
- Se cerrarán únicamente sesiones anteriores de Job-up en estado `abierta`, `en pausa` o `en redacción`; las sesiones `consolidada`, `cerrada` y `archivada` se conservarán sin reescritura.
- El cierre de una sesión anterior conservará su contenido histórico, añadirá la hora de cierre de la invocación y dejará trazado que fue cerrada al iniciar un nuevo bloque Job-up.
- La nueva sesión comenzará en estado `abierta` y usará la plantilla y entidad canónicas de PCS.
- La skill actualizará solo la trazabilidad necesaria de `estado-actual.md`; no cambiará el SPEC, los playbooks ni la investigación metodológica de entrevista.
- La skill no enviará candidaturas, no usará Chrome, no contactará con terceros y no preparará una candidatura concreta sin una instrucción posterior y explícita.
- Si falta una fuente canónica, el host no puede resolverse, existe una ambigüedad de alcance o no puede prepararse el conjunto completo de cambios, el flujo se detendrá antes de escribir.
- Las pruebas no modificarán el `.pcs/` operativo: usarán un fixture aislado o una copia de prueba fuera de la memoria viva del host.

---

### Task 1: Actualizar el diseño funcional y fijar el contrato de sesión

**Files:**
- Modify: `docs/superpowers/specs/2026-07-22-inicio-busqueda-empleo-skill-design.md`
- Read: `C:/Users/gusve/Documents/Apps/project-continuity-system/core/ENTIDAD_SESION.md`
- Read: `C:/Users/gusve/Documents/Apps/project-continuity-system/templates/TEMPLATE_SESION.md`
- Read: `.pcs/estado/estado-actual.md`
- Read: `.pcs/sesiones/sesion-20260727-2109-busqueda-empleo.md`

**Interfaces:**
- Consumes: la decisión del usuario de crear una sesión nueva por invocación y cerrar las anteriores de Job-up.
- Produces: requisitos verificables para la skill, el protocolo de bóveda y las pruebas.

- [x] **Step 1: Documentar el comportamiento actual que falla.**

Registrar en el apartado de pruebas del diseño que la skill actual solo rehidrata y responde; no crea sesiones, no registra la hora de invocación y no cierra sesiones Job-up anteriores.

- [x] **Step 2: Sustituir el contrato de “inicio sin escrituras”.**

Actualizar el diseño para indicar que la invocación sí puede escribir únicamente en:

```text
.pcs/sesiones/
.pcs/estado/estado-actual.md
```

La escritura estará limitada al ciclo de sesiones PCS de Job-up y no incluirá candidaturas, contactos ni acciones externas.

- [x] **Step 3: Fijar la selección de sesiones anteriores.**

Definir que una sesión pertenece a Job-up cuando su frontmatter, título o contenido la identifica explícitamente como búsqueda de empleo/Job-up, y que solo se cierran sesiones anteriores con estado `abierta`, `en pausa` o `en redacción`.

- [x] **Step 4: Fijar la transacción documental.**

Documentar el orden obligatorio: preparar timestamp y nombre, localizar y validar objetivos, cerrar sesiones anteriores, crear la nueva sesión y actualizar el estado. Si falla una validación previa, no se realiza ninguna escritura.

- [x] **Step 5: Revisar el diseño en español.**

Comprobar tildes, eñes, signos y consistencia terminológica antes de continuar.

### Task 2: Crear el fixture y ejecutar la prueba RED de ciclo de sesiones

**Files:**
- Create: `docs/superpowers/tests/2026-07-27-empleo-inicio-busqueda-sesiones.md`
- Create during test only: `docs/superpowers/tests/fixtures/empleo-inicio-busqueda-sesiones/`
- Read-only reference: `.pcs/sesiones/`

**Interfaces:**
- Consumes: la skill actual sin modificar y tres sesiones fixture con estados `abierta`, `en pausa` y `cerrada`, incluyendo una sesión no perteneciente a Job-up.
- Produces: evidencia RED y una matriz de expectativas para la prueba GREEN.

- [x] **Step 1: Crear un fixture aislado.**

Preparar cuatro sesiones mínimas en el fixture:

```text
sesion-job-up-abierta.md       estado: abierta
sesion-job-up-pausada.md       estado: en pausa
sesion-job-up-cerrada.md       estado: cerrada
sesion-metodologia-abierta.md  estado: abierta, no Job-up
```

Incluir en las dos primeras referencias explícitas a Job-up y una sesión previa relacionada.

- [x] **Step 2: Ejecutar tres escenarios RED con un agente fresco sin la actualización.**

Usar estos escenarios independientes:

1. Invocación normal: el agente debe iniciar Job-up con presión de rapidez y comprobar si crea la sesión fechada.
2. Invocación con varias sesiones previas: el agente debe cerrar las sesiones Job-up abiertas/pausadas sin tocar la sesión metodológica.
3. Invocación con una sesión anterior parcialmente documentada: el agente debe preservar el contenido y registrar el cierre sin inventar resultados.

- [x] **Step 3: Verificar el fallo RED.**

Registrar literalmente que la skill actual no crea ninguna sesión, no cierra las anteriores y mantiene la prohibición de escritura PCS. Registrar también cualquier racionalización del agente, como tratar la nueva sesión como una responsabilidad manual posterior.

- [x] **Step 4: Convertir las expectativas en criterios observables.**

La prueba GREEN deberá comprobar nombre, timestamp, estado, cierre, exclusión de sesiones no Job-up, actualización del puntero de estado, ausencia de acciones/decisiones nuevas y ausencia de acciones externas.

### Task 3: Actualizar la skill y el punto de entrada Job-up

**Files:**
- Modify: `.codex/skills/empleo-inicio-busqueda/SKILL.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md`
- Read: `C:/Users/gusve/Documents/Apps/project-continuity-system/core/ENTIDAD_SESION.md`
- Read: `C:/Users/gusve/Documents/Apps/project-continuity-system/templates/TEMPLATE_SESION.md`

**Interfaces:**
- Consumes: el contrato actualizado del diseño y el fixture RED.
- Produces: una skill explícita que gobierna el ciclo de sesión y un punto de entrada coherente con sus escrituras limitadas.

- [x] **Step 1: Reescribir el procedimiento de la skill en orden transaccional.**

El procedimiento deberá ordenar exactamente:

```text
1. Resolver host, fecha y hora de invocación.
2. Leer las fuentes canónicas de sesión y el estado vivo.
3. Identificar y validar las sesiones Job-up anteriores que estén abiertas, pausadas o en redacción.
4. Preparar sus cierres sin tocar sesiones consolidadas, cerradas, archivadas ni líneas no Job-up.
5. Crear la nueva sesión con frontmatter PCS, timestamp, sesión relacionada y estado abierta.
6. Actualizar el puntero y la mención de sesión activa en estado-actual.md.
7. Leer INICIO_SESION_WORK.md y seguir la consulta inicial de Job-up.
8. Responder con ámbito, estado breve, acciones relevantes y siguiente paso seguro.
```

- [x] **Step 2: Añadir reglas contra cierres incorrectos.**

Indicar que no se deben cerrar sesiones de metodología, ESCO, GitHub u otras líneas aunque estén abiertas, y que una sesión ya cerrada no debe volver a editarse.

- [x] **Step 3: Añadir regla de fallo seguro.**

Si el agente no puede determinar si una sesión es Job-up o no puede preparar todos los cambios, debe informar del bloqueo y no escribir ningún archivo PCS.

- [x] **Step 4: Actualizar el punto de entrada de bóveda.**

Eliminar la instrucción que prohíbe toda modificación durante el inicio y reemplazarla por el alcance exacto: se permiten únicamente las escrituras del ciclo de sesiones PCS; siguen prohibidos envíos, Chrome, contactos y modificaciones de candidaturas durante el inicio.

- [x] **Step 5: Mantener el aislamiento funcional.**

Conservar la lectura condicional de `datos-core-busqueda.md` y `datos-privados-candidatura.md`, y no ampliar la skill a la preparación automática de candidaturas.

### Task 4: Ejecutar GREEN y cerrar los huecos de interpretación

**Files:**
- Modify: `.codex/skills/empleo-inicio-busqueda/SKILL.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md`
- Modify: `docs/superpowers/tests/2026-07-27-empleo-inicio-busqueda-sesiones.md`

**Interfaces:**
- Consumes: la skill actualizada y el fixture RED.
- Produces: evidencia de cumplimiento y correcciones de redacción si aparecen racionalizaciones.

- [x] **Step 1: Validar el formato de la skill.**

Ejecutar:

```powershell
python 'C:\Users\gusve\.codex\skills\.system\skill-creator\scripts\quick_validate.py' '.codex/skills/empleo-inicio-busqueda'
git diff --check -- '.codex/skills/empleo-inicio-busqueda/SKILL.md' 'boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md' 'docs/superpowers/specs/2026-07-22-inicio-busqueda-empleo-skill-design.md'
```

Esperado: skill válida y ningún error de espacios o finales de línea.

- [x] **Step 2: Ejecutar los tres escenarios GREEN con un agente fresco.**

En cada escenario, el agente debe producir una nueva sesión con el timestamp de invocación, cerrar solo las sesiones Job-up activas anteriores, conservar las demás y continuar con la rehidratación.

- [x] **Step 3: Verificar la transacción documental.**

Comprobar que no quedan dos sesiones Job-up activas tras una invocación normal, que la sesión nueva es `abierta`, que cada sesión cerrada tiene `cierre`, que el estado apunta a la sesión nueva y que no aparecen acciones o decisiones PCS inventadas.

- [x] **Step 4: Probar colisión de nombre.**

Simular dos invocaciones en el mismo minuto y comprobar que la segunda usa el sufijo incremental permitido por `ENTIDAD_SESION.md`, sin sobrescribir la primera.

- [x] **Step 5: Probar fallo seguro.**

Retirar del fixture una fuente canónica o marcar una sesión con clasificación ambigua. Comprobar que el agente detiene la invocación antes de escribir y explica qué debe resolverse.

- [x] **Step 6: Registrar nuevas racionalizaciones.**

Si el agente cierra sesiones no Job-up, omite el estado, escribe parcialmente o trata el cierre como opcional, añadir una regla explícita a la skill y repetir el escenario afectado.

### Task 5: Verificación final y entrega del plan ejecutado

**Files:**
- Read: `.codex/skills/empleo-inicio-busqueda/SKILL.md`
- Read: `boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md`
- Read: `docs/superpowers/specs/2026-07-22-inicio-busqueda-empleo-skill-design.md`
- Read: `docs/superpowers/tests/2026-07-27-empleo-inicio-busqueda-sesiones.md`
- Read: `.pcs/estado/estado-actual.md`

**Interfaces:**
- Consumes: cambios implementados y evidencias GREEN/REFACTOR.
- Produces: confirmación trazable de que la actualización cumple el alcance sin alterar el Core PCS.

- [x] **Step 1: Revisar la cobertura contra la orden del usuario.**

Confirmar explícitamente que la invocación crea una sesión con fecha/hora, cierra las anteriores activas de Job-up, preserva otras líneas, actualiza el estado y mantiene las restricciones externas.

- [x] **Step 2: Revisar ortografía española.**

Corregir tildes, eñes, signos y términos inconsistentes en los documentos modificados.

- [x] **Step 3: Confirmar que el Core no fue modificado.**

Ejecutar:

```powershell
git status --short -- 'C:\Users\gusve\Documents\Apps\project-continuity-system'
```

Esperado: sin cambios atribuibles a esta actualización en el Core PCS.

- [x] **Step 4: Revisar el diff del host sin tocar cambios ajenos.**

Inspeccionar únicamente los archivos de esta actualización y conservar todas las modificaciones preexistentes del worktree.

- [x] **Step 5: Dejar los cambios listos para revisión humana y crear solo el commit del propio plan si, tras la verificación final, ese es el único cambio versionable.**

No crear commit de archivos ajenos ni modificar candidaturas; si procede, limitar el commit al propio plan. Entregar el resumen de archivos, pruebas y cualquier limitación restante.

## Self-review del plan

- La orden de crear una sesión por invocación está cubierta en Tasks 1, 3 y 4.
- El cierre de sesiones Job-up anteriores está cubierto en Tasks 1, 2, 3 y 4.
- La fecha/hora, colisión de nombres y trazabilidad están cubiertas en Tasks 3 y 4.
- El aislamiento respecto a metodología, Core PCS y acciones externas está cubierto en Global Constraints y Tasks 3–5.
- La prueba RED existe antes de modificar la skill y la prueba GREEN reutiliza los mismos escenarios.
- No hay marcadores de trabajo sin resolver ni referencias a funciones inexistentes; cada validación incluye ruta o criterio observable.
