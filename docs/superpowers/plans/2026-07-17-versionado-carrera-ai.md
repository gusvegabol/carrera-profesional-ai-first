# Carrera AI Functional Versioning Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Materializar el sistema de versionado funcional aprobado para que `Carrera AI 2.0 — en desarrollo` tenga una fuente única, un flujo operativo, un SPEC alineado y trazabilidad PCS coherente.

**Architecture:** La fuente funcional de verdad será `docs/VERSIONADO_CARRERA_AI.md`; el procedimiento vivirá separado en `docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md`. README, SPEC y estado PCS actuarán como consumidores resumidos, mientras las sesiones y una decisión PCS conservarán la trazabilidad sin sustituir la autoridad funcional.

**Tech Stack:** Markdown, YAML frontmatter, Git, PowerShell y `rg` para validaciones documentales.

## Global Constraints

- No modificar `C:/Users/gusve/Documents/Apps/project-continuity-system` ni `hosts/hosts.yaml`.
- No abrir formalmente `Carrera AI 2.5`; ESCO permanece como investigación paralela fuera del criterio de finalización de `2.0`.
- No renombrar retrospectivamente documentos ni asignar versiones propias a conceptos, patrones, plantillas o notas auxiliares.
- Usar `MAYOR.MENOR` para versiones globales y `MAYOR.MENOR.PARCHE` para componentes.
- Mantener `0.2` como número no utilizado deliberadamente.
- Una versión abandonada no puede declarar `continuada_en`.
- Una nueva `version_base` debe apuntar a una versión completada o a la raíz `0.0`.
- Conservar abiertas las líneas legítimas de cobertura, adaptación funcional y ESCO; cerrar únicamente la sesión histórica de alcance MVP de la línea `1.x` y la sesión técnica creada por este plan.
- No tratar la versión PCS `2.0` como versión funcional de Carrera AI; ambas numeraciones son independientes.
- Revisar explícitamente tildes, diéresis, eñes y signos de apertura en toda documentación española modificada.
- Respetar la jerarquía local: documento canónico de versión para versión global, SPEC para definición del producto, estado PCS para presente operativo y sesiones para historia.

---

### Task 1: Materializar la fuente canónica de versiones

**Files:**
- Create: `docs/VERSIONADO_CARRERA_AI.md`
- Reference: `docs/superpowers/specs/2026-07-17-versionado-carrera-ai-design.md`

**Interfaces:**
- Consumes: genealogía, estados, reglas de base y continuidad, composición de `2.0` y criterios de cierre aprobados en la SPEC de diseño.
- Produces: fuente única consultable por README, SPEC, estado PCS, sesiones y el flujo operativo de la Task 2.

- [ ] **Step 1: Crear el frontmatter y la declaración de autoridad**

Crear `docs/VERSIONADO_CARRERA_AI.md` con este frontmatter exacto:

```yaml
---
id: versionado-carrera-ai
titulo: Versionado funcional de Carrera AI
version_global_actual: "2.0"
estado_version_global: en_desarrollo
version_base: "1.6"
fecha_actualizacion: 2026-07-17
---
```

Abrir el cuerpo con `# Versionado funcional de Carrera AI` y declarar expresamente:

- que es la fuente funcional de verdad de la versión global;
- que la persona decide las versiones y PCS solo registra gobernanza y trazabilidad;
- que README, SPEC, estado y sesiones no sustituyen este documento;
- que la versión funcional de Carrera AI es independiente de `pcs_version`.

- [ ] **Step 2: Documentar la versión actual y su criterio de finalización**

Incluir una sección `## Versión global actual` con:

```yaml
version: "2.0"
version_base: "1.6"
estado: "en_desarrollo"
continuada_en:
```

Definir el objetivo mediante la secuencia:

```text
cobertura profesional
→ inmersión en profundidad
→ evidencias
→ síntesis de trayectoria
→ Perfil Profesional Accionable
```

Declarar como criterio de finalización la validación del recorrido completo con una persona capaz de revisar, corregir y reconocer como fiel el perfil resultante. Declarar ESCO fuera del criterio de finalización y como candidato provisional a `2.5`, sin abrir esa versión.

- [ ] **Step 3: Incorporar la genealogía completa y sus relaciones**

Crear `## Genealogía histórica` con una tabla que incluya exactamente:

- `0.0`: raíz inicial;
- `0.1`: `app-carrera-profesional`, abandonada, base `0.0`;
- `0.2`: número no utilizado deliberadamente, sin ficha de versión;
- `0.3`: `app-carrera-profesional-c#`, abandonada, base `0.0`;
- `0.4`: `app-carrera-bóveda-conocimiento`, abandonada, base `0.0`;
- `1.0` a `1.6`: completadas y enlazadas secuencialmente;
- `2.0`: en desarrollo, base `1.6`.

Registrar para cada versión `1.x` el hito funcional aprobado en la SPEC. Añadir un bloque explícito para `1.6`:

```yaml
version: "1.6"
version_base: "1.5"
estado: "completada"
continuada_en: "2.0"
```

- [ ] **Step 4: Documentar reglas globales, componentes y candidatos futuros**

Añadir secciones separadas para:

- numeración global `MAYOR.MENOR` sin parches globales;
- estados `propuesta`, `en_desarrollo`, `candidata_a_cierre`, `completada`, `abandonada`;
- invariantes de `version_base` y `continuada_en`;
- definición de componente funcional;
- estados de componentes `borrador`, `en_validacion`, `vigente`, `descartada`, `retirada`;
- versionado semántico de componentes;
- candidatos futuros, con ESCO como investigación paralela y posible `2.5`.

La matriz de `2.0` debe contener exactamente estas filas funcionales:

| Componente | Versión | Estado | Papel | Requisito de cierre |
| --- | --- | --- | --- | --- |
| Entrevista de profundidad | `1.3.2` | `vigente` | Obtener competencias con evidencia | Funcionar dentro del recorrido integral |
| Cobertura profesional | `1.0.0` | `borrador` | Recorrer y organizar la trayectoria | Alcanzar una versión validada |
| Perfil Profesional Accionable | pendiente | no formalizado | Integrar la salida final | Disponer de contrato y primera versión validada |
| ESCO | no es componente activo | investigación | Fuera del alcance de `2.0` | No bloquea el cierre |

- [ ] **Step 5: Añadir trazabilidad y validar la fuente canónica**

Enlazar mediante rutas relativas:

- `DOCUMENTO_SPEC_CARRERA_AI.md`;
- `FLUJO_CAMBIO_VERSION_CARRERA_AI.md`;
- la SPEC de diseño;
- las sesiones `20260630`, `20260705`, `20260710-2347` y `20260712`;
- la decisión que creará la Task 4.

Ejecutar:

```powershell
$p='docs/VERSIONADO_CARRERA_AI.md'
$t=Get-Content -Raw $p
@('version_global_actual: "2.0"','estado_version_global: en_desarrollo','version_base: "1.6"','0.2','no utilizado deliberadamente','Entrevista de profundidad','Cobertura profesional','Perfil Profesional Accionable','ESCO') | ForEach-Object { if (-not $t.Contains($_)) { throw "Falta: $_" } }
rg -n 'TODO|TBD|PENDIENTE:' $p
git diff --check -- $p
```

Resultado esperado: el script no lanza excepciones; `rg` no devuelve marcadores; `git diff --check` no informa errores.

- [ ] **Step 6: Confirmar la fuente canónica**

```powershell
git add -- docs/VERSIONADO_CARRERA_AI.md
git diff --cached --check
git commit -m "docs: materializa versión global de Carrera AI"
```

Resultado esperado: commit con un único archivo nuevo y sin errores de whitespace.

---

### Task 2: Crear el flujo operativo de cambio de versión

**Files:**
- Create: `docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md`
- Reference: `docs/VERSIONADO_CARRERA_AI.md`
- Reference: `docs/superpowers/specs/2026-07-17-versionado-carrera-ai-design.md`

**Interfaces:**
- Consumes: estados, invariantes, autoridad y composición declarados por la Task 1.
- Produces: listas operativas completas para abrir, promover, completar y abandonar versiones globales.

- [ ] **Step 1: Declarar propósito, autoridad y condiciones previas**

Crear el documento con título `# Flujo de cambio de versión de Carrera AI`. Declarar que:

- es un procedimiento funcional local del host `carrera-ai`;
- no modifica ni duplica PCS Core;
- consume `VERSIONADO_CARRERA_AI.md` como fuente de verdad;
- requiere aprobación humana para toda transición global;
- detiene el cambio ante contradicciones.

- [ ] **Step 2: Escribir la lista de comprobación para abrir una versión**

Incluir casillas `- [ ]` para estas tareas, en este orden:

