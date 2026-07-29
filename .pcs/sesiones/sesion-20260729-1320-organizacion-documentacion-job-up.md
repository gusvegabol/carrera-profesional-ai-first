---
id: sesion-20260729-1320-organizacion-documentacion-job-up
titulo: Definición y organización documental de Job-up
inicio: 2026-07-29 13:20
cierre: 2026-07-30 00:13
estado: cerrada
tipo: sesion
host: carrera-ai
sesion_relacionada: sesion-20260727-2109-busqueda-empleo
---

# Sesión PCS — Definición y organización documental de Job-up

## Contexto inmediato

Job-up es una rama operativa de búsqueda de empleo dentro de `carrera-ai`.
La continuidad de la rama se mantiene separada de la investigación metodológica
de entrevista y se organiza mediante sesiones PCS delimitadas para cada bloque
concreto de trabajo.

La petición de apertura de esta sesión surge para revisar si la definición de
Job-up está suficientemente explícita y, a partir de esa respuesta, determinar
la mejor forma de organizar su documentación sin mezclar estado vivo, historia
de trabajo, materiales de candidatura y documentación metodológica de Carrera
AI.

## Objetivo

Definir con mayor precisión qué es Job-up dentro del proyecto `carrera-ai`,
comprobar qué parte de esa definición ya está documentada de forma explícita y
proponer una organización documental coherente, trazable y sostenible para la
rama.

El primer bloque de trabajo debe responder, como mínimo:

- cuál es la función de Job-up dentro de `carrera-ai`;
- cuál es su alcance autorizado y cuáles son sus límites;
- qué fuentes documentales ya lo definen;
- si existe una fuente principal o si la definición está fragmentada;
- qué tipos de documentos necesita la rama y qué papel cumple cada uno.

## Capa episódica

La sesión se abre el 2026-07-29 a petición explícita de la persona responsable
para estudiar la definición y la organización documental de Job-up. Antes de
crear esta sesión se revisaron la gobernanza PCS aplicable, la entidad y la
plantilla canónicas de sesión, la decisión que creó la rama operativa, la
decisión que delimitó sus sesiones y las fuentes operativas de búsqueda de
empleo.

La revisión inicial encuentra una definición explícita, aunque distribuida:

- `DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo` define Job-up
  como una rama operativa de búsqueda de empleo dentro de Carrera AI;
- `boveda-entrevista-profesional/busqueda-empleo/README.md` y
  `INICIO_SESION_WORK.md` describen su espacio operativo, flujo y límites;
- `estado-actual.md` conserva la continuidad viva, la separación de líneas y
  los riesgos;
- las carpetas de candidaturas, ofertas, datos fuente y plantillas materializan
  el trabajo concreto de la rama.

La primera hipótesis de trabajo es que existe definición formal suficiente para
reconocer Job-up, pero no una pieza documental única que funcione como punto de
entrada conceptual y mapa de su arquitectura documental. Esta hipótesis queda
abierta a comprobación durante la sesión.

## Capa semántica

Job-up no es un nuevo producto independiente ni una redefinición de la
entrevista profesional. Es una rama operativa, subordinada al proyecto
`carrera-ai`, orientada a convertir información profesional factual en
materiales de búsqueda de empleo y candidaturas revisables para ofertas
concretas.

Sus límites ya documentados incluyen:

- no modificar por sí mismo el SPEC ni los playbooks de entrevista;
- mantener separada la investigación metodológica;
- no declarar competencias no evidenciadas;
- conservar trazabilidad factual y control de privacidad;
- requerir aprobación humana antes del envío de candidaturas;
- no autorizar por sí mismo uso de Chrome, conectores o contactos externos.

La organización documental que se proponga debe respetar la diferencia entre:

- continuidad viva de la rama;
- sesiones PCS históricas y delimitadas;
- fuentes profesionales reutilizables;
- ofertas y candidaturas concretas;
- documentos generados para cada candidatura;
- plantillas y reglas del flujo.

## Ideas y líneas cognitivas abiertas

- Determinar si conviene crear un documento principal de definición y mapa de
  Job-up, y cuál debe ser su autoridad respecto a `README.md`, el estado, las
  decisiones y la documentación operativa.
