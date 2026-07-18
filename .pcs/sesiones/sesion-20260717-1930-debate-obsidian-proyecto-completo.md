---
id: sesion-20260717-1930-debate-obsidian-proyecto-completo
titulo: Debate sobre la idoneidad de utilizar Obsidian en todo el proyecto
inicio: 2026-07-17 19:30
cierre:
estado: abierta
tipo: sesion
host: carrera-ai
sesion_relacionada: sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai
---

# Sesión PCS — Debate sobre la idoneidad de utilizar Obsidian en todo el proyecto

## Contexto inmediato

`carrera-ai` utiliza actualmente Obsidian de forma localizada en la carpeta
`boveda-entrevista-profesional/`. Sin embargo, el proyecto contiene otros
documentos Markdown en distintas carpetas que también forman parte del
conocimiento funcional, metodológico y operativo del conjunto.

La motivación de esta sesión es debatir si conviene ampliar el uso de Obsidian
al conjunto de archivos Markdown no excluidos por `.gitignore`, para facilitar
su lectura, navegación, enlace y comprensión relacional sin alterar por ello
la autoridad de cada tipo de documento.

## Objetivo inicial del debate (contexto histórico)

Evaluar la idoneidad, el alcance, los beneficios, los costes y los riesgos de
utilizar Obsidian en todo el proyecto sobre los archivos Markdown no excluidos
por `.gitignore`, en lugar de limitarlo a `boveda-entrevista-profesional/`.

Este objetivo ya se resolvió mediante la [decisión vigente de adopción](../decisiones/DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian.md): se establece una única bóveda raíz con configuración limpia y se retiran, tras una copia externa verificada, las configuraciones y directorios heredados definidos en ella. No quedan pendientes decisiones sobre el modelo de bóveda ni sobre el destino de esos directorios; queda pendiente su implantación controlada.

## Capa episódica

La persona plantea que existen documentos Markdown fuera de
`boveda-entrevista-profesional/` que necesitan leerse de forma cómoda y
enlazarse entre sí para obtener una comprensión más completa del proyecto.

El criterio inicial de alcance indicado es el contenido que no esté excluido
por `.gitignore`. Este criterio debe analizarse antes de decidir la
configuración, la estructura de bóveda, las convenciones de enlaces o la
inclusión de carpetas operativas como `.pcs/`.

## Capa semántica (historial del debate)

Durante el debate se establecieron los siguientes criterios de análisis. Este
apartado conserva el razonamiento histórico; las decisiones resultantes están
formalizadas en la [decisión vigente de adopción](../decisiones/DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian.md).

- Se debatió que la cuestión no consistía solo en instalar o extender una
  herramienta, sino en determinar si una vista relacional común mejoraba la
  comprensión del proyecto.
- Se acordó que el uso transversal de Obsidian no convertiría todos los
  documentos Markdown en fuentes con la misma autoridad.
- Se mantuvo la diferenciación entre documentación funcional, metodología,
  continuidad PCS, decisiones, acciones y artefactos de trabajo.
- Se utilizó `.gitignore` como alcance inicial del debate, sin considerarlo
  suficiente por sí solo para resolver las rutas de navegación, indexación o
  enlace dentro de la bóveda.
- Se decidió adoptar una bóveda raíz con configuración limpia y retirar de
  forma controlada las configuraciones heredadas tras una copia externa
  verificada.
- Se decidió retirar, con la misma salvaguarda, `obsilo-shared/` y
  `vault-operator-shared/`; no se trasladarán a `C:\Users\gusve\Documents\Apps`.

## Actualización histórica — Propuesta documentada y presentación

Se ha elaborado la propuesta
`docs/PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.md` y su presentación de
síntesis `docs/PRESENTACION_PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.pptx`.

La propuesta comparó cuatro alternativas: mantener la bóveda localizada,
abrir la raíz sin política, abrir una bóveda transversal gobernada y crear una
bóveda espejo. En aquel momento recomendó la tercera alternativa: abrir la
raíz de `carrera-ai` como bóveda de navegación, con exclusiones explícitas,
enlaces con ruta cuando existieran nombres repetidos y una migración reversible
de configuración y datos compartidos.

La propuesta distingue expresamente la navegación de la autoridad documental:
Obsidian facilitaría la lectura y los enlaces, pero no alteraría la precedencia
de estado, decisiones, sesiones, documentación funcional o metodología.

Respecto a los directorios, la propuesta inicial planteó migrar o regenerar
parte de la configuración y trasladar los directorios compartidos. Esa
recomendación histórica fue sustituida por la decisión vigente: se retirarán
las cinco rutas heredadas tras una copia externa verificada. No se ha ejecutado
ningún movimiento, eliminación ni cambio de configuración.

La propuesta dejó de ser debatible al aprobarse la decisión PCS y abrirse la
acción de implantación acotada.

## Contexto histórico — cuestiones ya resueltas

Las siguientes fueron líneas de análisis del debate. No representan decisiones
pendientes: su resolución quedó formalizada en la [decisión vigente de
adopción](../decisiones/DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian.md).

- Comparar una bóveda transversal con la bóveda localizada actual.
- Determinar si `.pcs/` debe formar parte de la navegación de Obsidian, aunque
  conserve su naturaleza de memoria operativa y sus reglas de privacidad.
- Identificar qué rutas Markdown quedan realmente dentro del alcance efectivo
  tras aplicar `.gitignore`.
- Evaluar si una bóveda única puede mejorar los enlaces sin aumentar la
  confusión entre fuentes históricas, funcionales y normativas.
- Definir convenciones de wikilinks, enlaces relativos, nombres y exclusiones
  si se adopta el enfoque transversal.
