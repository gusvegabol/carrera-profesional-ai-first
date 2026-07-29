---
name: job-up-candidatura-oferta
description: Use when the user explicitly provides a job offer by accessible URL, Markdown file, or pasted text and wants to prepare a traceable Job-up application.
---

# Job-up: candidatura por oferta

## Objetivo y límites

Prepara una candidatura por oferta trazable y revisable a partir del texto
completo de una oferta. La salida de fase 1 es un expediente documentado en
estado `pendiente_de_aprobacion`. No envía candidaturas, no completa
formularios, no contacta con empresas y no usa navegadores, conectores ni
canales externos.

La oferta no autoriza por sí sola la creación de una sesión PCS ni el uso de
datos privados. Esta skill no crea ni cierra sesiones directamente y no
reproduce la lógica de `job-up-inicia-sesion`.

## Entradas admitidas

Acepta exactamente cualquiera de estas modalidades:

1. Una URL pública accesible.
2. Un fichero Markdown de estructura libre aportado por la persona usuaria.
3. Texto de la oferta copiado y pegado en el chat.

No impongas una plantilla al Markdown ni al texto. Obtén el contenido completo
disponible y extrae la información con fidelidad. Una URL inaccesible no se
trata como contenido: pide un fichero Markdown o texto alternativo.

## Flujo obligatorio

Sigue este orden y deja constancia de cada decisión:

1. **Identificar la procedencia.** Registra la URL de origen y la fecha de
   consulta o recepción cuando exista. Para un fichero o texto aportado,
   registra el tipo de material, la referencia disponible y la fecha de
   recepción. Conserva el texto completo de la oferta en el análisis; no
   sustituyas la fuente por un resumen.
2. **Extraer la oferta.** Identifica empresa, puesto, funciones, requisitos,
   salario, modalidad, zona, jornada y contrato cuando estén disponibles.
   Mantén visibles también los campos ausentes y no descartes por salario,
   modalidad, zona, jornada o contrato.
3. **Pedir solo lo esencial que falte.** Solicita únicamente un dato ausente
   si es imprescindible para identificar el expediente o continuar de forma
   honesta. No pidas detalles accesorios ni completes huecos por inferencia.
   Si el dato esencial no puede obtenerse, detén la producción documental y
   registra el bloqueo.
4. **Resolver la sesión Job-up.** Busca señales documentales de sesiones Job-up
   abiertas. Si hay una única sesión abierta, vincula el expediente a ella.
   Si hay varias, o no puede determinarse una única sesión adecuada, muestra
   sus identificadores y pide a la persona usuaria que seleccione una; no
   elijas por recencia, similitud o inferencia.
5. **Gestionar la ausencia de sesión.** Si no existe ninguna sesión Job-up
   abierta, informa de ello y pregunta exactamente si desea ejecutar
   `job-up-inicia-sesion`. Detente sin invocarla ante una respuesta negativa,
   ambigua, implícita o sin respuesta. Solo tras una confirmación afirmativa
   explícita puedes invocar esa skill delegada; después comprueba de nuevo que
   existe una única sesión Job-up abierta antes de continuar. La oferta nunca
   cuenta como confirmación.
6. **Crear el análisis.** Dentro del expediente de la candidatura, registra la
   procedencia, el contenido completo, los campos extraídos, los faltantes,
   la sesión elegida y los bloqueos. Usa las rutas canónicas de Job-up:
   `boveda-entrevista-profesional/busqueda-empleo/fuentes/`,
   `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/`,
   `boveda-entrevista-profesional/busqueda-empleo/candidaturas/` y
   `boveda-entrevista-profesional/busqueda-empleo/seguimiento/`.
7. **Aplicar la metodología.** Sigue el playbook vigente
   `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md` y la matriz
   de artefactos de `boveda-entrevista-profesional/busqueda-empleo/README.md`.
   Antes de generar documentos, lee `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/GUIA_FORMATO_CV_Y_CARTA.md` y usa `TEMPLATE_CV_FORMATO.docx` y `TEMPLATE_CARTA_PRESENTACION_FORMATO.docx`. El guion gobierna el contenido de ambos documentos.
   Selecciona un perfil principal, uno secundario y de tres a cinco logros
   respaldados por `fuentes/datos-core-busqueda.md`; marca los requisitos no
   acreditados y mantén la trazabilidad frase por frase.
   La selección del titular, el tono, la traducción de una experiencia
   directiva a un puesto auxiliar o técnico, la experiencia histórica, las
   herramientas antiguas y el tratamiento de la sobrecualificación deben estar
   explicados en el guion; no son decisiones libres de redacción.
   En la carta, no inventes destinatario, cargo, fecha, localidad ni asunto:
   si no hay persona usa `Estimado equipo de [empresa]:`, la fecha es la de
   generación, la localidad se omite si no está confirmada y el asunto se
   deriva solo de empresa y puesto confirmados. Si falta un puesto confirmado,
   bloquea la carta por asunto ambiguo y continúa con el CV si es posible.
8. **Aplicar la autorización privada por candidatura.** Antes de consultar,
   copiar o incorporar cualquier dato de
   `fuentes/datos-privados-candidatura.md`, comprueba que existe autorización
   escrita aplicable a este expediente. Puedes reutilizar la autorización
   escrita de la ficha privada solo cuando identifica la misma candidatura;
   registra esa procedencia y su alcance. No copies ni propagues datos sin
   autorización, ni reutilices una autorización de otro expediente. Si la
   autorización falta, es ambigua o no cubre el dato, excluye ese dato y
   bloquea únicamente los documentos que lo necesitan; continúa con la parte
   factual que sí esté respaldada.
