---
titulo: Dictamen técnico — validación formal de contenido de CV
fecha: 2026-08-06
estado: evidencia_tecnica_verificada
alcance: validación formal no productiva
---

# Dictamen técnico — validación formal de contenido de CV

## Dictamen

La validación formal es conforme para el contrato de datos de generación de CV 1.2 y para los guiones regenerados 1.0.1 basados en la plantilla 2.1. La evidencia acredita el comportamiento del validador aislado y de su compositor pasivo; no acredita una aprobación humana ni habilita la generación productiva de documentos.

Los `GATE-GUION-CV-CONTENIDO` de `CAND-2026-020` (Lidl) y `CAND-2026-019` (ASIC) permanecen `pendiente` tras la regeneración. Cada evaluación individual declara `decision_humana: pendiente` y `estado_gate: pendiente`. Los fixtures no sustituyen esas dos decisiones.

## Evidencia auditable

- El contrato físico identifica `schema_id: datos-generacion-cv`, `schema_version: 1.2`, `template_id: TEMPLATE_DATOS_GENERACION_CV_v1.json` y `template_version: 1.2` en `TEMPLATE_DATOS_GENERACION_CV_v1_FINAL.json`.
- Los guiones de Lidl y ASIC se validan contra el contrato de guion 1.0.1 y plantilla 2.1, incluido el idioma explícito y su autoridad.
- Los fixtures positivos de Lidl y ASIC cumplen el contrato. Lidl cubre operación de tienda, pedidos y previsión, stock y rotación, resultados, equipo y límites de caja; ASIC cubre automatización documental, VB.NET, API de Trello, `GSC-01` en `SEC-04`, formación en IA en curso y restricciones tecnológicas.
- Los 23 casos negativos comprueban identificadores duplicados, referencias inválidas, destino de sección incorrecto, contenido omitido, continuidad indebida, restricciones, léxico prohibido, idioma, placeholders, carta o composición, cobertura obligatoria, trazabilidad factual y tecnologías no acreditadas.
- El compositor pasivo solo consume `contenido_cv` y devuelve secciones, bloques y textos ordenados. Ignora los campos de candidatura y control; no abre ni interpreta el guion ni toma decisiones editoriales, de composición o de maquetación.

## Pruebas verificadas

El 2026-08-06 se ejecutó `python -m unittest discover -s tests -v`: 47 pruebas superadas, sin fallos. Incluye los contratos existentes de generación de candidatura, los del playbook y plantilla de guion, el contrato 1.2 de contenido y el validador aislado.

También se ejecutó `git diff --check`: no informó errores de espacios. Solo emitió avisos de normalización LF a CRLF para archivos ya modificados en el árbol de trabajo.

## Límites y preocupaciones

- La validación trabaja con una representación JSON mínima del guion; una futura integración que extraiga datos desde Markdown deberá demostrar de nuevo las mismas garantías.
- La cobertura no autoriza crear `datos-generacion.json` productivo, CV, carta, PDF, DOCX, composición, maquetación ni envío.
- La sesión PCS sigue en pausa. Este dictamen no la cierra y no habilita una fase productiva.
- `DEF-ARQ-001` continúa abierto para novedades o contradicciones factuales.

## Revisión ortográfica

Se revisó la ortografía española del documento, incluidas tildes, mayúsculas y puntuación.
