---
id: veredicto-final-cv-CAND-2026-023
tipo: veredicto_final_cv
version_playbook: "1.1.0"
fecha_evaluacion: 2026-08-11
estado_veredicto: completado
gate_salida: GATE-VEREDICTO-CV
---

# Veredicto final del CV — CAND-2026-023

## 1. Identificación y versión

| Campo | Valor |
| --- | --- |
| Candidatura | `CAND-2026-023` |
| Empresa | ESTUDIO SANTA LUCIA DE TIRAJANA, S. L. / Tecnocasa Gáldar |
| Puesto | Auxiliar administrativo/a SIN EXPERIENCIA |
| CV evaluado | `cv.pdf` |
| Fecha de generación | 2026-08-11 |
| Fecha del veredicto | 2026-08-11 |
| Huella SHA-256 del PDF | `f88882af3dec319875545399bc67506ca0fae8d1f686ee1fa541eb6681434a9e` |
| Páginas | 1 |
| Revisión humana de origen | `revision-humana-cv.md` — `aprobado_para_veredicto` |
| Coincidencia de huella | `sí` |

El veredicto corresponde exclusivamente a la versión del PDF identificada por
la huella anterior.

## 2. Fuentes y roles

Se consultaron `cv.pdf`, `cv.docx`, `cv.tex`, `datos-generacion.json`,
`guion-adaptacion-cv.md`, `candidatura.md`, `analisis-oferta.md`,
`datos-core-busqueda.md`, `datos-privados-candidatura.md`,
`evaluacion-gate-contenido-cv-composicion.md` y
`manifest-generacion-cv.json`.

```yaml
rol_recruiter:
  aplicado: sí
rol_auditor_flujo:
  aplicado: sí
```

## 3. Precondiciones e identidad

- [x] Existen el PDF, DOCX, LaTeX, JSON, guion, ficha y análisis.
- [x] Las fuentes factuales y la autorización privada están disponibles.
- [x] `GATE-CONTENIDO-CV-COMPOSICION` está aprobado.
- [x] La composición terminó correctamente.
- [x] Existe `revision-humana-cv.md` con decisión `aprobado_para_veredicto`.
- [x] La huella de la revisión coincide con el PDF evaluado.
- [x] `presentada: false`.

```yaml
precondiciones:
  resultado: cumplidas
  bloqueos: []
revision_humana_origen:
  artefacto: revision-humana-cv.md
  decision: aprobado_para_veredicto
  huella_cv: f88882af3dec319875545399bc67506ca0fae8d1f686ee1fa541eb6681434a9e
huella_evaluada: f88882af3dec319875545399bc67506ca0fae8d1f686ee1fa541eb6681434a9e
coincide: sí
```

## 4. Capa 1 — Integridad

```yaml
integridad:
  resultado: apta
```

El CV mantiene cargos, fechas, formación, logros y herramientas respaldados por
las fuentes. La experiencia en documentación, Excel, procesos, atención y
gestión comercial se presenta como transferible, no como experiencia
inmobiliaria. No se introducen anuncios, software de fincas, experiencia en
Tecnocasa ni requisitos no acreditados. Los datos privados incluidos se limitan
a nombre, apellido 1, email, teléfono, ubicación y fotografía autorizados;
apellido 2 y LinkedIn no aparecen.

**Dictamen:** integridad apta; no hay incidencias bloqueantes.

## 5. Capa 2 — Fidelidad al flujo

```yaml
fidelidad_flujo:
  resultado: apta
```

| Comprobación | Resultado | Evidencia |
| --- | --- | --- |
| Estrategia reconocible | sí | Administración y gestión documental ocupan el posicionamiento principal. |
| Inclusiones prioritarias | sí | Organización, Excel, documentación, seguimiento, atención y apoyo a procesos aparecen. |
| Omisiones y advertencias | sí | No se afirma experiencia inmobiliaria ni se ocultan cargos históricos. |
| Orden y seniority | sí | El CV prioriza ejecución administrativa y contextualiza la dirección histórica. |
| JSON → CV | sí | No se observan adiciones, pérdidas, traducciones ni reescrituras semánticas. |
| Composición | sí | PDF de una página, equivalente al DOCX y al modelo LaTeX, sin cortes ni solapamientos. |

## 6. Privacidad

