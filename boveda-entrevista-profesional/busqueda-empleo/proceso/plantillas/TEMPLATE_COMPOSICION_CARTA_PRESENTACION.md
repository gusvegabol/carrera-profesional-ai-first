---
id: TEMPLATE_COMPOSICION_CARTA_PRESENTACION
tipo: template
version: "1.1.0"
estado: en_prueba
playbook: PLAYBOOK_COMPONER_CARTA_PRESENTACION
artefacto_instancia: evaluacion-composicion-carta-presentacion.md
entrada_principal: contenido-carta-presentacion.md
salidas:
  - carta-presentacion.docx
  - carta-presentacion.pdf
gate_entrada: GATE-CONTENIDO-CARTA-COMPOSICION
gate_salida: GATE-CARTA-REVISION-HUMANA
---

# Evaluación de composición de carta de presentación

> Registro auditable de la fase de composición.
>
> La composición transforma contenido semántico cerrado en representaciones operativas y documentales sin modificar su significado.

---

# 1. Identificación

| Campo | Valor |
| --- | --- |
| Candidatura | |
| Empresa | |
| Puesto | |
| Fecha de composición | |
| Contenido fuente | `contenido-carta-presentacion.md` |
| Versión contenido | |
| Playbook | `PLAYBOOK_COMPONER_CARTA_PRESENTACION` |
| Versión playbook | `1.1.0` |
| Template | `TEMPLATE_COMPOSICION_CARTA_PRESENTACION` |
| Versión template | `1.1.0` |
| Gate entrada | `GATE-CONTENIDO-CARTA-COMPOSICION` |
| Estado gate entrada | |
| Gate salida | `GATE-CARTA-REVISION-HUMANA` |

---

# 2. Modo de salida

```yaml
modo_salida:
  modo_texto:
    disponible:
    fuente: Carta completa consolidada
    artefacto_adicional_generado: false
    texto_intacto:
  modo_documento:
    solicitado:
    docx_generado:
    pdf_generado:
```

Control:

- [ ] `modo_texto` usa directamente `Carta completa consolidada`.
- [ ] No existe `carta-presentacion.txt`.
- [ ] La cabecera no se ha introducido en el texto para copiar/pegar.
- [ ] `modo_documento` utiliza la misma fuente semántica.

---

# 3. Estado de composición

```yaml
estado_composicion:
  resultado:
    # apta
    # requiere_correccion_composicion
    # requiere_revision_contenido
    # bloqueada
  motivo_principal:
```

---

# 4. Precondiciones

- [ ] Existe `contenido-carta-presentacion.md`.
- [ ] `estado_contenido: apto`.
- [ ] `GATE-CONTENIDO-CARTA-COMPOSICION` aprobado humanamente.
- [ ] Candidatura vigente.
- [ ] `presentada: false`.
- [ ] Existe `Carta completa consolidada`.
- [ ] No existen incidencias semánticas pendientes.
- [ ] Datos personales autorizados.
- [ ] Cabecera canónica resoluble.
- [ ] Formatos DOCX/PDF permitidos.

Si falla una precondición material:

```text
→ no componer
```

---

# 5. Fuente semántica cerrada

```yaml
fuente_semantica:
  archivo: contenido-carta-presentacion.md
  version:
  seccion_autorizada: Carta completa consolidada
  hash_o_identificador:
```

Control:

- [ ] Solo se ha utilizado `Carta completa consolidada` como cuerpo.
- [ ] No se han recuperado frases adicionales.
- [ ] No se ha usado `datos-core-busqueda.md` para ampliar el cuerpo.
- [ ] No se ha usado el guion para reescribir.
- [ ] No se ha usado el CV como fuente textual del cuerpo.
- [ ] No se ha usado la oferta o web para añadir texto.
- [ ] El archivo fuente permanece sin modificaciones.

---

# 6. Contenido semántico de referencia

Copiar aquí, sin modificar:

```text
Carta completa consolidada
```

---

[CONTENIDO SEMÁNTICO DE REFERENCIA]

---

# 7. Cabecera canónica

La identidad visual de la carta puede ser coherente con la del CV sin duplicar
la fotografía. La carta no incluye fotografía por defecto; su ausencia no es un
defecto ni bloquea composición o revisión. Una eventual inclusión requeriría
una decisión o configuración humana expresa específica para esta carta y no se
implementa en este contrato.

```yaml
cabecera:
  requerida:
  aplicada:
  origen:
  version_o_identificador:
  reutiliza_cabecera_cv:
  coherencia_cv:
  mecanismo_compartido:
  datos_personales_autorizados:
  incidencias: []
```

Control:

