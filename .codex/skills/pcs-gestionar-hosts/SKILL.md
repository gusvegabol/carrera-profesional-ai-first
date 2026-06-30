---
name: pcs-gestionar-hosts
description: Use when CODEX needs to create, add, update, archive, or validate PCS host records in `hosts/hosts.yaml`, including related Drive sources, local roots, YAML, and frontmatter.
---

# Gestionar Hosts

## Modo de uso

Usa esta skill cuando el usuario quiera crear el primer host PCS, añadir un host nuevo, registrar un proyecto anfitrión, registrar una fuente o bóveda de referencia, actualizar el registro de hosts o mantener el registro guiado de `hosts/hosts.yaml`.

No la uses para:

- pedir un fichero con todos los datos;
- pedir al usuario que escriba YAML;
- editar `hosts/hosts.yaml` de forma manual o disimulada;
- eliminar hosts por vía ordinaria;
- asumir un host activo global.
- cambiar el nombre fijo de `.pcs`.

## Regla crítica

Nunca pidas al usuario un fichero con todos los datos del host.
Nunca pidas al usuario que edite manualmente `hosts/hosts.yaml`.
Nunca generes ni modifiques `hosts/hosts.yaml` sin ejecutar antes el flujo guiado de preguntas y obtener confirmación explícita.
Para validar YAML o frontmatter, usa PyYAML con una invocacion minima y acotada. No intentes primero validadores PowerShell.
Si PowerShell resuelve `python` como `Function`, no dependas ciegamente de esa via: prefiere la ruta absoluta al `python.exe` real ya identificado o `py`.
Haz un unico intento automatico rapido, valida solo el YAML o frontmatter necesario y registra el comando exacto si falla.
Si hay timeout, quoting fragil, error del shell o fallo del entorno, aplica verificacion textual razonable e informa claramente si la validacion fue automatica con PyYAML o textual degradada.

## Lectura obligatoria

Antes de actuar, lee y usa como referencia:

- `README.md`
- `INDEX.md`
- `AGENTS.md`
- `.codex/AGENTS.md`
- `core/SEMANTICA_NUCLEAR_PCS.md`
- `core/FLUJO_CONFIGURACION_HOSTS_PCS.md`
- `core/REGLAS_GOBERNANZA_DOCUMENTAL.md`
- `core/FLUJO_OPERATIVO_MINIMO.md`
- `core/PROTOCOLO_APLICACION_PCS.md`
- `core/GLOSARIO_PCS.md`
- `.pcs/decisiones/DEC-20260522-1652-005-registro-anfitriones-pcs.md`

Si detectas contradicción entre estos documentos, detente e informa.

## Flujo obligatorio

1. Determina el ámbito operativo: PCS core, un host concreto o una referencia. No asumas un anfitrión global.
2. Comprueba si existe `hosts/hosts.yaml`.
3. Si no existe, inicia el flujo de creación; si existe, inicia el flujo de adición.
4. Lee el YAML actual, valida que sea parseable y calcula el `host_id` siguiente sin pedirlo al usuario.
5. Haz preguntas una a una, en este orden:
   - alias operativo
   - nombre humano
   - tipo de registro PCS
   - estado inicial
   - carpeta Drive visible para ChatGPT
   - uso de esa carpeta Drive
   - si desea añadir otra carpeta Drive
   - ruta local raíz para CODEX
   - uso de esa ruta local
   - si desea añadir otra ruta local
6. Traduce cada respuesta humana a su valor cerrado antes de escribir.
7. Resume el registro completo antes de tocar el fichero.
8. Pide confirmación explícita.
9. Solo después de la confirmación escribe `hosts/hosts.yaml`.
10. Si el registro confirmado tiene `pcs_role: host`, ejecuta también la comprobación de inicialización operativa mínima del host.
11. Valida el YAML final y confirma el resultado.

## Niveles de intervención

Cuando la tarea afecte a un registro con `pcs_role: host`, distingue siempre tres niveles:

1. Registro de host
   - Alta o actualización en `hosts/hosts.yaml`.
2. Preparación estructural mínima
   - Resolución de `.pcs` como `host_definition_root + "/.pcs"`.
   - Creación de `.pcs/` y de:
     - `.pcs/sesiones`
     - `.pcs/acciones`
     - `.pcs/decisiones`
     - `.pcs/estado`
