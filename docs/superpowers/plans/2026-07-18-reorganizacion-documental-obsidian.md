# Reorganización documental y nueva bóveda Obsidian Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reorganizar la documentación viva de Carrera AI en una única bóveda raíz de Obsidian, con histórico separado, enlaces comprobados y configuración heredada retirada de forma recuperable.

**Architecture:** La documentación viva se organiza bajo `docs/`; `.pcs/` conserva su estructura y autoridad; `historico/` contiene documentos superados bajo su ruta de procedencia. La bóveda se inicializa manualmente en la raíz después de retirar todas las configuraciones de Obsidian anidadas y de verificar una copia completa externa. La migración se ejecuta por bloques aprobados y con movimientos Git.

**Tech Stack:** Markdown, Git, PowerShell, Obsidian Desktop y el plugin comunitario Hide Folders.

## Global Constraints

- No usar Obsidian CLI.
- No mover, renombrar ni reestructurar `.pcs/`.
- No iniciar Obsidian en la raíz mientras exista `boveda-entrevista-profesional/.obsidian/`.
- Crear y verificar una copia completa de `carrera-ai` fuera de la carpeta de trabajo antes de eliminar configuraciones o datos heredados.
- Ignorar en Git la nueva `.obsidian/` y los futuros directorios técnicos de plugins.
- Preservar el historial de cada documento mediante `git mv`; no copiar ni recrear archivos para migrarlos.
- No clasificar ni mover documentos sin aprobación humana por bloques.
- Mantener la ortografía española en toda documentación nueva o modificada.

---

## Estructura de archivos prevista

| Ruta | Responsabilidad |
| --- | --- |
| `.pcs/decisiones/DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian.md` | Formalizar la decisión de implantar el diseño. |
| `.pcs/acciones/ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian.md` | Seguir la ejecución por bloques y sus criterios de cierre. |
| `.gitignore` | Ignorar la nueva configuración de Obsidian y los directorios técnicos futuros. |
| `docs/templates/TEMPLATE_DOCUMENTO_SUSTITUIBLE.md` | Template YAML del ciclo documental ligero. |
| `docs/templates/TEMPLATE_COMPONENTE_VERSIONABLE.md` | Template YAML para componentes funcionales con versión. |
| `docs/trabajo-en-curso/diseno/2026-07-18-mapa-clasificacion-documental.md` | Inventario aprobado de origen, destino, estado, motivo y enlaces de cada documento. |
| `docs/producto/` | Documentación viva de definición de producto y versionado. |
| `docs/metodologia/` | Conceptos, métodos, patrones, fricciones y playbooks vivos. |
| `docs/evidencias/` | Ejemplos y entrevistas piloto vivos. |
| `docs/fuentes/` | Fuentes e investigación vivas. |
| `docs/trabajo-en-curso/` | Ideas, debates, diseños, decisiones pendientes y ejecución. |
| `historico/` | Documentación superada, conservando su ruta de procedencia. |

## Task 1: Formalizar gobernanza y proteger el punto de partida

**Files:**
- Create: `.pcs/decisiones/DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian.md`
- Create: `.pcs/acciones/ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian.md`
- Modify: `.pcs/sesiones/sesion-20260717-1930-debate-obsidian-proyecto-completo.md`
- Modify: `.pcs/estado/estado-actual.md`

**Consumes:** La especificación `docs/superpowers/specs/2026-07-18-reorganizacion-documental-obsidian-design.md` aprobada por la persona responsable.

**Produces:** Una decisión PCS vigente y una acción ejecutable que autorizan exclusivamente el inventario, la copia externa, la configuración limpia y la migración por bloques validada.

- [ ] **Step 1: Resolver los cambios ajenos ya presentes en el árbol de trabajo**

Ejecutar:

```powershell
git status --short
git diff -- .pcs/estado/estado-actual.md
git diff -- boveda-entrevista-profesional/07_playbook/PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_0.md
```

Esperado: identificar qué cambios deben formar parte de la línea base antes de crear un espacio de trabajo aislado. No mover documentos mientras queden cambios cuyo propietario o destino no esté confirmado.

- [ ] **Step 2: Crear la decisión PCS a partir de la entidad canónica**

Crear la decisión con el identificador `DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian`. Debe declarar: configuración nueva en raíz, copia externa antes de borrar, retirada de las cinco rutas heredadas, migración con Git por bloques aprobados y prohibición de usar Obsidian CLI.

