---
id: DEC-20260724-1956-001-delimitar-sesiones-job-up
titulo: Delimitar las sesiones PCS de la línea Job-up
estado: vigente
fecha_registro: 2026-07-24
fecha_adopcion: 2026-07-24
fecha_vigencia: 2026-07-24
tipo: decision
host: carrera-ai
---

# DEC-20260724-1956-001 — Delimitar las sesiones PCS de la línea Job-up

## Enunciado de la decisión

Job-up continuará como línea operativa de búsqueda de empleo a largo plazo, pero no se mantendrá una única sesión PCS abierta de forma indefinida.

La continuidad viva de Job-up se mantendrá en `estado-actual.md`, acciones, decisiones y documentos operativos. Cada bloque concreto de trabajo —como valorar una oferta, preparar una candidatura o revisar el flujo— se documentará en una sesión PCS delimitada, que se consolidará o cerrará al dejar de estar en edición.

## Motivo

La entidad SESION es histórica y representa un evento de trabajo delimitado. Mantener abierta durante años la sesión de materialización de Job-up convertiría ese documento en un histórico operativo extenso y mezclaría continuidad viva con memoria histórica.

## Contexto

La sesión `sesion-20260722-1131-job-up` documentó la apertura y materialización de la rama Job-up y queda cerrada como registro histórico. La rama operativa continúa vigente.

## Alternativas descartadas

- Mantener abierta indefinidamente la sesión de materialización de Job-up.
- Usar esa sesión como lista viva de ofertas, candidaturas y pendientes.
- Crear una sesión nueva por cada microinteracción sin entidad histórica suficiente.

## Impacto esperado

- Mantener las sesiones PCS breves, delimitadas y trazables.
- Facilitar la rehidratación sin releer un histórico operativo acumulativo.
- Conservar el estado consultable y las acciones abiertas fuera de las sesiones históricas.

## Alcance

Esta decisión afecta a la organización documental y a la continuidad PCS de Job-up dentro de `carrera-ai`. No cambia el alcance funcional de Job-up, sus candidaturas, la aprobación humana requerida ni la separación respecto de la investigación metodológica de entrevista.

## Relaciones

- Sesión de origen: [[sesion-20260722-1131-job-up]].
- Acciones afectadas: [[ACC-20260721-1651-001-activar-rama-operativa-busqueda-empleo-fase-1]].
- Estado operativo: [[estado-actual]].
- Decisión anterior o sustituida: ninguna.

## Revisión futura

Revisar esta decisión si cambia la gobernanza canónica de SESION, si Job-up se separa en otro host o si aparece una necesidad documentada de un mecanismo operativo distinto.
