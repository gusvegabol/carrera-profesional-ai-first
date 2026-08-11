---
id: contenido-carta-presentacion-CAND-2026-020
tipo: contenido_carta_presentacion
version_playbook: "1.1.0"
version_template: "1.1.0"
version_guion: "1.0.1"
version_instancia: "1.1.0"
candidatura: CAND-2026-020
empresa: Lidl Supermercados SAU
puesto: Responsable de turno Tienda 40h Tamaraceite
idioma: es
fecha_generacion: 2026-08-10
motivo_regeneracion: correccion_expansion_semantica_y_regeneracion_desde_fuentes_canonicas
gate_entrada: GATE-GUION-CARTA-CONTENIDO
estado_gate_entrada: aprobado
gate_salida: GATE-CONTENIDO-CARTA-COMPOSICION
estado_contenido: apto
recomendacion_gate: aprobar
decision_humana: aprobado
estado_gate_salida: aprobado
fecha_decision_humana: 2026-08-10
motivo_decision_humana: contenido_factual_editorialmente_autorizado_y_trazable; autoriza_unicamente_composicion_futura
sesion: sesion-20260805-1757-job-up
---

# Contenido de carta de presentación — CAND-2026-020

> Artefacto semántico final antes de la composición. Regenerado desde el guion aprobado y las fuentes canónicas; no es una corrección incremental de la carta anterior.

## 1. Identificación

| Campo | Valor |
| --- | --- |
| Candidatura | `CAND-2026-020` |
| Empresa objetivo | Lidl Supermercados SAU |
| Puesto objetivo | Responsable de turno Tienda 40h Tamaraceite |
| Destinatario | Equipo de selección de Lidl Supermercados SAU |
| Idioma | `es` |
| Guion fuente | `guion-carta-presentacion.md` |
| Versión del guion | `1.0.1` |
| Playbook | `PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION` |
| Versión del playbook | `1.1.0` |
| Template | `TEMPLATE_CONTENIDO_CARTA_PRESENTACION` |
| Versión del template | `1.1.0` |
| Gate de entrada | `GATE-GUION-CARTA-CONTENIDO` |
| Estado gate entrada | `aprobado` |

## 2. Estado

```yaml
estado_contenido:
  resultado: apto
  motivo_principal: carta_factual_natural_y_fiel_al_guion_v1_1
  decision_humana: pendiente
  estado_gate_salida: pendiente
```

## 3. Fuentes

| Fuente | Disponible | Autoridad / uso |
| --- | --- | --- |
| `guion-carta-presentacion.md` | sí | autoridad editorial inmediata |
| `candidatura.md` | sí | estrategia común y privacidad |
| `analisis-oferta.md` | sí | contexto de necesidades |
| `datos-core-busqueda.md` | sí | verificación factual HER-03, HER-04, HER-07, HER-08 y HER-10 |
| declaraciones del usuario | sí | motivación personal: ninguna; relación previa: ninguna |
| fuentes culturales autorizadas | sí | contexto de Lidl, sin atribuir afinidad personal |

No se consultaron documentos de composición ni artefactos de presentación para decidir el contenido.

## 4. Brief heredado del guion

```yaml
destinatario: Equipo de selección de Lidl Supermercados SAU
idioma: es
objetivo_comunicativo: demostrar_encaje_operativo_transferible_para_responsable_de_turno
argumento_central: experiencia_practica_en_pedidos_stock_rotacion_ejecucion_y_caja
motivaciones_autorizadas: []
cultura_utilizable: [formacion_y_desarrollo_como_contexto_de_lidl]
evidencias_prioritarias: [HER-03, HER-07, HER-04, HER-08]
evidencias_factuales_no_seleccionadas: [HER-10]
longitud_objetivo: 220
rango_admisible: 180-280
tono: profesional_humano_directo
```

## 5. Ejecución de roles

### 5.1 Rol 1 — Redactor senior

