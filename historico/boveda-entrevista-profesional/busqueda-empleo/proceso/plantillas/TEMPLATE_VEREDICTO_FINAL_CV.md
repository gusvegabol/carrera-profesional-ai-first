---
id: template-veredicto-final-cv
tipo: veredicto_final_cv
proposito: evaluar_integridad_calidad_y_decision_del_cv
version: "1.1.0"
estado: vigente
fecha_version: 2026-07-29
---

# Veredicto final del CV

> Completar después de generar y revisar el CV, antes de consolidar la candidatura como `pendiente_de_aprobacion`. El veredicto no autoriza ningún envío.

## Identificación y trazabilidad

- **Candidatura:**
- **Versión de CV evaluada:**
- **Oferta y fecha de evaluación:**
- **Fuentes revisadas:** [[datos-core-busqueda]], análisis de oferta y guion de adaptación.
- **Revisión humana:** `revision-humana-cv.md`.
- **Huella SHA-256 del `cv.pdf`:**
- **Coincidencia de huella:** `sí` | `no`.

## Integridad factual y de privacidad

**Resultado:** `apta` | `no_apta`

| Comprobación | Resultado | Evidencia o incidencia | Corrección necesaria |
| --- | --- | --- | --- |
| Cada afirmación del CV puede rastrearse a la fuente factual |  |  |  |
| Los datos privados utilizados están autorizados para esta candidatura |  |  |  |
| No aparece histórico municipal restringido ni actividad independiente no autorizada |  |  |  |
| Las decisiones colegiadas no se atribuyen como decisiones individuales |  |  |  |
| Titulaciones, idiomas, tecnología, métricas y nivel de dominio no superan lo documentado |  |  |  |
| Los requisitos no acreditados no se presentan como cumplidos |  |  |  |

Si la huella de la revisión humana no coincide con el PDF, el veredicto queda
`bloqueado` y no se emite ninguna salida global.

> Si alguna comprobación resulta negativa, el resultado es `no_apta` y la decisión debe ser `corregir_antes_de_revisar`, sin importar las notas de calidad.

## Calidad del contenido

| Criterio | Nota (1–5) | Evidencia observada en el CV | Debilidad concreta | Mejora prioritaria | Límite factual de la mejora |
| --- | --- | --- | --- | --- | --- |
| Primer escaneo y posicionamiento |  |  |  |  |  |
| Encaje competitivo |  |  |  |  |  |
| Cobertura ATS respaldada |  |  |  |  |  |
| Fuerza de la experiencia |  |  |  |  |  |
| Adecuación narrativa |  |  |  |  |  |
| Calidad documental y visual |  |  |  |  |  |

### Escala común

| Nota | Significado |
| --- | --- |
| 1 | Deficiente: requiere reescritura. |
| 2 | Débil: requiere corrección prioritaria. |
| 3 | Correcta: cumple el mínimo, pero puede ganar especificidad, claridad o competitividad. |
| 4 | Sólida: clara, pertinente y creíble; admite mejoras menores. |
| 5 | Excelente: específica, diferenciada y plenamente respaldada para esta oferta. |

## Resultado global y decisión de veredicto

- **Media orientativa:**
- **Decisión:** `corregir_antes_de_revisar` | `revisar_antes_de_aprobar` | `lista_para_aprobacion_humana`

El resultado global solo puede ser `bloqueado_por_integridad`,
`requiere_correccion_de_flujo`, `no_competitivo`,
`revisar_antes_de_presentar` o `apto_para_presentacion`. La media es informativa.

Gate CV-only: `GATE-VEREDICTO-CV`.

```yaml
recomendacion_gate: aprobar | no_aprobar
decision_humana:
  estado: pendiente | aprobado | bloqueado
```

Este gate valida exclusivamente el CV. No sustituye `GATE-CANDIDATURA-PRESENTACION`
ni autoriza carta, email, formulario o envío.

Aplicar estas reglas, sin usar la media como puerta de salida:

- `corregir_antes_de_revisar`: integridad `no_apta` o una o más notas de 1 o 2.
- `revisar_antes_de_aprobar`: integridad `apta`, todas las notas son al menos 3 y existe alguna nota de 3.
- `lista_para_aprobacion_humana`: integridad `apta` y las cinco notas son 4 o 5.

## Cambios antes de la siguiente versión

- **Obligatorios:**
- **Recomendados:**

## Investigación contextual opcional posterior

> Esta investigación no modifica ni retrasa el veredicto inicial. Solo se inicia si la persona responsable la autoriza para esta candidatura.

- **Qué se propone investigar:**
- **URLs propuestas antes de consultar:**
- **Autorización de la persona responsable:** pendiente | autorizada | rechazada
- **URL utilizadas, si se autorizó:**
- **Recomendaciones contextuales verificadas:**
- **Documentos que deben ajustar el tono, si procede:** CV y carta de presentación | ninguno
- **¿Se requiere nueva versión y nuevo veredicto?:** sí | no

No atribuir a la empresa valores, prácticas, cultura o expectativas que no estén respaldados por una URL identificada. Si la investigación justifica adaptar el lenguaje corporativo, el mismo criterio debe aplicarse coherentemente al CV y a la carta de presentación, sin añadir hechos, funciones, tecnologías, métricas o resultados no acreditados. La ausencia de contexto externo verificado no reduce ninguna nota del CV.
