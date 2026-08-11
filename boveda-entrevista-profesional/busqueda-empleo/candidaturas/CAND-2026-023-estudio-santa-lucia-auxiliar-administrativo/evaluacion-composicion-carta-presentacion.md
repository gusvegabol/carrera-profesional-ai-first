---
id: evaluacion-composicion-carta-CAND-2026-023
tipo: evaluacion_composicion_carta_presentacion
version: "1.1.0"
estado: en_prueba
candidatura: CAND-2026-023
fecha_composicion: 2026-08-11
contenido_fuente: contenido-carta-presentacion.md
version_contenido: "1.1.0"
gate_entrada: GATE-CONTENIDO-CARTA-COMPOSICION
estado_gate_entrada: aprobado
gate_salida: GATE-CARTA-REVISION-HUMANA
decision_humana: aprobado
estado_gate: aprobado
---

# Evaluación de composición de carta de presentación — CAND-2026-023

## 1. Identificación

| Campo | Valor |
| --- | --- |
| Candidatura | CAND-2026-023 |
| Contenido fuente | `contenido-carta-presentacion.md` → `Carta completa consolidada` |
| Hash fuente normalizada | `0bc9bd4ba79f6d53c9c78d3082e90f5b92dff8dc1688c8a2e6cd51d5b3b38180` |
| Generador | `scripts/job-up/componer_carta_presentacion.py` |
| Versión generador | 1.1.0 |

## 2. Estado de composición

```yaml
estado_composicion: apta
recomendacion_gate: recomendar_aprobar
decision_humana: pendiente
estado_gate: aprobado
modo_salida: modo_documento
```

## 3. Cabecera canónica compartida

```yaml
requerida: true
aplicada: true
origen: datos-generacion.json:contenido_cv.encabezado
version_o_identificador: datos-generacion-cv@1.2
reutiliza_cabecera_cv: true
coherencia_cv: true
fuente: [Gustavo Vega, 'Administración y gestión documental | Organización, Excel y apoyo
    a procesos administrativos', Las Palmas | gusvegabol@gmail.com | 669 549 933]
docx: true
pdf: true
docx_pdf: true
```

La cabecera se resuelve mediante el mismo helper canónico que consume el compositor de CV; no se mantiene una cabecera independiente de carta.

## 4. Fuente semántica cerrada

Solo se utilizó `Carta completa consolidada`. No se consultaron guion, candidatura, análisis, datos-core, CV, oferta ni web para añadir texto.

## 5. Configuración visual aplicada

```yaml
tipografia: Calibri
tamano_cuerpo: 11 pt
tamano_nombre: 18 pt negrita
tamano_titular: 11 pt
tamano_contacto: 10.5 pt
fecha_documento: 11 de agosto de 2026
asunto_documento: Candidatura — Auxiliar administrativo/a SIN EXPERIENCIA — ESTUDIO SANTA LUCIA DE TIRAJANA, S. L. / Tecnocasa Gáldar
margenes: 2.0 cm superior/inferior; 2.1 cm izquierdo/derecho
interlineado: 1.15
espaciado_parrafos: 8 pt; apertura 14 pt
paginas_docx: 1
paginas_pdf: 1
coherencia_cv: Calibri y tratamiento sobrio del contacto; layout propio de carta
```

## 6. Equivalencia semántica del cuerpo

```yaml
fuente_docx: true
fuente_pdf: true
docx_pdf: true
omisiones: []
adiciones: []
cambios_cifras: []
cambios_orden: [false, false, false]
```

La secuencia material se conserva: saludo → apertura → desarrollo → contexto → cierre → despedida → firma. Las líneas físicas consecutivas del Markdown se reconstruyen como un único párrafo semántico.

## 7. Privacidad

```yaml
datos_autorizados: [Gustavo Vega, Las Palmas, gusvegabol@gmail.com, 669 549 933]
datos_adicionales: []
resultado: conforme
```

## 8. Roles

```yaml
ingeniero_composicion_documental: ejecutado
auditor_integridad_documental: ejecutado
redactor: no_aplica
recruiter: no_aplica
```

## 9. Salidas generadas

| Formato | Ruta | Estado |
| --- | --- | --- |
| DOCX | `carta-presentacion.docx` | generado y validado |
| PDF | `carta-presentacion.pdf` | generado y validado |
| Evaluación | `evaluacion-composicion-carta-presentacion.md` | generado |

## 10. Calidad técnica

```yaml
docx:
  abre: true
  legibilidad: apta
  render: apto
  incidencias: []
pdf:
  abre: true
  legibilidad: apta
  render: apto
  incidencias: []
render_generado: true
render_inspeccionado: true
revision_visual:
  ejecutada: true
  evidencia_inspeccion: tmp/qa-CAND-2026-023-carta/page-1.png
  renderizador: Poppler pdftoppm
  inspeccion: cabecera, márgenes, espaciado, saltos, paginación y ausencia de cortes/solapamientos
  comparacion_cv: cabecera, nombre, contacto y tipografía coherentes; layout propio de carta
  pdf2image: no_disponible
  impacto_pdf2image: no_bloqueante
```

## 11. Incidencias

`ninguna`

La inspección visual real del PNG confirmó una página legible, sin cortes,
solapamientos, desbordamientos ni problemas de jerarquía. La ausencia de
`pdf2image` no bloquea porque se utilizó el renderizador alternativo disponible.

## 12. Resultado de composición

```yaml
estado_composicion: apta
recomendacion_gate: recomendar_aprobar
decision_humana: aprobado
estado_gate: aprobado
```

La composición no aprueba la carta final; solo deja los artefactos disponibles para revisión humana y mantiene `presentada: false`.
