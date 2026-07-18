# Diseño: reorganización documental y nueva bóveda Obsidian

**Fecha:** 2026-07-18
**Estado:** aprobado para planificación; pendiente de formalización PCS antes de ejecutar movimientos o eliminaciones.
**Sesión relacionada:** `sesion-20260717-1930-debate-obsidian-proyecto-completo`

## Decisión de diseño

Carrera AI adoptará una única bóveda de Obsidian en la raíz del repositorio, con una configuración nueva y limpia. La implantación se realizará por bloques, con clasificación humana previa y movimientos trazables mediante Git.

La configuración heredada de Obsidian y sus datos asociados no se migrarán. Se eliminarán antes de crear la nueva bóveda, después de que exista una copia completa y verificable del repositorio fuera de la carpeta de trabajo.

La persona responsable realizará manualmente la inicialización de la bóveda y la configuración de Obsidian. No se utilizará Obsidian CLI.

## Objetivos

- Facilitar la lectura, búsqueda y navegación de toda la documentación viva del proyecto desde una única bóveda.
- Separar de forma visible la documentación viva, los debates en curso, la continuidad PCS y el histórico.
- Evitar que configuraciones, plugins y datos heredados condicionen la nueva arquitectura.
- Mantener la trazabilidad de los documentos y permitir la restauración completa ante un fallo.
- Reducir el coste recurrente de reubicar documentación canónica al evolucionar el proyecto.

## Límites de autoridad

- `.pcs/` conserva su nombre, estructura, entidades y gobernanza. No se renombra ni se integra bajo `docs/`.
- Obsidian es una superficie de lectura y navegación; no altera la autoridad de PCS, del SPEC, del versionado funcional ni de los playbooks.
- Un debate sustantivo vive en `docs/trabajo-en-curso/`. La sesión PCS correspondiente conserva contexto, trazabilidad y enlaces, sin duplicar el análisis.
- La aprobación de este diseño no sustituye la decisión PCS que deba formalizar su implantación ni crea por sí misma una acción de ejecución.

## Estructura objetivo

```text
carrera-profesional-ai-first/
├─ README.md
├─ AGENTS.md
├─ docs/
│  ├─ producto/
│  ├─ metodologia/
│  │  ├─ conceptos/
│  │  ├─ metodos/
│  │  ├─ patrones/
│  │  ├─ fricciones-y-antipatrones/
│  │  └─ playbooks/
│  ├─ evidencias/
│  │  ├─ ejemplos/
│  │  └─ entrevistas-piloto/
│  ├─ fuentes/
│  └─ trabajo-en-curso/
│     ├─ ideas/
│     ├─ debates/
│     ├─ diseno/
│     ├─ decisiones-pendientes/
│     └─ ejecucion/
├─ .pcs/
├─ historico/
│  └─ [ruta de procedencia del documento archivado]
├─ .obsidian/
├─ .agents/
├─ .codex/
├─ .playwright-cli/
├─ .tmp/
└─ .worktrees/
```

La actual carpeta `boveda-entrevista-profesional/` dejará de ser un área viva independiente. Sus documentos vigentes se clasificarán en las áreas estables de `docs/`; los superados pasarán a `historico/` y conservarán su ruta de procedencia.

Ejemplo de conservación de procedencia:

```text
historico/boveda-entrevista-profesional/07_playbook/
  PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_1.md
```

## Ciclo de vida documental

Los componentes funcionales, como los playbooks, reutilizarán el modelo de versionado funcional vigente en Carrera AI: versión semántica, estado, contrato, evidencia y decisión asociada.

Los documentos sustituibles que no sean componentes usarán un ciclo ligero con un template YAML que declare su estado documental, fecha, decisión que autoriza el cambio y relación de sustitución cuando exista.

Un documento puede nacer como no versionable. Solo pasará a ser versionable o sustituible tras una decisión explícita; en ese momento adoptará el template que corresponda.

Una versión posterior identifica una candidata a archivo, pero el traslado a `historico/` requiere confirmación humana y la decisión o el estado documental aplicable.

## Configuración nueva de Obsidian

Antes de inicializar la bóveda raíz, no puede existir una configuración `.obsidian/` dentro de una subcarpeta del repositorio. Mantenerla crearía una bóveda anidada y un contexto de configuración duplicado.

La nueva bóveda se creará manualmente en la raíz con Obsidian y el plugin *Hide Folders*. No se instalarán inicialmente Vault Operator ni Local REST API MCP.

