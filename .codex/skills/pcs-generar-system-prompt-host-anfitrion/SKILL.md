---
name: pcs-generar-system-prompt-host-anfitrion
description: Use when se necesite generar en `.tmp/` el system prompt corto de un workspace ChatGPT para un host anfitrión PCS ya registrado en `hosts/hosts.yaml`.
---

# Generar system prompt host anfitrión

## Overview

Genera un documento temporal en `.tmp/` a partir de la plantilla canónica `prompts/chatgpt-system-prompt/SYSTEM_PROMPT_CORTO_HOST_ANFITRION.md`, sustituyendo sus marcadores con datos reales de un host válido registrado en `hosts/hosts.yaml`.

La skill no crea ni actualiza el registro de hosts. Solo consume un host ya existente y produce el prompt corto listo para usar en ChatGPT.

## Cuándo usarla

- El usuario pide preparar el system prompt corto para el workspace ChatGPT de un host anfitrión PCS.
- El host ya debería existir en `hosts/hosts.yaml`.
- Se necesita un artefacto temporal en `.tmp/`.

No usarla para:

- crear o editar `hosts/hosts.yaml`;
- inferir un host no declarado;
- generar prompts para `pcs-host` si el caso pedido no es un host anfitrión;
- inventar datos que no estén en el registro del host.

## Lectura obligatoria

Antes de actuar, lee como mínimo:

- `README.md`
- `INDEX.md`
- `AGENTS.md`
- `.codex/AGENTS.md`
- `core/SEMANTICA_NUCLEAR_PCS.md`
- `core/REGLAS_GOBERNANZA_DOCUMENTAL.md`
- `core/FLUJO_OPERATIVO_MINIMO.md`
- `core/PROTOCOLO_APLICACION_PCS.md`
- `core/FLUJO_HUMANO_CHATGPT_CODEX_PCS.md`
- `core/FLUJO_CONFIGURACION_HOSTS_PCS.md`
- `hosts/hosts.yaml`
- `prompts/chatgpt-system-prompt/SYSTEM_PROMPT_CORTO_HOST_ANFITRION.md`

Si detectas contradicción entre estas fuentes, detente e informa antes de escribir nada.

## Flujo

1. Identifica el alias del host pedido por el usuario.
2. Lee `hosts/hosts.yaml` y verifica que el alias existe.
3. Rechaza el flujo si el registro encontrado no tiene `pcs_role: host`.
4. Extrae del registro, como mínimo:
   - `alias`
   - `human_name`
   - `status`
   - carpetas `chatgpt.visible_drive_sources`
   - rutas `codex.local_roots`
5. Localiza la carpeta Drive principal del anfitrión:
   - primero intenta `host_definition_sources`;
   - si no existe, usa `host_workspace_sources`;
   - si tampoco existe, detente y explica que falta una fuente Drive anfitrión válida para completar la plantilla sin inventar datos.
6. Lee la plantilla `prompts/chatgpt-system-prompt/SYSTEM_PROMPT_CORTO_HOST_ANFITRION.md`.
7. Sustituye los marcadores obligatorios:
   - `{{alias del host}}` -> alias real del host
   - `{{nombre carpeta DRIVE del host anfitrión}}` -> nombre de la carpeta Drive anfitriona elegida en el paso 5
8. Deriva el nombre del archivo de salida como:
   - `SYSTEM_PROMPT_CORTO_<ALIAS_NORMALIZADO>.md`
   - normalización: convertir a mayúsculas y sustituir guiones `-` por guiones bajos `_`
   - ejemplo: `carrera-ai` -> `SYSTEM_PROMPT_CORTO_CARRERA_AI.md`
9. Escribe el resultado en `.tmp/`.
10. Si el archivo ya existe en `.tmp/`, sobrescríbelo.
11. Verifica el resultado:
   - el archivo final existe;
   - no quedan marcadores `{{...}}`;
   - el alias correcto aparece en el documento;
   - la carpeta Drive anfitriona correcta aparece en el documento.
12. Informa el resultado separando:
   - documentos leídos;
   - documentos creados;
   - documentos modificados;
   - validaciones realizadas;
   - bloqueos o riesgos, si existen.

## Reglas de selección de datos

- El alias operativo sale de `hosts/hosts.yaml`, no de memoria conversacional.
- No uses `project-continuity-system` como carpeta anfitriona salvo que el host registrado lo declare realmente como fuente anfitriona, cosa poco habitual.
- Para el nombre de la carpeta Drive anfitriona, prioriza la fuente que represente al propio host, no la fuente del PCS canónico.
- Si el host tiene varias fuentes Drive anfitrionas del mismo tipo, detente y pide aclaración en vez de elegir arbitrariamente.
- Las rutas locales sirven como contexto de validación, no como sustituto del nombre de carpeta Drive que pide la plantilla.

## Validaciones obligatorias

Antes de declarar éxito, comprueba:

- `hosts/hosts.yaml` existe y es legible;
- el alias pedido existe exactamente una vez;
- el registro encontrado tiene `pcs_role: host`;
- la plantilla canónica existe;
- la plantilla contiene los dos marcadores esperados;
- el archivo final quedó dentro de `.tmp/`;
- el nombre de salida sigue la convención `SYSTEM_PROMPT_CORTO_<ALIAS_NORMALIZADO>.md`;
- el contenido final no conserva `{{...}}`.

## Errores comunes

- Tomar el alias desde memoria en vez de leer `hosts/hosts.yaml`.
- Usar la fuente `pcs_core_sources` como carpeta anfitriona.
- Generar el prompt para un alias que existe pero no es `pcs_role: host`.
- Escribir el archivo en otra carpeta distinta de `.tmp/`.
- Mantener el nombre temporal anterior del archivo aunque el alias cambie.
- Declarar éxito sin revisar que ya no queden marcadores.
- Inventar una carpeta Drive anfitriona cuando el registro no la define de forma suficiente.

## Resultado esperado

Si todo sale bien, el resultado debe dejar:

- un archivo nuevo o sobrescrito en `.tmp/`;
- el alias real del host incrustado en el prompt;
- la carpeta Drive anfitriona real incrustada en el prompt;
- verificación explícita de que no quedan marcadores pendientes.
