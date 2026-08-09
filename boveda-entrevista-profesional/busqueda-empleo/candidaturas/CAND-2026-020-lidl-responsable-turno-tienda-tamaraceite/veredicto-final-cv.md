---
id: veredicto-final-cv-CAND-2026-020
tipo: veredicto_final_cv
version_playbook: "1.1.0"
fecha_evaluacion: 2026-08-08
estado_veredicto: completado
gate_salida: GATE-VEREDICTO-CV
---

# Veredicto final del CV — CAND-2026-020

## 1. Identificación y versión

| Campo | Valor |
| --- | --- |
| Candidatura | `CAND-2026-020` |
| Empresa | Lidl Supermercados SAU |
| Puesto | Responsable de turno Tienda 40h Tamaraceite |
| CV evaluado | `cv.pdf` |
| Fecha de generación | 2026-08-08 |
| Fecha del veredicto | 2026-08-08 |
| Huella SHA-256 del PDF | `bfaef3008232e5ce3eefe315dab14a5aef7f347bb1df73a86561011958b0b667` |
| Páginas | 1 |
| Revisión humana de origen | [[revision-humana-cv]] — `aprobado_para_veredicto` |
| Coincidencia de huella | `sí` |

La huella de `revision-humana-cv.md` coincide con la del PDF evaluado. El
veredicto corresponde exclusivamente a esta versión.

## 2. Fuentes consultadas

| Fuente | Función | Consultada |
| --- | --- | --- |
| `cv.pdf` | Artefacto principal evaluado | sí |
| `cv.docx` | Control técnico | sí |
| `cv.tex` | Control de equivalencia textual | sí |
| `datos-generacion.json` | Contenido previo a composición | sí |
| `guion-adaptacion-cv.md` | Decisiones editoriales | sí |
| `candidatura.md` | Estrategia y privacidad | sí |
| `analisis-oferta.md` | Requisitos y encaje | sí |
| `datos-core-busqueda.md` | Factualidad profesional | sí |
| `datos-privados-candidatura.md` | Datos privados autorizables | sí |
| `evaluacion-gate-contenido-cv-composicion.md` | Gate de entrada | sí |
| `manifest-generacion-cv.json` | Publicación técnica | sí |

## 3. Roles aplicados

```yaml
rol_recruiter:
  aplicado: sí
rol_auditor_flujo:
  aplicado: sí
```

El primer rol evaluó la lectura recruiter y la competitividad; el segundo
contrastó la cadena análisis → candidatura → guion → JSON → composición → PDF.

## 4. Precondiciones

- [x] `cv.pdf`, `cv.docx`, `cv.tex` y `datos-generacion.json` existen.
- [x] `guion-adaptacion-cv.md`, `candidatura.md` y `analisis-oferta.md` existen.
- [x] Las fuentes factuales y privadas necesarias son accesibles.
- [x] La autorización de privacidad está resuelta.
- [x] `GATE-CONTENIDO-CV-COMPOSICION` está aprobado.
- [x] La composición terminó correctamente.
- [x] Existe revisión humana posterior a composición.
- [x] La decisión humana es `aprobado_para_veredicto`.
- [x] La huella revisada coincide con el PDF.
- [x] `presentada: false`.

```yaml
precondiciones:
  resultado: cumplidas
  bloqueos: []
```

## 5. Capa 1 — Integridad

```yaml
integridad:
  resultado: apta
```

