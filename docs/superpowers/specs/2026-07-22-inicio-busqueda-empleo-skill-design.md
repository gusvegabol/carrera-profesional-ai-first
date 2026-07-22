# Diseño — inicio de búsqueda de empleo mediante skill local

## Objetivo

Reducir el inicio de una sesión Work dedicada a la búsqueda de empleo a una invocación explícita y breve: `$empleo-inicio-busqueda`.

## Principio de diseño

La activación y las instrucciones reutilizables viven en una skill local de `carrera-ai`; el protocolo operativo específico vive en la bóveda de búsqueda de empleo. PCS conserva su gobernanza y su comando general de rehidratación sin cambios.

## Componentes

1. Skill local: `.codex/skills/empleo-inicio-busqueda/SKILL.md`.
   - Se activa únicamente cuando el usuario invoca `$empleo-inicio-busqueda`.
   - Sigue el protocolo de rehidratación del host y carga el punto de entrada operativo.
   - No ejecuta acciones de candidatura ni modifica información por el mero inicio de sesión.

2. Punto de entrada operativo: `boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md`.
   - Declara el alcance exclusivo de la rama de búsqueda de empleo.
   - Dirige la lectura de `README.md`, `seguimiento-candidaturas.md` y las fuentes PCS pertinentes.
   - Define la respuesta inicial: estado breve, candidaturas y acciones relevantes, siguiente paso seguro y espera de instrucciones.

## Secuencia

1. El usuario abre una sesión Work vacía e invoca `$empleo-inicio-busqueda`.
2. Work rehidrata el contexto mínimo de `carrera-ai` conforme al PCS.
3. Work lee `INICIO_SESION_WORK.md` y los documentos que este determina.
4. Work confirma el ámbito, presenta el estado mínimo y espera instrucciones del usuario.

## Límites

- La skill es local a `carrera-ai`; no se registra ningún comando nuevo en el Core PCS.
- La búsqueda de empleo no altera la investigación metodológica de entrevista ni sus documentos.
- No se usa Chrome, no se contacta con empresas y no se presenta ninguna candidatura sin una instrucción posterior y explícita del usuario.
- La skill no sustituye las fuentes de autoridad: el estado, las acciones y las decisiones PCS se consultan en sus documentos vigentes.

## Criterios de aceptación

- En una sesión Work vacía, `$empleo-inicio-busqueda` permite comenzar sin pegar el prompt largo de rehidratación.
- El inicio carga únicamente el contexto necesario y diferencia esta rama de la investigación de entrevista.
- La salida inicial es breve, trazable y termina esperando la siguiente instrucción del usuario.
- La invocación no produce escrituras ni acciones externas.
