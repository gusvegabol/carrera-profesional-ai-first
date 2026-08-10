---
id: TEMPLATE_CONTENIDO_CARTA_PRESENTACION
tipo: template
version: "1.1.0"
estado: en_prueba
playbook: PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION
artefacto_instancia: contenido-carta-presentacion.md
gate_entrada: GATE-GUION-CARTA-CONTENIDO
gate_salida: GATE-CONTENIDO-CARTA-COMPOSICION
---

# Contenido de carta de presentación

> Artefacto semántico final de la carta antes de composición.
>
> Contiene tanto el texto final como los controles necesarios para demostrar que fue generado conforme a `PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION`.
>
> **Los controles internos nunca deben filtrarse automáticamente a la carta visible.**

---

# 1. Identificación

| Campo | Valor |
| --- | --- |
| Candidatura | |
| Empresa objetivo | |
| Puesto objetivo | |
| Destinatario | |
| Idioma | |
| Fecha de generación | |
| Guion fuente | `guion-carta-presentacion.md` |
| Versión del guion | |
| Playbook | `PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION` |
| Versión del playbook | |
| Template | `TEMPLATE_CONTENIDO_CARTA_PRESENTACION` |
| Versión template | |
| Gate entrada | `GATE-GUION-CARTA-CONTENIDO` |
| Estado gate entrada | |

---

# 2. Estado

```yaml
estado_contenido:
  resultado:
    # apto
    # requiere_correccion
    # requiere_revision_origen
    # requiere_actualizacion_factual
    # bloqueado
  motivo_principal:
```

---

# 3. Fuentes

| Fuente | Disponible | Autoridad / uso |
| --- | --- | --- |
| `guion-carta-presentacion.md` | sí / no | autoridad editorial |
| `candidatura.md` | sí / no | estrategia |
| `analisis-oferta.md` | sí / no | contexto |
| `datos-core-busqueda.md` | sí / no | verificación factual |
| declaraciones usuario | sí / no / no_aplica | motivación/relación |
| fuentes culturales autorizadas | sí / no / no_aplica | contexto empresarial |

---

# 4. Precondiciones

- [ ] Existe guion.
- [ ] Guion `apto`.
- [ ] `GATE-GUION-CARTA-CONTENIDO` aprobado humanamente.
- [ ] Candidatura vigente.
- [ ] `presentada: false`.
- [ ] Destinatario resuelto.
- [ ] Idioma resuelto.
- [ ] Argumento central resuelto.
- [ ] Evidencias seleccionadas.
- [ ] Motivación clasificada.
- [ ] Cultura clasificada.
- [ ] Prohibiciones disponibles.

Si alguna precondición material falla:

```yaml
estado_contenido:
  resultado: bloqueado
```

o el estado de escalado correspondiente.

---

# 5. Brief heredado

No tomar decisiones nuevas en este bloque.

```yaml
brief_heredado:
  destinatario:
  idioma:
  objetivo_comunicativo:
  argumento_central:
  motivaciones_autorizadas: []
  cultura_utilizable: []
  evidencias_prioritarias: []
  carencias_a_tratar: []
  vocabulario_prioritario: []
  tono:
  longitud_objetivo:
  prohibiciones_clave: []
```

---

# 6. Ejecución de roles

## 6.1 Rol 1 — Redactor senior

```yaml
rol_redactor:
  ejecutado: true | false
  objetivo:
  decisiones_de_estilo_aplicadas: []
  incidencias_detectadas: []
```

Control:

- [ ] escribe para recruiter;
- [ ] usa voz de candidato;
- [ ] usa lenguaje concreto;
- [ ] evita burocracia;
- [ ] evita lenguaje defensivo;
- [ ] evita explicar controles internos;
- [ ] preserva el guion.

---

## 6.2 Rol 2 — Recruiter senior

```yaml
rol_recruiter:
  ejecutado: true | false
  primera_lectura:
  requiere_reescritura: true | false
  motivos: []
```

Debe leer el texto como destinatario real.

---