- Separar la arquitectura conceptual de Job-up de la estructura física actual
  de `boveda-entrevista-profesional/busqueda-empleo/`.
- Inventariar qué documentos son fuentes, cuáles son instrucciones, cuáles son
  registros vivos y cuáles son artefactos históricos o generados.
- Definir cómo deben relacionarse la rama, sus sesiones PCS, las candidaturas,
  las ofertas, las plantillas y el seguimiento global.
- Comprobar si el nombre `Job-up` debe aparecer de forma uniforme en títulos,
  enlaces, metadatos y puntos de entrada.

## Resultado de la sesión

La sesión comenzó identificando una definición explícita pero distribuida de
Job-up y terminó con su arquitectura documental aprobada e implantada en
`main`. Job-up conserva su carácter de rama operativa de `carrera-ai`, con un
único README funcional, estructura documental por función, histórico global y
skills de entrada adaptadas.

### Actualización — diseño aprobado

La persona responsable aprobó el diseño de organización documental el
2026-07-29. El diseño establece un `README.md` único como referencia funcional
de Job-up, una estructura por función, la conservación de `.pcs/` como capa de
gobernanza separada y el uso exclusivo de `historico/` como capa histórica
global de `carrera-ai`.

También incorpora una matriz de artefactos que distingue entre candidatura por
oferta y presentación espontánea. La especificación resultante se registra en
[[2026-07-29-organizacion-documental-job-up-design]]. La implantación posterior
se registra en la actualización de esta sesión.

La persona responsable aprobó además que el playbook de candidatura por oferta
controle su versión en frontmatter YAML. El archivo vigente tendrá un nombre
estable sin versión; solo las copias bajo `historico/` incluirán la versión en
el nombre. La propuesta conserva el contenido original de `v1.0.0` desde Git
como histórico y promueve el contenido actual a `1.1.0`.

Se identifica además que la arquitectura debe incluir las skills de entrada de
Job-up. Se acuerda renombrar `empleo-inicio-busqueda` a
`job-up-inicia-sesion` y `empleo-genera-cv-empresa` a
`job-up-genera-cv-empresa`, y añadir `job-up-candidatura-oferta` para iniciar
el flujo a partir de una URL. Esta última solo podrá vincularse a una sesión
Job-up ya abierta; no creará una sesión PCS salvo petición explícita.

Se aprobó además la simplificación de entrada: `INICIO_SESION_WORK.md` deja de
ser una fuente de entrada paralela. Sus reglas conceptuales útiles se integran
en el README, que mantendrá una capa de modelo mental y otra de uso operativo.
El detalle de ejecución del ciclo PCS quedará exclusivamente en
`job-up-inicia-sesion`; después, el documento sustituido se conservará bajo
`historico/` con su ruta de procedencia.

El análisis de activación semántica de las skills se difiere a
[[sesion-20260729-1534-activacion-semantica-skills-job-up]], creada en pausa.
No cambia todavía `allow_implicit_invocation` ni las rutas de las skills.

### Actualización — implantación integrada y verificada

La reorganización aprobada se implantó en worktrees independientes y se integró
en `main` el 2026-07-29 mediante el commit `55aaeb5` (`docs: integrar
reorganización documental de Job-up`). El árbol principal quedó limpio y pasó
la validación estructural de las tres skills:

- `job-up-inicia-sesion`;
- `job-up-genera-cv-empresa`;
- `job-up-candidatura-oferta`.

La documentación operativa quedó migrada a `fuentes/`, `proceso/plantillas/` y
`seguimiento/`. `INICIO_SESION_WORK.md` quedó únicamente en `historico/`; el
playbook vigente usa nombre estable y declara `1.1.0` en YAML, mientras que la
versión `1.0.0` se conserva en `historico/` con la versión en el nombre.

La nueva skill de candidatura por oferta acepta URL, fichero Markdown o texto
pegado; mantiene la selección humana de sesión y la autorización privada por
candidatura, y no realiza envíos ni contactos externos. Las candidaturas no
reciben versionado documental trazable. La prueba documental, los enlaces
locales, las rutas antiguas y los metadatos se verificaron después de la
integración.

## Acciones derivadas

- No se crea una acción PCS en la apertura. Solo se derivará una acción si la
  sesión identifica una tarea concreta que deba seguirse fuera de este registro
  histórico.