| Control | Resultado | Evidencia |
| --- | --- | --- |
| Hechos profesionales respaldados | apto | HER-03, HER-04, HER-07, HER-08 y HER-10 están en datos core. |
| Empresas, cargos y fechas correctos | apto | Trayectoria de Herfrailes conservada literalmente. |
| Métricas y resultados respaldados | apto | 30 %, 80 % y alcance de tres tiendas proceden del core. |
| Formación correctamente representada | apto | Bachillerato; no se presenta la FP no finalizada como título. |
| Tecnologías y niveles respaldados | apto | Excel y Trello aparecen con el alcance acreditado. |
| Formación no convertida en experiencia | apto | No aparece IA ni FP como experiencia o titulación. |
| Automatización no convertida indebidamente en IA | apto | Los algoritmos se presentan como sistemas de pedido y previsión. |
| Responsabilidad individual/colegiada correcta | apto | Se mantienen solo contribuciones individuales acreditadas. |
| Requisitos no acreditados no aparecen cumplidos | apto | La FP de Grado Medio queda fuera del contenido visible. |
| Datos privados según autorización | apto | Nombre, apellido 1, email, teléfono y fotografía incluidos. |
| Datos omitidos ausentes | apto | Apellido 2, LinkedIn y ubicación no aparecen. |

**Dictamen:** no se detectan incidencias de integridad. La falta de FP finalizada
es una carencia factual conocida, no una afirmación incorrecta del CV.

## 6. Capa 2 — Fidelidad al flujo

```yaml
fidelidad_flujo:
  resultado: apta
```

### Estrategia → CV

| Comprobación | Resultado | Evidencia |
| --- | --- | --- |
| Posicionamiento operativo reconocible | sí | Operaciones de supermercados, pedidos, stock y procesos. |
| Advertencias respetadas | sí | FP no finalizada y límites de caja no se convierten en claims. |
| Afirmaciones excluidas respetadas | sí | No hay tesorería, compras centralizadas o experiencia Lidl. |
| Carencias no ocultadas mediante equivalencias | sí | La formación no se presenta como equivalente. |

### Guion → CV

| Comprobación | Resultado | Evidencia |
| --- | --- | --- |
| Inclusiones prioritarias | sí | Pedidos, stock, rotación, mermas, equipos, tareas y caja. |
| Omisiones | sí | FP no finalizada y contenido directivo abstracto no dominan. |
| Reducciones | sí | La trayectoria directiva aparece como continuidad, no como eje. |
| Orden estratégico | sí | Perfil y experiencia operativa preceden a trayectoria. |
| Seniority e idioma | sí | Tono operativo en español, sin degradar el cargo histórico. |
| Restricciones y primer escaneo | sí | El encabezado comunica operación de supermercados. |

### JSON → CV

| Comprobación | Resultado | Evidencia |
| --- | --- | --- |
| Contenido añadido por composición | no | No observado. |
| Contenido semántico eliminado | no | Los textos del JSON están visibles. |
| Reescritura, resumen o traducción | no | DOCX, PDF y TEX conservan el contenido. |
| Fusión con cambio de significado | no | El compositor ordena, no interpreta. |

### Privacidad → CV

| Campo | Autorización | Observado | Conforme |
| --- | --- | --- | --- |
| Nombre | incluir | Gustavo | sí |
| Apellido 1 | incluir | Vega | sí |
| Apellido 2 | omitir | ausente | sí |
| Email | incluir | visible | sí |
| Teléfono | incluir | visible | sí |
| LinkedIn | omitir | ausente | sí |
| Ubicación | omitir | ausente | sí |
| Fotografía | incluir | visible | sí |

**Dictamen:** la composición es fiel a la estrategia, al guion, al JSON 1.2 y a
la autorización privada.

## 7. Capa 3 — Calidad recruiter

