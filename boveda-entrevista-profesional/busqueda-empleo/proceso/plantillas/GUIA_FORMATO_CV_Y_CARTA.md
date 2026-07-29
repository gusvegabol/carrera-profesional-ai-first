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
| Competencias clave | Selección visible de 6–8 competencias | Solo se incluyen las que sostienen el encaje |
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

## Marcadores de plantilla

El orden recomendado de sustitución es:

1. Identidad autorizada, contacto y fotografía.
2. Titular y perfil profesional.
3. Competencias y experiencia seleccionadas por el guion.
4. Valor diferencial, formación e información adicional.
5. Destinatario, fecha, asunto, saludo y cuerpo de la carta.
6. Revisión de longitud, justificación, ortografía y coherencia entre documentos.

Los marcadores de la plantilla son instrucciones de composición, no contenido para entregar. No puede quedar ningún marcador visible en un artefacto final.

## Controles contra improvisación

Antes de marcar la candidatura como `pendiente_de_aprobacion`, comprobar:

- cada afirmación del CV y de la carta tiene fuente identificable;
- los logros y métricas no han sido redondeados ni ampliados;
- las herramientas solo aparecen si están respaldadas;
- los requisitos de la oferta se distinguen de los requisitos que realmente cumple la persona;
- la experiencia histórica procede de la ficha o del historial autorizado;
- la foto corresponde a la persona y se ha autorizado su uso, salvo exclusión expresa;
- el nombre, teléfono, email y enlaces coinciden con los datos autorizados;
- el tono, tratamiento y llamada a la acción son coherentes con destinatario y canal;
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