## 6.3 Rol 3 — Auditor factual

```yaml
rol_auditor:
  ejecutado: true | false
  factualidad: apta | no_apta
  trazabilidad: apta | no_apta
  incidencias: []
```

---

## 6.4 Segunda lectura recruiter

```yaml
segunda_lectura_recruiter:
  ejecutada: true | false
  resultado: apta | requiere_correccion
  motivo:
```

Obligatoria después del auditor.

---

# 7. Trazabilidad por bloques

| Bloque | Función | Refs. guion |
| --- | --- | --- |
| B-01 | | |
| B-02 | | |
| B-03 | | |
| B-04 | | |
| B-05 | | |
| B-06 | | |

---

# 8. Saludo

## Texto

...

## Trazabilidad

```yaml
bloque:
funcion: saludo
refs_guion: []
```

Control:

- [ ] destinatario correcto;
- [ ] no inventa nombre;
- [ ] no inventa género;
- [ ] tratamiento profesional.

---

# 9. Apertura

## Texto

...

## Trazabilidad

```yaml
bloque:
funcion:
refs_guion:
  - A-...
```

Control:

- [ ] identifica oportunidad;
- [ ] posicionamiento reconocible;
- [ ] entra rápido en materia;
- [ ] voz de candidato;
- [ ] sin lenguaje metaanalítico;
- [ ] sin entusiasmo inventado;
- [ ] aporta valor en primer escaneo.

---

# 10. Desarrollo argumental

## Texto

...

## Trazabilidad

```yaml
bloque:
funcion:
refs_guion:
  - A-...
```

Control:

- [ ] evidencia autorizada;
- [ ] explica relevancia;
- [ ] no es inventario de experiencia;
- [ ] no amplía alcance;
- [ ] no contiene controles internos visibles;
- [ ] utiliza lenguaje concreto.

---

# 11. Desarrollo complementario

## Texto

...

## Trazabilidad

```yaml
bloque:
funcion:
refs_guion:
  - A-...
```

Control:

- [ ] complementa la tesis;
- [ ] no crea otra tesis;
- [ ] no convierte carta en CV;
- [ ] cada oración aporta utilidad recruiter.

---

# 12. Cultura

Completar solo si procede.

## Texto incorporado

...

## Fuente

...

## Refs. guion

```yaml
refs_guion:
  - A-...
```

Control:

- [ ] autorizada;
- [ ] usada como contexto;
- [ ] no convertida en atributo;
- [ ] no convertida en afinidad;
- [ ] no parece copia corporativa.

---

# 13. Motivación

```yaml
motivacion:
  declarada_usuario: true | false
  existe_motivacion_personal: true | false
  incluida_en_carta: true | false
  refs_guion: []
```

## Texto, si procede

...

Control:

- [ ] motivación personal acreditada;
- [ ] razón profesional no convertida en emoción;
- [ ] funciona aunque no exista motivación emocional;
- [ ] no hay pasión/admiración inventada.

---

# 14. Carencias y límites

Este bloque es **interno**.

| Límite | Tratamiento del guion | Aplicado internamente | Visible en carta | Correcto |
| --- | --- | --- | --- | --- |
| | | sí / no | sí / no | |

Regla:

> Un límite no debe ser visible por defecto.

Si es visible, justificar su valor comunicativo:

...

---

# 15. Control crítico — Restricción ≠ contenido

Para cada restricción relevante:

| Restricción interna | Qué impide afirmar | Formulación positiva utilizada |
| --- | --- | --- |
| | | |

Pregunta:

> ¿Alguna restricción se ha convertido innecesariamente en frase defensiva?

`si | no`

Si `sí`:

```text
→ requiere_correccion
```

---

# 16. Control de negaciones defensivas

Revisar en la carta consolidada apariciones de patrones como:

```text
sin...
no...
se limita a...
aunque no...
sin presentar...
sin convertir...
sin atribuir...
```

| Fragmento | Aporta valor recruiter | Es control interno visible | Acción |
| --- | --- | --- | --- |
| | sí / no | sí / no | mantener / reformular / eliminar |