## Decisiones derivadas

- No se crea una decisión PCS en la apertura.
- Se mantienen vigentes:
  - [[DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo]];
  - [[DEC-20260724-1956-001-delimitar-sesiones-job-up]].

## Problemas o bloqueos

- La definición funcional y la organización documental no deben confundirse:
  mejorar la estructura no implica ampliar el alcance de Job-up.
- No debe crearse una fuente normativa nueva ni modificarse el SPEC por
  inferencia durante esta primera revisión.
- Cualquier propuesta que cambie decisiones vigentes, estado operativo o
  alcance requerirá su flujo PCS correspondiente.

## Documentos afectados

- Este registro de sesión.
- `docs/superpowers/specs/2026-07-29-organizacion-documental-job-up-design.md`.
- `README.md`.
- `.pcs/estado/estado-actual.md`.
- `.pcs/decisiones/DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo.md`.
- `.pcs/decisiones/DEC-20260724-1956-001-delimitar-sesiones-job-up.md`.
- `boveda-entrevista-profesional/busqueda-empleo/README.md`.
- `boveda-entrevista-profesional/busqueda-empleo/fuentes/`.
- `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/`.
- `boveda-entrevista-profesional/busqueda-empleo/seguimiento/seguimiento-candidaturas.md`.
- `historico/boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md`.
- `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md` y su copia histórica.
- `.codex/skills/job-up-inicia-sesion/`, `.codex/skills/job-up-genera-cv-empresa/` y `.codex/skills/job-up-candidatura-oferta/`.
- La matriz de candidaturas y los documentos existentes afectados por la actualización de rutas.

## Rehidratación futura

- **Dónde quedó el trabajo:** el diseño y el plan están implantados en `main`,
  con el commit `55aaeb5`; queda probar el comportamiento operativo de las
  skills desde el árbol principal.
- **Leer primero:** este documento; `estado-actual.md`; la decisión de creación
  de Job-up; la decisión sobre sesiones delimitadas; el README de Job-up; y el
  plan `docs/superpowers/plans/2026-07-29-organizacion-documental-job-up.md`.
- **Líneas abiertas a retomar:** ejecutar pruebas de comportamiento de entrada,
  sesión y autorización privada; la activación semántica de skills permanece
  diferida en su sesión PCS específica.
- **Riesgos de malinterpretación:** no tratar esta sesión como estado vivo ni
  convertir la hipótesis inicial en decisión o norma.
- **Siguiente gesto recomendado:** ejecutar las pruebas de comportamiento de
  las tres skills desde `main` y registrar cualquier ajuste en una nueva sesión
  PCS delimitada.

## Actualización — candidatura CAND-2026-011

El 29/07/2026 se recibió autorización explícita para utilizar, únicamente en
la candidatura de SIA MEDIA SERVICES, nombre, primer apellido, teléfono y
correo. Se generaron `cv.docx`, `cv.pdf`, `cv.tex`,
`carta-presentacion.docx`, `carta-presentacion.pdf` y
`veredicto-final-cv.md`. El veredicto establece integridad `apta`, media
orientativa 3,8 y decisión `revisar_antes_de_aprobar`. La candidatura queda
`pendiente_de_aprobacion`; no se ha enviado ni contactado con la empresa.

La conversión DOCX→PDF del entorno no fue utilizable. Los PDF se generaron
con el motor alternativo disponible y se revisaron visualmente: CV de una
página y carta de una página, sin cortes ni desbordamientos. La comprobación
estructural de DOCX confirmó la presencia exclusiva de los datos privados
autorizados; no aparecen segundo apellido, localidad privada ni LinkedIn.

Posteriormente, la empresa comunicó que la oferta de CAND-2026-011 estaba
cerrada, aunque Indeed todavía la mostraba como abierta. El expediente se
actualizó a `detenida` con `estado_oferta: cerrada`; no procede la aprobación ni
el envío.

También se preparó CAND-2026-012 para Grupo Miguel León a partir de la oferta
consultada en la pestaña activa de Indeed. La autorización de nombre, primer
apellido, correo y teléfono permitió generar el paquete completo. La atención
al cliente se incorporó como evidencia de HER-06 tras confirmar que Gustavo
resolvía reclamaciones escaladas por responsables de tienda. El veredicto es
`apta`, con media 4,0/5 y decisión `revisar_antes_de_aprobar`.

