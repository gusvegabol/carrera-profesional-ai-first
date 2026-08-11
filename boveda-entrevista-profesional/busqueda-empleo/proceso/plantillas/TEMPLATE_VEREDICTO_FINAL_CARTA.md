---
id: TEMPLATE_VEREDICTO_FINAL_CARTA
tipo: template
version: "1.0.0"
estado: en_prueba
playbook: PLAYBOOK_VEREDICTO_FINAL_CARTA
artefacto_instancia: veredicto-final-carta.md
entrada_principal: carta-presentacion.pdf
gate_entrada: GATE-CARTA-REVISION-HUMANA
gate_salida: GATE-VEREDICTO-CARTA
---

# TEMPLATE — Veredicto final de carta de presentación

> Instancia documental del `PLAYBOOK_VEREDICTO_FINAL_CARTA`.
>
> Este documento evalúa una carta final concreta ya aprobada mediante revisión humana.
>
> No redacta, corrige, recompone ni amplía la carta.

---

# 1. Identificación

| Campo | Valor |
|---|---|
| Candidatura | `CAND-XXXX` |
| Empresa | |
| Puesto | |
| Carta evaluada | `carta-presentacion.pdf` |
| DOCX asociado | `carta-presentacion.docx` |
| CV de contraste | `cv.pdf` |
| Contenido semántico | `contenido-carta-presentacion.md` |
| Guion de carta | `guion-carta-presentacion.md` |
| Candidatura origen | `candidatura.md` |
| Evaluación de composición | `evaluacion-composicion-carta-presentacion.md` |
| Fecha del veredicto | `AAAA-MM-DD` |
| Playbook | `PLAYBOOK_VEREDICTO_FINAL_CARTA` |
| Versión playbook | `1.0.0` |
| Estado del veredicto | `en_evaluacion` \| `completado` \| `bloqueado` |

---

# 2. Gate de entrada

```yaml
gate_entrada:
  id: GATE-CARTA-REVISION-HUMANA
  estado:
  decision_humana:
  fecha_decision_humana:
```

Condición obligatoria:

```text
GATE-CARTA-REVISION-HUMANA = aprobado
```

## Resultado de precondición

```yaml
precondicion:
  cumplida: true | false
  incidencias: []
```

Si la precondición no se cumple:

```yaml
estado_veredicto: bloqueado
```

y no debe continuarse la evaluación competitiva.

---

# 3. Resultado ejecutivo

```yaml
resultado:
  veredicto: APTA | APTA_CON_RESERVAS | NO_APTA
  valor_incremental_frente_cv: alto | medio | bajo
  efecto_sobre_candidatura: mejora | neutro | perjudica
  recomendacion_inclusion_carta: incluir | incluir_con_reservas | no_incluir
```

## Justificación ejecutiva

[Explicar brevemente por qué se alcanza este resultado. No reescribir la carta.]

---

# 4. Evaluación independiente — Recruiter

## Pregunta central

> ¿Después de leer esta carta junto con el CV tengo más razones, las mismas o menos razones para avanzar con el candidato?

```yaml
recruiter:
  comprension_rapida_encaje:
    valor: alta | media | baja
    justificacion:

  valor_incremental_frente_cv:
    valor: alto | medio | bajo
    justificacion:

  credibilidad_motivacion:
    valor: alta | media | baja
    justificacion:

  especificidad_candidatura:
    valor: alta | media | baja
    justificacion:

  efecto_sobre_percepcion_candidato:
    valor: mejora | neutro | perjudica
    justificacion:

  hallazgos: []

  conclusion_rol:
    sin_objeciones | observaciones | reservas | hallazgo_bloqueante
```

## Hallazgos recruiter

| ID | Hallazgo | Evidencia | Severidad propuesta |
|---|---|---|---|
| REC-01 | | | bloqueante / reserva_relevante / reserva_menor / observacion |

---

# 5. Evaluación independiente — Responsable editorial/documental

## Pregunta central

> ¿La carta cumple su función con el mínimo texto necesario y sin ruido editorial?

