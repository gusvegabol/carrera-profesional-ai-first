---
id: estado-actual
titulo: carrera-profesional-ai-first
estado: vigente
fecha_actualizacion: 2026-07-12
ultima_sesion_relacionada: sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai
host: carrera-ai
---

# estado-actual

## Situación actual

La capa PCS del host ya no está solo en arranque mínimo: existe una sesión marco de alcance MVP y una sesión específica de Fase 1 para consolidar el objetivo real del MVP de `Carrera Profesional AI-First` como sistema AI-First apoyado en ChatGPT, CODEX, Notion, Drive y PCS.

La Fase 1 ya quedó materializada como paquete documental revisable y ahora se está evaluando la base funcional del host, con `docs/DOCUMENTO_SPEC_CARRERA_AI.md` como referencia principal visible.

La capa operativa ha detectado una desviación respecto a la idea original: el proyecto no debe quedarse en documentos mínimos ni en preguntas genéricas. El foco se ha corregido hacia la entrevista conversacional profunda como capacidad nuclear del sistema y, ahora, hacia la captura de la carrera completa de la persona mediante un Perfil Profesional Accionable. La bóveda `boveda-entrevista-profesional/` ya quedó consolidada como paso previo al playbook.

La bóveda ya quedó creada y validada, y la trazabilidad del reenfoque también quedó validada por ChatGPT. El siguiente trabajo recomendado empieza por `01_conceptos/` y `04_patrones_de_preguntas/`, mientras la base funcional principal visible del host queda en `docs/DOCUMENTO_SPEC_CARRERA_AI.md`.

PCS canónico no se modifica en este reajuste. La memoria operativa del host sigue viviendo en `.pcs/`.

La fase de trabajo reciente consolidó además que el MVP debe concretarse como un primer piloto de entrevista profesional profunda ejecutado por ChatGPT, con salida mínima de competencia profesional con evidencia verificable y reglas explícitas de gobierno para la conversación. La evolución actual ya no apunta solo a un concepto bien definido, sino a una entrevista capaz de capturar la carrera completa de la persona. La bóveda de entrevista ya quedó normalizada en sus `README.md` con la convención de nombres semánticos por carpeta.

La comprobación de gobernanza del host quedó aprobada tras actualizar `AGENTS.md` y `README.md`, sin duplicar PCS Core ni alterar la capa `.pcs/`.

En la revisión funcional inicial se comprobó que `docs/alcance-mvp.md` ya no existe. La referencia funcional principal visible ahora es `docs/DOCUMENTO_SPEC_CARRERA_AI.md`, mientras la bóveda de entrevista profesional actúa como soporte metodológico y documental del sistema.

Dictamen provisional: `docs/DOCUMENTO_SPEC_CARRERA_AI.md` queda como documento funcional principal del host; la bóveda no lo sustituye, sino que lo alimenta y complementa.

El trabajo actual pendiente del proyecto ya no es reescribir el `SPEC`, sino diseñar la nueva metodología de entrevista para capturar la carrera completa de una persona dentro del Perfil Profesional Accionable.

La sesión marco de alcance MVP sigue abierta como referencia de base para el arranque del proyecto, pero ya no es la línea central de trabajo. La sesión de Fase 1 ya quedó cerrada y pasó a ser referencia histórica. La referencia viva principal ha pasado a la línea metodológica de cobertura y al núcleo metodológico del Perfil Profesional Accionable.

Se abre ahora una nueva sesión para adaptar la parte funcional del host desde dentro del proyecto, con foco en la documentación propia y en el encaje honesto de `docs/DOCUMENTO_SPEC_CARRERA_AI.md`.

## Foco operativo

Definir el concepto de cobertura profesional y separar con precisión profundidad de cobertura, usando la bóveda de entrevista profesional como base de profundidad y la nueva sesión conceptual como espacio de diseño de la siguiente capa.

## Próximos pasos