1. detectar y clasificar el hito funcional;
2. comprobar la última versión completada o `0.0`;
3. asignar un número no utilizado;
4. definir objetivo, alcance, exclusiones y criterio de finalización;
5. definir componentes y evidencia esperada;
6. auditar todas las sesiones abiertas;
7. cerrar, suceder o mantener paralelas las sesiones según su relación con la versión;
8. obtener aprobación humana;
9. registrar la decisión funcional mediante PCS;
10. actualizar documento canónico, README, SPEC y estado;
11. abrir la sesión inicial de la nueva versión;
12. ejecutar las validaciones de consistencia.

- [ ] **Step 3: Escribir las listas de promoción, finalización y abandono**

Incluir tres secciones con casillas completas:

- `## Promover a candidata a cierre`: comprobar criterio, fijar versiones exactas, confirmar estados/evidencias, congelar provisionalmente, resolver contradicciones y registrar aprobación.
- `## Completar una versión`: validar con la persona, marcar completada, congelar objetivo/alcance/composición, revisar sesiones, actualizar superficies, registrar decisión de cierre y verificar.
- `## Abandonar una versión`: registrar motivo, dejar `continuada_en` vacío, volver a la última base completada, cerrar sesiones, separar aprendizajes de continuidad y materializar el estado.

- [ ] **Step 4: Documentar la auditoría obligatoria de sesiones**

Incluir una tabla con estas categorías:

| Tipo de sesión | Tratamiento |
| --- | --- |
| Objetivo concluido con la versión | Cerrar |
| Trabajo que continúa en la nueva versión | Cerrar y abrir sucesora enlazada |
| Línea paralela sin versión global | Mantener abierta |
| Infraestructura o gobernanza independiente | Mantener si el alcance sigue válido |
| Objetivo obsoleto | Cerrar documentando el resultado |

Prohibir cambiar retroactivamente `version_global_contexto` para trasladar una sesión entre versiones.

- [ ] **Step 5: Añadir validaciones y condiciones de parada reproducibles**

Documentar como comprobaciones obligatorias:

- unicidad de versión global actual;
- existencia y estado de la base;
- ausencia de continuidad en versiones abandonadas;
- reciprocidad base/continuación;
- componentes exactos al cierre;
- coherencia entre canónico, README, SPEC, estado y sesiones;
- coherencia entre nombre, título y versión interna de componentes;
- resolución de enlaces;
- revisión ortográfica.

Añadir el protocolo de fallo: no materializar, informar la contradicción, no interpretar automáticamente y mantener la propuesta abierta.

- [ ] **Step 6: Validar y confirmar el flujo**

Ejecutar:

```powershell
$p='docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md'
$t=Get-Content -Raw $p
@('## Abrir una versión','## Promover a candidata a cierre','## Completar una versión','## Abandonar una versión','## Auditoría de sesiones','## Condiciones de parada') | ForEach-Object { if (-not $t.Contains($_)) { throw "Falta sección: $_" } }
if (($t -split "`n" | Where-Object { $_ -match '^- \[ \]' }).Count -lt 30) { throw 'La lista operativa no contiene suficientes comprobaciones explícitas' }
git diff --check -- $p
git add -- $p
git diff --cached --check
git commit -m "docs: define flujo de cambio de versión"
```

Resultado esperado: al menos 30 casillas operativas, todas las secciones presentes y un commit limitado al flujo.

---

### Task 3: Alinear el SPEC y los componentes con Carrera AI 2.0

**Files:**
- Modify: `docs/DOCUMENTO_SPEC_CARRERA_AI.md:1`
- Modify: `docs/DOCUMENTO_SPEC_CARRERA_AI.md:3-20`
- Modify: `docs/DOCUMENTO_SPEC_CARRERA_AI.md:54-62`
- Modify: `docs/DOCUMENTO_SPEC_CARRERA_AI.md:122-136`
- Modify: `docs/DOCUMENTO_SPEC_CARRERA_AI.md:154-174`
- Modify: `docs/DOCUMENTO_SPEC_CARRERA_AI.md:507-581`
- Modify: `docs/DOCUMENTO_SPEC_CARRERA_AI.md:664-718`
- Modify: `docs/DOCUMENTO_SPEC_CARRERA_AI.md:720-818`
- Modify: `docs/DOCUMENTO_SPEC_CARRERA_AI.md:1010-1120`
- Modify: `boveda-entrevista-profesional/07_playbook/DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v2_0_0.md:1-20`

**Interfaces:**
- Consumes: alcance y exclusiones de `Carrera AI 2.0` declarados por la Task 1.
- Produces: SPEC revisión 1 coherente con `2.0` y componente de cobertura sin contradicción interna de versión.

- [ ] **Step 1: Añadir control de revisión al SPEC**

Anteponer este frontmatter exacto:

```yaml
---
id: documento-spec-carrera-ai
titulo: Product Spec — Carrera AI
version_producto: "2.0"
revision_spec: 1
estado: vigente
fecha_revision: 2026-07-17
---
```

Cambiar el subtítulo a `## Perfil Profesional Accionable` y añadir una nota de alcance que distinga:

- visión futura del producto, que puede incorporar interoperabilidad;
- alcance de `2.0`, que termina con un Perfil Profesional Accionable integral y revisable sin exigir ESCO;
- investigación ESCO paralela y candidata a un hito posterior.

- [ ] **Step 2: Separar ESCO de la definición y del alcance obligatorio de 2.0**

Revisar las secciones 1, 3, 5.4, 7.1 y 8.13 para que:

- ESCO aparezca como extensión futura opcional y revisable;
- la entidad principal de `2.0` no requiera correspondencia ESCO;
- el objetivo de `2.0` sea producir el perfil mediante cobertura, profundidad, evidencias y síntesis;
- se conserve la prudencia: ESCO nunca prueba ni certifica competencias.

No eliminar la descripción conceptual de correspondencias ESCO; moverla semánticamente a una capa futura fuera del criterio de cierre de `2.0`.

- [ ] **Step 3: Corregir flujo, funcionalidades, requisitos e hipótesis del MVP**

Aplicar estas modificaciones exactas:

- marcar `9.5 Mapeo ESCO candidato` como flujo futuro fuera de `2.0`;
- eliminar «Proponer correspondencias ESCO candidatas» de `10.1 Incluido en MVP`;
- añadir a `10.2 Fuera del MVP de Carrera AI 2.0` la integración operativa ESCO;
- marcar `RF-11 — Mapear a ESCO` como requisito futuro no exigible a `2.0`;
- cambiar la hipótesis ESCO de la sección 17 por una línea futura no bloqueante;
- retirar `ESCO mappings candidatos` del flujo recomendado de la sección 18;
- retirar correspondencias ESCO de la salida mínima de la sección 19;
- reescribir la definición de éxito de la sección 20 para que la persona reconozca un perfil fiel, útil, evidenciado y narrable, sin exigir traducción ESCO;
- mantener las decisiones técnicas de ESCO en la sección 21 como pendientes de una versión posterior.

- [ ] **Step 4: Añadir el historial interno de revisiones del SPEC**

Añadir al final `## 22. Historial de revisiones` con una tabla que registre:

| Revisión | Fecha | Cambio | Motivo | Impacto global |
| --- | --- | --- | --- | --- |
| `1` | 2026-07-17 | Se asocia el SPEC a `Carrera AI 2.0` y se separa ESCO del criterio de finalización | El Perfil Profesional Accionable debe poder validarse sin bloquearse por la investigación ESCO | No cambia `2.0`; aclara su alcance aprobado |

Enlazar `VERSIONADO_CARRERA_AI.md` y la decisión PCS de la Task 4.

- [ ] **Step 5: Corregir la contradicción interna del componente de cobertura**

En `DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v2_0_0.md`, sustituir:

```text
Esta versión `v1.0.4` parte de
```

por:

```text
Esta versión `v2.0.0` parte de
```

Conservar la referencia a `DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_3` y no modificar el contrato metodológico del componente.

- [ ] **Step 6: Validar alcance, revisión y coherencia de versión**

Ejecutar:

```powershell
$spec='docs/DOCUMENTO_SPEC_CARRERA_AI.md'
$coverage='boveda-entrevista-profesional/07_playbook/DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v2_0_0.md'
$s=Get-Content -Raw $spec
@('version_producto: "2.0"','revision_spec: 1','## 22. Historial de revisiones','fuera del criterio de finalización') | ForEach-Object { if (-not $s.Contains($_)) { throw "Falta en SPEC: $_" } }
if ((Get-Content -Raw $coverage) -match 'Esta versión `v1\.0\.4`') { throw 'Persiste la versión interna incorrecta v1.0.4' }
rg -n 'Esta versión `v2\.0\.0`' $coverage
git diff --check -- $spec $coverage
```

Resultado esperado: SPEC revisión 1, separación explícita de ESCO y una única versión interna `v2.0.0` en el componente.

- [ ] **Step 7: Confirmar la alineación funcional**

