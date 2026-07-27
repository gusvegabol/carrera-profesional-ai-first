---
id: sesion-20260724-2004-candidaturas-job-up
titulo: Candidaturas nuevas y antiguas — Job-up
inicio: 2026-07-24 20:04
cierre: 2026-07-27 12:45
estado: cerrada
tipo: sesion
host: carrera-ai
sesion_relacionada: sesion-20260722-1131-job-up
---

# Sesión PCS — Candidaturas nuevas y antiguas — Job-up

## Contexto inmediato

Job-up continúa como línea operativa de búsqueda de empleo dentro de Carrera AI. La sesión anterior de materialización de Job-up está cerrada y esta sesión abre un bloque de trabajo delimitado para revisar candidaturas existentes y preparar nuevas cuando corresponda.

## Objetivo

Revisar, mantener y mejorar candidaturas nuevas y antiguas con trazabilidad factual, control de arrastre entre ofertas y aprobación humana antes de cualquier envío.

## Alcance inicial

- Revisar el estado y los próximos pasos de las candidaturas existentes.
- Identificar candidaturas antiguas que requieran actualización, cierre o reaprovechamiento controlado.
- Valorar nuevas ofertas y preparar candidaturas solo con autorización expresa.
- Mantener separados los documentos, datos autorizados y condicionantes de cada candidatura.

## Capa episódica

La sesión comenzó con la revisión de candidaturas nuevas y antiguas de Job-up. Se consolidó la candidatura espontánea a Randstad (`CAND-2026-006`) y se revisaron los registros posteriores de AROGADI/AGD Center (`CAND-2026-007`), Baleària (`CAND-2026-008`), LIVVO Hotel Group (`CAND-2026-009`) y ACCIONA (`CAND-2026-010`). Se generaron y asociaron sus documentos de candidatura cuando correspondía, se registraron los envíos comunicados por la persona candidata y se mantuvieron separados los estados y condicionantes de cada oferta.

En el tramo final se completó la candidatura de ACCIONA en Workday y la persona candidata confirmó que había sido presentada. Se registró como enviada el 2026-07-27. También se convirtió su CV a `cv.tex` y, a partir de esa necesidad, se incorporó al flujo futuro la generación de un CV en LaTeX para tratamiento por IA.

## Capa semántica

La sesión debe preservar la separación entre la línea operativa Job-up y la investigación metodológica de entrevista. El estado vivo de candidaturas debe mantenerse en sus documentos operativos y en `estado-actual.md`, no únicamente en esta sesión.

La línea Job-up continúa abierta como actividad de largo plazo, pero esta sesión queda limitada al bloque histórico de revisión, preparación y presentación documentado aquí. La carpeta de cada candidatura es la fuente operativa de su estado y de sus documentos.

## Ideas y líneas cognitivas abiertas

- Abrir un nuevo bloque PCS cuando haya que valorar o preparar nuevas ofertas.
- Mantener la consistencia entre análisis de oferta, guion, veredicto, CV, `cv.tex`, carta y ficha de candidatura.

## Resultado de la sesión

- `CAND-2026-006`: presentación espontánea a Randstad preparada, pendiente de aprobación y no compartida.
- `CAND-2026-007`: candidatura presentada a AGD Center el 2026-07-26.
- `CAND-2026-008`: candidatura presentada a Baleària mediante Indeed el 2026-07-27.
- `CAND-2026-009`: candidatura presentada a LIVVO mediante Indeed el 2026-07-27.
- `CAND-2026-010`: candidatura presentada a ACCIONA mediante Workday el 2026-07-27.
- CAND-2026-001 permanece rechazada; CAND-2026-002 a CAND-2026-005 permanecen enviadas y pendientes de respuesta.

## Acciones derivadas

- No se crea una nueva acción PCS. La continuidad de la búsqueda queda registrada en [[estado-actual]] y se retomará mediante nuevas sesiones PCS delimitadas cuando exista una oferta o bloque concreto autorizado.

## Decisiones derivadas

- [[DEC-20260724-1956-001-delimitar-sesiones-job-up]] permanece vigente: Job-up continúa a largo plazo, pero sus sesiones PCS se delimitan y se cierran por bloques.
- El flujo documental de candidaturas incorpora `cv.tex` como artefacto obligatorio futuro y no usa LibreOffice para abrir o inspeccionar DOCX; esta regla queda materializada en el playbook y las plantillas de búsqueda de empleo.

## Problemas o bloqueos

