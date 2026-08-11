---
id: evaluacion-presentacion-CAND-2026-020
tipo: evaluacion_presentacion_candidatura
version: "1.0.0"
estado: completado
candidatura: CAND-2026-020
fecha_evaluacion: 2026-08-11
playbook: PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA
gate: GATE-CANDIDATURA-PRESENTACION
resultado: APTA_CON_PENDIENTES_HUMANOS
presentada: false
---

# Evaluación de presentación de candidatura — CAND-2026-020

## 1. Identificación

| Campo | Valor |
|---|---|
| Candidatura | `CAND-2026-020` |
| Empresa | Lidl Supermercados SAU |
| Puesto | Responsable de turno Tienda 40h Tamaraceite |
| Paquete evaluado | `paquete-presentacion.md` |
| CV | `cv.pdf` y `cv.docx` |
| Carta | `carta-presentacion.pdf` y `carta-presentacion.docx` |
| Canal | `portal_empresa` desde Indeed |
| URL de oferta | <https://empleo.lidl.es/jobs/responsable-de-turno-tienda-40h-tamaraceite-las-palmas-de-gran-canaria-gran-canaria-725913> |
| Referencia de oferta | `725913` |
| Fecha de evaluación | `2026-08-11` |

## 2. Precondiciones

```yaml
precondiciones:
  paquete_listo_para_gate: true
  gate_entrada_pendiente: true
  presentada_false: true
  gate_cv_aprobado: true
  gate_carta_aprobado: true
  incidencias: []
```

La decisión humana abrió `GATE-CANDIDATURA-PRESENTACION` en `pendiente` antes
de iniciar esta evaluación. No se aprobó el gate.

## 3. Canal real

```yaml
canal:
  tipo: portal_empresa
  origen: Indeed → portal de empleo Lidl
  url: https://empleo.lidl.es/jobs/responsable-de-turno-tienda-40h-tamaraceite-las-palmas-de-gran-canaria-gran-canaria-725913
  referencia_oferta: 725913
  canal_accesible: true
  oferta_disponible: true
  formatos_aceptados: no_determinados_sin_cuenta
  restricciones:
    - el botón Inscríbete conduce al flujo SuccessFactors
    - el flujo de inscripción requiere una cuenta o inicio de sesión
  cuenta_o_login: requerido
  captcha: no_observado
  consentimientos:
    - banner de tratamiento de datos/cookies visible en la oferta
    - términos de uso y política de privacidad requeridos al crear cuenta
  resultado: parcialmente_verificado
```

La oferta se inspeccionó directamente y sigue disponible. La navegación
reversible hasta el botón `Inscríbete` no envió información. El portal de
cuenta mostró las pantallas de inicio de sesión y creación de perfil, pero no
se introdujeron datos ni se aceptaron consentimientos.

## 4. Integridad documental

```yaml
integridad_documental:
  cv:
    requerido: true
    disponible: true
    aprobado: true
  carta:
    requerida: true
    disponible: true
    aprobada: true
  otros_requeridos: []
  otros_disponibles: []
  resultado: conforme
```

## 5. Identidad de candidatura

```yaml
identidad:
  candidatura_correcta: true
  empresa_correcta: true
  puesto_correcto: true
  canal_corresponde_oferta: true
  incidencias: []
```

La página confirma empresa Lidl, puesto, ubicación de Tamaraceite y referencia
`725913`.

## 6. Correspondencia de versiones

```yaml
versiones:
  cv:
    archivo: cv.pdf
    corresponde_version_aprobada: true
    referencia_aprobacion: GATE-VEREDICTO-CV aprobado
  carta:
    archivo: carta-presentacion.pdf
    corresponde_version_aprobada: true
    referencia_aprobacion: GATE-VEREDICTO-CARTA aprobado
  incidencias: []
```

No se generaron ni sustituyeron artefactos durante esta evaluación.

## 7. Compatibilidad con canal