La decisión debe enlazar la especificación aprobada, la sesión de debate y la acción de esta tarea. Debe distinguir la decisión de implantación de cada aprobación posterior de clasificación.

- [ ] **Step 3: Crear la acción PCS de implantación**

Crear `ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian.md` con estos criterios de cierre verificables:

```text
- Copia externa completa verificada.
- No quedan configuraciones Obsidian anidadas.
- Bóveda raíz inicializada y Hide Folders configurado manualmente.
- Mapa de clasificación aprobado por bloques.
- Movimientos Git y enlaces verificados para todos los bloques aprobados.
- Histórico separado y rutas técnicas excluidas de la navegación.
```

- [ ] **Step 4: Actualizar la sesión y el estado PCS**

En la sesión, enlazar la decisión, la acción y la especificación. En `estado-actual.md`, registrar la implantación como acción abierta sin afirmar que ya se han movido archivos o eliminado configuraciones.

- [ ] **Step 5: Verificar la gobernanza antes de seguir**

Ejecutar:

```powershell
rg -n 'DEC-20260718-1700-001|ACC-20260718-1700-001|reorganizacion-documental-obsidian' .pcs
git diff --check -- .pcs
```

Esperado: la decisión, acción, sesión y estado se enlazan de forma coherente; no hay errores de espacios en los archivos PCS modificados.

- [ ] **Step 6: Commit**

```powershell
git add -- .pcs/decisiones/DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian.md .pcs/acciones/ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian.md .pcs/sesiones/sesion-20260717-1930-debate-obsidian-proyecto-completo.md .pcs/estado/estado-actual.md
git commit -m "docs(pcs): adopta reorganización documental de Obsidian"
```

## Task 2: Crear copia completa externa y retirar el entorno heredado

**Files:**
- Delete: `boveda-entrevista-profesional/.obsidian/`
- Delete: `boveda-entrevista-profesional/.obsidian-agent/`
- Delete: `boveda-entrevista-profesional/.vault-operator/`
- Delete: `obsilo-shared/`
- Delete: `vault-operator-shared/`

**Consumes:** Acción PCS abierta y decisión vigente de la tarea 1.

**Produces:** Un repositorio sin bóvedas anidadas ni datos de plugins heredados, restaurable mediante una copia completa externa verificada.

- [ ] **Step 1: Cerrar Obsidian y crear la copia completa externa**

La persona responsable cierra Obsidian y copia por completo `C:\Users\gusve\Documents\Apps\carrera-profesional-ai-first` a una carpeta hermana de respaldo con marca temporal, fuera del repositorio de trabajo.

Ejemplo de destino: `C:\Users\gusve\Documents\Apps\backups\carrera-profesional-ai-first-20260718-antes-obsidian`.

- [ ] **Step 2: Verificar que la copia contiene las cinco rutas heredadas**

Ejecutar sobre la copia externa:

```powershell
$backup='C:\Users\gusve\Documents\Apps\backups\carrera-profesional-ai-first-20260718-antes-obsidian'
@(
  'boveda-entrevista-profesional/.obsidian',
  'boveda-entrevista-profesional/.obsidian-agent',
  'boveda-entrevista-profesional/.vault-operator',
  'obsilo-shared',
  'vault-operator-shared'
) | ForEach-Object {
  if(-not (Test-Path (Join-Path $backup $_))){ throw "Falta en la copia: $_" }
}
'BACKUP_VERIFIED'
```

Esperado: `BACKUP_VERIFIED`.

- [ ] **Step 3: Solicitar confirmación humana inmediatamente antes de borrar**

Mostrar las cinco rutas y confirmar que la copia externa verificada es el punto de restauración. No ejecutar el borrado sin esa confirmación específica.

- [ ] **Step 4: Eliminar exclusivamente las cinco rutas aprobadas**

Ejecutar desde la raíz del repositorio:

```powershell
$targets=@(
  (Resolve-Path 'boveda-entrevista-profesional/.obsidian'),
  (Resolve-Path 'boveda-entrevista-profesional/.obsidian-agent'),
  (Resolve-Path 'boveda-entrevista-profesional/.vault-operator'),
  (Resolve-Path 'obsilo-shared'),
  (Resolve-Path 'vault-operator-shared')
)
$targets | ForEach-Object { Remove-Item -LiteralPath $_ -Recurse -Force }
```

- [ ] **Step 5: Verificar que no queda configuración anidada**

