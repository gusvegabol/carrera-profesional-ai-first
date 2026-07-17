---
id: sesion-20260717-1642-materializacion-versionado-carrera-ai
titulo: Materialización del versionado funcional de Carrera AI
inicio: 2026-07-17 16:42
cierre: 2026-07-17 16:58
estado: cerrada
tipo: sesion
host: carrera-ai
sesion_relacionada: sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai
version_global_contexto: "2.0"
---

# Sesión PCS — Materialización del versionado funcional de Carrera AI

## Contexto inmediato

La persona aprobó el diseño funcional que separa la versión global de Carrera AI de las versiones semánticas de sus componentes y autorizó su materialización autónoma.

## Objetivo

Convertir el diseño aprobado en documentación canónica, procedimiento, SPEC alineado y memoria PCS coherente, sin modificar PCS Core.

## Resumen y resultado

Carrera AI 2.0 queda declarada en desarrollo, con base 1.6 y con el Perfil Profesional Accionable integral y revisable como objetivo de cierre. ESCO permanece como investigación paralela y candidata provisional a 2.5.

## Capa episódica

Se creó primero el plan ejecutable y un espacio de trabajo aislado. Después se materializaron la fuente canónica y el flujo, se revisó el SPEC para retirar ESCO de los requisitos de 2.0, se corrigió la versión interna del componente de cobertura y se actualizaron orientación, estado, sesiones, acción y decisión.

Dos auditorías paralelas de solo lectura detectaron requisitos implícitos de ESCO y varias contradicciones PCS. La ejecución incorporó esas correcciones antes del cierre.

## Capa semántica

- VERSIONADO_CARRERA_AI gobierna la versión global.
- El SPEC gobierna la definición del producto y mantiene histórico de revisiones.
- El núcleo metodológico gobierna la entrevista.
- PCS registra continuidad, acción, decisión y estado, pero no decide la versión.
- Las sesiones pertenecen como máximo a una versión; ESCO queda como línea paralela sin versión abierta.

## Ideas y líneas cognitivas abiertas

- Validar el recorrido integral de 2.0 con una persona.
- Formalizar el contrato y la primera versión del Perfil Profesional Accionable.
- Validar el componente de cobertura.
- Mantener ESCO fuera de 2.0 hasta una decisión posterior.

## Acciones derivadas

- Acción: [materializar el versionado funcional](../acciones/ACC-20260717-1642-001-materializar-versionado-carrera-ai.md).
- Estado: completada.

## Decisiones derivadas

- Decisión: [adoptar el versionado funcional](../decisiones/DEC-20260717-1642-001-versionado-funcional-carrera-ai.md).
- Estado: vigente.

## Problemas o bloqueos

No quedan bloqueos para el alcance de materialización. La validación del producto 2.0 sigue siendo trabajo funcional posterior.

## Documentos afectados

- docs/VERSIONADO_CARRERA_AI.md.
- docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md.
- docs/DOCUMENTO_SPEC_CARRERA_AI.md.
- README.md, AGENTS.md y docs/AGENTS.md.
- definición MVP del componente de cobertura v2.0.0.
- estado actual, cuatro sesiones preexistentes, esta sesión, una acción y una decisión PCS.

## Rehidratación futura

- Dónde quedó el trabajo: [documento canónico](../../docs/VERSIONADO_CARRERA_AI.md).
- Leer primero: documento canónico, SPEC y [estado actual](../estado/estado-actual.md).
- Líneas abiertas a retomar: cobertura, contrato del Perfil Profesional Accionable y validación integral.
- Riesgo de malinterpretación: PCS 2.0 no equivale a Carrera AI 2.0; ESCO 2.5 es solo una candidatura.
- Siguiente gesto recomendado: continuar el trabajo metodológico de cobertura bajo el objetivo de 2.0.

## Checklist de consolidación

- [x] La capa episódica registra el recorrido histórico relevante.
- [x] La capa semántica resume lo necesario para continuidad IA.
- [x] Las líneas cognitivas abiertas están identificadas.
- [x] Las acciones derivadas están creadas y actualizadas.
- [x] Las decisiones derivadas están creadas y actualizadas.
- [x] ESTADO_PROYECTO está actualizado.
- [x] Los documentos afectados están listados.
- [x] La rehidratación futura permite retomar el hilo.
- [x] La sesión no contiene estado operativo vivo como única fuente.

## Trazabilidad

- Origen: diseño aprobado del versionado funcional.
- Sesiones relacionadas: adaptación funcional, cobertura, investigación ESCO y alcance MVP 1.x.
- Acción relacionada: ACC-20260717-1642-001-materializar-versionado-carrera-ai.
- Decisión relacionada: DEC-20260717-1642-001-versionado-funcional-carrera-ai.
- Estado de proyecto relacionado: .pcs/estado/estado-actual.md.
- Cierre: materialización y validaciones documentales completadas el 2026-07-17 a las 16:58.