```yaml
compatibilidad_canal:
  cv_compatible: parcialmente_verificado
  carta_compatible: parcialmente_verificado
  limites_detectados: []
  requisitos_adicionales:
    - completar o iniciar sesión en el portal SuccessFactors
    - crear perfil si no existe cuenta
    - aceptar los términos de uso y la política de privacidad del portal
  resultado: parcialmente_verificado
```

No fue posible confirmar formatos, tamaño máximo ni campos específicos de la
oferta sin atravesar el inicio de sesión/creación de cuenta.

## 8. Campos del formulario identificados

| Campo | Estado | Valor/respuesta preparable | Fuente | Necesario antes del envío |
|---|---|---|---|---|
| Email | requiere_dato_existente | Sí, usando el dato privado autorizado; no se introdujo | datos privados autorizados | sí |
| Repetición del email | requiere_dato_existente | Sí, usando el dato privado autorizado; no se introdujo | datos privados autorizados | sí |
| Contraseña | requiere_decision_humana | Debe crearla o aportarla la persona responsable | portal Lidl | sí |
| Repetición de contraseña | requiere_decision_humana | Debe introducirla la persona responsable | portal Lidl | sí |
| Nombre | requiere_dato_existente | Sí, usando el dato privado autorizado; no se introdujo | autorización de datos CV | sí |
| Apellidos | requiere_dato_existente | Sí, usando el dato privado autorizado; no se introdujo | autorización de datos CV | sí |
| País/Región de residencia | requiere_decision_humana | No se infiere; debe confirmarlo la persona responsable | portal Lidl | sí |
| Visibilidad del perfil | requiere_decision_humana | Debe elegir una de las tres opciones del portal | portal Lidl | sí |
| Notificaciones de puestos | requiere_decision_humana | Opcional; decisión de la persona responsable | portal Lidl | no |
| Novedades de Lidl | requiere_decision_humana | Opcional; decisión de la persona responsable | portal Lidl | no |
| Términos de uso y privacidad | requiere_decision_humana | Debe leer y aceptar la persona responsable | portal Lidl | sí |

## 9. Preguntas adicionales

```yaml
preguntas_adicionales:
  estado: no_observadas_sin_cuenta
  preguntas: []
  limitacion: El formulario específico de la oferta no es visible antes de iniciar sesión o crear cuenta.
```

No se ha inventado ninguna respuesta sobre disponibilidad, salario, movilidad,
motivación u otras condiciones personales.

## 10. Respuestas preparables

```yaml
respuestas_preparables:
  - campo_o_pregunta: email, nombre y apellidos
    respuesta: disponible desde los datos privados autorizados, pendiente de introducción humana
    fuentes:
      - autorización de datos CV de CAND-2026-020
    requiere_revision_humana: true
```

Preparar estas respuestas no autoriza introducirlas ni enviarlas.

## 11. Decisiones humanas

```yaml
decisiones_humanas:
  - campo: consentimiento de cookies/tratamiento de datos del sitio
    decision_requerida: elegir configuración
    motivo: el banner estaba visible y no se debe elegir una preferencia de privacidad en nombre de la persona
    necesaria_antes_del_envio: no_determinable
  - campo: cuenta, contraseña y visibilidad del perfil
    decision_requerida: crear cuenta o iniciar sesión y elegir preferencias
    motivo: el portal SuccessFactors las exige antes de continuar
    necesaria_antes_del_envio: true
  - campo: términos de uso y política de privacidad
    decision_requerida: lectura y aceptación
    motivo: requisito explícito del portal
    necesaria_antes_del_envio: true
```

## 12. Pendientes humanos

```yaml
pendientes_humanos:
  - campo: cuenta o inicio de sesión Lidl
    motivo: el portal no permite continuar al formulario específico sin cuenta
    necesario_antes_envio: true
  - campo: contraseña y país/región de residencia
    motivo: datos/decisiones no disponibles en las fuentes permitidas
    necesario_antes_envio: true
  - campo: visibilidad del perfil y aceptación de términos
    motivo: consentimiento personal requerido por el portal
    necesario_antes_envio: true
```

## 13. Bloqueantes

```yaml
bloqueantes: []
```

La documentación está completa y la oferta/identidad son correctas. La falta
de acceso a la cuenta no se clasifica como defecto documental; queda como
pendiente humano previo al envío.

