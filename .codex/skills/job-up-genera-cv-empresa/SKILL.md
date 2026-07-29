---
name: job-up-genera-cv-empresa
description: Use when the user explicitly invokes $job-up-genera-cv-empresa to prepare a spontaneous job application to a named company with a web-researched context, a tailored Spanish email, and a Job-up CV for human review.
---

# Job-up: genera CV para empresa

## Objetivo

Preparar una candidatura espontánea dirigida a una empresa concreta. El resultado es un paquete revisable: contexto público verificable, fuentes enlazadas, email formal en español y CV seleccionado. La skill no envía emails, no comparte archivos y no contacta con la empresa.

## Cuándo usarla

Úsala cuando el usuario proporcione una empresa —o pida identificarla— y quiera presentar su CV sin una oferta explícita. No la uses para intermediarios de colocación, contactos personales o adaptación a una oferta: usa el modelo correspondiente de `email-presentacion.md`.

## Flujo obligatorio

1. **Confirmar el encargo.** Identifica razón social, web o ubicación si el nombre es ambiguo; confirma que el destinatario es una empresa concreta y que el objetivo es una candidatura espontánea. Si faltan datos esenciales, pregunta antes de redactar.
2. **Investigar fuentes públicas.** Usa búsqueda web actual. Prioriza, en este orden, web oficial, página de empleo, noticias y proyectos de la empresa, perfiles corporativos y fuentes sectoriales fiables. Registra para cada hecho el título, URL y fecha de consulta. No uses información privada ni conviertas una inferencia en un hecho.
3. **Separar hecho e hipótesis.** Redacta un breve contexto con dos apartados: «Hechos comprobados» y «Posibles puntos de encaje». Solo los hechos comprobados pueden aparecer como afirmaciones sobre la empresa. Si no encuentras un contexto fiable, usa una apertura neutra y dilo explícitamente.
4. **Aplicar la compuerta de datos privados.** Antes de consultar o usar cualquier dato privado, exige autorización explícita para esta candidatura o una autorización escrita en la ficha privada que identifique el mismo expediente. Esa autorización no se extiende a otra candidatura, empresa o uso posterior. Si falta o es ambigua, no consultes, copies ni propagues los datos privados; bloquea solo los documentos que los necesiten y continúa con las partes públicas o factuales que no los requieran.
5. **Seleccionar el CV.** Consulta el README canónico `boveda-entrevista-profesional/busqueda-empleo/README.md`, la fuente `boveda-entrevista-profesional/busqueda-empleo/fuentes/datos-core-busqueda.md`, `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/seleccion-factual.md` y el CV maestro. Prioriza Dirección, Administración y Operaciones. Mantén las acciones en primera persona, la atribución individual y las métricas registradas. No incluyas gestión pública, actividad política, Ayuntamiento de Gáldar, concejalía, parentescos ni información sensible.
   Antes de componerlo, lee `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/GUIA_FORMATO_CV_Y_CARTA.md` y usa `TEMPLATE_CV_FORMATO.docx`. Incluye la fotografía autorizada por defecto; solo la excluyas si la persona responsable lo indica expresamente en la invocación.
6. **Redactar el email.** Parte de `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/email-presentacion.md`. Para una empresa usa tratamiento formal coherente: «Estimado equipo…», «me dirijo a ustedes», «su tiempo», «¿Tendrían disponibilidad…?». Personaliza solo asunto, empresa, saludo y apertura con hechos comprobados. Conserva dos o tres pruebas profesionales verificables y una llamada a una conversación breve. No uses «Hola» con «vosotros/vuestro» ni prometas resultados no demostrados.
   Selecciona explícitamente un único módulo de destinatario (empresa concreta, intermediario o contacto personal) y anota la razón. Selecciona también los módulos opcionales de experiencia que procedan; si no hay evidencia de encaje, no los incluyas. El email no se convierte automáticamente en carta: si se solicita carta, usa `TEMPLATE_CARTA_PRESENTACION_FORMATO.docx` y el contrato de la guía común.
   No inventes persona destinataria, cargo, dirección, localidad, fecha, asunto
   ni vacante. Si no se conoce una persona, usa `Estimado equipo de [empresa]:`;
   la fecha es la de generación; la localidad se omite si no está confirmada;
   y el asunto será `Presentación profesional — [empresa]` cuando no exista un
   puesto confirmado. En una carta solicitada, aplica los mismos fallbacks y
   bloquea solo la carta si la ambigüedad restante impide redactarla con
   seguridad.