```yaml
estado: completado
entrada: guion-carta-presentacion.md
salida: primer_borrador_v1_1
voz_candidato: superada
evidencia_nueva: no
restricciones_expuestas: no
funcion: convertir_seis_bloques_autorizados_en_una_carta_directa_y_natural
```

El redactor utilizó únicamente A-001–A-006, mantuvo la motivación personal vacía y formuló las limitaciones como controles internos, no como frases visibles.

### 5.2 Rol 2 — Recruiter senior — Primera lectura recruiter

```yaml
estado: completado
primer_escaneo: si
utilidad_por_parrafo: si
encaje_comprensible: si
complementariedad_con_cv: interpreta_y_conecta
voz_natural: si
genericidad: no
lenguaje_defensivo: no
lenguaje_metaanalitico: no
senales_materiales_ia: no
accion: conservar_borrador_con_ajustes_de_concision
```

La primera lectura pidió que la apertura entrase directamente en operaciones de tienda y que el cierre no añadiera motivación no declarada.

### 5.3 Rol 3 — Auditor factual y contractual

```yaml
estado: completado
afirmaciones_trazables: si
metricas: 30_por_ciento_y_80_por_ciento_conservadas
responsabilidades_ampliadas: no
seniority_ampliado: no
herramientas_no_acreditadas: no
formacion_convertida_en_titulacion: no
motivacion_fabricada: no
cultura_convertida_en_afinidad: no
empresa_o_intermediario_inferido: no
privacidad: conforme
accion: mantener_formulaciones_positivas_y_no_exponer_precauciones
```

La auditoría confirmó los pedidos centralizados y directos autorizados por A-002. La negociación con proveedores existe en datos-core, pero no fue seleccionada por ningún A-NNN de este guion y queda excluida del contenido.

### 5.4 Segunda lectura recruiter tras corrección factual

```yaml
estado: completado
primer_escaneo: si
utilidad_por_parrafo: si
complementariedad_con_cv: interpreta_y_conecta
voz_natural: si
genericidad: no
lenguaje_defensivo: no
lenguaje_metaanalitico: no
regresion_tras_auditoria: no
resultado: apto
```

La segunda lectura es obligatoria y confirma que la revisión factual no convirtió el texto en una explicación del sistema.

## 6. Trazabilidad por bloques

| Bloque | Función | Refs. guion | Evidencias / contexto |
| --- | --- | --- | --- |
| B-01 | saludo | A-001 | destinatario resuelto |
| B-02 | apertura y encaje | A-001 | operaciones de supermercado |
| B-03 | pedidos y disponibilidad | A-002 | HER-03 |
| B-04 | stock, rotación y ejecución | A-003, A-004 | HER-07, HER-04, HER-08 |
| B-05 | disponibilidad y turnos | A-005 | disponibilidad confirmada |
| B-06 | adaptación contextual y cierre | A-005, A-006 | formación de Lidl como contexto; conversación profesional |

## 6.1 Conjunto cerrado de afirmaciones autorizadas

Cada afirmación profesional visible se vincula a una decisión editorial del guion y a la evidencia factual compatible con esa decisión.

