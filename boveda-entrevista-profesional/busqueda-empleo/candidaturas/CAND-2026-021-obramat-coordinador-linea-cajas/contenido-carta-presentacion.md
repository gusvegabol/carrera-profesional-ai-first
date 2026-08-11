---
id: contenido-carta-presentacion-CAND-2026-021
tipo: contenido_carta_presentacion
version_playbook: "1.1.0"
version_template: "1.1.0"
version_guion: "1.0.0"
version_instancia: "1.0.0"
candidatura: CAND-2026-021
empresa: OBRAMAT
puesto: Coordinador/a de línea de Cajas Evolutivo/a
idioma: es
fecha_generacion: 2026-08-11
gate_entrada: GATE-GUION-CARTA-CONTENIDO
estado_gate_entrada: aprobado
gate_salida: GATE-CONTENIDO-CARTA-COMPOSICION
estado_contenido: apto
recomendacion_gate: aprobar
decision_humana: aprobado
estado_gate_salida: aprobado
sesion: sesion-20260805-1757-job-up
---

# Contenido de carta de presentación — CAND-2026-021

> Artefacto semántico final antes de la composición. Redactado desde el guion
> aprobado; no contiene decisiones visuales ni autoriza composición o envío.

## 1. Identificación y fuentes

| Campo | Valor |
| --- | --- |
| Candidatura | `CAND-2026-021` |
| Empresa objetivo | OBRAMAT |
| Puesto | Coordinador/a de línea de Cajas Evolutivo/a |
| Destinatario | Equipo de selección de OBRAMAT |
| Idioma | `es` |
| Guion fuente | `guion-carta-presentacion.md` |
| Playbook | `PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION` v1.1.0 |
| Gate de entrada | `GATE-GUION-CARTA-CONTENIDO` aprobado el 2026-08-11 |

Fuentes consultadas: guion, candidatura, análisis de oferta, datos core,
declaraciones humanas registradas y contexto oficial de OBRAMAT. No se
consultaron artefactos de composición para decidir el contenido.

## 2. Ejecución de roles

```yaml
rol_redactor:
  estado: completado
  voz_candidato: superada
  evidencia_nueva: no
  restricciones_expuestas: no
rol_recruiter_primera_lectura:
  estado: completado
  primer_escaneo: sí
  utilidad_por_parrafo: sí
  encaje_comprensible: sí
  complementariedad_con_cv: interpreta_y_conecta
  genericidad: no
  lenguaje_defensivo: no
  lenguaje_metaanalitico: no
rol_auditor_factual:
  estado: completado
  afirmaciones_trazables: sí
  motivacion_fabricada: no
  cultura_convertida_en_afinidad: no
  responsabilidades_ampliadas: no
  privacidad: conforme
rol_recruiter_segunda_lectura:
  estado: completado
  regresion_tras_auditoria: no
  resultado: apto
```

## 3. Conjunto cerrado de afirmaciones autorizadas

| claim_id | Refs. guion | Evidencia compatible | Frase o idea visible |
| --- | --- | --- | --- |
| CL-001 | A-001 | HER-04, HER-06, HER-10 | Experiencia en operaciones de supermercados, atención, coordinación y cajas aplicada al puesto. |
| CL-002 | A-002 | HER-06 | Atención y resolución de reclamaciones cuando los responsables no podían hacerlo. |
| CL-003 | A-004 | HER-04, HER-08 | Equipos polivalentes y seguimiento de tareas, incluidas las de Cajas. |
| CL-004 | A-003 | HER-10 | Cuadres de caja y sistema de mejora en Excel. |
| CL-005 | A-004, A-006 | HER-07, confirmación humana, datos core | Pedidos, automatización de pedidos, stock, redistribución y turnos. |
| CL-006 | A-005 | declaración del usuario + contexto oficial | Conocimiento de OBRAMAT como cliente y contexto de servicio, sin afinidad atribuida. |
| CL-007 | A-007 | — | Cierre profesional abierto a conversación. |

Toda afirmación profesional visible pertenece a este conjunto. La negociación
con proveedores, la movilidad por Canarias y los sistemas específicos de caja
de OBRAMAT no se incorporan porque no están autorizados por ningún `A-NNN` para
este texto.