9. **Preparar y revisar.** Completa análisis, guion de adaptación, CV, carta,
   veredicto final y el índice de documentos según el playbook. Detente ante
   una contradicción factual, un bloqueo obligatorio abierto o una decisión
   `corregir_antes_de_revisar`.
10. **Actualizar el seguimiento.** Actualiza la ficha de candidatura y
    `seguimiento/seguimiento-candidaturas.md` con estado, sesión, procedencia,
    autorización aplicable, bloqueos, veredicto y rutas existentes.
11. **Entregar para aprobación humana.** Cuando no queden bloqueos que impidan
    la salida y el veredicto lo permita, entrega el paquete en estado
    `pendiente_de_aprobacion`. Expón lo que debe revisar la persona y deja
   claro que ninguna aprobación implícita permite enviar o contactar.

## Contrato documental obligatorio

- Usa los nombres exactos `cv.docx`, `cv.pdf`, `cv.tex`,
  `carta-presentacion.docx` y `carta-presentacion.pdf`.
- Genera el CV y la carta con las plantillas visuales comunes, sin copiar el
  contenido de una candidatura anterior como fuente factual.
- Incluye la fotografía autorizada por defecto en CV y carta. Solo puede
  excluirse cuando la persona responsable lo indique expresamente en la
  invocación; registra esa exclusión en el expediente.
- Justifica el contenido narrativo de CV y carta. Encabezados, contacto,
  saludos, asuntos, títulos y firma pueden conservar alineación funcional.
- Comprueba Calibri, jerarquía 14/12/11/10,5 pt, colores `#1F2937` y
  `#5B6573`, una página como objetivo, texto seleccionable y ausencia de
  tablas o columnas en el contenido narrativo.
- La carta puede resumir el CV, pero no puede introducir ningún hecho, logro,
  herramienta, requisito cumplido, dato de empresa o afirmación que no figure
  en el guion y el análisis.
- La carta debe resolver también `[DESPEDIDA]`; el tratamiento, saludo,
  despedida y llamada a la acción deben ser coherentes entre sí y con el canal.
- No inventes persona destinataria, cargo, dirección, localidad, fecha, asunto,
  vacante ni datos de contacto. Aplica los fallbacks de la guía común y deja
  constancia de los campos omitidos o derivados.
- El titular, la selección de tres a cinco logros, la experiencia histórica,
  las herramientas antiguas y cualquier traducción de experiencia directiva a
  un puesto auxiliar o técnico deben poder rastrearse al guion y a una fuente.
- Si la salida requiere tratar la sobrecualificación, usa únicamente la
  formulación aprobada en el guion; no la ocultes ni la compenses con promesas.
- Antes de entregar, revisa marcadores, datos privados, fotografía, tono,
  tratamiento, llamada a la acción, coherencia con `cv.tex` y enlaces del
  índice. Si un elemento concreto no puede verificarse, bloquea solo el
  artefacto afectado.
- Para la conversión DOCX→PDF, usa la instalación directa de LibreOffice
  mediante su ejecutable de consola (`soffice.com`), sin depender de que esté
  en `PATH`, y con un perfil temporal aislado para evitar instancias
  concurrentes. Ejecuta una sola conversión por documento y comprueba que el
  PDF existe antes de continuar.
- Si aparece el error de `bootstrap.ini`, detén la conversión, no abras una
  segunda instancia ni repitas el lanzamiento automáticamente y registra el
  diagnóstico. La validación estructural no sustituye a una verificación
  visual que no haya podido completarse.

## Detenciones obligatorias

Detén el flujo y explica el motivo cuando ocurra cualquiera de estas
condiciones. Cuando la condición sea un bloqueo de autorización para datos
privados, la detención afecta únicamente a los artefactos que necesitan esos
datos: permite continuar el análisis factual autorizado y no debe interpretarse
como una detención total del flujo.

- la fuente no contiene una oferta completa y no puede obtenerse el contenido;
- faltan datos esenciales imposibles de obtener;
- la URL es inaccesible y no se aporta Markdown o texto alternativo;
- hay varias sesiones y la selección humana sigue pendiente;
- no hay sesión abierta y no existe confirmación explícita para invocar
  `job-up-inicia-sesion`;
- la invocación delegada no produce exactamente una única sesión abierta;
- existe una contradicción factual sin resolver;
- un documento requiere datos privados cuya autorización por candidatura falta,
  es ambigua o no cubre su uso; bloquea solo ese documento o artefacto, y
  continúa el análisis factual autorizado;
- el veredicto exige corregir antes de revisar.

No resuelvas una detención inventando datos, eligiendo una sesión por tu
cuenta, ampliando el alcance de una autorización o convirtiendo una oferta en
permiso para crear una sesión.

## Lista de control de salida

- [ ] La entrada conserva el texto completo de la oferta.
- [ ] La procedencia y la fecha de recepción o consulta están registradas.
- [ ] Solo se pidieron datos esenciales ausentes.
- [ ] Hay una única sesión Job-up seleccionada humanamente cuando era necesario.
- [ ] La autorización privada está vinculada a esta candidatura o los datos
      privados quedaron excluidos y bloqueados solo donde correspondía.
- [ ] El análisis, la ficha, el seguimiento y las rutas de documentos están
      actualizados.
- [ ] La decisión del veredicto permite la salida.
- [ ] Destinatario, fecha, asunto, localidad, saludo y despedida están
      confirmados o resueltos mediante los fallbacks permitidos.
- [ ] El estado final es `pendiente_de_aprobacion`.
- [ ] No se ha enviado ninguna candidatura ni se ha contactado con nadie.
