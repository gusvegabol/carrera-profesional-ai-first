---
id: sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai
titulo: Adaptacion funcional del host Carrera AI desde dentro del proyecto
inicio: 2026-07-12
cierre:
estado: abierta
tipo: sesion
host: carrera-ai
sesion_padre: sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai
---

# Sesion PCS - Adaptacion funcional del host Carrera AI desde dentro del proyecto

## 1. Identificacion

| Campo | Valor |
| --- | --- |
| Tipo de documento | Sesion de trabajo PCS |
| Proyecto anfitrion | Carrera Profesional AI-First |
| Host anfitrion | `carrera-ai` |
| Nombre de sesion | Adaptacion funcional del host Carrera AI desde dentro del proyecto |
| Fichero | `sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai.md` |
| Fecha de apertura | 2026-07-12 |
| Estado | Abierta |
| Naturaleza | Adaptacion funcional y documental del host anfitrion |
| Ambito | Alinear la documentacion funcional propia del proyecto anfitrion desde dentro del host, sin tocar PCS Core ni confundir la capa funcional con la gobernanza comun |
| Sesion padre | `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md` |
| Ejecuta cambios fisicos | Si, solo dentro del alcance que se autorice expresamente |

## 2. Motivo de apertura

Esta sesion abre una linea de trabajo especifica para adaptar la parte funcional de `carrera-ai` desde dentro del propio proyecto anfitrion.

La comprobacion de gobernanza ya quedó aprobada en `AGENTS.md` y `README.md`. Lo que queda por resolver ahora es la capa funcional del host: qué es realmente el proyecto, cuál es su objetivo, qué documentos propios lo definen y cómo debe seguir evolucionando sin mezclar esa capa con la gobernanza PCS.

## 3. Objetivo

Diseñar la nueva metodologia de entrevista para que `carrera-ai` pueda capturar la carrera completa de una persona, no solo conceptos aislados, mediante una entrevista asistida por IA que recoja trayectoria, competencias, habilidades, evidencias, narrativas, transiciones y correspondencias candidatas.

## 4. Relacion con la sesion padre

Esta sesion queda vinculada a `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`.

La sesion padre conserva la arquitectura general:

- Perfil Profesional Accionable;
- cobertura y profundidad;
- correspondencias ESCO candidatas;
- criterios de evidencia y validacion;
- futura evolucion del playbook de cobertura.

Esta sesion hija se limita a la capa funcional del proyecto anfitrion:

- identificar y ordenar la documentacion propia;
- distinguir lo funcional de lo operativo PCS;
- revisar el encaje de `docs/DOCUMENTO_SPEC_CARRERA_AI.md`;
- decidir que debe quedar como documento vivo del host y que debe permanecer como antecedente;
- evitar que la capa funcional se convierta en una segunda gobernanza PCS.

## 5. Decisiones de partida

- PCS Core no se modifica en esta sesion.
- `.pcs/` sigue siendo la memoria operativa del host, no la documentacion funcional completa del proyecto.
- `README.md` y `AGENTS.md` del host ya reflejan la relacion con PCS; esta sesion no debe reabrir esa gobernanza salvo contradiccion nueva.
- La parte funcional del host debe describirse desde el propio proyecto, no desde PCS Core.
- `docs/DOCUMENTO_SPEC_CARRERA_AI.md` se mantiene estable por ahora; esta sesion no tiene como objetivo reescribir el SPEC del proyecto.
- No se deben inventar objetivos, uso, arquitectura o estado funcional que no esten documentados.
- Si falta documentacion funcional suficiente, debe quedar explicitamente como pendiente y no rellenarse por inferencia.

## 6. Lineas de trabajo

1. Inventariar la documentacion funcional propia del host que ya existe en la raiz y en `docs/`.
2. Determinar si `docs/DOCUMENTO_SPEC_CARRERA_AI.md` sigue siendo el documento funcional central o si necesita ajuste de rol.
3. Identificar que partes de la situacion actual del host describen producto real y cuales describen solo la linea de cobertura profesional.
4. Separar con claridad la narrativa del sistema AI-First, la entrevista profesional y el estado operativo PCS.
5. Decidir que documentos deben actualizarse para reflejar el estado funcional real sin mezclarlo con la capa de gobernanza.
6. Si procede, preparar una propuesta de cierre o refinamiento de la documentacion funcional base del host, sin reescribir el `SPEC` mientras siga vigente como base funcional.

## 7. Preguntas guia

1. Cual es hoy la definicion funcional mas honesta de `carrera-ai` dentro del propio proyecto?
2. Que documento debe actuar como entrada funcional principal del host?
3. Que parte del estado actual describe producto y que parte describe solo exploracion metodologica?
4. Que documentos propios del host merecen quedar como vivos, activos o de antecedente?
5. Como se mantiene separada la documentacion funcional del host respecto a la gobernanza PCS?
6. Que cambio minimo mejoraria la comprension del proyecto sin sobredimensionarlo?

## 8. Riesgos

- Reducir la sesion a una repeticion de lo ya asentado en gobernanza PCS.
- Inventar una descripcion funcional mas completa de la que realmente existe.
- Confundir la capa metodologica de carrera profesional con el producto anfitrion completo.
- Reabrir la gobernanza del host cuando lo que toca es solo aclarar la parte funcional.
- Convertir esta sesion en un redisenio total del proyecto en lugar de una adaptacion ordenada.

## 9. Resultado esperado

Esta sesion debera dejar una base suficiente para decidir:

1. cual es la documentacion funcional principal del host;
2. que contenido debe actualizarse en `README.md` o en otros docs del proyecto;
3. que elementos siguen pendientes de definicion funcional;
4. como mantener separadas la capa funcional y la capa PCS;
5. si hace falta abrir una segunda sesion para cambios materiales del host.

En esta fase no se espera una reescritura del `SPEC`; la prioridad es la metodologia de entrevista y el encaje funcional de la capa documental existente.

## 10. Siguiente gesto recomendado

Inventariar la documentacion funcional propia del host y decidir si `docs/DOCUMENTO_SPEC_CARRERA_AI.md` debe permanecer como documento central o pasar a un rol secundario o a un índice funcional reforzado.

## 12. Resultado de la primera revision funcional

La primera revision funcional confirma que `docs/alcance-mvp.md` ya no existe en la raiz del host.

La referencia funcional principal visible en esta inspeccion es `docs/DOCUMENTO_SPEC_CARRERA_AI.md`, que describe el producto como `Carrera AI` y como un perfil profesional accionable con equivalencia ESCO.

La bóveda de entrevista profesional aparece como la capa metodologica y documental que sostiene el sistema de entrevista, cobertura y profundidad:

- `boveda-entrevista-profesional/README.md`
- `boveda-entrevista-profesional/INDEX.md`

Conclusión provisional:

- la parte funcional del host ya no debe reencuadrarse alrededor de `docs/alcance-mvp.md`;
- la siguiente revision debe tomar como base `docs/DOCUMENTO_SPEC_CARRERA_AI.md` y la bóveda de entrevista profesional;
- la sesion funcional debe continuar desde esa base para decidir que documentos quedan vivos, activos o de antecedente.

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
- Sesion padre: `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`
- Sesiones relacionadas: `sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md`, `sesion-20260705-concepto-cobertura-profesional-carrera-ai.md`
- Estado de la sesion: abierta
- PCS canonico: no modificado
