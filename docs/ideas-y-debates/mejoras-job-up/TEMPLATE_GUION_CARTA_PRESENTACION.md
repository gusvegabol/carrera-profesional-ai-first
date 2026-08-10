---
id: TEMPLATE_GUION_CARTA_PRESENTACION
tipo: template
version: "1.0.0"
estado: probado
playbook: PLAYBOOK_GUION_CARTA_PRESENTACION
artefacto_instancia: guion-carta-presentacion.md
gate_entrada: GATE-CANDIDATURA-GUION
gate_salida: GATE-GUION-CARTA-CONTENIDO
---

# Guion de carta de presentación

> Mapa argumental y comunicativo de la carta.
>
> Este documento **no contiene la carta final**.
>
> No modifica la estrategia de candidatura, no inventa hechos ni motivaciones y no realiza composición o presentación externa.

---

# 1. Identificación

| Campo | Valor |
| --- | --- |
| Candidatura | |
| Empresa objetivo | |
| Puesto objetivo | |
| Plataforma publicadora | |
| Intermediario / recruiter | |
| Destinatario real | |
| Tipo de destinatario | `empresa_identificada` / `intermediario_con_empresa_identificada` / `intermediario_con_empresa_anonima` |
| Idioma de la carta | |
| Fecha de generación | |
| Playbook | `PLAYBOOK_GUION_CARTA_PRESENTACION` |
| Versión del playbook | |
| Gate de entrada | `GATE-CANDIDATURA-GUION` |
| Estado gate entrada | |

---

# 2. Fuentes consultadas

Registrar únicamente las fuentes realmente utilizadas.

| Fuente | Tipo | Disponible | Fecha lectura | Autoridad | Referencia / URL |
| --- | --- | --- | --- | --- | --- |
| `candidatura.md` | estrategia | sí / no | | estrategia común | |
| `analisis-oferta.md` | análisis | sí / no | | necesidades y señales | |
| oferta fuente | oferta | sí / no | | texto y contexto de la oportunidad | |
| `datos-core-busqueda.md` | factual | sí / no | | hechos profesionales | |
| declaraciones usuario | humana | sí / no | | motivación y relación personal | |
| URL oficial empresa | cultura | sí / no / no_aplica | | cultura y propuesta de empleador | |

---

# 3. Clasificación del destinatario

```yaml
destinatario:
  plataforma_publicadora:
  intermediario:
  empresa_objetivo:
  tipo:
    # empresa_identificada
    # intermediario_con_empresa_identificada
    # intermediario_con_empresa_anonima
  destinatario_real:
  forma_de_direccion:
  anonimato_empresa: true | false
```

## 3.1 Decisión

**A quién debe hablar realmente la carta:**

...

**Justificación:**

...

## 3.2 Restricciones derivadas

- ...
- ...

---

# 4. Contexto de la oferta para la carta

## 4.1 Necesidades funcionales

| Ref. | Necesidad | Relevancia para la carta | Fuente |
| --- | --- | --- | --- |
| N-001 | | alta / media / baja | |

## 4.2 Requisitos

| Ref. | Requisito | Estado candidato | Tratamiento |
| --- | --- | --- | --- |
| R-001 | | acreditado / parcial / no_acreditado | |

## 4.3 Atributos personales buscados

| Ref. | Atributo expresado en la oferta | Naturaleza | Puede atribuirse al candidato | Evidencia |
| --- | --- | --- | --- | --- |
| AP-001 | | atributo_buscado | sí / no | |

> Un atributo buscado por la empresa no se convierte automáticamente en atributo del candidato.

---

# 5. Cultura y propuesta de empleador

## 5.1 Cultura detectada en la propia oferta

| Ref. | Señal cultural | Texto / significado resumido | Fuente | Utilizable |
| --- | --- | --- | --- | --- |
| CULT-001 | | | oferta | sí / no / condicionado |

## 5.2 Propuesta de empleador detectada en la oferta

| Ref. | Elemento | Fuente | Relevancia |
| --- | --- | --- | --- |
| EVP-001 | | oferta | |