Ejecutar:

```powershell
rg --files -g '.obsidian' -g '.obsidian-agent' -g '.vault-operator' -g 'obsilo-shared' -g 'vault-operator-shared'
Test-Path 'boveda-entrevista-profesional/.obsidian'
```

Esperado: ningún directorio heredado encontrado y `False` para la antigua `.obsidian/`.

## Task 3: Preparar la estructura, los templates y la política Git

**Files:**
- Modify: `.gitignore`
- Create: `docs/templates/TEMPLATE_DOCUMENTO_SUSTITUIBLE.md`
- Create: `docs/templates/TEMPLATE_COMPONENTE_VERSIONABLE.md`
- Create: `docs/producto/.gitkeep`
- Create: `docs/metodologia/.gitkeep`
- Create: `docs/evidencias/.gitkeep`
- Create: `docs/fuentes/.gitkeep`
- Create: `docs/trabajo-en-curso/ideas/.gitkeep`
- Create: `docs/trabajo-en-curso/debates/.gitkeep`
- Create: `docs/trabajo-en-curso/diseno/.gitkeep`
- Create: `docs/trabajo-en-curso/decisiones-pendientes/.gitkeep`
- Create: `docs/trabajo-en-curso/ejecucion/.gitkeep`
- Create: `historico/.gitkeep`

**Consumes:** El entorno heredado ha sido retirado y hay una copia externa verificada.

**Produces:** La estructura destino existe, Git ignora las configuraciones nuevas y los dos ciclos documentales tienen templates reutilizables.

- [ ] **Step 1: Sustituir las reglas de configuración heredada en `.gitignore`**

El bloque final de `.gitignore` debe ser exactamente:

```gitignore
.obsidian/
.obsidian-agent/
.vault-operator/
vault-operator-shared/
obsilo-shared/
.playwright-cli/
.worktrees/
.tmp/
```

Eliminar las tres rutas específicas de `boveda-entrevista-profesional/` y la línea duplicada de `vault-operator-shared/`.

- [ ] **Step 2: Crear el template de documento sustituible**

Crear `docs/templates/TEMPLATE_DOCUMENTO_SUSTITUIBLE.md` con este frontmatter y cuerpo:

```markdown
---
id:
titulo:
estado_documental: borrador
fecha_actualizacion:
decision_autorizadora:
sustituido_por:
---

# [Título]

## Propósito

## Contenido

## Trazabilidad
```

- [ ] **Step 3: Crear el template de componente versionable**

Crear `docs/templates/TEMPLATE_COMPONENTE_VERSIONABLE.md` con este frontmatter y cuerpo:

```markdown
---
id:
titulo:
version: "0.1.0"
estado: borrador
decision_autorizadora:
sustituye:
---

# [Título]

## Contrato

## Criterio de validación

## Evidencia

## Trazabilidad
```

- [ ] **Step 4: Crear los directorios destino vacíos**

Ejecutar:

```powershell
$folders=@(
  'docs/producto','docs/metodologia','docs/evidencias','docs/fuentes',
  'docs/trabajo-en-curso/ideas','docs/trabajo-en-curso/debates',
  'docs/trabajo-en-curso/diseno','docs/trabajo-en-curso/decisiones-pendientes',
  'docs/trabajo-en-curso/ejecucion','historico'
)
$folders | ForEach-Object { New-Item -ItemType Directory -Force $_ | Out-Null }
```

Crear un `.gitkeep` vacío dentro de cada directorio listado en la sección **Files**.

- [ ] **Step 5: Verificar exclusiones y templates**

Ejecutar:

```powershell
git check-ignore -v .obsidian/app.json .vault-operator/data.json .playwright-cli/state.json
rg -n 'estado_documental: borrador|version: "0.1.0"|Criterio de validación' docs/templates
git diff --check -- .gitignore docs/templates
```

Esperado: las tres rutas técnicas están ignoradas y los dos templates contienen los campos requeridos sin errores de formato.

- [ ] **Step 6: Commit**

```powershell
git add -- .gitignore docs/templates docs/producto docs/metodologia docs/evidencias docs/fuentes docs/trabajo-en-curso historico
git commit -m "docs: prepara estructura documental objetivo"
```

## Task 4: Inicializar y validar manualmente la bóveda raíz

**Files:**
- Create (ignorado): `.obsidian/`

**Consumes:** No existen configuraciones Obsidian anidadas y `.gitignore` ya protege la nueva configuración.

