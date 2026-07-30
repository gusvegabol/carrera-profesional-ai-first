---
tipo: guia-formato-documental
version: 1.0.0
estado: activo
fecha: 2026-07-29
---

# Guía de formato de CV y carta de presentación

Esta guía es el contrato común de contenido y formato para los documentos de candidatura de Job-up. Se aplica tanto a una candidatura por oferta como a un CV dirigido a una empresa sin oferta activa.

## Fuente de contenido

El documento de origen es siempre el guion de adaptación de CV de la candidatura, junto con el análisis de la oferta o la selección factual vigente. La plantilla controla la presentación; no autoriza a crear hechos.

| Guion o fuente | CV | Carta de presentación |
| --- | --- | --- |
| Titular | Titular principal adaptado al puesto | Puede reaparecer en la apertura si aporta contexto |
| Perfil profesional | Resumen principal | Se transforma en una apertura breve, no se copia completo |
| Competencias clave | Selección visible de hasta 4 competencias | Solo se incluyen las que sostienen el encaje; el límite responde a los cuatro slots de la plantilla DOCX |
| Experiencia relevante | Evidencias y funciones priorizadas | Máximo dos evidencias desarrolladas |
| Valor diferencial | Bloque de propuesta de valor | Argumento central de encaje |
| Sobrecualificación o límites | Tratamiento definido por el guion | Solo si el guion indica que debe abordarse |
| Datos privados | Solo los autorizados para esa candidatura | Solo los autorizados y necesarios |
| Frase de encaje | Cierre o síntesis del CV cuando proceda | Llamada a la acción y cierre |

La carta puede seleccionar menos información que el CV, pero nunca puede añadir logros, herramientas, responsabilidades, métricas, titulaciones o experiencias que no estén respaldados por el guion y sus fuentes.

## Contrato visual

- Fuente: Calibri.
- Jerarquía: 14 pt para títulos principales, 12 pt para subtítulos, 11 pt para cuerpo y 10,5 pt para metadatos y fechas.
- Colores: `#1F2937` para texto principal y `#5B6573` para información secundaria.
- Alineación: contenido narrativo justificado. La alineación funcional puede mantenerse en el encabezado, datos de contacto, saludo, asunto, títulos y firma.
- Extensión: una página como objetivo operativo. Si la legibilidad exige superar una página, se detiene la generación para revisión humana.
- Fotografía: obligatoria por defecto, tanto en CV como en carta, salvo que la persona responsable indique expresamente lo contrario al invocar la skill.
- Proporción de fotografía: cuadrada, 1:1. La imagen de referencia es de 270 × 270 px; si se redimensiona, deben modificarse ancho y alto proporcionalmente, nunca solo una dimensión.
- Texto: seleccionable y extraíble; no se convierten párrafos en imágenes.
- Estructura: encabezados estándar y viñetas reales; no se usan tablas ni columnas para el contenido narrativo.
- El encabezado puede usar una tabla de dos celdas exclusivamente como mecanismo de composición para distribuir identidad y fotografía.
- La cabecera debe conservar la composición del template en tres párrafos reales: nombre completo en 18 pt y negrita, titular en 11 pt e información de contacto en 10,5 pt. No se permite concatenar nombre, titular y contacto en una sola línea ni sustituir la jerarquía por texto plano.

## Marcadores de plantilla

El CV utiliza slots de experiencia y formación como párrafos independientes.
La última etapa utiliza `[EXPERIENCIA 6 CABECERA]` y
`[EXPERIENCIA 6 DESCRIPCION]` en runs separados dentro del mismo párrafo para
mantener la cabecera en negrita y la descripción en estilo normal. Nunca se
resuelve un slot de experiencia o formación introduciendo varios bloques
separados por saltos de línea dentro del mismo párrafo.

La carta utiliza exactamente estos marcadores, que deben resolverse antes de
entregarla: `[DESTINATARIO]`, `[FECHA]`, `[ASUNTO]`, `[SALUDO]`, `[APERTURA]`,
`[EVIDENCIA 1]`, `[EVIDENCIA 2]`, `[ENCAJE]`, `[CIERRE]`, `[DESPEDIDA]` y
`[FIRMA]`. El CV utiliza los marcadores definidos en su plantilla y en el
guion de adaptación. No se puede introducir un marcador nuevo sin actualizar
la plantilla, esta guía y la skill que la utiliza.

El orden recomendado de sustitución es:

1. Identidad autorizada, contacto y fotografía.
2. Titular y perfil profesional.
3. Competencias y experiencia seleccionadas por el guion.
4. Valor diferencial, formación e información adicional.
5. Destinatario, fecha, asunto, saludo y cuerpo de la carta.
6. Revisión de longitud, justificación, ortografía y coherencia entre documentos.

Los marcadores de la plantilla son instrucciones de composición, no contenido para entregar. No puede quedar ningún marcador visible en un artefacto final.

## Decisiones cerradas para evitar improvisaciones

- No se inventan destinatario, cargo de la persona destinataria, dirección,
  localidad, fecha, asunto, vacante, empresa, requisitos, herramientas,
  métricas, logros ni datos de contacto.
- Si no se conoce una persona concreta, `[DESTINATARIO]` usa la empresa o el
  equipo confirmado; el `[SALUDO]` será `Estimado equipo de [empresa]:`.
- `[FECHA]` usa la fecha de generación del documento. No se presenta como fecha
  de envío ni se obtiene de una inferencia.
- La localidad solo se incluye si figura en la oferta, en una fuente pública
  fiable o en una instrucción autorizada. No se utiliza la localidad privada
  de la persona por defecto. Si no está confirmada, se omite.
- `[ASUNTO]` se deriva únicamente del puesto y la empresa confirmados. En una
  candidatura espontánea sin puesto confirmado se usa `Presentación
  profesional — [empresa]`; nunca se crea una vacante para completar el
  campo.
- Si falta información del destinatario, asunto o localidad, se aplica este
  fallback y se deja constancia en el expediente. Si la ambigüedad impide una
  carta o un email seguro, se bloquea ese artefacto, pero se continúa con el CV
  cuando pueda generarse de forma factual.
- El titular, el tono, el tratamiento, la llamada a la acción, la selección de
  tres a cinco logros, la traducción de un cargo directivo a un puesto auxiliar
  o técnico, la inclusión de experiencia histórica y el uso de herramientas
  antiguas deben estar justificados por el guion y sus fuentes. La
  sobrecualificación se trata solo según la estrategia explícita del guion.
- En candidaturas espontáneas, los hechos de la empresa, las hipótesis de
  encaje, el módulo de destinatario y los módulos opcionales del email se
  seleccionan y etiquetan por separado. Una hipótesis nunca entra en el CV ni
  se presenta como necesidad de la empresa.

## Controles contra improvisación

Antes de marcar la candidatura como `pendiente_de_aprobacion`, comprobar:

- cada afirmación del CV y de la carta tiene fuente identificable;
- el titular, el perfil, los tres a cinco logros y la experiencia histórica
  seleccionada corresponden al guion y no son una elección ornamental;
- cada punto y aparte de experiencia y formación corresponde a un párrafo
  real; no hay saltos internos usados para simular párrafos ni líneas
  justificadas artificialmente;
- los logros y métricas no han sido redondeados ni ampliados;
- las herramientas solo aparecen si están respaldadas;
- los requisitos de la oferta se distinguen de los requisitos que realmente cumple la persona;
- la experiencia histórica procede de la ficha o del historial autorizado;
- la foto corresponde a la persona y se ha autorizado su uso, salvo exclusión expresa;
- el placeholder `[FOTO]` de la plantilla ha sido sustituido por la fotografía
  real autorizada; no basta con comprobar que el DOCX contiene una imagen;
- los encabezados y pies de página no contienen texto interno de template,
  instrucciones de composición ni marcadores antes de entregar el artefacto;
- el nombre, teléfono, email y enlaces coinciden con los datos autorizados;
- el tono, tratamiento y llamada a la acción son coherentes con destinatario y canal;
- destinatario, fecha, asunto y localidad siguen las reglas cerradas de esta
  guía y no contienen inferencias;
- la carta resuelve todos sus marcadores, incluido `[DESPEDIDA]`, y no amplía
  los hechos seleccionados para el CV;
- CV, carta y LaTeX no contienen contradicciones;
- la salida cumple una página, texto seleccionable, cuerpo justificado y jerarquía visual;
- no quedan marcadores, notas internas, hipótesis ni datos no autorizados;
- no se realiza ningún envío.

## Artefactos y nombres

Cada candidatura debe conservar, cuando el flujo aplique, exactamente estos nombres:

- `cv.docx`
- `cv.pdf`
- `cv.tex`
- `carta-presentacion.docx`
- `carta-presentacion.pdf`

La plantilla no sustituye al índice de candidatura ni al estado PCS. La aprobación humana sigue siendo necesaria antes de presentar cualquier documento.
