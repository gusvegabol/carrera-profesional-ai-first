---
id: veredicto-final-cv-CAND-2026-021
tipo: veredicto_final_cv
version_playbook: "1.1.0"
fecha_evaluacion: 2026-08-11
estado_veredicto: completado
gate_salida: GATE-VEREDICTO-CV
---

# Veredicto final del CV — CAND-2026-021

## 1. Identificación y versión

| Campo | Valor |
| --- | --- |
| Candidatura | `CAND-2026-021` |
| Empresa | OBRAMAT |
| Puesto | Coordinador/a de línea de Cajas Evolutivo/a |
| CV evaluado | `cv.pdf` |
| Fecha de generación | 2026-08-11 |
| Fecha del veredicto | 2026-08-11 |
| Huella SHA-256 del PDF | `818f44552896c7b673ec9e6a7fb151b09f10a5e38a1e993d3f595f02e39cf18f` |
| Páginas | 1 |
| Revisión humana de origen | [[revision-humana-cv]] — `aprobado_para_veredicto` |
| Coincidencia de huella | `sí` |

El veredicto corresponde exclusivamente a la versión del PDF identificada por
la huella anterior.

## 2. Fuentes consultadas

| Fuente | Función | Consultada |
| --- | --- | --- |
| `cv.pdf` | Artefacto principal evaluado | sí |
| `cv.docx` | Control técnico | sí |
| `cv.tex` | Control de equivalencia | sí |
| `datos-generacion.json` | Contenido previo a composición | sí |
| `guion-adaptacion-cv.md` | Decisiones editoriales | sí |
| `candidatura.md` | Estrategia y privacidad | sí |
| `analisis-oferta.md` | Requisitos y encaje | sí |
| `datos-core-busqueda.md` | Factualidad profesional | sí |
| `datos-privados-candidatura.md` | Datos privados autorizables | sí |
| `evaluacion-gate-contenido-cv-composicion.md` | Gate de entrada | sí |
| `manifest-generacion-cv.json` | Control técnico de publicación | sí |

## 3. Roles aplicados

```yaml
rol_recruiter:
  aplicado: sí
rol_auditor_flujo:
  aplicado: sí
```

## 4. Precondiciones

- [x] Existen `cv.pdf`, `cv.docx`, `cv.tex` y `datos-generacion.json`.
- [x] Existen `guion-adaptacion-cv.md`, `candidatura.md` y `analisis-oferta.md`.
- [x] Las fuentes factuales y privadas necesarias son accesibles.
- [x] Existe autorización vigente de datos privados.
- [x] `GATE-CONTENIDO-CV-COMPOSICION` está aprobado.
- [x] La composición terminó correctamente.
- [x] Existe `revision-humana-cv.md` con decisión `aprobado_para_veredicto`.
- [x] La huella revisada coincide con el PDF evaluado.
- [x] La candidatura mantiene `presentada: false`.

```yaml
precondiciones:
  resultado: cumplidas
  bloqueos: []
revision_humana_origen:
  artefacto: revision-humana-cv.md
  decision: aprobado_para_veredicto
  huella_cv: 818f44552896c7b673ec9e6a7fb151b09f10a5e38a1e993d3f595f02e39cf18f
huella_evaluada: 818f44552896c7b673ec9e6a7fb151b09f10a5e38a1e993d3f595f02e39cf18f
coincide: sí
```

## 5. Capa 1 — Integridad

```yaml
integridad:
  resultado: apta
```

| Control | Resultado | Evidencia |
| --- | --- | --- |
| Hechos profesionales respaldados | apto | Atención, equipos, tareas, pedidos, stock y cuadres remiten a HER-04, HER-06, HER-07, HER-08 y HER-10. |
| Empresas, cargos y fechas correctos | apto | Se conserva Director Ejecutivo en Herfrailes S. L. y su periodo histórico. |
| Métricas y resultados respaldados | apto | No se introducen métricas no acreditadas; la mejora de cuadres no se cuantifica. |
| Formación correctamente representada | apto | Solo aparece Bachillerato; la FP no finalizada no se presenta como título. |
| Tecnologías y niveles respaldados | apto | Excel y Trello aparecen con el alcance acreditado. |
| Formación no convertida en experiencia | apto | No se transforma formación en experiencia laboral. |
| Automatización no convertida indebidamente en IA | apto | Los sistemas de pedidos y cuadres se describen como mejoras operativas. |
| Transferibilidad no presentada como experiencia literal | apto | No se afirma haber trabajado con OBRAMAT ni con sus sistemas. |
| Responsabilidad correctamente atribuida | apto | Se limitan las afirmaciones a contribuciones individuales acreditadas. |
| Requisitos no acreditados no aparecen como cumplidos | apto | No aparecen movilidad por Canarias ni dominio del sistema de cajas de OBRAMAT. |
| Datos privados incluidos según autorización | apto | Nombre, apellido 1, email, teléfono, LinkedIn y fotografía autorizados aparecen. |
| Datos privados omitidos ausentes | apto | Apellido 2 y ubicación no aparecen. |