## 14. Advertencias

```yaml
advertencias:
  - descripcion: El canal muestra un banner de cookies/tratamiento de datos antes de continuar.
    impacto: Requiere una elección humana de privacidad o una configuración ya existente.
  - descripcion: La oferta contiene un requisito de FP de Grado Medio o equivalente que no se presenta como titulación finalizada en el expediente.
    impacto: Debe revisarse personalmente cualquier pregunta del portal sobre formación.
  - descripcion: La discrepancia salarial entre Indeed y Lidl se conserva con su procedencia.
    impacto: No debe resolverse por inferencia al responder campos salariales.
```

## 15. Preparación operativa

```yaml
preparacion_operativa:
  artefactos_localizados: true
  canal_identificado: true
  canal_verificado: parcialmente
  campos_obligatorios_identificados: parcialmente
  respuestas_requeridas_resueltas: false
  pendientes_humanos:
    - cuenta/login
    - contraseña
    - país/región de residencia
    - visibilidad del perfil
    - aceptación de términos
  bloqueos: []
```

## 16. Resultado

```yaml
resultado:
  evaluacion: APTA_CON_PENDIENTES_HUMANOS
  bloqueantes: []
  pendientes_humanos:
    - cuenta o inicio de sesión
    - datos y preferencias requeridos por SuccessFactors
    - consentimientos y términos
  advertencias:
    - formulario específico no visible sin cuenta
    - banner de privacidad requiere decisión humana
  observaciones:
    - La candidatura documental está completa y sus versiones corresponden a las aprobadas.
```

La determinación es `APTA_CON_PENDIENTES_HUMANOS`: no hay bloqueantes
documentales, pero sí decisiones y datos obligatorios antes de poder enviar.

## 17. Estado del gate

```yaml
gate:
  id: GATE-CANDIDATURA-PRESENTACION
  estado: pendiente
  decision_humana: apertura_de_validacion
  fecha_decision_humana: 2026-08-11
  motivo: La validación detecta pendientes humanos obligatorios; no se aprueba el gate.
```

## 18. Control de no presentación

```yaml
control_no_presentacion:
  se_pulso_enviar: false
  se_confirmo_candidatura: false
  se_envio_email: false
  se_realizo_accion_irreversible: false
  presentada: false
```

No se introdujeron datos personales, no se aceptaron términos, no se creó una
cuenta y no se ejecutó ninguna acción irreversible.

## 19. Siguiente acción

```yaml
siguiente_accion:
  responsable: persona_responsable
  accion: Resolver los pendientes de cuenta, privacidad y formulario, y aportar una orden explícita solo si desea presentar.
  requiere_orden_humana_explicita: true
  no_iniciar_envio_automatico: true
```

La evaluación no abre por sí sola una orden de envío.

## 20. Trazabilidad y revisión

| Comprobación | Resultado | Fuente/evidencia |
|---|---|---|
| T01 paquete y canal compatibles | parcial | paquete + oferta Lidl |
| T02 CV ausente | pasa | `cv.pdf` disponible y aprobado |
| T03 carta ausente | pasa | `carta-presentacion.pdf` disponible y aprobada |
| T04 documento no aprobado | pasa | gates CV y carta aprobados |
| T05 versión no validada | pasa | artefactos coinciden con veredictos |
| T06 empresa/puesto incorrectos | pasa | oferta Lidl, puesto y referencia `725913` |
| T07 pendiente humano | detectado | cuenta, privacidad y campos obligatorios |
| T08 pregunta resoluble | parcial | datos de identidad pueden prepararse, no introducirse |
| T09 pregunta sin evidencia | pendiente | formulario específico aún no visible |
| T10 gate aprobado no presenta | no aplica; gate sigue pendiente | control de gate |
| T11 sin confirmación sigue false | pasa | no existe confirmación |
| T12 confirmación real permite true | no ejecutado | fuera de alcance |

La evaluación deberá regenerarse si la persona crea/inicia sesión, si el portal
revela campos adicionales o si cambia un artefacto, el canal o un requisito
material.
