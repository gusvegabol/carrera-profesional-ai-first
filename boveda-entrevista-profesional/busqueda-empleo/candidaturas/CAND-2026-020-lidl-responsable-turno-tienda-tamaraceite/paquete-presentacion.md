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
| Canal de origen | Indeed |
| URL de la oferta | <https://es.indeed.com/viewjob?jk=bc1828a858d36c87> |
| Canal de envío confirmado | pendiente de comprobar |
| Fecha de comprobación | |
| Requisitos del canal | pendiente de comprobar |

La URL de la oferta no demuestra por sí sola que el canal de envío esté
resuelto. Debe comprobarse si Indeed permite postulación directa, si redirige a
Lidl y qué campos o documentos exige.

## 3. Artefactos requeridos por el canal

| Artefacto | ¿Requerido? | Estado | Revisión o gate | Enlace |
| --- | --- | --- | --- | --- |
| CV PDF | sí | disponible | `GATE-VEREDICTO-CV` aprobado | [[cv.pdf]] |
| CV DOCX | pendiente del canal | disponible | `GATE-VEREDICTO-CV` aprobado | [[cv.docx]] |
| Carta | pendiente de comprobar | no creada | módulo de carta pendiente | — |
| Email de presentación | pendiente de comprobar | no creado | revisión propia pendiente | — |
| Respuestas de formulario | pendiente de comprobar | no resueltas | revisión propia pendiente | — |

## 4. Estado del gate completo

```yaml
gate: GATE-CANDIDATURA-PRESENTACION
estado: no_abierto
recomendacion: no_abrir
decision_humana:
  estado: pendiente
  fecha:
  decidido_por:
  observaciones: Faltan canal confirmado y requisitos de carta, email o formulario.
```

## 5. Comprobaciones pendientes

- [ ] Comprobar el canal de envío real desde Indeed.
- [ ] Registrar los requisitos del canal y los campos del formulario.
- [ ] Determinar si se requiere carta, email o respuestas abiertas.
- [ ] Diseñar o ejecutar el módulo específico de los artefactos requeridos.
- [ ] Actualizar la ficha de candidatura con todos los artefactos operativos.
- [ ] Abrir `GATE-CANDIDATURA-PRESENTACION` solo cuando el paquete esté completo.

No se ha realizado ningún envío y `presentada` permanece en `false`.