- Desarrollar `boveda-entrevista-profesional/01_conceptos/CONCEPTO_COBERTURA_PROFESIONAL.md` como puente entre profundidad y cobertura.
- Tomar `sesion-20260705-concepto-cobertura-profesional-carrera-ai.md` como antecedente para decidir qué significa un mapa inicial razonable de trayectoria dentro de la línea núcleo actual.
- Mantener `PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA` como playbook de profundidad mientras la cobertura queda en diseño.
- Inventariar la documentacion funcional propia del host y decidir si `docs/DOCUMENTO_SPEC_CARRERA_AI.md` requiere refinamiento o un índice funcional adicional.
- Mantener `docs/DOCUMENTO_SPEC_CARRERA_AI.md` como referencia central funcional mientras se decide si requiere refinamiento o un índice funcional adicional.
- Definir si la nueva sesión funcional requiere una segunda sesión material para cambios documentales.

## Acciones abiertas relevantes

- No hay acciones formales registradas todavía.
- Queda como acción candidata desarrollar el concepto de cobertura profesional y decidir si luego pide patrón, método o capa superior adicional.

## Decisiones vigentes relevantes

- `hosts/hosts.yaml` registra `carrera-ai` como host PCS.
- La carpeta `.pcs/` es la memoria operativa del host.
- Se mantiene la separación de capas entre PCS canónico, proyecto anfitrión, `.pcs/`, Notion, Drive y CODEX.
- `PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA` sigue gobernando la profundidad.
- La cobertura profesional se trata como una capa superior en diseño, no como sustituto del playbook actual.

## Bloqueos o riesgos

- El propósito funcional local del host sigue pendiente de consolidación en artefactos base del repositorio.
- Existe riesgo de volver a derivar hacia desarrollar una aplicación propia antes de validar el sistema AI-First.
- Existe riesgo de ampliar el proyecto hasta convertirlo en un segundo cerebro generalista en lugar de mantener el foco en carrera profesional.
- Existe riesgo de seguir haciendo pilotos de profundidad como si ya resolvieran cobertura.
- Si la entrevista no funciona, el enfoque AI-First conversacional no justifica continuar.
- Notion no debe confundirse con estado vivo ni sustituir sin criterio a la capa `.pcs/`.
- `.tmp/` queda excluida por defecto del uso operativo y de lectura salvo autorización explícita.

## Referencias históricas

- `sesion-20260618-2300-primera-sesion-MVP-desarrollo-idea.md`: sesión inicial ya cerrada y superada por el alcance MVP.
- `sesion-20260630-fase-1-objetivo-real-mvp-carrera-ai.md`: fase cerrada que consolidó el objetivo real del MVP.
- `sesion-20260630-alcance-mvp-carrera-ai.md`: sesión base del alcance MVP; conserva valor de contexto, pero ya no es la línea principal.
- `sesion-20260705-concepto-cobertura-profesional-carrera-ai.md`: sesión fundacional del concepto de cobertura; útil como antecedente, pero el trabajo vivo ya está en la línea núcleo.

## Nota de vigencia

Estado actualizado a partir de la materialización de la Fase 1. Refleja líneas vigentes y candidatas, no decisiones ni acciones ya formalizadas.

## Trazabilidad

- Última sesión: sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai
- Sesión anterior cerrada: sesion-20260630-fase-1-objetivo-real-mvp-carrera-ai
- Línea histórica de base: sesion-20260630-alcance-mvp-carrera-ai
- Línea histórica fundacional: sesion-20260705-concepto-cobertura-profesional-carrera-ai
- Nueva sesión abierta: sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai
- Origen del cambio: materialización de la Fase 1 del alcance MVP en sesión específica y evolución hacia la línea núcleo metodológica
- Documentos creados o modificados:
  - .pcs/estado/estado-actual.md
  - .pcs/sesiones/sesion-20260630-fase-1-objetivo-real-mvp-carrera-ai.md
  - .pcs/sesiones/sesion-20260630-alcance-mvp-carrera-ai.md
  - .pcs/sesiones/sesion-20260618-2300-primera-sesion-MVP-desarrollo-idea.md
  - docs/alcance-mvp.md
  - README.md
  - boveda-entrevista-profesional/README.md y README de sus carpetas