---

# 6. Fuente cultural externa

## 6.1 Estado

```yaml
fuente_cultural_externa:
  empresa_identificada: true | false
  url_aportada_al_inicio: true | false
  url_solicitada_posteriormente: true | false
  url_aportada:
  url:
  tipo_fuente:
    # oficial_empleo
    # oficial_corporativa
    # otra
  validada_como_empresa_objetivo: true | false | no_aplica
```

## 6.2 Regla aplicada

- [ ] La URL ya existía y no volvió a solicitarse.
- [ ] La URL no existía y se ofreció al usuario aportarla.
- [ ] El usuario no disponía de URL y el proceso continuó.
- [ ] La empresa es anónima y no se solicitó URL.
- [ ] La fuente pertenece realmente a la empresa objetivo.

## 6.3 Señales extraídas

| Ref. | Señal | Fuente | Utilidad para la carta | Límite |
| --- | --- | --- | --- | --- |
| CULT-EXT-001 | | | | |

---

# 7. Matriz cultural consolidada

Mantener la procedencia de cada señal.

| Ref. | Señal | Oferta | Web oficial | Prioridad contextual | Uso previsto |
| --- | --- | --- | --- | --- | --- |
| CULT-001 | | sí / no | sí / no | alta / media / baja | |

No fusionar señales de fuentes distintas de manera que se pierda su procedencia.

---

# 8. Información humana verificada

## 8.1 Interés real por el puesto

```yaml
interes_puesto:
  declarado: true | false
  texto_literal_o_resumen_fiel:
  fecha:
```

**Uso permitido:**

...

**Uso prohibido:**

...

---

## 8.2 Relación o conocimiento previo de la empresa

```yaml
conocimiento_empresa:
  aplica: true | false
  declarado: true | false
  tipo:
    # cliente
    # antiguo_empleado
    # proveedor
    # proceso_anterior
    # contacto_profesional
    # seguimiento_real
    # conocimiento_productos_servicios
    # ninguno
    # otro
  descripcion:
```

**Uso permitido:**

...

**Uso prohibido:**

...

---

## 8.3 Preferencias profesionales

| Ref. | Preferencia declarada | Puede utilizarse | Cómo |
| --- | --- | --- | --- |
| MOT-001 | | sí / no | |

---

# 9. Clasificación de motivaciones

## 9.1 Motivación personal declarada

| Ref. | Declaración | Fuente | Uso |
| --- | --- | --- | --- |
| MOT-001 | | usuario | |

## 9.2 Razones profesionales factuales

| Ref. | Razón profesional | Evidencia | Uso |
| --- | --- | --- | --- |
| RP-001 | | | |

## 9.3 Afirmaciones no acreditadas

| Afirmación potencial | Estado | Tratamiento |
| --- | --- | --- |
| «Me apasiona...» | prohibida / acreditada | |
| «Siempre he querido...» | prohibida / acreditada | |
| «Admiro su empresa...» | prohibida / acreditada | |
| «Comparto sus valores...» | prohibida / acreditada | |
| «Sigo su empresa desde hace años...» | prohibida / acreditada | |

Añadir otras específicas del caso:

- ...
- ...

---

# 10. Matriz de afirmaciones permitidas

| Ref. | Idea / afirmación | Tipo | Fuente | Permitida | Límite |
| --- | --- | --- | --- | --- | --- |
| AF-001 | | `hecho_profesional` / `motivacion_declarada` / `razon_profesional` / `contexto_empresa` / `contexto_oferta` / `no_acreditada` | | sí / no / condicionado | |

Toda afirmación `no_acreditada` debe quedar:

```text
prohibida
```

---

# 11. Objetivo comunicativo

Completar una sola frase operativa:

> **La carta debe conseguir que el recruiter entienda que...**

...

Debe expresar el efecto buscado, no la redacción final.

---

# 12. Tesis de la carta

## 12.1 Argumento central

```text
necesidad de la oportunidad
+
evidencia del candidato
+
valor aportable
```

**Formulación conceptual:**

