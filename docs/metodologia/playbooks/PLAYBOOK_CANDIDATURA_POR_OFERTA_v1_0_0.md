# Playbook de candidatura por oferta v1.0.0

## 1. Propósito y alcance

Este playbook convierte el texto completo de una oferta en un CV y una carta de presentación adaptados, revisables y trazables. Es una rama operativa de búsqueda de empleo: consume evidencias ya documentadas y no modifica la metodología de investigación de la entrevista profesional.

La fase 1 termina con los documentos preparados y la candidatura en estado `pendiente_de_aprobacion`. No incluye enviar candidaturas, completar formularios ni remitir documentos sin aprobación humana.

## 2. Entradas y artefactos de trabajo

La entrada obligatoria es el texto completo de la oferta. No se inicia el análisis a partir de un resumen, un título de puesto o una lista parcial de requisitos.

El proceso utiliza:

- [[datos-core-busqueda]] como matriz factual y fuente única de evidencias profesionales;
- [[datos-privados-candidatura]] como ficha privada, solo cuando su uso esté autorizado;
- [[seguimiento-candidaturas]] como registro de estado y rutas documentales;
- [[TEMPLATE_ANALISIS_OFERTA]] para registrar el análisis;
- [[TEMPLATE_CANDIDATURA]] para documentar la selección factual, los bloqueos y los archivos producidos.
- [[TEMPLATE_GUION_ADAPTACION_CV]] para fijar el enfoque narrativo antes de generar los documentos.
- [[TEMPLATE_VEREDICTO_FINAL_CV]] para documentar la revisión de integridad, calidad y decisión antes de la aprobación humana.

## 3. Análisis de entrada y descarte

1. Copiar el texto completo de la oferta en una instancia de [[TEMPLATE_ANALISIS_OFERTA]].
2. Extraer literalmente o resumir con fidelidad las funciones y los requisitos.
3. Extraer las palabras clave literales que probablemente utilicen un ATS o la persona reclutadora.
4. Clasificar el nivel del puesto (auxiliar, técnico, responsable o dirección) y compararlo con el nivel de la trayectoria disponible.
5. Mostrar siempre, aunque falten o resulten desfavorables, estos campos: salario, modalidad, zona geográfica, jornada y contrato.
6. No excluir automáticamente una oferta por salario, modalidad, zona, jornada o contrato. Estos datos se presentan para revisión humana.
7. Clasificar el encaje profesional como:
   - `fuerte`: existe correspondencia factual clara con el perfil y los logros disponibles;
   - `parcial`: existe correspondencia útil, pero también faltan requisitos o evidencias relevantes;
   - `sin_encaje`: no existe respaldo factual suficiente para construir una candidatura honesta.
8. Descartar automáticamente solo las ofertas clasificadas como `sin_encaje`. Registrar el descarte y su fundamento factual en [[seguimiento-candidaturas]].

## 4. Selección factual

Para cada oferta `fuerte` o `parcial`:

1. Seleccionar exactamente un perfil principal y un perfil secundario de [[datos-core-busqueda]].
2. Elegir entre tres y cinco logros del banco de la matriz que respondan directamente a la oferta.
3. Registrar la relación entre cada logro y las funciones o requisitos de la oferta.
4. Excluir cualquier afirmación que no pueda vincularse a un hecho concreto de la matriz.
5. Comprobar que cada frase del CV y de la carta de presentación pueda rastrearse hasta [[datos-core-busqueda]]. La cercanía semántica o una palabra clave de la oferta no sustituyen la evidencia.
6. Marcar expresamente los requisitos no acreditados o solo parcialmente acreditados; no completarlos por inferencia.

### Guion narrativo previo

Antes de redactar el CV se debe completar [[TEMPLATE_GUION_ADAPTACION_CV]]. El guion debe fijar el titular, el resumen, las competencias prioritarias, las organizaciones y logros que ocuparán el primer plano y el contenido que no debe dominar el documento.