```yaml
editorial:
  claridad:
    valor: alta | media | baja
    justificacion:

  foco:
    valor: alto | medio | bajo
    justificacion:

  progresion_argumental:
    valor: solida | suficiente | debil
    justificacion:

  redundancia:
    valor: baja | media | alta
    justificacion:

  tono:
    valor: adecuado | mejorable | inadecuado
    justificacion:

  extension:
    valor: adecuada | aceptable | problematica
    justificacion:

  apertura:
    valor: fuerte | suficiente | debil
    justificacion:

  cierre:
    valor: fuerte | suficiente | debil
    justificacion:

  hallazgos: []

  conclusion_rol:
    sin_objeciones | observaciones | reservas | hallazgo_bloqueante
```

## Hallazgos editoriales

| ID | Hallazgo | Evidencia | Severidad propuesta |
|---|---|---|---|
| EDI-01 | | | bloqueante / reserva_relevante / reserva_menor / observacion |

## Control anti-preferencia

```yaml
control_preferencia_estilistica:
  se_detectaron_preferencias_no_defectos: true | false
  descartadas_como_hallazgo: []
```

---

# 6. Evaluación independiente — Auditor de coherencia

## Pregunta central

> ¿Esta carta final sigue siendo exactamente la carta que la arquitectura autorizó producir?

```yaml
auditor:
  gates_previos_validos:
    valor: si | no
    justificacion:

  coherencia_con_candidatura:
    valor: si | no
    justificacion:

  coherencia_con_cv:
    valor: si | no
    justificacion:

  respeto_autorizaciones:
    valor: si | no
    justificacion:

  ausencia_afirmaciones_nuevas_no_autorizadas:
    valor: si | no
    justificacion:

  identidad_empresa_puesto_correcta:
    valor: si | no
    justificacion:

  integridad_flujo:
    valor: si | no
    justificacion:

  contradicciones: []

  conclusion_rol:
    sin_objeciones | observaciones | reservas | hallazgo_bloqueante
```

## Hallazgos de auditoría

| ID | Hallazgo | Fuente | Evidencia | Severidad propuesta |
|---|---|---|---|---|
| AUD-01 | | | | bloqueante / reserva_relevante / reserva_menor / observacion |

---

# 7. Independencia de roles

```yaml
independencia_roles:
  recruiter_evaluado_independientemente: true | false
  editorial_evaluado_independientemente: true | false
  auditor_evaluado_independientemente: true | false
  contaminacion_entre_roles_detectada: true | false
  incidencias: []
```

La evaluación solo es válida si:

```text
recruiter independiente
+
editorial independiente
+
auditor independiente
```

---

# 8. Síntesis determinista

La síntesis no introduce hallazgos nuevos.

Debe limitarse a consolidar y clasificar lo detectado por los tres roles.

```yaml
sintesis:
  hallazgos_recibidos_recruiter:
  hallazgos_recibidos_editorial:
  hallazgos_recibidos_auditor:
  duplicados_eliminados:
  nuevos_hallazgos_introducidos_por_sintesis: 0
```

Condición:

```text
nuevos_hallazgos_introducidos_por_sintesis = 0
```

---

# 9. Hallazgos clasificados

```yaml
hallazgos:
  bloqueantes: []
  reservas_relevantes: []
  reservas_menores: []
  observaciones: []
```

## Detalle

| ID | Origen | Hallazgo | Clasificación final | Motivo |
|---|---|---|---|---|
| | recruiter / editorial / auditor | | bloqueante / reserva_relevante / reserva_menor / observacion | |

---

# 10. Control de bloqueantes

```yaml
control_bloqueantes:
  existen: true | false
  cantidad:
  ids: []
```

Regla:

```text
cantidad >= 1
→ resultado_final = NO_APTA
```

---

# 11. Control de reservas relevantes

```yaml
control_reservas_relevantes:
  existen: true | false
  cantidad:
  ids: []
```

Regla:

```text
sin bloqueantes
+
>= 1 reserva relevante
→ APTA_CON_RESERVAS
```

---

# 12. Reservas menores

```yaml
reservas_menores:
  cantidad:
  ids: []
  afectan_resultado_final: false
```