- [ ] Cabecera requerida en `modo_documento`.
- [ ] Cabecera presente en DOCX.
- [ ] Cabecera presente en PDF.
- [ ] Procede de una fuente canónica identificable.
- [ ] Reutiliza el sistema del CV.
- [ ] No existe una definición divergente mantenida únicamente para carta.
- [ ] No exige edición manual posterior.
- [ ] No modifica el cuerpo semántico.

---

# 8. Elementos de cabecera

| Elemento | CV canónico | DOCX carta | PDF carta | Conforme |
| --- | --- | --- | --- | --- |
| nombre | | | | |
| identificación profesional | | | | |
| email | | | | |
| teléfono | | | | |
| LinkedIn | | | | |
| ubicación | | | | |
| tipografía | | | | |
| jerarquía | | | | |
| alineación | | | | |
| separadores | | | | |
| otros | | | | |

---

# 9. Privacidad de cabecera

| Dato | Autorizado | Cabecera CV | Cabecera DOCX | Cabecera PDF | Conforme |
| --- | --- | --- | --- | --- | --- |
| nombre | | | | | |
| apellido 1 | | | | | |
| apellido 2 | | | | | |
| email | | | | | |
| teléfono | | | | | |
| LinkedIn | | | | | |
| ubicación | | | | | |
| otros | | | | | |

Regla bloqueante:

```text
dato nuevo no autorizado
→ no_apta
```

---

# 10. Separación cuerpo / presentación

```yaml
separacion_documental:
  texto_semantico_carta:
  elementos_presentacion_documental:
    - cabecera
  comparacion_semantica_excluye_cabecera: true | false
```

Debe cumplirse:

```text
cuerpo fuente
=
cuerpo DOCX
=
cuerpo PDF
```

y por separado:

```text
cabecera canónica
=
cabecera DOCX
=
cabecera PDF
```

---

# 11. Rol 1 — Ingeniero de composición documental

```yaml
ingeniero_composicion:
  ejecutado: true | false
  resultado:
  incidencias: []
```

Debe comprobar:

- [ ] legibilidad;
- [ ] jerarquía visual;
- [ ] estabilidad DOCX;
- [ ] estabilidad PDF;
- [ ] consistencia visual;
- [ ] compatibilidad;
- [ ] aplicación correcta de cabecera;
- [ ] correcta representación de datos de contacto;
- [ ] ausencia de decisiones semánticas.

---

# 12. Rol 2 — Auditor de integridad documental

```yaml
auditor_integridad:
  ejecutado: true | false
  equivalencia_cuerpo_docx:
  equivalencia_cuerpo_pdf:
  equivalencia_cuerpo_docx_pdf:
  equivalencia_cabecera_docx:
  equivalencia_cabecera_pdf:
  equivalencia_cabecera_docx_pdf:
  incidencias: []
```

---

# 13. Configuración visual aplicada

```yaml
configuracion_visual:
  plantilla_visual:
  familia_tipografica:
  tamano_cuerpo:
  tamano_nombre:
  interlineado:
  margenes:
  alineacion:
  espaciado_parrafos:
  tratamiento_contacto:
  numero_paginas_docx:
  numero_paginas_pdf:
```

---

# 14. Coherencia con el CV

```yaml
coherencia_cv:
  aplicada: true | false
  cabecera_identica_o_coherente:
  sistema_visual_compartido:
  elementos_compartidos:
    - tipografia
    - tratamiento_nombre
    - tratamiento_contacto
    - jerarquia
    - otros
  observaciones:
```

Control:

- [ ] existe identidad profesional común;
- [ ] la carta sigue siendo reconocible como carta;
- [ ] no se ha copiado innecesariamente todo el layout del CV;
- [ ] no existe divergencia material entre cabeceras.

---

# 15. Salidas generadas

| Formato | Ruta | Generado | Abre correctamente | Cabecera presente |
| --- | --- | --- | --- | --- |
| DOCX | `carta-presentacion.docx` | sí / no | sí / no | sí / no |
| PDF | `carta-presentacion.pdf` | sí / no | sí / no | sí / no |

---

# 16. Trazabilidad

```yaml
generacion:
  candidatura:
  fecha:
  contenido_fuente:
  version_contenido:
  hash_fuente:
  generador:
  version_generador:
  fuente_cabecera:
  version_cabecera:
  docx:
    archivo:
    hash:
  pdf:
    archivo:
    hash:
```

---

# 17. Control de inmutabilidad semántica

Pregunta:

> ¿Se ha modificado alguna palabra, cifra, frase, argumento o decisión semántica del cuerpo?

```text
si | no
```

Si `sí`:

```text
→ requiere_revision_contenido
```

| Tipo | Fuente | DOCX | PDF | Severidad |
| --- | --- | --- | --- | --- |
| palabra | | | | |
| cifra | | | | |
| frase | | | | |
| omisión | | | | |
| adición | | | | |
| orden | | | | |

La cabecera canónica autorizada no se registra como adición semántica al cuerpo.

---

# 18. Normalizaciones técnicas