| Campo | Autorización | Observado | Conforme |
| --- | --- | --- | --- |
| Nombre | incluir | Gustavo | sí |
| Apellido 1 | incluir | Vega | sí |
| Apellido 2 | omitir | ausente | sí |
| Email | incluir | visible | sí |
| Teléfono | incluir | visible | sí |
| LinkedIn | omitir | ausente | sí |
| Ubicación | incluir | Las Palmas | sí |
| Fotografía | incluir | visible | sí |

## 7. Capa 3 — Evaluación recruiter

| Criterio | Nota | Evidencia y diagnóstico |
| --- | ---: | --- |
| C1 — Primer escaneo y posicionamiento | 4 | El encabezado identifica administración, gestión documental, organización y Excel. |
| C2 — Encaje competitivo real | 3 | Las capacidades son transferibles y la oferta no exige experiencia, pero no hay experiencia inmobiliaria específica y existe riesgo de sobrecualificación. |
| C3 — Cobertura ATS respaldada | 4 | Incluye administración, documentación, procesos, Excel, atención y organización sin añadir keywords no acreditadas. |
| C4 — Fuerza de la evidencia | 4 | Incluye sistemas documentales, informes Excel y mejora de tiempos de 20 a 3 minutos. |
| C5 — Adecuación narrativa y seniority | 3 | Se conserva la trayectoria de Director Ejecutivo y se orienta a ejecución, pero puede persistir percepción de sobrecualificación. |
| C6 — Calidad documental y visual | 5 | PDF de una página, legible, equilibrado, con fotografía autorizada y sin defectos visibles. |

```yaml
media_recruiter: 3.8
```

La media es informativa y no gobierna la precedencia.

## 8. Diagnóstico competitivo

### Fortalezas

1. Experiencia acreditada en documentación, organización y seguimiento de procesos.
2. Excel aplicado a informes económicos y mejora medible de tiempos.
3. Posicionamiento administrativo claro y ausencia de experiencia previa exigida por la oferta.

### Debilidades no corregibles solo con redacción

1. No consta experiencia literal en inmobiliaria, Tecnocasa o publicación de anuncios.
2. La trayectoria de Director Ejecutivo puede generar sobrecualificación percibida.
3. No consta experiencia con software específico de una oficina inmobiliaria.

| Hallazgo | Clasificación | Acción |
| --- | --- | --- |
| Claridad del posicionamiento administrativo | corregible_con_evidencia_existente | Mantener la composición actual. |
| Experiencia inmobiliaria específica | no_corregible_sin_nueva_evidencia | No maquillarla ni añadir keywords. |
| Riesgo de sobrecualificación | no_corregible_sin_nueva_evidencia | Mantener el cargo histórico y el enfoque operativo. |

## 9. Defectos y enrutamiento

`ninguno` en integridad, fidelidad o composición. Las debilidades competitivas
anteriores pertenecen a `competitividad_no_corregible` y no justifican regenerar
el CV sin nueva evidencia.

## 10. Resultado global

```yaml
resultado_global: revisar_antes_de_presentar
regeneracion:
  necesaria: no
  motivo: ""
  capa_origen: competitividad_no_corregible
  artefactos_downstream_a_regenerar: []
recomendacion_gate: no_aprobar
```

El CV es íntegro y fiel al flujo, pero el encaje competitivo requiere revisión
humana antes de cualquier decisión de avance. El resultado no implica que exista
carta, paquete o presentación autorizada.

## 11. Gate y decisión humana

```yaml
gate: GATE-VEREDICTO-CV
estado_gate: aprobado
decision_humana:
  estado: aprobado
  fecha: 2026-08-11
  decidido_por: persona_responsable
  observaciones: Se aprueba el CV pese a las advertencias de encaje condicionado y sobrecualificación; la decisión autoriza únicamente el avance documental del CV.
```

La decisión humana aprueba este gate pese a las advertencias de encaje
condicionado y sobrecualificación. No autoriza carta, paquete ni presentación
externa.

## 12. Control final e invalidación

- [x] Integridad, privacidad y trazabilidad contrastadas.
- [x] Estrategia, guion, JSON y composición contrastados.
- [x] PDF real revisado visualmente y aprobado por la persona responsable.
- [x] C1–C6 evaluados y debilidades clasificadas.
- [x] Resultado global único emitido respetando la precedencia.
- [x] Decisión humana del gate registrada sin simulación.

```yaml
version_cv:
  material_regenerado: no
  revision_humana_anterior_vigente: sí
  veredicto_anterior_vigente: no_aplica
```

Una regeneración material posterior exige nueva revisión humana y nuevo
veredicto.