## 4. Carta completa consolidada

Estimado equipo de selección:

Me gustaría poner mi experiencia en operaciones de supermercados a disposición
del puesto de Coordinador/a de línea de Cajas en el Almacén Jinámar. Mi
trayectoria combina atención al cliente, coordinación de equipos, seguimiento
de tareas y control de cajas, una base directamente relacionada con la
operación diaria de este puesto.

En Herfrailes atendía y resolvía reclamaciones cuando los responsables no
podían hacerlo y organicé equipos polivalentes para ajustar el apoyo entre
caja, reposición y secciones de frescos. También implanté Trello para asignar,
registrar y seguir tareas operativas, incluidas las de Cajas, lo que facilitaba
una ejecución ordenada y el seguimiento de incidencias.

Realicé cuadres de caja durante mi primer año en Herfrailes S. L. y diseñé
después un sistema en Excel que mejoró el proceso final de cuadre de todas las
cajas. A ello sumo experiencia en pedidos diarios, automatización de pedidos,
stock y redistribución entre tiendas. Tengo vehículo propio y disponibilidad
para trabajar en turnos rotativos de mañana o tarde.

Como cliente de OBRAMAT, conozco su entorno de compra. Mi experiencia puede
trasladarse a una operación orientada a la atención, la disponibilidad de
producto y el trabajo coordinado del equipo. Quedo a su disposición para
conversar sobre cómo podría contribuir al Almacén Jinámar.

Atentamente,

Gustavo Vega

## 5. Controles editoriales

| Control | Resultado | Observación |
| --- | --- | --- |
| Restricción no convertida en contenido visible | conforme | No se explican límites internos. |
| Formulación positiva | conforme | La experiencia se comunica directamente. |
| Voz del candidato | conforme | Primera persona y tono profesional. |
| Lenguaje metaanalítico | no detectado | No se habla del expediente ni del análisis. |
| Utilidad frase por frase | conforme | Cada bloque explica encaje, evidencia o continuidad. |
| Primer escaneo recruiter | conforme | Puesto y núcleo de encaje aparecen en las primeras líneas. |
| Anti-segundo-CV | conforme | Interpreta y conecta, no enumera cronología completa. |
| Anti-genericidad | conforme | Jinámar, línea de cajas, OBRAMAT y funciones concretas. |
| Anti-IA | conforme | Lenguaje directo, sin clichés ni elogios vacíos. |
| ATS / recruiter IA | conforme | Vocabulario respaldado y natural. |
| Factualidad | conforme | Afirmaciones dentro del conjunto CL-001–CL-007. |
| No expansión semántica | conforme | No se añaden hechos ni motivaciones. |

## 6. Motivación, cultura y privacidad

```yaml
motivacion_personal:
  declarada: no
  incluida: no
razon_profesional:
  incluida: sí
  base: experiencia_en_supermercados_atencion_caja_y_coordinacion
relacion_empresa:
  tipo: cliente
  uso: contexto_de_conocimiento_real
cultura:
  uso: contexto_de_servicio_y_disponibilidad
  afinidad_personal_atribuida: no
datos_privados_incorporados:
  nombre: no
  apellido_1: no
  email: no
  telefono: no
  linkedin: no
```

Los datos de contacto quedan reservados para la composición según su contrato
de privacidad; no se trasladan automáticamente al contenido semántico.

## 7. Control final y estado

```yaml
palabras_reales: 220
resultado: interpreta_y_conecta
podria_enviarse_a_otra_empresa_cambiando_solo_el_nombre: no
restricciones_internas_expuestas: no
lenguaje_defensivo_visible: no
voz_candidato: sí
lenguaje_metaanalitico: no
frases_prescindibles: no
segunda_lectura_recruiter: superada
correccion_factual_revisada_por_recruiter: sí
no_se_detectan_afirmaciones_profesionales_nuevas: sí
```

```yaml
estado_contenido: apto
recomendacion_gate: aprobar
decision_humana: aprobado
estado_gate: aprobado
```

La recomendación autoriza únicamente la futura composición de la carta tras
aprobación humana de `GATE-CONTENIDO-CARTA-COMPOSICION`. No autoriza todavía
DOCX/PDF, revisión humana, veredicto final, paquete ni presentación externa.
