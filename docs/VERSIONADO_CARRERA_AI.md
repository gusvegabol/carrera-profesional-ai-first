---
id: versionado-carrera-ai
titulo: Versionado funcional de Carrera AI
version_global_actual: "2.0"
estado_version_global: en_desarrollo
version_base: "1.6"
fecha_actualizacion: 2026-07-17
---

# Versionado funcional de Carrera AI

Este documento es la fuente funcional de verdad para la versión global de Carrera AI. La persona responsable del producto decide la apertura, promoción, finalización o abandono de cada versión; PCS formaliza esas decisiones y conserva su trazabilidad, pero no las sustituye.

El README, el SPEC, el estado PCS y las sesiones consumen o contextualizan esta información. Ninguno reemplaza este documento como registro de la versión global. La versión funcional de Carrera AI también es independiente de pcs_version: que ambos sistemas utilicen el número 2.0 no implica que compartan significado ni ciclo de vida.

## Versión global actual

~~~yaml
version: "2.0"
version_base: "1.6"
estado: "en_desarrollo"
continuada_en:
~~~

### Objetivo

Validar con una persona el recorrido funcional completo:

~~~text
cobertura profesional
→ inmersión en profundidad
→ evidencias
→ síntesis de trayectoria
→ Perfil Profesional Accionable
~~~

La versión se podrá completar cuando la persona pueda revisar y corregir el Perfil Profesional Accionable resultante, y reconocerlo como una representación fiel, útil y sustentada en evidencias de su trayectoria.

La correspondencia con ESCO queda fuera del criterio de finalización de 2.0. Se mantiene como investigación paralela y candidata provisional a una posible versión 2.5, que no está abierta ni comprometida.

### Composición funcional

| Componente | Versión | Estado | Papel | Requisito de cierre |
| --- | --- | --- | --- | --- |
| Entrevista de profundidad | 1.3.2 | vigente | Obtener competencias con evidencia | Funcionar dentro del recorrido integral |
| Cobertura profesional | 1.0.0 | borrador | Recorrer y organizar la trayectoria | Alcanzar una versión validada |
| Perfil Profesional Accionable | pendiente | no formalizado | Integrar la salida final | Disponer de contrato y primera versión validada |
| ESCO | no es componente activo | investigación | Fuera del alcance de 2.0 | No bloquea el cierre |

## Genealogía histórica

| Versión | Nombre o hito funcional | Base | Estado | Continuada en |
| --- | --- | --- | --- | --- |
| 0.0 | Raíz inicial de la genealogía | — | raíz | — |
| 0.1 | app-carrera-profesional: aplicación Python con IA local; abandonada al comprobar que el coste del frontend impedía abordar el núcleo del producto | 0.0 | abandonada | — |
| 0.2 | Número no utilizado deliberadamente; no constituye una versión ni tiene ficha propia | — | no utilizado | — |
| 0.3 | app-carrera-profesional-c#: cambio del frontend a C#; abandonada por reproducir el coste desproporcionado del frontend | 0.0 | abandonada | — |
| 0.4 | app-carrera-bóveda-conocimiento: Obsidian con gobernanza mediante IA local; abandonada por el coste de prompts y guardarraíles locales | 0.0 | abandonada | — |
| 1.0 | Carrera Profesional AI-First: sistema gobernado mediante ChatGPT sin desarrollar una aplicación propia | 0.0 | completada | 1.1 |
| 1.1 | Delimitación del primer MVP: resultado útil, entradas, salidas y exclusiones | 1.0 | completada | 1.2 |
| 1.2 | Entrevista profesional como núcleo: reorientación del MVP hacia la entrevista profunda | 1.1 | completada | 1.3 |
| 1.3 | Primera metodología ejecutable: bóveda, conceptos, patrones, salvaguardas y playbook de profundidad | 1.2 | completada | 1.4 |
| 1.4 | Primera validación empírica: una entrevista produjo una competencia con evidencia y validación personal | 1.3 | completada | 1.5 |
| 1.5 | Validación mediante varios pilotos y refinamiento del método ante tensiones diferentes | 1.4 | completada | 1.6 |
| 1.6 | Cierre del MVP-A: hipótesis mínima de profundidad validada y límite de cobertura identificado | 1.5 | completada | 2.0 |
| 2.0 | Perfil Profesional Accionable mediante cobertura, profundidad, evidencias y síntesis de trayectoria | 1.6 | en desarrollo | — |

La entrada 0.2 reserva deliberadamente un hueco histórico. No debe reconstruirse ni reutilizarse para acomodar retrospectivamente trabajo no documentado.

