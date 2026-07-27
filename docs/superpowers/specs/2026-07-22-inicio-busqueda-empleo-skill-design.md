# Diseño — inicio de búsqueda de empleo mediante skill local

## Objetivo

Reducir el inicio de una sesión Work dedicada a la búsqueda de empleo a una invocación explícita y breve: `$empleo-inicio-busqueda`.

## Principio de diseño

La activación y las instrucciones reutilizables viven en una skill local de `carrera-ai`; el protocolo operativo específico vive en la bóveda de búsqueda de empleo. PCS conserva su gobernanza y su comando general de rehidratación sin cambios.

## Línea base RED

La versión actual de `$empleo-inicio-busqueda` solo rehidrata contexto y responde. No crea una sesión nueva, no registra la hora de invocación y no cierra sesiones previas de Job-up.

## Componentes

1. Skill local: `.codex/skills/empleo-inicio-busqueda/SKILL.md`.
   - Se activa únicamente cuando el usuario invoca `$empleo-inicio-busqueda`.
   - Sigue el protocolo de rehidratación del host y carga el punto de entrada operativo.
   - Puede escribir únicamente en `.pcs/sesiones/` y `.pcs/estado/estado-actual.md`, y solo para materializar el ciclo de vida de sesión de Job-up.
   - No ejecuta acciones de candidatura ni modifica otra información por el mero inicio de sesión.

2. Punto de entrada operativo: `boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md`.
   - Declara el alcance exclusivo de la rama de búsqueda de empleo.
   - Dirige la lectura de `README.md`, `seguimiento-candidaturas.md` y las fuentes PCS pertinentes.
   - Define la respuesta inicial: estado breve, candidaturas y acciones relevantes, siguiente paso seguro y espera de instrucciones.

## Contrato funcional de escritura

- La invocación puede crear una nueva sesión de Job-up en `.pcs/sesiones/`.
- La invocación puede cerrar sesiones previas activas de Job-up dentro de `.pcs/sesiones/`.
- La invocación puede actualizar `.pcs/estado/estado-actual.md` para reflejar la nueva sesión viva relacionada.
- No se permite ninguna otra escritura local ni externa.
- Si alguna validación previa falla, la invocación no debe escribir nada.

## Selección de sesiones Job-up

Una sesión previa se considera candidata a cierre automático solo si pertenece de forma explícita a la rama Job-up o a búsqueda de empleo. La identificación debe apoyarse en señales documentales verificables dentro de la propia sesión:

- frontmatter YAML;
- título;
- contenido del cuerpo.

La sesión solo puede cerrarse automáticamente si su estado actual es uno de estos: `abierta`, `en pausa` o `en redacción`.

Las sesiones en estado `consolidada`, `cerrada` o `archivada` deben preservarse sin reescritura.

La selección debe respetar la entidad canónica de sesión PCS: cada sesión sigue siendo una entidad histórica, con identificación documental propia y sin convertirse en estado vivo por automatización.

## Secuencia

1. El usuario abre una sesión Work vacía e invoca `$empleo-inicio-busqueda`.
2. Work rehidrata el contexto mínimo de `carrera-ai` conforme al PCS.
3. Work resuelve la marca temporal y el nombre de archivo de la nueva sesión.
4. Work identifica y valida las sesiones Job-up candidatas a cierre.
5. Si la validación completa es correcta, Work cierra primero las sesiones activas previas de Job-up.
6. Después crea la nueva sesión con estructura compatible con la entidad y la plantilla canónica de PCS.
7. Finalmente actualiza `.pcs/estado/estado-actual.md` para dejar trazada la nueva sesión relacionada.
8. Work lee `INICIO_SESION_WORK.md` y los documentos que este determina.
9. Work confirma el ámbito, presenta el estado mínimo y espera instrucciones del usuario.

## Orden transaccional y preflight

El flujo de escritura debe comportarse como una transacción documental acotada:

1. resolver marca temporal e identificador documental;
2. calcular la ruta y el nombre de archivo de la nueva sesión;
3. identificar sesiones Job-up potencialmente afectadas;
4. validar que las sesiones detectadas existen, pertenecen a Job-up y están en un estado cerrable;
5. ejecutar las escrituras en este orden fijo:
   - cerrar sesiones activas previas de Job-up;
   - crear la nueva sesión;
   - actualizar el estado vivo.

Si cualquiera de las comprobaciones previas falla, el flujo se aborta completo y no debe dejar escrituras parciales.

## Límites

- La skill es local a `carrera-ai`; no se registra ningún comando nuevo en el Core PCS.
- La búsqueda de empleo no altera la investigación metodológica de entrevista ni sus documentos.
- La invocación no modifica metodología, ESCO, investigación GitHub ni otros documentos fuera del ciclo de vida de sesión Job-up.
- No se usa Chrome, no se contacta con empresas y no se presenta ninguna candidatura sin una instrucción posterior y explícita del usuario.
- La skill no sustituye las fuentes de autoridad: el estado, las acciones y las decisiones PCS se consultan en sus documentos vigentes.

## Criterios de aceptación

- En una sesión Work vacía, `$empleo-inicio-busqueda` permite comenzar sin pegar el prompt largo de rehidratación.
- El inicio carga únicamente el contexto necesario y diferencia esta rama de la investigación de entrevista.
- La salida inicial es breve, trazable y termina esperando la siguiente instrucción del usuario.
- La invocación registra el ciclo de vida mínimo de sesión Job-up solo en `.pcs/sesiones/` y `.pcs/estado/estado-actual.md`.
- La invocación no produce acciones externas.
