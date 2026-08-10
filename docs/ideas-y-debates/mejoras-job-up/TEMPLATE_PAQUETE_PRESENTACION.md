---
id: paquete-presentacion-CAND-AAAA-NNN
tipo: paquete_presentacion
version: "1.0.0"
estado: pendiente_de_preparacion
gate: GATE-CANDIDATURA-PRESENTACION
presentada: false
---

# Paquete de presentación — CAND-AAAA-NNN

Este artefacto coordina la candidatura completa después de validar los
artefactos individuales. El paquete mínimo siempre contiene CV y carta de
presentación. No sustituye a `candidatura.md`, no redacta la carta ni autoriza
por sí mismo un envío.

## 1. Identificación

| Campo | Valor |
| --- | --- |
| Candidatura | `CAND-AAAA-NNN` |
| Empresa | |
| Puesto | |
| Estado del paquete | `pendiente_de_preparacion` |
| Presentada | `false` |

## 2. Canal de presentación

| Campo | Valor |
| --- | --- |
| Canal | `indeed` / `portal_empresa` / `email` / `otro` |
| URL u origen | |
| Fecha de comprobación | |
| Requisitos del canal | |
| Cuenta o sesión necesaria | |

El canal u origen se registra cuando se conoce, pero la auditoría o el
formulario concreto del portal no son una precondición general del paquete
mínimo. No se infieren requisitos a partir del nombre de la empresa.

## 3. Artefactos requeridos por el canal

| Artefacto | ¿Requerido? | Estado | Revisión o gate | Enlace |
| --- | --- | --- | --- | --- |
| CV PDF | sí | | `GATE-VEREDICTO-CV` | |
| CV DOCX | según canal | | | |
| Carta | sí | | módulo de carta propio | |
| Email de presentación | según canal | | revisión propia | |
| Respuestas de formulario | según canal | | revisión propia | |
| Otros | | | | |

Un artefacto marcado como requerido no puede quedar vacío, pendiente o
sin revisión cuando se abra el gate completo.

## 4. Revisión de integridad del paquete

- [ ] El canal u origen conocido está registrado.
- [ ] El CV tiene `GATE-VEREDICTO-CV` aprobado.
- [ ] El CV y la carta existen y tienen su revisión o gate propio.
- [ ] No se ha añadido ningún hecho no acreditado.
- [ ] La ficha `candidatura.md` enumera todos los artefactos operativos.
- [ ] `presentada: false` sigue reflejando un hecho real.

Los formularios, credenciales, cargas y pasos específicos de un portal quedan
bajo responsabilidad de la persona responsable y no se completan como parte
del flujo general de Job-up.

## 5. Gate de candidatura completa

```yaml
gate: GATE-CANDIDATURA-PRESENTACION
estado: pendiente_de_preparacion
recomendacion: no_abrir
decision_humana:
  estado: pendiente
  fecha:
  decidido_por:
  observaciones:
```

Solo se puede usar `listo_para_gate` cuando el CV y la carta estén completos y
revisados y las casillas aplicables estén completadas. La decisión `aprobado`
autoriza a la persona responsable a presentar manualmente la candidatura; no
cambia `presentada` por sí sola.

## 6. Evidencia de presentación

Se completa únicamente después de una acción real:

```yaml
estado: presentado
presentada: true
evidencia:
  canal:
  fecha_hora:
  ejecutado_por:
  confirmacion:
  referencia_externa:
```

Sin evidencia de envío, el estado debe permanecer en `presentada: false`.
