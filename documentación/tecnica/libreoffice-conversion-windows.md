# Conversión de documentos con LibreOffice en Windows

## Objetivo

Documentar la forma estable de convertir documentos Office a PDF en Windows
dentro de este proyecto, para que cualquier proceso nuevo pueda reutilizarla
sin depender del perfil interactivo ni de la resolución de ejecutables mediante
`PATH`.

## Alcance

- Conversión headless de DOCX a PDF.
- Aislamiento del perfil de LibreOffice por conversión.
- Configuración mediante `.env`.
- Validación técnica de los PDF generados.
- Tratamiento de errores y bloqueos.

## Contenido técnico

### Ejecutable

El proceso debe leer desde el `.env` situado junto al script una variable
`SOFFICE_PATH` con la ruta absoluta al ejecutable de consola `soffice.com`:

```env
SOFFICE_PATH=C:\\Program Files\\LibreOffice\\program\\soffice.com
```

No se debe ejecutar `soffice` por nombre ni depender de que LibreOffice esté
incluido en `PATH`. En el entorno validado, `soffice.com` es la opción que
permite una invocación de consola fiable.

### Perfil aislado y ruta corta de conversión

Cada conversión de un DOCX debe realizarse en una invocación separada, con un
perfil LibreOffice exclusivo y no reutilizable. Los resultados finales de la
conversión pertenecen a la carpeta temporal de la ejecución:

```text
.tmp/job-up-generador/<id-candidatura>/<ejecucion>/
```

No se debe compartir el perfil entre el CV y la carta ni convertir ambos
documentos en una única invocación. En Windows no se deben forzar las variables
`HOME` ni `XDG_CONFIG_HOME`.

La ejecución de LibreOffice utilizará además un área de staging de ruta corta
dentro de `.tmp/job-up-lo/<id-ejecucion>/`; el perfil se ubicará en su
subcarpeta `profile`. El DOCX se copiará allí antes de
invocar `soffice.com`, y el PDF se copiará de vuelta a la carpeta de ejecución
de la candidatura. Esta separación es necesaria porque LibreOffice puede
terminar con el código `3221226505` cuando el perfil y el `--outdir` están bajo
la ruta temporal larga de una candidatura en Windows. El staging se elimina
en un bloque de limpieza garantizado, tanto si la conversión termina bien como
si falla.

### Parámetros mínimos

La invocación directa de `SOFFICE_PATH` debe incluir:

```text
--headless
--nologo
--nodefault
--nofirststartwizard
--norestore
-env:UserInstallation=file:///...
--outdir <staging-corto>
--convert-to pdf
```

La ruta del perfil debe transformarse correctamente a una URI `file:///` y
ser única para esa conversión.

Cada conversión tiene un timeout de 60 segundos. Si se supera, se termina el
árbol de procesos de Windows, se comprueba que no quedan descendientes y se
registra el diagnóstico. No se abre una segunda instancia ni se reintenta
automáticamente.

### Verificación

El proceso no considerará resuelta la conversión solo porque LibreOffice
devuelva código de salida correcto. Debe comprobar, para cada PDF:

- que existe y no está vacío;
- que puede abrirse como PDF;
- que contiene páginas válidas;
- que puede renderizarse para comprobar visualmente el resultado;
- que no se ha validado por error un PDF antiguo.

La verificación puede apoyarse en Poppler o PDFium (`pypdfium2`) disponibles en
el entorno. `render_docx.py` no debe utilizarse como mecanismo de conversión
del generador porque en este entorno ejecuta `soffice` por nombre y puede
quedarse bloqueado.

### Errores

Si LibreOffice devuelve un error, no produce el PDF o queda bloqueado, el
proceso debe detener la ejecución actual, registrar el diagnóstico y no abrir
una segunda instancia ni repetir automáticamente. Una nueva ejecución manual
solo se permite después de corregir la entrada o la configuración.

## Decisiones o reglas clave

- La ruta del ejecutable es absoluta y se configura mediante `SOFFICE_PATH`.
- Se utiliza `soffice.com`, no `soffice` resuelto mediante `PATH`.
- Cada DOCX tiene una conversión y un perfil aislado propios.
- No se fuerzan `HOME` ni `XDG_CONFIG_HOME` en Windows.
- La existencia y el renderizado correcto del PDF son requisitos de éxito.
- Los fallos detienen la ejecución y no provocan reintentos automáticos.
- Los temporales se limitan a la subcarpeta de ejecución dentro de `.tmp/`.
- El staging corto de LibreOffice se limita a `.tmp/job-up-lo/` y se elimina
  siempre al terminar cada conversión.

## Referencias

- `docs/superpowers/specs/2026-07-30-generador-documental-candidaturas-oferta-design.md`
- `.codex/skills/job-up-candidatura-oferta/SKILL.md`
- `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/GUIA_FORMATO_CV_Y_CARTA.md`
