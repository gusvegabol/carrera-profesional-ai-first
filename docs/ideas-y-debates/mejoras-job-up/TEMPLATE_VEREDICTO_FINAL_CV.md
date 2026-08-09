---
id: TEMPLATE_VEREDICTO_FINAL_CV
tipo: template
version: "1.1.0"
estado: vigente
playbook: PLAYBOOK_VEREDICTO_FINAL_CV
artefacto_instancia: veredicto-final-cv.md
gate_salida: GATE-VEREDICTO-CV
---

# TEMPLATE_VEREDICTO_FINAL_CV — CV-only

> Instancia documental del `PLAYBOOK_VEREDICTO_FINAL_CV`.
>
> Este documento evalúa un CV final concreto.
>
> No modifica el CV, no corrige artefactos anteriores, no autoriza un envío y no sustituye la decisión humana del gate.

---

# 1. Identificación

| Campo | Valor |
| --- | --- |
| Candidatura | `CAND-AAAA-NNN` |
| Empresa | |
| Puesto objetivo | |
| Fecha del veredicto | `AAAA-MM-DD` |
| Estado del veredicto | `en_evaluacion` \| `completado` \| `bloqueado` |
| Playbook | `PLAYBOOK_VEREDICTO_FINAL_CV` |
| Versión del playbook | |
| Evaluador IA | |
| Revisión humana previa a veredicto | `realizada` \| `no_realizada` |
| Huella del `cv.pdf` evaluado | SHA-256 |

---

# 2. CV evaluado

## 2.1 Artefacto principal

| Campo | Valor |
| --- | --- |
| Archivo | `cv.pdf` |
| Fecha de generación | |
| Versión / hash / huella | |
| Número de páginas | |
| PDF accesible y revisable | `sí` \| `no` |

## 2.2 Artefactos equivalentes

| Artefacto | Identificador / versión | Estado |
| --- | --- | --- |
| `cv.docx` | | `disponible` \| `no_disponible` |
| `cv.tex` | | `disponible` \| `no_disponible` |
| `datos-generacion.json` | | `disponible` \| `no_disponible` |

> **Regla:** cualquier regeneración material posterior del CV invalida este veredicto como veredicto vigente.

---

# 3. Precondiciones

Marcar cada condición antes de evaluar.

- [ ] Existe `cv.pdf`.
- [ ] Existe `cv.docx`.
- [ ] Existe `datos-generacion.json`.
- [ ] Existe `guion-adaptacion-cv.md`.
- [ ] Existe `candidatura.md`.
- [ ] Existe `analisis-oferta.md`.
- [ ] Las fuentes factuales necesarias son accesibles.
- [ ] Existe autorización vigente de datos privados.
- [ ] `GATE-CONTENIDO-CV-COMPOSICION` está aprobado.
- [ ] La composición terminó correctamente.
- [ ] La revisión humana posterior a composición fue realizada.
- [ ] La candidatura mantiene `presentada: false`.

## 3.1 Resultado de precondiciones

```yaml
precondiciones:
  resultado: cumplidas | no_cumplidas
  bloqueos: []
```

Si existe una precondición incumplida:

```yaml
estado_veredicto: bloqueado
```

y no se emite resultado de salida.

## 3.2 Identidad de versión

```yaml
revision_humana_origen:
  artefacto: revision-humana-cv.md
  decision: aprobado_para_veredicto
  huella_cv: SHA-256
huella_evaluada: SHA-256
coincide: sí | no
```

Si `coincide: no`, el estado es `bloqueado` y el motivo es
`revision_humana_corresponde_a_otra_version`.

---

# 4. Fuentes consultadas

Registrar únicamente las realmente utilizadas.

| Fuente | Función | Consultada |
| --- | --- | --- |
| `cv.pdf` | Artefacto principal evaluado | `sí` |
| `cv.docx` | Control técnico opcional | `sí` \| `no` |
| `cv.tex` | Control técnico opcional | `sí` \| `no` |
| `datos-generacion.json` | Contenido final previo a composición | `sí` \| `no` |
| `guion-adaptacion-cv.md` | Decisión editorial | `sí` \| `no` |
| `candidatura.md` | Estrategia y privacidad | `sí` \| `no` |
| `analisis-oferta.md` | Oferta, requisitos y encaje | `sí` \| `no` |
| `datos-core-busqueda.md` | Factualidad profesional | `sí` \| `no` |
| Gate de contenido → composición | Control de traspaso | `sí` \| `no` |
| Manifiesto de composición | Control técnico | `sí` \| `no` |

