# Integrar Job-up en main — Plan de ejecución

> **Para agentes de ejecución:** SUBSKILL REQUERIDA: usar `superpowers:executing-plans` para ejecutar este plan tarea por tarea con puntos de verificación.

**Objetivo:** integrar en `main` los materiales finales de Job-up conservando de forma reversible todos los cambios locales que ya existen en `main`.

**Arquitectura:** La rama `codex/job-up-candidatura-espontanea` aporta el conjunto versionado de datos core enriquecidos, selección factual, CV, PDF, emails, especificación y plan. `main` conserva sus cambios locales mediante un stash con nombre antes del merge; después se restaura ese stash y se resuelven únicamente las coincidencias documentales necesarias.

**Tecnologías:** Git, Markdown, DOCX, PDF y validaciones estructurales ya disponibles en el worktree.

## Restricciones globales

- No ejecutar `git reset --hard`, `git checkout --`, `git clean` ni borrar directorios amplios.
- No perder ni sobrescribir los cambios locales actuales de `main`.
- El archivo `datos-core-busqueda-v3.md` del worktree ya cumplió su objetivo y puede eliminarse únicamente tras comprobar que la versión final de `datos-core-busqueda.md` contiene sus hechos necesarios.
- No integrar `docs/superpowers/plans/2026-07-22-cv-maestro-candidatura-espontanea.md`, que permanece como plan anterior no versionado.
- Mantener la experiencia municipal en el histórico factual, fuera del CV, PDF, selección factual y emails.
- No enviar ni compartir candidaturas ni realizar contactos externos.

---

### Task 1: Auditar y preparar la integración

**Archivos y estados:**
- Leer: `C:/Users/gusve/Documents/Apps/carrera-profesional-ai-first/.worktrees/codex-job-up-candidatura-espontanea/boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda.md`
- Leer: `C:/Users/gusve/Documents/Apps/carrera-profesional-ai-first/.worktrees/codex-job-up-candidatura-espontanea/boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda-v3.md`
- Leer: `C:/Users/gusve/Documents/Apps/carrera-profesional-ai-first/boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda.md`
- No modificar los archivos locales de `main` durante esta tarea.

**Pasos:**

- [ ] Comparar las tres versiones y comprobar que los hechos necesarios de la v3 están en la versión final del worktree: HER-04, HER-05, HER-06, escala de Herfrailes, mantenimiento de vehículos, Granintra y Certificación Universitaria.
- [ ] Confirmar que la v3 no contiene hechos únicos necesarios que falten en la versión final.
- [ ] Verificar que la skill `empleo-genera-cv-empresa` ya está confirmada en `main` y no requiere traslado desde el worktree.
- [ ] Eliminar únicamente el archivo exacto `...\.worktrees\codex-job-up-candidatura-espontanea\boveda-entrevista-profesional\busqueda-empleo\datos-core-busqueda-v3.md` después de la comprobación anterior.
- [ ] Confirmar que el plan anterior no versionado queda fuera de la integración.

### Task 2: Crear un respaldo reversible de main

**Estado afectado:** repositorio principal `C:/Users/gusve/Documents/Apps/carrera-profesional-ai-first`.

**Pasos:**

- [ ] Confirmar que `main` está en la rama `main` y registrar su commit actual.
- [ ] Confirmar que los cambios locales de `main` siguen presentes y no se han alterado desde la auditoría.
- [ ] Crear el stash `job-up-pre-integracion-main-20260722` con cambios rastreados y no rastreados mediante `git stash push -u -m "job-up-pre-integracion-main-20260722"`.
- [ ] Comprobar que el árbol de `main` queda limpio y que el stash contiene los cambios locales antes de continuar.

### Task 3: Integrar la rama de Job-up

**Ramas:**
- Base: `main`.
- Rama fuente: `codex/job-up-candidatura-espontanea`.

**Pasos:**

- [ ] Ejecutar `git merge --no-ff codex/job-up-candidatura-espontanea -m "merge: integra materiales finales de Job-up"` desde el repositorio principal.
- [ ] Si Git informa un conflicto, detenerse en el archivo concreto y resolver conservando la versión enriquecida de Job-up solo cuando el contenido anterior de `main` ya esté incluido; no resolver por descarte global.
- [ ] Confirmar que el merge incluye el CV DOCX, PDF, emails, selección factual, datos core, especificación y plan de Job-up.
- [ ] Confirmar que la skill `empleo-genera-cv-empresa` permanece en `main`.

### Task 4: Restaurar y reconciliar los cambios locales de main

**Estado afectado:** stash `job-up-pre-integracion-main-20260722`.

**Pasos:**

- [ ] Ejecutar `git stash pop` y registrar si la restauración es limpia o produce conflictos.
- [ ] Si hay conflicto en `datos-core-busqueda.md`, conservar los hechos enriquecidos de la rama integrada y comprobar que permanecen las correcciones anteriores de main.
- [ ] Resolver cualquier otro conflicto examinando archivo por archivo; no usar comandos destructivos ni descartar cambios completos.
- [ ] Comprobar que los cambios no relacionados de main siguen presentes como modificaciones locales o archivos no rastreados.
- [ ] Mantener el stash hasta confirmar que el árbol restaurado y los documentos integrados son correctos; eliminarlo solo después de una verificación explícita de recuperación.

### Task 5: Verificación final en main

**Pasos:**

- [ ] Comprobar que el CV DOCX y PDF existen, que el PDF tiene dos páginas y que el texto corresponde al DOCX.
- [ ] Comprobar que los tres modelos de email están presentes y usan los tratamientos acordados.
- [ ] Buscar en CV, PDF, selección y emails referencias a `Gáldar`, `Ayuntamiento`, `Concejal`, `GAL-01`, gestión pública, parentescos y conflictos sensibles; no debe haber coincidencias candidatables.
- [ ] Confirmar en datos core las correcciones de mantenimiento de vehículos, Granintra y Certificación Universitaria.
- [ ] Confirmar que `empleo-genera-cv-empresa` está en `main` y que exige investigación pública, fuentes, revisión humana y estado no enviado.
- [ ] Ejecutar `git diff --check` sobre los cambios integrados y revisar el estado final de `main`.
- [ ] Mantener el worktree y la rama fuente como respaldo hasta que el usuario confirme que desea retirarlos; no usar `git worktree remove --force`.
