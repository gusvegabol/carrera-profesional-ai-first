---
name: pcs-genera-documentos-host-anfitrion
description: Use when se necesite generar en `.tmp/` los borradores coordinados de `README` y `AGENTS` para un host anfitrión PCS ya registrado en `hosts/hosts.yaml`.
---

# Generar documentos de host anfitrión

## Overview

Genera en `.tmp/` dos documentos temporales coordinados para un host anfitrión válido:

- `README_<ALIAS_NORMALIZADO>.md`
- `AGENTS_<ALIAS_NORMALIZADO>.md`

Ambos se derivan de:

- `templates/TEMPLATE_README_ANFITRION.md`
- `templates/TEMPLATE_AGENTS_ANFITRION.md`

La skill no escribe nada en el repositorio anfitrión real y no modifica `hosts/hosts.yaml`.

## Cuándo usarla

- El usuario pide generar los borradores de `README` y `AGENTS` para un host anfitrión PCS.
- El host ya debería existir en `hosts/hosts.yaml`.
- Se necesita una derivación temporal y revisable en `.tmp/`.

No usarla para:

- crear o editar `hosts/hosts.yaml`;
- generar documentos para `pcs-host` o registros `pcs_role: core`;
- escribir `README.md` o `AGENTS.md` dentro del host real;
- inventar contexto funcional del anfitrión.

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
- `templates/TEMPLATE_README_ANFITRION.md`
- `templates/TEMPLATE_AGENTS_ANFITRION.md`

Si detectas contradicción entre estas fuentes, detente e informa antes de escribir nada.

## Flujo

1. Identifica el alias del host pedido por el usuario.
2. Lee `hosts/hosts.yaml` y verifica que el alias existe exactamente una vez.
3. Rechaza el flujo si el registro encontrado no tiene `pcs_role: host`.
4. Extrae del registro, como mínimo:
   - `alias`
   - `human_name`
   - `status`
   - `chatgpt.visible_drive_sources`
   - `codex.local_roots`
5. Localiza una única ruta con rol `host_definition_root`.
6. Rechaza el flujo si falta esa ruta, si aparece más de una o si no es accesible.
7. Inspecciona el host real con esta prioridad:
   - `README.md`, si existe;
   - `AGENTS.md`, si existe;
   - `.pcs/estado/estado-actual.md`, si existe;
   - una sesión inicial o la sesión más útil en `.pcs/sesiones/`, si existe.
8. Construye una base verificable del host con identidad mínima, estado resumible, documentos confirmados, límites observables y vacíos que deban mantenerse como pendientes.
9. Deriva los dos borradores desde sus plantillas canónicas.
10. Normaliza el alias a mayúsculas y cambia `-` por `_`.
11. Escribe:
   - `.tmp/README_<ALIAS_NORMALIZADO>.md`
   - `.tmp/AGENTS_<ALIAS_NORMALIZADO>.md`
12. Sobrescribe los archivos si ya existen.
13. Verifica la salida y reporta el resultado separando documentos leídos, creados, modificados, validaciones y riesgos.

## Reglas de derivación

- Usa las plantillas como estructura canónica, no como sustitución ciega de marcadores.
- Rellena cada sección con una de estas estrategias:
  - dato verificado;
  - síntesis verificable;
  - pendiente explícito.
- Si un dato no existe, déjalo como `[PENDIENTE: ...]`.
- Nunca rellenes huecos con supuestos.

## Reglas de degradación

Si faltan artefactos del host, degrada con este orden:

1. intentar `README.md` y `AGENTS.md` del host si existen;
2. usar `.pcs/estado/estado-actual.md` como base mínima si existe;
3. si falta el estado, revisar sesiones útiles en `.pcs/sesiones/`;
4. si falta `.pcs/`, detenerse y declarar que no existe memoria operativa local suficiente;
5. si falta `hosts/hosts.yaml` o no puede resolverse el alias, detenerse;
6. si existe el alias pero no es `pcs_role: host`, rechazar el flujo.

## Validaciones obligatorias

Antes de declarar éxito, comprueba:

- `hosts/hosts.yaml` existe y es legible;
- el alias existe exactamente una vez;
- el registro encontrado tiene `pcs_role: host`;
- existe una única ruta `host_definition_root`;
- las dos plantillas canónicas existen;
- los dos archivos finales quedaron en `.tmp/`;
- no quedan marcadores `{{...}}` en la salida;
- el alias correcto aparece en ambos documentos;
- no se modificó el repositorio anfitrión real;
- no se escribió fuera de `.tmp/`.

## Errores comunes

- Tomar el alias desde memoria en vez de leer `hosts/hosts.yaml`.
- Aceptar un `human_name` como si fuera alias.
- Generar documentos para `pcs-host`.
- Inventar propósito funcional del host porque el repositorio está vacío.
- Tratar `.pcs/` como sustituto total de la documentación anfitriona.
- Derivar solo uno de los dos documentos y declarar el flujo exitoso.
- Dejar marcadores `{{...}}` sin resolver.

## Resultado esperado

Si todo sale bien, el resultado debe dejar:

- `.tmp/README_<ALIAS_NORMALIZADO>.md`
- `.tmp/AGENTS_<ALIAS_NORMALIZADO>.md`
- ambos documentos sin marcadores pendientes del template;
- ambos documentos basados solo en contexto verificable o pendientes explícitos.