```powershell
git add -- docs/DOCUMENTO_SPEC_CARRERA_AI.md boveda-entrevista-profesional/07_playbook/DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v2_0_0.md
git diff --cached --check
git commit -m "docs: alinea SPEC y cobertura con Carrera AI 2.0"
```

Resultado esperado: commit con dos archivos y sin cambios en otros documentos metodológicos.

---

### Task 4: Integrar versión, autoridad y trazabilidad en las superficies operativas

**Files:**
- Create: `.pcs/sesiones/sesion-20260717-1642-materializacion-versionado-carrera-ai.md`
- Create: `.pcs/decisiones/DEC-20260717-1642-001-versionado-funcional-carrera-ai.md`
- Modify: `README.md:1-64`
- Modify: `AGENTS.md:20-29`
- Modify: `docs/AGENTS.md:7-17`
- Modify: `.pcs/estado/estado-actual.md:1-90`
- Modify: `.pcs/sesiones/sesion-20260630-alcance-mvp-carrera-ai.md:1-8`
- Modify: `.pcs/sesiones/sesion-20260630-alcance-mvp-carrera-ai.md:end`
- Modify: `.pcs/sesiones/sesion-20260705-concepto-cobertura-profesional-carrera-ai.md:1-8`
- Modify: `.pcs/sesiones/sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md:1-10`
- Modify: `.pcs/sesiones/sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai.md:1-10`
- Modify: `.pcs/sesiones/sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai.md:end`

**Interfaces:**
- Consumes: fuente canónica de Task 1, flujo de Task 2 y SPEC alineado de Task 3.
- Produces: orientación visible, decisión vigente, estado operativo y sesiones delimitadas por versión.

- [ ] **Step 1: Crear y cerrar la sesión técnica de materialización**

Crear `.pcs/sesiones/sesion-20260717-1642-materializacion-versionado-carrera-ai.md` conforme a `TEMPLATE_SESION.md` con este frontmatter:

```yaml
---
id: sesion-20260717-1642-materializacion-versionado-carrera-ai
titulo: Materialización del versionado funcional de Carrera AI
inicio: 2026-07-17 16:42
cierre: 2026-07-17
estado: cerrada
tipo: sesion
host: carrera-ai
sesion_relacionada: sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai
version_global_contexto: "2.0"
---
```

El cuerpo debe contener las capas episódica y semántica, la decisión derivada, todos los documentos afectados, una rehidratación futura que apunte al documento canónico y el checklist de consolidación completamente marcado. Declarar que no existen acciones formales abiertas derivadas de la materialización.

- [ ] **Step 2: Registrar la decisión funcional mediante PCS**

Crear `.pcs/decisiones/DEC-20260717-1642-001-versionado-funcional-carrera-ai.md` conforme a `TEMPLATE_DECISION.md` con:

```yaml
---
id: DEC-20260717-1642-001-versionado-funcional-carrera-ai
titulo: Adoptar el versionado funcional de Carrera AI
estado: vigente
fecha_registro: 2026-07-17
fecha_adopcion: 2026-07-17
fecha_vigencia: 2026-07-17
tipo: decision
host: carrera-ai
---
```

El enunciado debe adoptar:

- el modelo de dos niveles;
- `Carrera AI 2.0 — en desarrollo`, base `1.6`;
- el Perfil Profesional Accionable como objetivo de cierre;
- ESCO fuera de `2.0` y candidato provisional a `2.5`;
- `VERSIONADO_CARRERA_AI.md` como fuente funcional de verdad;
- `FLUJO_CAMBIO_VERSION_CARRERA_AI.md` como procedimiento local.

Registrar como alternativas descartadas: versión única para todo, versionar solo playbooks y mantener el versionado distribuido entre sesiones/README. Relacionar la sesión técnica, la sesión funcional activa, el estado y la ausencia de acciones formales.

- [ ] **Step 3: Delimitar las sesiones existentes por versión**

Aplicar exactamente:

- `sesion-20260630-alcance-mvp-carrera-ai.md`: establecer `cierre: 2026-07-17`, `estado: cerrada`, añadir `linea_version_global: "1.x"`, cambiar también la fila visible `Estado` de `Abierta` a `Cerrada` y añadir una sección final de cierre histórico que indique que no admite trabajo de `2.0`.
- `sesion-20260705-concepto-cobertura-profesional-carrera-ai.md`: añadir `version_global_contexto: "2.0"` y mantenerla abierta.
- `sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai.md`: añadir `version_global_contexto: "2.0"`, mantenerla abierta y registrar el diseño aprobado, la decisión y los dos documentos funcionales creados.
- `sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md`: añadir `linea_paralela: esco`, `fuera_del_alcance_de: "2.0"` y `version_global_candidata: "2.5"`; no añadir `version_global_contexto` y mantenerla abierta.

