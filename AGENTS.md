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

No se verificó `README.md` ni `AGENTS.md` previos en la raíz del host.

[PENDIENTE: identificar documentación local adicional del proyecto si existe]

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

Los agentes automáticos no deben leer, recorrer, indexar, resumir, modificar ni usar ningún contenido dentro de `.tmp/` salvo autorización explícita del usuario.

`.tmp/` es una zona temporal y auxiliar. No forma parte del proyecto operativo, de la bóveda `boveda-entrevista-profesional/` ni de ninguna fuente de verdad del host.

Esta exclusión incluye `.tmp/notas/` y cualquier otro contenido temporal, borrador, export parcial, prueba o resultado intermedio.