**Dictamen:** integridad apta. No se detectan incidencias bloqueantes ni
afirmaciones factuales nuevas.

## 6. Capa 2 — Fidelidad al flujo

```yaml
fidelidad_flujo:
  resultado: apta
```

### Estrategia → CV

| Comprobación | Resultado | Evidencia |
| --- | --- | --- |
| Posicionamiento operativo reconocible | sí | El encabezado y el perfil priorizan cajas, operaciones de tienda, atención y mejora. |
| Advertencias respetadas | sí | Se mantienen los límites sobre cargo formal, sistemas OBRAMAT y movilidad. |
| Afirmaciones excluidas respetadas | sí | No hay tesorería, banca, movilidad por Canarias ni experiencia literal en OBRAMAT. |
| Carencias no ocultadas mediante equivalencias | sí | La experiencia transferible no se convierte en cargo formal equivalente. |

### Guion → CV

| Comprobación | Resultado | Evidencia |
| --- | --- | --- |
| Inclusiones prioritarias presentes | sí | Cliente, reclamaciones, cuadres, Excel, Trello, equipos, pedidos y stock. |
| Omisiones respetadas | sí | FP no finalizada y movilidad por Canarias no aparecen. |
| Reducciones respetadas | sí | La dirección histórica queda comprimida y no domina el documento. |
| Orden estratégico conservado | sí | Perfil y experiencia operativa preceden a la continuidad histórica y formación. |
| Seniority e idioma respetados | sí | Se conserva el cargo histórico, con tono operativo y español. |
| Primer escaneo coherente | sí | El encaje con una línea de cajas es visible desde el encabezado. |

### `datos-generacion.json` → CV

| Comprobación | Resultado | Evidencia |
| --- | --- | --- |
| Contenido añadido por composición | no | No observado. |
| Contenido semántico eliminado | no | Las unidades semánticas aprobadas se conservan. |
| Reescritura o resumen autónomo | no | El compositor ordena y presenta, sin reinterpretar. |
| Fusión con cambio de significado | no | No observado. |
| Traducción no autorizada | no | El CV se mantiene en español. |

### Privacidad → CV

| Campo | Autorización | Observado | Conforme |
| --- | --- | --- | --- |
| Nombre | incluir | Gustavo | sí |
| Apellido 1 | incluir | Vega | sí |
| Apellido 2 | omitir | ausente | sí |
| Email | incluir | visible | sí |
| Teléfono | incluir | visible | sí |
| LinkedIn | incluir | visible | sí |
| Ubicación | omitir | ausente | sí |
| Fotografía | incluir | visible | sí |

**Dictamen:** fidelidad al flujo apta.

## 7. Capa 3 — Calidad recruiter

| Criterio | Nota | Evidencia observada | Fortaleza | Debilidad | Capa propietaria |
| --- | ---: | --- | --- | --- | --- |
| C1 — Primer escaneo y posicionamiento | 5 | En pocos segundos se identifica experiencia operativa de supermercados, cajas y atención. | Encaje inmediato y claro. | Ninguna material. | estrategia |
| C2 — Encaje competitivo real | 4 | Cubre atención, reclamaciones, caja, equipos, tareas, pedidos, stock y vehículo propio. | Alta equivalencia funcional. | No consta cargo formal idéntico ni sistema de caja OBRAMAT. | competitividad_no_corregible |
| C3 — Cobertura ATS respaldada | 4 | Usa atención al cliente, cuadres, caja, incidencias, equipos, pedidos, stock y operaciones. | Léxico natural y defendible. | Se omiten keywords no acreditadas, como herramientas específicas de OBRAMAT. | contenido |
| C4 — Fuerza de la evidencia | 4 | Cuadres en Excel, Trello, reorganización de equipos y pedidos automatizados muestran acciones concretas. | Evidencia práctica y trazable. | El impacto del sistema de cuadres no está cuantificado. | contenido |
| C5 — Adecuación narrativa y seniority | 4 | Mantiene el cargo histórico y orienta la lectura hacia coordinación operativa. | Controla la sobrecualificación sin falsear la trayectoria. | La transición desde Dirección Ejecutiva puede requerir explicación narrativa posterior. | estrategia |
| C6 — Calidad documental y visual | 5 | PDF de una página, legible, equilibrado, con fotografía autorizada y sin cortes ni solapamientos. | Lectura limpia y jerarquía clara. | Ninguna material. | composicion |

