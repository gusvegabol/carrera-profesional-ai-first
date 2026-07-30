---
id: 2026-07-30-generador-documental-candidaturas-oferta-design
titulo: Diseño del generador documental para candidaturas por oferta
tipo: especificacion_de_diseno
estado: implementada
fecha: 2026-07-30
---

# Diseño del generador documental para candidaturas por oferta

## 1. Propósito

Crear un generador Python determinista que acelere la creación de los documentos de una candidatura por oferta y evite que el procedimiento de composición cambie entre interacciones.

El generador será una herramienta de producción documental. No será un agente de análisis, redacción, adaptación, revisión metodológica ni gestión del expediente.

## 2. Alcance de la primera versión

La primera versión se aplicará únicamente a candidaturas por oferta.

Generará exactamente estos cinco artefactos:

- `cv.docx`;
- `cv.pdf`;
- `carta-presentacion.docx`;
- `carta-presentacion.pdf`;
- `cv.tex`.

Las candidaturas espontáneas quedan fuera de esta versión. Su email de presentación y la posible equiparación posterior con el paquete documental de una candidatura por oferta se abordarán en un diseño separado.

“Exactamente cinco artefactos” significa exactamente cinco archivos que el
generador crea o sustituye en las rutas canónicas. No significa que la carpeta
de la candidatura no pueda contener análisis, guiones, veredictos, imágenes u
otros documentos operativos. El generador nunca eliminará ni modificará esos
otros archivos.

## 3. Responsabilidades y límites

### 3.1. Responsabilidad de la IA

La IA seguirá siendo responsable de:

- analizar la oferta;
- seleccionar el enfoque factual;
- redactar y adaptar el contenido;
- completar y revisar `guion-adaptacion-cv.md`;
- generar `datos-generacion.json`;
- actualizar `candidatura.md`, el veredicto y el seguimiento según el flujo Job-up.

La IA no generará el contenido de los documentos a partir de los marcadores durante la ejecución del script. Deberá entregar en el JSON todos los textos finales que se insertarán.

### 3.2. Responsabilidad del script

El script deberá:

- recibir la ruta de un `datos-generacion.json`;
- leer la ruta absoluta del proyecto desde un `.env` situado junto al script;
- resolver las rutas relativas del JSON;
- consultar el estado vivo de la candidatura;
- validar entradas, marcadores, fotografía y salidas;
- insertar literalmente los textos del JSON en las plantillas;
- incorporar la fotografía indicada;
- generar los cinco artefactos;
- validar técnicamente el resultado;
- publicar los resultados solo cuando toda la ejecución haya sido válida;
- registrar los fallos sin alterar el resto del expediente.

El script no deberá:

- analizar la oferta;
- interpretar o corregir la redacción;
- adaptar textos;
- consultar la matriz factual para completar campos;
- actualizar `candidatura.md`;
- actualizar `veredicto-final-cv.md`;
- actualizar `seguimiento-candidaturas.md`;
- enviar o compartir documentos;
- decidir si una candidatura es adecuada;
- buscar automáticamente fotografías o plantillas por nombre.

El script nunca actualizará el estado, la ficha ni el seguimiento. Si falla,
dejará intactos esos documentos y comunicará el resultado mediante consola y
registro. La skill o la IA podrán reflejar posteriormente `fallida` mediante
su propio flujo documental, pero esa transición no será automática ni
necesaria para permitir una nueva ejecución manual con `presentada: false`.

## 4. Flujo de uso

La IA creará, dentro de la carpeta de cada candidatura, un fichero llamado:

```text
datos-generacion.json
```

El script se invocará pasando su ruta:

```text
python RUTA_PROYECTO/scripts/job-up/generar_candidatura.py ruta/al/datos-generacion.json
```

La ubicación canónica del script será
`RUTA_PROYECTO/scripts/job-up/generar_candidatura.py`. El comando podrá
ejecutarse desde cualquier directorio; el script resolverá el `.env` relativo a
su propia ubicación, no al directorio de trabajo actual. La configuración de
referencia se documenta en `scripts/job-up/.env.example` y las dependencias en
`scripts/job-up/requirements.txt`.

La ruta recibida podrá ser relativa o absoluta para la invocación, pero deberá resolverse de forma inequívoca. El contenido del JSON usará rutas relativas a `RUTA_PROYECTO`.

El fichero `.env` situado junto al script contendrá la raíz absoluta del proyecto:

```env
RUTA_PROYECTO=C:\Users\gusve\Documents\Apps\carrera-profesional-ai-first
SOFFICE_PATH=C:\Program Files\LibreOffice\program\soffice.com
```

`SOFFICE_PATH` deberá apuntar al ejecutable de consola `soffice.com`, no a `soffice` resuelto mediante `PATH`.

Si el `.env`, cualquiera de las variables o sus rutas no existen o no son válidos, el script se detendrá antes de escribir.

