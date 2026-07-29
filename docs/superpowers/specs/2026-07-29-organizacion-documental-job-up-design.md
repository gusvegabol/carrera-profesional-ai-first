# Diseño de definición y organización documental de Job-up

## Estado

Diseño aprobado por la persona responsable el 2026-07-29. Define la futura
organización documental de Job-up, pero no materializa todavía movimientos,
renombrados ni cambios de contenido fuera de esta especificación.

## Propósito

Clarificar qué es Job-up dentro de `carrera-ai` y reorganizar su documentación
para que tanto una persona como un agente puedan orientarse con rapidez,
mantener la trazabilidad de cada candidatura y escalar la rama sin duplicar las
capas de gobernanza del proyecto.

## Definición operativa

Job-up es la rama operativa de búsqueda de empleo de Carrera AI. Usa
información profesional factual para valorar ofertas y preparar materiales de
candidatura revisables.

No es un proyecto independiente ni modifica por sí mismo el SPEC o los
playbooks de entrevista de Carrera AI. Toda candidatura requiere aprobación
humana antes de un envío, una inscripción, un contacto externo o cualquier
acción equivalente.

La decisión vigente
[[DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo]] conserva la
autoridad sobre su creación y alcance. La decisión
[[DEC-20260724-1956-001-delimitar-sesiones-job-up]] mantiene las sesiones PCS
como registros históricos delimitados, no como soporte operativo permanente.

## Principios de organización

- El `README.md` de Job-up será la referencia funcional única de la rama:
  explicará propósito, alcance, límites, estructura, flujo y matriz de
  artefactos.
- Cada documento tendrá una función única: fuente, proceso, registro vivo,
  expediente de candidatura, material espontáneo o histórico.
- `.pcs/` conservará estado, decisiones, acciones y sesiones. El README podrá
  enlazar estas fuentes, pero no las duplicará ni las sustituirá.
- `historico/` seguirá siendo una capa global de `carrera-ai`; Job-up no
  creará una carpeta local llamada `archivo` ni un histórico paralelo.
- La documentación metodológica vigente de `docs/` mantendrá su autoridad y
  será enlazada desde Job-up. La reorganización solo moverá artefactos
  operativos propios de la rama.
- Los movimientos conservarán trazabilidad mediante Git y los enlaces se
  actualizarán y validarán.

## Arquitectura objetivo

La raíz operativa seguirá siendo
`boveda-entrevista-profesional/busqueda-empleo/`, mientras no se adopte una
decisión posterior sobre la ubicación global de la rama.

```text
boveda-entrevista-profesional/busqueda-empleo/
├─ README.md
├─ fuentes/
│  ├─ datos-core-busqueda.md
│  └─ datos-privados-candidatura.md
├─ proceso/
│  └─ plantillas/
├─ seguimiento/
│  └─ seguimiento-candidaturas.md
├─ candidaturas/
└─ presentacion-espontanea/

docs/metodologia/playbooks/
└─ PLAYBOOK_CANDIDATURA_POR_OFERTA.md

historico/
└─ boveda-entrevista-profesional/busqueda-empleo/  (solo documentos aprobados como históricos)
```

La carpeta `proceso/` organizará plantillas e indicará el playbook canónico de
`docs/`, sin crear una versión duplicada del playbook. Las especificaciones y
planes de diseño continuarán en `docs/superpowers/` como memoria de diseño y
planificación, no como instrucciones de uso diario.

## Contenido del README de Job-up

El README sustituirá el índice actual de materiales y la referencia aislada a
una candidatura antigua. Mantendrá dos capas con una frontera explícita:

1. **Modelo mental.** Qué es Job-up, misión, alcance, exclusiones, principios
   y arquitectura conceptual.
2. **Uso operativo.** Cómo empezar, mapa de la estructura, flujo de trabajo,
   skills, playbooks, matriz de artefactos, trazabilidad y reglas de histórico.

Esta separación es interna al README. Si la capa conceptual crece lo suficiente
en el futuro, podrá extraerse a un documento de arquitectura sin alterar el
README como punto de entrada.

