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

## 3. Análisis de entrada y descarte

1. Copiar el texto completo de la oferta en una instancia de [[TEMPLATE_ANALISIS_OFERTA]].
2. Extraer literalmente o resumir con fidelidad las funciones y los requisitos.
3. Mostrar siempre, aunque falten o resulten desfavorables, estos campos: salario, modalidad, zona geográfica, jornada y contrato.
4. No excluir automáticamente una oferta por salario, modalidad, zona, jornada o contrato. Estos datos se presentan para revisión humana.
5. Clasificar el encaje profesional como:
   - `fuerte`: existe correspondencia factual clara con el perfil y los logros disponibles;
   - `parcial`: existe correspondencia útil, pero también faltan requisitos o evidencias relevantes;
   - `sin_encaje`: no existe respaldo factual suficiente para construir una candidatura honesta.
6. Descartar automáticamente solo las ofertas clasificadas como `sin_encaje`. Registrar el descarte y su fundamento factual en [[seguimiento-candidaturas]].

## 4. Selección factual

Para cada oferta `fuerte` o `parcial`:

1. Seleccionar exactamente un perfil principal y un perfil secundario de [[datos-core-busqueda]].
2. Elegir entre tres y cinco logros del banco de la matriz que respondan directamente a la oferta.
3. Registrar la relación entre cada logro y las funciones o requisitos de la oferta.
4. Excluir cualquier afirmación que no pueda vincularse a un hecho concreto de la matriz.
5. Comprobar que cada frase del CV y de la carta de presentación pueda rastrearse hasta [[datos-core-busqueda]]. La cercanía semántica o una palabra clave de la oferta no sustituyen la evidencia.

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
3. Realizar la revisión factual completa contra [[datos-core-busqueda]].
4. Usar la skill `documents:documents` para crear los archivos DOCX.
5. Usar la skill `pdf:pdf` para exportar los DOCX a PDF y verificar los PDF.
6. Comprobar visualmente tanto los DOCX como los PDF: estructura, cortes, desbordamientos, legibilidad, datos y coherencia entre formatos.
7. Registrar en [[TEMPLATE_CANDIDATURA]] y [[seguimiento-candidaturas]] las rutas del CV DOCX, CV PDF, carta DOCX y carta PDF.
8. Marcar la candidatura como `pendiente_de_aprobacion`.

La existencia de DOCX y PDF verificados no autoriza el envío. La aprobación y cualquier actuación posterior corresponden a una fase distinta y requieren intervención humana explícita.

## 7. Revisión humana y salida de fase 1

Antes de cerrar la preparación, una persona debe revisar:

- la clasificación de encaje y los motivos de cualquier descarte;
- los perfiles y los tres a cinco logros seleccionados;
- la trazabilidad de cada frase del CV y de la carta;
- los límites sobre decisiones colegiadas, estudios, idiomas y tecnología histórica;
- el uso autorizado de datos privados;
- la presentación visual y las rutas registradas de los cuatro documentos.

La salida válida de fase 1 es una candidatura documentada, con sus archivos preparados, sus rutas registradas y estado `pendiente_de_aprobacion`. El playbook no autoriza enviar candidaturas ni realizar un envío sin aprobación humana.

## 8. Lista de control final

- [ ] La entrada conserva el texto completo de la oferta.
- [ ] El encaje es `fuerte` o `parcial`; solo `sin_encaje` se descarta automáticamente.
- [ ] Salario, modalidad, zona, jornada y contrato están visibles y no actuaron como filtros automáticos.
- [ ] Hay un perfil principal, uno secundario y de tres a cinco logros factuales.
- [ ] Cada frase del CV y de la carta se rastrea hasta [[datos-core-busqueda]].
- [ ] Los verbos de acción de la persona candidata están en primera persona; la tercera persona solo describe a otros sujetos.
- [ ] No queda ningún bloqueo obligatorio abierto.
- [ ] Los DOCX y los PDF se comprobaron visualmente.
- [ ] Las cuatro rutas documentales están registradas.
- [ ] El estado final es `pendiente_de_aprobacion`.
- [ ] No se ha realizado ni autorizado ningún envío.
