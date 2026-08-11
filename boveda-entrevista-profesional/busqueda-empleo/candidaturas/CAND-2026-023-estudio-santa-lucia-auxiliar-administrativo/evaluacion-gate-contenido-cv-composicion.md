---
id: evaluacion-gate-contenido-cv-composicion-CAND-2026-023
tipo: evaluacion_gate_contenido_cv_composicion
candidatura: CAND-2026-023
gate: GATE-CONTENIDO-CV-COMPOSICION
datos_generacion_evaluados: "[[busqueda-empleo/candidaturas/CAND-2026-023-estudio-santa-lucia-auxiliar-administrativo/datos-generacion|datos-generacion]]"
guion_origen: "[[busqueda-empleo/candidaturas/CAND-2026-023-estudio-santa-lucia-auxiliar-administrativo/guion-adaptacion-cv|guion-adaptacion-cv]]"
fecha_evaluacion: 2026-08-11
resultado_evaluacion: apto_con_advertencias
recomendacion_ia: aprobar
decision_humana: aprobado
estado_gate: aprobado
fecha_decision_humana: 2026-08-11
sesion: sesion-20260805-1757-job-up
---

# Evaluación del gate de contenido CV — CAND-2026-023

## Resultado técnico

`datos-generacion.json` es JSON válido y materializa el guion aprobado para la
oferta de auxiliar administrativo/a. El contenido mantiene el foco en
administración, documentación, organización, Excel, comunicación y apoyo a
procesos. Las unidades profesionales trazan al guion y a las fuentes
autorizadas.

| Criterio | Resultado | Evidencia |
| --- | --- | --- |
| Precondiciones, idioma y JSON | conforme | Gate de guion CV aprobado; idioma `es`; serialización JSON y validador de contrato correctos. |
| Datos privados | conforme | Nombre, apellido 1, email, teléfono, ubicación y fotografía autorizados; apellido 2 y LinkedIn omitidos. La fotografía solo consta como recurso técnico en control. |
| Cobertura, orden y trazabilidad | conforme | M-001 a M-012 y M-015 están materializados; M-013 y M-014 permanecen omitidos según el guion. |
| Factualidad | conforme | Se preservan cargos, fechas, evidencias y métricas de HER-01, HER-02, HER-06, COMP-01 y GRAN-01. |
| Seniority y tono | conforme | La apertura prioriza tareas administrativas y documentación; la dirección histórica queda contextualizada sin ocultarse. |
| Restricciones y léxico | conforme | No se afirma experiencia inmobiliaria, anuncios, software de fincas ni perfil junior ficticio. |
| Frontera de artefacto | conforme | Solo contiene contenido CV; no incluye carta, composición, instrucciones visuales ni acciones externas. |

## Advertencias activas

- La trayectoria directiva puede producir percepción de sobrecualificación; la composición debe respetar el orden y la jerarquía del JSON sin reescribir.
- La experiencia inmobiliaria, la publicación de anuncios y el software de fincas no están acreditados y no aparecen.
- La aprobación de este gate no autoriza la revisión humana, el veredicto final ni la presentación externa.

## Recomendación y decisión

- **Resultado técnico:** `apto_con_advertencias`.
- **Recomendación de IA:** `aprobar`.
- **Decisión humana:** `aprobado`.
- **Estado oficial del gate:** `aprobado`.

La aprobación humana de este gate autorizó únicamente la composición técnica
del CV conforme al contenido literal. La composición ya produjo `cv.docx`,
`cv.pdf` y `cv.tex`. No autoriza todavía la revisión humana, el veredicto final,
la carta ni la presentación externa.