- Cada candidatura requiere comprobar sus datos privados autorizados y su estado antes de reutilizar materiales.
- Ningún documento autoriza por sí mismo el envío de una candidatura.
- La verificación visual de DOCX puede quedar limitada si el entorno no dispone de un renderizador operativo; se debe declarar la limitación y conservar la validación estructural.

## Documentos afectados

- `.pcs/estado/estado-actual.md`
- `.pcs/decisiones/DEC-20260724-1956-001-delimitar-sesiones-job-up.md`
- `boveda-entrevista-profesional/busqueda-empleo/seguimiento-candidaturas.md`
- `boveda-entrevista-profesional/busqueda-empleo/candidaturas/`
- `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md`
- `boveda-entrevista-profesional/busqueda-empleo/templates/TEMPLATE_CANDIDATURA.md`

## Rehidratación futura

- **Dónde quedó el trabajo:** esta sesión está consolidada y cerrada; la rama Job-up sigue viva en `estado-actual.md`, el seguimiento general y las carpetas de candidatura.
- **Leer primero:** `boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md`, `seguimiento-candidaturas.md`, `datos-core-busqueda.md`, `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md` y `estado-actual.md`.
- **Líneas abiertas a retomar:** valorar una oferta concreta o abrir un nuevo bloque para preparar una candidatura; mantener `cv.tex` junto al DOCX y PDF.
- **Riesgos de malinterpretación:** no reutilizar documentos entre ofertas sin revisar el enfoque, los datos autorizados y los condicionantes específicos.
- **Siguiente gesto recomendado:** abrir una nueva sesión PCS delimitada cuando se autorice la siguiente oferta o bloque de candidaturas.

## Actualización — CAND-2026-006 Randstad

Se creó la candidatura espontánea `CAND-2026-006` para presentar a Gustavo a Randstad en procesos de intermediación. El eje es Dirección/Management y los perfiles secundarios son Operaciones, Administración, mejora de procesos e Informática aplicada y automatización. Se prepararon análisis, guion, CV de dos páginas con Calibri 11 pt y encabezados 14/12 pt, carta de presentación de una página y veredicto final.

La candidatura tiene integridad `apta`, media orientativa 4,2/5 y decisión `revisar_antes_de_aprobar`. Está pendiente de revisión humana y no se ha compartido con Randstad.

### Ajuste de redacción del hito HER-05

Se sustituyó en la selección factual y en el CV la formulación ambigua sobre la expansión. La nueva redacción separa explícitamente el análisis realizado, el dato del 42 % y la decisión posterior del Consejo de Dirección. Se regeneraron el CV y su PDF; la carta se regeneró también para mantener el conjunto actualizado. La revisión visual confirmó que el CV tiene dos páginas y la carta una, sin problemas de composición.

### Ajuste tipográfico y de estilos

A petición del usuario, el CV utiliza Calibri, el estilo de párrafo `Body Text`/«Cuerpo de texto» a 11 pt, `Heading 1` a 14 pt y `Heading 2` a 12 pt. Se retiró el uso predominante del estilo de párrafo predeterminado y se mantuvieron los bloques de experiencia unidos cuando el salto de página lo permite.

### Ajuste de redacción del hito HER-09

Se reemplazó el énfasis aislado en el ahorro de papel por el valor principal del sistema: identificación de Workplace from Facebook/Meta, diseño de publicaciones semiautomáticas, centralización de comunicaciones de la central, acceso segmentado para Dirección, Administración y responsables operativos, sustitución de la distribución física recurrente y consulta inmediata de la información.

## Trazabilidad de CAND-2026-006

- Candidatura: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-006-randstad-presentacion-espontanea/`.
- SPEC: `docs/superpowers/specs/2026-07-24-candidatura-espontanea-randstad-design.md`.
- Plan: `docs/superpowers/plans/2026-07-24-candidatura-espontanea-randstad.md`.

## Trazabilidad

- Origen: apertura explícita de una sesión PCS para trabajar en candidaturas nuevas y antiguas.
- Sesiones relacionadas: `sesion-20260722-1131-job-up`.
- Acciones relacionadas: `ACC-20260721-1651-001-activar-rama-operativa-busqueda-empleo-fase-1`.
- Decisiones relacionadas: `DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo`, `DEC-20260724-1956-001-delimitar-sesiones-job-up`.
- Estado de proyecto relacionado: `estado-actual`.
- Cierre: 2026-07-27. La sesión queda cerrada como registro histórico del bloque de revisión, preparación y presentación de candidaturas; la continuidad de Job-up permanece fuera de esta sesión.