No se prohíben las negaciones legítimas.

---

# 17. Control de voz del candidato

Pregunta obligatoria:

> ¿Podría el candidato decir naturalmente cada frase en una conversación profesional?

Resultado:

`si | no`

Fragmentos problemáticos:

| Fragmento | Voz detectada | Reformulación necesaria |
| --- | --- | --- |
| | candidato / auditor / sistema / analista / burocrática | |

Si existe voz de auditor/sistema/analista material:

```text
→ requiere_correccion
```

---

# 18. Control de lenguaje metaanalítico

Buscar formulaciones equivalentes a:

```text
la oferta describe...
el contexto de la oferta...
según el análisis...
la evidencia demuestra...
está confirmado...
el candidato...
la candidatura...
se ha identificado...
```

| Fragmento | Necesario para recruiter | Revela análisis interno | Acción |
| --- | --- | --- | --- |
| | sí / no | sí / no | |

Resultado:

```yaml
lenguaje_metaanalitico:
  detectado: true | false
  material: true | false
```

Si es material:

```text
→ requiere_correccion
```

---

# 19. Utilidad frase por frase

Clasificar conceptualmente cada oración significativa con una función:

```text
entiende_encaje
obtiene_evidencia
entiende_valor
entiende_motivacion_real
obtiene_contexto_relevante
entiende_disponibilidad
facilita_continuidad
```

| Fragmento / oración | Función |
| --- | --- |
| | |

Si una frase solo cumple:

```text
demuestra_que_el_sistema_no_ha_inventado
```

debe eliminarse o reformularse.

---

# 20. Control de primer escaneo

Responder sin consultar otros documentos:

### ¿Qué puesto solicita?

...

### ¿Cuál es su encaje principal?

...

### ¿Qué evidencia inicial justifica seguir leyendo?

...

Si estas respuestas no son claras tras apertura/primer bloque:

```text
→ requiere_correccion
```

---

# 21. Control de segundo CV

Pregunta:

> ¿La carta interpreta y conecta evidencia o reproduce el CV?

```text
interpreta_y_conecta
|
repite_cv
```

Si:

```text
repite_cv
```

entonces:

```text
→ requiere_correccion
```

---

# 22. Control de genericidad

Pregunta:

> ¿Podría enviarse prácticamente la misma carta a otra empresa cambiando nombre y puesto?

`si | no`

Si `sí`:

```text
→ requiere_correccion
```

Justificación:

...

---

# 23. Control anti-IA

Evaluar individualmente:

| Riesgo | Detectado |
| --- | --- |
| abstracción innecesaria | sí / no |
| conectores mecánicos | sí / no |
| estructuras repetitivas | sí / no |
| párrafos simétricos | sí / no |
| lenguaje corporativo genérico | sí / no |
| elogios vacíos | sí / no |
| clichés | sí / no |
| exceso de adjetivos | sí / no |
| copia/reformulación de la oferta | sí / no |
| texto excesivamente pulido | sí / no |
| explicaciones impropias de una carta | sí / no |
| apertura intercambiable | sí / no |
| cierre intercambiable | sí / no |

Resultado:

```yaml
anti_ia:
  superado: true | false
  observaciones:
```

Un indicador aislado no bloquea necesariamente.

Un patrón material sí requiere corrección.

---

# 24. ATS / recruiter IA

| Término | Fuente | Ref. guion | Uso natural |
| --- | --- | --- | --- |
| | | | sí / no |

Control:

- [ ] puesto reconocible;
- [ ] necesidades reconocibles;
- [ ] vocabulario respaldado;
- [ ] sin keyword stuffing;
- [ ] lectura humana prioritaria.

---

# 25. Control factual

- [ ] cargos;
- [ ] fechas;
- [ ] responsabilidades;
- [ ] métricas;
- [ ] herramientas;
- [ ] resultados;
- [ ] atribuciones;
- [ ] seniority;
- [ ] formación;
- [ ] transferibilidad;
- [ ] cultura;
- [ ] motivación.