...

## 12.2 Qué NO debe convertirse en argumento central

- ...
- ...

---

# 13. Gancho inicial

## Objetivo

...

## Idea que debe transmitir

...

## Evidencia o contexto que lo respalda

...

## Evitar

- «Me pongo en contacto...»
- «Por medio de la presente...»
- ...
- ...

No redactar todavía la frase final.

---

# 14. Mapa argumental

Cada unidad utiliza una referencia `A-NNN`.

| Ref. | Función argumental | Idea | Tipo de afirmación | Fuente | Evidencia | Necesidad objetivo | Presencia | Obligatoriedad | Orden | Nivel detalle | Relación con CV | Personalización | Límites | Prohibiciones |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A-001 | | | | | | | incluir / omitir | obligatoria / opcional | | breve / normal | | | | |

---

# 15. Funciones argumentales utilizadas

Marcar las aplicables:

- [ ] `captar_atencion`
- [ ] `explicar_encaje`
- [ ] `demostrar_valor`
- [ ] `humanizar`
- [ ] `diferenciar`
- [ ] `conectar_empresa`
- [ ] `contextualizar`
- [ ] `mitigar_riesgo`
- [ ] `reforzar_keyword`
- [ ] `invitar_conversacion`

---

# 16. Evidencias narrables

Seleccionar solo las que aportan valor a la argumentación.

| Evidencia | Referencia factual | Qué demuestra | Necesidad con la que conecta | Uso narrativo | Límite |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

---

# 17. Relación con el CV

## 17.1 Qué debe interpretar del CV

- ...
- ...

## 17.2 Qué debe contextualizar

- ...
- ...

## 17.3 Qué NO debe repetir

- ...
- ...

## 17.4 Control de segundo CV

- [ ] No reproduce cronología.
- [ ] No copia bullets.
- [ ] No enumera todas las herramientas.
- [ ] No repite todas las responsabilidades.
- [ ] Cada evidencia utilizada tiene función argumental.

---

# 18. Personalización

## 18.1 Nivel disponible

```yaml
personalizacion:
  puesto: true | false
  oferta: true | false
  empresa: true | false
  cultura: true | false
  motivacion_usuario: true | false
```

## 18.2 Elementos concretos de personalización

| Nivel | Elemento | Fuente | Uso |
| --- | --- | --- | --- |
| puesto | | | |
| oferta | | | |
| empresa | | | |
| cultura | | | |
| motivación | | | |

---

# 19. Control de empresa anónima

Completar solo si aplica.

```yaml
empresa_anonima:
  aplica: true | false
  intermediario:
  personalizacion_permitida:
    - puesto
    - funciones
    - necesidades
    - sector
  cultura_intermediario_utilizada_como_empresa_final: false
```

## Tratamiento

...

---

# 20. Tratamiento de carencias

| Carencia | Relevancia | Decisión | Motivo | Redacción permitida | Redacción prohibida |
| --- | --- | --- | --- | --- | --- |
| | alta / media / baja | `no_mencionar` / `contextualizar` / `reconocer_brevemente` / `bloqueante_para_carta` | | | |

Regla:

> La carta no utiliza entusiasmo para sustituir evidencia ausente.

---

# 21. Cobertura semántica ATS / IA

## 21.1 Vocabulario utilizable

| Término | Fuente | Evidencia / contexto | Uso previsto |
| --- | --- | --- | --- |
| | oferta | | |

## 21.2 Uso condicionado

| Término | Condición | Uso permitido | Prohibición |
| --- | --- | --- | --- |
| | | | |

## 21.3 Prohibido como atributo del candidato

| Término | Motivo |
| --- | --- |
| | |

---

# 22. Control ATS / recruiter IA

- [ ] El puesto objetivo será reconocible.
- [ ] Aparecerán las necesidades principales cuando sean relevantes.
- [ ] El vocabulario profesional estará conectado a evidencia.
- [ ] No existen keywords atribuidas al candidato sin respaldo.
- [ ] No existe keyword stuffing.
- [ ] La semántica del encaje es explícita.
- [ ] La optimización no perjudica la naturalidad.

