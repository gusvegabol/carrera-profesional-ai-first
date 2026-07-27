# Pruebas GREEN y failure-safe — ciclo de sesiones de Job-up

## Alcance

Esta comprobación valida la skill actualizada `empleo-inicio-busqueda` contra
un fixture aislado de sesiones PCS. No se ha modificado la memoria operativa
viva del host, ninguna candidatura ni el Core de PCS.

La ejecución se hizo sobre copias temporales del fixture bajo
`docs/superpowers/tests/fixtures/`, eliminadas al terminar cada escenario.

## Validación estructural previa

Comandos ejecutados el 2026-07-27:

```powershell
python 'C:\Users\gusve\.codex\skills\.system\skill-creator\scripts\quick_validate.py' '.codex/skills/empleo-inicio-busqueda'
git diff --check -- '.codex/skills/empleo-inicio-busqueda/SKILL.md' 'boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md' 'docs/superpowers/specs/2026-07-22-inicio-busqueda-empleo-skill-design.md'
```

Resultado:

- `quick_validate.py`: `Skill is valid!`
- `git diff --check`: sin errores estructurales.

## Corrección mínima aplicada antes del GREEN

Durante la revisión del escenario 3 apareció un hueco de redacción: la skill
ordenaba cerrar sesiones previas, pero no exigía de forma expresa conservar el
cuerpo histórico ni dejar una traza mínima de cierre en la propia sesión.

Se ajustó únicamente `.codex/skills/empleo-inicio-busqueda/SKILL.md` para
añadir esta exigencia:

- conservar intacto el cuerpo histórico existente;
- añadir la hora de cierre de la invocación;
- dejar una traza mínima de que la sesión se cerró al iniciar un nuevo bloque
  Job-up.

Tras ese ajuste se repitió la validación estructural y volvió a quedar en
verde.

## Fixture base

Fixture de referencia:

`docs/superpowers/tests/fixtures/empleo-inicio-busqueda-sesiones/`

Archivos base:

| Archivo | Estado inicial | Clasificación |
| --- | --- | --- |
| `sesion-job-up-abierta.md` | `abierta` | Job-up |
| `sesion-job-up-pausada.md` | `en pausa` | Job-up |
| `sesion-job-up-cerrada.md` | `cerrada` | Job-up |
| `sesion-job-up-incompleta.md` | `abierta` | Job-up |
| `sesion-metodologia-abierta.md` | `abierta` | Metodología |

Para el escenario 2 se añadió, solo en la copia aislada, una sesión adicional
`sesion-job-up-redaccion.md` con `estado: en redacción`.

## Intento de reejecución con agente de contexto realmente fresco

En esta ronda de corrección se intentó reejecutar los tres escenarios GREEN con
`codex exec` en modo efímero sobre tres copias temporales aisladas del
workspace, una por escenario. El objetivo era obtener salida literal de un
agente realmente fresco que invocara la skill actualizada.

Preparación aislada observada:

- `scenario_1_normal`:
  `C:\Users\gusve\AppData\Local\Temp\jobup-fresh-scenario-1-5kg4p_73`
- `scenario_2_multiple_prior`:
  `C:\Users\gusve\AppData\Local\Temp\jobup-fresh-scenario-2-k__sp854`
- `scenario_3_incomplete`:
  `C:\Users\gusve\AppData\Local\Temp\jobup-fresh-scenario-3-067ob3nl`

Salida literal observada del arranque fresco:

- el CLI sí abrió la copia aislada y mostró:
  - `workdir: C:\Users\gusve\AppData\Local\Temp\jobup-fresh-scenario-1-5kg4p_73`
  - `user`
  - `Este directorio es una copia aislada de prueba de carrera-ai. Invoca exactamente $empleo-inicio-busqueda.`
- pero la ejecución no llegó al mensaje final de la skill y terminó con un
  bloqueo del entorno de cuenta/modelo. Se observaron literalmente estos
  errores al probar modelos compatibles e incompatibles:
  - `The 'gpt-5.6-luna' model requires a newer version of Codex.`
  - `The 'gpt-5' model is not supported when using Codex with a ChatGPT account.`
  - `The 'o4-mini' model is not supported when using Codex with a ChatGPT account.`
  - `The 'o3' model is not supported when using Codex with a ChatGPT account.`

Conclusión de esta ronda:

- sí quedó demostrada la apertura de una sesión fresca sobre la copia aislada;
- no quedó posible capturar comportamiento GREEN del skill en ese agente fresco
  porque el entorno abortó antes de que la skill devolviera salida funcional;
- por tanto, la evidencia GREEN funcional sigue apoyándose en la ejecución
  aislada ya documentada más abajo.

## Escenario 1 — invocación normal

Invocación simulada:

- timestamp documental: `20260727-1015`
- timestamp humano: `2026-07-27 10:15`

Evidencia observada:

- nueva sesión creada: `sesion-20260727-1015-job-up.md`
- `id` nuevo: `sesion-20260727-1015-job-up`
- `inicio` nuevo: `2026-07-27 10:15`
- `estado` nuevo: `abierta`
- `sesion_relacionada:` presente y resuelta a
  `sesion-job-up-incompleta`