| claim_id | Refs. guion | Evidencia factual compatible | Frase visible exacta |
| --- | --- | --- | --- |
| CL-001 | A-001 | HER-03, HER-07 | Me gustaría poner mi experiencia en operaciones de supermercados a disposición del puesto de Responsable de turno en Tamaraceite. |
| CL-002 | A-001, A-004 | HER-03, HER-04, HER-07, HER-08 | He trabajado con la disponibilidad de producto, la organización diaria y el seguimiento de tareas que sostienen el funcionamiento de una tienda. |
| CL-003 | A-002 | HER-03 | En Herfrailes preparaba previsiones a partir de las ventas y diseñaba pedidos diarios para la central y para proveedores directos. |
| CL-004 | A-002 | HER-03 | Automatizar parte de ese proceso me ayudaba a ajustar las cantidades al consumo real y a mantener el surtido disponible. |
| CL-005 | A-003 | HER-03, HER-07 | En la gestión de stock y rotación conseguí reducir un 30 % las caducidades y un 80 % los productos sin venta durante más de un mes, y coordiné la redistribución de existencias entre tres tiendas. |
| CL-006 | A-004 | HER-04, HER-08 | Organizaba el trabajo por tienda, seguía las tareas y atendía las incidencias escaladas. |
| CL-007 | A-005 | CONTEXTO | Tengo disponibilidad para trabajar en turnos rotativos de mañana o tarde. |
| CL-008 | A-005 | CONTEXTO | La formación inicial de Lidl ofrece un marco para conocer sus procedimientos y trasladar esta experiencia a la operativa de Tamaraceite. |
| CL-009 | A-006 | — | Quedo a su disposición para conversar sobre cómo podría contribuir al equipo. |

La negociación con proveedores y los cuadres de caja existen en datos-core, pero no pertenecen a ningún `A-NNN` autorizado en este guion; por ello no forman parte de este conjunto.

## 7. Controles editoriales

| Control | Resultado | Observación interna |
| --- | --- | --- |
| Restricción ≠ contenido | conforme | se afirma la experiencia permitida; no se explican límites |
| Formulación positiva | conforme | pedidos, caja y Excel expresados directamente; negociación no incorporada |
| Voz del candidato | conforme | primera persona y tono profesional |
| Lenguaje metaanalítico | no detectado | no se habla del análisis ni del expediente |
| Utilidad frase por frase | conforme | cada párrafo explica encaje, evidencia o continuidad |
| Primer escaneo | conforme | puesto y núcleo operativo aparecen en la apertura |
| Anti-segundo-CV | conforme | se interpreta la relevancia y no se enumera la trayectoria |
| Anti-genericidad | conforme | Tamaraceite, Lidl y necesidades operativas concretas |
| Anti-IA | conforme | lenguaje directo, sin clichés ni simetría artificial |
| Elogios genéricos | no | no hay elogios vacíos a Lidl |
| ATS / recruiter IA | conforme | vocabulario respaldado, sin keyword stuffing |
| Factualidad | conforme | solo afirmaciones del conjunto cerrado A-001–A-006 |
| No expansión semántica | conforme | no se detectan afirmaciones profesionales nuevas |

## 8. Saludo

### Texto

Estimado equipo de selección:

### Trazabilidad

`B-01` / `A-001`

## 9. Apertura

### Texto

Me gustaría poner mi experiencia en operaciones de supermercados a disposición del puesto de Responsable de turno en Tamaraceite. He trabajado con la disponibilidad de producto, la organización diaria y el seguimiento de tareas que sostienen el funcionamiento de una tienda.

### Trazabilidad

`B-02` / `A-001`, `A-004` / HER-03, HER-04, HER-07, HER-08

## 10. Desarrollo argumental

### Texto

En Herfrailes preparaba previsiones a partir de las ventas y diseñaba pedidos diarios para la central y para proveedores directos. Automatizar parte de ese proceso me ayudaba a ajustar las cantidades al consumo real y a mantener el surtido disponible.

### Trazabilidad

`B-03` / `A-002` / HER-03

## 11. Desarrollo complementario

### Texto

En la gestión de stock y rotación conseguí reducir un 30 % las caducidades y un 80 % los productos sin venta durante más de un mes, y coordiné la redistribución de existencias entre tres tiendas. Organizaba el trabajo por tienda, seguía las tareas y atendía las incidencias escaladas.

### Trazabilidad

`B-04` / `A-003`, `A-004` / HER-07, HER-04, HER-08

## 12. Cultura y contexto de empresa

### Texto incorporado

