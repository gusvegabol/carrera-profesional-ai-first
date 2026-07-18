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

## Objetivo

Evaluar la idoneidad, el alcance, los beneficios, los costes y los riesgos de
utilizar Obsidian en todo el proyecto sobre los archivos Markdown no excluidos
por `.gitignore`, en lugar de limitarlo a `boveda-entrevista-profesional/`.

La sesión deberá permitir decidir, en una fase posterior, si se mantiene el
alcance actual, se amplía Obsidian al proyecto completo o se adopta una
solución intermedia con límites explícitos.

También deberá resolver el destino de las configuraciones y directorios de
soporte de Obsidian que viven hoy dentro de
`boveda-entrevista-profesional/`, así como la conveniencia de reubicar los
directorios compartidos de Vault Operator fuera de la raíz del proyecto.

## Capa episódica

La persona plantea que existen documentos Markdown fuera de
`boveda-entrevista-profesional/` que necesitan leerse de forma cómoda y
enlazarse entre sí para obtener una comprensión más completa del proyecto.

El criterio inicial de alcance indicado es el contenido que no esté excluido
por `.gitignore`. Este criterio debe analizarse antes de decidir la
configuración, la estructura de bóveda, las convenciones de enlaces o la
inclusión de carpetas operativas como `.pcs/`.

## Capa semántica

- La cuestión no es solo instalar o extender una herramienta, sino determinar
  si una vista relacional común mejora la comprensión del proyecto.
- El posible uso transversal de Obsidian no debe convertir todos los
  documentos Markdown en fuentes con la misma autoridad.
- Deben mantenerse diferenciadas la documentación funcional, la metodología,
  la continuidad PCS, las decisiones, las acciones y los artefactos de trabajo.
- `.gitignore` define el alcance inicial indicado para el debate, pero no
  resuelve por sí solo qué carpetas deben abrirse, indexarse o enlazarse dentro
  de una bóveda.
- La exclusión de configuraciones internas de Obsidian en
  `boveda-entrevista-profesional/` no implica todavía una decisión sobre la
  configuración futura de una bóveda transversal.
- Los directorios `.obsidian/`, `.obsidian-agent/` y `.vault-operator/` que
  residen dentro de `boveda-entrevista-profesional/` requieren una decisión de
  destino: conservarlos allí, migrar una configuración pertinente o retirarlos
  de forma controlada si dejan de tener función.
- `obsilo-shared/` y `vault-operator-shared/` están hoy en la raíz de
  `carrera-ai`; debe evaluarse si corresponde moverlos a
  `C:\Users\gusve\Documents\Apps`, donde suelen situarse las carpetas
  compartidas de una bóveda gestionada mediante el plugin Vault Operator.

## Actualización — Propuesta documentada y presentación

Se ha elaborado la propuesta
`docs/PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.md` y su presentación de
síntesis `docs/PRESENTACION_PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.pptx`.

La propuesta compara cuatro alternativas: mantener la bóveda localizada,
abrir la raíz sin política, abrir una bóveda transversal gobernada y crear una
bóveda espejo. Recomienda la tercera alternativa: abrir la raíz de
`carrera-ai` como bóveda de navegación, con exclusiones explícitas, enlaces
con ruta cuando existan nombres repetidos y una migración reversible de
configuración y datos compartidos.

La propuesta distingue expresamente la navegación de la autoridad documental:
Obsidian facilitaría la lectura y los enlaces, pero no alteraría la precedencia
de estado, decisiones, sesiones, documentación funcional o metodología.

Respecto a los directorios, la recomendación no es borrar: `.obsidian/` debe
migrarse selectivamente a la nueva raíz; `.vault-operator/` debe migrarse o
regenerarse tras respaldo; `.obsidian-agent/` requiere inventario antes de
actuar; y `obsilo-shared/` junto con `vault-operator-shared/` deben trasladarse
de forma controlada al directorio `Apps` si se adopta la nueva raíz de bóveda.
No se ha ejecutado ningún movimiento, eliminación ni cambio de configuración.

La recomendación sigue siendo una propuesta debatible. Su adopción requerirá
una decisión PCS explícita y una acción de implantación acotada.

## Ideas y líneas cognitivas abiertas

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
- Decidir el tratamiento de `.obsidian/`, `.obsidian-agent/` y
  `.vault-operator/` dentro de `boveda-entrevista-profesional/`: conservar,
  migrar parcialmente, regenerar para una nueva bóveda o retirar.
- Decidir si `obsilo-shared/` y `vault-operator-shared/` deben trasladarse a
  `C:\Users\gusve\Documents\Apps` para ubicarlos en el nivel superior de la
  carpeta gestionada por Obsidian con Vault Operator, o si existe una opción
  más adecuada que preserve su funcionamiento.