Incidencias:

...

---

# 26. No expansión semántica

Para cada afirmación profesional relevante:

| Afirmación | Ref. guion | Trazable | Amplía significado |
| --- | --- | --- | --- |
| | | sí / no | sí / no |

Si no es trazable:

```text
→ requiere_correccion
```

Si incorpora evidencia nueva:

```text
→ requiere_actualizacion_factual
```

---

# 27. Longitud

```yaml
longitud:
  objetivo_guion:
  palabras_reales:
  dentro_rango: true | false
```

No rellenar para alcanzar límite superior.

---

# 28. Tono

```yaml
tono:
  esperado:
  observado:
  conforme: true | false
```

Evaluar:

- profesionalidad;
- naturalidad;
- seguridad;
- cercanía;
- sobriedad;
- ausencia de arrogancia;
- ausencia de servilismo;
- ausencia de entusiasmo artificial.

---

# 29. Privacidad

| Dato | Autorizado | Incluido | Conforme |
| --- | --- | --- | --- |
| nombre | | | |
| apellidos | | | |
| email | | | |
| teléfono | | | |
| LinkedIn | | | |
| ubicación | | | |
| otros | | | |

---

# 30. Carta completa consolidada

> Esta es la única sección que la futura capa de composición debe utilizar como contenido visible principal.
>
> Ningún control interno de las secciones anteriores debe aparecer aquí salvo que forme parte legítima de la comunicación al recruiter.

---

[FORMULA DE DIRECCIÓN / SALUDO]

[APERTURA]

[DESARROLLO ARGUMENTAL]

[DESARROLLO COMPLEMENTARIO]

[CULTURA / MOTIVACIÓN SOLO SI PROCEDE]

[CIERRE]

[DESPEDIDA]

[FIRMA SEMÁNTICA]

---

# 31. Lectura recruiter final

Después de consolidar la carta, responder:

### R1 — ¿Entiendo rápidamente el encaje?

`si | no`

### R2 — ¿Seguiría leyendo después del primer párrafo?

`si | no`

### R3 — ¿La carta aporta algo distinto al CV?

`si | no`

### R4 — ¿Las evidencias ayudan a valorar al candidato?

`si | no`

### R5 — ¿Suena como una persona profesional?

`si | no`

### R6 — ¿Percibo lenguaje de sistema, auditor o expediente?

`si | no`

### R7 — ¿Percibo entusiasmo fabricado?

`si | no`

### R8 — ¿La personalización es suficiente?

`si | no`

### R9 — ¿Hay frases prescindibles?

`si | no`

### R10 — ¿La enviaría sin reescritura semántica?

`si | no`

Para `apto`:

```text
R1 sí
R2 sí
R3 sí
R4 sí
R5 sí
R6 no
R7 no
R8 sí
R9 no
R10 sí
```

---

# 32. Auditoría factual final

Después de la lectura recruiter:

```yaml
auditoria_final:
  factualidad: apta | no_apta
  trazabilidad: apta | no_apta
  motivacion: conforme | no_conforme
  cultura: conforme | no_conforme
  privacidad: conforme | no_conforme
```

---

# 33. Control de regresión tras auditoría

Pregunta:

> ¿Alguna corrección factual ha convertido la carta en lenguaje defensivo, administrativo o metaanalítico?

`si | no`

Si `sí`:

```text
→ regresar a redacción
```

sin ampliar el significado autorizado.

---

# 34. Incidencias

| ID | Tipo | Descripción | Severidad | Acción |
| --- | --- | --- | --- | --- |
| INC-CONT-CARTA-001 | | | | |

Tipos:

```text
editorial
factual
trazabilidad
origen
privacidad
arquitectura
```

---

# 35. Nueva información

## Nueva evidencia

| Dato | Fuente | Impacto | Acción |
| --- | --- | --- | --- |
| | | | devolver al flujo factual |

No incorporar localmente.

## Nueva decisión necesaria