Pueden coexistir con:

```text
APTA
```

---

# 13. Observaciones

```yaml
observaciones:
  cantidad:
  ids: []
  afectan_resultado_final: false
```

Una observación:

```text
≠ defecto
```

y no debe provocar reescritura.

---

# 14. Valor incremental frente al CV

```yaml
valor_incremental:
  nivel: alto | medio | bajo

  explica:

  repite_cv:
    nivel: bajo | medio | alto
    detalle:

  aporta_contexto_nuevo_autorizado:
    valor: si | parcialmente | no
    detalle:

  refuerza_motivacion:
    valor: alto | medio | bajo
    detalle:

  mejora_percepcion_recruiter:
    valor: si | neutro | no
    detalle:
```

Regla:

```text
valor_incremental = bajo
→ reserva_relevante
```

salvo que exista un bloqueante de mayor prioridad.

---

# 15. Comparación carta / CV

| Aspecto | Ya cubierto suficientemente por CV | La carta añade valor | Comentario |
|---|---|---|---|
| Encaje profesional | sí / no | alto / medio / bajo | |
| Motivación | sí / no | alto / medio / bajo | |
| Contextualización | sí / no | alto / medio / bajo | |
| Relación con puesto | sí / no | alto / medio / bajo | |
| Relación con empresa | sí / no | alto / medio / bajo | |
| Diferenciación | sí / no | alto / medio / bajo | |

---

# 16. Conveniencia de inclusión de la carta

```yaml
inclusion_carta:
  recomendacion: incluir | incluir_con_reservas | no_incluir
  motivo:
```

Esta recomendación es editorial: indica si la carta debe conservarse junto al
CV como documentación de la candidatura. No crea un paquete, un gate de
presentación ni autorización de envío.

Debe distinguirse siempre:

```text
resultado del veredicto
≠
decisión de presentación externa
```

---

# 17. Coherencia con candidatura

```yaml
coherencia_candidatura:
  posicionamiento_respetado: true | false
  prioridades_respetadas: true | false
  estrategia_modificada: true | false
  contradicciones: []
```

Condición esperada:

```text
estrategia_modificada = false
```

---

# 18. Coherencia con CV

```yaml
coherencia_cv:
  contradicciones_profesionales: []
  contradicciones_de_posicionamiento: []
  contradicciones_de_identidad: []
  coherente: true | false
```

Una contradicción profesional relevante no resuelta:

```text
→ bloqueante
```

---

# 19. Respeto de autorizaciones

```yaml
autorizaciones:
  afirmaciones_visibles_verificadas: true | false
  afirmaciones_no_autorizadas: []
  datos_personales_no_autorizados: []
  resultado: conforme | no_conforme
```

`no_conforme` material implica:

```text
→ bloqueante
```

---

# 20. Control de identidad de candidatura

```yaml
identidad:
  empresa_correcta: true | false
  puesto_correcto: true | false
  destinatario_correcto_o_no_necesario: true | false
  incidencias: []
```

Empresa o puesto incorrectos:

```text
→ bloqueante
```

---

# 21. Integridad de flujo

```yaml
integridad_flujo:
  candidatura_aprobada_en_fases_previas: true | false
  guion_carta_valido: true | false
  contenido_carta_valido: true | false
  composicion_valida: true | false
  revision_humana_aprobada: true | false
  incidencias: []
```

---

# 22. Control de fuentes — Recruiter

```yaml
fuentes_recruiter:
  carta_pdf: usada | no_usada
  cv_pdf: usada | no_usada
  candidatura_md: usada | no_usada
  analisis_oferta_md: usada | no_usada
  fuentes_no_permitidas_consultadas: []
```

Esperado:

```text
fuentes_no_permitidas_consultadas = []
```

---

# 23. Control de fuentes — Editorial

```yaml
fuentes_editorial:
  carta_pdf: usada | no_usada
  contenido_carta_md: usada | no_usada
  cv_pdf: usada | no_usada
  guion_carta_md: usada | no_usada
  fuentes_no_permitidas_consultadas: []
```

---

# 24. Control de fuentes — Auditor