**Produces:** Una única bóveda limpia en la raíz, configurada manualmente con Hide Folders.

- [ ] **Step 1: Abrir manualmente la raíz como nueva bóveda**

En Obsidian Desktop, elegir **Open folder as vault** y seleccionar `C:\Users\gusve\Documents\Apps\carrera-profesional-ai-first`.

Esperado: Obsidian crea únicamente `C:\Users\gusve\Documents\Apps\carrera-profesional-ai-first\.obsidian\`.

- [ ] **Step 2: Instalar y habilitar Hide Folders**

Desde la configuración de plugins comunitarios de Obsidian, instalar **Hide Folders** y habilitarlo.

- [ ] **Step 3: Pegar la lista acordada de carpetas excluidas**

En **Hide Folders → Folders to hide**, pegar exactamente:

```text
.agents
.codex
.git
.obsidian
.obsidian-agent
.vault-operator
.playwright-cli
.tmp
.worktrees
historico
obsilo-shared
vault-operator-shared
```

Activar **Add hidden folders to Obsidian exclusion-list**.

- [ ] **Step 4: Validar visualmente y por búsqueda**

La persona responsable confirma que `README.md`, `AGENTS.md`, `docs/` y `.pcs/` son visibles. Confirmar que las rutas de la lista no aparecen en el explorador, la búsqueda, el grafo ni las sugerencias de enlaces.

- [ ] **Step 5: Verificar que Git no registra la configuración nueva**

Ejecutar:

```powershell
git check-ignore -v .obsidian/app.json .obsidian/plugins/hide-folders/data.json
git status --short -- .obsidian
```

Esperado: `git check-ignore` identifica `.gitignore` y `git status` no muestra archivos de `.obsidian/`.

## Task 5: Elaborar y aprobar el mapa de clasificación completo

**Files:**
- Create: `docs/trabajo-en-curso/diseno/2026-07-18-mapa-clasificacion-documental.md`

**Consumes:** Directorios destino creados y bóveda raíz validada.

**Produces:** Un mapa completo, aprobado por bloques, que permite migrar sin inferir destinos documentales.

- [ ] **Step 1: Generar el inventario de Markdown candidato**

Ejecutar:

```powershell
$excluded='(^|\\)(\.obsidian|\.obsidian-agent|\.vault-operator|\.git|\.worktrees|\.tmp|node_modules)(\\|$)'
rg --files -g '*.md' | Where-Object { $_ -notmatch $excluded } | Sort-Object
```

Esperado: el inventario incluye README, AGENTS, `docs/`, `.pcs/` y los documentos vivos de la antigua bóveda, sin configuraciones técnicas.

- [ ] **Step 2: Crear el mapa con una fila por documento reubicable**

El documento debe tener esta tabla:

```markdown
| Origen | Destino propuesto | Estado | Motivo | Enlaces que revisar | Aprobación |
| --- | --- | --- | --- | --- | --- |
```

Usar `vigente`, `historico` o `sin_mover` en la columna **Estado**. Todo documento bajo `.pcs/` debe usar `sin_mover`.

- [ ] **Step 3: Clasificar y revisar por estos bloques, en este orden**

```text
1. docs existentes y archivos raíz de orientación.
2. Propósito, conceptos, métodos, roles y patrones de la bóveda.
3. Fricciones, antipatrones, ejemplos y entrevistas piloto.
4. Playbooks y definiciones MVP.
5. Fuentes, artefactos de cobertura y templates de la bóveda.
6. Versiones históricas y documentos sustituidos.
```

Tras completar cada bloque, pedir aprobación humana antes de marcar sus filas como `aprobado`.

- [ ] **Step 4: Identificar los destinos de wikilinks ambiguos**

El mapa debe decidir una fuente viva para estos tres nombres y señalar el wikilink con ruta necesario:

```text
idea-central
Análisis estructural de la reconstrucción de trayectorias profesionales
Narrative career counseling - My career story and pictorial narratives
```

- [ ] **Step 5: Verificar que el mapa no tiene documentos sin clasificación**

Ejecutar:

```powershell
$map='docs/trabajo-en-curso/diseno/2026-07-18-mapa-clasificacion-documental.md'
rg -n '\|.*\|.*\|\s*\|.*\|.*\|' $map
rg -n 'pendiente|por decidir|sin clasificar' $map
```

Esperado: no hay filas con destino o estado vacío, y no quedan expresiones de clasificación pendiente después de la aprobación de todos los bloques.

- [ ] **Step 6: Commit**

```powershell
git add -- docs/trabajo-en-curso/diseno/2026-07-18-mapa-clasificacion-documental.md
git commit -m "docs: clasifica migración documental de Obsidian"
```

## Task 6: Migrar los bloques aprobados y corregir enlaces

**Files:**
- Modify: Todos los Markdown con filas `aprobado` en `docs/trabajo-en-curso/diseno/2026-07-18-mapa-clasificacion-documental.md`
- Create: Rutas destino aprobadas bajo `docs/` y `historico/`
- Delete: Rutas origen aprobadas tras cada `git mv`

**Consumes:** Mapa completo aprobado por bloques.

**Produces:** Documentación viva bajo `docs/`, documentación superada bajo `historico/` y enlaces locales resueltos.

- [ ] **Step 1: Ejecutar solo los movimientos aprobados del primer bloque**

Para cada fila aprobada, usar el patrón:

```powershell
git mv -- 'ruta/origen.md' 'ruta/destino.md'
```

No mover `.pcs/`. No mezclar en un mismo commit documentos de bloques distintos.

- [ ] **Step 2: Corregir los enlaces que hayan perdido validez por la ruta nueva**

Mantener wikilinks simples cuando el nombre siga siendo único. Para los tres destinos ambiguos, usar estas rutas completas desde la raíz de la bóveda:

```markdown
[[docs/metodologia/conceptos/idea-central|idea central]]
[[docs/fuentes/Análisis estructural de la reconstrucción de trayectorias profesionales|Análisis estructural de la reconstrucción de trayectorias profesionales]]
[[docs/fuentes/Narrative career counseling - My career story and pictorial narratives|Narrative career counseling - My career story and pictorial narratives]]
```

No crear otras copias vivas con esos tres nombres.

- [ ] **Step 3: Verificar los enlaces Markdown relativos del bloque**

Ejecutar este verificador de solo lectura desde la raíz:

```powershell
$files = git diff --name-only -- '*.md'
foreach($path in $files){
  $file = Get-Item -LiteralPath $path
  $lineNo = 0
  foreach($line in Get-Content -LiteralPath $file.FullName){
    $lineNo++
    foreach($m in [regex]::Matches($line,'(?<!\!)\[[^\]]*\]\(([^\s\)]+)(?:\s+[^\)]*)?\)')){
      $target=$m.Groups[1].Value.Trim('<>')
      if($target -match '^(https?:|mailto:|tel:|data:|ftp:|obsidian:|#)'){continue}
      $candidate=Join-Path $file.DirectoryName (($target -split '[#?]',2)[0] -replace '/','\\')
      if(-not (Test-Path -LiteralPath $candidate -PathType Leaf)){throw "Enlace roto: $path:$lineNo -> $target"}
    }
  }
}
'RELATIVE_LINKS_OK'
```

Esperado: `RELATIVE_LINKS_OK`.

- [ ] **Step 4: Verificar los wikilinks y los nombres ambiguos**

En Obsidian, revisar **Unresolved links**, backlinks y grafo para el bloque. Confirmar que los tres nombres ambiguos usan rutas aprobadas y que no aparecen nuevas sugerencias técnicas u históricas.

- [ ] **Step 5: Revisar ortografía y diff del bloque**

Ejecutar:

```powershell
git diff --check
git diff --stat
git status --short
```

Releer toda la prosa española modificada y corregir tildes, eñes y puntuación antes del commit.

- [ ] **Step 6: Commit por bloque**

```powershell
$changed = @(git diff --name-only -- docs historico boveda-entrevista-profesional)
if($changed.Count -eq 0){ throw 'El bloque no contiene cambios documentales para registrar.' }
git add -- $changed
git commit -m "docs: migra bloque documental de Obsidian"
```

Repetir los pasos 1 a 6 para cada bloque aprobado del mapa.

## Task 7: Consolidar la migración y cerrar la acción PCS

**Files:**
- Modify: `.pcs/acciones/ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian.md`
- Modify: `.pcs/estado/estado-actual.md`
- Modify: `.pcs/sesiones/sesion-20260717-1930-debate-obsidian-proyecto-completo.md`
- Modify: `README.md`
- Modify: `AGENTS.md`
- Modify: `docs/AGENTS.md`

**Consumes:** Todos los bloques del mapa están migrados y verificados.

**Produces:** La nueva estructura queda documentada, la acción PCS se cierra con evidencia y la continuidad futura es recuperable.

- [ ] **Step 1: Ejecutar auditoría final de archivos Markdown**

Ejecutar:

```powershell
$excluded='(^|\\)(\.obsidian|\.obsidian-agent|\.vault-operator|\.git|\.worktrees|\.tmp|node_modules)(\\|$)'
$md=@(rg --files -g '*.md' | Where-Object { $_ -notmatch $excluded })
"MARKDOWN_RELEVANTES=$($md.Count)"
rg -n --glob '*.md' '\[\[[^\]]+\]\]' docs .pcs README.md AGENTS.md
```

Esperado: la documentación viva está en `docs/`, `.pcs/` conserva sus entidades y no se observan rutas técnicas en los resultados de navegación previstos.

- [ ] **Step 2: Confirmar los criterios de aceptación de la especificación**

Contrastar uno a uno los nueve criterios de `docs/superpowers/specs/2026-07-18-reorganizacion-documental-obsidian-design.md` contra evidencia directa: copia externa, ausencia de configuraciones anidadas, visibilidad de documentos, exclusiones, movimientos Git, enlaces, templates y ausencia de plugins heredados.

- [ ] **Step 3: Actualizar documentación de orientación**

Actualizar `README.md`, `AGENTS.md` y `docs/AGENTS.md` para que describan las nuevas rutas documentales sin duplicar la gobernanza de `.pcs/`.

- [ ] **Step 4: Cerrar la acción y consolidar PCS**

En la acción, registrar la evidencia de cada criterio de cierre. Actualizar la sesión como consolidada y usar `pcs::actualiza-estado` para proponer la actualización del estado operativo.

- [ ] **Step 5: Verificación final**

Ejecutar:

```powershell
git diff --check
git status --short
rg -n 'boveda-entrevista-profesional/.obsidian|boveda-entrevista-profesional/.vault-operator|vault-operator-shared|obsilo-shared' .gitignore README.md AGENTS.md docs .pcs
```

Esperado: no quedan referencias operativas obsoletas; cualquier referencia histórica está marcada como tal.

- [ ] **Step 6: Commit**

```powershell
$changed = @(git diff --name-only -- README.md AGENTS.md docs .pcs historico .gitignore)
if($changed.Count -eq 0){ throw 'No hay cambios de consolidación para registrar.' }
git add -- $changed
git commit -m "docs: consolida nueva arquitectura documental"
```

## Task 8: Evaluar plugins posteriores como iniciativa independiente

**Files:**
- Create: `docs/trabajo-en-curso/ideas/evaluacion-vault-operator-y-local-rest-api.md`

**Consumes:** La acción de reorganización está cerrada y la bóveda raíz funciona sin plugins heredados.

**Produces:** Una evaluación separada de Vault Operator y Local REST API MCP, sin contaminar ni reabrir la migración documental.

- [ ] **Step 1: Crear la nota de evaluación posterior**

Crear la nota con estos apartados:

```markdown
# Evaluación posterior de Vault Operator y Local REST API MCP