La relación final de la línea completada anterior queda expresada así:

~~~yaml
version: "1.6"
version_base: "1.5"
estado: "completada"
continuada_en: "2.0"
~~~

## Reglas de las versiones globales

### Numeración

Las versiones globales usan MAYOR.MENOR.

- MAYOR cambia cuando el objetivo de producto o la arquitectura funcional representan una etapa distinta.
- MENOR cambia cuando se alcanza un hito funcional coherente dentro de la misma etapa.
- No existen parches globales. Las correcciones documentales no generan por sí mismas una versión del producto.

### Estados

| Estado | Significado |
| --- | --- |
| propuesta | Objetivo y alcance sometidos a debate, sin desarrollo autorizado |
| en_desarrollo | Versión abierta, con objetivo y criterio de finalización aprobados |
| candidata_a_cierre | Recorrido implementado y sometido a validación final |
| completada | Objetivo validado, composición fijada y cierre aprobado |
| abandonada | Trabajo detenido sin continuidad funcional declarada |

### Base y continuidad

- version_base debe señalar una versión existente y completada, o la raíz 0.0 cuando todavía no exista una versión previa completada.
- Una versión abandonada deja continuada_en vacío.
- continuada_en expresa sucesión efectiva entre versiones no abandonadas; no equivale a una simple derivación experimental.
- Cuando una versión completada declara continuada_en, la versión indicada debe reconocerla como version_base.
- Una investigación paralela no abre una versión global ni puede usar como base una versión que continúe en_desarrollo.
- Solo puede existir una versión global en en_desarrollo o candidata_a_cierre.

## Componentes funcionales

Un componente funcional es una parte del producto con contrato propio, resultado observable, criterio de validación y evolución independiente. Los playbooks de profundidad y cobertura y el contrato del Perfil Profesional Accionable encajan en esta definición.

Los conceptos, patrones, plantillas, documentación auxiliar y el propio SPEC no son componentes. Pueden necesitar revisión e histórico documental, pero no reciben una versión de componente.

### Versionado de componentes

Los componentes usan versionado semántico MAYOR.MENOR.PARCHE:

- MAYOR cambia el contrato o rompe la compatibilidad metodológica.
- MENOR incorpora una capacidad compatible.
- PARCHE corrige o aclara sin modificar el contrato.

Estados admitidos:

| Estado | Significado |
| --- | --- |
| borrador | Definición incompleta o aún no validada |
| en_validacion | Contrato definido y sometido a comprobación |
| vigente | Versión aceptada para su uso |
| descartada | Propuesta no adoptada |
| retirada | Versión antes vigente que ya no debe usarse |

Los componentes pueden evolucionar sin cambiar la versión global mientras conserven el objetivo, el alcance y los criterios de finalización de esta. El documento de versión global fija las versiones exactas de los componentes al promoverla a candidata a cierre.

## Candidatos futuros

ESCO permanece como investigación paralela sobre correspondencia profesional. No es un componente activo de 2.0, no condiciona su cierre y no autoriza por sí sola una versión nueva.

Una posible 2.5 solo podrá abrirse mediante decisión humana posterior, cuando 2.0 esté completada y se hayan definido el objetivo, el alcance, las exclusiones, la base y el criterio de finalización de esa nueva versión.

## Trazabilidad

- [Definición funcional del producto](DOCUMENTO_SPEC_CARRERA_AI.md)
- [Flujo operativo de cambio de versión](FLUJO_CAMBIO_VERSION_CARRERA_AI.md)
- [Diseño aprobado del sistema de versionado](superpowers/specs/2026-07-17-versionado-carrera-ai-design.md)
- [Sesión histórica del alcance MVP 1.x](../.pcs/sesiones/sesion-20260630-alcance-mvp-carrera-ai.md)
- [Sesión de cobertura profesional de 2.0](../.pcs/sesiones/sesion-20260705-concepto-cobertura-profesional-carrera-ai.md)
- [Investigación paralela ESCO](../.pcs/sesiones/sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md)
- [Sesión activa de adaptación funcional](../.pcs/sesiones/sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai.md)
- [Decisión PCS de adopción del versionado](../.pcs/decisiones/DEC-20260717-1642-001-versionado-funcional-carrera-ai.md)

## Mantenimiento

Toda transición de una versión global debe seguir el [flujo de cambio de versión](FLUJO_CAMBIO_VERSION_CARRERA_AI.md), contar con aprobación humana y actualizar de forma coherente las superficies consumidoras. La historia se corrige solo cuando existe evidencia; no se rellenan huecos mediante inferencias.