### Otras fuentes autorizadas utilizadas

| Fuente | Motivo |
| --- | --- |
| | |

---

# 5. Roles de evaluación

## 5.1 Recruiter senior + coach de carrera

Pregunta central:

> ¿Qué percibe un recruiter al enfrentarse a este CV y qué capacidad tiene el documento de provocar una lectura favorable o una entrevista para esta oportunidad?

Estado:

```yaml
rol_recruiter:
  aplicado: sí | no
```

---

## 5.2 Auditor senior de flujo agentic

Pregunta central:

> ¿El CV final preserva correctamente las decisiones, límites, autorizaciones y contenido que llegaron hasta la fase de composición?

Estado:

```yaml
rol_auditor_flujo:
  aplicado: sí | no
```

---

# 6. CAPA 1 — Integridad

## 6.1 Resultado

```yaml
integridad:
  resultado: apta | no_apta
```

---

## 6.2 Controles

| Control | Resultado | Evidencia / incidencia |
| --- | --- | --- |
| Hechos profesionales respaldados | `apto` \| `incidencia` | |
| Empresas, cargos y fechas correctos | `apto` \| `incidencia` | |
| Métricas y resultados respaldados | `apto` \| `incidencia` | |
| Formación correctamente representada | `apto` \| `incidencia` | |
| Tecnologías y niveles de dominio respaldados | `apto` \| `incidencia` | |
| Formación no convertida en experiencia | `apto` \| `incidencia` | |
| Automatización no convertida indebidamente en IA | `apto` \| `incidencia` | |
| Transferibilidad no presentada como experiencia literal | `apto` \| `incidencia` | |
| Responsabilidad individual/colegiada correctamente atribuida | `apto` \| `incidencia` | |
| Requisitos no acreditados no aparecen como cumplidos | `apto` \| `incidencia` | |
| Datos privados incluidos según autorización | `apto` \| `incidencia` | |
| Datos privados marcados para omisión no aparecen | `apto` \| `incidencia` | |

---

## 6.3 Incidencias de integridad

| ID | Incidencia | Evidencia en CV | Fuente de contraste | Capa propietaria | Bloqueante |
| --- | --- | --- | --- | --- | --- |
| INT-01 | | | | `factual` \| `privacidad` \| otra | `sí` |

Si no existen:

```text
ninguna
```

---

## 6.4 Dictamen de integridad

**Resultado:** `apta` / `no_apta`

**Justificación:**

...

> Si el resultado es `no_apta`, el resultado global deberá ser `bloqueado_por_integridad`.

---

# 7. CAPA 2 — Fidelidad al flujo

## 7.1 Resultado

```yaml
fidelidad_flujo:
  resultado: apta | no_apta
```

---

## 7.2 Estrategia → CV

| Comprobación | Resultado | Evidencia |
| --- | --- | --- |
| El posicionamiento de `candidatura.md` sigue reconocible | `sí` \| `no` | |
| Se respetan advertencias | `sí` \| `no` | |
| Se respetan afirmaciones excluidas | `sí` \| `no` | |
| No se intentan ocultar carencias mediante equivalencias | `sí` \| `no` | |

---

## 7.3 Guion → CV

| Comprobación | Resultado | Evidencia |
| --- | --- | --- |
| Inclusiones prioritarias presentes | `sí` \| `no` | |
| Omisiones respetadas | `sí` \| `no` | |
| Reducciones respetadas | `sí` \| `no` | |
| Orden estratégico conservado | `sí` \| `no` | |
| Seniority respetado | `sí` \| `no` | |
| Idioma respetado | `sí` \| `no` | |
| Restricciones respetadas | `sí` \| `no` | |
| Primer escaneo coherente con el guion | `sí` \| `no` | |

---

## 7.4 `datos-generacion.json` → CV

| Comprobación | Resultado | Evidencia |
| --- | --- | --- |
| No hay contenido añadido por composición | `sí` \| `no` | |
| No hay contenido semántico eliminado | `sí` \| `no` | |
| No hay reescritura | `sí` \| `no` | |
| No hay resumen autónomo | `sí` \| `no` | |
| No hay fusión con cambio de significado | `sí` \| `no` | |
| No hay traducción no autorizada | `sí` \| `no` | |

---

## 7.5 Privacidad → CV

| Campo | Decisión autorizada | Resultado observado | Conforme |
| --- | --- | --- | --- |
| Nombre | | | `sí` \| `no` |
| Apellido 1 | | | `sí` \| `no` |
| Apellido 2 | | | `sí` \| `no` |
| Email | | | `sí` \| `no` |
| Teléfono | | | `sí` \| `no` |
| LinkedIn | | | `sí` \| `no` |
| Ubicación | | | `sí` \| `no` |
| Fotografía | | | `sí` \| `no` |