La calidad de la adaptación se mide por relevancia, no por cantidad de trayectoria reproducida. El CV puede agrupar o dejar fuera etapas históricas cuando no respondan a la oferta. Una candidatura anterior puede servir como referencia visual, pero nunca como fuente factual ni como fuente automática de enfoque: todo contenido heredado debe validarse de nuevo contra el guion, el análisis y [[datos-core-busqueda]].

Para puestos auxiliares o técnicos cuando exista riesgo de sobrecualificación, el guion debe traducir la experiencia a tareas, organización, documentación y resultados operativos, manteniendo los cargos históricos literalmente. Puede añadirse una frase breve de motivación orientada al encaje con el puesto, sin ocultar la trayectoria ni inventar una experiencia distinta.

La redacción debe conservar estos límites:

- las decisiones colegiadas no se atribuyen a la persona como decisiones individuales;
- los estudios no finalizados se presentan expresamente como no finalizados;
- el nivel de idiomas no se eleva por encima del documentado;
- la tecnología histórica no se presenta como dominio actual sin confirmación nueva.

### Transformación de voz narrativa

[[datos-core-busqueda]] registra los hechos en tercera persona y no se copia literalmente en los documentos de candidatura.

- Redactar en primera persona cada acción cuyo sujeto sea la persona candidata: «Diseñé», «Automaticé», «Clasifiqué».
- Mantener la tercera persona cuando el sujeto sea distinto, por ejemplo: «el personal pasó a recibir…» o «las decisiones correspondían al Consejo de Dirección».
- Cambiar únicamente la voz gramatical; no ampliar responsabilidades, métricas, titulaciones, tecnologías ni resultados.

## 5. Bloqueos obligatorios

Detener la producción documental y registrar el motivo cuando ocurra cualquiera de estas condiciones:

- falta información factual necesaria para sostener una afirmación relevante;
- la oferta exige una capacidad no documentada en [[datos-core-busqueda]];
- existe una contradicción de fechas sin resolver;
- la información de [[datos-privados-candidatura]] no está autorizada para esa candidatura.

Un bloqueo no se resuelve mediante suposición, ampliación retórica ni inferencia desde el cargo. La candidatura queda `detenida` hasta que una revisión humana aporte o confirme la información necesaria.

## 6. Producción documental

Una vez resueltos los bloqueos, seguir este orden fijo:

1. Revisar cada logro seleccionado: identificar su sujeto, usar primera persona si la acción corresponde a la persona candidata y conservar tercera persona solo para otros sujetos.
2. Preparar el texto del CV y de la carta de presentación.
   El CV se genera en una sola página siempre que la legibilidad lo permita, con estructura compatible con ATS: encabezados estándar, texto seleccionable, viñetas y sin tablas, columnas, gráficos ni fotografía.
   En todo CV y carta, establecer el idioma de revisión en Español (España), no usar fuente inferior a 10 pt y justificar el texto de contenido; los títulos, saludos, despedidas y datos de contacto pueden conservar su alineación funcional.
3. Realizar la revisión factual completa contra [[datos-core-busqueda]].
4. Ejecutar una revisión de arrastre: comparar titular, resumen, competencias y experiencia con el guion de adaptación y comprobar que no aparecen el perfil dominante ni afirmaciones de otra candidatura.
5. Usar la skill `documents:documents` para crear los archivos DOCX.
6. Usar la skill `pdf:pdf` para exportar los DOCX a PDF y verificar los PDF.
7. Comprobar visualmente tanto los DOCX como los PDF: estructura, cortes, desbordamientos, legibilidad, datos y coherencia entre formatos.
8. Completar [[TEMPLATE_VEREDICTO_FINAL_CV]] sobre el CV ya generado: comprobar integridad, puntuar los cinco criterios, registrar evidencia y mejoras, calcular la decisión sin usar la media como puerta y corregir el CV si la decisión es `corregir_antes_de_revisar`.
9. Si una investigación contextual autorizada justifica ajustar el lenguaje corporativo, aplicar el mismo criterio de tono al CV y a la carta de presentación. No se adapta solo uno de los dos documentos; la adaptación no puede añadir hechos, funciones, tecnologías, métricas o resultados no acreditados.
10. Al crear cada artefacto, actualizar el índice «Documentos de la candidatura» de [[TEMPLATE_CANDIDATURA]]. Debe enumerar todos los documentos operativos existentes en la carpeta —análisis, guion, veredicto, informe de empresa y preparación de entrevista cuando exista, CV y carta en DOCX y PDF—, no solo el CV y la carta. Si posteriormente se añade, sustituye o elimina cualquier documento, actualizar de nuevo ese índice y comprobar que no queden enlaces a archivos inexistentes. Las capturas y otros archivos internos de control visual no forman parte del índice.
11. Registrar en [[TEMPLATE_CANDIDATURA]] y [[seguimiento-candidaturas]] el estado, el enlace al veredicto y su decisión.
12. Marcar la candidatura como `pendiente_de_aprobacion` solo cuando la decisión del veredicto no sea `corregir_antes_de_revisar`.