## Actualización — formato documental común para CV y carta

El 29/07/2026 se ejecutó el plan aprobado para reducir la improvisación en la
generación de documentos de candidatura. Se creó el contrato común
`GUIA_FORMATO_CV_Y_CARTA.md`, junto con las plantillas visuales
`TEMPLATE_CV_FORMATO.docx` y `TEMPLATE_CARTA_PRESENTACION_FORMATO.docx` y sus
guías Markdown de uso.

El contrato fija Calibri, la jerarquía 14/12/11/10,5 pt, los colores `#1F2937`
y `#5B6573`, el contenido narrativo justificado, una página como objetivo,
texto seleccionable y fotografía obligatoria por defecto en CV y carta. La
fotografía solo puede excluirse mediante instrucción expresa en la invocación
de la skill. La tabla de dos celdas se reserva al encabezado para distribuir
identidad y fotografía; no se usa para el contenido narrativo.

El guion de adaptación, el playbook de candidatura por oferta y las skills
`job-up-candidatura-oferta` y `job-up-genera-cv-empresa` quedaron alineados con
ese contrato. También se reforzó `email-presentacion.md` para exigir selección
explícita de módulo, fuente factual, destinatario y llamada a la acción, sin
improvisar necesidades, cultura, proyectos, contactos, logros, métricas ni
herramientas.

La validación estructural de las dos plantillas confirmó una imagen de
fotografía en cada DOCX, fuente Calibri, paleta acordada, marcadores sin datos
heredados de CAND-2026-010 y párrafos justificados. Se ejecutaron búsquedas de
rutas y referencias reales y `git diff --check` quedó limpio. No se realizó
renderizado visual porque el entorno no dispone de Word ni LibreOffice; esta
limitación queda registrada y no se declara una revisión visual completada.

La ejecución se mantiene en una rama de trabajo aislada pendiente de
consolidación en `main`. El plan y el diseño aprobado permanecen trazados en
`docs/superpowers/plans/2026-07-29-formato-documental-candidaturas.md` y
`docs/superpowers/specs/2026-07-29-formato-documental-candidaturas-design.md`.

## Actualización — verificación LibreOffice y corrección visual

