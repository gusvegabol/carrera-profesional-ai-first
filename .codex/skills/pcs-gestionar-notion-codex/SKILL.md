---
name: pcs-gestionar-notion-codex
description: Use when CODEX receives an approved URL or page ID from `pcs-prompts-codex`, especially for prompts tied to a PCS host, local repository work, or a linked Notion response cycle.
---

# Skill: pcs-gestionar-notion-codex

## Propósito

Convertir en procedimiento repetible la ejecución de prompts aprobados en Notion dentro del flujo:

```text
Usuario -> ChatGPT -> pcs-prompts-codex -> CODEX -> pcs-respuestas-prompts-codex -> ChatGPT/usuario
```

La skill no sustituye al prompt.

La skill fija el protocolo que CODEX debe aplicar para:

- validar la entrada;
- resolver el host y el directorio físico de trabajo;
- ejecutar solo el alcance autorizado;
- cerrar el ciclo operativo en Notion con trazabilidad suficiente.

## Versionado interno

El frontmatter de `SKILL.md` se mantiene mínimo por especificación. El versionado vive aquí para no romper la validación de la skill.

| Campo | Valor |
|---|---|
| Versión | 0.2.6 |
| Última actualización | 2026-06-11 |
| Cambio principal | Salida documental separada por categorias y contrato de escritura Notion explicitado para `Prompt_Origen` y `Respuesta_Codex` |

## Cuándo usar esta skill

Usa esta skill cuando la entrada principal sea una URL o un ID de página de Notion que pertenezca a `pcs-prompts-codex` y el prompt esté aprobado para ejecución por CODEX.

Úsala especialmente cuando el prompt:

- afecte a un host PCS concreto;
- exija resolver la raíz local ejecutable del host declarado;
- requiera leer documentos locales y/o páginas Notion vinculadas;
- deba dejar una respuesta larga separada en `pcs-respuestas-prompts-codex`;
- necesite cerrar el prompt origen en Notion al terminar.

## Entrada aceptada

La skill solo acepta como entrada principal:

```text
URL o ID de una página perteneciente a pcs-prompts-codex
```

Condiciones mínimas de aceptación:

- la página pertenece a `pcs-prompts-codex`;
- `Para = codex`;
- `Estado = aprobado_para_codex`;
- `Host` está informado;
- `Respuesta_Codex` no está informada;
- el cuerpo de la página contiene el contrato ejecutable completo.

## Entrada no aceptada

La skill no acepta como entrada ejecutable principal:

- páginas de `pcs-documentos`;
- páginas de `pcs-respuestas-prompts-codex`;
- páginas sueltas de Notion fuera de `pcs-prompts-codex`;
- conversaciones;
- instrucciones vagas del usuario sin prompt aprobado;
- propiedades aisladas como `Instruccion` o `Introduccion` sin contrato suficiente en el cuerpo;
- propuestas o documentos de trabajo no convertidos en prompt aprobado.

Los documentos relacionados en la propiedad `Documentos` son apoyo contextual. Nunca equivalen por sí solos a una autorización de ejecución.

## Validaciones previas obligatorias

Antes de ejecutar, CODEX debe validar todo lo siguiente.

### 1. Pertenencia y destinatario

- La página pertenece a `pcs-prompts-codex`.
- `Para = codex`.

Si cualquiera de estas dos validaciones falla, la skill debe detenerse.

### 2. Estado ejecutable

- `Estado = aprobado_para_codex`.

No debe ejecutar si el estado es `borrador`, `pendiente_aprobacion`, `en_ejecucion`, `ejecutado`, `pendiente_revision`, `validado`, `descartado`, `error` u otro valor no ejecutable.

### 3. Host informado y coherente

