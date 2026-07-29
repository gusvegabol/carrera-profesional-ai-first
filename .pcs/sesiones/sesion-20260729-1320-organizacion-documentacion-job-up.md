---
id: sesion-20260729-1320-organizacion-documentacion-job-up
titulo: Definición y organización documental de Job-up
inicio: 2026-07-29 13:20
cierre:
estado: abierta
tipo: sesion
host: carrera-ai
sesion_relacionada: sesion-20260727-2109-busqueda-empleo
---

# Sesión PCS — Definición y organización documental de Job-up

## Contexto inmediato

Job-up es una rama operativa de búsqueda de empleo dentro de `carrera-ai`.
La continuidad de la rama se mantiene separada de la investigación metodológica
de entrevista y se organiza mediante sesiones PCS delimitadas para cada bloque
concreto de trabajo.

La petición de apertura de esta sesión surge para revisar si la definición de
Job-up está suficientemente explícita y, a partir de esa respuesta, determinar
la mejor forma de organizar su documentación sin mezclar estado vivo, historia
de trabajo, materiales de candidatura y documentación metodológica de Carrera
AI.

## Objetivo

Definir con mayor precisión qué es Job-up dentro del proyecto `carrera-ai`,
comprobar qué parte de esa definición ya está documentada de forma explícita y
proponer una organización documental coherente, trazable y sostenible para la
rama.

El primer bloque de trabajo debe responder, como mínimo:

- cuál es la función de Job-up dentro de `carrera-ai`;
- cuál es su alcance autorizado y cuáles son sus límites;
- qué fuentes documentales ya lo definen;
- si existe una fuente principal o si la definición está fragmentada;
- qué tipos de documentos necesita la rama y qué papel cumple cada uno.

## Capa episódica

La sesión se abre el 2026-07-29 a petición explícita de la persona responsable
para estudiar la definición y la organización documental de Job-up. Antes de
crear esta sesión se revisaron la gobernanza PCS aplicable, la entidad y la
plantilla canónicas de sesión, la decisión que creó la rama operativa, la
decisión que delimitó sus sesiones y las fuentes operativas de búsqueda de
empleo.

La revisión inicial encuentra una definición explícita, aunque distribuida:

- `DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo` define Job-up
  como una rama operativa de búsqueda de empleo dentro de Carrera AI;
- `boveda-entrevista-profesional/busqueda-empleo/README.md` y
  `INICIO_SESION_WORK.md` describen su espacio operativo, flujo y límites;
- `estado-actual.md` conserva la continuidad viva, la separación de líneas y
  los riesgos;
- las carpetas de candidaturas, ofertas, datos fuente y plantillas materializan
  el trabajo concreto de la rama.

La primera hipótesis de trabajo es que existe definición formal suficiente para
reconocer Job-up, pero no una pieza documental única que funcione como punto de
entrada conceptual y mapa de su arquitectura documental. Esta hipótesis queda
abierta a comprobación durante la sesión.

## Capa semántica

Job-up no es un nuevo producto independiente ni una redefinición de la
entrevista profesional. Es una rama operativa, subordinada al proyecto
`carrera-ai`, orientada a convertir información profesional factual en
materiales de búsqueda de empleo y candidaturas revisables para ofertas
concretas.

Sus límites ya documentados incluyen:

- no modificar por sí mismo el SPEC ni los playbooks de entrevista;
- mantener separada la investigación metodológica;
- no declarar competencias no evidenciadas;
- conservar trazabilidad factual y control de privacidad;
- requerir aprobación humana antes del envío de candidaturas;
- no autorizar por sí mismo uso de Chrome, conectores o contactos externos.

La organización documental que se proponga debe respetar la diferencia entre:

- continuidad viva de la rama;
- sesiones PCS históricas y delimitadas;
- fuentes profesionales reutilizables;
- ofertas y candidaturas concretas;
- documentos generados para cada candidatura;
- plantillas y reglas del flujo.

## Ideas y líneas cognitivas abiertas

- Determinar si conviene crear un documento principal de definición y mapa de
  Job-up, y cuál debe ser su autoridad respecto a `README.md`, el estado, las
  decisiones y la documentación operativa.
- Separar la arquitectura conceptual de Job-up de la estructura física actual
  de `boveda-entrevista-profesional/busqueda-empleo/`.
- Inventariar qué documentos son fuentes, cuáles son instrucciones, cuáles son
  registros vivos y cuáles son artefactos históricos o generados.
- Definir cómo deben relacionarse la rama, sus sesiones PCS, las candidaturas,
  las ofertas, las plantillas y el seguimiento global.
- Comprobar si el nombre `Job-up` debe aparecer de forma uniforme en títulos,
  enlaces, metadatos y puntos de entrada.

## Resultado de la sesión

Sesión abierta. El resultado inicial es la identificación de una definición
explícita pero distribuida de Job-up y la delimitación del trabajo necesario
para convertirla, si procede, en una arquitectura documental más clara.

### Actualización — diseño aprobado

