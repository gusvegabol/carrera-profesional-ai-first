---
id: evaluacion-gate-candidatura-guion-CAND-2026-020
tipo: evaluacion_gate
fecha_evaluacion: 2026-08-05
candidatura: CAND-2026-020
gate: GATE-CANDIDATURA-GUION
resultado_caso: apto_para_revision_de_aprobacion
estado_gate_global: aprobado
aprobacion_humana: 2026-08-05
sesion_pcs: sesion-20260805-1757-job-up
---

# Evaluación — GATE-CANDIDATURA-GUION — CAND-2026-020

## Alcance

Se evalúa el caso de continuación normal `preparar_con_advertencias` mediante la relación entre [[analisis-oferta]] y [[candidatura]]. La evaluación aporta la evidencia que la persona responsable aprobó explícitamente para el gate global; habilita diseñar `PLAYBOOK_GUION_ADAPTACION_CV`, pero no generar documentos ni enviar la candidatura.

## Resultado del caso

`apto_para_revision_de_aprobacion`

La ficha contiene la información necesaria para iniciar un guion sin rehacer el análisis: origen, decisión, posición, evidencias, límites, advertencias, estado, artefactos y siguiente fase. Las correcciones factuales posteriores ya se han propagado al análisis y a la ficha. Junto con los dos casos controlados, la cobertura prevista queda completa y pasa a revisión humana de aprobación; esta evaluación no aprueba por sí misma el gate global.

## Criterios del gate

### Responsabilidad

- [x] La ficha gobierna el caso sin repetir la extracción factual ni la matriz completa.
- [x] No rehace el análisis de la oferta.
- [x] No redacta CV, carta, guion ni veredicto.

### Trazabilidad

- [x] El origen y la fuente completa están identificados.
- [x] El análisis de origen está enlazado.
- [x] La decisión estratégica se conserva y coincide con el análisis.
- [x] Las evidencias prioritarias reflejan la actualización factual de `HER-03` sobre pedidos y proveedores.
- [x] Los límites principales son trazables.

### Estado

- [x] La decisión estratégica y el estado operativo están separados.
- [x] Advertencias, datos pendientes y bloqueos están diferenciados.
- [x] `presentada: false` expresa un hecho.
- [x] La siguiente fase queda identificada.

### Economía documental

- [x] La ficha no duplica la matriz de encaje ni contenido de fases futuras.
- [x] Contiene información suficiente para gobernar el caso.

### Calidad competitiva

- [x] Existe una tesis de candidatura en la justificación compacta.
- [x] Existe un posicionamiento principal, secundario y enfoques a evitar.
- [x] El gancho puede identificarse a partir del ángulo: «operaciones de supermercados para mejorar disponibilidad, previsión, stock, rotación, cuadres de caja y ejecución de procesos de tienda».
- [x] La selección de evidencias incluye el alcance actualizado de `HER-03` sobre pedidos diarios y negociación acotada con proveedores directos.
- [x] Los riesgos permiten un relato competitivo sin ocultar la FP no finalizada, la sobreexperiencia potencial ni el alcance de caja.
- [x] Las afirmaciones prohibidas son claras.

### Traspaso

- [x] El futuro guion puede identificar relato, experiencia prioritaria, riesgos y afirmaciones a evitar.
- [x] El futuro guion podría consumir la ficha como fuente de gobierno del caso sin reconstruir la estrategia.

## Defectos resueltos

### DEF-CAND-020-001

- **Clasificación:** `CASO`.
- **Criticidad:** alta.
- **Estado:** resuelto.
- **Descripción:** tras actualizar `HER-03`, el análisis recoge los pedidos diarios a CENCOSU y a proveedores directos, los sistemas automatizados y la negociación acotada de los tres primeros años; la ficha `candidatura.md` conserva una selección de evidencias y límites que no incorpora por completo ese alcance.
- **Evidencia:** [[analisis-oferta]] frente a [[candidatura]].
- **Impacto:** un guion posterior podría omitir evidencia relevante o reconstruir la estrategia desde el análisis, incumpliendo el contrato de traspaso.
- **Corrección aplicada:** se sincronizó en la ficha la función de `HER-03`, las afirmaciones excluidas y el posicionamiento derivado, manteniendo los límites temporales y de responsabilidad.

### DEF-CAND-020-002

- **Clasificación:** `CASO`.
- **Criticidad:** media.
- **Estado:** resuelto.
- **Descripción:** el análisis mantiene en su argumento competitivo la condición «si se confirma la disponibilidad para turnos», aunque esta disponibilidad ya está confirmada y registrada en `datos-core-busqueda.md`.
- **Evidencia:** [[analisis-oferta]], sección 7.1, frente a la matriz de encaje y la fuente factual.
- **Impacto:** deja una advertencia obsoleta y reduce innecesariamente la claridad del traspaso.
- **Corrección aplicada:** se actualizó el argumento competitivo para reflejar la disponibilidad confirmada, sin introducir disponibilidad adicional no acreditada.

## Incertidumbres

Ninguna nueva. La disponibilidad para turnos ya está confirmada; la FP no finalizada y el alcance limitado de la experiencia de caja son límites conocidos, no incertidumbres.

## Cobertura del gate

- [x] `CAND-2026-020` cubre la continuación normal `preparar_con_advertencias`.
- [x] [Caso controlado 001](../../../../docs/ideas-y-debates/mejoras-job-up/casos-controlados/gate-candidatura-guion/caso-001-bloqueo/analisis-origen.md) comprueba `pedir_datos_adicionales_antes_de_redactar`: la ficha existe, queda `detenida`, mantiene `presentada: false` y no contiene guion ni producción documental.
- [x] [Caso controlado 002](../../../../docs/ideas-y-debates/mejoras-job-up/casos-controlados/gate-candidatura-guion/caso-002-no-recomendada/analisis-origen.md) comprueba `no_recomendada`: se conserva el análisis de trazabilidad y no existe `candidatura.md`, guion ni producción documental.

## Conclusión

La cobertura prevista del gate está completa. La persona responsable aprobó explícitamente el gate el 2026-08-05.

`GATE-CANDIDATURA-GUION: aprobado`

Queda autorizado comenzar el diseño de `PLAYBOOK_GUION_ADAPTACION_CV`. Esta aprobación no autoriza todavía la generación documental ni el envío de la candidatura.
