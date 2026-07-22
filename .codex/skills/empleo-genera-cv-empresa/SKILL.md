---
name: empleo-genera-cv-empresa
description: Use when preparing a spontaneous job application to a named company and the user needs a web-researched context, a tailored Spanish email, and the appropriate Job-up CV for human review.
---

# Empleo: genera CV para empresa

## Objetivo

Preparar una candidatura espontánea dirigida a una empresa concreta. El resultado es un paquete revisable: contexto público verificable, fuentes enlazadas, email formal en español y CV seleccionado. La skill no envía emails, no comparte archivos y no contacta con la empresa.

## Cuándo usarla

Úsala cuando el usuario proporcione una empresa —o pida identificarla— y quiera presentar su CV sin una oferta explícita. No la uses para intermediarios de colocación, contactos personales o adaptación a una oferta: usa el modelo correspondiente de `email-presentacion.md`.

## Flujo obligatorio

1. **Confirmar el encargo.** Identifica razón social, web o ubicación si el nombre es ambiguo; confirma que el destinatario es una empresa concreta y que el objetivo es una candidatura espontánea. Si faltan datos esenciales, pregunta antes de redactar.
2. **Investigar fuentes públicas.** Usa búsqueda web actual. Prioriza, en este orden, web oficial, página de empleo, noticias y proyectos de la empresa, perfiles corporativos y fuentes sectoriales fiables. Registra para cada hecho el título, URL y fecha de consulta. No uses información privada ni conviertas una inferencia en un hecho.
3. **Separar hecho e hipótesis.** Redacta un breve contexto con dos apartados: «Hechos comprobados» y «Posibles puntos de encaje». Solo los hechos comprobados pueden aparecer como afirmaciones sobre la empresa. Si no encuentras un contexto fiable, usa una apertura neutra y dilo explícitamente.
4. **Seleccionar el CV.** Consulta `boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda.md`, `presentacion-espontanea/seleccion-factual.md` y el CV maestro. Prioriza Dirección, Administración y Operaciones. Mantén las acciones en primera persona, la atribución individual y las métricas registradas. No incluyas gestión pública, actividad política, Ayuntamiento de Gáldar, concejalía, parentescos ni información sensible.
5. **Redactar el email.** Parte de `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/email-presentacion.md`. Para una empresa usa tratamiento formal coherente: «Estimado equipo…», «me dirijo a ustedes», «su tiempo», «¿Tendrían disponibilidad…?». Personaliza solo asunto, empresa, saludo y apertura con hechos comprobados. Conserva dos o tres pruebas profesionales verificables y una llamada a una conversación breve. No uses «Hola» con «vosotros/vuestro» ni prometas resultados no demostrados.
6. **Pasar controles.** Comprueba que el email está en español, en primera persona, sin afirmaciones inventadas, sin métricas nuevas y con todas las fuentes enlazadas fuera del cuerpo del email. Verifica que el PDF adjunto corresponde al CV seleccionado y que no se han filtrado datos privados. Si la empresa no tiene una fuente fiable o el destinatario no es oficial, marca la incertidumbre y no la ocultes.
7. **Entregar para revisión.** Presenta, en este orden: (a) empresa y destinatario investigados; (b) hechos comprobados con enlaces y fecha; (c) puntos de encaje, marcados como hipótesis; (d) email completo; (e) CV y nombre exacto del archivo que se adjuntaría; (f) dudas o campos pendientes. Termina solicitando aprobación humana del contenido y del adjunto. La aprobación no autoriza por sí sola un envío automático: el usuario debe enviarlo manualmente.

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
| Añadir un logro para encajar con la empresa | Usa solo `datos-core-busqueda.md` y la selección factual. |
| Dejar el email listo para enviar sin revisión | Etiqueta siempre el paquete como pendiente de aprobación humana. |

## Ejemplo de apertura segura

> He comprobado que [hecho público con enlace]. Por ese motivo, me dirijo a ustedes para presentarles mi experiencia en Dirección, Administración y Operaciones y valorar si puede ser pertinente para sus necesidades actuales o futuras.
