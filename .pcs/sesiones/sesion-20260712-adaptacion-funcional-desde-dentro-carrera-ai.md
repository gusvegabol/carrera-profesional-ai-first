---
id: sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai
titulo: Adaptación funcional del host Carrera AI desde dentro del proyecto
inicio: 2026-07-12
cierre:
estado: abierta
tipo: sesion
host: carrera-ai
sesion_padre: sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai
version_global_contexto: "2.0"
---

# Sesión PCS - Adaptación funcional del host Carrera AI desde dentro del proyecto

## 1. Identificación

| Campo | Valor |
| --- | --- |
| Tipo de documento | Sesión de trabajo PCS |
| Proyecto anfitrión | Carrera Profesional AI-First |
| Host anfitrión | `carrera-ai` |
| Nombre de sesión | Adaptación funcional del host Carrera AI desde dentro del proyecto |
| Fichero | `sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai.md` |
| Fecha de apertura | 2026-07-12 |
| Estado | Abierta |
| Naturaleza | Adaptación funcional y documental del host anfitrión |
| Ámbito | Alinear la documentación funcional propia del proyecto anfitrión desde dentro del host, sin tocar PCS Core ni confundir la capa funcional con la gobernanza común |
| Sesión padre | `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md` |
| Ejecuta cambios físicos | Sí, solo dentro del alcance que se autorice expresamente |

## 2. Motivo de apertura

Esta sesión abre una línea de trabajo específica para adaptar la parte funcional de `carrera-ai` desde dentro del propio proyecto anfitrión.

La comprobación de gobernanza ya quedó aprobada en `AGENTS.md` y `README.md`. Lo que queda por resolver ahora es la capa funcional del host: qué es realmente el proyecto, cuál es su objetivo, qué documentos propios lo definen y cómo debe seguir evolucionando sin mezclar esa capa con la gobernanza PCS.

## 3. Objetivo

Diseñar la nueva metodología de entrevista para que `carrera-ai` pueda capturar la carrera completa de una persona, no solo conceptos aislados, mediante una entrevista asistida por IA que recoja trayectoria, competencias, habilidades, evidencias, narrativas, transiciones y correspondencias candidatas.

## 4. Relación con la sesión padre

Esta sesión queda vinculada a `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`.

La sesión padre conserva la arquitectura general:

- Perfil Profesional Accionable;
- cobertura y profundidad;
- correspondencias ESCO candidatas;
- criterios de evidencia y validación;
- futura evolución del playbook de cobertura.

Esta sesión hija se limita a la capa funcional del proyecto anfitrión:

- identificar y ordenar la documentación propia;
- distinguir lo funcional de lo operativo PCS;
- revisar el encaje de `docs/DOCUMENTO_SPEC_CARRERA_AI.md`;
- decidir qué debe quedar como documento vivo del host y qué debe permanecer como antecedente;
- evitar que la capa funcional se convierta en una segunda gobernanza PCS.

## 5. Decisiones de partida

- PCS Core no se modifica en esta sesión.
- `.pcs/` sigue siendo la memoria operativa del host, no la documentación funcional completa del proyecto.
- `README.md` y `AGENTS.md` del host ya reflejan la relación con PCS; esta sesión no debe reabrir esa gobernanza salvo contradicción nueva.
- La parte funcional del host debe describirse desde el propio proyecto, no desde PCS Core.
- `docs/DOCUMENTO_SPEC_CARRERA_AI.md` se mantiene estable por ahora; esta sesión no tiene como objetivo reescribir el SPEC del proyecto.
- No se deben inventar objetivos, uso, arquitectura o estado funcional que no estén documentados.
- Si falta documentación funcional suficiente, debe quedar explícitamente como pendiente y no rellenarse por inferencia.

## 6. Líneas de trabajo

1. Inventariar la documentación funcional propia del host que ya existe en la raíz y en `docs/`.
2. Determinar si `docs/DOCUMENTO_SPEC_CARRERA_AI.md` sigue siendo el documento funcional central o si necesita ajuste de rol.
3. Identificar qué partes de la situación actual del host describen producto real y cuáles describen solo la línea de cobertura profesional.
4. Separar con claridad la narrativa del sistema AI-First, la entrevista profesional y el estado operativo PCS.
5. Decidir qué documentos deben actualizarse para reflejar el estado funcional real sin mezclarlo con la capa de gobernanza.
6. Si procede, preparar una propuesta de cierre o refinamiento de la documentación funcional base del host, sin reescribir el `SPEC` mientras siga vigente como base funcional.

## 7. Preguntas guía

