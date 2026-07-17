# Flujo de cambio de versión de Carrera AI

## Propósito y autoridad

Este documento define el procedimiento funcional local del host carrera-ai para abrir, promover, completar o abandonar una versión global del producto.

El procedimiento consume [VERSIONADO_CARRERA_AI.md](VERSIONADO_CARRERA_AI.md) como fuente funcional de verdad. No modifica, extiende ni duplica PCS Core: la persona responsable aprueba cada transición y PCS registra la decisión y su trazabilidad.

Antes de materializar un cambio deben estar identificados el hito funcional, la base, el alcance y la evidencia. Si las fuentes se contradicen, el flujo se detiene y la propuesta permanece abierta hasta que la persona resuelva el conflicto.

## Abrir una versión

- [ ] Detectar el hito funcional que motiva el cambio.
- [ ] Clasificar el hito como cambio MAYOR o MENOR.
- [ ] Comprobar cuál es la última versión completada o, en su ausencia, la raíz 0.0.
- [ ] Verificar que la versión elegida como base existe y está completada.
- [ ] Asignar un número global que no se haya utilizado antes.
- [ ] Definir el objetivo único de la nueva versión.
- [ ] Delimitar el alcance incluido.
- [ ] Declarar expresamente las exclusiones.
- [ ] Formular un criterio de finalización observable.
- [ ] Identificar los componentes funcionales necesarios.
- [ ] Definir la evidencia esperada para validar cada componente.
- [ ] Auditar todas las sesiones abiertas.
- [ ] Cerrar, suceder o mantener paralelas las sesiones según su relación con la versión.
- [ ] Obtener la aprobación humana del objetivo, alcance, base y criterio de finalización.
- [ ] Registrar mediante PCS la decisión funcional aprobada.
- [ ] Actualizar el documento canónico de versionado.
- [ ] Actualizar el README, el SPEC y el estado PCS como superficies consumidoras.
- [ ] Abrir la sesión inicial de la nueva versión y asignarle version_global_contexto.
- [ ] Comprobar las relaciones version_base y continuada_en.
- [ ] Ejecutar todas las validaciones de consistencia y ortografía.

## Promover a candidata a cierre

- [ ] Comprobar que el recorrido satisface el criterio de finalización aprobado.
- [ ] Fijar las versiones exactas de todos los componentes incluidos.
- [ ] Confirmar el estado y las evidencias de cada componente.
- [ ] Verificar que ningún elemento excluido esté actuando como requisito implícito.
- [ ] Congelar provisionalmente el objetivo, el alcance y la composición.
- [ ] Auditar las sesiones abiertas y sus trabajos pendientes.
- [ ] Resolver todas las contradicciones entre las superficies documentales.
- [ ] Obtener aprobación humana para iniciar la validación final.
- [ ] Registrar mediante PCS la promoción a candidata a cierre.
- [ ] Actualizar el documento canónico y el estado PCS.

## Completar una versión

- [ ] Validar el resultado con la persona según el criterio de finalización.
- [ ] Registrar la evidencia de validación y las correcciones aceptadas.
- [ ] Confirmar que la persona reconoce el resultado como fiel al objetivo.
- [ ] Marcar la versión global como completada.
- [ ] Congelar el objetivo, el alcance y la composición final.
- [ ] Fijar las versiones de los componentes que forman la entrega.
- [ ] Revisar y clasificar todas las sesiones abiertas.
- [ ] Cerrar las sesiones cuyo objetivo concluye con la versión.
- [ ] Crear sesiones sucesoras cuando un trabajo continúe en otra versión.
- [ ] Actualizar documento canónico, README, SPEC y estado PCS.
- [ ] Registrar mediante PCS la decisión humana de cierre.
- [ ] Verificar enlaces, genealogía, reciprocidad y ortografía.

## Abandonar una versión

- [ ] Registrar el motivo concreto del abandono.
- [ ] Marcar la versión global como abandonada.
- [ ] Dejar continuada_en vacío.
- [ ] Identificar la última versión completada o la raíz 0.0 como base disponible.
- [ ] Cerrar las sesiones vinculadas exclusivamente a la versión abandonada.
- [ ] Separar los aprendizajes reutilizables de cualquier declaración de continuidad.
- [ ] Evitar abrir automáticamente una versión sustituta.
- [ ] Obtener aprobación humana del abandono.
- [ ] Registrar mediante PCS la decisión y su justificación.
- [ ] Actualizar documento canónico, README, SPEC y estado PCS.
- [ ] Verificar que ninguna sesión siga presentando la versión como activa.

## Auditoría de sesiones

Cada sesión pertenece, como máximo, a una versión global. Una sesión paralela puede no pertenecer a ninguna y debe declarar esa condición sin simular una versión abierta.

| Tipo de sesión | Tratamiento |
| --- | --- |
| Objetivo concluido con la versión | Cerrar |
| Trabajo que continúa en la nueva versión | Cerrar y abrir sucesora enlazada |
| Línea paralela sin versión global | Mantener abierta |
| Infraestructura o gobernanza independiente | Mantener si el alcance sigue válido |
| Objetivo obsoleto | Cerrar documentando el resultado |

Está prohibido cambiar retroactivamente version_global_contexto para trasladar una sesión entre versiones. Si el trabajo continúa, la sesión anterior se cierra y se abre una sucesora enlazada con el nuevo contexto.

## Validaciones obligatorias

- [ ] Existe una única versión global actual.
- [ ] Solo una versión está en desarrollo o candidata a cierre.
- [ ] Cada version_base existe y apunta a una versión completada o a 0.0.
- [ ] Ninguna versión abandonada declara continuada_en.
- [ ] Toda relación continuada_en es recíproca con version_base.
- [ ] La composición al cierre contiene versiones exactas de componentes.
- [ ] El canónico, el README, el SPEC y el estado PCS declaran la misma versión actual.
- [ ] Las sesiones pertenecen, como máximo, a una versión global.
- [ ] Las líneas paralelas no simulan una versión global abierta.
- [ ] El nombre, el título y la versión interna de cada componente son coherentes.
- [ ] Todos los enlaces locales resuelven.
- [ ] La documentación española supera una revisión ortográfica explícita.
- [ ] La decisión PCS identifica la aprobación humana que formaliza.

## Condiciones de parada

El cambio no se materializa cuando:

- la base no existe o no está completada;
- el número ya fue utilizado;
- hay más de una versión global activa;
- objetivo, alcance o criterio de finalización son ambiguos;
- una versión abandonada contiene continuidad;
- las sesiones no pueden clasificarse sin reinterpretar su objetivo;
- dos fuentes con igual autoridad sostienen datos incompatibles;
- falta la aprobación humana requerida.

Ante cualquiera de estas condiciones se informa la contradicción, no se interpreta automáticamente la intención y se mantiene la propuesta abierta. PCS puede registrar el bloqueo, pero no resolver por sí mismo la decisión funcional.

## Trazabilidad del procedimiento

- [Versionado funcional de Carrera AI](VERSIONADO_CARRERA_AI.md)
- [Diseño aprobado del sistema de versionado](superpowers/specs/2026-07-17-versionado-carrera-ai-design.md)
- [Definición funcional del producto](DOCUMENTO_SPEC_CARRERA_AI.md)
