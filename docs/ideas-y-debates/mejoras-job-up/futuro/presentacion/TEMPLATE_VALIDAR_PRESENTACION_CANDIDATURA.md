---
id: TEMPLATE_EVALUACION_PRESENTACION_CANDIDATURA
tipo: template
version: "1.0.0"
estado: en_prueba
playbook: PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA
artefacto_instancia: evaluacion-presentacion-candidatura.md
entrada_principal: paquete-presentacion.md
gate_entrada: GATE-CANDIDATURA-PRESENTACION
estado_gate_entrada_requerido: pendiente
gate_salida: GATE-CANDIDATURA-PRESENTACION
---

# TEMPLATE — Evaluación de presentación de candidatura

> Instancia documental del `PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA`.
>
> Este documento valida si una candidatura documentalmente completa está preparada operativamente para ser presentada por el canal identificado.
>
> No presenta, no envía y no marca la candidatura como presentada.

---

# 1. Identificación

| Campo | Valor |
|---|---|
| Candidatura | `CAND-XXXX` |
| Empresa | |
| Puesto | |
| Paquete evaluado | `paquete-presentacion.md` |
| CV | `cv.pdf` |
| Carta | `carta-presentacion.pdf` |
| Veredicto CV | `veredicto-final-cv.md` |
| Veredicto carta | `veredicto-final-carta.md` |
| Canal | |
| URL/origen | |
| Fecha de evaluación | `AAAA-MM-DD` |
| Playbook | `PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA` |
| Versión playbook | `1.0.0` |
| Estado de evaluación | `en_evaluacion` \| `completado` \| `bloqueado` |

---

# 2. Estado inicial del gate

```yaml
gate_entrada:
  id: GATE-CANDIDATURA-PRESENTACION
  estado:
```

Condición requerida:

```text
GATE-CANDIDATURA-PRESENTACION = pendiente
```

## Comprobación

```yaml
precondicion_gate:
  cumplida: true | false
  incidencias: []
```

Si:

```text
cumplida = false
```

la evaluación debe quedar:

```yaml
estado_evaluacion: bloqueado
```

---

# 3. Precondiciones del paquete

```yaml
precondiciones:
  paquete_presentacion:
    estado:
    esperado: listo_para_gate

  presentada:
    valor:
    esperado: false

  gate_veredicto_cv:
    estado:
    esperado: aprobado

  gate_veredicto_carta:
    requerido: true | false
    estado:
    esperado: aprobado

  resultado:
    conforme: true | false
    incidencias: []
```

Si existe una precondición obligatoria incumplida:

```text
→ evaluación bloqueada_por_precondicion
```

---

# 4. Resultado ejecutivo

```yaml
resultado:
  evaluacion:
    APTA_PARA_PRESENTACION
    | APTA_CON_PENDIENTES_HUMANOS
    | BLOQUEADA

  bloqueantes: []
  pendientes_humanos: []
  advertencias: []

  gate_candidatura_presentacion:
    pendiente | aprobado | bloqueado

  presentada: false
```

## Justificación ejecutiva

[Explicar brevemente por qué la candidatura está preparada, pendiente de decisiones humanas o bloqueada.]

---

# 5. Canal de presentación

```yaml
canal_presentacion:
  tipo:
  origen:
  url:
  accesible: true | false
  oferta_disponible: true | false
  corresponde_empresa: true | false
  corresponde_puesto: true | false
  fecha_comprobacion:
  incidencias: []
```

## Evidencia

[Registrar evidencia suficiente para confirmar que se está evaluando el canal correcto.]

---

# 6. Integridad documental

```yaml
integridad_documental:
  cv:
    requerido: true | false
    disponible: true | false
    aprobado: true | false
    archivo:

  carta:
    requerida: true | false
    disponible: true | false
    aprobada: true | false
    archivo:

  otros_artefactos_requeridos: []
  otros_artefactos_disponibles: []

  resultado:
    conforme | no_conforme
```

## Incidencias documentales

| ID | Artefacto | Incidencia | Severidad |
|---|---|---|---|
| DOC-01 | | | bloqueante / advertencia / observacion |

---

# 7. Identidad de candidatura

```yaml
identidad:
  candidatura_correcta: true | false
  empresa_correcta: true | false
  puesto_correcto: true | false
  canal_corresponde_oferta: true | false
  incidencias: []
```