## 18 bis. Contrato de párrafos y elementos documentales

```yaml
hard_wrap_markdown:
  lineas_consecutivas_no_vacias: un_parrafo
  linea_vacia: separacion_de_parrafos
  saltos_manuales_word_por_salto_simple: prohibidos
fecha_y_asunto:
  fuente: candidatura_confirmada_y_fecha_de_composicion
  invencion: prohibida
jerarquia_visual:
  nombre: 18 pt negrita
  titular: 11 pt
  contacto: 10,5 pt
  cuerpo: 11 pt
  cuerpo_justificado: true
```

| Normalización | Aplicada |
| --- | --- |
| espacios técnicos | sí / no |
| saltos de línea | sí / no |
| caracteres tipográficos | sí / no |
| enlaces clicables | sí / no |
| no separación | sí / no |
| viudas/huérfanas | sí / no |
| otras | |

Control:

- [ ] ninguna altera significado;
- [ ] ninguna elimina texto.

---

# 19. Comparación cuerpo fuente → DOCX

```yaml
comparacion_cuerpo_docx:
  equivalencia_normalizada: true | false
  omisiones: []
  adiciones: []
  cambios_cifras: []
  cambios_orden: []
```

Resultado:

```text
apta | no_apta
```

---

# 20. Comparación cuerpo fuente → PDF

```yaml
comparacion_cuerpo_pdf:
  equivalencia_normalizada: true | false
  omisiones: []
  adiciones: []
  cambios_cifras: []
  cambios_orden: []
```

Resultado:

```text
apta | no_apta
```

---

# 21. Comparación cuerpo DOCX ↔ PDF

```yaml
comparacion_cuerpo_docx_pdf:
  equivalencia_normalizada: true | false
  diferencias: []
```

---

# 22. Comparación cabecera canónica → DOCX

```yaml
comparacion_cabecera_docx:
  equivalencia: true | false
  diferencias: []
  datos_no_autorizados: []
```

---

# 23. Comparación cabecera canónica → PDF

```yaml
comparacion_cabecera_pdf:
  equivalencia: true | false
  diferencias: []
  datos_no_autorizados: []
```

---

# 24. Comparación cabecera DOCX ↔ PDF

```yaml
comparacion_cabecera_docx_pdf:
  equivalencia: true | false
  diferencias: []
```

---

# 25. Control de orden del cuerpo

Registrar la secuencia real:

```text
saludo
→ apertura
→ desarrollo
→ cierre
→ despedida
→ firma
```

```yaml
orden:
  fuente:
  docx:
  pdf:
  conforme: true | false
```

---

# 26. Control de legibilidad DOCX

- [ ] cabecera completa;
- [ ] fuente legible;
- [ ] tamaño suficiente;
- [ ] contraste adecuado;
- [ ] interlineado correcto;
- [ ] párrafos distinguibles;
- [ ] datos de contacto legibles;
- [ ] ninguna línea cortada;
- [ ] ningún elemento superpuesto;
- [ ] ninguna página vacía inesperada;
- [ ] sin comentarios;
- [ ] sin marcas de revisión;
- [ ] sin artefactos editoriales visibles.

---

# 27. Control de legibilidad PDF

- [ ] cabecera completa;
- [ ] render completo;
- [ ] caracteres correctos;
- [ ] texto seleccionable cuando proceda;
- [ ] sin texto cortado;
- [ ] sin superposición;
- [ ] sin página vacía inesperada;
- [ ] enlaces correctos;
- [ ] firma completa;
- [ ] datos de contacto completos.

---

# 28. Paginación

```yaml
paginacion:
  objetivo_preferente: 1
  paginas_docx:
  paginas_pdf:
  legibilidad_comprometida_para_caber: true | false
```

Regla:

> Nunca reducir legibilidad ni alterar contenido para forzar una página.

---

# 29. Tipografía

```yaml
tipografia:
  fuente_disponible: true | false
  sustitucion_producida: true | false
  sustitucion_segura: true | false
  pdf_correcto: true | false
```

---

# 30. Control anti-reescritura

Confirmar que NO se ha utilizado:

- [ ] corrector con reescritura;
- [ ] IA generativa sobre el cuerpo;
- [ ] resumen automático;
- [ ] «mejorar redacción»;
- [ ] adaptación automática;
- [ ] cambio de tono;
- [ ] parafraseo;
- [ ] compresión semántica.

```yaml
reescritura_automatica:
  detectada: true | false
```

---

# 31. Revisión visual real

```yaml
render_generado: true | false
render_inspeccionado: true | false
revision_visual:
  ejecutada: true | false
  evidencia_inspeccion:
  docx:
  pdf:
  coherencia_con_cv:
  incidencias: []
```

Solo puede marcarse `ejecutada: true` si el render ha sido inspeccionado realmente.

Comprobar:

- [ ] cabecera;
- [ ] alineación;
- [ ] cortes;
- [ ] solapamientos;
- [ ] saltos;
- [ ] espaciado;
- [ ] página vacía;
- [ ] tipografía;
- [ ] coherencia con CV.

---

# 32. Incidencias

| ID | Tipo | Descripción | Severidad | Acción |
| --- | --- | --- | --- | --- |
| INC-COMP-CARTA-001 | | | | |

Tipos:

```text
composicion
cabecera
render
tipografia
paginacion
compatibilidad
integridad
privacidad
arquitectura
```

---

# 33. Clasificación de incidencias

### Visual o técnica

```text
→ corregir en composición
```

### Cabecera

Si es un defecto del sistema documental:

```text
→ corregir composición/helper/configuración compartida
```

### Semántica

```text
→ no corregir aquí
→ requiere_revision_contenido
```

---

# 34. Resultado DOCX

```yaml
docx:
  generado: true | false
  abre_correctamente: true | false
  cabecera_correcta: true | false
  equivalencia_cuerpo: true | false
  legibilidad: apta | no_apta
  render: apto | no_apto
```

---

# 35. Resultado PDF

```yaml
pdf:
  generado: true | false
  abre_correctamente: true | false
  cabecera_correcta: true | false
  equivalencia_cuerpo: true | false
  legibilidad: apta | no_apta
  render: apto | no_apto
```

---

# 36. Estado final

```yaml
resultado_composicion:
  estado:
    # apta
    # requiere_correccion_composicion
    # requiere_revision_contenido
    # bloqueada
  motivo_principal:
```

Precedencia:

```text
bloqueada
>
requiere_revision_contenido
>
requiere_correccion_composicion
>
apta
```

---

# 37. Checklist bloqueante de `apta`

## Entrada

- [ ] contenido apto;
- [ ] gate aprobado;
- [ ] candidatura vigente;
- [ ] privacidad resuelta.

## Modo texto

- [ ] `Carta completa consolidada` intacta;
- [ ] sin cabecera añadida;
- [ ] sin artefacto redundante;
- [ ] fuente no modificada.

## Cabecera

- [ ] requerida;
- [ ] aplicada;
- [ ] presente en DOCX;
- [ ] presente en PDF;
- [ ] origen registrado;
- [ ] reutiliza sistema del CV;
- [ ] coherente con CV;
- [ ] sin datos nuevos no autorizados;
- [ ] DOCX = PDF.

## Cuerpo

- [ ] fuente = cuerpo DOCX;
- [ ] fuente = cuerpo PDF;
- [ ] cuerpo DOCX = cuerpo PDF;
- [ ] sin omisiones;
- [ ] sin adiciones;
- [ ] sin cambios de cifras;
- [ ] sin cambios de orden;
- [ ] sin reescritura.

## Generación

- [ ] DOCX generado;
- [ ] PDF generado;
- [ ] ambos abren correctamente;
- [ ] no requieren edición manual.

## Render

- [ ] revisión visual ejecutada;
- [ ] DOCX apto;
- [ ] PDF apto;
- [ ] coherencia visual con CV comprobada.

---

# 38. Gate de salida

```yaml
gate_salida:
  nombre: GATE-CARTA-REVISION-HUMANA
  recomendacion:
    # abrir_revision
    # no_abrir
  motivo:
  decision_humana:
    # pendiente
    # aprobado
    # bloqueado
```

La evaluación técnica no sustituye la decisión humana.

---

# 39. Tests contractuales

| Test | Resultado | Evidencia |
| --- | --- | --- |
| Tests v1.0.0 | | |
| T15 Cabecera canónica obligatoria | | |
| T16 Canal texto independiente | | |
| T17 Cabecera ausente bloquea | | |
| T18 Cabecera divergente bloquea | | |
| T19 Privacidad de cabecera | | |
| T20 Cuerpo correcto con cabecera | | |
| T21 Misma cabecera DOCX/PDF | | |
| T22 Fuente semántica inmutable | | |

---

# 40. Conclusión

```yaml
conclusion:
  composicion:
  modo_texto:
  modo_documento:
  cabecera:
  integridad_cuerpo:
  privacidad:
  render:
  gate_revision_humana:
```

---

# 41. Historial

### v1.0.0

Primera versión para auditar composición DOCX/PDF, equivalencia semántica, privacidad, render y coherencia visual.

### v1.1.0

Añadidos:

- `modo_texto`;
- `modo_documento`;
- contrato explícito de cabecera canónica;
- origen y versión de cabecera;
- reutilización de cabecera CV;
- controles separados de cuerpo y presentación;
- privacidad específica de cabecera;
- equivalencia de cabecera DOCX/PDF;
- revisión visual de coherencia con CV;
- tests T15–T22;
- prohibición explícita de generar `.txt`.