---

# 23. Arquitectura narrativa

| Orden | Bloque | Función | Contenido conceptual | Extensión |
| --- | --- | --- | --- | --- |
| 1 | apertura | | | |
| 2 | desarrollo | | | |
| 3 | desarrollo | | | |
| 4 | cierre | | | |

La tabla puede tener más o menos filas.

No es obligatorio utilizar cinco párrafos.

---

# 24. Apertura

**Función:**

...

**Idea principal:**

...

**Elementos que debe incluir:**

- ...
- ...

**Elementos que debe evitar:**

- ...
- ...

---

# 25. Desarrollo argumental

## Bloque principal

**Necesidad:**

...

**Evidencia:**

...

**Valor aportable:**

...

## Bloque complementario

...

---

# 26. Conexión con empresa / cultura

## ¿Debe existir?

`si | no | no_aplica`

## Señal utilizada

...

## Fuente

...

## Conexión factual o personal que permite utilizarla

...

## Límite

...

No escribir automáticamente:

```text
"Comparto sus valores"
```

---

# 27. Motivación

## ¿Debe aparecer motivación personal explícita?

`si | no`

## Motivación autorizada

...

## Fuente

`declaracion_usuario | no_aplica`

## Razones profesionales que pueden complementar

...

## Afirmaciones emocionales prohibidas

- ...
- ...

---

# 28. Cierre

## Objetivo

- reafirmar interés legítimo;
- dejar abierta conversación;
- evitar presión;
- evitar fórmulas grandilocuentes.

## Idea conceptual

...

## Elementos que debe evitar

- ...
- ...

---

# 29. Tono

```yaml
tono:
  descriptor_principal:
  formalidad:
  cercania:
  nivel_tecnico:
  directividad:
```

## Descriptores

- ...
- ...

## Evitar

- excesivamente corporativo;
- solemne;
- adulador;
- artificialmente entusiasta;
- burocrático;
- genérico;
- lenguaje claramente generado por IA.

---

# 30. Idioma

```yaml
idioma_carta:
  valor:
  autoridad:
  justificacion:
```

Si existe ambigüedad:

```text
requiere_revision_origen
```

---

# 31. Longitud

```yaml
longitud:
  objetivo_palabras:
  rango_admisible:
  parrafos_aproximados:
  densidad:
```

La extensión no se aumenta para rellenar página.

---

# 32. Prohibiciones específicas

Además de las restricciones heredadas:

- [ ] No inventar experiencia.
- [ ] No inventar tecnologías.
- [ ] No inventar métricas.
- [ ] No inventar motivación.
- [ ] No inventar relación con la empresa.
- [ ] No inventar cultura.
- [ ] No convertir cultura en atributo personal.
- [ ] No convertir formación en experiencia.
- [ ] No convertir transferibilidad en experiencia literal.
- [ ] No ocultar carencias mediante ambigüedad.
- [ ] No repetir el CV.
- [ ] No utilizar keyword stuffing.
- [ ] No elogiar genéricamente a la empresa.
- [ ] No tratar una empresa anónima como identificada.

Prohibiciones adicionales del caso:

- ...
- ...

---

# 33. Control recruiter humano

Responder:

### 33.1 ¿La carta tendrá una razón clara para existir?

...

### 33.2 ¿El recruiter entenderá rápidamente por qué considerar la candidatura?

...

### 33.3 ¿Aporta algo distinto del CV?

...

### 33.4 ¿La motivación proyectada resulta creíble?

...

### 33.5 ¿La personalización es real?

...

### 33.6 ¿La longitud prevista favorece lectura?

...

---

# 34. Control de genericidad

Pregunta:

> ¿Podría usarse prácticamente el mismo guion para otra empresa cambiando solo el nombre?

```text
sí | no
```

Si `sí`:

```text
requiere_correccion
```

**Justificación:**

...

---

# 35. Control factual