Empresa, puesto u oferta incorrectos:

```text
→ bloqueante
```

---

# 8. Correspondencia de versiones

```yaml
versiones:
  cv:
    corresponde_version_aprobada: true | false
    evidencia:

  carta:
    corresponde_version_aprobada: true | false
    evidencia:

  otros_artefactos: []

  incidencias: []
```

Una versión no aprobada:

```text
→ bloqueante
```

---

# 9. Compatibilidad con el canal

```yaml
compatibilidad_canal:
  formatos_documentales_aceptados: []
  limites_tamano: []
  otras_restricciones: []

  cv:
    compatible: true | false | no_verificable
    motivo:

  carta:
    compatible: true | false | no_aplica | no_verificable
    motivo:

  otros_artefactos: []

  resultado:
    conforme | no_conforme | parcialmente_verificado
```

---

# 10. Requisitos adicionales del canal

```yaml
requisitos_adicionales:
  cuenta_usuario:
    requerida: true | false | desconocido

  inicio_sesion:
    requerido: true | false | desconocido

  captcha:
    detectado: true | false | desconocido

  consentimiento:
    requerido: true | false | desconocido

  otros: []
```

---

# 11. Campos del formulario

Registrar cada campo identificado.

| ID | Campo | Obligatorio | Estado | Fuente / decisión necesaria |
|---|---|---:|---|---|
| CAM-01 | | sí / no | resuelto / requiere_dato_existente / requiere_decision_humana / requiere_respuesta_nueva / no_aplica | |

Estados válidos:

```text
resuelto
requiere_dato_existente
requiere_decision_humana
requiere_respuesta_nueva
no_aplica
```

---

# 12. Datos objetivos reutilizables

```yaml
datos_reutilizables:
  - campo:
    valor:
    fuente:
    autorizado: true | false
    listo_para_uso: true | false
```

Solo se consideran reutilizables datos:

```text
existentes
+
trazables
+
autorizados
```

---

# 13. Preguntas adicionales del canal

```yaml
preguntas_adicionales:
  - id:
    pregunta:
    obligatoria: true | false
    estado:
      resuelta
      | preparable_desde_fuentes
      | requiere_decision_humana
      | sin_evidencia_suficiente
    fuente_respuesta:
    respuesta_preparada:
```

No inventar respuestas.

---

# 14. Respuestas preparables

Una respuesta puede prepararse cuando existe respaldo suficiente en:

```text
datos-core
+
candidatura
+
artefactos aprobados
+
datos privados autorizados
```

Registrar:

```yaml
respuestas_preparables:
  - pregunta:
    respuesta:
    fuentes:
    requiere_validacion_humana: true | false
```

Preparar:

```text
≠ enviar
```

---

# 15. Decisiones humanas requeridas

```yaml
decisiones_humanas:
  - id:
    campo_o_pregunta:
    decision_necesaria:
    motivo:
    obligatoria_antes_envio: true | false
```

Ejemplos:

- disponibilidad;
- salario esperado;
- movilidad;
- fecha de incorporación;
- consentimiento;
- declaración personal;
- aceptación de condiciones.

---

# 16. Pendientes humanos

```yaml
pendientes_humanos:
  - id:
    tipo:
    descripcion:
    necesario_antes_envio: true | false
    estado: pendiente | resuelto
```

Un pendiente humano no es automáticamente un defecto documental.

---

# 17. Bloqueantes

```yaml
bloqueantes:
  existen: true | false
  cantidad:
  elementos: []
```

Ejemplos de bloqueantes:

- oferta incorrecta;
- oferta no disponible cuando impide presentación;
- empresa incorrecta;
- puesto incorrecto;
- CV requerido ausente;
- carta requerida ausente;
- artefacto no aprobado;
- versión no validada;
- formato no admitido;
- dato obligatorio imposible de resolver;
- gate previo obligatorio no aprobado.

---

# 18. Advertencias

```yaml
advertencias:
  - id:
    descripcion:
    impacto:
```

Las advertencias no impiden necesariamente la presentación.

---

# 19. Observaciones

```yaml
observaciones:
  - id:
    descripcion:
```

Observación:

```text
≠ bloqueante
≠ pendiente humano
```

---

# 20. Preparación operativa

