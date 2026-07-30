---
id: 2026-07-30-generador-documental-candidaturas-oferta-design
titulo: Diseño del generador documental para candidaturas por oferta
tipo: especificacion_de_diseno
estado: aprobado_para_revision_documental
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

## 4. Flujo de uso

La IA creará, dentro de la carpeta de cada candidatura, un fichero llamado:

```text
datos-generacion.json
```

El script se invocará pasando su ruta:

```text
python generar_candidatura.py ruta/al/datos-generacion.json
```

La ruta recibida podrá ser relativa o absoluta para la invocación, pero deberá resolverse de forma inequívoca. El contenido del JSON usará rutas relativas a `RUTA_PROYECTO`.

El fichero `.env` situado junto al script contendrá la raíz absoluta del proyecto:

```env
RUTA_PROYECTO=C:\Users\gusve\Documents\Apps\carrera-profesional-ai-first
```

Si el `.env`, la variable o la ruta del proyecto no existen o no son válidos, el script se detendrá antes de escribir.

## 5. Contrato de `datos-generacion.json`

La estructura estará definida por:

```text
boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_DATOS_GENERACION_CANDIDATURA.json
```

La skill `job-up-candidatura-oferta` indicará a la IA cuándo debe crear el JSON y deberá remitir a esta plantilla.

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
    "[CONTACTO]": "...",
    "[PERFIL]": "...",
    "[EXPERIENCIA 1]": "...",
    "[FORMACION 1]": "..."
  },
  "carta": {
    "[FECHA]": "...",
    "[ASUNTO]": "...",
    "[SALUDO]": "...",
    "[PARRAFO 1]": "...",
    "[PARRAFO 2]": "...",
    "[DESPEDIDA]": "..."
  },
  "latex": {
    "[NOMBRE]": "...",
    "[TITULAR]": "...",
    "[PERFIL]": "...",
    "[EXPERIENCIA 1]": "...",
    "[FORMACION 1]": "..."
  }
}
```

Los nombres de los campos de contenido coincidirán literalmente con los marcadores definidos en cada plantilla, incluidos corchetes, espacios y mayúsculas. No habrá una capa de traducción implícita entre nombres de JSON y marcadores.

La ruta de la fotografía será obligatoria. La IA la tomará de `boveda-entrevista-profesional/busqueda-empleo/fuentes/datos-privados-candidatura.md` y la copiará al campo `entradas.foto`. El script no buscará la imagen por nombre.

## 6. Validación previa

El orden de validación será:

1. comprobar que `datos-generacion.json` existe y es accesible;
2. comprobar que su contenido es JSON válido;
3. cargar y validar `RUTA_PROYECTO` desde `.env`;
4. comprobar que `id_candidatura` y `ruta_candidatura` son coherentes;
5. consultar `seguimiento/seguimiento-candidaturas.md`;
6. decidir si el estado permite sobrescribir;
7. inspeccionar la existencia de los documentos de salida;
8. comprobar que las rutas de salida están dentro de `ruta_candidatura`;
9. comprobar plantillas, fotografía y demás entradas;
10. comparar los marcadores de las plantillas con las claves del JSON;
11. comprobar que no faltan campos obligatorios ni existen campos desconocidos;
12. iniciar la generación solo si todas las validaciones anteriores pasan.

La ausencia de documentos de salida no será un error en una candidatura no presentada. Si una candidatura no presentada tiene algunos o todos los artefactos, se permitirá regenerarlos.

Una candidatura presentada no se modificará: el script se detendrá aunque falte alguno de los documentos esperados. Un estado ausente, desconocido o ambiguo también provocará detención.

La primera versión introducirá `en_preparacion` como estado inicial para candidaturas recién creadas. La documentación del vocabulario de estados deberá distinguirlo de `pendiente_de_aprobacion`, `detenida`, `enviada`, `rechazada`, `aprobada`, `duplicada` y `fallida`.

## 7. Generación atómica

La generación se realizará en:

```text
<RUTA_PROYECTO>/.tmp/job-up-generador/<id-candidatura>/<fecha-hora-de-ejecucion>/
```

Esta carpeta contendrá únicamente los resultados intermedios de la ejecución actual. La ruta quedará excluida expresamente de Git.

El script deberá:

1. crear la carpeta temporal de ejecución;
2. copiar o abrir las plantillas necesarias;
3. sustituir literalmente los marcadores;
4. insertar la fotografía en CV y carta;
5. convertir los DOCX a PDF mediante el método validado;
6. validar los cinco artefactos en la carpeta temporal;
7. preparar una copia de respaldo temporal de los archivos finales existentes que vayan a sobrescribirse;
8. publicar los cinco resultados en las rutas finales indicadas en el JSON;
9. si la publicación falla, restaurar los respaldos y registrar los documentos realmente publicados o restaurados;
10. limpiar la subcarpeta temporal de esa ejecución.

Si falla cualquier paso anterior a la publicación, no se publicará ningún documento nuevo ni se sobrescribirá ningún documento existente. Si falla durante la publicación, el script intentará restaurar el estado anterior mediante los respaldos temporales. La ejecución se considerará fallida aunque la restauración sea correcta, y el registro indicará el resultado real de la publicación y de la restauración. Se eliminarán únicamente los temporales de esa ejecución cuando sea posible.

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
- texto extraíble y seleccionable;
- ausencia de marcadores visibles;
- fotografía presente cuando corresponda;
- formato y paginación conformes a la salida DOCX.

### LaTeX

- archivo existente;
- texto UTF-8 válido;
- marcadores resueltos;
- campos previstos presentes;
- contenido correspondiente al JSON de la sección `latex`.

## 9. Conversión DOCX→PDF: puerta técnica previa

Antes de convertir este diseño en un plan de implementación se ejecutará una prueba técnica aislada con las dos plantillas DOCX, un JSON controlado y una fotografía de prueba.

La prueba deberá verificar:

- ruta exacta de `soffice.com`;
- uso de un perfil LibreOffice aislado;
- conversión repetible de CV y carta;
- ausencia del error `bootstrap.ini`;
- ejecución sin abrir una segunda instancia;
- existencia, apertura y renderizado de los dos PDF;
- limpieza de la carpeta temporal.

La generación PDF no se considerará resuelta por configuración teórica. Si la prueba falla, se revisará el diseño técnico antes de redactar el plan de implementación.

## 10. Registro de errores

Los errores se mostrarán en consola y se conservarán como JSON en:

```text
boveda-entrevista-profesional/busqueda-empleo/registros-generacion/
```

El nombre incluirá candidatura y fecha/hora:

```text
generacion-error-CAND-2026-017-20260730-211500.json
```

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

La ruta de los registros generados se añadirá a `.gitignore` sin ignorar necesariamente un `README.md` de documentación dentro de la carpeta.

## 11. Limpieza desde `job-up-inicia-sesion`

En cada invocación de `job-up-inicia-sesion`, la skill preparará y ejecutará una limpieza limitada a:

```text
boveda-entrevista-profesional/busqueda-empleo/registros-generacion/
```

Solo se borrarán registros JSON cuya propiedad `fecha` sea válida y tenga más de dos días. El nombre del archivo servirá para identificarlo, pero no será el criterio temporal principal.

Los registros dañados, sin `fecha` o con una fecha no interpretable no se borrarán. La skill informará al finalizar de cada archivo no eliminado, su ruta y la candidatura asociada cuando pueda identificarse.

La misma skill comprobará si quedan archivos o subcarpetas en:

```text
<RUTA_PROYECTO>/.tmp/job-up-generador/
```

Informará de los temporales no eliminados, con su ruta, candidatura identificable y fecha de modificación cuando esté disponible.

La skill deberá ampliar sus límites para permitir únicamente esta limpieza técnica adicional, sin tocar otros contenidos de `.tmp/` ni otros documentos Job-up.

## 12. Documentación que deberá actualizarse durante la implementación

- `.codex/skills/job-up-candidatura-oferta/SKILL.md`;
- `.codex/skills/job-up-inicia-sesion/SKILL.md`;
- `boveda-entrevista-profesional/busqueda-empleo/README.md`;
- `boveda-entrevista-profesional/busqueda-empleo/seguimiento/README.md`;
- `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md`;
- `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_DATOS_GENERACION_CANDIDATURA.json`;
- `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_CV_FORMATO.tex`;
- un `README.md` dentro de `boveda-entrevista-profesional/busqueda-empleo/registros-generacion/`;
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
