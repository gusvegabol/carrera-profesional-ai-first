---
tipo: plantilla-formato-cv
version: 1.0.0
estado: activo
fecha: 2026-07-29
---

# TEMPLATE_CV_FORMATO.docx

Plantilla visual basada en `CAND-2026-010-acciona-administrativo/cv.docx`.

## Orden de sustitución

1. Sustituir `[NOMBRE]`, `[TITULAR]`, `[EMAIL]`, `[TELÉFONO]` y `[LINKEDIN]`
   únicamente por datos autorizados.
2. La plantilla conserva un único slot estructural de imagen en la celda
   derecha de la cabecera para reservar el espacio, pero nunca se entrega con
   la imagen de prueba. Sustituir ese slot por la fotografía autorizada antes
   de guardar el documento final. La fotografía se mantiene siempre salvo
   exclusión expresa en la invocación. El hueco y la imagen deben conservar
   proporción cuadrada 1:1; la referencia es 270 × 270 px.
3. Completar `[PERFIL PROFESIONAL]` y `[PROPUESTA DE VALOR]` desde el guion.
   Completar los pares `[EXPERIENCIA 1 CABECERA]` /
   `[EXPERIENCIA 1 DESCRIPCION]` hasta `[EXPERIENCIA 6 CABECERA]` /
   `[EXPERIENCIA 6 DESCRIPCION]`. Los marcadores que ocupan una cabecera
   conservan negrita; los que ocupan una descripción factual permanecen en
   estilo normal justificado. En cada etapa, la cabecera y la descripción
   ocupan el mismo párrafo, en runs separados, para que solo la cabecera quede
   en negrita. Completar también
   `[COMPETENCIA 1]` a `[COMPETENCIA 4]` y `[FORMACION 1]` a `[FORMACION 3]`
   como párrafos independientes. La plantilla admite como máximo cuatro
   competencias visibles.
4. Para una experiencia no aplicable, dejar vacíos en el JSON tanto
   `[EXPERIENCIA N CABECERA]` como `[EXPERIENCIA N DESCRIPCION]`. El generador
   eliminará el párrafo completo de esa experiencia, incluido su salto de
   línea final; nunca dejará una línea o un párrafo en blanco.
5. Eliminar cualquier otro marcador no aplicable; nunca dejarlo visible.
6. Revisar que el contenido narrativo quede justificado y que el documento ocupe una página.

## Invariantes de sustitución

La sustitución es únicamente de contenido. No puede modificar propiedades de
formato del template: alineación, fuente, tamaño, color, negrita, espaciado,
indentación, sangría, interlineado, tabla de cabecera, celda de fotografía ni
proporción de la imagen. En particular, la cabecera debe conservar tres
párrafos independientes y alineados al inicio (`start`/izquierda): nombre,
titular y contacto. Nunca se debe aplicar centrado a la cabecera por conveniencia
de la longitud del texto.

Antes de entregar el documento, se debe comparar la cabecera sustituida con el
template y verificar que solo han cambiado los textos y la fotografía autorizada.

Cada punto y aparte de experiencia y formación debe ser un párrafo real. No
se deben introducir saltos de línea internos para simular párrafos: la última
línea de un párrafo justificado no puede quedar estirada artificialmente.

La plantilla DOCX contiene solo marcadores y una reserva visual de fotografía; no contiene datos de CAND-2026-010.
