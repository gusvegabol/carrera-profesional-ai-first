---
name: job-up-inicia-sesion
description: Use when the user explicitly invokes $job-up-inicia-sesion in a fresh Work session to start or resume Job-up, the employment-search branch of carrera-ai.
---

# Iniciar Job-up

## Procedimiento

1. Resolver el host `carrera-ai` y la fecha/hora exactas de invocación antes de cualquier escritura.
2. Leer las fuentes canónicas de sesión y el estado vivo: `C:/Users/gusve/Documents/Apps/project-continuity-system/core/ENTIDAD_SESION.md`, `C:/Users/gusve/Documents/Apps/project-continuity-system/templates/TEMPLATE_SESION.md`, `./.pcs/estado/estado-actual.md` y las sesiones PCS necesarias para validar la continuidad de Job-up.
3. Identificar y validar las sesiones previas de Job-up que estén en `abierta`, `en pausa` o `en redacción`, usando señales documentales verificables en frontmatter, título o cuerpo.
4. Preparar sus cierres sin tocar sesiones `consolidada`, `cerrada` o `archivada`, sin tocar líneas no Job-up y sin escribir todavía nada. Cada sesión seleccionada debe pasar explícitamente a `cierre: <timestamp de invocación>` y `estado: cerrada`, conservar intacto el cuerpo histórico existente y dejar una traza mínima de que se cerró al iniciar un nuevo bloque Job-up.
5. Preparar la creación obligatoria de una nueva sesión PCS con nombre canónico `sesion-YYYYMMDD-HHMM-slug.md`, `id` alineado con el nombre base, `estado: abierta`, timestamp de invocación y `sesion_relacionada:` siempre presente; rellenarla con la sesión Job-up relevante más reciente o dejarla vacía solo cuando no exista relación aplicable.
6. Preparar y validar una actualización mínima de `./.pcs/estado/estado-actual.md` que toque solo la trazabilidad dirigida de Job-up, preserve intacto todo el contenido no Job-up y apunte a la nueva sesión.
7. Ejecutar las escrituras solo después de validar el conjunto completo y siempre en este orden fijo: cerrar sesiones Job-up previas, crear la nueva sesión, actualizar `./.pcs/estado/estado-actual.md`.
8. Leer `boveda-entrevista-profesional/busqueda-empleo/README.md` como referencia funcional única y seguir su orden de consulta de Job-up: fuentes en `fuentes/` y seguimiento en `seguimiento/seguimiento-candidaturas.md`. El playbook estable aplicable se consulta desde `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md` cuando el trabajo lo requiera.
9. Confirmar que el ámbito es Job-up, responder con el estado breve de candidaturas y acciones relevantes, proponer el siguiente paso seguro y esperar instrucciones.

## Validaciones previas obligatorias

- Detenerse antes de cualquier escritura si hay ambigüedad o invalidez al resolver el host, localizar las fuentes canónicas, clasificar una sesión como Job-up o no Job-up, seleccionar `sesion_relacionada:`, resolver una colisión de nombre de archivo o preparar el conjunto completo de cambios.
- Explicar expresamente la ambigüedad o invalidez detectada; no continuar por aproximación ni por coincidencia parcial.
- Tratar la creación de la nueva sesión como obligatoria en cada invocación de `$job-up-inicia-sesion`; no convertirla en una tarea opcional o manual posterior.
- Preparar y validar todo el lote de escrituras antes de mutar archivos para evitar cierres parciales, creación parcial o actualización parcial del estado.
- Si dos invocaciones comparten minuto, resolver la colisión con un sufijo incremental compatible con `ENTIDAD_SESION.md`; no sobrescribir ni duplicar nombres de archivo.

## Contramedidas explícitas

- No cerrar sesiones de metodología, ESCO, investigación GitHub u otras líneas abiertas aunque estén en `abierta`, `en pausa` o `en redacción`.
- No reescribir sesiones `consolidada`, `cerrada` o `archivada`.
- No reescribir contenido no Job-up de `./.pcs/estado/estado-actual.md`; solo se permite la traza mínima dirigida de Job-up.
- No omitir `sesion_relacionada:` en la nueva sesión; la clave debe existir siempre, con valor o vacía cuando corresponda.
- No crear una nueva sesión con un nombre ya existente ni continuar si la colisión no puede resolverse con seguridad.
- No continuar después de una coincidencia ambigua, de una clasificación dudosa o de una selección incierta de la sesión relacionada.

## Límites

- Trabajar solo en Job-up, la rama operativa de búsqueda de empleo.
- No modificar la investigación de entrevista.
- No crear comandos nuevos en PCS Core ni alterar la metodología de entrevista.
- Solo se permiten escrituras del ciclo de vida de sesión en `./.pcs/sesiones/` y `./.pcs/estado/estado-actual.md`.
- No realizar modificaciones de candidaturas, envíos, navegación en Chrome, contactos externos ni otras acciones externas por esta invocación.