- [ ] Cada hecho profesional tiene respaldo.
- [ ] Cada métrica tiene respaldo.
- [ ] Cada tecnología tiene respaldo.
- [ ] Cada motivación personal procede del usuario.
- [ ] Cada referencia cultural tiene fuente.
- [ ] La identidad de empresa está correctamente tratada.
- [ ] Los límites de seniority se mantienen.
- [ ] Las carencias no se maquillan.

---

# 36. Incidencias

| ID | Tipo | Descripción | Capa propietaria | Severidad | Acción |
| --- | --- | --- | --- | --- | --- |
| INC-CARTA-001 | | | | | |

Tipos posibles:

```text
editorial
interaccion_usuario
origen
factual
fuente
arquitectura
```

---

# 37. Nueva información detectada

## 37.1 Nueva evidencia profesional

| Dato | Fuente | Impacto | Acción |
| --- | --- | --- | --- |
| | | | devolver a flujo factual |

No incorporar directamente.

## 37.2 Nueva declaración personal

| Declaración | Fecha | Tipo | Uso autorizado |
| --- | --- | --- | --- |
| | | motivacion / relacion_empresa / preferencia | |

Las declaraciones personales no se convierten automáticamente en evidencia profesional.

---

# 38. Estado del guion

```yaml
estado_guion:
  resultado:
    # apto
    # requiere_correccion
    # requiere_interaccion_usuario
    # requiere_revision_origen
    # requiere_actualizacion_factual
    # bloqueado
  motivo_principal:
```

> Este campo describe el estado documental del guion.
>
> El estado oficial de `GATE-GUION-CARTA-CONTENIDO` debe vivir en su propio artefacto de evaluación.

---

# 39. Control previo al gate

- [ ] Gate de entrada aprobado.
- [ ] Candidatura vigente.
- [ ] `presentada: false`.
- [ ] Fuentes resolubles.
- [ ] Destinatario clasificado.
- [ ] Empresa anónima tratada correctamente cuando aplica.
- [ ] Cultura de la oferta analizada.
- [ ] URL inicial utilizada si existía.
- [ ] URL opcional solicitada cuando correspondía.
- [ ] Ausencia de URL no tratada como bloqueo.
- [ ] Motivaciones utilizadas verificadas.
- [ ] No existen sentimientos inventados.
- [ ] Objetivo comunicativo definido.
- [ ] Argumento central definido.
- [ ] Mapa `A-NNN` completo.
- [ ] Evidencias narrables seleccionadas.
- [ ] Relación con CV explícita.
- [ ] Personalización suficiente.
- [ ] Carencias tratadas.
- [ ] Cobertura ATS/IA definida.
- [ ] Sin keyword stuffing.
- [ ] Tono definido.
- [ ] Idioma definido.
- [ ] Longitud definida.
- [ ] Prohibiciones explícitas.
- [ ] Control recruiter ejecutado.
- [ ] Control de genericidad superado.
- [ ] Control factual superado.
- [ ] No existe carta redactada dentro del guion.

---

# 40. Recomendación para `GATE-GUION-CARTA-CONTENIDO`

```yaml
gate_salida:
  id: GATE-GUION-CARTA-CONTENIDO
  recomendacion:
    # aprobar
    # no_aprobar
  motivo:
```

Regla:

```text
estado_guion: apto
→ recomendar aprobar

cualquier otro estado
→ recomendar no_aprobar
```

La IA no aprueba el gate.

---

# 41. Brief derivado para la siguiente capa

> Este bloque resume decisiones ya tomadas.
>
> No introduce ninguna decisión nueva.

```yaml
brief_carta:
  destinatario:
  idioma:
  objetivo:
  argumento_central:
  apertura:
  evidencias_prioritarias: []
  motivaciones_autorizadas: []
  cultura_utilizable: []
  carencias_a_tratar: []
  vocabulario_prioritario: []
  tono:
  longitud:
  prohibiciones_clave: []
```

---

# 42. Principio final

> **El guion debe dejar a la capa de redacción libertad para escribir bien, pero ninguna libertad para inventar estrategia, hechos, motivaciones, cultura o encaje.**