7. **Pasar controles.** Comprueba que el email está en español, en primera persona, sin afirmaciones inventadas, sin métricas nuevas y con todas las fuentes enlazadas fuera del cuerpo del email. Verifica que el PDF adjunto corresponde al CV seleccionado y que no se han filtrado datos privados. Si la empresa no tiene una fuente fiable o el destinatario no es oficial, marca la incertidumbre y no la ocultes. Cuando el proceso remita al playbook de candidatura por oferta, usa la versión estable `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md`.
8. **Entregar para revisión.** Presenta, en este orden: (a) empresa y destinatario investigados; (b) hechos comprobados con enlaces y fecha; (c) puntos de encaje, marcados como hipótesis; (d) email completo; (e) CV y nombre exacto del archivo que se adjuntaría; (f) dudas o campos pendientes. Termina solicitando aprobación humana del contenido y del adjunto. La aprobación no autoriza por sí sola un envío automático: el usuario debe enviarlo manualmente.

## Contrato documental y antiimprovisación

- El CV debe salir de `TEMPLATE_CV_FORMATO.docx`, conservar el contrato de
  `GUIA_FORMATO_CV_Y_CARTA.md`, usar Calibri 14/12/11/10,5 pt, los colores
  `#1F2937` y `#5B6573`, contenido justificado y texto seleccionable.
- La fotografía es obligatoria por defecto y solo se excluye con instrucción
  expresa en la invocación. Registra la decisión.
- En el CV, rellena `[EXPERIENCIA 1]` a `[EXPERIENCIA 6]` y `[FORMACION 1]` a
  `[FORMACION 3]` como párrafos independientes. No introduzcas varios párrafos
  mediante saltos internos en un único slot; elimina los slots no aplicables.
- La salida del CV debe llamarse `cv.docx`, con su PDF equivalente cuando se
  genere. No mezcles el formato de una candidatura anterior.
- El email debe declarar el módulo elegido, el destinatario y la llamada a la
  acción. Empresa, cultura, necesidad, proyectos y contacto se distinguen
  entre hecho comprobado e hipótesis; nunca se presentan como hechos por
  conveniencia retórica.
- Cada afirmación del email y del CV debe proceder de una fuente factual o de
  una hipótesis etiquetada. No se improvisan logros, herramientas, métricas,
  necesidades, titular, selección de logros, experiencia histórica, traducción
  de experiencia directiva, tratamiento, llamada a la acción ni destinatario.
- La sobrecualificación y el uso de herramientas antiguas solo se tratan si la
  selección factual o el guion lo justifican. No se suavizan con afirmaciones
  inventadas.
- El email debe declarar el módulo de destinatario elegido y los módulos
  opcionales incluidos. Solo los hechos comprobados pueden describir la
  empresa; los puntos de encaje permanecen como hipótesis etiquetadas y no se
  trasladan al CV como hechos.
- Antes de entregar, revisa coherencia entre el email y el CV, marcadores,
  datos privados, fotografía, longitud, justificación, ortografía y estado de
  aprobación humana. No se envía nada.

## Salida mínima

```text
Empresa y destinatario:
Hechos comprobados (fuente y fecha):
Puntos de encaje posibles (hipótesis):
Email propuesto:
CV seleccionado:
Pendientes y riesgos:
Estado: pendiente de revisión y aprobación humana; no enviado.
```

## Reglas de seguridad y calidad

- No inventes necesidades, proyectos, cultura, contacto ni vacantes.
- No inventes fecha, localidad, cargo, asunto ni persona destinataria. Aplica
  los fallbacks de la guía común y registra cualquier omisión.
- No presentes una inferencia como «la empresa busca» o «necesita».
- No envíes, publiques, compartas ni abras un canal externo sin una instrucción posterior y explícita; esta skill solo prepara el paquete.
- Si la información pública contradice los datos del CV, conserva el dato profesional factual y señala la discrepancia.
- Si no hay contexto verificable, redacta una candidatura espontánea genérica; una personalización débil es peor que una apertura honesta.
- Conserva las formulaciones precisas de la fuente y no las acortes ni amplíes: por ejemplo, «Diseñé una solución que combinaba programación propia, Trello y Notion para gestionar candidaturas, precontratación, incorporación y seguimiento»; no la sustituyas por «Diseñé procesos de selección».

## Errores frecuentes

| Atajo | Corrección |
|---|---|
| «La empresa está buscando…» sin fuente | Escribe el hecho comprobado o conviértelo en hipótesis explícita. |
| «Hola equipo» + «vuestro» | Usa registro formal completo: «Estimado equipo» + «ustedes/su». |
| Añadir un logro para encajar con la empresa | Usa solo `fuentes/datos-core-busqueda.md` y la selección factual. |
| Reutilizar una autorización privada de otra candidatura | Exige una autorización específica o escrita en la ficha privada del mismo expediente; si no existe, bloquea solo los documentos que requieran esos datos. |
| Dejar el email listo para enviar sin revisión | Etiqueta siempre el paquete como pendiente de aprobación humana. |

## Ejemplo de apertura segura

> He comprobado que [hecho público con enlace]. Por ese motivo, me dirijo a ustedes para presentarles mi experiencia en Dirección, Administración y Operaciones y valorar si puede ser pertinente para sus necesidades actuales o futuras.
