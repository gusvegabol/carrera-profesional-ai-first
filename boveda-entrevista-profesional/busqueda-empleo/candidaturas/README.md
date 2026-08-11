# Carpetas de candidaturas

Cada candidatura aprobada para su preparación se guarda en una carpeta con el formato `CAND-YYYY-NNN-slug/`.

La carpeta puede contener estos artefactos documentales de salida:

- `cv.docx`
- `cv.pdf`
- `cv.tex`
- `carta-presentacion.docx`
- `carta-presentacion.pdf`

Además, contiene el análisis de la oferta en Markdown y la ficha de candidatura basada en [[TEMPLATE_ANALISIS_OFERTA]] y [[TEMPLATE_CANDIDATURA]].

El archivo `cv.tex` es la versión estructurada del CV para procesamiento automático por IA; debe mantenerse alineado con el contenido factual del DOCX y del PDF.

No se guardan credenciales ni datos que no sean necesarios para preparar, revisar o registrar la candidatura.

## Fin del flujo documental

Una candidatura queda documentalmente completa cuando tiene el CV final
aprobado y, cuando su contrato lo requiere, la carta final aprobada. Esta
condición no depende de `GATE-CANDIDATURA-PRESENTACION` ni cambia
`presentada: false`.

La presentación externa, los formularios, las credenciales y los
consentimientos quedan fuera del flujo actual y bajo responsabilidad de la
persona candidata. Los artefactos de validación de presentación se conservan
como línea futura en `docs/ideas-y-debates/mejoras-job-up/futuro/presentacion/`.