No modificar el objetivo metodológico de cobertura ni el objetivo investigador de ESCO.

- [ ] **Step 4: Actualizar README y superficies de orientación**

En `README.md`, añadir tras la introducción:

```markdown
## Versión global actual

`Carrera AI 2.0` está `en desarrollo`.

Su objetivo es validar un primer Perfil Profesional Accionable integral y revisable mediante cobertura profesional, inmersión en profundidad, evidencias y síntesis de trayectoria. ESCO queda fuera del criterio de finalización de `2.0` y continúa como investigación paralela.

La fuente funcional de verdad es [Versionado funcional de Carrera AI](docs/VERSIONADO_CARRERA_AI.md). El procedimiento de transición está en [Flujo de cambio de versión](docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md).
```

Añadir ambos documentos a `Documentación principal del proyecto`.

En `AGENTS.md`, añadir `./docs/VERSIONADO_CARRERA_AI.md` y `./docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md` a «Qué consultar primero» cuando la tarea afecte al versionado funcional.

En `docs/AGENTS.md`, situar `VERSIONADO_CARRERA_AI.md` como autoridad para versión global y `FLUJO_CAMBIO_VERSION_CARRERA_AI.md` como procedimiento, sin desplazar al SPEC de su autoridad sobre producto ni al núcleo metodológico sobre entrevista.

- [ ] **Step 5: Actualizar el estado operativo vivo**

En `.pcs/estado/estado-actual.md`:

- mantener `fecha_actualizacion: 2026-07-17`;
- declarar `Carrera AI 2.0 — en desarrollo` y base `1.6` al inicio de la situación actual;
- señalar `VERSIONADO_CARRERA_AI.md` como fuente funcional de verdad;
- añadir como próximo paso aplicar `FLUJO_CAMBIO_VERSION_CARRERA_AI.md` en futuras transiciones;
- registrar la decisión `DEC-20260717-1642-001-versionado-funcional-carrera-ai` como vigente;
- conservar el foco metodológico actual de cobertura;
- conservar ESCO como investigación paralela no bloqueante;
- añadir la sesión técnica cerrada y la SPEC de diseño a referencias de continuidad.

- [ ] **Step 6: Validar PCS, sesiones y orientación**

Ejecutar:

```powershell
$decision='.pcs/decisiones/DEC-20260717-1642-001-versionado-funcional-carrera-ai.md'
$session='.pcs/sesiones/sesion-20260717-1642-materializacion-versionado-carrera-ai.md'
if (-not (Test-Path $decision)) { throw 'Falta la decisión PCS' }
if (-not (Test-Path $session)) { throw 'Falta la sesión técnica' }
if ((Get-Content -Raw $decision) -notmatch 'estado: vigente') { throw 'La decisión no está vigente' }
if ((Get-Content -Raw $session) -notmatch 'estado: cerrada') { throw 'La sesión técnica no está cerrada' }
if ((Get-Content -Raw '.pcs/sesiones/sesion-20260630-alcance-mvp-carrera-ai.md') -notmatch 'estado: cerrada') { throw 'La sesión histórica 1.x sigue abierta' }
if ((Get-Content -Raw '.pcs/sesiones/sesion-20260705-concepto-cobertura-profesional-carrera-ai.md') -notmatch 'version_global_contexto: "2.0"') { throw 'Cobertura no está vinculada a 2.0' }
if ((Get-Content -Raw '.pcs/sesiones/sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md') -match 'version_global_contexto:') { throw 'ESCO no debe pertenecer a una versión global abierta' }
rg -n 'Carrera AI 2\.0|VERSIONADO_CARRERA_AI|FLUJO_CAMBIO_VERSION' README.md AGENTS.md docs/AGENTS.md .pcs/estado/estado-actual.md
git diff --check
```

Resultado esperado: decisión vigente, sesión técnica e histórica cerradas, cobertura/adaptación en `2.0`, ESCO paralela y ninguna inconsistencia de whitespace.

- [ ] **Step 7: Confirmar la integración operativa**

