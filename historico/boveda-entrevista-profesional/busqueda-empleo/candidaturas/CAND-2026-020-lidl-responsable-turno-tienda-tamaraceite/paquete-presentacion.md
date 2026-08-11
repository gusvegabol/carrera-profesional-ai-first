---
id: paquete-presentacion-CAND-2026-020
tipo: paquete_presentacion
version: "1.0.0"
estado: listo_para_gate
gate: GATE-CANDIDATURA-PRESENTACION
presentada: false
---

# Paquete de presentación — CAND-2026-020

## 1. Identificación

| Campo | Valor |
| --- | --- |
| Candidatura | `CAND-2026-020` |
| Empresa | Lidl Supermercados SAU |
| Puesto | Responsable de turno Tienda 40h Tamaraceite |
| Estado del paquete | `listo_para_gate` |
| Presentada | `false` |

## 2. Canal de presentación

| Campo | Valor |
| --- | --- |
| Canal | `portal_empresa` (acceso desde Indeed) |
| URL u origen | Indeed redirige a <https://empleo.lidl.es/jobs/responsable-de-turno-tienda-40h-tamaraceite-las-palmas-de-gran-canaria-gran-canaria-725913> |
| Fecha de comprobación | 2026-08-09 |
| Requisitos del canal | El paquete Job-up exige como mínimo CV y carta; la inscripción concreta del portal Lidl queda bajo responsabilidad de la persona responsable. |
| Cuenta o sesión necesaria | Pendiente de comprobar; el portal muestra acceso «Registrarme» mediante SuccessFactors. |

La oferta de Indeed muestra «Solicitar en la página de la empresa» y conduce al
portal de empleo de Lidl. Por tanto, el canal queda identificado como portal de
empresa. Los requisitos concretos del formulario y de la cuenta no son una
precondición del paquete mínimo y los gestionará la persona responsable.

La inspección del formulario no se continuó porque no forma parte de la
preparación mínima. No se aceptó ni rechazó ninguna preferencia, no se inició
sesión y no se introdujeron datos personales.

### 2.1 Discrepancias y datos adicionales de la fuente de empresa

La página de Lidl consultada desde Indeed identifica la referencia `725913`,
contrato indefinido, jornada completa y la dirección Hermanos Domínguez Santana
s/n, 35018 Las Palmas de Gran Canaria. También muestra un salario de 25.000 € a
29.000 € brutos anuales, mientras que la copia de Indeed conserva 18.800 € a
21.000 € anuales. Ambas cifras se mantienen con su procedencia; no se elige una
ni se incorpora ninguna como afirmación estratégica de la candidatura.

## 3. Artefactos requeridos por el canal

| Artefacto | ¿Requerido? | Estado | Revisión o gate | Enlace |
| --- | --- | --- | --- | --- |
| CV PDF | sí | disponible | `GATE-VEREDICTO-CV` aprobado | [[cv.pdf]] |
| CV DOCX | según canal | disponible | `GATE-VEREDICTO-CV` aprobado | [[cv.docx]] |
| Contenido semántico de carta | sí | generado_apto | `GATE-CONTENIDO-CARTA-COMPOSICION` aprobado | [[contenido-carta-presentacion]] |
| Carta DOCX | sí | generado_composicion_revision_humana_aprobada | `GATE-CARTA-REVISION-HUMANA` aprobado | [[carta-presentacion.docx]] |
| Carta PDF | sí | generado_composicion_revision_humana_aprobada | `GATE-CARTA-REVISION-HUMANA` aprobado | [[carta-presentacion.pdf]] |
| Evaluación de composición | sí | apta_revision_humana_aprobada | `GATE-CARTA-REVISION-HUMANA` aprobado | [[evaluacion-composicion-carta-presentacion]] |
| Veredicto final de carta | sí | APTA; incluir | `GATE-VEREDICTO-CARTA` aprobado | [[veredicto-final-carta]] |
| Evaluación de presentación | sí | en_evaluacion | `GATE-CANDIDATURA-PRESENTACION` pendiente | [[evaluacion-presentacion-candidatura]] |
| Email de presentación | no aplica salvo que el canal lo exija | no creado | revisión propia pendiente | — |
| Respuestas de formulario | según canal; responsabilidad de la persona responsable | no gestionadas por Job-up | fuera del paquete mínimo | — |

## 4. Estado del gate completo

```yaml
gate: GATE-CANDIDATURA-PRESENTACION
  estado: pendiente
  recomendacion: validar_presentacion
  decision_humana: apertura_de_validacion
  fecha: 2026-08-11
  decidido_por: persona_responsable
  observaciones: Canal de empresa identificado. `GATE-CARTA-REVISION-HUMANA` y `GATE-VEREDICTO-CARTA` están aprobados humanamente el 2026-08-10. La persona responsable abrió el gate en `pendiente` para validar presentación. La inscripción y cualquier formulario los realizará la persona responsable.
```

## 5. Comprobaciones pendientes

- [x] Comprobar el canal de envío real desde Indeed.
- [x] Registrar el paquete mínimo obligatorio: CV + carta.
- [x] Mantener explícitamente documentada la discrepancia salarial entre Indeed y el portal de Lidl.
- [x] Diseñar y ejecutar el módulo específico de carta de presentación.
- [x] Resolver la interacción humana del guion de carta.
- [x] Registrar la aprobación humana de `GATE-GUION-CARTA-CONTENIDO` y generar el contenido semántico.
- [x] Componer la carta de presentación y generar DOCX/PDF equivalentes.
- [x] Actualizar la ficha de candidatura con todos los artefactos operativos.
- [x] Aprobar mediante una nueva decisión `GATE-CARTA-REVISION-HUMANA` la carta regenerada.
- [x] Revisar humanamente la carta y registrar su resultado.
- [x] Diseñar e implantar el veredicto final de la carta.
- [x] Resolver la propagación del gate de revisión humana y regenerar el veredicto.
- [x] Decidir humanamente `GATE-VEREDICTO-CARTA`.
- [x] Abrir `GATE-CANDIDATURA-PRESENTACION` en `pendiente` para validar la presentación.

El paquete documental está completo, pero no equivale a autorización de envío ni
a candidatura presentada. `GATE-CANDIDATURA-PRESENTACION` permanece en `pendiente`
y `presentada` permanece en `false`.