3. Inicialización operativa mínima
   - Comprobación o creación de `.pcs/estado/estado-actual.md`.
   - Comprobación o creación de una sesión inicial en `.pcs/sesiones/`.

No presentes un host como "inicializado" si solo quedó completado el nivel estructural.

## Preguntas y traducciones

### Alias operativo

Pregunta:

```text
¿Qué alias operativo quieres usar para este registro?
```

Reglas:

- no pedir `host_id`;
- no aceptar vacío;
- no duplicar otro alias.

### Nombre humano

Pregunta:

```text
¿Cuál es el nombre humano del proyecto, bóveda o fuente?
```

### Tipo de registro PCS

Pregunta:

```text
¿Qué tipo de registro es?

1. El propio PCS normativo
2. Proyecto gestionado por PCS
3. Espacio de referencia o continuidad cognitiva que PCS puede consultar o acompañar
```

Mapeo:

- `El propio PCS normativo` -> `core`
- `Proyecto gestionado por PCS` -> `host`
- `Espacio de referencia o continuidad cognitiva que PCS puede consultar o acompañar` -> `reference`

### Estado inicial

Pregunta:

```text
¿Cuál es el estado inicial?

1. vigente
2. pendiente de actualización
3. desactualizado
4. archivado
```

Mapeo:

- `vigente` -> `vigente`
- `pendiente de actualización` -> `pendiente_de_actualizacion`
- `desactualizado` -> `desactualizado`
- `archivado` -> `archivado`

### Carpetas Drive visibles para ChatGPT

Pregunta:

```text
¿Qué carpeta espejo de Drive debe reconocer ChatGPT para este registro?
```

Reglas:

- aceptar solo nombre de carpeta;
- no aceptar URL;
- no aceptar ruta local;
- repetir si el usuario quiere añadir más carpetas.

Pregunta de uso:

```text
¿Qué uso tiene esa carpeta Drive?

1. Fuentes del PCS normativo
2. Documentos que definen qué debe ser el proyecto anfitrión
3. Documentos o carpeta vinculada a la codificación del proyecto anfitrión
4. Bóveda o espacio de trabajo del proyecto anfitrión
5. Fuentes auxiliares de consulta
```

Mapeo:

- `Fuentes del PCS normativo` -> `pcs_core_sources`
- `Documentos que definen qué debe ser el proyecto anfitrión` -> `host_definition_sources`
- `Documentos o carpeta vinculada a la codificación del proyecto anfitrión` -> `host_code_sources`
- `Bóveda o espacio de trabajo del proyecto anfitrión` -> `host_workspace_sources`
- `Fuentes auxiliares de consulta` -> `reference_sources`

Si no hay acceso a Drive, registra la carpeta como fuente esperada para ChatGPT sin intentar verificarla.

### Rutas locales para CODEX

Pregunta:

```text
¿Cuál es la ruta local raíz que usará CODEX?
```

Pregunta de uso:

```text
¿Qué uso tiene esa ruta local?

1. Raíz local del PCS normativo
2. Raíz local de los documentos que definen el proyecto anfitrión
3. Raíz local del código del proyecto anfitrión
4. Raíz local de la bóveda o espacio de trabajo del proyecto anfitrión
5. Raíz local de fuentes auxiliares de consulta
```

Mapeo:

- `Raíz local del PCS normativo` -> `pcs_core_root`
- `Raíz local de los documentos que definen el proyecto anfitrión` -> `host_definition_root`
- `Raíz local del código del proyecto anfitrión` -> `host_code_root`
- `Raíz local de la bóveda o espacio de trabajo del proyecto anfitrión` -> `host_workspace_root`
- `Raíz local de fuentes auxiliares de consulta` -> `reference_root`

Si un host tiene una unica ruta local para CODEX y esa ruta es `host_definition_root`, esa raiz actua como raiz local integral del host para efectos operativos, pudiendo contener definicion, documentacion de trabajo y, si procede, codigo, siempre que no existan rutas locales mas especificas como `host_code_root` o `host_workspace_root`.

## Validaciones obligatorias

Antes de escribir, valida:

- `host_id` no se pregunta, no se reutiliza y es incremental;
- el alias no está vacío ni duplicado;
- `pcs_role` solo puede ser `core`, `host` o `reference`;
- `status` solo puede ser `vigente`, `pendiente_de_actualizacion`, `desactualizado` o `archivado`;
- cada carpeta Drive tiene `folder_name` y `role`;
- cada ruta local tiene `environment`, `path` y `role`;
- si `pcs_role: host`, existe una única `host_definition_root`;
- no hay dos carpetas Drive con distinto `folder_name` y mismo `role` dentro del mismo registro;
- no hay dos rutas locales con distinto `path` y mismo `role` dentro del mismo registro;
- no existe `active_host`;
- no existe `pcs_operational_root`;
- no existe `pcs_paths`;
- no se crea un nombre distinto de `.pcs`;
- si el registro es `host`, la carpeta operativa se resuelve como `host_definition_root + "/.pcs"`;
- si falta `.pcs`, créala junto con:
  - `.pcs/sesiones`
  - `.pcs/acciones`
  - `.pcs/decisiones`
  - `.pcs/estado`
- si el registro es `host`, comprueba si existe `.pcs/estado/estado-actual.md`; si falta, créalo usando `templates/TEMPLATE_ESTADO_PROYECTO.md` como referencia y sin inventar contexto funcional no disponible;
- si el registro es `host`, comprueba si existe al menos una sesión inicial o de arranque en `.pcs/sesiones/`; si falta, crea una sesión con patrón `sesion-YYYYMMDD-HHMM-inicio-pcs-en-host.md` o variante equivalente compatible con el patrón vigente;
- el `estado-actual.md` inicial debe ser breve, actual, accionable y trazable; debe incluir proyecto anfitrión, fecha/hora de inicialización, estado operativo inicial, foco inicial, sesiones relevantes, acciones abiertas, decisiones vigentes, riesgos o advertencias y siguiente gesto recomendado;
- la sesión inicial debe registrar históricamente la aplicación de PCS al host, separar contexto, objetivo, capa episódica, capa semántica, líneas abiertas, derivaciones, documentos afectados y rehidratación futura, y dejar claro que `.pcs/` es memoria operativa del host y no redefine el núcleo PCS;
- la sesión inicial puede nacer `consolidada` si solo registra la inicialización ya completada, o `abierta` si el usuario está iniciando trabajo real sobre ese host; explica ese criterio al usuario;
- valida el YAML final con PyYAML usando una via determinista: ruta absoluta a `python.exe` si ya esta identificada y es estable, o `py` como alternativa razonable;
- si `python` aparece como `Function`, evita depender de esa via cuando exista alternativa mas explicita;
- valida solo el YAML o frontmatter necesario, no lotes masivos de archivos;
- haz un unico intento automatico rapido;
- si falla, registra el comando exacto y aplica verificacion textual razonable declarando el modo de validacion usado.

## Resumen previo obligatorio

Antes de escribir el fichero, muestra un resumen legible con:

- `host_id` generado;
- alias;
- nombre humano;
- tipo de registro PCS;
- valor YAML de `pcs_role`;
- estado;
- carpetas Drive y su uso humano/YAML;
- rutas locales y su uso humano/YAML;
- `.pcs` derivada si aplica;
- subcarpetas estándar que se comprobarán o crearán.
- si `pcs_role: host`, aclara también que se comprobará o creará la inicialización operativa mínima con `estado-actual.md` y sesión inicial.

Termina con una pregunta clara de confirmación explícita.

## Operaciones derivadas

Si la tarea concreta es actualizar o archivar un registro, sigue el flujo correspondiente del documento de configuración de hosts y mantén la misma disciplina:

- preguntas una a una;
- traducción de lenguaje humano a valores YAML cerrados;
- resumen previo;
- confirmación explícita;
- validación final con Python y PyYAML.

## Escritura segura

Solo escribe `hosts/hosts.yaml` después de la confirmación.

Si el fichero no existe, crea una estructura mínima con:

```yaml
schema_version: 1
hosts: []
```

Luego inserta el nuevo bloque sin alterar los registros existentes.

## Resultado esperado

Cuando termines, deja claro:

- qué host se añadió o inicializó;
- qué validaciones pasaron;
- si `hosts/hosts.yaml` se modificó o no;
- si quedaron rutas, carpetas o documentos operativos pendientes de creación o verificación;
- si el host quedó solo registrado, preparado estructuralmente o inicializado operativamente.
