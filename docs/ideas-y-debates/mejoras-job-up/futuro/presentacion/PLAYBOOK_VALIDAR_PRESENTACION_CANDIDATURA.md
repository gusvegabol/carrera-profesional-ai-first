---
id: PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA
tipo: playbook
version: "1.0.0"
estado: en_prueba
alcance: validacion_paquete_presentacion
entrada_principal: paquete-presentacion.md
entradas_auxiliares:
  - candidatura.md
  - cv.pdf
  - carta-presentacion.pdf
  - veredicto-final-cv.md
  - veredicto-final-carta.md
artefacto_salida: evaluacion-presentacion-candidatura.md
gate_entrada: GATE-CANDIDATURA-PRESENTACION
estado_gate_entrada_requerido: pendiente
gate_salida: GATE-CANDIDATURA-PRESENTACION
---

# PLAYBOOK — Validar presentación de candidatura

## 1. Propósito

Este playbook valida si una candidatura documentalmente completa está preparada para ser presentada correctamente por el canal identificado.

Su función comienza cuando:

```text
paquete-presentacion.md
→ estado = listo_para_gate
```

y una decisión humana abre:

```text
GATE-CANDIDATURA-PRESENTACION
→ pendiente
```

El playbook produce:

```text
evaluacion-presentacion-candidatura.md
```

y determina si el gate puede quedar:

```text
aprobado
o
bloqueado
```

No presenta ni envía la candidatura.

---

# 2. Pregunta central

La pregunta del playbook es:

> ¿Está el paquete completo, correcto y compatible con el canal real de presentación, de forma que una instrucción humana posterior pueda ordenar su envío sin reabrir la generación documental?

---

# 3. Posición en el flujo

```text
rama CV aprobada
        +
rama carta aprobada
        ↓
paquete-presentacion.md
estado = listo_para_gate
        ↓
DECISIÓN HUMANA:
abrir GATE-CANDIDATURA-PRESENTACION
        ↓
estado gate = pendiente
        ↓
PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA
        ↓
evaluacion-presentacion-candidatura.md
        ↓
GATE-CANDIDATURA-PRESENTACION
        ↓
aprobado | bloqueado
        ↓
si aprobado:
esperar instrucción humana explícita de presentación
```

---

# 4. Frontera contractual

Debe mantenerse siempre:

```text
paquete listo
≠
gate abierto
≠
gate aprobado
≠
orden humana de presentación
≠
envío efectivo
```

Y:

```text
GATE-CANDIDATURA-PRESENTACION = aprobado
≠
presentada = true
```

El gate valida preparación.

No ejecuta presentación.

---

# 5. Precondiciones

El playbook solo puede ejecutarse si:

```text
GATE-CANDIDATURA-PRESENTACION = pendiente
```

y además:

```text
paquete_presentacion = listo_para_gate
presentada = false
```

Debe comprobarse también, cuando la candidatura requiera CV y carta:

```text
GATE-VEREDICTO-CV = aprobado
GATE-VEREDICTO-CARTA = aprobado
```

Si cualquiera de estas precondiciones falla:

```text
evaluacion = bloqueada_por_precondicion
```

No continuar.

---

# 6. Responsabilidad

Este playbook valida exclusivamente la **preparación para la presentación**.

Debe comprobar:

1. integridad del paquete;
2. identidad de candidatura;
3. vigencia y correspondencia de artefactos;
4. adecuación al canal;
5. requisitos adicionales del formulario;
6. datos necesarios para completar la presentación;
7. existencia de bloqueos operativos;
8. coherencia entre lo preparado y lo que realmente exige el canal.

No debe:

- reescribir CV;
- reescribir carta;
- cambiar estrategia;
- generar nuevos argumentos;
- modificar hechos;
- presentar automáticamente;
- pulsar botones de envío;
- aceptar consentimientos;
- crear cuentas;
- responder preguntas nuevas con información inventada.

---

# 7. Fuente principal

La fuente principal es:

```text
paquete-presentacion.md
```

Este documento debe declarar al menos:

- candidatura;
- empresa;
- puesto;
- canal;
- URL u origen;
- artefactos requeridos;
- artefactos disponibles;
- estado del paquete;
- estado de presentación.

---

# 8. Fuentes auxiliares permitidas

Puede consultar:

```text
candidatura.md
cv.pdf
carta-presentacion.pdf
veredicto-final-cv.md
veredicto-final-carta.md
```

Solo para comprobar:

- identidad;
- versión correcta;
- aprobación;
- coherencia;
- contenido necesario para rellenar campos del canal.

Puede consultar también datos privados previamente autorizados cuando sean necesarios para completar campos objetivos del formulario.

---

# 9. Consulta del canal real

A diferencia de los playbooks editoriales anteriores, esta fase sí puede necesitar inspeccionar el canal externo de presentación.

Puede comprobar:

- que la URL sigue funcionando;
- que corresponde a la oferta correcta;
- campos obligatorios;
- documentos admitidos;
- formatos;
- límites de tamaño;
- preguntas adicionales;
- requisitos de cuenta;
- consentimientos;
- ubicación;
- disponibilidad;
- incorporación;
- experiencia requerida;
- otros campos que el portal solicite.

Pero:

> inspeccionar el canal no equivale a presentar la candidatura.

---

# 10. Prohibición de envío

Durante esta fase está prohibido ejecutar cualquier acción irreversible o externa que constituya presentación.

Incluye:

- pulsar `Enviar`;
- pulsar `Submit`;
- confirmar candidatura;
- aceptar una declaración final equivalente a envío;
- enviar email;
- completar automáticamente un último paso irreversible;
- marcar `presentada: true`.

Si el portal obliga a una acción irreversible para descubrir pasos posteriores:

```text
detener
→ registrar limitación
→ solicitar acción humana
```

---

# 11. Dimensiones de validación

La evaluación debe cubrir seis dimensiones.

## D1 — Integridad documental

Comprobar:

```yaml
integridad_documental:
  cv_requerido:
  cv_disponible:
  cv_aprobado:

  carta_requerida:
  carta_disponible:
  carta_aprobada:

  otros_artefactos_requeridos: []
  otros_artefactos_disponibles: []

  resultado:
    conforme | no_conforme
```

---

# 12. D2 — Identidad de candidatura

Comprobar:

```yaml
identidad:
  candidatura_correcta: true | false
  empresa_correcta: true | false
  puesto_correcto: true | false
  canal_corresponde_oferta: true | false
  incidencias: []
```

Una oferta o empresa incorrecta constituye bloqueante.

---

# 13. D3 — Correspondencia de versiones

Debe garantizarse que los archivos que se pretenden presentar son los mismos que fueron aprobados.

```yaml
versiones:
  cv:
    corresponde_version_aprobada: true | false

  carta:
    corresponde_version_aprobada: true | false

  incidencias: []
```

Una versión diferente no validada:

```text
→ bloqueante
```

---

# 14. D4 — Compatibilidad con el canal

Comprobar:

```yaml
compatibilidad_canal:
  canal_accesible: true | false
  oferta_disponible: true | false

  formatos_documentales_aceptados: []
  cv_compatible: true | false
  carta_compatible: true | false

  limites_detectados: []
  requisitos_adicionales: []

  resultado:
    conforme | no_conforme
```

---

# 15. D5 — Campos y preguntas del formulario

Registrar los campos visibles o conocidos que el canal exige.

Clasificar cada uno como:

```text
resuelto
requiere_dato_existente
requiere_decision_humana
requiere_respuesta_nueva
no_aplica
```

Ejemplo:

```yaml
campos_formulario:
  - campo: teléfono
    estado: resuelto
    fuente: datos autorizados

  - campo: disponibilidad
    estado: requiere_decision_humana

  - campo: experiencia gestionando equipos
    estado: requiere_respuesta_nueva
```

---

# 16. Respuestas nuevas solicitadas por el canal

Si el canal formula preguntas no contempladas previamente, no deben responderse mediante invención.

Debe intentarse resolverlas con:

```text
datos-core
+
candidatura
+
artefactos aprobados
+
datos privados autorizados
```

Si existe evidencia suficiente:

```text
→ puede prepararse una respuesta
```

Si requiere una decisión personal o información inexistente:

```text
→ requiere_decision_humana
```

La respuesta preparada no debe enviarse automáticamente.

---

# 17. D6 — Preparación operativa

Debe comprobarse:

```yaml
preparacion_operativa:
  artefactos_localizados: true | false
  canal_identificado: true | false
  campos_obligatorios_identificados: true | false
  respuestas_requeridas_resueltas: true | false
  decisiones_humanas_pendientes: []
  bloqueos: []
```