## Necesidad que resolvería cada plugin

## Datos y rutas que crearía

## Riesgos de privacidad y mantenimiento

## Prueba mínima reversible

## Decisión requerida
```

- [ ] **Step 2: Verificar separación de alcance**

Ejecutar:

```powershell
rg -n 'Vault Operator|Local REST API MCP' docs/trabajo-en-curso/ideas/evaluacion-vault-operator-y-local-rest-api.md
git status --short
```

Esperado: la evaluación existe como idea posterior y no instala ni configura plugins.

- [ ] **Step 3: Commit**

```powershell
git add -- docs/trabajo-en-curso/ideas/evaluacion-vault-operator-y-local-rest-api.md
git commit -m "docs: abre evaluación posterior de plugins Obsidian"
```

## Cobertura de la especificación

| Requisito de diseño | Tarea que lo materializa |
| --- | --- |
| Decisión y acción PCS previas | Task 1 |
| Copia completa y retirada previa del entorno heredado | Task 2 |
| `.gitignore`, estructura y templates | Task 3 |
| Configuración manual de Obsidian y Hide Folders | Task 4 |
| Clasificación humana por bloques | Task 5 |
| Movimientos Git y corrección de enlaces | Task 6 |
| Validación, orientación y cierre PCS | Task 7 |
| Plugins futuros fuera de alcance | Task 8 |