- `Host` está informado.
- Si la tarea afecta al propio PCS, `Host = pcs-host`.
- Si la tarea afecta a otro anfitrión registrado, `Host` debe ser el alias de ese anfitrión.
- `general` solo es válido para tareas realmente no ligadas a repositorio, host, `.pcs/`, skill, configuración local ni documentación específica.
- En caso de duda, `general` no debe aceptarse.
- Si el esquema real de `pcs-prompts-codex` todavía no expone el alias necesario como opción válida de `Host`, la skill debe detenerse y registrar incidencia de esquema antes de intentar ejecutar sobre ese anfitrión.

### 4. Resolución local del host

Cuando `Host != general`, la skill debe:

- resolver el alias contra `hosts/hosts.yaml`;
- comprobar que el host existe;
- leer `pcs_role`;
- resolver la raíz local física según ese tipo de registro;
- confirmar que la ruta local requerida es accesible;
- interpretar `.pcs/` según la raíz operativa que corresponda cuando la tarea dependa de esa memoria.

No debe usar rutas `*_sources` de Drive como directorio de ejecución.

### 5. Cuerpo ejecutable suficiente

El cuerpo de la página es la única fuente aceptada para el prompt ejecutable completo.

La propiedad `Instruccion` o `Introduccion`, si existe, solo puede actuar como resumen auxiliar.

La skill debe detenerse si el cuerpo no contiene contexto suficiente sobre:

- objetivo;
- cambios solicitados;
- permisos de modificación;
- restricciones;
- validaciones;
- salida esperada;
- criterios de parada, si son necesarios para evitar daño o deriva.

### 6. Coherencia interna

La skill debe comprobar que no hay contradicción relevante entre:

- propiedades del prompt;
- cuerpo del prompt;
- host declarado;
- documentos vinculados;
- rutas locales;
- restricciones;
- salida esperada.

Si hay contradicción relevante, debe detenerse.

### 7. No reejecución

Si `Respuesta_Codex` ya tiene valor, la skill debe detenerse y no reejecutar el prompt.

Un prompt con `Respuesta_Codex` informada se considera ya procesado o no seguro para ejecución automática.

## Resolución de host y rutas

La ubicación física de esta skill dentro de `pcs-host` no determina el directorio físico de ejecución del prompt.

La regla correcta es:

1. leer `Host` en la página de `pcs-prompts-codex`;
2. si `Host != general`, resolver el alias en `hosts/hosts.yaml`;
3. leer `pcs_role` del registro resuelto;
4. si `pcs_role = core`, usar `pcs_core_root` como directorio físico de ejecución;
5. si `pcs_role = host`, usar `host_definition_root` como directorio físico de ejecución;
6. si `pcs_role = reference`, no asumir raíz ejecutable ordinaria salvo que el prompt aprobado declare explícitamente una ruta local válida, su rol, el alcance y los permisos;
7. interpretar la memoria operativa `.pcs/` dentro de `pcs_core_root` cuando el registro sea `core` y dentro de `host_definition_root` cuando el registro sea `host`, siempre que la tarea dependa de esa memoria.

Reglas operativas:

- `*_sources` describen fuentes visibles para ChatGPT; no son la ruta local de ejecución;
- `*_root` describen rutas locales físicas para CODEX;
- la `.pcs/` del host declarado no debe confundirse con la `.pcs/` de `pcs-host`, salvo que `Host = pcs-host`;
- si `pcs_role = core` y no puede resolverse `pcs_core_root`, la skill debe detenerse;
- si `pcs_role = host` y no puede resolverse `host_definition_root`, la skill debe detenerse;
- si `pcs_role = reference` y el prompt no aporta autorización local explícita suficiente, la skill debe detenerse.

## Lectura del prompt y documentos vinculados

Una vez superadas las validaciones previas, la skill debe leer en este orden:

1. la página completa del prompt;
2. los documentos Notion vinculados en `Documentos` cuando el cuerpo del prompt los use como fuente necesaria;
3. los documentos locales obligatorios que el propio prompt liste, siempre desde el contexto físico del host declarado salvo ruta absoluta explícita y autorizada.

Reglas:

- la relación `Documentos` aporta contexto, no autorización;
- una página de `pcs-documentos` puede ser contrato operativo solo si el cuerpo del prompt lo indica explícitamente;
- si falta un documento obligatorio, la skill debe detenerse;
- la skill no debe inventar contenido ausente ni completar vacíos por intuición.

## Reglas de ejecución

Durante la ejecución, CODEX debe respetar estas reglas:

1. Ejecutar solo los cambios explícitamente autorizados por el prompt aprobado.
2. Separar claramente lectura y escritura.
3. No ampliar el alcance aunque detecte mejoras posibles.
4. No elevar propuestas de Notion a norma canónica.
5. No crear acciones, decisiones, sesiones, plantillas, documentos canónicos ni otras skills salvo que el prompt aprobado lo solicite de forma explícita y con permisos claros.
6. No cerrar sesiones salvo que el prompt aprobado lo ordene explícitamente, identifique la sesión afectada y autorice la ruta o página correspondiente.
7. No hacer correcciones masivas salvo que el prompt aprobado lo solicite explícitamente, delimite alcance, rutas afectadas, criterios de parada y validaciones.
8. No marcar el resultado como revisado o validado por iniciativa propia.

Regla defensiva central:

```text
Lo mencionado no queda autorizado.
Solo queda autorizado lo indicado explícitamente en Cambios solicitados y Permisos de modificación.
```

## Contrato de escritura Notion

CODEX no debe inferir el formato de una relación Notion por su significado semántico ni por el formato que devuelve la lectura. Debe usar exactamente la forma que espera cada operación de escritura.

### Escritura en `pcs-respuestas-prompts-codex`

Al crear la respuesta larga con `mcp__codex_apps__notion._notion_create_pages`:

| Propiedad | Formato de escritura | Nota |
|---|---|---|
| `Nombre` | texto | Título de la respuesta larga |
| `Estado_Revision` | texto select | Usar `pendiente_revision` al crear |
| `Prompt_Origen` | URL simple como string | No enviar lista, aunque la lectura muestre una relación |

### Escritura en el prompt origen de `pcs-prompts-codex`

Al actualizar el prompt origen con `mcp__codex_apps__notion._notion_update_page`:

| Propiedad | Formato de escritura | Nota |
|---|---|---|
| `Estado` | texto select | Usar `ejecutado` si fue correcto o `error` si falló |
| `Resultado` | texto | Resumen breve |
| `Respuesta_Codex` | URL simple como string | La lectura puede devolver una lista, pero la escritura debe usar un único URL |

### Ejemplos de escritura correctos

```json
{
  "Nombre": "Respuesta CODEX — Ejemplo",
  "Estado_Revision": "pendiente_revision",
  "Prompt_Origen": "https://app.notion.com/p/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

```json
{
  "Estado": "ejecutado",
  "Resultado": "Resumen breve.",
  "Respuesta_Codex": "https://app.notion.com/p/yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
}
```

### Regla de no improvisación

- No convertir `Prompt_Origen` en lista si el conector espera string.
- No convertir `Respuesta_Codex` en string si el conector espera lista al leer.
- No deducir el formato por simetría entre propiedades.
- Si el conector rechaza un payload, revisar primero el esquema del data source y un ejemplo existente del mismo data source.
- No reintentar con otro formato "a ojo" sin evidencia previa.

### Orden obligatorio de cierre

1. Crear la respuesta larga.
2. Confirmar la URL creada.
3. Actualizar el prompt origen con `Estado`, `Resultado` y `Respuesta_Codex`.
4. Verificar que ambos objetos quedaron vinculados correctamente.

## Cierre obligatorio en Notion

Cerrar el ciclo en Notion forma parte de la tarea.

Si no puede cerrarse correctamente, la ejecución no debe presentarse como completada.

### Si la ejecución fue correcta

La skill debe indicar que CODEX:

1. cree una respuesta larga en `pcs-respuestas-prompts-codex`;
2. la vincule al prompt origen mediante `Prompt_Origen`;
3. actualice el prompt origen con:

```text
Estado = ejecutado
Resultado = resumen breve
Respuesta_Codex = página de respuesta larga creada
```

### Si hubo bloqueo o error

La skill debe indicar que CODEX:

1. cree una respuesta larga de error en `pcs-respuestas-prompts-codex`;
2. la vincule al prompt origen mediante `Prompt_Origen`;
3. actualice el prompt origen con:

```text
Estado = error
Resultado = resumen breve del bloqueo
Respuesta_Codex = página de respuesta larga de error creada
```

Si una imposibilidad técnica real impide crear o vincular la respuesta larga, la ejecución queda incompleta, debe declararse explícitamente como incidencia grave de cierre, debe informarse al usuario y el prompt no puede considerarse cerrado correctamente.

## Respuesta larga en pcs-respuestas-prompts-codex

La creación de la respuesta larga no es opcional.

La página creada en `pcs-respuestas-prompts-codex` debe incluir, como mínimo:

- `Nombre`;
- `Prompt_Origen = {{url_prompt_notion_en_pcs-prompts-codex}}`;
- `Estado_Revision = pendiente_revision`.

La respuesta larga debe usar esta estructura mínima:

```text
# Respuesta CODEX — [nombre del prompt]