```yaml
fuentes_auditor:
  candidatura_md: usada | no_usada
  guion_carta_md: usada | no_usada
  contenido_carta_md: usada | no_usada
  evaluacion_composicion: usada | no_usada
  carta_docx: usada | no_usada
  carta_pdf: usada | no_usada
  cv_pdf: usada | no_usada
  gates_previos: usados | no_usados

  datos_core:
    consultado: true | false
    motivo:
    solo_para_verificacion: true | false

  fuentes_no_permitidas_consultadas: []
```

---

# 25. Control de mejora oportunista

```yaml
mejora_oportunista:
  se_buscaron_nuevos_hechos: true | false
  se_propuso_informacion_no_autorizada: true | false
  se_penalizo_ausencia_de_hechos_no_autorizados: true | false
  conforme: true | false
```

Esperado:

```text
false
false
false
true
```

---

# 26. Información nueva detectada

```yaml
informacion_nueva:
  detectada: true | false
  elementos: []
  incorporada_a_la_carta: false
```

Si `detectada = true`, valorar si constituye:

```text
incidencia_fuera_de_fase
```

---

# 27. Incidencias fuera de fase

```yaml
incidencias_fuera_de_fase: []
```

Cada incidencia debe indicar:

```yaml
- id:
  tipo:
  descripcion:
  fase_responsable:
  bloquea_veredicto: true | false
```

Si existe una incidencia material sin resolver:

```text
estado_veredicto = bloqueado
```

---

# 28. Regla anti-perfeccionismo

```yaml
control_antiperfeccionismo:
  se_propuso_reescritura_sin_defecto_real: true | false
  se_convirtieron_preferencias_en_defectos: true | false
  se_iniciaron_mejoras_no_necesarias: true | false
  conforme: true | false
```

Esperado:

```text
false
false
false
true
```

---

# 29. Retorno a fase responsable

Si existen defectos:

| Hallazgo | Fase responsable |
|---|---|
| Factual | datos-core / análisis correspondiente |
| Estrategia | candidatura |
| Decisión editorial | guion |
| Redacción | contenido |
| Composición | composición |
| Visual | composición / revisión humana |

```yaml
retorno_fase:
  necesario: true | false
  fase:
  motivo:
```

El veredicto nunca corrige directamente.

---

# 30. Determinación del resultado

Aplicar en este orden:

```text
1. ¿Existe bloqueante?
   sí → NO_APTA

2. ¿Existen reservas relevantes?
   sí → APTA_CON_RESERVAS

3. En cualquier otro caso
   → APTA
```

```yaml
determinacion:
  bloqueantes:
  reservas_relevantes:
  resultado_calculado:
```

---

# 31. Comprobación de consistencia del resultado

```yaml
consistencia_resultado:
  reglas_aplicadas_correctamente: true | false
  contradicciones: []
```

Ejemplos no permitidos:

```text
bloqueante presente + APTA
```

```text
reserva relevante presente + APTA
```

sin justificación contractual.

---

# 32. Resultado final

```yaml
resultado_final:
  veredicto: APTA | APTA_CON_RESERVAS | NO_APTA
  valor_incremental_frente_cv: alto | medio | bajo
  efecto_sobre_candidatura: mejora | neutro | perjudica
  recomendacion_inclusion_carta: incluir | incluir_con_reservas | no_incluir
```

## Justificación final

[Máximo enfoque diagnóstico. No reescribir la carta.]

---

# 33. Gate de salida

```yaml
gate_salida:
  id: GATE-VEREDICTO-CARTA
  estado: pendiente
  decision_humana: pendiente
```

Regla:

```text
el playbook nunca aprueba automáticamente GATE-VEREDICTO-CARTA
```

---

# 34. Compatibilidad resultado / gate

## Si `APTA`

```yaml
gate:
  habilitado_para_decision_humana: true
  aprobacion_automatica: false
```

## Si `APTA_CON_RESERVAS`

```yaml
gate:
  habilitado_para_decision_humana: true
  requiere_revision_explicita_de_reservas: true
  aprobacion_automatica: false
```

## Si `NO_APTA`