---

## 7.6 Incidencias de fidelidad

| ID | Incidencia | Traspaso afectado | Capa propietaria | Evidencia | Bloqueante |
| --- | --- | --- | --- | --- | --- |
| FLU-01 | | | `estrategia` \| `guion` \| `contenido` \| `privacidad` \| `composicion` | | `sí` |

Si no existen:

```text
ninguna
```

---

## 7.7 Dictamen de fidelidad

**Resultado:** `apta` / `no_apta`

**Justificación:**

...

> Si `integridad: apta` y `fidelidad_flujo: no_apta`, el resultado global será `requiere_correccion_de_flujo`.

---

# 8. CAPA 3 — Evaluación recruiter

Solo utilizar como evaluación de salida cuando:

```text
integridad: apta
fidelidad_flujo: apta
```

---

# 9. C1 — Primer escaneo y posicionamiento

**Pregunta**

> ¿En aproximadamente 6–10 segundos queda claro quién es esta persona, qué aporta para esta oportunidad y por qué merece continuar leyendo?

```yaml
C1:
  nota: 1 | 2 | 3 | 4 | 5
```

**Evidencia observada**

...

**Fortaleza**

...

**Debilidad**

...

**Impacto recruiter**

...

**Mejora posible**

...

**Capa propietaria**

`estrategia` | `guion` | `contenido` | `composicion` | `competitividad_no_corregible`

**Límite factual**

...

---

# 10. C2 — Encaje competitivo real

**Pregunta**

> ¿El CV demuestra de forma convincente las evidencias más relevantes para las necesidades reales de la oferta?

```yaml
C2:
  nota: 1 | 2 | 3 | 4 | 5
```

**Evidencia observada**

...

**Fortaleza**

...

**Debilidad**

...

**Impacto recruiter**

...

**Mejora posible**

...

**Capa propietaria**

...

**Límite factual**

...

### 10.1 Carencias competitivas materiales

| Carencia | Relevancia en la oferta | Acreditada | Corregible mediante redacción |
| --- | --- | --- | --- |
| | | `sí` \| `no` | `sí` \| `no` |

---

# 11. C3 — Cobertura ATS respaldada

**Pregunta**

> ¿El CV utiliza de forma natural el vocabulario relevante de la oferta que puede defenderse factual y profesionalmente?

```yaml
C3:
  nota: 1 | 2 | 3 | 4 | 5
```

**Keywords prioritarias correctamente utilizadas**

- 
- 

**Keywords correctamente omitidas por falta de respaldo**

- 
- 

**Evidencia observada**

...

**Fortaleza**

...

**Debilidad**

...

**Impacto recruiter / ATS**

...

**Mejora posible**

...

**Capa propietaria**

...

**Límite factual**

...

---

# 12. C4 — Fuerza de la evidencia

**Pregunta**

> ¿Las experiencias prioritarias demuestran acciones, contexto, alcance y resultados con suficiente fuerza?

```yaml
C4:
  nota: 1 | 2 | 3 | 4 | 5
```

**Evidencias más fuertes del CV**

| Evidencia | Por qué funciona |
| --- | --- |
| | |

**Evidencias débiles o demasiado genéricas**

| Evidencia | Problema |
| --- | --- |
| | |

**Fortaleza**

...

**Debilidad**

...

**Impacto recruiter**

...

**Mejora posible**

...

**Capa propietaria**

...

**Límite factual**

...

---

# 13. C5 — Adecuación narrativa y seniority

**Pregunta**

> ¿El documento presenta correctamente la trayectoria para esta oportunidad sin falsear cargos ni degradar artificialmente la historia profesional?

```yaml
C5:
  nota: 1 | 2 | 3 | 4 | 5
```

**Evidencia observada**

...

**Lectura de seniority**

...

**Riesgo de sobrecualificación**

`ninguno` | `bajo` | `medio` | `alto`

**Fortaleza**

...

**Debilidad**

...

**Impacto recruiter**

...

**Mejora posible**

...

**Capa propietaria**

...

**Límite factual**

...

---

# 14. C6 — Calidad documental y visual

**Pregunta**

> ¿El PDF terminado favorece la lectura recruiter y materializa correctamente la jerarquía editorial?

```yaml
C6:
  nota: 1 | 2 | 3 | 4 | 5
```

## 14.1 Controles visuales