La nueva `.obsidian/` y las configuraciones de sus plugins se ignorarán en Git. Durante la implantación se actualizará `.gitignore` para sustituir las rutas heredadas por las rutas técnicas de la bóveda raíz. La configuración se conservará mediante la copia completa externa, no mediante el repositorio.

En *Hide Folders* se configurará una carpeta por línea:

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

También se activará la opción que añade las carpetas ocultas a la lista de exclusión de Obsidian. Así no aparecerán en el explorador, búsqueda, grafo ni sugerencias de enlaces.

`.pcs/` se mostrará íntegra, incluidas las sesiones.

## Retirada del entorno heredado y copia de seguridad

Con Obsidian cerrado, la persona responsable creará una copia completa de la carpeta `carrera-ai` fuera de la carpeta de trabajo. Esa copia será el punto de restauración y deberá verificarse antes de cualquier eliminación.

Una vez validada la copia y antes de abrir la raíz como nueva bóveda, se eliminarán las rutas heredadas:

```text
boveda-entrevista-profesional/.obsidian/
boveda-entrevista-profesional/.obsidian-agent/
boveda-entrevista-profesional/.vault-operator/
obsilo-shared/
vault-operator-shared/
```

Las futuras instalaciones de Vault Operator y Local REST API MCP serán nuevas y se evaluarán después de consolidar la estructura documental.

## Migración por bloques

1. Formalizar la decisión PCS y abrir la acción de implantación.
2. Preparar un mapa completo de clasificación, con destino, estado, motivo, ruta final y necesidad de corrección de enlaces para cada bloque.
3. Obtener aprobación humana de cada bloque antes de mover documentos.
4. Crear y validar la copia completa; retirar el entorno heredado; inicializar manualmente la bóveda raíz y *Hide Folders*.
5. Mover los documentos aprobados con Git, sin copiar ni recrear archivos.
6. Corregir enlaces afectados y verificar enlaces, backlinks, autoridad documental y ortografía después de cada bloque.
7. Crear los templates documentales, actualizar índices y verificar la estructura final.
8. Evaluar por separado la instalación limpia de plugins adicionales.

## Enlaces

Los wikilinks simples existentes no necesitan reescribirse por el mero movimiento si conservan un nombre de archivo único. La auditoría inicial identificó tres destinos con colisión potencial al ampliar la bóveda: `idea-central`, `Análisis estructural de la reconstrucción de trayectorias profesionales` y `Narrative career counseling - My career story and pictorial narratives`.

Para cada destino ambiguo se decidirá una fuente viva y se usará un wikilink con ruta. También se revisarán los enlaces Markdown relativos que queden afectados por los movimientos de documentos.

## Beneficio, coste y riesgo

La base de trabajo contiene 99 Markdown relevantes: 70 de la bóveda de entrevista, 27 en `docs/` y 2 en la raíz. La migración no es un mero cambio de configuración: requiere clasificar, mover y comprobar la documentación.

| Factor | Valoración |
| --- | ---: |
| Beneficio | 5/5 |
| Coste inicial | 3/5 |
| Coste recurrente | 1/5 |
| Riesgo residual con salvaguardas | 2/5 |

El cálculo preliminar es `5 - 3 = +2`. Se considera viable y con coste aceptable porque el esfuerzo se concentra en una única reorganización controlada y reduce la complejidad recurrente de la documentación y de las configuraciones heredadas.

## Criterios de aceptación

- Existe una única `.obsidian/` en la raíz del repositorio y no quedan configuraciones de Obsidian anidadas.
- La copia completa externa permite restaurar el proyecto antes de que se retire el entorno heredado.
- `docs/`, `.pcs/`, `README.md` y `AGENTS.md` se consultan desde la bóveda raíz.
- Las rutas técnicas, compartidas y `historico/` permanecen excluidas de la navegación, búsqueda, grafo y sugerencias de enlaces.
- Cada documento migrado tiene un destino aprobado, una trazabilidad Git comprobable y enlaces locales resueltos.
- Los tres destinos inicialmente ambiguos tienen una resolución inequívoca.
- Los documentos versionables y sustituibles usan el template que corresponda.
- No se instala Vault Operator ni Local REST API MCP antes de consolidar la estructura.
- La documentación modificada supera una revisión ortográfica española explícita.

## Fuera de alcance

- Migrar configuraciones, plugins, historiales o datos de la bóveda anterior.
- Instalar Vault Operator o Local REST API MCP durante la reorganización documental.
- Alterar la estructura o gobernanza de `.pcs/`.
- Eliminar documentación sin una clasificación aprobada y sin la copia completa recuperable.