## Actualización — Cadena documental de cobertura profesional y consolidación v2_0_0

La trazabilidad de cobertura profesional queda ahora alineada con la secuencia documental manual ya creada en la bóveda:

- `DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v1.md`: primera definición operativa de cobertura como mapa inicial no exhaustivo, línea ChatGPT.
- `DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_1.md`: línea Claude, centrada en arquitectura multi-sesión, checkpoint, calibración de tiempo y reanudación.
- `DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_2.md`: primera síntesis explícita entre la línea ChatGPT y la línea Claude.
- `DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_3.md`: versión intermedia de consolidación, con integración de `PATRON_STAR_SIMPLE` y control de escaneo.
- `DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v2_0_0.md`: versión consolidada vigente y referencia actual para la definición MVP del futuro playbook de cobertura profesional.

La referencia vigente pasa a ser `v2_0_0`, sin borrar la trazabilidad de las versiones previas. La capa de cobertura queda definida como orquestación multi-sesión separada del playbook de profundidad `v1.3.2`, con estos estados canónicos del mapa: `explorada`, `candidata`, `parcial` y `pendiente`.

La línea viva actual para diseñar la nueva entrevista de cobertura es `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`, con `sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md` y `sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai.md` como ramas activas de trabajo.

La arquitectura de escaneo queda separada en tres pisos:

- panorámica abierta;
- `PATRON_STAR_SIMPLE` como prevalidación ligera;
- `PATRON_STAR_AMPLIADO` o `PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA` cuando procede una inmersión profunda.

Se mantiene la regla de volumen: `PATRON_STAR_SIMPLE` se aplica, como máximo, a una o dos candidatas por sesión de escaneo y nunca a todas las candidatas detectadas.

Queda como foco posterior, si procede, derivar un futuro `PLAYBOOK_COBERTURA_PROFESIONAL`, pero todavía no existe como playbook operativo final.

## Actualización — Entrevista piloto Herfrailes RRHH

Ya existe una primera entrevista piloto real/simulada-operativa registrada en la bóveda de entrevista profesional.

El caso de `Herfrailes SL` produjo una competencia profesional profunda con evidencia fuerte:

- `Diseño de sistemas internos socio-técnicos`
- creación desde cero de un sistema interno de RRHH con automatización, normativa y experiencia del personal integradas

El playbook `PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA` queda validado parcialmente para seguir probando, no aprobado definitivamente.

El foco inmediato pasa a revisar el documento creado y decidir si conviene una segunda entrevista con otra tensión o un ajuste mínimo del método.

PCS canónico no se modifica en este reajuste.
La memoria operativa del host sigue viviendo en `.pcs/`.

## Actualización — Auditoría transversal de trazabilidad documental

Se ejecutó una auditoría transversal de `boveda-entrevista-profesional/` frente a la memoria operativa `.pcs/` para comprobar qué capas nuevas ya estaban recogidas y cuáles seguían desalineadas.

### Ya recogido en `.pcs/`

- La separación entre profundidad y cobertura profesional ya está asentada.
- La sesión conceptual `sesion-20260705-concepto-cobertura-profesional-carrera-ai.md` queda como antecedente fundacional; la referencia viva de cobertura pasa a `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`.
- Los pilotos tardíos `PILOTO_004_ENTREVISTA_EMPRESA_FAMILIAR.md` y `PILOTO_005_ENTREVISTA_REPONEDOR_SUPERMERCADO.md` ya quedaron incorporados como evidencia tardía.
- La secuencia documental `v1 -> v1_0_1 -> v1_0_2 -> v1_0_3 -> v2_0_0` de cobertura profesional ya figura como trazabilidad vigente.
- La carpeta `artefactos-cobertura-profesional/` ya quedó registrada como capa viva de ejecución.

