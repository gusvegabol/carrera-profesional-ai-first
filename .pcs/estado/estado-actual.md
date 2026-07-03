---
id: estado-actual
titulo: carrera-profesional-ai-first
estado: pendiente_de_actualizacion
fecha_actualizacion: 2026-07-03 00:00
ultima_sesion_relacionada: sesion-20260630-fase-1-objetivo-real-mvp-carrera-ai
host: carrera-ai
---

# estado-actual

## Situación actual

La capa PCS del host ya no está solo en arranque mínimo: existe una sesión marco de alcance MVP y una sesión específica de Fase 1 para consolidar el objetivo real del MVP de `Carrera Profesional AI-First` como sistema AI-First apoyado en ChatGPT, CODEX, Notion, Drive y PCS.

La Fase 1 ya quedó materializada como paquete documental revisable y ahora se está evaluando el contenido de `docs/alcance-mvp.md` por parte del usuario y de ChatGPT.

La capa operativa ha detectado una desviación respecto a la idea original: el proyecto no debe quedarse en documentos mínimos ni en preguntas genéricas. El foco se ha corregido hacia la entrevista conversacional profunda como capacidad nuclear del sistema, y la bóveda `boveda-entrevista-profesional/` ya quedó consolidada como paso previo al playbook.

La bóveda ya quedó creada y validada, y la trazabilidad del reenfoque también quedó validada por ChatGPT. El siguiente trabajo recomendado empieza por `01_conceptos/` y `04_patrones_de_preguntas/`, mientras `docs/alcance-mvp.md` sigue pendiente de reinterpretación desde la entrevista como núcleo.

PCS canónico no se modifica en este reajuste. La memoria operativa del host sigue viviendo en `.pcs/`.

La fase de trabajo reciente consolidó además que el MVP debe concretarse como un primer piloto de entrevista profesional profunda ejecutado por ChatGPT, con salida mínima de competencia profesional con evidencia verificable y reglas explícitas de gobierno para la conversación. La bóveda de entrevista ya quedó normalizada en sus `README.md` con la convención de nombres semánticos por carpeta.

La sesión marco de alcance MVP y la sesión de Fase 1 siguen abiertas y continúan siendo la referencia viva para el cierre del objetivo real del MVP.

## Foco operativo

Investigar y desarrollar la bóveda de entrevista profesional hasta convertirla en base del futuro playbook, usando la entrevista conversacional profunda como la capacidad nuclear a validar en el MVP.

## Próximos pasos

- Desarrollar los conceptos y patrones nucleares de `boveda-entrevista-profesional/`.
- Evaluar si la entrevista conversacional profunda realmente funciona como núcleo del sistema.
- Replantear el MVP a partir de la entrevista antes de ampliar el alcance a nuevas fases.

## Acciones abiertas relevantes

- No hay acciones formales registradas todavía.
- Queda como acción candidata investigar y desarrollar `boveda-entrevista-profesional/` hasta producir un primer playbook.

## Decisiones vigentes relevantes

- `hosts/hosts.yaml` registra `carrera-ai` como host PCS.
- La carpeta `.pcs/` es la memoria operativa del host.
- Se mantiene la separación de capas entre PCS canónico, proyecto anfitrión, `.pcs/`, Notion, Drive y CODEX.
- No hay todavía una decisión formal nueva; queda como decisión candidata validar primero la entrevista conversacional profunda como núcleo del sistema.

## Bloqueos o riesgos

- El propósito funcional local del host sigue pendiente de consolidación en artefactos base del repositorio.
- Existe riesgo de volver a derivar hacia desarrollar una aplicación propia antes de validar el sistema AI-First.
- Existe riesgo de ampliar el proyecto hasta convertirlo en un segundo cerebro generalista en lugar de mantener el foco en carrera profesional.
- Si la entrevista no funciona, el enfoque AI-First conversacional no justifica continuar.
- Notion no debe confundirse con estado vivo ni sustituir sin criterio a la capa `.pcs/`.
- `.tmp/` queda excluida por defecto del uso operativo y de lectura salvo autorización explícita.

## Nota de vigencia

Estado actualizado a partir de la materialización de la Fase 1. Refleja líneas vigentes y candidatas, no decisiones ni acciones ya formalizadas.

## Trazabilidad

- Última sesión: sesion-20260630-fase-1-objetivo-real-mvp-carrera-ai
- Origen del cambio: materialización de la Fase 1 del alcance MVP en sesión específica y documento base
- Documentos creados o modificados:
  - .pcs/estado/estado-actual.md
  - .pcs/sesiones/sesion-20260630-fase-1-objetivo-real-mvp-carrera-ai.md
  - .pcs/sesiones/sesion-20260630-alcance-mvp-carrera-ai.md
  - docs/alcance-mvp.md
  - README.md
  - boveda-entrevista-profesional/README.md y README de sus carpetas

## Actualización — Entrevista piloto Herfrailes RRHH

Ya existe una primera entrevista piloto real/simulada-operativa registrada en la bóveda de entrevista profesional.

El caso de `Herfrailes SL` produjo una competencia profesional profunda con evidencia fuerte:

- `Diseño de sistemas internos socio-técnicos`
- creación desde cero de un sistema interno de RRHH con automatización, normativa y experiencia del personal integradas

El playbook `PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA` queda validado parcialmente para seguir probando, no aprobado definitivamente.

El foco inmediato pasa a revisar el documento creado y decidir si conviene una segunda entrevista con otra tensión o un ajuste mínimo del método.

PCS canónico no se modifica en este reajuste.
La memoria operativa del host sigue viviendo en `.pcs/`.