Desde su primera versión, el README utilizará las secciones estructurales
estables «Modelo mental de Job-up» y «Uso operativo de Job-up». La futura
extracción de la capa conceptual conservará el README como puerta de entrada y
no obligará a rediseñar la capa operativa.

El README incluirá, como mínimo:

1. Qué es Job-up y qué no es.
2. Límites: separación de la entrevista metodológica, evidencia factual,
   privacidad y aprobación humana.
3. Mapa de la estructura y papel de cada área.
4. Cómo empezar y qué skill corresponde a cada entrada operativa.
5. Flujo operativo desde la valoración de una oferta hasta su cierre.
6. Matriz de artefactos por tipo de preparación.
7. Enlaces a fuentes canónicas: decisiones PCS, estado, playbook y seguimiento.
8. Reglas de trazabilidad y de traslado al histórico.

## Matriz de artefactos

El README incluirá una matriz breve. Las plantillas y el playbook mantendrán el
detalle normativo de cada artefacto.

| Artefacto | Candidatura por oferta | Presentación espontánea |
| --- | --- | --- |
| Análisis de oferta | Obligatorio | No aplica |
| Ficha de candidatura | Obligatoria | Según destinatario concreto |
| Guion de adaptación | Obligatorio | Selección factual general |
| Veredicto final | Obligatorio antes de aprobar | Revisión proporcional |
| CV DOCX y PDF | Obligatorios | Base obligatoria |
| CV LaTeX | Obligatorio | Previsto para futuras versiones |
| Carta DOCX y PDF | Obligatorias | Solo si la solicita el destinatario |
| Email de presentación | Según canal | Base obligatoria |
| Informe de empresa o preparación de entrevista | Solo si se genera | Solo si se genera |

La matriz no autoriza excepciones al playbook, no reemplaza la revisión de
evidencia y no convierte un artefacto opcional en obligatorio cuando la fuente
canónica aplicable indique otra cosa.

## Flujo operativo

1. Persona o agente abre el README y clasifica la petición.
2. Para una oferta, consulta las fuentes factuales y registra el análisis en
   el expediente correspondiente.
3. Solo cuando existe autorización para el caso, consulta los datos privados y
   prepara los documentos definidos por el proceso. Puede reutilizar una
   autorización escrita en la ficha privada si delimita expresamente esa misma
   candidatura; no autoriza otras ofertas, empresas ni usos posteriores.
4. El expediente inventaría todos sus documentos operativos y el seguimiento
   refleja el estado vivo.
5. La persona candidata revisa y aprueba antes de cualquier envío o contacto.
6. El seguimiento se actualiza tras la acción. PCS se actualiza solo cuando el
   hecho requiere sesión, decisión, acción o cambio de estado operativo.

Si falta evidencia factual, debe declararse como límite y no completarse por
inferencia. Si no existe autorización de datos privados, esos datos no se
consultan ni se incorporan. Sin aprobación humana, la candidatura no supera el
estado `pendiente_de_aprobacion`.

Los datos privados aportados sin una autorización aplicable no se copian ni se
propagan. Se bloquea únicamente la parte del flujo que necesite esos datos y se
solicita una confirmación mínima de uso; el análisis factual o público que no
los requiera puede continuar.

## Migración propuesta

- Mover `datos-core-busqueda.md` y `datos-privados-candidatura.md` a
  `fuentes/`.
- Mover `templates/` a `proceso/plantillas/`.
- Mover `seguimiento-candidaturas.md` a `seguimiento/`.
- Conservar `candidaturas/` y `presentacion-espontanea/` como expedientes
  operativos diferenciados.
- Integrar en el README el contenido conceptual de `INICIO_SESION_WORK.md` y
  trasladar este último a `historico/` una vez que deje de ser una entrada.
- Mantener el playbook y las especificaciones de diseño en `docs/` y enlazarlos
  desde la raíz de Job-up.
- Trasladar a `historico/` solo documentos sustituidos o no vigentes, con
  confirmación humana y manteniendo su ruta de procedencia.

No se moverán ni reescribirán archivos de `.pcs/` como parte de la
reorganización, salvo que el ciclo PCS de este trabajo requiera actualizar el
registro de la sesión o el estado operativo.

## Validación

La implantación se considerará correcta cuando:

- el README permita localizar cada función sin leer toda la rama;
- todos los enlaces Markdown y wikilinks modificados resuelvan;
- el seguimiento refleje candidaturas y estados existentes;
- cada expediente inventaríe sus documentos operativos reales;
- se mantengan explícitos los límites de privacidad, evidencia factual y
  aprobación humana;
- las skills de Job-up resuelvan las rutas nuevas y no conserven referencias
  operativas a `INICIO_SESION_WORK.md`;
- el README explique qué skill usar y no duplique el ciclo PCS ni la lógica
  detallada de las skills;
- los documentos históricos, si los hubiera, estén en `historico/` con su ruta
  de procedencia y autorización de traslado;
- no se hayan alterado indebidamente las fuentes PCS ni los playbooks
  metodológicos externos a este alcance.

## Versionado del playbook de candidatura por oferta

El playbook vigente tendrá un nombre estable, sin versión en el archivo:

```text
docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md
```

Su control de versión vivirá en el frontmatter YAML. La primera versión
materializada bajo esta regla será `1.1.0`, porque incorpora capacidades
compatibles respecto a la versión original: guion narrativo, veredicto final,
controles de arrastre y ATS, CV en LaTeX y validación estructural.

```yaml
---
id: playbook-candidatura-por-oferta
tipo: playbook
version: "1.1.0"
estado: vigente
fecha_version: 2026-07-29
version_anterior: "1.0.0"
sustituye: PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0
---
```

Solo los documentos históricos incluirán la versión en el nombre. La versión
original recuperada desde Git se conservará en:

```text
historico/docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md
```

Su YAML documentará el cierre de vigencia:

```yaml
---
id: playbook-candidatura-por-oferta
tipo: playbook
version: "1.0.0"
estado: retirada
fecha_version: 2026-07-21
fecha_retiro: 2026-07-29
sustituida_por: "1.1.0"
---
```

La implantación recuperará el contenido exacto del commit de creación de
`v1.0.0` para la copia histórica. El contenido actual, que ya incorpora las
mejoras posteriores, será la base del playbook vigente `1.1.0`. Así no se
atribuye retrospectivamente a la versión histórica contenido que no tuvo.

## Control de versión de fuentes y plantillas

Las fuentes y plantillas de Job-up tendrán control de versión en frontmatter
YAML, con campos adecuados a su tipo documental: `id`, `tipo`, `version`,
`estado`, `fecha_version` y, cuando exista, `version_anterior`. El estado de
una fuente o plantilla reflejará su vigencia documental, no el avance de una
candidatura.

Las candidaturas y los documentos de sus expedientes no tendrán versionado
trazable. Su gestión se basa en el seguimiento, los artefactos producidos y el
estado propio de la candidatura; añadir versiones a esos documentos no aporta
mejora operativa. El traslado de una fuente o plantilla a `historico/` seguirá
requiriendo sustitución identificada, confirmación humana y conservación de la
ruta de procedencia; nunca será automático por su estado.

## Skills de entrada de Job-up

Las skills de Codex son puntos de entrada operativos de la rama y deben
aparecer en el README, aunque continúen físicamente bajo `.codex/skills/`.

La reorganización renombrará las dos skills existentes para hacer explícita su
pertenencia a Job-up:

| Nombre actual | Nombre objetivo | Función |
| --- | --- | --- |
| `empleo-inicio-busqueda` | `job-up-inicia-sesion` | Abrir explícitamente un nuevo bloque Job-up y gestionar su ciclo PCS. |
| `empleo-genera-cv-empresa` | `job-up-genera-cv-empresa` | Preparar una candidatura espontánea investigada para una empresa concreta. |

Se añadirá una tercera skill:

| Skill | Función |
| --- | --- |
| `job-up-candidatura-oferta` | Recibir una oferta mediante URL, fichero Markdown o texto pegado y activar el flujo de candidatura por oferta. |

La oferta podrá recibirse en cualquiera de estas tres modalidades:

- URL pública accesible.
- Fichero Markdown de estructura libre aportado por la persona usuaria.
- Texto de la oferta copiado y pegado en el chat.