---

# 18. Clasificación de hallazgos

Los hallazgos se clasifican como:

```text
bloqueante
pendiente_humano
advertencia
observacion
```

---

# 19. Bloqueantes

Son bloqueantes, entre otros:

- oferta incorrecta;
- oferta cerrada o inaccesible cuando impida presentación;
- empresa o puesto incorrectos;
- falta de CV requerido;
- falta de carta requerida;
- CV no aprobado;
- carta no aprobada;
- versión de documento distinta de la aprobada;
- formato no admitido;
- falta de un dato obligatorio que no puede resolverse;
- contradicción entre paquete y canal;
- gate previo requerido no aprobado.

Regla:

```text
≥ 1 bloqueante
→ GATE-CANDIDATURA-PRESENTACION = bloqueado
```

---

# 20. Pendientes humanos

Un pendiente humano no significa que el paquete sea incorrecto.

Ejemplos:

- disponibilidad;
- salario esperado;
- consentimiento;
- movilidad;
- incorporación;
- respuesta personal;
- aceptación de condiciones;
- creación manual de cuenta;
- captcha;
- confirmación final.

Debe registrarse:

```yaml
pendientes_humanos:
  - campo:
    motivo:
    necesario_antes_envio: true | false
```

---

# 21. Advertencias

Son elementos que no impiden continuar pero deben conocer quien presenta.

Ejemplos:

- el portal no permite adjuntar carta;
- el canal transforma el CV;
- existe límite de tamaño;
- determinada información debe pegarse manualmente;
- la oferta podría exigir una pregunta adicional después de iniciar sesión.

---

# 22. Resultado de evaluación

La evaluación puede resultar:

```text
APTA_PARA_PRESENTACION
BLOQUEADA
APTA_CON_PENDIENTES_HUMANOS
```

---

# 23. Regla de determinación

```text
si existe bloqueante
→ BLOQUEADA
```

```text
si no existen bloqueantes
pero existen pendientes humanos necesarios antes del envío
→ APTA_CON_PENDIENTES_HUMANOS
```

```text
si no existen bloqueantes
ni pendientes humanos previos
→ APTA_PARA_PRESENTACION
```

---

# 24. Relación con el gate

## Resultado `BLOQUEADA`

```text
GATE-CANDIDATURA-PRESENTACION = bloqueado
```

Debe identificarse la causa y la fase responsable.

---

## Resultado `APTA_CON_PENDIENTES_HUMANOS`

El gate puede considerarse documentalmente validado solo si el contrato establece que esos pendientes se resolverán en el momento de presentación.

Por defecto:

```text
GATE-CANDIDATURA-PRESENTACION = pendiente
```

hasta resolver los pendientes humanos que sean obligatorios antes del envío.

---

## Resultado `APTA_PARA_PRESENTACION`

Habilita:

```text
GATE-CANDIDATURA-PRESENTACION = aprobado
```

pero no ejecuta presentación.

---

# 25. Decisión humana y envío

Incluso con:

```text
GATE-CANDIDATURA-PRESENTACION = aprobado
```

debe existir una nueva instrucción humana explícita equivalente a:

> Presenta esta candidatura.

Sin esa orden:

```text
presentada = false
```

---

# 26. Estado `presentada`

Solo puede pasar a:

```text
true
```

cuando exista evidencia de presentación efectiva.

Ejemplos:

- confirmación del portal;
- identificador de candidatura;
- email de confirmación;
- comprobante equivalente.

Nunca debe inferirse de:

```text
gate aprobado
```

---

# 27. Artefacto de salida

Genera:

```text
evaluacion-presentacion-candidatura.md
```

con estructura mínima:

```text
1. Identificación
2. Precondiciones
3. Canal
4. Integridad documental
5. Identidad
6. Versiones
7. Compatibilidad con canal
8. Campos del formulario
9. Respuestas requeridas
10. Pendientes humanos
11. Bloqueantes
12. Advertencias
13. Preparación operativa
14. Resultado
15. Estado del gate
16. Siguiente acción
```

---

# 28. Frontmatter mínimo

