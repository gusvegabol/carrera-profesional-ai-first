---
id: 2026-07-29-formato-documental-candidaturas-design
tipo: diseño
estado: aprobado
fecha: 2026-07-29
---

# Diseño de formato documental para candidaturas Job-up

## Objetivo

Establecer un contrato común para generar CV y cartas de presentación de Job-up
con un formato visual estable y una correspondencia explícita con
`TEMPLATE_GUION_ADAPTACION_CV.md`.

## Componentes

1. `TEMPLATE_CV_FORMATO.docx`: plantilla visual reutilizable basada en el CV de
   CAND-2026-010.
2. `TEMPLATE_CARTA_PRESENTACION_FORMATO.docx`: plantilla visual reutilizable
   para cartas de presentación, con la misma identidad documental.
3. `GUIA_FORMATO_CV_Y_CARTA.md`: contrato de correspondencia entre el guion,
   el CV y la carta, junto con reglas de formato y control.
4. `TEMPLATE_GUION_ADAPTACION_CV.md`: ajuste de sus reglas visuales para
   admitir fotografía obligatoria salvo exclusión expresa.
5. `job-up-candidatura-oferta/SKILL.md` y
   `job-up-genera-cv-empresa/SKILL.md`: incorporación del contrato documental,
   los controles de improvisación y la obligación de producir documentos
   coherentes entre sí.

## Contrato visual

- Fuente: Calibri.
- Jerarquía: 14 pt para secciones, 12 pt para subtítulos, 11 pt para contenido
  y 10,5 pt para fechas y metadatos.
- Colores: `#1F2937` para texto y títulos; `#5B6573` para metadatos.
- Contenido justificado, con excepción del encabezado, títulos, saludo, firma y
  datos de contacto cuando su alineación funcional sea necesaria.
- Una página para CV y una página para carta.
- Fotografía siempre, salvo que la persona responsable indique expresamente lo
  contrario durante la invocación de la skill.
- Texto seleccionable, encabezados estándar y viñetas; no usar tablas ni
  columnas en el contenido operativo del CV.

## Contrato de contenido

El guion de adaptación es la fuente de composición. El CV y la carta deben
compartir titular, perfil, competencias, evidencias y límites. La carta puede
seleccionar menos evidencias, pero no añadir afirmaciones que no existan en el
guion y el análisis factual.

## Control de improvisación

Las skills deberán controlar explícitamente titular, selección de logros,
traducción de sobrecualificación, requisitos no acreditados, experiencia
histórica, herramientas antiguas, fotografía, datos privados, nombres de
archivo, extensión, alineación, tono, fuentes públicas y llamada a la acción.

La salida seguirá siendo `pendiente_de_aprobacion`; ningún formato ni
verificación visual autoriza el envío.