Tengo disponibilidad para trabajar en turnos rotativos de mañana o tarde. La formación inicial de Lidl ofrece un marco para conocer sus procedimientos y trasladar esta experiencia a la operativa de Tamaraceite.

### Fuente y refs. guion

Oferta, datos-core y `CULT-EXT-002` / `A-005`.

### Control

Se usa la formación de Lidl como contexto de adaptación. No se afirma experiencia previa en Lidl, afinidad cultural ni motivación personal.

## 13. Motivación

```yaml
declarada_por_usuario: false
incluida_en_carta: false
tratamiento: la carta se apoya en razón profesional factual y no inventa emoción
```

## 14. Carencias y límites

La FP de Grado Medio no se incorpora a la carta porque el guion la reserva para contextualización solo si resulta imprescindible. No se presenta titulación ni equivalencia.

## 15. Cierre

### Texto

Quedo a su disposición para conversar sobre cómo podría contribuir al equipo.

Atentamente,

Gustavo Vega

gusvegabol@gmail.com

669 549 933

### Trazabilidad

`B-06` / `A-006` / datos privados autorizados en `candidatura.md`

## 16. Carta completa consolidada

Estimado equipo de selección:

Me gustaría poner mi experiencia en operaciones de supermercados a disposición del puesto de Responsable de turno en Tamaraceite. He trabajado con la disponibilidad de producto, la organización diaria y el seguimiento de tareas que sostienen el funcionamiento de una tienda.

En Herfrailes preparaba previsiones a partir de las ventas y diseñaba pedidos diarios para la central y para proveedores directos. Automatizar parte de ese proceso me ayudaba a ajustar las cantidades al consumo real y a mantener el surtido disponible.

En la gestión de stock y rotación conseguí reducir un 30 % las caducidades y un 80 % los productos sin venta durante más de un mes, y coordiné la redistribución de existencias entre tres tiendas. Organizaba el trabajo por tienda, seguía las tareas y atendía las incidencias escaladas.

Tengo disponibilidad para trabajar en turnos rotativos de mañana o tarde. La formación inicial de Lidl ofrece un marco para conocer sus procedimientos y trasladar esta experiencia a la operativa de Tamaraceite.

Quedo a su disposición para conversar sobre cómo podría contribuir al equipo.

Atentamente,

Gustavo Vega
gusvegabol@gmail.com
669 549 933

## 17. Control final del contenido

```yaml
palabras_reales: 185
resultado: interpreta_y_conecta
podria_enviarse_a_otra_empresa_cambiando_solo_el_nombre: no
restricciones_internas_expuestas: no
lenguaje_defensivo_visible: no
voz_candidato: si
lenguaje_metaanalitico: no
frases_prescindibles: no
segunda_lectura_recruiter: superada
correccion_factual_revisada_por_recruiter: si
No_se_detectan_afirmaciones_profesionales_nuevas: si
```

## 18. Nueva información

### Nueva evidencia profesional

```yaml
detectada: no
accion: no incorporar; no requiere actualización factual
```

### Nueva decisión necesaria

```yaml
detectada: no
accion: no decidir localmente
```

No se detecta ninguna decisión nueva ni expansión semántica; el contenido se mantiene dentro del contrato aprobado.

No se detectan afirmaciones profesionales nuevas.

## 19. Resultado y gate

```yaml
estado_contenido: apto
recomendacion_ia: aprobar
decision_humana: aprobado
estado_gate: aprobado
```

La aprobación humana autoriza únicamente el avance a la futura fase de composición de la carta. No autoriza el gate final de la carta, incorporar la carta al paquete como aprobada, abrir `GATE-CANDIDATURA-PRESENTACION` ni presentar o enviar externamente la candidatura.

## 20. Postcondición

El contenido semántico queda aprobado para pasar a la futura composición. No se han creado carta DOCX/PDF/LaTeX, ni se ha iniciado sesión, cargado archivo o enviado información a Lidl. La composición se diseñará primero en ChatGPT.