### Recogido solo parcialmente

- `.pcs/estado/estado-actual.md` menciona la carpeta viva de cobertura, pero no detalla todavía sus reglas internas de IDs, plantillas y ciclo operativo.
- La sesión abierta de cobertura sigue hablando de la estructura viva, pero no cita el conjunto completo de capas nuevas de la bóveda.
- La auditoría detectó que el estado aún no refleja la existencia del primer playbook operativo de cobertura `07_playbook/PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_0.md`.

### No recogido todavía

- `08_entrevistas_piloto/PILOTO_002_ENTREVISTA_HERFRAILES_INFORMATICA.md` existe como primer registro empírico real y no aparece individualizado en el estado.
- La bóveda ya contiene más documentos activos en `01_conceptos/` y `04_patrones_de_preguntas/` de los que el estado resume hoy.
- `08_fuentes/` ya tiene fuentes de base que sostienen los conceptos y patrones nuevos, pero todavía no se reflejan en la memoria operativa.
- `artefactos-cobertura-profesional/entrevistados/README.md` ya fija una política mínima para entrevistados, pero esa capa aún no aparece en el estado.
- `artefactos-cobertura-profesional/_contadores.md` no existe todavía, pese a que el README de la carpeta lo da por necesario.

### Riesgos vigentes

- Hay deriva entre la bóveda real, sus README de carpeta y la memoria `.pcs/`.
- El árbol documental ya se adelantó al resumen de estado, así que una futura rehidratación debe leer la bóveda con más detalle antes de confiar en un resumen.
- La presencia de `PILOTO_002` introduce datos reales sensibles y conviene tratar esa pieza con cuidado operativo.

### Siguiente gesto recomendado

Mantener esta sesión de cobertura abierta como referencia conceptual y, cuando el flujo lo autorice, actualizar la documentación de trazabilidad de la bóveda para que su índice y sus README no sigan por detrás del inventario real.

## Trazabilidad adicional

- Nueva sesión de mantenimiento documental: `sesion-20260708-actualizacion-documentacion-solicitada-usuario-carrera-ai.md`
- Origen: auditoría transversal de `boveda-entrevista-profesional/` solicitada por el usuario
- Estado de la bóveda: más desarrollada que el resumen histórico previo de `.pcs/`, pero todavía con desajustes documentales menores

## Actualización — Estructura de artefactos de cobertura profesional

Queda registrada la consolidación de `boveda-entrevista-profesional/artefactos-cobertura-profesional/` como carpeta no numerada de ejecución y aplicacion dentro de la bóveda de entrevista profesional.

Su función es almacenar artefactos generados por procesos de cobertura profesional entre IA y humano, mientras la documentación metodológica permanece en las carpetas numeradas de la bóveda.

La estructura verificada incluye estas subcarpetas:

- `checkpoints/`: estados parciales de inmersiones interrumpidas.
- `competencias/`: una ficha por cada zona que llega a estado `explorada`.
- `inmersiones/`: fichas completas cuando cobertura invoca profundidad.
- `mapas/`: mapas vivos de cobertura.
- `sesiones/`: registros de sesiones de cobertura, si se decide conservarlos.
- `templates/`: plantillas para crear artefactos homogéneos.

Tambien queda verificada la existencia de `boveda-entrevista-profesional/artefactos-cobertura-profesional/README.md` y de los templates operativos con frontmatter YAML:

- `boveda-entrevista-profesional/artefactos-cobertura-profesional/templates/TEMPLATE_MAPA.md`
- `boveda-entrevista-profesional/artefactos-cobertura-profesional/templates/TEMPLATE_SESION.md`
- `boveda-entrevista-profesional/artefactos-cobertura-profesional/templates/TEMPLATE_INMERSION.md`
- `boveda-entrevista-profesional/artefactos-cobertura-profesional/templates/TEMPLATE_CHECKPOINT.md`
- `boveda-entrevista-profesional/artefactos-cobertura-profesional/templates/TEMPLATE_COMPETENCIA.md`

