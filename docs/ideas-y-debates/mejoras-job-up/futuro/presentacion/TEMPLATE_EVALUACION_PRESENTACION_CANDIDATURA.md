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

# Evaluación de presentación de candidatura

Este template documenta la preparación operativa del paquete. No presenta,
envía, confirma ni modifica `presentada`.

## 1. Identificación

| Campo | Valor |
|---|---|
| Candidatura | `CAND-XXXX` |
| Empresa | |
| Puesto | |
| Canal | |
| URL/origen | |
| Fecha de evaluación | `AAAA-MM-DD` |
| Paquete evaluado | `paquete-presentacion.md` |

## 2. Precondiciones

```yaml
precondiciones:
  paquete_listo_para_gate: true | false
  gate_entrada_pendiente: true | false
  presentada_false: true | false
  gate_cv_aprobado: true | false
  gate_carta_aprobado: true | false
  incidencias: []
```

## 3. Canal

```yaml
canal:
  tipo:
  url:
  corresponde_oferta: true | false
  accesible: true | false
  oferta_disponible: true | false
  formatos_aceptados: []
  restricciones: []
  cuenta_o_login:
  captcha:
  consentimientos:
  resultado: conforme | no_conforme | parcialmente_verificado
```

## 4. Integridad documental

```yaml
integridad_documental:
  cv:
    requerido: true
    disponible: true | false
    aprobado: true | false
  carta:
    requerida: true
    disponible: true | false
    aprobada: true | false
  otros_requeridos: []
  otros_disponibles: []
  resultado: conforme | no_conforme
```

## 5. Identidad

```yaml
identidad:
  candidatura_correcta: true | false
  empresa_correcta: true | false
  puesto_correcto: true | false
  canal_corresponde_oferta: true | false
  incidencias: []
```

## 6. Versiones

```yaml
versiones:
  cv:
    archivo:
    corresponde_version_aprobada: true | false
    referencia_aprobacion:
  carta:
    archivo:
    corresponde_version_aprobada: true | false
    referencia_aprobacion:
  incidencias: []
```

## 7. Compatibilidad con canal

```yaml
compatibilidad_canal:
  cv_compatible: true | false
  carta_compatible: true | false
  limites_detectados: []
  requisitos_adicionales: []
  resultado: conforme | no_conforme | parcialmente_verificado
```

## 8. Campos del formulario

| Campo | Estado | Valor/respuesta preparable | Fuente | Necesario antes del envío |
|---|---|---|---|---|
| | resuelto / requiere_dato_existente / requiere_decision_humana / requiere_respuesta_nueva / no_aplica | | | sí/no |

## 9. Preguntas adicionales

| Pregunta | Clasificación | Evidencia disponible | Respuesta preparable | Fuente |
|---|---|---|---|---|
| | resuelto / requiere_decision_humana / requiere_respuesta_nueva / no_aplica | | | |

No se inventarán respuestas. Preparar una respuesta no equivale a enviarla.

## 10. Respuestas preparables

```yaml
respuestas_preparables:
  - campo_o_pregunta:
    respuesta:
    fuentes: []
    requiere_revision_humana: true | false
```

## 11. Decisiones humanas

```yaml
decisiones_humanas:
  - campo:
    decision_requerida:
    motivo:
    necesaria_antes_del_envio: true | false
```

## 12. Pendientes humanos

```yaml
pendientes_humanos:
  - campo:
    motivo:
    necesario_antes_envio: true | false
```

## 13. Bloqueantes

```yaml
bloqueantes:
  - id:
    descripcion:
    fase_responsable:
    consecuencia:
```

## 14. Advertencias

```yaml
advertencias:
  - descripcion:
    impacto:
```

## 15. Preparación operativa

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

## 16. Resultado

```yaml
resultado:
  evaluacion: APTA_PARA_PRESENTACION | APTA_CON_PENDIENTES_HUMANOS | BLOQUEADA
  bloqueantes: []
  pendientes_humanos: []
  advertencias: []
  observaciones: []
```

Regla determinista:

```text
algún bloqueante → BLOQUEADA
sin bloqueantes y pendiente humano obligatorio → APTA_CON_PENDIENTES_HUMANOS
sin bloqueantes ni pendientes humanos obligatorios → APTA_PARA_PRESENTACION
```

## 17. Estado del gate

```yaml
gate:
  id: GATE-CANDIDATURA-PRESENTACION
  estado: pendiente | aprobado | bloqueado
  decision_humana:
  fecha_decision_humana:
  motivo:
```

`GATE-CANDIDATURA-PRESENTACION: aprobado` solo significa que puede recibirse
una orden humana posterior. No equivale a `presentada: true`.

## 18. Control de no presentación

```yaml
control_no_presentacion:
  se_pulso_enviar: false
  se_confirmo_candidatura: false
  se_envio_email: false
  se_realizo_accion_irreversible: false
  presentada: false
```

## 19. Siguiente acción

```yaml
siguiente_accion:
  responsable:
  accion:
  requiere_orden_humana_explicita: true
  no_iniciar_envio_automatico: true
```

## 20. Trazabilidad y revisión

| Comprobación | Resultado | Fuente/evidencia |
|---|---|---|
| T01 paquete y canal compatibles | | |
| T02 CV ausente | | |
| T03 carta ausente | | |
| T04 documento no aprobado | | |
| T05 versión no validada | | |
| T06 empresa/puesto incorrectos | | |
| T07 pendiente humano | | |
| T08 pregunta resoluble | | |
| T09 pregunta sin evidencia | | |
| T10 gate aprobado no presenta | | |
| T11 sin confirmación sigue false | | |
| T12 confirmación real permite true | | |

La evaluación debe regenerarse si cambia un artefacto, el canal o un requisito
material de presentación.