1. ¿Cuál es hoy la definición funcional más honesta de `carrera-ai` dentro del propio proyecto?
2. ¿Qué documento debe actuar como entrada funcional principal del host?
3. ¿Qué parte del estado actual describe producto y qué parte describe solo exploración metodológica?
4. ¿Qué documentos propios del host merecen quedar como vivos, activos o de antecedente?
5. ¿Cómo se mantiene separada la documentación funcional del host respecto a la gobernanza PCS?
6. ¿Qué cambio mínimo mejoraría la comprensión del proyecto sin sobredimensionarlo?

## 8. Riesgos

- Reducir la sesión a una repetición de lo ya asentado en gobernanza PCS.
- Inventar una descripción funcional más completa de la que realmente existe.
- Confundir la capa metodológica de carrera profesional con el producto anfitrión completo.
- Reabrir la gobernanza del host cuando lo que toca es solo aclarar la parte funcional.
- Convertir esta sesión en un rediseño total del proyecto en lugar de una adaptación ordenada.

## 9. Resultado esperado

Esta sesión deberá dejar una base suficiente para decidir:

1. cuál es la documentación funcional principal del host;
2. qué contenido debe actualizarse en `README.md` o en otros docs del proyecto;
3. qué elementos siguen pendientes de definición funcional;
4. cómo mantener separadas la capa funcional y la capa PCS;
5. si hace falta abrir una segunda sesión para cambios materiales del host.

En esta fase no se espera una reescritura del `SPEC`; la prioridad es la metodología de entrevista y el encaje funcional de la capa documental existente.

## 10. Siguiente gesto recomendado

Inventariar la documentación funcional propia del host y decidir si `docs/DOCUMENTO_SPEC_CARRERA_AI.md` debe permanecer como documento central o pasar a un rol secundario o a un índice funcional reforzado.

## 12. Resultado de la primera revisión funcional

La primera revisión funcional confirma que `docs/alcance-mvp.md` ya no existe en la raíz del host.

La referencia funcional principal visible en esta inspección era `docs/DOCUMENTO_SPEC_CARRERA_AI.md`, que describía el producto como `Carrera AI` y como un perfil profesional accionable con equivalencia ESCO.

La bóveda de entrevista profesional aparece como la capa metodológica y documental que sostiene el sistema de entrevista, cobertura y profundidad:

- `boveda-entrevista-profesional/README.md`
- `boveda-entrevista-profesional/INDEX.md`

Conclusión provisional:

- la parte funcional del host ya no debe reencuadrarse alrededor de `docs/alcance-mvp.md`;
- la siguiente revisión debe tomar como base `docs/DOCUMENTO_SPEC_CARRERA_AI.md` y la bóveda de entrevista profesional;
- la sesión funcional debe continuar desde esa base para decidir qué documentos quedan vivos, activos o de antecedente.

## 13. Dictamen provisional de centralidad funcional

Tras la revisión inicial, la centralidad funcional del host queda provisionalmente así:

- `docs/DOCUMENTO_SPEC_CARRERA_AI.md` actúa como documento funcional principal del proyecto;
- `boveda-entrevista-profesional/` actúa como soporte metodológico y documental del sistema de entrevista, cobertura y profundidad;
- `docs/alcance-mvp.md` ya no es una referencia activa porque no existe en la raíz del host.

Implicación práctica:

- la siguiente revisión funcional debe partir de `docs/DOCUMENTO_SPEC_CARRERA_AI.md`;
- la sesión funcional deberá decidir si ese documento necesita ser refinado, indexado mejor o acompañado por otro documento funcional central;
- la bóveda no sustituye al documento funcional principal, sino que lo alimenta y lo complementa.

## 11. Trazabilidad

- Host resuelto: `carrera-ai` -> `C:/Users/gusve/Documents/Apps/carrera-profesional-ai-first`
- Sesión padre: `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`
- Sesiones relacionadas: `sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md`, `sesion-20260705-concepto-cobertura-profesional-carrera-ai.md`
- Estado de la sesión: abierta
- PCS canónico: no modificado

## 14. Actualización — Adopción del versionado funcional

Las afirmaciones anteriores sobre mantener estable el SPEC describen la fase exploratoria previa. La decisión `DEC-20260717-1642-001-versionado-funcional-carrera-ai` autoriza ahora una alineación acotada del SPEC para asociarlo a Carrera AI 2.0 y retirar ESCO de su criterio de finalización, sin desplazar su autoridad sobre la definición del producto.

La división de autoridad queda así:

- `docs/VERSIONADO_CARRERA_AI.md`: versión global, genealogía, estado y composición;
- `docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md`: procedimiento local de transición;
- `docs/DOCUMENTO_SPEC_CARRERA_AI.md`: definición y límites del producto;
- `docs/Núcleo Metodológico del Playbook/`: metodología de entrevista;
- `.pcs/`: continuidad, decisiones, acciones y estado operativo.

Carrera AI 2.0 permanece en desarrollo. Esta sesión continúa abierta como sesión funcional activa de Work.
