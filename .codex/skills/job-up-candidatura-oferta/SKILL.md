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
   Después de completar y revisar el guion, crea
   `datos-generacion.json` dentro de la carpeta de la candidatura conforme a
   `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_DATOS_GENERACION_CANDIDATURA.json`.
   El JSON debe contener los textos finales de CV, carta y LaTeX, las rutas
   relativas al proyecto de las plantillas, la fotografía autorizada y las
   cinco salidas. No delegues la redacción ni la adaptación al script.
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
   Antes de invocar el generador, comprueba que la ficha contiene en su
   frontmatter `estado` y `presentada` con valor booleano. Si falta alguno, o
   el estado global no coincide, detén el flujo.
9. **Generar y revisar.** Completa análisis, guion de adaptación y
   `datos-generacion.json`; después invoca el generador Python pasando la ruta
   del JSON, por ejemplo `python RUTA_PROYECTO/scripts/job-up/generar_candidatura.py ruta/al/datos-generacion.json`.
   El generador debe producir `cv.docx`, `cv.pdf`,
   `carta-presentacion.docx`, `carta-presentacion.pdf` y `cv.tex` solo después
   de superar todas sus validaciones. Si falla, lee el registro de error,
   corrige el JSON o las entradas desde la IA y permite una nueva ejecución
   manual cuando proceda; no hagas reintentos automáticos ni generes
   manualmente una variante paralela. Completa
   después el veredicto final y el índice de documentos según el playbook.
   Detente ante una contradicción factual, un bloqueo obligatorio abierto, un
   error del generador o una decisión `corregir_antes_de_revisar`.
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
- Sustituye la única imagen de la celda derecha de la cabecera de cada plantilla
  DOCX por la fotografía real autorizada antes de guardar el DOCX. No busques la
  foto por nombre ni reemplaces la primera imagen del documento: si la plantilla
  no contiene exactamente ese único slot estructural, detén la generación.
  Comprueba el contenido binario de la imagen embebida; detectar una imagen no
  demuestra que la foto haya sido incorporada.
- Elimina del resultado cualquier pie o encabezado que identifique el archivo
  como `Plantilla`, `template` o instrucciones internas de composición. Esos
  textos pueden permanecer únicamente en el DOCX reutilizable de la plantilla.
- Justifica el contenido narrativo de CV y carta. Encabezados, contacto,
  saludos, asuntos, títulos y firma pueden conservar alineación funcional.
- Conserva la cabecera visual de las plantillas: nombre completo en un párrafo
  independiente de 18 pt y negrita, titular en un segundo párrafo de 11 pt y
  contacto en un tercer párrafo de 10,5 pt, todos alineados al inicio
  (`start`/izquierda) como en el template. No concatenes nombre, titular y
  contacto en una sola línea, no apliques centrado y no alteres ninguna
  propiedad de formato al sustituir el contenido.
- Comprueba Calibri, jerarquía 14/12/11/10,5 pt, colores `#1F2937` y
  `#5B6573`, una página como objetivo, texto seleccionable y ausencia de
  tablas o columnas en el contenido narrativo.
- La carta puede resumir el CV, pero no puede introducir ningún hecho, logro,
  herramienta, requisito cumplido, dato de empresa o afirmación que no figure
  en el guion y el análisis.
- La carta debe resolver también `[DESPEDIDA]`; el tratamiento, saludo,
  despedida y llamada a la acción deben ser coherentes entre sí y con el canal.
- En el CV, rellena los pares `[EXPERIENCIA 1 CABECERA]` /
  `[EXPERIENCIA 1 DESCRIPCION]` hasta `[EXPERIENCIA 6 CABECERA]` /
  `[EXPERIENCIA 6 DESCRIPCION]`, además de `[FORMACION 1]` a `[FORMACION 3]`,
  como párrafos independientes según la plantilla. No introduzcas varios
  párrafos mediante saltos internos en un único slot; elimina los slots no
  aplicables.
