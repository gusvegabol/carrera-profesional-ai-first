---
id: DEC-20260717-1642-001-versionado-funcional-carrera-ai
titulo: Adoptar el versionado funcional de Carrera AI
estado: vigente
fecha_registro: 2026-07-17
fecha_adopcion: 2026-07-17
fecha_vigencia: 2026-07-17
tipo: decision
host: carrera-ai
---

# DEC-20260717-1642-001-versionado-funcional-carrera-ai — Adoptar el versionado funcional de Carrera AI

## Enunciado de la decisión

Se adopta un modelo de dos niveles: versiones globales MAYOR.MENOR para el producto y versiones semánticas MAYOR.MENOR.PARCHE para sus componentes funcionales.

Carrera AI 2.0 queda en desarrollo con base 1.6. Su objetivo de cierre es validar con una persona un Perfil Profesional Accionable integral y revisable mediante cobertura profesional, inmersión en profundidad, evidencias y síntesis de trayectoria.

ESCO queda fuera de 2.0 como investigación paralela y candidata provisional a un posible hito 2.5. Esa candidatura no abre la versión ni puede bloquear el cierre de 2.0.

[VERSIONADO_CARRERA_AI.md](../../docs/VERSIONADO_CARRERA_AI.md) es la fuente funcional de verdad para la versión global y [FLUJO_CAMBIO_VERSION_CARRERA_AI.md](../../docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md) es su procedimiento local de transición.

## Motivo

El proyecto había acumulado referencias de versión distribuidas entre README, SPEC, nombres de componentes y sesiones. El modelo aprobado separa el ciclo del producto del ciclo de sus componentes y permite conocer la versión actual, su base, su objetivo y su criterio de finalización sin reinterpretar el historial.

## Contexto

La línea 1.x completó el MVP centrado en profundidad e identificó su límite de cobertura. Carrera AI 2.0 integra cobertura, profundidad, evidencias y síntesis para producir el Perfil Profesional Accionable.

La versión funcional Carrera AI 2.0 y la versión de gobernanza PCS 2.0 son numeraciones independientes. El SPEC conserva su autoridad sobre la definición del producto; el documento de versionado gobierna únicamente la versión global y su composición.

## Alternativas descartadas

- Usar una única versión para el proyecto y todos sus componentes.
- Versionar solamente los playbooks y dejar el producto sin versión global.
- Mantener el versionado distribuido entre sesiones y README.

## Impacto esperado

- Una fuente única para la genealogía y el estado de la versión global.
- Un flujo reproducible para abrir, promover, completar o abandonar versiones.
- Componentes capaces de evolucionar de forma independiente dentro del alcance global.
- Trazabilidad PCS de las aprobaciones humanas sin convertir PCS en decisor funcional.

## Alcance

La decisión afecta al versionado funcional del host carrera-ai, a sus superficies de orientación, al SPEC y a la delimitación de sus sesiones. No modifica PCS Core, hosts/hosts.yaml ni el contrato metodológico de los playbooks.

## Relaciones

- Sesión de origen: [sesión técnica de materialización](../sesiones/sesion-20260717-1642-materializacion-versionado-carrera-ai.md).
- Sesión funcional activa: [adaptación funcional](../sesiones/sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai.md).
- Acción afectada: [ACC-20260717-1642-001-materializar-versionado-carrera-ai](../acciones/ACC-20260717-1642-001-materializar-versionado-carrera-ai.md).
- Estado operativo: [estado actual](../estado/estado-actual.md).
- Decisión anterior o sustituida: ninguna.

## Revisión futura

Revisar esta decisión al promover 2.0 a candidata a cierre, completarla o abandonarla; al cambiar su base; o al proponer formalmente que la investigación ESCO abra una versión posterior.
