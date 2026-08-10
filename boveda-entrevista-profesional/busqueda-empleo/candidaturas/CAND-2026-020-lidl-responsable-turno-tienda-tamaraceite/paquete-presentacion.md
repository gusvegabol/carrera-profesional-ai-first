---
id: paquete-presentacion-CAND-2026-020
tipo: paquete_presentacion
version: "1.0.0"
estado: pendiente_de_preparacion
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
| Estado del paquete | `pendiente_de_preparacion` |
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
| Contenido semántico de carta | sí | generado_apto | `GATE-CONTENIDO-CARTA-COMPOSICION` pendiente | [[contenido-carta-presentacion]] |
| Carta DOCX/PDF | sí | no compuesta | composición y revisión pendientes | — |
| Email de presentación | no aplica salvo que el canal lo exija | no creado | revisión propia pendiente | — |
| Respuestas de formulario | según canal; responsabilidad de la persona responsable | no gestionadas por Job-up | fuera del paquete mínimo | — |

## 4. Estado del gate completo

```yaml
gate: GATE-CANDIDATURA-PRESENTACION
  estado: no_abierto
  recomendacion: no_abrir
  decision_humana:
  estado: pendiente
  fecha:
  decidido_por:
  observaciones: Canal de empresa identificado; el contenido semántico de la carta está apto, pero su composición y revisión siguen pendientes. La inscripción y cualquier formulario los realizará la persona responsable.
```

## 5. Comprobaciones pendientes

- [x] Comprobar el canal de envío real desde Indeed.
- [x] Registrar el paquete mínimo obligatorio: CV + carta.
- [x] Mantener explícitamente documentada la discrepancia salarial entre Indeed y el portal de Lidl.
- [x] Diseñar y ejecutar el módulo específico de carta de presentación.
- [x] Resolver la interacción humana del guion de carta.
- [x] Registrar la aprobación humana de `GATE-GUION-CARTA-CONTENIDO` y generar el contenido semántico.
- [ ] Componer y revisar la carta de presentación.
- [ ] Actualizar la ficha de candidatura con todos los artefactos operativos.
- [ ] Abrir `GATE-CANDIDATURA-PRESENTACION` solo cuando el paquete esté completo.

No se ha realizado ningún envío y `presentada` permanece en `false`.