| Control | Resultado | Observación |
| --- | --- | --- |
| Legibilidad | `apto` \| `mejorable` \| `deficiente` | |
| Jerarquía | | |
| Densidad | | |
| Uso del espacio | | |
| Márgenes | | |
| Fotografía | | |
| Equilibrio de bloques | | |
| Longitud | | |
| Paginación | | |
| Cortes/desbordamientos | | |
| Consistencia | | |
| Visibilidad de información prioritaria | | |

**Fortaleza**

...

**Debilidad**

...

**Impacto recruiter**

...

**Mejora posible**

...

**Capa propietaria**

`composicion` | otra

**Límite**

...

---

# 15. Resumen de puntuaciones

| Criterio | Nota |
| --- | ---: |
| C1 — Primer escaneo y posicionamiento | |
| C2 — Encaje competitivo real | |
| C3 — Cobertura ATS respaldada | |
| C4 — Fuerza de la evidencia | |
| C5 — Adecuación narrativa y seniority | |
| C6 — Calidad documental y visual | |

```yaml
media_recruiter: 0.0
```

> La media es únicamente informativa y comparativa.
>
> No puede gobernar el resultado global.

---

# 16. Diagnóstico competitivo

## 16.1 Fortalezas principales

1. 
2. 
3. 

## 16.2 Debilidades principales

1. 
2. 
3. 

## 16.3 Riesgos de descarte

| Riesgo | Nivel | Motivo | Corregible |
| --- | --- | --- | --- |
| | `bajo` \| `medio` \| `alto` | | `sí` \| `no` |

---

# 17. Clasificación corregible / no corregible

| Hallazgo | Clasificación | Evidencia disponible | Acción |
| --- | --- | --- | --- |
| | `corregible_con_evidencia_existente` | | |
| | `no_corregible_sin_nueva_evidencia` | | |

Regla:

> Una carencia `no_corregible_sin_nueva_evidencia` no puede convertirse en fortaleza mediante redacción.

---

# 18. Defectos y capa propietaria

| ID | Hallazgo | Severidad | Capa propietaria | Acción requerida |
| --- | --- | --- | --- | --- |
| DEF-01 | | `bloqueante` \| `material` \| `menor` | `factual` \| `estrategia` \| `guion` \| `contenido` \| `privacidad` \| `composicion` \| `competitividad_no_corregible` | |

Si no existen:

```text
ninguno
```

---

# 19. Enrutamiento

## Factual

```text
→ fuente factual
→ mecanismo de propagación vigente
```

Hallazgos aplicables:

...

## Estrategia

```text
→ analisis-oferta.md / candidatura.md
```

Hallazgos:

...

## Guion

```text
→ PLAYBOOK_GUION_ADAPTACION_CV
```

Hallazgos:

...

## Contenido

```text
→ PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
```

Hallazgos:

...

## Privacidad

```text
→ autorización de candidatura
```

Hallazgos:

...

## Composición

```text
→ compositor / template / configuración técnica
```

Hallazgos:

...

## Competitividad no corregible

```text
→ no maquillar
→ decisión humana sobre mantener o abandonar candidatura
```

Hallazgos:

...

---

# 20. Resultado global

Seleccionar **un único valor**:

```yaml
resultado_global:
  bloqueado_por_integridad
  # o
  requiere_correccion_de_flujo
  # o
  no_competitivo
  # o
  revisar_antes_de_presentar
  # o
  apto_para_presentacion
```

Eliminar los valores no aplicables en la instancia final.

---

# 21. Justificación del resultado

## 21.1 Síntesis recruiter

...

## 21.2 Síntesis de auditoría de flujo

...

## 21.3 Razón decisiva

> ...

---

# 22. Regla de precedencia aplicada

Marcar una sola:

- [ ] `bloqueado_por_integridad`
- [ ] `requiere_correccion_de_flujo`
- [ ] `no_competitivo`
- [ ] `revisar_antes_de_presentar`
- [ ] `apto_para_presentacion`

Confirmación:

- [ ] La media no se utilizó para alterar la precedencia.
- [ ] Ninguna carencia factual fue maquillada.
- [ ] Ninguna keyword no respaldada fue añadida como requisito de aprobación.
- [ ] El resultado distingue calidad del CV de competitividad de la candidatura.

---

# 23. Cambios requeridos antes de nueva evaluación

## 23.1 Obligatorios

1. 
2. 
3. 

Si no existen:

```text
ninguno
```

## 23.2 Recomendados pero no bloqueantes

1. 
2. 

Si no existen:

```text
ninguno
```

---

# 24. Necesidad de regeneración

```yaml
regeneracion:
  necesaria: sí | no
  motivo:
  capa_origen:
  artefactos_downstream_a_regenerar: []
```

Si se genera un nuevo CV:

> Este veredicto pasa a histórico y deja de ser vigente.

---

# 25. Recomendación de gate

Gate:

```text
GATE-VEREDICTO-CV
```

```yaml
recomendacion_gate: aprobar | no_aprobar
```

Regla:

```text
apto_para_presentacion
→ aprobar

cualquier otro resultado
→ no_aprobar
```

---

# 26. Decisión humana del gate

> Esta sección no puede ser completada autónomamente por la IA.

```yaml
decision_humana:
  estado: pendiente | aprobado | bloqueado
  fecha:
  decidido_por:
  observaciones:
```

---

# 27. Significado de la decisión humana

## Si `aprobado`

Significa exclusivamente:

> El CV evaluado puede avanzar hacia la futura fase de presentación.

No significa:

- candidatura enviada;
- carta aprobada;
- aceptación de condiciones;
- aprobación de empresa;
- autorización para envío automático.

## Si `bloqueado`

Registrar causa:

...

---

# 28. Investigación contextual externa

```yaml
investigacion_contextual:
  realizada: no
```

Por defecto:

```text
fuera del veredicto base
```

Si en una futura versión del sistema se activa esta capacidad, deberá existir autorización específica y un contrato propio.

---

# 29. Contradicciones arquitectónicas detectadas

| ID | Fuentes en conflicto | Descripción | Impacto | Bloquea |
| --- | --- | --- | --- | --- |
| ARQ-DEF-01 | | | | `sí` \| `no` |

Si no existen:

```text
ninguna
```

---

# 30. Nueva evidencia detectada

| Evidencia | Estado | Acción |
| --- | --- | --- |
| | `no_utilizada` | devolver a fuente factual y propagar |

Si no existe:

```text
ninguna
```

> Nueva evidencia nunca se incorpora directamente al CV desde el veredicto.

---

# 31. Control final de ejecución

## Integridad

- [ ] Integridad evaluada.
- [ ] Privacidad contrastada.
- [ ] No existe hecho sin respaldo.

## Fidelidad

- [ ] Estrategia contrastada.
- [ ] Guion contrastado.
- [ ] `datos-generacion.json` contrastado.
- [ ] Composición contrastada.

## Recruiter

- [ ] Primer escaneo evaluado.
- [ ] Encaje competitivo evaluado.
- [ ] ATS evaluado.
- [ ] Fuerza de evidencia evaluada.
- [ ] Narrativa y seniority evaluados.
- [ ] PDF visualmente evaluado.

## Diagnóstico

- [ ] Debilidades clasificadas como corregibles/no corregibles.
- [ ] Defectos asignados a capa propietaria.
- [ ] Resultado global único emitido.
- [ ] Precedencia respetada.
- [ ] Recomendación de gate emitida.
- [ ] Decisión humana no simulada.

---

# 32. Veredicto compacto

```yaml
veredicto_final_cv:
  candidatura:
  cv_evaluado:
  huella_cv:
  fecha:
  integridad: apta | no_apta
  fidelidad_flujo: apta | no_apta

  puntuaciones:
    primer_escaneo:
    encaje_competitivo:
    cobertura_ats:
    fuerza_evidencia:
    adecuacion_narrativa_seniority:
    calidad_documental_visual:

  media_recruiter:

  resultado_global:
    # bloqueado_por_integridad
    # requiere_correccion_de_flujo
    # no_competitivo
    # revisar_antes_de_presentar
    # apto_para_presentacion

  regeneracion_necesaria: sí | no
  recomendacion_gate: aprobar | no_aprobar

  decision_humana:
    estado: pendiente
```

## 34. Control de invalidación

```yaml
version_cv:
  material_regenerado: sí | no
  revision_humana_anterior_vigente: sí | no
  veredicto_anterior_vigente: sí | no
```

Una regeneración material exige nueva revisión y nuevo veredicto; no se admite
cambiar solo la referencia o reutilizar una huella anterior.

---

# 33. Principio de cierre

> **El template no está diseñado para producir un resultado favorable. Está diseñado para producir un resultado defendible.**

Un `no_competitivo` puede ser una salida correcta de un pipeline que funcionó perfectamente.

Un `apto_para_presentacion` solo es válido cuando el CV concreto evaluado es íntegro, fiel al flujo y suficientemente competitivo dentro de los límites factuales existentes.
