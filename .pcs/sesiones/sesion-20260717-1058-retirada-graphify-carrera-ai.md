---
id: sesion-20260717-1058-retirada-graphify-carrera-ai
titulo: Retirada de Graphify de carrera-ai
inicio: 2026-07-17 10:58
cierre: 2026-07-17 11:40
estado: cerrada
tipo: sesion
host: carrera-ai
sesion_relacionada: sesion-20260713-1344-integracion-operacion-graphify-carrera-ai
---

# Sesión PCS - Retirada de Graphify de `carrera-ai`

## Contexto inmediato

El 2026-07-17 se decidió aplicar en `carrera-ai` la misma retirada de Graphify formalizada en PCS Core mediante `DEC-20260715-0004-retirada-graphify-pcs-host`.

El host mantenía una decisión local vigente sobre tres corpus Graphify, `DEC-20260713-1344-001-integrar-graphify-tres-corpus`, que queda sustituida por la nueva decisión de retirada. La sesión registra el trabajo `Work` asociado a esta transición y conservará la trazabilidad de las comprobaciones y materializaciones que se realicen.

## Objetivo

Formalizar la retirada de Graphify de `carrera-ai`, trasladar al host las razones documentadas en PCS Core, identificar los artefactos afectados y dejar preparado el registro para comprobar la retirada física sin modificar PCS Core.

## Capa episódica

Se rehidrató el host `carrera-ai` desde `hosts/hosts.yaml`, `.pcs/estado/estado-actual.md` y las sesiones PCS pertinentes. Se localizó y leyó la decisión canónica de PCS Core `DEC-20260715-0004-retirada-graphify-pcs-host`.

La decisión de referencia establece que el coste de tiempo y recursos de la extracción semántica es desproporcionado, que los resultados dependen de modelos que no siempre generan salidas estructuradas válidas y que el mantenimiento cotidiano debe apoyarse en fuentes Markdown y enlaces directos.

Con autorización del usuario, se crea esta sesión `Work`, la decisión equivalente del host y la actualización del estado vivo. A continuación se eliminan los artefactos físicos y se limpian las instrucciones operativas asociadas.

La retirada comprende:

- los directorios `.pcs/graphify-out/`, `docs/graphify-out/` y `boveda-entrevista-profesional/graphify-out/`, incluidas sus cachés;
- `run-graphify.bat`;
- `.pcs/.graphifyignore` y `docs/.graphifyignore`;
- las reglas operativas específicas en `AGENTS.md`, `.pcs/AGENTS.md` y `docs/AGENTS.md`;
- las exclusiones ya innecesarias de `.gitignore`.

Las búsquedas finales se realizan excluyendo `.tmp/`, conforme a la gobernanza local. No se modifica PCS Core.

## Capa semántica

La retirada de Graphify es una determinación local de operación documental para `carrera-ai`, derivada por aplicación controlada de una decisión vigente de PCS Core. No es una modificación de PCS Core ni una adopción de una alternativa tecnológica.

La autoridad documental queda reordenada así: el estado actual informa del presente, las decisiones vigentes fijan determinaciones, las sesiones conservan la historia y las fuentes Markdown junto con sus enlaces se revisan directamente para verificar relaciones documentales.

## Ideas y líneas cognitivas abiertas

- No quedan líneas cognitivas abiertas sobre la materialización de esta retirada.
- Una futura necesidad de análisis semántico requerirá una decisión nueva, concreta y aprobada.

## Acciones derivadas

- Acción: materializar y verificar la retirada física de Graphify en `carrera-ai`.
  Estado: completada el 2026-07-17.
  Resultado: artefactos eliminados e instrucciones operativas limpiadas; las referencias PCS conservadas tienen carácter histórico o documentan la retirada vigente.

## Decisiones derivadas

- `DEC-20260717-1058-001-retirada-graphify-carrera-ai`.
  Estado: vigente.
  Enlace: `.pcs/decisiones/DEC-20260717-1058-001-retirada-graphify-carrera-ai.md`.

## Problemas o bloqueos

- La política del terminal bloqueó la primera eliminación recursiva. La retirada se completó mediante borrado explícito de archivos versionados y limpieza limitada a las tres rutas autorizadas.
- No quedan bloqueos abiertos.
- La decisión no autoriza modificaciones en PCS Core ni la adopción de otra herramienta semántica.