| Decisión | Motivo | Acción |
| --- | --- | --- |
| | | `requiere_revision_origen` |

---

# 36. Resultado

```yaml
resultado_contenido:
  estado:
    # apto
    # requiere_correccion
    # requiere_revision_origen
    # requiere_actualizacion_factual
    # bloqueado
  motivo_principal:
```

Precedencia:

```text
bloqueado
>
requiere_actualizacion_factual
>
requiere_revision_origen
>
requiere_correccion
>
apto
```

---

# 37. Checklist bloqueante de `apto`

## Contrato

- [ ] gate de entrada aprobado;
- [ ] guion apto;
- [ ] candidatura vigente;
- [ ] no presentada.

## Fidelidad

- [ ] argumento preservado;
- [ ] evidencias autorizadas;
- [ ] ninguna evidencia nueva;
- [ ] motivación conforme;
- [ ] cultura conforme;
- [ ] carencias conforme.

## Redacción

- [ ] voz de candidato;
- [ ] restricciones no convertidas en contenido;
- [ ] afirmaciones positivas cuando corresponden;
- [ ] sin lenguaje defensivo material;
- [ ] sin lenguaje metaanalítico material;
- [ ] utilidad frase por frase;
- [ ] primer escaneo superado;
- [ ] no segundo CV;
- [ ] no genérica;
- [ ] anti-IA superado;
- [ ] tono conforme;
- [ ] longitud conforme.

## Integridad

- [ ] factualidad;
- [ ] trazabilidad;
- [ ] privacidad;
- [ ] ATS/IA natural.

## Frontera

- [ ] no contiene decisiones visuales;
- [ ] no requiere reescritura por compositor;
- [ ] no se generó DOCX/PDF.

Una casilla bloqueante no superada impide `apto`.

---

# 38. Recomendación del gate

```yaml
gate_salida:
  id: GATE-CONTENIDO-CARTA-COMPOSICION
  recomendacion:
    # aprobar
    # no_aprobar
  motivo:
  decision_humana: pendiente
```

Regla:

```text
estado_contenido: apto
→ recomendar aprobar

cualquier otro estado
→ recomendar no_aprobar
```

La IA nunca sustituye la decisión humana.

---

# 39. Postcondición

Si el contenido es `apto`, la siguiente fase únicamente puede:

```text
tomar contenido semántico final
+
aplicar presentación visual
+
generar formatos
```

No puede:

```text
reescribir
resumir
ampliar
añadir
eliminar
cambiar tono
cambiar argumento
alterar evidencia
```

---

# 40. Principio final

> **La carta visible debe parecer una buena comunicación profesional, no la salida de un sistema de control.**

La rigurosidad debe poder auditarse en este documento.

El recruiter, en cambio, solo debe percibir:

- claridad;
- relevancia;
- evidencia;
- naturalidad;
- profesionalidad.

---

# 41. Registro de pruebas T13–T18

| Prueba | Entrada o regresión | Resultado | Acción requerida |
| --- | --- | --- | --- |
| T13 — Restricción convertida en contenido | frase defensiva derivada de un límite interno | superada / fallida | reformular positivamente |
| T14 — Voz de auditor | voz de sistema, auditor o expediente | superada / fallida | volver a voz del candidato |
| T15 — Lenguaje metaanalítico | descripción del análisis o del contexto interno | superada / fallida | hablar directamente al recruiter |
| T16 — Precaución interna visible | cautela sin utilidad comunicativa | superada / fallida | eliminar del texto visible |
| T17 — Anti-IA | cliché, simetría o abstracción material | superada / fallida | reescribir con lenguaje concreto |
| T18 — Regresión tras auditoría factual | corrección que reintroduce lenguaje defensivo | superada / fallida | ejecutar segunda lectura recruiter |

```yaml
pruebas_v1_1:
  rol_redactor_registrado: true | false
  primera_lectura_recruiter_registrada: true | false
  auditoria_factual_registrada: true | false
  segunda_lectura_recruiter_registrada: true | false
  t13_t18_resultado: superado | requiere_correccion
```