| Criterio | Nota | Evidencia observada | Fortaleza | Debilidad | Impacto recruiter | Mejora posible | Capa propietaria | Límite factual |
| --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| C1 — Primer escaneo y posicionamiento | 5 | En pocos segundos se identifica operación de supermercados, pedidos, stock y mejora. | Posicionamiento directo. | Ninguna material. | Alta claridad inicial. | Mantener. | estrategia | No afirmar experiencia Lidl. |
| C2 — Encaje competitivo real | 4 | El CV cubre pedidos, inventario/stock, rotación, mermas, equipos, tareas y caja. | Evidencias directamente relacionadas. | No acredita FP finalizada ni posición idéntica. | Encaje funcional fuerte con una carencia formal. | Mantener experiencia transferible. | competitividad_no_corregible | No inventar equivalencia de FP. |
| C3 — Cobertura ATS respaldada | 4 | Usa pedidos, stock, rotación, mermas, previsión, equipos y cuadres de caja. | Keywords naturales y defendibles. | No incorpora términos no acreditados. | Buena recuperación para funciones centrales. | No añadir herramientas de Lidl. | contenido | No convertir palabras clave en experiencia literal. |
| C4 — Fuerza de la evidencia | 4 | Incluye algoritmo de pedidos, reducciones del 30 %/80 %, redistribución y sistema de caja. | Acciones y resultados concretos. | Algunas funciones de equipo se expresan sin métrica. | Credibilidad alta. | Mantener límites. | contenido | No inventar resultados adicionales. |
| C5 — Adecuación narrativa y seniority | 4 | El CV prioriza ejecución operativa y conserva el cargo histórico. | Controla la sobrecualificación. | La trayectoria directiva puede requerir explicación posterior. | Riesgo moderado y manejable. | Explicar motivación en fase de carta si procede. | estrategia | No ocultar cargos ni degradarlos. |
| C6 — Calidad documental y visual | 5 | PDF de una página, legible, equilibrado, con fotografía y sin desbordamientos. | Jerarquía clara y lectura limpia. | Ninguna material. | Favorece el primer escaneo. | Mantener plantilla. | composicion | La revisión visual se limita al PDF actual. |

```yaml
media_recruiter: 4.3
```

La media es únicamente informativa.

## 8. Diagnóstico competitivo

### Fortalezas

1. Experiencia real de operación de supermercados.
2. Pedidos, stock, rotación, mermas y sistemas de mejora con resultados.
3. Coordinación operativa, tareas, caja y disponibilidad para turnos rotativos.

### Debilidades

1. No consta FP de Grado Medio finalizada o equivalencia documental.
2. No existe experiencia literal como responsable de turno de Lidl.

| Hallazgo | Clasificación | Acción |
| --- | --- | --- |
| FP no finalizada | no_corregible_sin_nueva_evidencia | Mantener como carencia, no maquillarla. |
| Experiencia transferible a Lidl | corregible_con_evidencia_existente | Ya está presentada desde funciones operativas. |

No se detectan defectos que obliguen a regenerar el CV.

## 9. Defectos y enrutamiento

| ID | Hallazgo | Severidad | Capa propietaria | Acción |
| --- | --- | --- | --- | --- |
| ninguno | No hay defecto bloqueante o material. | — | — | Ninguna. |

No se detecta nueva evidencia ni contradicción arquitectónica.

## 10. Resultado global

```yaml
resultado_global: apto_para_presentacion
regeneracion:
  necesaria: no
  motivo: ""
recomendacion_gate: aprobar
```

La candidatura es íntegra, fiel y competitiva dentro de sus límites factuales.
La falta de FP finalizada puede afectar a la decisión externa, pero no invalida
este CV ni se puede corregir mediante redacción.

## 11. Gate y decisión humana

```yaml
gate: GATE-VEREDICTO-CV
decision_humana:
  estado: aprobado
  fecha: 2026-08-09
  decidido_por: persona_responsable
  observaciones: Gate aprobado; la candidatura no se ha enviado y requiere una instrucción de presentación separada.
```

`apto_para_presentacion` fue aprobado por la persona responsable. Esta decisión
no significa que la candidatura haya sido enviada.

## 12. Control final

- [x] Integridad y privacidad contrastadas.
- [x] Estrategia, guion, JSON y composición contrastados.
- [x] PDF real revisado visualmente.
- [x] C1–C6 evaluados.
- [x] Debilidades clasificadas por corregibilidad.
- [x] Resultado global único y precedencia respetada.
- [x] Recomendación de gate emitida.
- [x] Decisión humana del gate no simulada.