Los templates incorporan frontmatter para identificacion, estado, fechas y relaciones entre artefactos, incluyendo campos como `id`, `tipo`, `estado`, `fecha_creacion`, `fecha_actualizacion`, `fecha_cierre`, `id_entrevistado`, `id_mapa`, `id_zona`, `id_inmersion` e `id_competencia`, segun corresponda.

Queda en debate o pendiente de cierre el detalle fino de identificadores, entrevistados, zonas y la relacion con otros documentos de la bóveda; esta actualización solo deja constancia de la estructura ya creada y de su separacion entre conocimiento metodologico y ejecucion operativa.

## Actualización — Piloto dirigido GESCAN

Ya existe `PILOTO_003_ENTREVISTA_GESCAN.md` como piloto dirigido realizado con otra IA conversacional.

El piloto confirma la utilidad del formato de piloto dirigido, donde la persona entrevistada provoca tensiones no reveladas hasta después del cierre.

Aporta evidencia metodológica sobre dos puntos:

- `ANTIPATRON_RIGOR_SIN_AMORTIGUACION`: reconocer antes de pedir más evidencia.
- Mantener foco ante saltos temporales y datos de bajo valor.

La competencia extraída fue `Aprendizaje profundo dirigido a la resolución, con trazabilidad de diseño`.

El playbook `PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA` queda reforzado parcialmente, pero no aprobado definitivamente.

Siguiente paso recomendado: incorporar estas reglas en una futura revisión del playbook o preparar un nuevo piloto con otra tensión no probada.

## Actualización tardía — Pilotos 004 y 005 como evidencia previa al cierre de Fase 1

Quedan ahora regularizados como evidencia tardía, ocurrida fuera de PCS entre `PILOTO_003` y el cierre de Fase 1, dos trabajos que ya existían en la bóveda:

- `PILOTO_004_ENTREVISTA_EMPRESA_FAMILIAR`: primer piloto real con una persona distinta al arquitecto de la bóveda. La entrevista mostró una fricción de parquedad frente a posible desinterés, dejó una unidad profesional de valor con evidencia media y dio lugar a `FRICCION_AMBIGUEDAD_PARQUEDAD_O_DESINTERES`.
- `PILOTO_005_ENTREVISTA_REPONEDOR_SUPERMERCADO`: segundo piloto con una verdad de fondo conocida de antemano y no revelada durante la sesión. La entrevista validó `ANTIPATRON_AISLAMIENTO_FORZADO_DEL_MERITO` en su preparación y dejó como hueco estructural el segundo componente de cobertura, que no apareció dentro del hilo de profundidad. De ese hueco surge `ANTIPATRON_CIERRE_ANCLADO_AL_HILO_UNICO`.

La cobertura profesional pasa así a apoyarse en una ausencia empírica, no en una hipótesis teórica. El remedio de apertura ya quedó incorporado en el playbook como permiso explícito de salida desde el inicio.

## Actualización — Separación entre ejemplos y entrevistas piloto

La bóveda ya distingue con claridad entre materiales de ejemplo y entrevistas piloto.

- `06_ejemplos/` queda reservado para ejemplos didácticos, sintéticos, anotados o calibradores.
- `08_entrevistas_piloto/` queda reservado para entrevistas piloto reales o semi-reales usadas como evidencia parcial de validación del método.
- `PILOTO_001_ENTREVISTA_HERFRAILES_RRHH.md` queda como primer piloto registrado del MVP.
- El piloto Herfrailes mantiene evidencia fuerte sobre la competencia `Diseño de sistemas internos socio-técnicos`.
- El playbook `PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA` sigue validado parcialmente para seguir probando, no aprobado definitivamente.
- El foco inmediato sigue siendo revisar el piloto y decidir una segunda entrevista con otra tensión o un ajuste mínimo del método.

PCS canónico no se modifica en este reajuste.
La memoria operativa del host sigue viviendo en `.pcs/`.