```yaml
preparacion_operativa:
  artefactos_localizados: true | false
  canal_identificado: true | false
  canal_verificado: true | false
  campos_obligatorios_identificados: true | false
  respuestas_requeridas_resueltas: true | false
  pendientes_humanos: []
  bloqueos: []
```

---

# 21. Clasificación consolidada

```yaml
clasificacion:
  bloqueantes: []
  pendientes_humanos: []
  advertencias: []
  observaciones: []
```

---

# 22. Determinación del resultado

Aplicar:

```text
si existe ≥ 1 bloqueante
→ BLOQUEADA
```

```text
si no existen bloqueantes
y existen pendientes humanos obligatorios antes del envío
→ APTA_CON_PENDIENTES_HUMANOS
```

```text
si no existen bloqueantes
ni pendientes humanos obligatorios previos
→ APTA_PARA_PRESENTACION
```

Registrar:

```yaml
determinacion:
  numero_bloqueantes:
  numero_pendientes_humanos_previos:
  resultado_calculado:
```

---

# 23. Consistencia del resultado

```yaml
consistencia:
  reglas_aplicadas_correctamente: true | false
  incidencias: []
```

No permitido:

```text
bloqueante presente
+
APTA_PARA_PRESENTACION
```

---

# 24. Estado de `GATE-CANDIDATURA-PRESENTACION`

## Si `BLOQUEADA`

```yaml
gate:
  id: GATE-CANDIDATURA-PRESENTACION
  estado: bloqueado
  motivo:
```

---

## Si `APTA_CON_PENDIENTES_HUMANOS`

Por defecto:

```yaml
gate:
  id: GATE-CANDIDATURA-PRESENTACION
  estado: pendiente
  pendientes_por_resolver: []
```

No aprobar automáticamente mientras existan decisiones obligatorias previas.

---

## Si `APTA_PARA_PRESENTACION`

```yaml
gate:
  id: GATE-CANDIDATURA-PRESENTACION
  estado: aprobado
```

Esto significa únicamente:

```text
preparada para recibir una orden humana de presentación
```

---

# 25. Control de no presentación

```yaml
control_no_presentacion:
  se_pulso_enviar: false
  se_confirmo_candidatura: false
  se_envio_email: false
  se_realizo_accion_irreversible: false
  presentada: false
  conforme: true | false
```

Esperado:

```text
false
false
false
false
false
true
```

---

# 26. Acciones externas realizadas

```yaml
acciones_externas:
  inspeccion_canal: true | false
  navegacion_reversible: true | false
  campos_revisados: true | false
  formulario_enviado: false
  confirmacion_final_realizada: false
```

---

# 27. Acción irreversible detectada

```yaml
accion_irreversible:
  detectada: true | false
  descripcion:
  ejecutada: false
```

Si para continuar fuera necesario ejecutar una acción irreversible:

```text
detener
→ requerir instrucción humana
```

---

# 28. Estado `presentada`

```yaml
presentacion:
  presentada: false
  evidencia_presentacion: []
```

Solo puede pasar a `true` con evidencia real posterior de presentación efectiva.

---

# 29. Evidencias válidas de presentación futura

Ejemplos:

```text
confirmación del portal
identificador de candidatura
email de confirmación
comprobante equivalente
```

No constituye evidencia:

```text
GATE-CANDIDATURA-PRESENTACION = aprobado
```

---

# 30. Retorno a fase responsable

| Tipo de problema | Fase responsable |
|---|---|
| Documento incorrecto | fase documental correspondiente |
| Contenido incorrecto | contenido / guion correspondiente |
| Dato profesional insuficiente | fuente factual |
| Decisión personal pendiente | persona usuaria |
| Canal incorrecto | `paquete-presentacion.md` |
| Problema operativo portal | presentación |

```yaml
retorno_fase:
  necesario: true | false
  fase:
  motivo:
```

---

# 31. Revalidación

```yaml
revalidacion:
  necesaria: true | false
  motivo:
```

Debe considerarse si cambia materialmente:

- CV;
- carta;
- paquete;
- canal;
- oferta;
- requisito obligatorio;
- respuesta necesaria.

---

# 32. Siguiente acción

```yaml
siguiente_accion:
  tipo:
    corregir_bloqueo
    | resolver_pendientes_humanos
    | solicitar_orden_humana_de_presentacion
  detalle:
```

