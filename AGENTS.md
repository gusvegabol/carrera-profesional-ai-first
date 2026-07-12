# AGENTS — carrera-profesional-ai-first

## Propósito

Este repositorio corresponde al host `carrera-ai`.

Su propósito local es:
`[PENDIENTE: documentar el propósito funcional local de carrera-profesional-ai-first]`

## Relación con PCS

Este host usa Project Continuity System (PCS) como marco común de continuidad, gobernanza y trazabilidad.

Ruta del PCS core:
`C:/Users/gusve/Documents/Apps/project-continuity-system`

El PCS core actúa como fuente normativa común. Este repositorio anfitrión conserva su contexto local y su memoria operativa vive en `./.pcs/`.

## Contrato de gobernanza PCS

Cuando la tarea afecte gobernanza PCS, creación o actualización de sesiones, acciones, decisiones, estado, hosts o fuentes compartidas, el agente debe aplicar el contrato canónico vigente en:

```text
C:/Users/gusve/Documents/Apps/project-continuity-system/core/CONTRATO_CANONICO_GOBERNANZA_HOSTS.md
```

Este `AGENTS.md` orienta al agente localmente, pero no sustituye el contrato ni las entidades, plantillas, decisiones o protocolos del PCS Core.

## Rehidratación mínima obligatoria

Cuando el usuario declare el host, el agente debe:

1. resolver el alias del host;
2. consultar `hosts/hosts.yaml` del PCS core si está disponible;
3. consultar `./.pcs/estado/estado-actual.md` si existe;
4. resumir situación, acciones abiertas relevantes, decisiones vigentes condicionantes, riesgos y siguiente gesto recomendado;
5. no abrir ni actualizar una sesión PCS solo por esa declaración.

## Regla de degradación

Si faltan artefactos:

1. intentar `./.pcs/estado/estado-actual.md`;
2. si falta, revisar `./.pcs/sesiones/` abiertas o en pausa;
3. si falta `./.pcs/`, declarar el vacío de memoria operativa;
4. si falta `hosts/hosts.yaml`, declarar el límite de resolución del host.

## Documentos principales del host

Documentos verificados durante esta validación:

- `./.pcs/estado/estado-actual.md`
- `./.pcs/sesiones/sesion-20260614-2132-inicio-pcs-en-carrera-ai.md`
- `./docs/DOCUMENTO_SPEC_CARRERA_AI.md`

## Límites locales

- No hay todavía una descripción funcional confirmada del proyecto anfitrión.
- El estado verificado es de arranque mínimo PCS, no de operación funcional madura.
- No debe inferirse arquitectura, uso ni alcance del proyecto fuera de lo documentado en `.pcs/`.
- La memoria operativa confirmada del host vive en `./.pcs/`.

## Restricciones

- No tratar sesiones como estado vivo.
- No inventar contexto funcional no documentado.
- No editar `hosts/hosts.yaml` fuera del flujo guiado.
- No duplicar el núcleo PCS dentro de este repositorio.

## Exclusión operativa de `.tmp/`

Todo el contenido de `.tmp/` debe considerarse material temporal, auxiliar o de trabajo local.

La carpeta `.tmp/` no forma parte del proyecto operativo, no forma parte de la bóveda `boveda-entrevista-profesional/` y no debe usarse como fuente de verdad.

Su contenido no debe leerse, resumirse, indexarse, modificarse ni usarse salvo petición explícita del usuario.

Esto incluye, entre otros posibles contenidos:

- `.tmp/notas/`
- borradores temporales
- exports parciales
- pruebas
- resultados intermedios
- material auxiliar recopilado por el usuario

## Exclusión operativa de `.tmp/`

Los agentes automáticos no deben leer, recorrer, indexar, resumir, modificar ni usar ningún contenido dentro de `.tmp/` salvo autorización explícita del usuario.

`.tmp/` es una zona temporal y auxiliar. No forma parte del proyecto operativo, de la bóveda `boveda-entrevista-profesional/` ni de ninguna fuente de verdad del host.

Esta exclusión incluye `.tmp/notas/` y cualquier otro contenido temporal, borrador, export parcial, prueba o resultado intermedio.