## Actualización — Simulación 000 de cobertura y rehidratación viva

La simulación `boveda-entrevista-profesional/artefactos-cobertura-profesional/sesiones/SESION_COBERTURA_0000_20260708_1730.md` queda registrada como evidencia metodológica reciente, no como entrevista real. No debe leerse como competencia profesional confirmada ni como mapa operativo válido para uso con entrevistados reales.

La línea viva actual sigue siendo cobertura profesional. La sesión principal de trabajo y rehidratación es `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`, con `sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md` y `sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai.md` como ramas activas.

`TEMPLATE_SESION.md` ya incorpora la sección de hilos abiertos y competencias candidatas para la próxima sesión, y `graphify` quedó actualizado como apoyo de navegación y rehidratación, no como fuente única de verdad.

La prioridad siguiente es corregir y refinar el playbook de cobertura antes de usarlo con entrevistados reales.

## Actualización — Cierre de Fase 1 y apertura de cobertura profesional

La Fase 1 / MVP-A queda cerrada como hipótesis mínima validada. Los pilotos 001-005 siguen siendo evidencia útil de profundidad, pero ya no son el siguiente objetivo por sí mismos.

El nuevo foco pasa a la cobertura profesional: construir un mapa inicial razonable de competencias y zonas pendientes, distinguiendo con claridad entre profundidad y cobertura.

La nueva sesión viva relacionada es `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`.

La cobertura profesional deja de ser solo una idea de arquitectura porque `PILOTO_005` mostró un hueco real: una dimensión profesional conocida de antemano no emergió durante la entrevista de profundidad y, desde dentro del texto, no había señales suficientes para detectarlo.

El concepto de cobertura profesional queda documentado en `boveda-entrevista-profesional/01_conceptos/CONCEPTO_COBERTURA_PROFESIONAL.md`.

PCS canónico no se modifica en este reajuste.
La memoria operativa del host sigue viviendo en `.pcs/`.

## Actualización — Propuesta documentada de regla de numeración para artefactos de cobertura

Ya existe un documento específico para concentrar la propuesta mejorada de numeración y trazabilidad interna de `artefactos-cobertura-profesional/`:

- `boveda-entrevista-profesional/artefactos-cobertura-profesional/REGLA_NUMERACION_ARTEFACTOS.md`

Su finalidad es reunir en una sola pieza:

- la propuesta de identificadores de entrevistado, mapa, zona, sesión, inmersión y competencia;
- la ubicación y semántica de los contadores;
- el criterio operativo de qué significa que un artefacto haya sido realmente creado;
- la relación entre `checkpoint` e `inmersión`;
- el impacto que tendría adoptar esa regla sobre templates y README de la carpeta.

Esta pieza todavía no debe leerse como convención vigente del sistema. Por ahora queda registrada como propuesta a debatir antes de adaptar:

- `artefactos-cobertura-profesional/templates/`;
- `artefactos-cobertura-profesional/templates/README.md`;
- `artefactos-cobertura-profesional/README.md`.

El estado real del proyecto en esta línea es, por tanto, intermedio:

- la necesidad de corregir la numeración de artefactos ya está identificada;
- la propuesta mejorada ya está escrita y guardada en documento propio;
- la adopción de esa regla y su traducción a templates y estructura viva sigue pendiente de decisión.

PCS canónico no se modifica en este reajuste.
La memoria operativa del host sigue viviendo en `.pcs/`.

## Actualización — Apertura de sesión sobre núcleo metodológico y Perfil Profesional Accionable

Se abre `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md` como nueva línea de trabajo para preparar el próximo playbook de cobertura profesional.

Su objetivo es orientar la cobertura hacia la construcción progresiva de un Perfil Profesional Accionable: una representación viva de la trayectoria, experiencias, competencias, herramientas, uso de IA, evidencias, patrones, preferencias, opciones, narrativas, brechas, preguntas pendientes y correspondencias ESCO candidatas de una persona.