```yaml
media_recruiter: 4.3
```

La media es informativa y no gobierna la precedencia del resultado.

## 8. Diagnóstico competitivo

### Fortalezas principales

1. Experiencia prolongada en operaciones de supermercados y atención al cliente.
2. Experiencia directa en cuadres de caja y mejora del proceso mediante Excel.
3. Coordinación de equipos, seguimiento de tareas, pedidos, stock y vehículo propio confirmado.

### Debilidades principales

1. No consta experiencia literal con el sistema de cajas de OBRAMAT.
2. El cargo histórico es Director Ejecutivo, no Coordinador/a de línea de Cajas.
3. La movilidad geográfica por Canarias está sin confirmar, aunque es solo valorable en la oferta.

| Hallazgo | Clasificación | Evidencia disponible | Acción |
| --- | --- | --- | --- |
| Sistema específico de OBRAMAT no acreditado | no_corregible_sin_nueva_evidencia | No existe evidencia factual | No nombrarlo; mantener experiencia funcional. |
| Cargo formal específico no acreditado | no_corregible_sin_nueva_evidencia | La trayectoria conserva otro cargo | No cambiarlo; describir responsabilidades transferibles. |
| Movilidad por Canarias no confirmada | no_corregible_sin_nueva_evidencia | No hay decisión expresa | Omitirla. |
| Claridad del posicionamiento operativo | corregible_con_evidencia_existente | Ya está respaldada por el CV | Mantener composición actual. |

## 9. Defectos, enrutamiento e incidencias

| ID | Hallazgo | Severidad | Capa propietaria | Acción requerida |
| --- | --- | --- | --- | --- |
| ninguno | No hay defecto bloqueante o material en el CV concreto. | — | — | Ninguna. |

No se detecta nueva evidencia, contradicción arquitectónica ni necesidad de
regeneración.

## 10. Resultado global

```yaml
resultado_global: apto_para_presentacion
regeneracion:
  necesaria: no
  motivo: ""
  capa_origen: ""
  artefactos_downstream_a_regenerar: []
recomendacion_gate: aprobar
```

El CV es íntegro, fiel al flujo y suficientemente competitivo dentro de los
límites factuales disponibles. La recomendación no implica que exista carta,
que el paquete esté completo ni que pueda realizarse un envío.

## 11. Gate y decisión humana

Gate:

```text
GATE-VEREDICTO-CV
```

```yaml
decision_humana:
  estado: aprobado
  fecha: 2026-08-11
  decidido_por: persona_responsable
  observaciones: Gate aprobado; valida únicamente el CV y no autoriza carta, paquete ni presentación externa.
```

La persona responsable ha aprobado el veredicto de este CV el 2026-08-11.

## 12. Significado de la aprobación

La aprobación significa exclusivamente que este CV puede avanzar hacia la
futura fase de presentación. No significa candidatura enviada, carta aprobada,
paquete completo, aceptación de condiciones, inicio de sesión, carga de
archivos ni autorización de envío externo.

## 13. Control final

- [x] Integridad y privacidad contrastadas.
- [x] Estrategia, guion, JSON y composición contrastados.
- [x] PDF real revisado visualmente y aprobado por la persona responsable.
- [x] C1–C6 evaluados.
- [x] Debilidades clasificadas como corregibles o no corregibles.
- [x] Defectos asignados a capa propietaria.
- [x] Resultado global único emitido respetando la precedencia.
- [x] Recomendación de gate emitida.
- [x] Decisión humana no simulada.

## 14. Control de invalidación

```yaml
version_cv:
  material_regenerado: no
  revision_humana_anterior_vigente: sí
  veredicto_anterior_vigente: no_aplica
```

Una regeneración material posterior exige nueva revisión humana y nuevo
veredicto.

## 15. Veredicto compacto

```yaml
veredicto_final_cv:
  candidatura: CAND-2026-021
  cv_evaluado: cv.pdf
  huella_cv: 818f44552896c7b673ec9e6a7fb151b09f10a5e38a1e993d3f595f02e39cf18f
  fecha: 2026-08-11
  integridad: apta
  fidelidad_flujo: apta
  puntuaciones:
    primer_escaneo: 5
    encaje_competitivo: 4
    cobertura_ats: 4
    fuerza_evidencia: 4
    adecuacion_narrativa_seniority: 4
    calidad_documental_visual: 5
  media_recruiter: 4.3
  resultado_global: apto_para_presentacion
  regeneracion_necesaria: no
  recomendacion_gate: aprobar
  decision_humana:
    estado: aprobado
```

## 16. Principio de cierre

> El resultado es una recomendación defendible sobre este CV concreto; la
> decisión humana del gate permanece separada y no autoriza por sí sola la
> presentación externa de la candidatura.