```yaml
---
id: evaluacion-presentacion-CAND-XXXX
tipo: evaluacion_presentacion_candidatura
version: "1.0.0"
estado: completado
candidatura: CAND-XXXX
fecha_evaluacion: AAAA-MM-DD
playbook: PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA
gate: GATE-CANDIDATURA-PRESENTACION
resultado: APTA_PARA_PRESENTACION | APTA_CON_PENDIENTES_HUMANOS | BLOQUEADA
presentada: false
---
```

---

# 29. Resultado ejecutivo

```yaml
resultado:
  evaluacion:
  bloqueantes: []
  pendientes_humanos: []
  advertencias: []
  gate_candidatura_presentacion:
  presentada: false
```

---

# 30. Retorno a fase responsable

Si se detecta un defecto:

```text
documento incorrecto
→ fase documental correspondiente

contenido incorrecto
→ fase de contenido correspondiente

datos insuficientes
→ fuente factual / decisión humana

canal incorrecto
→ paquete-presentacion

problema del portal
→ registrar bloqueo operativo
```

El playbook no debe corregir silenciosamente otra fase.

---

# 31. Revalidación

Si se modifica:

- CV;
- carta;
- paquete;
- canal;
- información obligatoria;

la evaluación debe revisarse o regenerarse cuando el cambio afecte materialmente a la presentación.

---

# 32. Pruebas mínimas

## T01 — Paquete correcto y canal compatible

Esperado:

```text
APTA_PARA_PRESENTACION
```

---

## T02 — CV requerido ausente

Esperado:

```text
BLOQUEADA
```

---

## T03 — Carta requerida ausente

Esperado:

```text
BLOQUEADA
```

---

## T04 — Documento no aprobado

Esperado:

```text
BLOQUEADA
```

---

## T05 — Versión distinta de la aprobada

Esperado:

```text
BLOQUEADA
```

---

## T06 — Empresa o puesto incorrectos

Esperado:

```text
BLOQUEADA
```

---

## T07 — Campo obligatorio pendiente de decisión humana

Esperado:

```text
APTA_CON_PENDIENTES_HUMANOS
```

---

## T08 — Pregunta resoluble desde fuentes autorizadas

Esperado:

```text
respuesta_preparable
```

sin envío automático.

---

## T09 — Pregunta sin evidencia suficiente

Esperado:

```text
requiere_decision_humana
```

---

## T10 — Gate aprobado

Esperado:

```text
presentada = false
```

---

## T11 — Presentación efectiva sin confirmación

Esperado:

```text
presentada sigue false
```

---

## T12 — Confirmación real de presentación

Solo entonces:

```text
presentada = true
```

---

# 33. Regla anti-automatización irreversible

La automatización puede:

- inspeccionar;
- validar;
- preparar;
- rellenar borradores reversibles;
- identificar campos;
- proponer respuestas.

No puede sin orden humana explícita:

- enviar;
- confirmar;
- aceptar el paso final;
- marcar presentada.

---

# 34. Criterios de éxito

El playbook se considera correctamente ejecutado si:

1. parte de un paquete `listo_para_gate`;
2. el gate está `pendiente`;
3. verifica los artefactos aprobados;
4. inspecciona los requisitos reales del canal;
5. identifica campos y decisiones pendientes;
6. no inventa respuestas;
7. distingue bloqueos de decisiones humanas;
8. determina preparación para presentación;
9. no ejecuta el envío;
10. mantiene `presentada: false`.

---

# 35. Estado inicial

```text
version: 1.0.0
estado: en_prueba
```

Debe validarse con CAND-2026-020 y al menos un caso de contraste antes de considerarse estable.

---

# 36. Criterio final

`PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA` constituye la frontera entre una candidatura documentalmente terminada y una candidatura preparada operativamente para ser presentada.

Su aprobación significa:

> La candidatura está preparada para que una persona responsable pueda ordenar su presentación.

No significa:

> La candidatura ha sido presentada.

---

# 37. Historial

## 1.0.0

Primera versión.

Introduce:

- separación entre paquete listo, gate abierto, gate aprobado y envío;
- validación del canal real;
- comprobación de artefactos y versiones;
- detección de campos y preguntas adicionales;
- clasificación de bloqueantes y pendientes humanos;
- prohibición de envío automático;
- salida `evaluacion-presentacion-candidatura.md`;
- estados `APTA_PARA_PRESENTACION`, `APTA_CON_PENDIENTES_HUMANOS` y `BLOQUEADA`;
- pruebas mínimas T01–T12.