El entorno mínimo soportado es Windows con Python 3.12 o posterior,
`python-docx`, `Pillow`, `pypdf`, `jsonschema`, LibreOffice instalado y las
herramientas PDF/Poppler o PDFium utilizadas para comprobar y renderizar los PDF. La
ausencia de una dependencia se informa como bloqueo de configuración, antes de
crear o modificar documentos.

## 5. Contrato de `datos-generacion.json`

La estructura estará definida por:

```text
boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_DATOS_GENERACION_CANDIDATURA.json
```

La skill `job-up-candidatura-oferta` indicará a la IA cuándo debe crear el JSON y deberá remitir a esta plantilla.

La plantilla es un esqueleto de trabajo y puede contener cadenas vacías. El
`datos-generacion.json` final deberá cumplir el esquema cerrado
`SCHEMA_DATOS_GENERACION_CANDIDATURA_1.0.json`; la plantilla no se valida como
una entrada final.

El JSON incluirá como mínimo:

- `schema_version`;
- `id_candidatura`;
- `ruta_candidatura`;
- `entradas`;
- `salidas`;
- `cv`;
- `carta`;
- `latex`.

Las rutas serán relativas a `RUTA_PROYECTO`.

`ruta_candidatura` deberá resolver a una carpeta situada bajo
`boveda-entrevista-profesional/busqueda-empleo/candidaturas/`, cuyo nombre
deberá comenzar por `id_candidatura` seguido, si procede, de un sufijo
descriptivo separado por `-`. Las cinco rutas de
`salidas` no serán configurables libremente: deberán resolver exactamente a
`ruta_candidatura/cv.docx`, `ruta_candidatura/cv.pdf`,
`ruta_candidatura/carta-presentacion.docx`,
`ruta_candidatura/carta-presentacion.pdf` y `ruta_candidatura/cv.tex`.

Las entradas de plantilla deberán resolver a las plantillas canónicas
indicadas por la SPEC. La fotografía será la ruta explícita autorizada en
`entradas.foto`; el script no la buscará, elegirá ni sustituirá por otra.

Ejemplo conceptual:

```json
{
  "schema_version": "1.0",
  "id_candidatura": "CAND-2026-017",
  "ruta_candidatura": "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-017-lidl-responsable-almacen-transporte",
  "entradas": {
    "template_cv": "boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_CV_FORMATO.docx",
    "template_carta": "boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_CARTA_PRESENTACION_FORMATO.docx",
    "template_latex": "boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_CV_FORMATO.tex",
    "foto": "boveda-entrevista-profesional/busqueda-empleo/foto-perfil.png"
  },
  "salidas": {
    "cv_docx": "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-017-lidl-responsable-almacen-transporte/cv.docx",
    "cv_pdf": "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-017-lidl-responsable-almacen-transporte/cv.pdf",
    "carta_docx": "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-017-lidl-responsable-almacen-transporte/carta-presentacion.docx",
    "carta_pdf": "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-017-lidl-responsable-almacen-transporte/carta-presentacion.pdf",
    "cv_tex": "boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-017-lidl-responsable-almacen-transporte/cv.tex"
  },
  "cv": {
    "[NOMBRE]": "...",
    "[TITULAR]": "...",
    "[EMAIL]": "...",
    "[TELÉFONO]": "...",
    "[LINKEDIN]": "...",
    "[PERFIL PROFESIONAL]": "...",
    "[PROPUESTA DE VALOR]": "...",
    "[EXPERIENCIA 1 CABECERA]": "...",
    "[EXPERIENCIA 1 DESCRIPCION]": "...",
    "[EXPERIENCIA 2 CABECERA]": "...",
    "[EXPERIENCIA 2 DESCRIPCION]": "...",
    "[EXPERIENCIA 3 CABECERA]": "...",
    "[EXPERIENCIA 3 DESCRIPCION]": "...",
    "[EXPERIENCIA 4 CABECERA]": "...",
    "[EXPERIENCIA 4 DESCRIPCION]": "...",
    "[EXPERIENCIA 5 CABECERA]": "...",
    "[EXPERIENCIA 5 DESCRIPCION]": "...",
    "[EXPERIENCIA 6 CABECERA]": "...",
    "[EXPERIENCIA 6 DESCRIPCION]": "...",
    "[COMPETENCIA 1]": "...",
    "[COMPETENCIA 2]": "...",
    "[COMPETENCIA 3]": "...",
    "[COMPETENCIA 4]": "...",
    "[FORMACION 1]": "...",
    "[FORMACION 2]": "...",
    "[FORMACION 3]": "...",
    "[INFORMACION ADICIONAL]": "..."
  },
  "carta": {
    "[NOMBRE]": "...",
    "[TITULAR]": "...",
    "[EMAIL]": "...",
    "[TELÉFONO]": "...",
    "[LINKEDIN]": "...",
    "[DESTINATARIO]": "...",
    "[FECHA]": "...",
    "[ASUNTO]": "...",
    "[SALUDO]": "...",
    "[APERTURA]": "...",
    "[EVIDENCIA 1]": "...",
    "[EVIDENCIA 2]": "...",
    "[ENCAJE]": "...",
    "[CIERRE]": "...",
    "[DESPEDIDA]": "...",
    "[FIRMA]": "..."
  },
  "latex": {
    "[NOMBRE]": "...",
    "[TITULAR]": "...",
    "[EMAIL]": "...",
    "[TELÉFONO]": "...",
    "[LINKEDIN]": "...",
    "[PERFIL PROFESIONAL]": "...",
    "[PROPUESTA DE VALOR]": "...",
    "[EXPERIENCIA 1 CABECERA]": "...",
    "[EXPERIENCIA 1 DESCRIPCION]": "...",
    "[EXPERIENCIA 2 CABECERA]": "...",
    "[EXPERIENCIA 2 DESCRIPCION]": "...",
    "[EXPERIENCIA 3 CABECERA]": "...",
    "[EXPERIENCIA 3 DESCRIPCION]": "...",
    "[EXPERIENCIA 4 CABECERA]": "...",
    "[EXPERIENCIA 4 DESCRIPCION]": "...",
    "[EXPERIENCIA 5 CABECERA]": "...",
    "[EXPERIENCIA 5 DESCRIPCION]": "...",
    "[EXPERIENCIA 6 CABECERA]": "...",
    "[EXPERIENCIA 6 DESCRIPCION]": "...",
    "[COMPETENCIA 1]": "...",
    "[COMPETENCIA 2]": "...",
    "[COMPETENCIA 3]": "...",
    "[COMPETENCIA 4]": "...",
    "[FORMACION 1]": "...",
    "[FORMACION 2]": "...",
    "[FORMACION 3]": "...",
    "[INFORMACION ADICIONAL]": "..."
  }
}
```