```powershell
git add -- README.md AGENTS.md docs/AGENTS.md .pcs/estado/estado-actual.md .pcs/decisiones/DEC-20260717-1642-001-versionado-funcional-carrera-ai.md .pcs/sesiones/sesion-20260630-alcance-mvp-carrera-ai.md .pcs/sesiones/sesion-20260705-concepto-cobertura-profesional-carrera-ai.md .pcs/sesiones/sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md .pcs/sesiones/sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai.md .pcs/sesiones/sesion-20260717-1642-materializacion-versionado-carrera-ai.md
git diff --cached --check
git commit -m "docs(pcs): registra adopción del versionado funcional"
```

Resultado esperado: commit limitado a orientación y memoria PCS, sin tocar PCS Core ni `hosts/hosts.yaml`.

---

### Task 5: Ejecutar la auditoría integral contra la SPEC

**Files:**
- Verify: `docs/VERSIONADO_CARRERA_AI.md`
- Verify: `docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md`
- Verify: `docs/DOCUMENTO_SPEC_CARRERA_AI.md`
- Verify: `README.md`
- Verify: `AGENTS.md`
- Verify: `docs/AGENTS.md`
- Verify: `.pcs/estado/estado-actual.md`
- Verify: `.pcs/decisiones/DEC-20260717-1642-001-versionado-funcional-carrera-ai.md`
- Verify: `.pcs/sesiones/*.md`
- Verify: `boveda-entrevista-profesional/07_playbook/DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v2_0_0.md`

**Interfaces:**
- Consumes: todos los entregables de las Tasks 1-4.
- Produces: evidencia final de cumplimiento requisito por requisito y árbol de trabajo limpio.

- [ ] **Step 1: Verificar presencia y autoridad de los artefactos**

```powershell
$required=@(
  'docs/VERSIONADO_CARRERA_AI.md',
  'docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md',
  'docs/DOCUMENTO_SPEC_CARRERA_AI.md',
  '.pcs/decisiones/DEC-20260717-1642-001-versionado-funcional-carrera-ai.md',
  '.pcs/sesiones/sesion-20260717-1642-materializacion-versionado-carrera-ai.md'
)
$required | ForEach-Object { if (-not (Test-Path $_)) { throw "Falta artefacto: $_" } }
rg -n 'fuente funcional de verdad|version_global_actual: "2.0"|version_base: "1.6"' docs/VERSIONADO_CARRERA_AI.md
```

Resultado esperado: cinco artefactos presentes y declaraciones canónicas localizadas.

- [ ] **Step 2: Verificar genealogía e invariantes**

```powershell
$v=Get-Content -Raw 'docs/VERSIONADO_CARRERA_AI.md'
@('0.0','0.1','0.2','0.3','0.4','1.0','1.1','1.2','1.3','1.4','1.5','1.6','2.0') | ForEach-Object { if (-not $v.Contains($_)) { throw "Falta versión: $_" } }
if ($v -notmatch '0\.2.+no utilizado deliberadamente') { throw '0.2 no está documentada como no utilizada' }
if ($v -notmatch 'version: "1\.6"[\s\S]+version_base: "1\.5"[\s\S]+estado: "completada"[\s\S]+continuada_en: "2\.0"') { throw 'La continuidad 1.6 -> 2.0 no está completa' }
```

Resultado esperado: genealogía completa, hueco `0.2` preservado y continuidad `1.6 → 2.0` demostrada.

- [ ] **Step 3: Verificar composición y exclusión de ESCO**

```powershell
$v=Get-Content -Raw 'docs/VERSIONADO_CARRERA_AI.md'
$s=Get-Content -Raw 'docs/DOCUMENTO_SPEC_CARRERA_AI.md'
@('1.3.2','1.0.0','Perfil Profesional Accionable','No bloquea el cierre') | ForEach-Object { if (-not $v.Contains($_)) { throw "Falta composición: $_" } }
if ($s -notmatch 'ESCO[\s\S]{0,300}fuera del criterio de finalización') { throw 'El SPEC no separa ESCO del cierre de 2.0' }
if ($s -match '→ ESCO mappings candidatos') { throw 'El flujo MVP todavía exige ESCO' }
```

Resultado esperado: componentes exactos y ESCO no bloqueante en canónico y SPEC.

- [ ] **Step 4: Verificar sesiones, decisión y coherencia transversal**