La persona responsable aprobó el diseño de organización documental el
2026-07-29. El diseño establece un `README.md` único como referencia funcional
de Job-up, una estructura por función, la conservación de `.pcs/` como capa de
gobernanza separada y el uso exclusivo de `historico/` como capa histórica
global de `carrera-ai`.

También incorpora una matriz de artefactos que distingue entre candidatura por
oferta y presentación espontánea. La especificación resultante se registra en
[[2026-07-29-organizacion-documental-job-up-design]]. No se han movido aún
documentos ni se han alterado materiales operativos durante el diseño.

La persona responsable aprobó además que el playbook de candidatura por oferta
controle su versión en frontmatter YAML. El archivo vigente tendrá un nombre
estable sin versión; solo las copias bajo `historico/` incluirán la versión en
el nombre. La propuesta conserva el contenido original de `v1.0.0` desde Git
como histórico y promueve el contenido actual a `1.1.0`.

Se identifica además que la arquitectura debe incluir las skills de entrada de
Job-up. Se acuerda renombrar `empleo-inicio-busqueda` a
`job-up-inicia-sesion` y `empleo-genera-cv-empresa` a
`job-up-genera-cv-empresa`, y añadir `job-up-candidatura-oferta` para iniciar
el flujo a partir de una URL. Esta última solo podrá vincularse a una sesión
Job-up ya abierta; no creará una sesión PCS salvo petición explícita.

## Acciones derivadas

- No se crea una acción PCS en la apertura. Solo se derivará una acción si la
  sesión identifica una tarea concreta que deba seguirse fuera de este registro
  histórico.

## Decisiones derivadas

- No se crea una decisión PCS en la apertura.
- Se mantienen vigentes:
  - [[DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo]];
  - [[DEC-20260724-1956-001-delimitar-sesiones-job-up]].

## Problemas o bloqueos

- La definición funcional y la organización documental no deben confundirse:
  mejorar la estructura no implica ampliar el alcance de Job-up.
- No debe crearse una fuente normativa nueva ni modificarse el SPEC por
  inferencia durante esta primera revisión.
- Cualquier propuesta que cambie decisiones vigentes, estado operativo o
  alcance requerirá su flujo PCS correspondiente.

## Documentos afectados

- Este registro de sesión.
- `docs/superpowers/specs/2026-07-29-organizacion-documental-job-up-design.md`.
- `README.md`.
- `.pcs/estado/estado-actual.md`.
- `.pcs/decisiones/DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo.md`.
- `.pcs/decisiones/DEC-20260724-1956-001-delimitar-sesiones-job-up.md`.
- `boveda-entrevista-profesional/busqueda-empleo/README.md`.
- `boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md`.
- `boveda-entrevista-profesional/busqueda-empleo/seguimiento-candidaturas.md`.
- Las plantillas y carpetas de ofertas y candidaturas, solo si la revisión
  posterior determina que deben afectarse.

## Rehidratación futura

- **Dónde quedó el trabajo:** la sesión está abierta y ha establecido que
  Job-up cuenta con un diseño aprobado de organización documental; falta que la
  persona responsable revise la especificación escrita antes de crear el plan
  de implantación.
- **Leer primero:** este documento; la decisión de creación de Job-up; la
  decisión sobre sesiones delimitadas; `estado-actual.md`; y
  `boveda-entrevista-profesional/busqueda-empleo/README.md`.
- **Líneas abiertas a retomar:** revisar la especificación, resolver las
  observaciones que surjan y crear después un plan de implantación.
- **Riesgos de malinterpretación:** no tratar esta sesión como estado vivo ni
  convertir la hipótesis inicial en decisión o norma.
- **Siguiente gesto recomendado:** revisar
  `docs/superpowers/specs/2026-07-29-organizacion-documental-job-up-design.md`
  antes de planificar movimientos o cambios documentales.

## Checklist de consolidación

- [ ] La capa episódica registra el recorrido histórico relevante.
- [ ] La capa semántica resume lo necesario para continuidad IA.
- [ ] Las líneas cognitivas abiertas están identificadas.
- [ ] Las acciones derivadas están creadas o marcadas como pendientes.
- [ ] Las decisiones derivadas están creadas o marcadas como pendientes.
- [ ] ESTADO_PROYECTO está actualizado o marcado como pendiente.
- [ ] Los documentos afectados están listados.
- [ ] La rehidratación futura permite retomar el hilo.
- [ ] La sesión no contiene estado operativo vivo como única fuente.

## Trazabilidad

- **Origen:** petición explícita de abrir una sesión PCS para definir Job-up y
  organizar mejor su documentación.
- **Sesiones relacionadas:**
  `sesion-20260727-2109-busqueda-empleo`,
  `sesion-20260724-2004-candidaturas-job-up` y
  `sesion-20260722-1131-job-up`.
- **Acciones relacionadas:**
  `ACC-20260721-1651-001-activar-rama-operativa-busqueda-empleo-fase-1`.
- **Decisiones relacionadas:**
  `DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo` y
  `DEC-20260724-1956-001-delimitar-sesiones-job-up`.
- **Estado de proyecto relacionado:** `estado-actual`.
- **Cierre:** pendiente.
