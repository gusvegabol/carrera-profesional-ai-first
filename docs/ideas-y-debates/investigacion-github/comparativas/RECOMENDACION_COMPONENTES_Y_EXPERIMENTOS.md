# Recomendación de componentes y experimentos

> Plantilla para transformar la comparación de repositorios en propuestas
> técnicas acotadas. No autoriza por sí sola instalaciones, forks,
> integraciones ni cambios metodológicos.

## Propósito

Este documento reúne las recomendaciones que surgen de las fichas y de la
matriz comparativa. Su función es decidir qué ideas merece la pena probar,
qué componentes pueden quedar como referencia y qué líneas deben descartarse
para proteger la MVP.

## Contexto de la recomendación

**Fecha:** `[AAAA-MM-DD]`  
**Necesidad analizada:** `[problema concreto]`  
**Matriz de origen:** [`MATRIZ_COMPARATIVA_REPOSITORIOS.md`](./MATRIZ_COMPARATIVA_REPOSITORIOS.md)  
**Fichas de origen:** `[enlaces]`

## Componentes candidatos

| Prioridad | Componente o patrón | Repositorio de origen | Tipo | Evidencia actual | Valor esperado | Coste | Riesgo | Fase propuesta | Decisión |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `[componente]` | `[repositorio]` | `idea / modelo / prompt / flujo / código / interfaz` | `lectura / inspección / experimento / integración` | `[valor]` | `bajo / medio / alto` | `bajo / medio / alto` | `MVP / posterior / referencia` | `prototipar` |

## Recomendaciones

### Adoptar como patrón o idea

`[componente o patrón]`

**Motivo:** `[qué problema resuelve y por qué encaja]`  
**Límites:** `[qué no implica adoptar]`

### Probar mediante experimento

`[componente]`

**Motivo:** `[qué incertidumbre queremos resolver]`  
**Experimento:** `[EXP-...]`

### Mantener como referencia

`[repositorio o componente]`

**Motivo:** `[qué aprendizaje aporta sin justificar integración]`

### Posponer o descartar

`[repositorio o componente]`

**Motivo:** `[coste, riesgo, falta de encaje o dependencia]`

## Experimentos priorizados

| ID | Pregunta | Hipótesis | Repositorio o componente | Coste | Aprendizaje esperado | Criterio de éxito | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EXP-001` | `[pregunta]` | `[hipótesis]` | `[origen]` | `bajo` | `[aprendizaje]` | `[resultado observable]` | `propuesto` |

### Secuencia recomendada

1. `[experimento de menor coste y mayor aprendizaje]`;
2. `[experimento dependiente, si procede]`;
3. `[experimento posterior]`.

No se iniciará un experimento posterior si el resultado del anterior elimina
la necesidad o cambia sustancialmente la hipótesis.

## Impacto posible en Carrera AI-First

### MVP

`[qué podría mejorar sin ampliar indebidamente el alcance]`

### Fases posteriores

`[qué queda fuera de la MVP y por qué]`

### Fuera de alcance o descartado

`[qué no se incorporará]`

## Decisión y condiciones

**Recomendación general:** `continuar investigando / prototipar / adoptar patrón /
posponer / descartar`

**Condiciones para avanzar:**

- `[condición técnica]`;
- `[condición de licencia o privacidad]`;
- `[autorización necesaria]`.

**No implica:**

- integrar automáticamente el repositorio;
- modificar el SPEC o los playbooks;
- crear una arquitectura multiagente;
- conservar datos profesionales reales sin autorización.

## Revisión final

- [ ] Cada recomendación enlaza con una ficha o con la matriz.
- [ ] Cada experimento tiene una pregunta y un criterio de éxito.
- [ ] Se han separado patrones, componentes e integración de código.
- [ ] Se han documentado costes, riesgos y dependencias.
- [ ] Se ha distinguido la MVP de las fases posteriores.
- [ ] Las decisiones formales, si fueran necesarias, se derivarán por el flujo PCS correspondiente.

## Trazabilidad

- Investigación general: [`../INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md`](../INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md).
- Matriz comparativa: [`MATRIZ_COMPARATIVA_REPOSITORIOS.md`](./MATRIZ_COMPARATIVA_REPOSITORIOS.md).
- Sesión PCS: `[identificador o ruta]`.
- Decisión PCS: `[identificador o no aplica]`.