```powershell
$checks=@{
  'README.md'='Carrera AI 2.0'
  'docs/DOCUMENTO_SPEC_CARRERA_AI.md'='version_producto: "2.0"'
  '.pcs/estado/estado-actual.md'='Carrera AI 2.0'
  '.pcs/sesiones/sesion-20260705-concepto-cobertura-profesional-carrera-ai.md'='version_global_contexto: "2.0"'
  '.pcs/sesiones/sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai.md'='version_global_contexto: "2.0"'
}
foreach($entry in $checks.GetEnumerator()) { if ((Get-Content -Raw $entry.Key) -notlike "*$($entry.Value)*") { throw "Incoherencia en $($entry.Key): falta $($entry.Value)" } }
if ((Get-Content -Raw '.pcs/sesiones/sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md') -notmatch 'version_global_candidata: "2.5"') { throw 'La línea ESCO no conserva su candidatura futura' }
```

Resultado esperado: todas las superficies declaran el papel correcto sin convertir ESCO en versión abierta.

- [ ] **Step 5: Verificar enlaces Markdown locales**

Ejecutar un script PowerShell de solo lectura sobre los archivos modificados que extraiga destinos Markdown relativos, ignore `http`, anclas y rutas futuras que ya deban existir, resuelva cada destino contra el directorio del archivo y lance una excepción si falta alguno. Incluir al menos los enlaces de README, SPEC, documentos de versionado, decisión y sesiones.

Comando base:

```powershell
$files=git show --pretty='' --name-only HEAD~4..HEAD | Where-Object { $_ -match '\.md$' } | Sort-Object -Unique
$errors=@()
foreach($file in $files){
  $text=Get-Content -Raw $file
  $matches=[regex]::Matches($text,'\[[^\]]+\]\((?!https?://|#)([^)]+)\)')
  foreach($m in $matches){
    $target=$m.Groups[1].Value.Trim('<','>') -replace '#.*$',''
    if(-not $target){continue}
    $base=Split-Path -Parent $file
    if(-not $base){$base='.'}
    $resolved=[IO.Path]::GetFullPath((Join-Path $base $target))
    if(-not (Test-Path -LiteralPath $resolved)){$errors += "$file -> $target"}
  }
}
if($errors.Count){$errors; throw 'Hay enlaces locales rotos'}
```

Resultado esperado: ninguna ruta rota.

- [ ] **Step 6: Ejecutar revisión ortográfica dirigida y comprobaciones Git**

Buscar pérdidas frecuentes de ortografía en el texto nuevo o añadido:

```powershell
$files=git show --pretty='' --name-only HEAD~4..HEAD | Where-Object { $_ -match '\.md$' } | Sort-Object -Unique
rg -n -i '\b(accion|decision|sesion|version|metodologia|validacion|revision|documentacion|relacion|proposito|ambito|canonico|diseno)\b' $files
git diff HEAD~4..HEAD --check
git status --short
git log -5 --oneline
```

Resultado esperado: `rg` no encuentra formas españolas sin tilde en prosa nueva; `git diff --check` no informa errores; `git status --short` está vacío; el historial muestra los cuatro commits del plan después del commit de la SPEC de diseño.

- [ ] **Step 7: Revisar requisito por requisito y registrar el resultado**

Contrastar los ocho criterios de aceptación de `docs/superpowers/specs/2026-07-17-versionado-carrera-ai-design.md` contra evidencia directa de los archivos y comandos anteriores. No declarar completado el trabajo si cualquier criterio carece de evidencia o si persiste una contradicción.

No crear un commit adicional si la auditoría no requiere correcciones. Si requiere una corrección estrictamente necesaria, aplicarla en el archivo propietario, repetir todas las validaciones afectadas y confirmar con:

```powershell
git add -- README.md AGENTS.md docs/AGENTS.md docs/VERSIONADO_CARRERA_AI.md docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md docs/DOCUMENTO_SPEC_CARRERA_AI.md boveda-entrevista-profesional/07_playbook/DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v2_0_0.md .pcs/estado/estado-actual.md .pcs/decisiones/DEC-20260717-1642-001-versionado-funcional-carrera-ai.md .pcs/sesiones/sesion-20260630-alcance-mvp-carrera-ai.md .pcs/sesiones/sesion-20260705-concepto-cobertura-profesional-carrera-ai.md .pcs/sesiones/sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md .pcs/sesiones/sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai.md .pcs/sesiones/sesion-20260717-1642-materializacion-versionado-carrera-ai.md
git diff --cached --check
git commit -m "docs: corrige validación final del versionado"
```

Resultado esperado: los ocho criterios demostrados y ningún trabajo requerido pendiente.