No se impondrá una plantilla al Markdown ni al texto, ya que las fuentes de
ofertas utilizan formatos propios. La skill extraerá la información disponible
y, si faltan datos esenciales para preparar la candidatura, señalará las
ausencias y solicitará únicamente la información imprescindible. Una URL cuyo
contenido no pueda leerse por permisos u otras restricciones podrá sustituirse
por cualquiera de las otras dos modalidades.

### Reglas de sesión para `job-up-candidatura-oferta`

La skill de candidatura por oferta no abrirá una nueva sesión PCS por sí misma.
Solo podrá vincular el trabajo a una única sesión Job-up que ya esté abierta.

- Si existe una única sesión Job-up abierta, la candidatura se vincula a ella.
- Si existen varias sesiones abiertas o no puede determinarse una única sesión
  adecuada, la skill pide a la persona usuaria que elija aquella a la que debe
  vincularse el trabajo.
- Si no existe ninguna sesión Job-up abierta, la skill lo informa y pregunta si
  desea ejecutar en ese momento `job-up-inicia-sesion`. Solo tras una respuesta
  afirmativa explícita invoca esa skill y comprueba de nuevo que existe una
  única sesión abierta.
- La entrega de una oferta, por cualquiera de las tres modalidades, no equivale
  por sí sola a autorización para crear una sesión PCS.
- `job-up-candidatura-oferta` no crea directamente sesiones ni reproduce la
  lógica de PCS de `job-up-inicia-sesion`.

### Flujo de `job-up-candidatura-oferta`

1. Recibir la oferta mediante URL, fichero Markdown o texto pegado.
2. Obtener o extraer el contenido disponible y registrar su procedencia: URL
   de origen cuando exista, o contenido aportado por la persona usuaria y fecha
   de recepción.
3. Identificar los datos esenciales que falten y solicitarlos solo cuando sean
   necesarios para continuar.
4. Resolver una única sesión Job-up abierta; si existen varias o hay
   ambigüedad, pedir a la persona usuaria que elija una.
5. Si no existe una sesión abierta, informar de ello y ofrecer ejecutar
   `job-up-inicia-sesion`; continuar solo tras una confirmación afirmativa
   explícita y la creación correcta de la sesión por esa skill.
6. Crear el análisis de la oferta dentro del expediente correspondiente.
7. Aplicar el playbook canónico y la matriz de artefactos.
8. Consultar datos privados solo si existe autorización para esa candidatura.
9. Preparar los documentos y el veredicto final.
10. Actualizar la ficha y el seguimiento de la candidatura.
11. Entregar el paquete en `pendiente_de_aprobacion`, sin enviar ni contactar.

Las tres skills tendrán `allow_implicit_invocation: false` y se documentarán
como entradas separadas en el README de Job-up.

`INICIO_SESION_WORK.md` dejará de ser una entrada paralela. Su contenido
conceptual útil —ámbito, límites y orientación inicial— se integrará en el
README. El ciclo exacto de apertura, cierre y trazabilidad de sesiones quedará
solo en `job-up-inicia-sesion`, para evitar duplicar autoridad operativa. Una
vez extraído el contenido, el documento se trasladará a
`historico/boveda-entrevista-profesional/busqueda-empleo/`, preservando su ruta
de procedencia.

## Fuera de alcance

- Enviar candidaturas, usar Chrome, conectores o contactos externos.
- Alterar el SPEC, los playbooks de entrevista o la decisión de creación de
  Job-up.
- Crear un host o proyecto independiente.
- Mover documentos a `historico/` solo porque sean antiguos.
- Rediseñar los formatos de CV, carta o los criterios de evaluación de las
  candidaturas.
- Implementar las skills renombradas o crear `job-up-candidatura-oferta`; eso
  pertenece al plan de implantación posterior.

## Trazabilidad

- Sesión PCS: [[sesion-20260729-1320-organizacion-documentacion-job-up]].
- Línea futura de investigación y networking:
  [[sesion-20260729-1614-investigacion-empresas-relaciones-profesionales]].
- Decisión de alcance: [[DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo]].
- Decisión de sesiones: [[DEC-20260724-1956-001-delimitar-sesiones-job-up]].
- Playbook canónico: [[PLAYBOOK_CANDIDATURA_POR_OFERTA]].
