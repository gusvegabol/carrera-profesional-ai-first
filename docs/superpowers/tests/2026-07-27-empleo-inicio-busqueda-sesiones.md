# Prueba RED — ciclo de sesiones de Job-up

## Objetivo

Documentar el comportamiento actual de `$empleo-inicio-busqueda` frente a un
fixture aislado de sesiones PCS, sin modificar la skill ni la memoria operativa
viva.

## Fixture aislado

Ruta:

`docs/superpowers/tests/fixtures/empleo-inicio-busqueda-sesiones/`

Archivos:

| Archivo | Estado | Propósito |
| --- | --- | --- |
| `sesion-job-up-abierta.md` | `abierta` | Sesión Job-up abierta con referencia a una sesión previa relacionada. |
| `sesion-job-up-pausada.md` | `en pausa` | Sesión Job-up pausada con referencia a una sesión previa relacionada. |
| `sesion-job-up-cerrada.md` | `cerrada` | Sesión Job-up ya cerrada para comprobar que no se reabre ni se reescribe. |
| `sesion-metodologia-abierta.md` | `abierta` | Sesión no Job-up, claramente metodológica, para verificar exclusión. |

## Línea base observada

La skill actual:

- rehidrata el contexto del host;
- lee `boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md`;
- confirma que el ámbito es Job-up;
- responde con un estado breve y espera instrucciones;
- prohíbe explícitamente las escrituras PCS durante esta invocación.

Ese comportamiento deja sin cubrir el ciclo de vida PCS de Job-up: no crea una
nueva sesión fechada, no cierra sesiones previas y no actualiza el puntero de
estado.

## Escenarios RED

### 1. Invocación normal bajo presión de tiempo

**Entrada de prueba:** una sesión Work vacía con `$empleo-inicio-busqueda` y el
fixture anterior.

**Esperado en la versión actual:** no se crea una nueva sesión PCS fechada.

**Resultado RED observado:** la skill responde, pero no materializa ninguna
escritura en `.pcs/sesiones/` ni genera una sesión nueva con timestamp.

### 2. Varias sesiones previas

**Entrada de prueba:** las tres sesiones Job-up del fixture más la sesión
metodológica abierta.

**Esperado en la versión actual:** no se cierran las sesiones Job-up previas y
la sesión metodológica no se toca.

**Resultado RED observado:** no hay cierre de sesiones Job-up activas, no se
añade cierre a la sesión pausada ni a la abierta, y la sesión metodológica
permanece intacta porque no existe ninguna escritura de ciclo de vida.

### 3. Sesión previa parcialmente documentada

**Entrada de prueba:** una sesión Job-up previa con metadatos mínimos y cuerpo
incompleto.

**Esperado en la versión actual:** no se preserva y cierra porque no existe una
escritura de ciclo de vida.

**Resultado RED observado:** la skill no registra cierre, no completa el
contenido histórico y no deja una traza documental nueva para esa sesión.

## Racionalización detectada

Durante el análisis de la versión actual aparece una racionalización peligrosa:
tratar la creación de la nueva sesión como una tarea manual para más tarde.
Esa lectura no cumple el contrato del flujo, porque deja la invocación sin
sesión viva nueva, sin cierre de previas y sin actualización del estado.

## Criterios GREEN esperados

- [ ] El nombre de archivo de la nueva sesión sigue `sesion-YYYYMMDD-HHMM-slug.md`.
- [ ] El `id` de frontmatter coincide con el nombre base del archivo.
- [ ] El `inicio` y el timestamp documental de la nueva sesión coinciden con la
  invocación.
- [ ] La nueva sesión queda con `estado: abierta`.
- [ ] Las sesiones Job-up previas en estado cerrable quedan con `cierre`.
- [ ] La sesión metodológica no Job-up queda excluida de cualquier cierre.
- [ ] El puntero de estado queda actualizado hacia la nueva sesión.
- [ ] No se crean acciones nuevas ni decisiones nuevas.
- [ ] No se producen acciones externas.