Los nombres de los campos de contenido coincidirán literalmente con los marcadores definidos en cada plantilla, incluidos corchetes, espacios y mayúsculas. No habrá una capa de traducción implícita entre nombres de JSON y marcadores.

Cuando la IA decida que no son necesarias seis experiencias, mantendrá todos
los campos del contrato y dejará vacíos los pares que no se utilicen. Por
ejemplo, si solo se incluyen tres experiencias, los pares de las experiencias
4, 5 y 6 tendrán exactamente el valor `""` tanto en `CABECERA` como en
`DESCRIPCION`.

El generador tratará una experiencia cuyo marcador `[EXPERIENCIA N CABECERA]`
esté vacío como un slot no aplicable: eliminará el párrafo completo de esa
experiencia, incluidos sus dos marcadores, el separador ` - ` y el salto de
línea final. No sustituirá los marcadores por una cadena vacía dejando un
párrafo en blanco. La pareja cabecera/descripción deberá estar vacía o
completa; una cabecera vacía con descripción no vacía será un error de
validación.

Esta misma regla se aplicará a los marcadores de experiencia de `cv.tex`; la
futura plantilla LaTeX deberá definir esos marcadores literalmente con el
mismo nombre. Cuando una pareja esté vacía, se eliminará la línea LaTeX
completa que contiene esa experiencia, incluidos el salto de línea y cualquier
separador asociado.

La ruta de la fotografía será obligatoria. La IA la tomará de `boveda-entrevista-profesional/busqueda-empleo/fuentes/datos-privados-candidatura.md` y la copiará al campo `entradas.foto`. El script no buscará la imagen por nombre.

La fotografía deberá ser un PNG o JPEG válido, de entre 1 KB y 10 MB, con
dimensiones superiores a 270 × 270 píxeles. El generador realizará un recorte
centrado a formato cuadrado solo para adaptarla al hueco, sin modificar el
archivo fuente. En cada DOCX sustituirá la única imagen situada en la celda
derecha de la cabecera de la plantilla, conservando su relación de tamaño y
posición. Si no existe exactamente un slot de imagen en esa ubicación, la
plantilla estará invalidada y la generación se detendrá.

Los marcadores de texto se buscarán sobre el texto concatenado de cada
contenedor OOXML soportado, aunque estén divididos en varios `runs`. La
implementación deberá conservar el formato de los runs de cabecera y
descripción, y soportará únicamente cuerpo principal, tablas, encabezados y
pies. Cuadros de texto, formas, hipervínculos y marcadores duplicados serán
errores de plantilla, no casos que el script deba resolver por inferencia.
Un marcador ausente, parcialmente encontrado o desconocido bloqueará la
generación. Los valores de los slots no podrán contener saltos de línea ni
caracteres de control.

La semántica de los slots distintos de experiencia será cerrada:

- `[NOMBRE]`, `[TITULAR]`, `[PERFIL PROFESIONAL]`, `[PROPUESTA DE VALOR]`,
  `[APERTURA]`, `[CIERRE]`, `[DESPEDIDA]` y `[FIRMA]` son obligatorios y no
  pueden estar vacíos;
- `[EMAIL]`, `[TELÉFONO]` y `[LINKEDIN]` pueden estar vacíos; si lo están, se
  elimina el componente de contacto sin dejar separadores sobrantes;
- competencias, formación e información adicional son opcionales; un slot
  vacío elimina su párrafo o viñeta, y si todos los slots de una sección están
  vacíos también se elimina el título de la sección;
- `[DESTINATARIO]`, `[FECHA]`, `[ASUNTO]` y `[SALUDO]` son obligatorios en la
  carta;
- `[EVIDENCIA 1]`, `[EVIDENCIA 2]` y `[ENCAJE]` son opcionales y eliminan su
  párrafo individual cuando están vacíos.

Una plantilla que no contenga un marcador obligatorio, contenga un marcador
duplicado o añada un marcador no declarado será inválida.

## 6. Validación previa

El orden de validación será:

1. comprobar que `datos-generacion.json` existe y es accesible;
2. comprobar que su contenido es JSON válido;
3. cargar y validar `RUTA_PROYECTO` desde `.env`;
4. comprobar que `id_candidatura` y `ruta_candidatura` son coherentes;
   el frontmatter debe declarar el mismo identificador mediante `id` (o
   `id_candidatura` solo durante la migración histórica);
5. consultar el estado de la candidatura en
   `seguimiento/seguimiento-candidaturas.md` y el frontmatter de
   `candidatura.md`, que debe contener `estado` y `presentada`;
6. detenerse si cualquiera de las fuentes falta, no tiene esos campos, no
   coincide con la otra o contiene un valor desconocido o ambiguo;
7. decidir si el estado permite sobrescribir;
8. inspeccionar la existencia de los documentos de salida;
9. comprobar que las rutas de salida son exactamente las cinco rutas
    canónicas de `ruta_candidatura`;
10. comprobar plantillas, fotografía y demás entradas;
11. comparar los marcadores de las plantillas con las claves del JSON;
12. comprobar que no faltan campos obligatorios ni existen campos
    desconocidos;
13. iniciar la generación solo si todas las validaciones anteriores pasan.

La ausencia de documentos de salida no será un error en una candidatura no presentada. Si una candidatura no presentada tiene algunos o todos los artefactos, se permitirá regenerarlos.

Una candidatura presentada no se modificará: el script se detendrá aunque falte alguno de los documentos esperados. Un estado ausente, desconocido o ambiguo también provocará detención.

La sobrescritura solo estará permitida cuando el frontmatter contenga
`presentada: false` y el estado no sea `duplicada`. `en_preparacion`,
`pendiente_de_aprobacion` y `fallida` exigen `presentada: false`; `detenida`
solo permite regenerar con `presentada: false`; `enviada` y `rechazada` exigen
`presentada: true`; `aprobada` puede preceder o seguir a la presentación, por
lo que siempre requiere el booleano explícito. Si el estado y `presentada` no
forman una combinación válida, el script se detendrá.

Toda ruta del JSON deberá ser relativa, usar separadores `/`, no contener
segmentos `..`, no ser una ruta UNC ni una ruta absoluta de Windows, y deberá
resolverse mediante la ruta canónica del sistema antes de comprobar su raíz
autorizada. Se rechazarán enlaces simbólicos, junctions y reparse points en
las rutas de entrada, salida, candidatura y temporales. La comprobación se
hará después de resolver la ruta, no mediante una comparación textual de
prefijos.

La primera versión usará `en_preparacion` como estado inicial para candidaturas
recién creadas. Antes de implementar el generador, el vocabulario canónico de
seguimiento deberá sustituir `preparada` por `en_preparacion` y distinguirlo de
`pendiente_de_aprobacion`, `detenida`, `enviada`, `rechazada`, `aprobada`,
`duplicada` y `fallida`. Mientras esa alineación no se haya realizado, la
validación del estado será un bloqueo y el generador no modificará la
candidatura.

## 7. Generación y publicación transaccional recuperable

La generación se realizará en:

```text
<RUTA_PROYECTO>/.tmp/job-up-generador/<id-candidatura>/<fecha-hora-de-ejecucion>/
```

Esta carpeta contendrá únicamente los resultados intermedios de la ejecución
actual, un manifiesto de publicación y, cuando proceda, copias de respaldo.
La ruta quedará excluida expresamente de Git.

La publicación no se describirá como una sustitución simultánea de los cinco
archivos, porque el sistema de archivos no ofrece esa operación para una
carpeta que también contiene otros documentos. Será una publicación
transaccional recuperable por archivo:

- se adquiere un bloqueo exclusivo por `id_candidatura` en
  `.tmp/job-up-generador/<id-candidatura>/.lock`;
- se escribe y sincroniza un `manifest.json` con el identificador de
  ejecución, fase, rutas, hashes y copias de respaldo;
- cada destino se sustituye con una operación de reemplazo atómico del sistema
  de archivos;
- después de cada reemplazo se actualiza el manifiesto;
- se verifica el conjunto publicado contra los hashes de los temporales;
- solo después de esa verificación se marca el manifiesto como `completado` y
  se eliminan respaldos y temporales.

Si una ejecución nueva encuentra un manifiesto en fase `publicando`, intentará
la recuperación usando sus respaldos. Si la recuperación no puede verificarse
completamente, se detendrá y dejará el manifiesto y los archivos para decisión
humana. No iniciará una segunda generación sobre esa candidatura.

El script deberá:

1. crear la carpeta temporal de ejecución;
2. copiar o abrir las plantillas necesarias;
3. sustituir literalmente los marcadores;
4. insertar la fotografía en CV y carta;
5. convertir los DOCX a PDF mediante la ruta absoluta de `SOFFICE_PATH` y un perfil LibreOffice único para esa conversión;
6. validar los cinco artefactos en la carpeta temporal;
7. preparar una copia de respaldo temporal de los archivos finales existentes que vayan a sobrescribirse;
8. escribir el manifiesto y publicar los cinco resultados mediante el protocolo transaccional anterior;
9. si la publicación falla, restaurar los respaldos, verificar la restauración y registrar los documentos realmente publicados o restaurados;
10. liberar el bloqueo y limpiar únicamente la subcarpeta temporal de esa ejecución.

Después de publicar, el script volverá a comprobar la existencia, tamaño, hash
y apertura de los cinco destinos. Si cualquiera difiere del temporal validado,
la ejecución será fallida y se intentará restaurar el estado anterior.

Si falla cualquier paso anterior a la publicación, no se publicará ningún documento nuevo ni se sobrescribirá ningún documento existente. Si falla durante la publicación, el script intentará restaurar el estado anterior mediante los respaldos temporales. La ejecución se considerará fallida aunque la restauración sea correcta, y el registro indicará el resultado real de la publicación y de la restauración. Se eliminarán únicamente los temporales de esa ejecución cuando sea posible. Una ejecución concurrente para la misma candidatura se rechazará antes de modificar documentos.

## 8. Criterios de salida válida

### DOCX

- paquete OOXML válido;
- apertura estructural posible con `python-docx`;
- textos esperados presentes;
- ausencia de marcadores visibles;
- fotografía embebida realmente en CV y carta;
- preservación de estilos y estructura esencial de las plantillas;
- cabecera, tipografías, alineaciones y párrafos conformes a la guía visual;
- ausencia de pies o encabezados internos de plantilla;
- ausencia de desbordamientos o páginas inesperadas.

### PDF

- archivo existente y no vacío;
- apertura válida;
- renderizado posible;
- exactamente una página para el CV y exactamente una página para la carta en
  las plantillas de la primera versión;
- texto extraíble y seleccionable;
- ausencia de marcadores visibles;
- fotografía presente cuando corresponda;
- formato y paginación conformes a la salida DOCX.

El script comprobará automáticamente existencia, tamaño, apertura, número de
páginas, texto extraíble, ausencia de marcadores y presencia de la imagen. La
comprobación estética de desbordamientos, alineación, espaciado y fidelidad
visual será una revisión humana obligatoria de la skill antes de
`pendiente_de_aprobacion`; no se presentará como una validación automática.

### LaTeX

- archivo existente;
- texto UTF-8 válido;
- marcadores resueltos;
- campos previstos presentes;
- contenido correspondiente al JSON de la sección `latex`;
- valores ya preparados por la IA para LaTeX, con los caracteres especiales
  escapados cuando corresponda; el script no redactará ni reinterpretará esos
  valores;
- estructura básica de llaves y entornos equilibrada.

El script no compilará `cv.tex` ni requerirá un compilador LaTeX: ese fichero se
genera como artefacto de texto reutilizable y no es una fuente de los PDF
finales.
El resultado de esta comprobación será `validado_estructuralmente`; una
estructura inválida bloqueará la publicación.

## 9. Conversión DOCX→PDF: puerta técnica previa — REALIZADA

La prueba técnica aislada se realizó el 2026-07-30 con las dos plantillas
DOCX, documentos reales de CV y carta, una fotografía de prueba y perfiles
LibreOffice independientes por conversión.

Resultado de la prueba:

- `SOFFICE_PATH` apunta directamente a `soffice.com` y no depende de `PATH`;
- se utiliza un perfil LibreOffice único por conversión;
- la conversión de CV y carta es repetible;
- no aparece el error `bootstrap.ini`;
- la ejecución no necesita abrir una segunda instancia;
- los PDF existen, pueden abrirse y se renderizan correctamente;
- la subcarpeta temporal de cada ejecución queda limitada al ámbito de esa
  ejecución y se limpia al finalizar cuando el entorno lo permite.