```yaml
gate:
  habilitado_para_aprobacion: false
  requiere_correccion_y_nuevo_veredicto: true
```

---

# 35. Relación con presentación de candidatura

```yaml
estado_documental:
  gate_veredicto_cv:
  gate_veredicto_carta:
  presentada:
```

Cuando CV y carta son requeridos, ambos veredictos aprobados permiten registrar
el cierre documental de la candidatura. No abren ningún gate de presentación ni
modifican `presentada`.

---

# 36. Checklist de éxito

## Precondiciones

- [ ] Carta final disponible.
- [ ] CV final disponible.
- [ ] `GATE-CARTA-REVISION-HUMANA = aprobado`.

## Roles

- [ ] Recruiter evaluado independientemente.
- [ ] Editorial evaluado independientemente.
- [ ] Auditor evaluado independientemente.

## Fuentes

- [ ] Cada rol respetó sus fuentes.
- [ ] No se realizó investigación externa no autorizada.
- [ ] No se recuperaron hechos para mejorar la carta.

## Evaluación

- [ ] Hallazgos clasificados.
- [ ] Bloqueantes identificados.
- [ ] Reservas relevantes identificadas.
- [ ] Reservas menores identificadas.
- [ ] Observaciones separadas de defectos.
- [ ] Valor incremental evaluado.
- [ ] Conveniencia de inclusión evaluada.

## Arquitectura

- [ ] No se modificó estrategia.
- [ ] No se reescribió contenido.
- [ ] No se modificó composición.
- [ ] No se aprobaron gates automáticamente.
- [ ] El veredicto no inicia presentación externa ni crea un módulo posterior.

## Resultado

- [ ] Resultado determinista.
- [ ] Gate de salida queda pendiente de decisión humana.

---

# 37. Registro de pruebas

| Test | Resultado | Evidencia |
|---|---|---|
| T01 — Carta correcta, útil y coherente | | |
| T02 — Poco valor incremental | | |
| T03 — Afirmación no autorizada | | |
| T04 — Empresa/puesto incorrectos | | |
| T05 — Contradicción con CV | | |
| T06 — Redundancias menores | | |
| T07 — Editorialmente mejorable | | |
| T08 — Gate humano no aprobado | | |
| T09 — Información nueva | | |
| T10 — Recruiter positivo + auditor bloqueante | | |
| T11 — Mayoría positiva + bloqueante | | |
| T12 — Valor incremental bajo | | |
| T13 — Valor incremental medio/alto | | |
| T14 — Hecho no autorizado en datos-core | | |
| T15 — Independencia de roles | | |
| T16 — APTA deja gate pendiente | | |
| T17 — NO_APTA exige corrección | | |

---

# 38. Generalización de defectos

```yaml
defectos_generalizables: []
```

Para cada defecto:

```yaml
- id:
  descripcion:
  candidatura_origen:
  fase_responsable:
  es_generalizable: true | false
  playbook_afectado:
  template_afectado:
  prueba_automatizable:
  accion_recomendada:
```

No introducir parches específicos en el playbook sin justificar generalización.

---

# 39. Estado del artefacto

```yaml
estado_veredicto:
  valor: en_evaluacion | completado | bloqueado
  motivo:
```

---

# 40. Conclusión

```yaml
conclusion:
  candidatura:
  resultado_final:
  valor_incremental_frente_cv:
  recomendacion_inclusion_carta:
  bloqueantes:
  reservas_relevantes:
  gate_salida: GATE-VEREDICTO-CARTA
  estado_gate_salida: pendiente
  siguiente_accion: decision_humana
```

---

# 41. Historial

## 1.0.0

Primera versión.

Implementa el contrato de `PLAYBOOK_VEREDICTO_FINAL_CARTA v1.0.0` con:

- tres evaluaciones independientes;
- síntesis determinista;
- severidad de hallazgos;
- valoración incremental frente al CV;
- recomendación editorial de inclusión de la carta junto al CV;
- control de fuentes;
- control anti-mejora oportunista;
- incidencias fuera de fase;
- gate humano de salida;
- pruebas T01–T17;
- registro de defectos generalizables.
