# Task 2 report — fixture y prueba RED de ciclo de sesiones

## Alcance ejecutado

Se completó la tarea 2 del brief sin modificar la skill local, sin tocar la
PCS viva y sin intervenir en candidaturas, Core PCS ni documentos operativos
fuera del paquete de prueba solicitado.

## Artefactos creados

- `docs/superpowers/tests/2026-07-27-empleo-inicio-busqueda-sesiones.md`
- `docs/superpowers/tests/fixtures/empleo-inicio-busqueda-sesiones/sesion-job-up-abierta.md`
- `docs/superpowers/tests/fixtures/empleo-inicio-busqueda-sesiones/sesion-job-up-pausada.md`
- `docs/superpowers/tests/fixtures/empleo-inicio-busqueda-sesiones/sesion-job-up-cerrada.md`
- `docs/superpowers/tests/fixtures/empleo-inicio-busqueda-sesiones/sesion-metodologia-abierta.md`

## Diseño del fixture

El fixture contiene cuatro sesiones Markdown mínimas:

1. una sesión Job-up abierta;
2. una sesión Job-up en pausa;
3. una sesión Job-up cerrada;
4. una sesión metodológica abierta que no pertenece a Job-up.

Las dos primeras incluyen referencia explícita a Job-up y `sesion_relacionada`.
La sesión metodológica deja claro que no es Job-up y sirve como exclusión
positiva para los cierres automáticos.

## Prueba RED documentada

El log de prueba registra tres escenarios RED contra la versión actual de la
skill:

1. invocación normal bajo presión de tiempo;
2. invocación con varias sesiones previas;
3. sesión previa parcialmente documentada.

En los tres casos se deja trazado que la versión actual rehidrata, lee el punto
de entrada, confirma Job-up y responde, pero no crea una nueva sesión fechada,
no cierra sesiones previas, no toca la sesión metodológica y mantiene la
prohibición de escrituras PCS.

## Racionalización registrada

Se documentó la racionalización a evitar: tratar la creación de la nueva sesión
como una tarea manual para más tarde. El log la marca como insuficiente porque
no cumple el contrato transaccional de Job-up.

## Criterios GREEN dejados preparados

El final del log incluye la matriz de aceptación para la futura implementación:

- nombre de archivo con patrón `sesion-YYYYMMDD-HHMM-slug.md`;
- `id` alineado con el nombre base;
- `inicio` y timestamp coherentes;
- `estado: abierta`;
- cierre de sesiones Job-up previas con `cierre`;
- exclusión de la sesión metodológica no Job-up;
- actualización del puntero de estado;
- ausencia de nuevas acciones o decisiones PCS;
- ausencia de acciones externas.

## Verificación realizada

- Se revisó el contenido creado en el worktree aislado.
- Se comprobó que el diff visible contiene únicamente el paquete de prueba de
  esta tarea y un plan preexistente no tocado.
- No se modificó `.pcs/`, no se editó la skill y no se hicieron escrituras
  fuera del alcance del brief.

## Observaciones

- El archivo de plan mostrado por `git status` ya existía como un cambio sin
  seguir y no se incluyó en esta entrega.
- No se generó ninguna escritura PCS real; la entrega es exclusivamente un
  fixture y su log RED.