- Si se seleccionan menos de seis experiencias, conserva todos los pares de
  experiencia en `datos-generacion.json` y deja con valor `""` los pares no
  utilizados. Si la cabecera de una experiencia está vacía, el generador debe
  eliminar la línea completa de esa experiencia, incluido su retorno de carro;
  no debe dejar un párrafo vacío. La cabecera y la descripción deben estar
  ambas vacías o ambas informadas. Esta regla se aplica tanto al CV DOCX como
  a `cv.tex`.
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
- El generador debe leer, desde el `.env` situado junto al script, estas
  variables:
  `RUTA_PROYECTO` y `SOFFICE_PATH`.
  `SOFFICE_PATH` debe apuntar a la ruta absoluta de `soffice.com`; no se debe
  depender de `PATH` ni ejecutar `soffice` por nombre. En este entorno la ruta
  validada es `C:\Program Files\LibreOffice\program\soffice.com`.
- La ubicación canónica del generador es
  `scripts/job-up/generar_candidatura.py`; la invocación debe funcionar desde
  cualquier directorio y usar el `.env` de esa carpeta.
- Solo se permite regenerar si el frontmatter de `candidatura.md` contiene
  `presentada: false` y el estado es compatible. La skill no interpreta
  observaciones en lenguaje natural para decidirlo.
- Para cada DOCX, el generador debe hacer una invocación separada y única de
  `SOFFICE_PATH`, con un perfil LibreOffice exclusivo y no reutilizable para
  esa conversión dentro de `.tmp/job-up-lo/<id-ejecucion>/profile`; el DOCX
  debe copiarse al staging corto `.tmp/job-up-lo/<id-ejecucion>/` y el PDF
  validado debe volver a `.tmp/job-up-generador/<id-candidatura>/<ejecucion>/`.
  Esta ruta corta es obligatoria en Windows porque la ruta larga de la
  candidatura puede provocar el código `3221226505`. No debe convertir el
  CV y la carta en una misma invocación ni compartir perfil entre ambos,
  mediante
  `--headless`, `--nologo`, `--nodefault`, `--nofirststartwizard`,
  `--norestore`, `-env:UserInstallation=file:///...` y
  `--convert-to pdf`. No debe forzar `HOME` o `XDG_CONFIG_HOME` en Windows.
- No se debe reutilizar `render_docx.py` como mecanismo de conversión del
  generador: en este entorno ejecuta `soffice` por nombre y puede quedarse
  bloqueado. La verificación PDF se realizará después con las herramientas de
  PDF y el renderizador Poppler disponible.
- Comprueba que cada PDF existe, no está vacío, puede abrirse y puede
  renderizarse antes de continuar con el veredicto. Si falla cualquier fase
  del generador —JSON, sustitución, DOCX, LibreOffice o PDF—, detén la
  ejecución actual, no abras una segunda instancia ni repitas automáticamente
  y registra el diagnóstico en
  `boveda-entrevista-profesional/busqueda-empleo/registros-generacion/`.

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
- `datos-generacion.json` no existe, no es accesible, no es JSON válido o no
  cumple el contrato de la plantilla;
- falta `RUTA_PROYECTO`, `SOFFICE_PATH`, una plantilla, la fotografía o una
  salida requerida;
- el generador Python devuelve un error o no produce los cinco artefactos;
- LibreOffice no puede convertir un DOCX, no responde o produce un PDF vacío.

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
- [ ] Existe un `datos-generacion.json` válido y conforme a su plantilla.
- [ ] El generador Python produjo los cinco artefactos esperados.
- [ ] La conversión utilizó la ruta absoluta validada de `soffice.com` y un
      perfil único por documento.
- [ ] Los PDF existen, tienen contenido y se renderizaron correctamente.
- [ ] Destinatario, fecha, asunto, localidad, saludo y despedida están
      confirmados o resueltos mediante los fallbacks permitidos.
- [ ] El estado final es `pendiente_de_aprobacion`.
- [ ] No se ha enviado ninguna candidatura ni se ha contactado con nadie.
