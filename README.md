# carrera-profesional-ai-first

## Qué es este proyecto

Repositorio anfitrión registrado en PCS con alias `carrera-ai` y con capa operativa `.pcs/` ya inicializada.

La información verificable disponible describe solo el arranque mínimo de PCS sobre el host. No hay todavía una descripción funcional confirmada del proyecto más allá de su identidad como anfitrión PCS.

## Objetivo del proyecto

[PENDIENTE: documentar el objetivo funcional real de `carrera-profesional-ai-first`]

## Estado actual

La capa PCS del host ya existe y su estado vivo indica que el arranque mínimo está hecho. La definición operativa del MVP ya tiene una primera materialización revisable.

El foco operativo verificado es revisar el paquete de Fase 1 y consolidar la siguiente fase solo si la base documental se aprueba.

Para estado operativo vivo, consultar `./.pcs/estado/estado-actual.md` si existe.

## Estructura del proyecto

Estructura verificada en la raíz del host:

- `.git/`
- `.pcs/`

Dentro de `.pcs/` se ha confirmado, como mínimo:

- `estado/estado-actual.md`
- `sesiones/sesion-20260614-2132-inicio-pcs-en-carrera-ai.md`

[PENDIENTE: documentar otras carpetas o artefactos del anfitrión si existen y se confirman]

## Relación con PCS

Este proyecto usa Project Continuity System (PCS) como capa de continuidad, gobernanza y trazabilidad.

PCS gobierna únicamente su capa operativa `.pcs/` y no sustituye la documentación funcional, técnica o estructural propia del proyecto anfitrión.

## Continuidad operativa

- Las sesiones registran historia.
- El estado vivo se consulta en `.pcs/estado/estado-actual.md`.
- Las acciones abiertas viven en `.pcs/acciones/`.
- Las decisiones vigentes viven en `.pcs/decisiones/`.

## Documentación propia del proyecto

No se ha verificado documentación raíz propia del anfitrión fuera de `.pcs/`.

Nota mínima de alcance: el primer documento base del MVP vive en `docs/alcance-mvp.md`.

Documentos confirmados durante esta validación:

- `./.pcs/estado/estado-actual.md`
- `./.pcs/sesiones/sesion-20260614-2132-inicio-pcs-en-carrera-ai.md`
- `./docs/alcance-mvp.md`

[PENDIENTE: identificar README, documentación funcional o documentación técnica propia del host si existen]

## Datos pendientes de completar

- [PENDIENTE: completar descripción funcional del proyecto]
- [PENDIENTE: completar objetivo principal del host]
- [PENDIENTE: completar instrucciones de uso si existen]
- [PENDIENTE: completar documentación propia fuera de `.pcs/`]

## Restricciones

- No inventar estado real del proyecto.
- No inventar arquitectura ni flujos técnicos no documentados.
- No tratar `.pcs/` como sustituto de la documentación del proyecto.
- No materializar este texto como `README.md` real del anfitrión sin revisión humana y autorización explícita.

## Siguiente gesto recomendado

Revisar `docs/alcance-mvp.md` como base del MVP y decidir si la Fase 2 debe arrancar.


## Carpetas auxiliares excluidas

Todo el contenido de `.tmp/` debe considerarse material temporal, auxiliar o de trabajo local.

La carpeta `.tmp/` no forma parte del proyecto operativo, no forma parte de la bóveda `boveda-entrevista-profesional/` y no debe usarse como fuente de verdad.

Su contenido no debe leerse, resumirse, indexarse, modificarse ni usarse salvo petición explícita del usuario.

Esto incluye, entre otros posibles contenidos:

- `.tmp/notas/`
- borradores temporales
- exports parciales
- pruebas
- resultados intermedios
- material auxiliar recopilado por el usuario