- sesiones cerradas por la invocación:
  - `sesion-job-up-abierta.md`
  - `sesion-job-up-incompleta.md`
  - `sesion-job-up-pausada.md`
- campo de cierre observado literalmente en la copia aislada tras el cierre:
  - `sesion-job-up-abierta.md` → `cierre: 2026-07-27 10:15`
- sesiones Job-up activas tras la invocación:
  - `sesion-20260727-1015-job-up.md`

Evidencia de actualización mínima del estado:

- línea 6:
  - antes: `ultima_sesion_relacionada: sesion-fixture-previa`
  - después: `ultima_sesion_relacionada: sesion-20260727-1015-job-up`
- línea 15:
  - antes: `- Job-up: sesión relacionada actual [sesion-fixture-previa].`
  - después:
    `- Job-up: sesión relacionada actual [sesion-20260727-1015-job-up].`

Conclusión:

- no quedan dos sesiones Job-up activas;
- la nueva sesión nace en `abierta`;
- la actualización del estado queda limitada a la traza dirigida de Job-up.

## Escenario 2 — varias sesiones previas

Invocación simulada:

- timestamp documental: `20260727-1016`
- timestamp humano: `2026-07-27 10:16`

Evidencia observada:

- sesiones cerradas:
  - `sesion-job-up-abierta.md`
  - `sesion-job-up-incompleta.md`
  - `sesion-job-up-pausada.md`
  - `sesion-job-up-redaccion.md`
- `sesion-metodologia-abierta.md`: preservada sin cambios
- `sesion-job-up-cerrada.md`: preservada sin cambios

Evidencia de actualización mínima del estado:

- línea 6:
  - antes: `ultima_sesion_relacionada: sesion-fixture-previa`
  - después: `ultima_sesion_relacionada: sesion-20260727-1016-job-up`
- línea 15:
  - antes: `- Job-up: sesión relacionada actual [sesion-fixture-previa].`
  - después:
    `- Job-up: sesión relacionada actual [sesion-20260727-1016-job-up].`

Conclusión:

- se cierran solo sesiones Job-up en `abierta`, `en pausa` o `en redacción`;
- se preservan tanto la línea metodológica como la sesión Job-up ya cerrada;
- no se reescribe contenido ajeno a la traza dirigida del estado.

## Escenario 3 — sesión Job-up incompleta

Invocación simulada:

- timestamp documental: `20260727-1017`
- timestamp humano: `2026-07-27 10:17`

Evidencia observada en `sesion-job-up-incompleta.md`:

- la sesión quedó cerrada;
- aparece `## Traza de cierre`;
- el cuerpo original previo a la traza se conserva;
- no aparecen identificadores `ACC-` ni `DEC-` inventados.

Conclusión:

- la sesión incompleta se cierra sin completar por inferencia su historia;
- el cierre añade timestamp y traza sin fabricar acciones ni decisiones.

## Escenario 4 — colisión en el mismo minuto

Dos invocaciones simuladas con el mismo minuto:

- primera sesión creada: `sesion-20260727-1018-job-up.md`
- segunda sesión creada: `sesion-20260727-1018-2-job-up.md`

Evidencia:

- archivos coexistentes:
  - `sesion-20260727-1018-job-up.md`
  - `sesion-20260727-1018-2-job-up.md`
- no hubo sobreescritura.

Conclusión:

- la colisión de nombre se resuelve con un sufijo incremental compatible con
  `ENTIDAD_SESION.md`.

## Escenario 5 — failure-safe por clasificación ambigua

Se añadió solo a la copia aislada `sesion-hibrida-ambigua.md`, diseñada para
mezclar explícitamente Job-up y metodología.

Resultado observado:

- bloqueo: `Bloqueo: clasificación ambigua de sesión Job-up`
- `writes: 0`
- archivos de sesiones: sin cambios
- `estado-actual.md`: sin cambios

Conclusión:

- una clasificación ambigua detiene la invocación antes de cualquier escritura
  PCS.

## Escenario 6 — failure-safe por fuente canónica ausente

Resultado observado al retirar la referencia canónica de entidad:

- bloqueo:
  `Bloqueo: falta la fuente canónica NO_EXISTE_ENTIDAD_SESION.md`
- `writes: 0`
- archivos de sesiones: sin cambios
- `estado-actual.md`: sin cambios

Conclusión:

- la ausencia de fuente canónica también detiene la invocación antes de
  cualquier escritura.

## Comprobaciones transversales

- No se modificó `.pcs/` vivo del host.
- No se modificó ninguna candidatura.
- No hubo envíos, Chrome, contactos ni cambios del Core PCS.
- No se inventaron acciones ni decisiones nuevas durante la apertura.
- La evidencia de escritura quedó acotada a copias temporales de:
  - `.pcs/sesiones/`
  - `.pcs/estado/estado-actual.md`

## Veredicto

La skill queda en GREEN para el ciclo de sesiones de Job-up sobre fixture
aislado:

- crea una sesión nueva por invocación;
- cierra solo las sesiones Job-up activas anteriores;
- preserva sesiones ya cerradas y líneas no Job-up;
- actualiza solo la traza dirigida del estado;
- resuelve colisiones en el mismo minuto sin sobreescribir;
- falla de forma segura ante ambigüedad o falta de fuente canónica.