## Resumen ejecutivo
## Validaciones previas
## Documentos Notion leídos
## Documentos locales leídos
## Documentos creados
## Documentos modificados
## Documentos relacionados o usados como contexto, pero no modificados
## Objetos Notion creados o modificados
## Cambios realizados
## Cambios no realizados
## Validaciones realizadas
## Incidencias o límites
## Estado final en Notion
## Siguiente paso recomendado
```

La skill debe dejar claro que:

- `Resultado` en el prompt origen contiene solo un resumen breve;
- la respuesta larga es la superficie recuperable para revisión posterior;
- la salida final revisable no debe usar un bloque unico ambiguo como `Documentos afectados` cuando pueda separar lectura, creacion, modificacion, contexto y objetos Notion;
- CODEX no debe marcar `Estado_Revision` como `revisada`, `con_incidencias` o `descartada`;
- esa revisión corresponde a ChatGPT y/o al usuario.

## Criterios de parada

La skill debe detenerse sin ejecutar cambios físicos si ocurre cualquiera de estas situaciones:

- la página no pertenece a `pcs-prompts-codex`;
- `Para != codex`;
- `Estado != aprobado_para_codex`;
- `Host` falta o es incoherente;
- `Host != general` y no puede resolverse el host declarado;
- `Host != general` y no puede resolverse la raíz local exigida por el `pcs_role` real del registro;
- `pcs_role = core` y no puede ubicarse `.pcs/` dentro de `pcs_core_root` cuando la tarea depende de esa memoria operativa;
- `pcs_role = host` y no puede ubicarse `.pcs/` dentro de `host_definition_root` cuando la tarea depende de esa memoria operativa;
- `pcs_role = reference` y la ejecución requeriría asumir una raíz local no autorizada explícitamente por el prompt aprobado;
- la tarea afecta a PCS y `Host != pcs-host`;
- `Respuesta_Codex` ya está informada;
- el cuerpo no contiene contrato ejecutable suficiente;
- existe contradicción relevante entre propiedades, cuerpo, host o documentos vinculados;
- falta acceso a documentos imprescindibles;
- para completar la tarea sería necesario modificar documentación canónica o rutas no autorizadas;
- para completar la tarea sería necesario crear entidades PCS no autorizadas.

Cuando se detenga por bloqueo:

- no debe improvisar una ruta alternativa;
- no debe corregir el prompt por su cuenta;
- debe dejar trazabilidad suficiente para ChatGPT/usuario;
- debe cerrar Notion como `error` si el esquema y las herramientas disponibles lo permiten.

## Validaciones finales

Al finalizar una ejecución, la skill debe exigir como mínimo:

- comprobación de existencia de los archivos o páginas que el prompt ordenaba crear;
- validación básica del contenido modificado;
- `git diff --check` cuando haya cambios locales de repositorio;
- `git diff --stat` cuando haya cambios locales de repositorio;
- verificación de que el diff está limitado al alcance esperado;
- validación fiable de YAML/frontmatter si se modificó;
- comprobación de que el prompt origen quedó con `Resultado` breve y `Estado` final correcto;
- comprobación de que la respuesta larga quedó creada y vinculada mediante `Prompt_Origen`.

Si alguna validación no puede ejecutarse, la skill debe exigir que se declare como incidencia, no ocultarla.

## Referencia rápida

| Caso | Acción obligatoria |
|---|---|
| Página fuera de `pcs-prompts-codex` | Detenerse |
| `Para != codex` | Detenerse |
| `Estado != aprobado_para_codex` | Detenerse |
| `Respuesta_Codex` ya informada | Detenerse y no reejecutar |
| `Host != general` y no resuelve la raíz local requerida por su `pcs_role` | Detenerse |
| Cuerpo sin contrato ejecutable suficiente | Detenerse |
| Ejecución correcta | Crear respuesta larga, vincular `Prompt_Origen`, actualizar prompt a `ejecutado` |
| Bloqueo o error | Crear respuesta larga de error si es posible y actualizar prompt a `error` |

## Salida esperada

La salida final de una ejecución basada en esta skill debe incluir, como mínimo:

1. validaciones previas realizadas;
2. documentos Notion leídos;
3. documentos locales leídos;
4. documentos creados;
5. documentos modificados;
6. documentos relacionados o usados como contexto, pero no modificados;
7. objetos Notion creados o modificados;
8. cambios realizados;
9. cambios no realizados;
10. validaciones realizadas;
11. incidencias o límites;
12. estado final en Notion;
13. URL de la respuesta larga creada en `pcs-respuestas-prompts-codex`;
14. confirmación de que `Prompt_Origen` apunta al prompt origen;
15. siguiente paso recomendado.

## Errores comunes

- Tratar `Instruccion` o `Introduccion` como prompt completo.
  Corrección: usar el cuerpo de la página como contrato ejecutable principal.
- Ejecutar sobre `pcs-host` por defecto aunque el `Host` declarado sea otro.
  Corrección: resolver siempre `hosts/hosts.yaml` y usar la raíz local que corresponda a `pcs_role`.
- Confundir `*_sources` de Drive con rutas locales `*_root`.
  Corrección: ejecutar solo sobre rutas locales físicas.
- Suponer que lo vinculado en `Documentos` autoriza cambios.
  Corrección: usar `Documentos` solo como apoyo contextual salvo instrucción explícita en el cuerpo.
- Cerrar el trabajo solo por terminal sin cerrar Notion.
  Corrección: crear siempre la respuesta larga y actualizar el prompt origen.
- Reejecutar un prompt que ya tiene `Respuesta_Codex`.
  Corrección: detenerse y registrar incidencia en vez de crear una segunda respuesta principal.

## Límites de la skill

Esta skill:

- no sustituye al prompt aprobado;
- no valida por sí sola que una propuesta de Notion sea canónica;
- no convierte `pcs-documentos` en fuente automática de ejecución;
- no declara un host activo global;
- no obliga a ejecutar siempre sobre `pcs-host`;
- no autoriza cambios fuera del alcance explícito del prompt;
- no sustituye la revisión final de ChatGPT/usuario;
- no cierra correctamente una tarea si falta la respuesta larga o su vinculación en Notion.

## Banderas rojas

- "El cuerpo es corto, pero con `Instruccion` ya me vale"
- "Aunque `Host` no exista en el esquema, puedo asumir el repositorio correcto"
- "Ya existe `Respuesta_Codex`, pero puedo crear una segunda porque esta vez es mejor"
- "Como el documento vinculado lo menciona, queda autorizado tocarlo"
- "No pude cerrar Notion, pero el cambio local ya está hecho"

Si aparece cualquiera de estas racionalizaciones, la skill debe detener la ejecución o dejarla en `error`, nunca continuar como si el cierre fuera válido.