- Valorar si la navegación transversal debe ser solo local para Codex/Obsidian
  o si requiere cambios en la estructura documental del repositorio.

## Acciones derivadas

- Acción: pendiente de determinar tras el debate.
- Estado: no creada en esta apertura.
- Enlace: no aplica.

## Decisiones derivadas

- Decisión: pendiente de determinar tras el debate.
- Estado: no creada en esta apertura.
- Enlace: no aplica.

## Problemas o bloqueos

- Aún no se ha evaluado el conjunto exacto de Markdown alcanzable según las
  reglas de `.gitignore`.
- No está decidido si la navegación transversal exige una única bóveda, una
  bóveda adicional o una configuración más limitada.
- No se ha determinado la función efectiva ni el carácter regenerable de los
  directorios internos de Obsidian y Vault Operator antes de decidir si se
  conservan, migran o eliminan.
- No se ha comprobado todavía si mover `obsilo-shared/` y
  `vault-operator-shared/` al directorio común de aplicaciones conserva todas
  las referencias, permisos y rutas requeridas por Vault Operator.
- No debe confundirse la conveniencia de leer y enlazar documentos con la
  autorización para modificar su contenido o su gobernanza.

## Documentos afectados

- `.gitignore`.
- `boveda-entrevista-profesional/` como ámbito actual de Obsidian.
- `boveda-entrevista-profesional/.obsidian/`.
- `boveda-entrevista-profesional/.obsidian-agent/`.
- `boveda-entrevista-profesional/.vault-operator/`.
- `obsilo-shared/` y `vault-operator-shared/` en la raíz actual del proyecto.
- `.pcs/` y sus reglas locales, si el debate concluye que deben incluirse en
  la navegación.
- `docs/` y demás carpetas con archivos Markdown no ignorados, como posibles
  fuentes del conocimiento transversal.
- Esta sesión PCS.
- `docs/PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.md`.
- `docs/PRESENTACION_PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.pptx`.

## Rehidratación futura

- Dónde quedó el trabajo: se ha abierto el debate sobre ampliar Obsidian al
  conjunto de Markdown no excluido por `.gitignore`, incluido el destino de
  sus directorios de configuración y soporte actuales. Existe una propuesta
  comparativa que recomienda la alternativa de bóveda transversal gobernada,
  todavía pendiente de adopción explícita.
- Leer primero: `.gitignore`, `.pcs/AGENTS.md`, `README.md`,
  `docs/AGENTS.md` y la configuración/documentación de
  `boveda-entrevista-profesional/` relacionada con Obsidian; después,
  `docs/PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.md`.
- Líneas abiertas a retomar: alcance efectivo, inclusión de `.pcs/`, modelo de
  bóveda, convenciones de enlaces, destino de `.obsidian/`,
  `.obsidian-agent/` y `.vault-operator/`, posible traslado de
  `obsilo-shared/` y `vault-operator-shared/`, riesgos y alternativa
  recomendada.
- Riesgos de malinterpretación: Obsidian sería una herramienta de lectura y
  navegación; no sustituye PCS Core, el estado actual, las decisiones ni las
  autoridades documentales del proyecto.
- Siguiente gesto recomendado: debatir y decidir si se adopta la alternativa
  recomendada. Si se aprueba, abrir una acción PCS limitada a inventario,
  respaldo y bóveda piloto antes de modificar, mover o eliminar
  configuraciones.

## Checklist de consolidación

- [x] La capa episódica registra el motivo y el alcance inicial del debate.
- [x] La capa semántica separa navegación documental de autoridad documental.
- [ ] Las líneas cognitivas abiertas están identificadas.
- [ ] Las acciones derivadas están creadas o marcadas como pendientes.
- [ ] Las decisiones derivadas están creadas o marcadas como pendientes.
- [ ] `ESTADO_PROYECTO` está actualizado o marcado como pendiente.
- [x] Los documentos afectados están listados.
- [x] La rehidratación futura permite retomar el hilo.
- [ ] La sesión no contiene estado operativo vivo como única fuente.

## Trazabilidad

- Origen: petición de crear una sesión PCS para debatir el uso transversal de
  Obsidian en `carrera-ai`.
- Sesiones relacionadas:
  - `sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai.md`.
  - `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`.
- Acciones relacionadas: ninguna creada.
- Decisiones relacionadas: ninguna creada.
- Estado de proyecto relacionado: `.pcs/estado/estado-actual.md`, sin
  modificación en esta apertura.
- Entregables de debate:
  - `docs/PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.md`.
  - `docs/PRESENTACION_PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.pptx`.
- Cierre: sesión abierta; pendiente de decisión y, si procede, de una acción
  de implantación.
