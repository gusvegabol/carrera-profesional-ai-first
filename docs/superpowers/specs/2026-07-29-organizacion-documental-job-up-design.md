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
└─ PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md

historico/
└─ boveda-entrevista-profesional/busqueda-empleo/  (solo documentos aprobados como históricos)
```

La carpeta `proceso/` organizará plantillas e indicará el playbook canónico de
`docs/`, sin crear una versión duplicada del playbook. Las especificaciones y
planes de diseño continuarán en `docs/superpowers/` como memoria de diseño y
planificación, no como instrucciones de uso diario.

## Contenido del README de Job-up

El README sustituirá el índice actual de materiales y la referencia aislada a
una candidatura antigua por estas secciones:

1. Qué es Job-up y qué no es.
2. Límites: separación de la entrevista metodológica, evidencia factual,
   privacidad y aprobación humana.
3. Mapa de la estructura y papel de cada área.
4. Flujo operativo desde la valoración de una oferta hasta su cierre.
5. Matriz de artefactos por tipo de preparación.
6. Enlaces a fuentes canónicas: decisiones PCS, estado, playbook y seguimiento.
7. Reglas de trazabilidad y de traslado al histórico.

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
   prepara los documentos definidos por el proceso.
4. El expediente inventaría todos sus documentos operativos y el seguimiento
   refleja el estado vivo.
5. La persona candidata revisa y aprueba antes de cualquier envío o contacto.
6. El seguimiento se actualiza tras la acción. PCS se actualiza solo cuando el
   hecho requiere sesión, decisión, acción o cambio de estado operativo.

Si falta evidencia factual, debe declararse como límite y no completarse por
inferencia. Si no existe autorización de datos privados, esos datos no se
consultan ni se incorporan. Sin aprobación humana, la candidatura no supera el
estado `pendiente_de_aprobacion`.

## Migración propuesta

- Mover `datos-core-busqueda.md` y `datos-privados-candidatura.md` a
  `fuentes/`.
- Mover `templates/` a `proceso/plantillas/`.
- Mover `seguimiento-candidaturas.md` a `seguimiento/`.
- Conservar `candidaturas/` y `presentacion-espontanea/` como expedientes
  operativos diferenciados.
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

## Fuera de alcance

- Enviar candidaturas, usar Chrome, conectores o contactos externos.
- Alterar el SPEC, los playbooks de entrevista o la decisión de creación de
  Job-up.
- Crear un host o proyecto independiente.
- Mover documentos a `historico/` solo porque sean antiguos.
- Rediseñar los formatos de CV, carta o los criterios de evaluación de las
  candidaturas.

## Trazabilidad

- Sesión PCS: [[sesion-20260729-1320-organizacion-documentacion-job-up]].
- Decisión de alcance: [[DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo]].
- Decisión de sesiones: [[DEC-20260724-1956-001-delimitar-sesiones-job-up]].
- Playbook canónico: [[PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0]].