En Windows, la conversión del generador no reutilizará la invocación interna de `render_docx.py`, porque esa ruta ejecuta `soffice` por nombre y puede quedarse colgada al combinar el perfil y el entorno de ejecución. El generador invocará directamente `SOFFICE_PATH` con `--headless`, `--nologo`, `--nodefault`, `--nofirststartwizard`, `--norestore`, `-env:UserInstallation=file:///...` y `--convert-to pdf`.

La invocación completa añadirá `--outdir <staging-corto>` y recibirá un solo
DOCX por proceso. Para evitar el fallo de Windows `3221226505` observado con
rutas largas de candidatura, el generador copiará el DOCX a
`.tmp/job-up-lo/<id-ejecucion>/`, ejecutará allí LibreOffice y copiará el PDF
resultante a la carpeta temporal de la ejecución de la candidatura. El
staging corto y su perfil se eliminarán siempre al terminar esa conversión;
el PDF esperado tendrá el mismo nombre base que el DOCX. Antes de la
invocación se eliminará cualquier PDF con ese nombre y después se comprobará
su fecha de creación, tamaño y hash.

Cada proceso tendrá un timeout de 60 segundos. Si vence, se terminará el árbol
de procesos con la terminación forzada de Windows, se comprobará que no queda
ningún proceso descendiente asociado a esa ejecución y se registrará el
diagnóstico. No se abrirá una segunda instancia ni se reintentará
automáticamente. La URI del perfil se generará mediante `Path.resolve().as_uri()`
desde una ruta local ya validada; las rutas UNC, enlaces simbólicos, junctions,
reparse points y rutas que escapen de la raíz temporal serán rechazados.

Esta prueba técnica queda como referencia de implementación. La prueba
automatizada del generador deberá cubrir las mismas invariantes, pero la
puerta técnica de LibreOffice ya está cerrada.

## 10. Registro de errores

Los errores se mostrarán en consola y se conservarán como JSON en:

```text
boveda-entrevista-profesional/busqueda-empleo/registros-generacion/
```

El registro deberá cumplir
`boveda-entrevista-profesional/busqueda-empleo/registros-generacion/SCHEMA_REGISTRO_GENERACION_ERROR_1.0.json`.
Si el JSON de entrada no puede cargarse o todavía no permite conocer la
candidatura, `id_candidatura` será `null` y se conservará la entrada recibida.
El registro tendrá siempre un `execution_id` único y el resultado `fallido`.

El nombre incluirá candidatura y fecha/hora:

```text
generacion-error-CAND-2026-017-20260730-211500.json
```

El nombre incluirá también un identificador único de ejecución, o una
precisión temporal suficiente, para que dos ejecuciones de la misma candidatura
no puedan sobrescribir el mismo registro.

El registro incluirá como mínimo:

- `fecha` en ISO 8601 con zona horaria;
- estado del resultado;
- identificador de candidatura;
- fichero JSON de entrada;
- fase del fallo;
- código de error;
- campo o ruta afectada;
- mensaje;
- lista de documentos publicados;
- lista de documentos restaurados;
- lista de documentos cuya publicación o restauración no pudo completarse.

La estructura del registro será interna al script y no dependerá de un documento que la IA deba completar.

Si no se puede escribir el registro persistente, el script debe informar del
fallo en consola con la fase, el código de error y la entrada recibida. No
reintentará indefinidamente ni ocultará el error de registro.

La ruta de los registros generados se añadirá a `.gitignore` sin ignorar necesariamente un `README.md` de documentación dentro de la carpeta.

## 11. Limpieza desde `job-up-inicia-sesion`

En cada invocación de `job-up-inicia-sesion`, la skill preparará y ejecutará una limpieza limitada a:

```text
boveda-entrevista-profesional/busqueda-empleo/registros-generacion/
```

Solo se borrarán registros JSON cuya propiedad `fecha` sea válida y tenga más de dos días. El nombre del archivo servirá para identificarlo, pero no será el criterio temporal principal.

La comparación significará más de 48 horas transcurridas, usando la fecha y
hora con zona horaria de `fecha` frente al instante de la limpieza. Las fechas
futuras no se borrarán. Nunca se borrarán por antigüedad registros sin `fecha`,
con una fecha inválida ni los README o esquemas de documentación de la
carpeta.

Los registros dañados, sin `fecha` o con una fecha no interpretable no se borrarán. La skill informará al finalizar de cada archivo no eliminado, su ruta y la candidatura asociada cuando pueda identificarse.

La misma skill comprobará si quedan archivos o subcarpetas en:

```text
<RUTA_PROYECTO>/.tmp/job-up-generador/
<RUTA_PROYECTO>/.tmp/job-up-lo/
```

Informará de los temporales no eliminados, con su ruta, candidatura identificable y fecha de modificación cuando esté disponible.

No se tocará ni eliminará una carpeta temporal cuyo bloqueo de ejecución siga
activo. Una carpeta sin bloqueo activo se considerará huérfana y se informará
con su ruta, candidatura y fecha; la eliminación manual quedará a decisión de
la persona usuaria.

La skill deberá ampliar sus límites para permitir únicamente esta inspección
técnica adicional, sin tocar otros contenidos de `.tmp/` ni otros documentos
Job-up.

## 12. Documentación que deberá actualizarse durante la implementación

- `scripts/job-up/generar_candidatura.py`;
- `scripts/job-up/.env.example` y `scripts/job-up/requirements.txt`;
- `.codex/skills/job-up-candidatura-oferta/SKILL.md`;
- `.codex/skills/job-up-inicia-sesion/SKILL.md`;
- `boveda-entrevista-profesional/busqueda-empleo/README.md`;
- `boveda-entrevista-profesional/busqueda-empleo/seguimiento/README.md`;
- `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md`;
- `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_DATOS_GENERACION_CANDIDATURA.json`;
- `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/SCHEMA_DATOS_GENERACION_CANDIDATURA_1.0.json`;
- `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_CV_FORMATO.docx` y su guía Markdown;
- `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_CARTA_PRESENTACION_FORMATO.docx` y su guía Markdown;
- `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_CV_FORMATO.tex`;
- un `README.md` dentro de `boveda-entrevista-profesional/busqueda-empleo/registros-generacion/`;
- `boveda-entrevista-profesional/busqueda-empleo/registros-generacion/SCHEMA_REGISTRO_GENERACION_ERROR_1.0.json`;
- `docs/superpowers/tests/2026-07-30-generador-documental-candidaturas-oferta.md`;
- `.gitignore`.

La actualización del playbook será acotada: documentará que la producción de los cinco artefactos se realiza mediante el generador, sin cambiar el análisis, la adaptación, el veredicto, la aprobación humana ni el seguimiento.

## 13. Fuera de alcance y evolución posterior

Quedan fuera de esta especificación:

- candidaturas espontáneas;
- generación de emails de presentación;
- modificación automática de fichas, veredictos o seguimiento;
- envío o contacto externo;
- búsqueda automática de fotografías;
- análisis semántico del JSON o de los documentos;
- reparación automática de campos incompletos;
- limpieza automática de registros que no puedan interpretarse.

La futura equiparación de candidaturas espontáneas se diseñará después de validar el generador con candidaturas por oferta.

## 13.1. Precondiciones de migración antes de ejecutar — CUMPLIDAS

La migración documental explícita se completó el 2026-07-31 antes de procesar
una candidatura real con el generador:

- `seguimiento/seguimiento-candidaturas.md` debe tener una columna
  `presentada` con valor YAML booleano `true` o `false` en todas las filas;
- cada `candidatura.md` que vaya a procesarse debe tener en su frontmatter
  `estado` y `presentada`, también como booleano estructurado;
- el identificador, el estado y `presentada` de ambas fuentes deben coincidir;
- las candidaturas históricas sin ese dato no se pueden completar por
  inferencia a partir de `observaciones`, nombres de archivos o existencia de
  documentos: se dejan bloqueadas hasta decisión humana;
- la primera fixture de integración debe ser una candidatura por oferta nueva,
  no presentada, con estado `en_preparacion` y sin artefactos finales.

La migración no la realiza el generador: queda registrada como cambio
documental separado. La validación estructural confirmó tres candidaturas
regenerables (`presentada: false`) y catorce candidaturas bloqueadas
(`presentada: true`). La prueba de integración continúa usando una fixture
sintética para no modificar candidaturas reales.

## 14. Puntos de control para dar por implementada la SPEC

La SPEC no se considerará implementada hasta que todos los controles de esta
sección estén marcados y exista evidencia verificable para cada uno. El estado
inicial de esta lista refleja el trabajo pendiente de implementación; la puerta
técnica de LibreOffice ya está superada.

### Contrato y configuración

- [x] Existe el script generador y acepta como entrada la ruta de
  `datos-generacion.json`.
- [x] El script está en `scripts/job-up/generar_candidatura.py` y funciona
  aunque el comando se ejecute desde otro directorio.
- [x] Existe `TEMPLATE_DATOS_GENERACION_CANDIDATURA.json` y sus claves
  coinciden literalmente con los marcadores de las plantillas.
- [x] Existe y se valida `SCHEMA_DATOS_GENERACION_CANDIDATURA_1.0.json` con
  un esquema cerrado y reglas de tipos, rutas y versión.
- [x] El contrato contiene las seis parejas de experiencia para el CV DOCX y
  para `cv.tex`, además de los campos de carta, formación y competencias que
  correspondan.
