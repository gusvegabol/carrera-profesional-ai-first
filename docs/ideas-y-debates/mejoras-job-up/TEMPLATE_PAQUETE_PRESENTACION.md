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
artefactos individuales. No sustituye a `candidatura.md`, no redacta carta ni
autoriza por sí mismo un envío.

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

El canal debe estar identificado antes de abrir `GATE-CANDIDATURA-PRESENTACION`.
No se infieren requisitos a partir del nombre de la empresa.

## 3. Artefactos requeridos por el canal

| Artefacto | ¿Requerido? | Estado | Revisión o gate | Enlace |
| --- | --- | --- | --- | --- |
| CV PDF | sí | | `GATE-VEREDICTO-CV` | |
| CV DOCX | según canal | | | |
| Carta | según canal | | módulo de carta propio | |
| Email de presentación | según canal | | revisión propia | |
| Respuestas de formulario | según canal | | revisión propia | |
| Otros | | | | |

Un artefacto marcado como requerido no puede quedar vacío, pendiente o
sin revisión cuando se abra el gate completo.

## 4. Revisión de integridad del paquete

- [ ] El canal y su origen están comprobados.
- [ ] Los requisitos del canal están documentados.
- [ ] El CV tiene `GATE-VEREDICTO-CV` aprobado.
- [ ] Cada artefacto requerido existe y tiene su revisión o gate propio.
- [ ] No se ha añadido ningún hecho no acreditado.
- [ ] La ficha `candidatura.md` enumera todos los artefactos operativos.
- [ ] `presentada: false` sigue reflejando un hecho real.

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

Solo se puede usar `listo_para_gate` cuando todas las casillas anteriores estén
completadas. La decisión `aprobado` autoriza el paso a una instrucción humana de
presentación; no cambia `presentada` por sí sola.

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
