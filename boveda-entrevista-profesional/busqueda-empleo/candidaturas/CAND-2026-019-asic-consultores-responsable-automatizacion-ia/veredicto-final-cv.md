---
id: veredicto-final-cv-CAND-2026-019
tipo: veredicto_final_cv
version_playbook: "1.1.0"
fecha_evaluacion: 2026-08-08
estado_veredicto: completado
resultado_global: no_competitivo
gate_salida: GATE-VEREDICTO-CV
---

# Veredicto final del CV — CAND-2026-019

## Identificación y alcance

| Campo | Valor |
| --- | --- |
| Candidatura | `CAND-2026-019` |
| Empresa | ASIC CONSULTORES CANARIAS |
| Puesto | Responsable de Automatización e Inteligencia Artificial |
| CV evaluado | `cv.pdf` |
| Huella SHA-256 | `b8f0906d1503e548c8030fcfb066ed18c306d335cddcc59c7063f8464eea96e0` |
| Revisión humana previa | `revision-humana-cv.md` — `aprobado_para_veredicto` |
| Presentada | `false` |

Este documento evalúa el CV actual y no autoriza por sí mismo la presentación.
El veredicto histórico del flujo anterior se conserva en
`historico/veredicto-final-cv-flujo-anterior.md` y no se reutiliza.

## Fuentes y responsabilidades

| Fuente | Uso |
| --- | --- |
| `cv.pdf` | Evidencia visual y contenido finalmente compuesto. |
| `cv.docx` / `cv.tex` | Comprobación de coherencia entre salidas del compositor. |
| `revision-humana-cv.md` | Confirmación de revisión humana y huella del PDF. |
| `manifest-generacion-cv.json` | Identidad de candidatura, contrato y artefactos. |
| `gate-contenido-cv.md` | Confirmación de que el contenido fue aprobado antes de componer. |
| `datos-core-busqueda.md`, `analisis-oferta.md`, `candidatura.md`, `guion-adaptacion-cv.md` | Trazabilidad de estrategia y hechos, no nuevas decisiones editoriales. |

El Rol A verifica integridad, fidelidad y trazabilidad. El Rol B realiza la
revisión humana previa. La persona responsable conserva la autoridad sobre el
gate de presentación y el envío.

## Precondiciones

- [x] `revision-humana-cv.md` existe y contiene `aprobado_para_veredicto`.
- [x] La huella de `cv.pdf` coincide con la revisión humana.
- [x] `cv.docx`, `cv.pdf` y `cv.tex` existen y pertenecen a la candidatura.
- [x] `manifest-generacion-cv.json` y `gate-contenido-cv.md` existen.
- [x] Las fuentes declaradas son resolubles.
- [x] `seguimiento.md` mantiene `presentada: false`.
- [x] La autorización de datos del CV está resuelta para este artefacto.

## Integridad técnica

| Comprobación | Resultado | Evidencia |
| --- | --- | --- |
| Huella SHA-256 de `cv.pdf` | apta | Coincide con la registrada en la revisión humana. |
| Artefactos de salida | apta | DOCX, PDF y TEX presentes. |
| Publicación transaccional | apta | No se detecta publicación parcial ni sustitución durante la evaluación. |
| Estado de presentación | apta | `presentada: false`; no se ha realizado envío. |

**Resultado de integridad: `apta`.**

## Fidelidad al contenido y a la estrategia

| Dimensión | Resultado | Observación |
| --- | --- | --- |
| Contenido literal | apta | El texto visible corresponde al contenido CV aprobado. |
| Posicionamiento | apta | El CV mantiene el posicionamiento elegido para la candidatura. |
| Evidencias | apta | Las afirmaciones utilizadas son trazables a las fuentes declaradas. |
| Datos privados | apta | Solo aparecen los datos autorizados en el bloque de privacidad. |

**Resultado de fidelidad: `apta`.**

## Evaluación de criterios

| Criterio | Puntuación (1–5) | Evidencia y diagnóstico |
| --- | ---: | --- |
| C1. Encaje con la oferta | 4 | El CV presenta automatización, operaciones y mejora de procesos, pero no acredita todo el perfil solicitado. |
| C2. Evidencia diferencial | 2 | No se acredita experiencia profesional aplicada con el ecosistema principal de la oferta: Power Automate, Power Apps, Copilot Studio, Azure AI, Dynamics 365 Business Central o Salesforce. |
| C3. Claridad y jerarquía | 3 | La lectura es clara, aunque el encaje específico con ASIC queda limitado por la distancia entre experiencia y requisitos técnicos. |
| C4. Credibilidad y trazabilidad | 4 | La experiencia descrita es verificable y no se detectan afirmaciones inventadas. |
| C5. Riesgo de interpretación | 4 | El CV evita sobreafirmar dominio de tecnologías no acreditadas; persiste riesgo de descarte por requisitos esenciales. |
| C6. Presentabilidad técnica | 5 | Una página, composición estable, fotografía y datos de contacto visibles; revisión humana aprobada. |
| **Media orientativa** | **3,7** | La media no supera las carencias materiales de encaje. |

## Diagnóstico consolidado

La integridad y la fidelidad del CV son aptas. Sin embargo, el encaje
competitivo es insuficiente para esta oferta: no existe evidencia acreditada de
experiencia aplicada en las plataformas y productos centrales solicitados, y la
formación reglada indicada no está finalizada. La experiencia histórica en
Power BI tampoco compensa por sí sola esas carencias.

No procede regenerar el CV: no se ha detectado un defecto de composición ni una
inexactitud factual. El problema es de competitividad frente a requisitos
materiales de la oferta.

## Enrutamiento y resultado

```yaml
resultado_global: no_competitivo
recomendacion: no_aprobar
accion: no_presentar
regeneracion_cv: no_necesaria
motivo: carencias_materiales_de_encaje_tecnologico_y_formativo
```

## Gate de salida

```yaml
gate: GATE-VEREDICTO-CV
recomendacion_gate: no_aprobar
decision_humana:
  estado: bloqueado
  fecha: 2026-08-09
  decidido_por: persona_responsable
  observaciones: Gate bloqueado; no avanzar a presentación por resultado no_competitivo.
```

El gate queda bloqueado por decisión de la persona responsable. La candidatura
no avanza a presentación, no cambia a enviada y no se realiza ningún envío.

## Control de vigencia

Si cambia el PDF, la revisión humana, la evidencia factual, el análisis, la
candidatura o el guion, este veredicto queda invalidado y debe regenerarse
completamente desde los artefactos sincronizados.