- [x] Los marcadores del JSON de carta coinciden literalmente con
  `[NOMBRE]`, `[TITULAR]`, `[EMAIL]`, `[TELÉFONO]`, `[LINKEDIN]`,
  `[DESTINATARIO]`, `[FECHA]`, `[ASUNTO]`, `[SALUDO]`, `[APERTURA]`,
  `[EVIDENCIA 1]`, `[EVIDENCIA 2]`, `[ENCAJE]`, `[CIERRE]`, `[DESPEDIDA]` y
  `[FIRMA]`.
- [x] El `.env` situado junto al script contiene `RUTA_PROYECTO` y
  `SOFFICE_PATH`, y ambas rutas se validan antes de escribir.

### Validación y seguridad de publicación

- [x] El generador valida JSON, rutas, plantillas, fotografía, marcadores y
  salidas antes de iniciar la generación.
- [x] Consulta el seguimiento y solo sobrescribe cuando el estado de la
  candidatura lo permite.
- [x] El vocabulario de seguimiento usa `en_preparacion` como estado inicial
  y ya no contiene `preparada` como sinónimo ambiguo.
- [x] Compara el estado del seguimiento con el frontmatter de la candidatura
  cuando ambas fuentes existan y se detiene si difieren.
- [x] Una candidatura presentada nunca se modifica, aunque falten documentos.
- [x] Una candidatura no presentada sin documentos puede generarse, y una con
  documentos existentes puede sobrescribirse conforme al seguimiento.
- [x] La publicación es transaccional por archivo, puede restaurar los
  documentos anteriores mediante el manifiesto y recupera ejecuciones
  interrumpidas.
- [x] Una segunda ejecución simultánea para la misma candidatura se detiene por
  el bloqueo exclusivo.
- [x] Las cinco rutas de salida son exactamente los nombres canónicos dentro
  de `ruta_candidatura`.

### Contenido y documentos generados

- [x] El script solo sustituye datos del JSON y no redacta ni adapta textos.
- [x] La fotografía autorizada se incorpora en los documentos previstos.
- [x] Las plantillas contienen exactamente un slot estructural de fotografía
  en la celda derecha de la cabecera y el generador lo sustituye sin buscar
  imágenes por nombre.
- [x] Las plantillas están en UTF-8 válido, no contienen caracteres `�` y no
  contienen pies, encabezados ni textos internos de instrucciones.
- [x] Los slots de experiencia no utilizados con valor `""` eliminan el
  párrafo completo, sin dejar líneas en blanco, tanto en DOCX como en `cv.tex`.
- [x] Una ejecución correcta produce exactamente `cv.docx`, `cv.pdf`,
  `carta-presentacion.docx`, `carta-presentacion.pdf` y `cv.tex`.
- [x] Los cinco artefactos se validan en la carpeta temporal antes de
  publicarse en sus rutas finales.

### Conversión PDF y fallos

- [x] La puerta técnica de LibreOffice está superada mediante la prueba
  aislada documentada en la sección 9.
- [x] La implementación usa una invocación separada y un perfil exclusivo por
  DOCX, y no reutiliza `render_docx.py` para convertir.
- [x] Cada PDF existe, no está vacío, puede abrirse y contiene la fotografía;
      la revisión visual/renderizado Poppler o PDFium sigue siendo un control humano.
- [x] `cv.tex` supera la validación estructural sin requerir un compilador
  LaTeX; no se convierte a PDF.
- [x] Cualquier error genera un registro JSON con nombre de candidatura y
  fecha/hora y un identificador único de ejecución, incluyendo `fecha` ISO
  8601 con zona horaria.
- [x] Los errores detienen la ejecución actual y no provocan reintentos
  automáticos ni una segunda instancia de LibreOffice.
- [x] La conversión aplica el timeout de 60 segundos, termina el árbol de
  procesos y comprueba que no quedan procesos residuales.
- [x] La limpieza elimina únicamente la subcarpeta temporal de la ejecución y
  deja constancia de los temporales que no pueda borrar.

### Integración documental y prueba final

- [x] Las skills, el playbook, los README, las plantillas y `.gitignore` de la
  sección 12 están actualizados.
- [x] Existe una prueba de integración con una candidatura por oferta no
  presentada que verifica generación, sobrescritura permitida, los cinco
  artefactos y los PDF.
- [x] Existe una prueba de fallo que verifica detención, registro de error,
  ausencia de publicación parcial y restauración cuando corresponda.
- [x] La matriz reproducible de
  `docs/superpowers/tests/2026-07-30-generador-documental-candidaturas-oferta.md`
  se ejecuta con fixtures aislados y todas sus filas pasan.
- [x] La candidatura de prueba queda en `pendiente_de_aprobacion` y no se
  realiza ningún envío ni contacto externo.