## Documentos afectados

- `.pcs/estado/estado-actual.md`.
- `.pcs/decisiones/DEC-20260713-1344-001-integrar-graphify-tres-corpus.md` como decisión sustituida.
- `.pcs/decisiones/DEC-20260717-1058-001-retirada-graphify-carrera-ai.md`.
- `.pcs/sesiones/sesion-20260717-1058-retirada-graphify-carrera-ai.md`.
- `run-graphify.bat`, eliminado.
- `.pcs/.graphifyignore` y `docs/.graphifyignore`, eliminados.
- `.pcs/graphify-out/`, `docs/graphify-out/` y `boveda-entrevista-profesional/graphify-out/`, eliminados con sus cachés y datos derivados.
- `AGENTS.md`, `.pcs/AGENTS.md`, `docs/AGENTS.md` y `.gitignore`, actualizados para retirar instrucciones operativas y exclusiones específicas.

## Verificación final

La comprobación completa del repositorio, excluyendo `.git/` y `.tmp/`, confirma:

- cero directorios `graphify-out/`;
- cero archivos de datos o soporte de Graphify, incluidos `.graphify*`, `graph.json`, `graph.html`, `GRAPH_REPORT.md` y `run-graphify.bat`;
- cero referencias a Graphify fuera de `.pcs/`;
- las decisiones anteriores están marcadas como `sustituida` y las sesiones anteriores que lo mencionan incluyen una nota explícita de vigencia histórica;
- las únicas referencias actuales en `.pcs/` pertenecen a la decisión de retirada, esta sesión y el estado vivo que documenta la eliminación;
- `git diff --check` no detecta errores de espacios ni de formato del parche.

## Rehidratación futura

- **Dónde quedó el trabajo:** la decisión local de retirada está vigente, la eliminación física está completada, el estado vivo la registra y esta sesión `Work` queda cerrada.
- **Leer primero:** `.pcs/estado/estado-actual.md`, `DEC-20260717-1058-001-retirada-graphify-carrera-ai.md`, esta sesión y la decisión de referencia de PCS Core.
- **Líneas abiertas a retomar:** ninguna sobre esta materialización.
- **Riesgos de malinterpretación:** no tratar las menciones históricas como instrucciones vigentes, no retirar fuentes documentales metodológicas y no modificar PCS Core.
- **Siguiente gesto recomendado:** continuar con el foco metodológico vigente del host; cualquier herramienta semántica futura requerirá una decisión nueva.

## Checklist de consolidación

- [x] La capa episódica registra el recorrido histórico relevante.
- [x] La capa semántica resume lo necesario para continuidad IA.
- [x] Las líneas cognitivas abiertas están identificadas.
- [x] La acción de materialización está completada y verificada.
- [x] La decisión derivada está creada y vinculada.
- [x] `ESTADO_PROYECTO` está actualizado.
- [x] Los documentos afectados están listados.
- [x] La rehidratación futura permite retomar el hilo.
- [x] La sesión no contiene estado operativo vivo como única fuente.

## Trazabilidad

- Origen: decisión del usuario de aplicar en `carrera-ai` la retirada de Graphify formalizada en PCS Core.
- Fuente canónica: `C:/Users/gusve/Documents/Apps/project-continuity-system/.pcs/decisiones/DEC-20260715-0004-retirada-graphify-pcs-host.md`.
- Sesión relacionada: `sesion-20260713-1344-integracion-operacion-graphify-carrera-ai.md`.
- Decisión sustituida: `DEC-20260713-1344-001-integrar-graphify-tres-corpus`.
- Decisión creada: `DEC-20260717-1058-001-retirada-graphify-carrera-ai`.
- Estado relacionado: `.pcs/estado/estado-actual.md`.
- Estado de la sesión: cerrada el 2026-07-17 a las 11:40, con la retirada física completada y verificada.
- PCS Core: no modificado.

## Cierre

La sesión queda cerrada tras completar la retirada de Graphify, limpiar las instrucciones operativas, verificar la ausencia de datos derivados y dejar las referencias históricas correctamente señaladas. No quedan acciones abiertas derivadas de esta sesión.