La nueva sesión toma como base `docs/DOCUMENTO_SPEC_CARRERA_AI.md`, `docs/Núcleo Metodológico del Playbook/PERFIL_PROFESIONAL_ACCIONABLE_Y_EQUIVALENCIA_ESCO.md` y los documentos de la raíz de `docs/Núcleo Metodológico del Playbook/`. No sustituye la sesión conceptual previa de cobertura ni modifica el playbook de profundidad vigente.

Las decisiones de partida quedan fijadas así:

- la entrevista es el mecanismo de captura; el Perfil Profesional Accionable es el resultado que debe alimentar;
- la cobertura sigue siendo distinta de la profundidad y debe invocarla cuando haga falta evidencia robusta;
- ESCO se tratará como correspondencia candidata, explicable y revisable, nunca como asignación automática definitiva;
- la próxima fase debe definir primero el modelo de información, los umbrales de evidencia, la incertidumbre y la validación antes de rediseñar artefactos, identificadores o playbooks operativos.

El siguiente gesto recomendado es elaborar una matriz entre las capas del Perfil Profesional Accionable y el núcleo metodológico para decidir qué información se captura, con qué técnica, qué evidencia exige y qué relación ESCO puede proponerse.

## Actualización — Apertura de línea de investigación operativa ESCO

Se abre `sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md` como sesión hija de `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`.

Su objetivo es aislar el subproblema de cómo obtener correspondencias ESCO candidatas a partir de una competencia, habilidad, ocupación, profesión o formulación profesional. Esta línea puede avanzar en paralelo a la SPEC general del playbook de cobertura profesional.

La decisión de partida es que ESCO no debe usarse como asignación automática definitiva, sino como correspondencia candidata, explicable, trazable, versionada y revisable.

Esta línea alimentará principalmente la Fase 2 del Perfil Profesional Accionable:

- Fase 1: primera versión útil del perfil sin ESCO.
- Fase 2: primera versión útil del perfil con correspondencias ESCO candidatas.
- Fase 3: perfil completo por ciclos, con ESCO integrado como capa revisable.

El siguiente gesto recomendado es investigar el uso oficial de ESCO en aplicaciones: API, descargas, versionado, identificadores, búsqueda y formatos de respuesta. Después se podrá diseñar el contrato de una futura skill ESCO que devuelva candidatos explicados, no códigos definitivos.

## Actualizacion - Fases, pruebas sinteticas y relacion con ESCO

El trabajo de cobertura profesional queda ordenado provisionalmente en tres fases de alcance creciente:

- **Fase 1:** primera version util del Perfil Profesional Accionable, sin ESCO como requisito. Debe recoger trayectoria, experiencias significativas, evidencias, competencias candidatas, herramientas y sistemas, uso de IA y preguntas pendientes.
- **Fase 2:** primera version util con correspondencias ESCO candidatas, explicadas, trazables, versionadas y revisables.
- **Fase 3:** perfil completo por ciclos, con narrativas, preferencias, opciones, brechas y ESCO como capa revisable.

La decision vigente es no redactar todavia la SPEC operativa final del playbook. Antes debe sintetizarse el nucleo metodologico en decisiones de diseno sobre informacion a capturar, tecnica, evidencia, incertidumbre y criterio de inmersion de profundidad. La Fase 1 es el alcance recomendado para el primer playbook operativo.

La SPEC futura debera declarar las capacidades de la fase y las familias de pruebas sinteticas obligatorias, pero el detalle de casos y resultados vivira en documentos separados. Las pruebas sinteticas no validan el metodo con personas: prueban reglas y guardarrailes; los pilotos reales o semi-reales mantienen su funcion de evidencia limitada de utilidad.

Podra explorarse una automejora acotada mediante agentes por caso sintetico, con intentos maximos, limites de cambio y revision transversal final. La investigacion ESCO continua por separado en la sesion hija vigente y alimentara la Fase 2, sin bloquear la definicion de la Fase 1.
