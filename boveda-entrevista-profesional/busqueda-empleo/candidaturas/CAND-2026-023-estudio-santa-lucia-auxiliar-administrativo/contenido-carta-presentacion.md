---
id: contenido-carta-presentacion-CAND-2026-023
tipo: contenido_carta_presentacion
version_playbook: "1.1.0"
version_guion: "1.0.0"
version_instancia: "1.0.0"
candidatura: CAND-2026-023
empresa: ESTUDIO SANTA LUCIA DE TIRAJANA, S. L. / Tecnocasa Gáldar
puesto: Auxiliar administrativo/a SIN EXPERIENCIA
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

# Contenido de carta de presentación — CAND-2026-023

> Artefacto semántico final antes de la composición. Redactado desde el guion
> aprobado; no contiene decisiones visuales ni autoriza composición o envío.

## 1. Identificación y fuentes

| Campo | Valor |
| --- | --- |
| Candidatura | `CAND-2026-023` |
| Empresa objetivo | ESTUDIO SANTA LUCIA DE TIRAJANA, S. L.; oficina de Tecnocasa en Gáldar |
| Puesto | Auxiliar administrativo/a SIN EXPERIENCIA |
| Destinatario | Equipo de selección de ESTUDIO SANTA LUCIA DE TIRAJANA, S. L. / Tecnocasa Gáldar |
| Idioma | `es` |
| Guion fuente | `guion-carta-presentacion.md` |
| Playbook | `PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION` v1.1.0 |
| Gate de entrada | `GATE-GUION-CARTA-CONTENIDO` aprobado el 2026-08-11 |

Fuentes consultadas: guion, candidatura, análisis de oferta, oferta fuente,
datos core y declaraciones humanas registradas. No se consultó una fuente
cultural externa y no se utilizaron artefactos de composición para decidir el
contenido.

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
| CL-001 | A-001 | candidatura, HER-01, HER-02 | Experiencia administrativa y documental aplicable al puesto. |
| CL-002 | A-002 | HER-01, HER-02 | Organización y seguimiento de documentación y procesos. |
| CL-003 | A-003 | HER-01 | Informes y hojas de cálculo avanzadas en Excel; mejora del tiempo de preparación de 20 a 3 minutos. |
| CL-004 | A-004 | HER-06 | Atención y resolución de reclamaciones con comunicación profesional. |
| CL-005 | A-005 | COMP-01 | Experiencia histórica con sistemas de gestión comercial y contabilidad como apoyo a equipos. |
| CL-006 | A-006 | candidatura, oferta | Traslado de capacidades a tareas administrativas presenciales y disposición a aprender el sector. |
| CL-007 | A-007 | — | Cierre profesional abierto a conversación. |

Toda afirmación profesional visible pertenece a este conjunto. No se incorporan
experiencia inmobiliaria, publicación de anuncios, gestión de agendas
inmobiliarias ni software de fincas.

## 4. Carta completa consolidada

Estimado equipo de selección:

Presento mi candidatura al puesto de Auxiliar administrativo/a para su oficina
de Tecnocasa en Gáldar. Mi experiencia en administración, gestión documental,
organización y Excel puede trasladarse a las tareas de apoyo y seguimiento que
requiere el puesto. Estoy acostumbrado a trabajar con información sensible y
tareas que exigen orden, precisión y continuidad.

En Herfrailes S. L. organicé procesos documentales y sistemas de seguimiento,
trabajando con información que debía mantenerse ordenada y validada. También
elaboré informes económicos y hojas de cálculo avanzadas en Excel; una de estas
mejoras redujo el tiempo de preparación de 20 a 3 minutos. Esta forma de
trabajar puede aportar rigor y continuidad a la gestión diaria de documentos y
al seguimiento de tareas de la oficina.

Además, atendí y resolví reclamaciones de clientes cuando los responsables de
tienda no podían hacerlo, y cuento con experiencia previa en sistemas de
gestión comercial y contabilidad. Son capacidades que pueden resultar útiles
para apoyar al equipo y mantener una comunicación ordenada con clientes y
compañeros.

Quedo a su disposición para explicar en una entrevista cómo puedo trasladar
esta experiencia a las tareas administrativas del puesto.

Atentamente,

Gustavo Vega

## 5. Controles editoriales

| Control | Resultado | Observación |
| --- | --- | --- |
| Restricción no convertida en contenido visible | conforme | No se explican límites internos. |
| Formulación positiva | conforme | La experiencia se comunica directamente. |
| Voz del candidato | conforme | Primera persona y tono profesional. |
| Lenguaje metaanalítico | no detectado | No se habla del análisis ni del expediente. |
| Utilidad frase por frase | conforme | Cada párrafo explica encaje, evidencia o continuidad. |
| Primer escaneo recruiter | conforme | Puesto y núcleo administrativo aparecen en las primeras líneas. |
| Anti-segundo-CV | conforme | Interpreta y conecta evidencias sin repetir cronología completa. |
| Anti-genericidad | conforme | Gáldar, oficina, funciones documentales y apoyo al equipo concretan el texto. |
| Anti-IA | conforme | Lenguaje directo, sin clichés ni elogios vacíos. |
| ATS / recruiter IA | conforme | Vocabulario administrativo respaldado y natural. |
| Factualidad | conforme | Afirmaciones dentro del conjunto CL-001–CL-007. |
| No expansión semántica | conforme | No se añaden hechos ni motivaciones. |

## 6. Motivación, relación con empresa y privacidad

```yaml
motivacion_personal:
  declarada: no
  incluida: no
razon_profesional:
  incluida: sí
  base: experiencia_administrativa_documental_organizacion_excel
relacion_empresa:
  tipo: ninguna
  uso: no_se_usa
cultura:
  uso: no_disponible
  afinidad_personal_atribuida: no
datos_privados_incorporados:
  nombre: no
  apellido_1: no
  email: no
  telefono: no
  linkedin: no
  fotografia: no
```

Los datos de contacto quedan reservados para la composición según su contrato
de privacidad; no se trasladan automáticamente al contenido semántico.

## 7. Control final y estado

```yaml
palabras_reales: 189
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

La aprobación humana autoriza únicamente la composición de la carta. No
autoriza todavía revisión humana, veredicto final, paquete ni presentación
externa.
