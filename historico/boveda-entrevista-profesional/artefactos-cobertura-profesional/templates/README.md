# README - templates

## Estado de este documento

Este README describe la funcion de la carpeta `templates/` y las reglas de uso de los templates de cobertura profesional.

No sustituye a los propios templates. Cada template sigue siendo la fuente real para crear artefactos nuevos.

## Funcion de esta carpeta

`templates/` contiene modelos para crear artefactos homogeneos de cobertura profesional.

Los templates ayudan a evitar que cada IA o persona invente desde cero:

- el frontmatter;
- la estructura minima;
- los nombres de campos;
- las relaciones entre documentos;
- las secciones obligatorias;
- los criterios de cierre.

## Templates disponibles

### TEMPLATE_MAPA.md

Template para crear mapas vivos de cobertura profesional.

El artefacto resultante debe guardarse en:

`../mapas/`

Debe usarse cuando se inicia o formaliza un proceso de cobertura profesional para un entrevistado o caso.

Relacion principal:

- referencia las zonas detectadas y apunta a checkpoints, inmersiones y competencias.

### TEMPLATE_SESION.md

Template para crear sesiones de cobertura profesional.

El artefacto resultante debe guardarse en:

`../sesiones/`

Debe usarse para registrar una sesion completa de cobertura: apertura, panoramica, prevalidacion, activacion de profundidad y cierre.

Relacion principal:

- se vincula al mapa asociado y puede dejar trazabilidad de reanudacion o cierre.

### TEMPLATE_INMERSION.md

Template para crear inmersiones de profundidad dentro de una cobertura.

El artefacto resultante debe guardarse en:

`../inmersiones/`

Debe usarse cuando una zona de cobertura activa una inmersion completa para validar o descartar una competencia.

Relacion principal:

- puede enlazarse con un checkpoint de origen y con la competencia derivada, si existe.

### TEMPLATE_CHECKPOINT.md

Template para crear checkpoints de una inmersion interrumpida.

El artefacto resultante debe guardarse en:

`../checkpoints/`

Debe usarse cuando una zona queda en estado parcial y hace falta poder reanudar sin perder contexto.

Relacion principal:

- apunta al mapa, a la zona afectada y a la instruccion de reanudacion.

### TEMPLATE_COMPETENCIA.md

Template para crear fichas breves de competencia ya extraida.

El artefacto resultante debe guardarse en:

`../competencias/`

Debe usarse cuando una inmersion cerrada produce una competencia con evidencia suficiente para resumirla.

Relacion principal:

- deriva de una inmersion cerrada y sirve como indice rapido de lectura.

## Convencion de nombres

Los templates vigentes no llevan sufijo `_COBERTURA`.

Convencion vigente:

- `TEMPLATE_MAPA.md`
- `TEMPLATE_SESION.md`
- `TEMPLATE_INMERSION.md`
- `TEMPLATE_CHECKPOINT.md`
- `TEMPLATE_COMPETENCIA.md`

## Frontmatter común

Todos los templates usan frontmatter YAML.

Campos comunes observados en la carpeta:

- `id_mapa`
- `id_entrevistado`
- `fecha_creacion`
- `fecha_cierre`

Campos que aparecen segun el tipo de artefacto:

- `fecha_actualizacion`
- `estado`
- `motivo_cierre`
- `id_zona`
- `id_competencia`
- `id_inmersion`
- `calidad_evidencia`
- `resultado`

Resumen por template:

| Template | Campos de frontmatter observados |
|---|---|
| `TEMPLATE_MAPA.md` | `tipo`, `id_mapa`, `id_entrevistado`, `fecha_creacion`, `fecha_actualizacion`, `estado`, `fecha_cierre` |
| `TEMPLATE_SESION.md` | `tipo`, `id_mapa`, `id_entrevistado`, `fecha_creacion`, `estado`, `fecha_cierre`, `motivo_cierre` |
| `TEMPLATE_INMERSION.md` | `tipo`, `id_mapa`, `id_entrevistado`, `id_zona`, `id_competencia`, `fecha_creacion`, `resultado` |
| `TEMPLATE_CHECKPOINT.md` | `tipo`, `id_mapa`, `id_entrevistado`, `id_zona`, `fecha_creacion`, `estado`, `fecha_cierre` |
| `TEMPLATE_COMPETENCIA.md` | `tipo`, `id_competencia`, `id_mapa`, `id_entrevistado`, `id_zona`, `id_inmersion`, `fecha_creacion`, `calidad_evidencia` |

## Relacion entre template y artefacto real

Un template nunca es un artefacto real.

- `TEMPLATE_MAPA.md` crea documentos reales dentro de `../mapas/`.
- `TEMPLATE_SESION.md` crea documentos reales dentro de `../sesiones/`.
- `TEMPLATE_INMERSION.md` crea documentos reales dentro de `../inmersiones/`.
- `TEMPLATE_CHECKPOINT.md` crea documentos reales dentro de `../checkpoints/`.
- `TEMPLATE_COMPETENCIA.md` crea documentos reales dentro de `../competencias/`.

## Reglas de uso

- Copia el template correspondiente antes de crear un artefacto.
- Sustituye los campos vacios del frontmatter.
- No dejes IDs genericos.
- No dejes fechas placeholder.
- No modifiques el template para adaptar un caso concreto.
- Guarda el artefacto creado en la subcarpeta correspondiente.
- Nombra el archivo final segun la convencion definida en `../README.md`.

## Que no debe hacerse

- No usar templates como documentos reales.
- No guardar entrevistas, mapas o checkpoints dentro de `templates/`.
- No modificar templates para resolver necesidades puntuales de una persona.
- No duplicar templates con sufijo `_COBERTURA`.
- No cambiar campos de frontmatter sin revisar el impacto en todos los artefactos.
- No introducir decisiones metodologicas nuevas dentro de este README.

## Mantenimiento de templates

Los templates son documentos sensibles porque afectan a todos los artefactos futuros.

Si cambia un template, debe revisarse:

- la coherencia con `../README.md`;
- la coherencia con los README de subcarpetas, si existen;
- la coherencia del frontmatter;
- el impacto en artefactos ya creados;
- si hace falta registrar el cambio en el estado o en la sesion abierta.

## Historico

| Fecha | Cambio | Autor |
|---|---|---|
| 2026-07-07 | Creacion inicial del README de templates. | CODEX |
