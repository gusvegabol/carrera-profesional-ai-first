# Informe Task 1 — Actualizar el diseño funcional y fijar el contrato de sesión

## Resumen

Se ha actualizado `docs/superpowers/specs/2026-07-22-inicio-busqueda-empleo-skill-design.md` para reflejar el nuevo ciclo de vida documental de `$empleo-inicio-busqueda` antes de la implementación de la skill.

## Archivos modificados

- `docs/superpowers/specs/2026-07-22-inicio-busqueda-empleo-skill-design.md`
- `.superpowers/sdd/2026-07-27-actualizar-inicio-busqueda-empleo-sesiones-pcs/task-1-report.md`

## Fuentes leídas

- `C:/Users/gusve/Documents/Apps/project-continuity-system/core/ENTIDAD_SESION.md`
- `C:/Users/gusve/Documents/Apps/project-continuity-system/templates/TEMPLATE_SESION.md`
- `.pcs/estado/estado-actual.md`
- `docs/AGENTS.md`
- `README.md`
- `AGENTS.md`
- `.superpowers/sdd/2026-07-27-actualizar-inicio-busqueda-empleo-sesiones-pcs/task-1-brief.md`

No se encontró `./.pcs/sesiones/sesion-20260727-2109-busqueda-empleo.md` en el worktree, por lo que la tarea se resolvió con las demás fuentes requeridas disponibles.

## Cambios aplicados

1. Se registró la línea base RED: la skill actual solo rehidrata y responde; no crea sesión, no registra la hora de invocación y no cierra sesiones previas de Job-up.
2. Se sustituyó el contrato de “inicio sin escrituras” por un contrato acotado de escritura solo en `.pcs/sesiones/` y `.pcs/estado/estado-actual.md`.
3. Se fijó la selección de sesiones Job-up: identificación explícita por frontmatter, título o contenido, y cierre limitado a estados `abierta`, `en pausa` y `en redacción`.
4. Se documentó el orden transaccional: resolver marca temporal y nombre, identificar y validar objetivos, cerrar sesiones previas, crear la nueva sesión y actualizar el estado; si falla la validación previa, no se escribe nada.
5. Se reforzaron los límites: sin cambios en Core PCS, metodología, ESCO, investigación GitHub, candidaturas, Chrome o contactos externos.
6. Se revisó la ortografía y la consistencia terminológica del documento en español.

## Validaciones ejecutadas

### 1. Revisión del diff

Comando:

```powershell
git -C 'C:/Users/gusve/Documents/Apps/carrera-profesional-ai-first/.worktrees/codex-actualizar-job-up-sesiones' diff -- 'docs/superpowers/specs/2026-07-22-inicio-busqueda-empleo-skill-design.md'
```

Resultado:

- El diff muestra únicamente la ampliación del diseño funcional con la línea base RED, el nuevo contrato de escritura, la selección de sesiones Job-up, el orden transaccional y la actualización de criterios de aceptación.

### 2. Comprobación de espacios y formato Git

Comando:

```powershell
git -C 'C:/Users/gusve/Documents/Apps/carrera-profesional-ai-first/.worktrees/codex-actualizar-job-up-sesiones' diff --check -- 'docs/superpowers/specs/2026-07-22-inicio-busqueda-empleo-skill-design.md'
```

Resultado:

- Sin errores de espacios o formato bloqueantes.
- Git avisó de normalización `LF -> CRLF` en el worktree de Windows, sin impedir la validación.

### 3. Comprobación rápida de cobertura textual

Comando:

```powershell
rg -n "Línea base RED|Contrato funcional de escritura|Selección de sesiones Job-up|Orden transaccional y preflight|\.pcs/sesiones/|en redacción|acciones externas" 'C:/Users/gusve/Documents/Apps/carrera-profesional-ai-first/.worktrees/codex-actualizar-job-up-sesiones/docs/superpowers/specs/2026-07-22-inicio-busqueda-empleo-skill-design.md'
```

Resultado:

- Confirmadas las secciones y frases clave del brief dentro del documento final.

### 4. Estado del worktree antes del commit

Comando:

```powershell
git -C 'C:/Users/gusve/Documents/Apps/carrera-profesional-ai-first/.worktrees/codex-actualizar-job-up-sesiones' status --short
```

Resultado:

- Detectado un archivo ajeno sin seguimiento: `docs/superpowers/plans/2026-07-27-actualizar-inicio-busqueda-empleo-sesiones-pcs.md`.
- Se ha dejado fuera del commit para no mezclar cambios no solicitados con Task 1.

## Autoevaluación

- El diseño actualizado cubre los cinco requisitos del brief.
- La referencia a la entidad y la plantilla canónica de sesión queda integrada en el propio contrato funcional, sin modificar PCS Core.
- El documento mantiene la separación entre continuidad PCS, rama Job-up y límites externos.
- No se han introducido cambios de implementación ni escrituras en `.pcs/`.

## Incidencias o preocupaciones

- `git diff --check` emitió un aviso de finales de línea `LF -> CRLF`, pero no reportó errores de formato.
- La sesión fuente opcional `sesion-20260727-2109-busqueda-empleo.md` no estaba presente en el worktree.