- Considerar el impacto sobre Git, sincronización, plugins, rendimiento,
  privacidad y mantenimiento.
- Establecer el tratamiento de `.obsidian/`, `.obsidian-agent/` y
  `.vault-operator/` dentro de `boveda-entrevista-profesional/`.
- Establecer el destino de `obsilo-shared/` y `vault-operator-shared/`.
- Valorar si la navegación transversal debe ser solo local para Codex/Obsidian
  o si requiere cambios en la estructura documental del repositorio.

## Actualización — Decisión y acción de implantación

La persona responsable aprobó el diseño de reorganización documental y se ha formalizado la [decisión de adopción](../decisiones/DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian.md). La decisión adopta la bóveda raíz con configuración limpia, exige una copia externa verificada antes de retirar las cinco rutas heredadas, prohíbe usar Obsidian CLI y limita los movimientos a bloques previamente aprobados.

También se ha abierto la [acción de implantación](../acciones/ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian.md). Permanece pendiente: no se han movido documentos, eliminado configuraciones ni inicializado la nueva bóveda. La clasificación de cada bloque requerirá aprobación posterior e independiente.

## Acciones derivadas

- Acción: [ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian](../acciones/ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian.md).
- Estado: pendiente.
- Especificación: [diseño de reorganización documental y nueva bóveda Obsidian](../../docs/superpowers/specs/2026-07-18-reorganizacion-documental-obsidian-design.md).

## Decisiones derivadas

- Decisión: [DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian](../decisiones/DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian.md).
- Estado: vigente.
- Especificación: [diseño de reorganización documental y nueva bóveda Obsidian](../../docs/superpowers/specs/2026-07-18-reorganizacion-documental-obsidian-design.md).

## Problemas o bloqueos

- Debe crearse y verificarse una copia externa completa antes de retirar las
  cinco rutas heredadas.
- Cada bloque documental necesita un mapa de clasificación y la aprobación de
  la persona responsable antes de mover documentos o corregir sus enlaces.
- La inicialización de la bóveda raíz y la configuración de Hide Folders
  requieren la intervención manual de la persona responsable después de que
  no queden configuraciones Obsidian anidadas.
- No debe confundirse la conveniencia de leer y enlazar documentos con la
  autorización para modificar su contenido o su gobernanza.

## Documentos afectados

- `.gitignore`.
- `boveda-entrevista-profesional/` como ámbito actual de Obsidian.
- `boveda-entrevista-profesional/.obsidian/`.
- `boveda-entrevista-profesional/.obsidian-agent/`.
- `boveda-entrevista-profesional/.vault-operator/`.
- `obsilo-shared/` y `vault-operator-shared/` en la raíz actual del proyecto.
- `.pcs/` y sus reglas locales, incluidas en la navegación de la bóveda raíz
  por decisión vigente.
- `docs/` y demás carpetas con archivos Markdown no ignorados, como posibles
  fuentes del conocimiento transversal.
- Esta sesión PCS.
- `docs/PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.md`.
- `docs/PRESENTACION_PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.pptx`.

## Rehidratación futura

- Dónde quedó el trabajo: se adoptó la reorganización documental y una única
  bóveda raíz de Obsidian mediante una [decisión vigente](../decisiones/DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian.md). La [acción de implantación](../acciones/ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian.md) permanece pendiente y no se han realizado movimientos, eliminaciones ni cambios de configuración.
- Leer primero: `.gitignore`, `.pcs/AGENTS.md`, `README.md`,
  `docs/AGENTS.md`, la [decisión vigente](../decisiones/DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian.md), la [acción pendiente](../acciones/ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian.md) y la especificación aprobada.
- Líneas abiertas a retomar: verificación de la copia externa, inventario y
  mapa de clasificación, aprobación humana de cada bloque, configuración
  manual de la bóveda raíz y corrección de enlaces tras los movimientos
  aprobados.
- Riesgos de malinterpretación: Obsidian sería una herramienta de lectura y
  navegación; no sustituye PCS Core, el estado actual, las decisiones ni las
  autoridades documentales del proyecto.
- Siguiente gesto recomendado: ejecutar la [acción de implantación](../acciones/ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian.md) empezando por el inventario y el mapa de clasificación; no mover ni eliminar archivos hasta contar con la aprobación de cada bloque y una copia externa verificada.

## Checklist de consolidación

- [x] La capa episódica registra el motivo y el alcance inicial del debate.
- [x] La capa semántica separa navegación documental de autoridad documental.
- [ ] Las líneas cognitivas abiertas están identificadas.
- [x] Las acciones derivadas están creadas o marcadas como pendientes.
- [x] Las decisiones derivadas están creadas o marcadas como pendientes.
- [x] `ESTADO_PROYECTO` está actualizado o marcado como pendiente.
- [x] Los documentos afectados están listados.
- [x] La rehidratación futura permite retomar el hilo.
- [ ] La sesión no contiene estado operativo vivo como única fuente.

## Trazabilidad

- Origen: petición de crear una sesión PCS para debatir el uso transversal de
  Obsidian en `carrera-ai`.
- Sesiones relacionadas:
  - `sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai.md`.
  - `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`.
- Acciones relacionadas: [ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian](../acciones/ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian.md).
- Decisiones relacionadas: [DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian](../decisiones/DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian.md).
- Estado de proyecto relacionado: [estado actual](../estado/estado-actual.md).
- Especificación aprobada: [diseño de reorganización documental y nueva bóveda Obsidian](../../docs/superpowers/specs/2026-07-18-reorganizacion-documental-obsidian-design.md).
- Entregables de debate:
  - `docs/PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.md`.
  - `docs/PRESENTACION_PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.pptx`.
- Cierre: sesión abierta; decisión vigente y acción de implantación pendiente.