Si:

```text
resultado = APTA_PARA_PRESENTACION
```

la siguiente acción esperada es:

```text
solicitar_orden_humana_de_presentacion
```

---

# 33. Checklist de validación

## Precondiciones

- [ ] `paquete-presentacion.md = listo_para_gate`.
- [ ] `GATE-CANDIDATURA-PRESENTACION = pendiente`.
- [ ] `presentada = false`.
- [ ] `GATE-VEREDICTO-CV = aprobado`.
- [ ] `GATE-VEREDICTO-CARTA = aprobado`, cuando corresponda.

## Documentos

- [ ] CV requerido disponible.
- [ ] CV corresponde a versión aprobada.
- [ ] Carta requerida disponible.
- [ ] Carta corresponde a versión aprobada.
- [ ] Otros artefactos requeridos disponibles.

## Canal

- [ ] Canal identificado.
- [ ] URL/origen correcto.
- [ ] Empresa correcta.
- [ ] Puesto correcto.
- [ ] Oferta disponible o estado conocido.
- [ ] Formatos/restricciones revisados.

## Formulario

- [ ] Campos obligatorios identificados en lo posible.
- [ ] Datos objetivos trazables.
- [ ] Preguntas adicionales clasificadas.
- [ ] Decisiones humanas pendientes registradas.
- [ ] No se inventaron respuestas.

## Seguridad operativa

- [ ] No se realizó envío.
- [ ] No se confirmó candidatura.
- [ ] No se ejecutó acción irreversible.
- [ ] `presentada = false`.

## Resultado

- [ ] Bloqueantes clasificados.
- [ ] Pendientes humanos clasificados.
- [ ] Advertencias clasificadas.
- [ ] Resultado determinista.
- [ ] Gate actualizado de forma coherente.

---

# 34. Registro de pruebas

| Test | Resultado | Evidencia |
|---|---|---|
| T01 — Paquete correcto y canal compatible | | |
| T02 — CV requerido ausente | | |
| T03 — Carta requerida ausente | | |
| T04 — Documento no aprobado | | |
| T05 — Versión distinta de la aprobada | | |
| T06 — Empresa o puesto incorrectos | | |
| T07 — Campo pendiente de decisión humana | | |
| T08 — Pregunta resoluble desde fuentes | | |
| T09 — Pregunta sin evidencia suficiente | | |
| T10 — Gate aprobado mantiene `presentada=false` | | |
| T11 — Sin confirmación no se marca presentada | | |
| T12 — Confirmación real permite `presentada=true` | | |

---

# 35. Defectos generalizables

```yaml
defectos_generalizables: []
```

Para cada uno:

```yaml
- id:
  descripcion:
  candidatura_origen:
  fase_responsable:
  es_generalizable: true | false
  playbook_afectado:
  template_afectado:
  test_automatizable:
  accion_recomendada:
```

---

# 36. Resultado final

```yaml
resultado_final:
  evaluacion:
    APTA_PARA_PRESENTACION
    | APTA_CON_PENDIENTES_HUMANOS
    | BLOQUEADA

  bloqueantes: []
  pendientes_humanos: []
  advertencias: []

  gate_candidatura_presentacion:
    pendiente | aprobado | bloqueado

  presentada: false
```

## Justificación final

[Resumen diagnóstico breve.]

---

# 37. Conclusión contractual

```yaml
conclusion:
  candidatura:
  paquete:
  resultado:
  gate:
  presentada: false
  siguiente_accion:
```

Interpretación obligatoria:

```text
gate aprobado
→ candidatura preparada para una orden humana de presentación
```

No significa:

```text
candidatura presentada
```

---

# 38. Historial

## 1.0.0

Primera versión.

Implementa el contrato de `PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA v1.0.0` con:

- validación de precondiciones;
- integridad documental;
- identidad de candidatura;
- correspondencia de versiones;
- compatibilidad con canal;
- inventario de campos y preguntas;
- respuestas preparables;
- pendientes humanos;
- bloqueantes;
- control explícito de no presentación;
- resultados `APTA_PARA_PRESENTACION`, `APTA_CON_PENDIENTES_HUMANOS` y `BLOQUEADA`;
- gestión de `GATE-CANDIDATURA-PRESENTACION`;
- pruebas T01–T12.