La revisión posterior confirmó que LibreOffice está instalado en
`C:\Program Files\LibreOffice\program\` y que el diagnóstico de la sesión
`019faf0a-e68e-7812-96cc-856952550d44` es válido: el ejecutable directo puede
arrancar correctamente. El mensaje mostrado sobre `bootstrap.ini` aparece en
una ruta o instancia de arranque concreta; no debe interpretarse como ausencia
de LibreOffice.

Se actualizó el flujo para invocar `soffice.com` directamente, sin depender de
`PATH`, con un perfil temporal aislado y una única conversión por documento. Si
aparece el error de `bootstrap.ini`, el flujo debe detenerse y registrar el
diagnóstico, sin abrir una segunda instancia ni reintentar automáticamente.

La conversión directa de `TEMPLATE_CV_FORMATO.docx` y
`TEMPLATE_CARTA_PRESENTACION_FORMATO.docx` generó PDFs de una página. La
revisión visual detectó y corrigió un defecto de la carta: su encabezado con
nombre y fotografía no se mostraba al exportar. Tras reconstruir la carta a
partir del encabezado del CV, ambas plantillas muestran encabezado, fotografía,
contenido y pie correctamente.

## Actualización — regeneración de CAND-2026-012 con los nuevos templates

El 29/07/2026 se regeneró el paquete documental de Grupo Miguel León
(`CAND-2026-012`) usando `TEMPLATE_CV_FORMATO.docx` y
`TEMPLATE_CARTA_PRESENTACION_FORMATO.docx`. Se conservaron el análisis, el
guion y el contenido factual ya aprobado para revisión; se actualizaron
`cv.docx`, `cv.pdf`, `cv.tex`, `carta-presentacion.docx` y
`carta-presentacion.pdf`.

La fotografía de perfil se incorporó en CV y carta. No se añadió segundo
apellido, localidad privada, LinkedIn ni ningún otro dato no autorizado. La
validación confirmó una página por documento, texto seleccionable, contenido
justificado, fotografía visible y ausencia de marcadores.

La conversión DOCX→PDF se realizó con `soffice.com` y perfil temporal aislado,
sin instancias concurrentes. La revisión visual corrigió el orden de la
experiencia profesional y la composición de la formación en el CV. El estado
de la candidatura permanece `pendiente_de_aprobacion`; no se ha enviado.

## Actualización — fotografía cuadrada en templates y CAND-2026-012

Se corrigieron los templates de CV y carta para reservar la fotografía en
proporción 1:1, tomando como referencia la imagen de 270 × 270 px. La
redimensión actual modifica ancho y alto conjuntamente; no se deforma la
imagen ni se crea un hueco vertical adicional.

`CAND-2026-012` se volvió a generar desde los templates actualizados. La
revisión visual de CV y carta confirma fotografía cuadrada visible, una página
por documento, contenido sin cortes y el orden correcto de experiencia y
formación. El estado permanece `pendiente_de_aprobacion`.

## Actualización — candidaturas CAND-2026-013 a CAND-2026-015 y cierre

El 29/07/2026 se comprobó que la oferta de CAND-2026-013 ya no estaba
disponible en la web de ALDI, aunque la referencia externa todavía podía
mostrarla. El expediente se actualizó a `detenida` con la oferta marcada como
cerrada.

Para CAND-2026-014 se generó el paquete documental con los templates vigentes,
incluida la fotografía autorizada, y se presentó correctamente en el portal de
ALDI el 29/07/2026. El expediente quedó en estado `enviada`.

El 30/07/2026 se contrastaron en InfoJobs las candidaturas que figuraban como
inscritas o descartadas. CAND-2026-003 (Randstad), CAND-2026-004 (Globaenergy)
y CAND-2026-005 (Pro A Pro) quedaron confirmadas como `enviada`; CAND-2026-002
(Islas Natura) pasó a `rechazada` porque InfoJobs la mostraba como descartada.
También se creó el registro mínimo de CAND-2026-015 (Unide, Gestor de Cuentas /
Key Account Manager), al figurar como inscrita, sin generar documentación de
candidatura adicional. La oferta anónima de administrativo con conocimientos
de contabilidad no se guardó, conforme a la instrucción expresa del usuario.

Con estas comprobaciones queda cerrado este bloque de trabajo. Las nuevas
candidaturas, el seguimiento de respuestas y cualquier trabajo pendiente de
activación semántica de skills deberán abrirse en una sesión PCS nueva; el
estado operativo vivo permanece en los expedientes y en el seguimiento, no en
esta sesión histórica.

## Checklist de consolidación

- [x] La capa episódica registra el recorrido histórico relevante.
- [x] La capa semántica resume lo necesario para continuidad IA.
- [x] Las líneas cognitivas abiertas están identificadas.
- [x] Las acciones derivadas están creadas o marcadas como pendientes.
- [x] Las decisiones derivadas están creadas o marcadas como pendientes.
- [x] ESTADO_PROYECTO está actualizado o marcado como pendiente.
- [x] Los documentos afectados están listados.
- [x] La rehidratación futura permite retomar el hilo.
- [x] La sesión no contiene estado operativo vivo como única fuente.
- [x] No quedan tareas documentales abiertas dentro de este bloque.

## Trazabilidad

- **Origen:** petición explícita de abrir una sesión PCS para definir Job-up y
  organizar mejor su documentación.
- **Sesiones relacionadas:**
  `sesion-20260727-2109-busqueda-empleo`,
  `sesion-20260724-2004-candidaturas-job-up` y
  `sesion-20260722-1131-job-up`.
- **Acciones relacionadas:**
  `ACC-20260721-1651-001-activar-rama-operativa-busqueda-empleo-fase-1`.
- **Decisiones relacionadas:**
  `DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo` y
  `DEC-20260724-1956-001-delimitar-sesiones-job-up`.
- **Estado de proyecto relacionado:** `estado-actual`.
- **Cierre:** 2026-07-30. Sesión consolidada y cerrada; la continuidad
  operativa queda en los expedientes y documentos de seguimiento indicados.