La existencia de DOCX y PDF verificados no autoriza el envío. La aprobación y cualquier actuación posterior corresponden a una fase distinta y requieren intervención humana explícita.

## 7. Revisión humana y salida de fase 1

Antes de cerrar la preparación, una persona debe revisar:

- la clasificación de encaje y los motivos de cualquier descarte;
- los perfiles y los tres a cinco logros seleccionados;
- la trazabilidad de cada frase del CV y de la carta;
- los límites sobre decisiones colegiadas, estudios, idiomas y tecnología histórica;
- el uso autorizado de datos privados;
- el resultado de integridad, las notas y las mejoras del veredicto final del CV;
- la autorización y las URL registradas de cualquier investigación contextual posterior;
- la presentación visual de los documentos y que el índice de [[TEMPLATE_CANDIDATURA]] enumere todos los artefactos operativos de la carpeta sin enlaces rotos.

La salida válida de fase 1 es una candidatura documentada, con sus archivos preparados, sus rutas registradas y estado `pendiente_de_aprobacion`. El playbook no autoriza enviar candidaturas ni realizar un envío sin aprobación humana.

## 8. Lista de control final

- [ ] La entrada conserva el texto completo de la oferta.
- [ ] El encaje es `fuerte` o `parcial`; solo `sin_encaje` se descarta automáticamente.
- [ ] Salario, modalidad, zona, jornada y contrato están visibles y no actuaron como filtros automáticos.
- [ ] Hay un perfil principal, uno secundario y de tres a cinco logros factuales.
- [ ] Cada frase del CV y de la carta se rastrea hasta [[datos-core-busqueda]].
- [ ] Existe un guion de adaptación y el documento no arrastra el enfoque ni el contenido factual de otra candidatura.
- [ ] El titular, el resumen, las competencias y la experiencia priorizada responden a las funciones de la oferta.
- [ ] Las palabras clave integradas están respaldadas por el core y los requisitos no acreditados aparecen identificados.
- [ ] Si existe riesgo de sobrecualificación, el lenguaje prioriza tareas y resultados operativos sin falsear los cargos.
- [ ] Existe un [[TEMPLATE_VEREDICTO_FINAL_CV]], la integridad es `apta` y no quedan incidencias sin corregir.
- [ ] Las notas de 1 o 2 se corrigieron antes de pasar a revisión humana.
- [ ] La investigación contextual, si existe, fue autorizada para esta candidatura y conserva sus URL propuestas y utilizadas.
- [ ] Si la investigación contextual motivó un ajuste de lenguaje, CV y carta aplican el mismo criterio de tono sin introducir afirmaciones no acreditadas.
- [ ] Los verbos de acción de la persona candidata están en primera persona; la tercera persona solo describe a otros sujetos.
- [ ] No queda ningún bloqueo obligatorio abierto.
- [ ] Los DOCX y los PDF se comprobaron visualmente.
- [ ] El índice de [[TEMPLATE_CANDIDATURA]] enumera todos los artefactos operativos existentes de la carpeta, se actualizó al crear o modificar documentos y no contiene enlaces rotos.
- [ ] El estado final es `pendiente_de_aprobacion`.
- [ ] No se ha realizado ni autorizado ningún envío.
