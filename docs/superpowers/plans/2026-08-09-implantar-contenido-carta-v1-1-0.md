# Implantar contenido de carta v1.1.0 — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implantar el contrato v1.1.0 de generación del contenido de la carta de presentación, incorporar los tres roles obligatorios y sus guardarraíles, regenerar desde cero el contenido de `CAND-2026-020` y dejar la prueba técnica preparada sin aprobar humanamente el gate.

**Architecture:** `guion-carta-presentacion.md` aprobado alimenta un artefacto exclusivo de contenido de carta. El playbook y su template definen roles, secuencia, restricciones y trazabilidad. Un verificador determinista audita el texto visible sin decidir estrategia ni consultar fuentes fuera del artefacto de contenido. La composición y la presentación quedan fuera de esta iteración.

**Tech Stack:** Markdown contractual, Python 3 y `unittest`, artefactos de candidatura bajo `outputs/candidaturas/`.

## Global Constraints

- Mantener `version: "1.1.0"` y `estado: en_prueba` en el playbook y el template.
- Regenerar `CAND-2026-020` desde las fuentes canónicas actuales; no parchear ni copiar la carta anterior.
- Mantener motivación personal como `ninguna`, cultura como contexto y la trazabilidad factual existente.
- La prioridad contractual es factualidad, utilidad para recruiter, argumentación, naturalidad y, por último, ATS/IA.
- La restricción interna no puede aparecer como texto visible de la carta.
- La segunda lectura del recruiter es obligatoria después de toda corrección factual.
- Mantener `decision_humana: pendiente` y `estado_gate: pendiente`; no aprobar, componer ni presentar.
- No generar ni modificar DOCX, PDF, LaTeX ni formularios de presentación.
- Preservar cambios previos del usuario en el checkout sucio; no hacer reset, checkout destructivo ni limpiar archivos ajenos. Se trabaja en el checkout existente porque contiene los artefactos contractuales y de candidatura no comprometidos que forman parte de esta tarea.
- Tras cada tarea se ejecutarán comprobaciones proporcionales; al final se ejecutarán los tests específicos, la suite completa y `git diff --check`.

---

## Task 1 — Fijar la línea base y mapear el contrato

- [ ] Leer completamente el prompt recibido, el playbook, el template, `guion-carta-presentacion.md`, `candidatura.md`, `analisis-oferta.md`, `datos-core-busqueda.md`, el expediente de `CAND-2026-020` y los tests existentes.
- [ ] Confirmar las versiones/estados actuales, el gate de entrada aprobado y el gate de composición aún pendiente.
- [ ] Ejecutar la prueba específica existente para registrar la línea base antes de cambios.
- [ ] Documentar cualquier discrepancia que exija una corrección posterior, sin modificar todavía otros módulos.

## Task 2 — Consolidar el playbook v1.1.0

- [ ] Verificar o completar el frontmatter `version: "1.1.0"`, `estado: en_prueba`, alcance exclusivo de carta y gates correctos.
- [ ] Verificar los tres roles obligatorios, sus límites de autoridad y la secuencia redactor → recruiter → auditor → corrección → segunda lectura recruiter.
- [ ] Verificar los guardarraíles de restricción interna, voz del candidato, lenguaje meta-analítico, utilidad de cada frase, anti-segundo-CV, anti-genericidad y anti-señales de IA.
- [ ] Verificar T13–T18 y la regla de convertir cada defecto generalizable en cambio de playbook, template y test.
- [ ] Revisar ortografía española y conservar el documento en `en_prueba`.

## Task 3 — Consolidar el template v1.1.0

- [ ] Verificar o completar el frontmatter `version: "1.1.0"`, `estado: en_prueba`, artefacto, gates y fuentes.
- [ ] Verificar campos de ejecución de los tres roles, primera y segunda lectura recruiter, auditoría factual, restricciones internas y formulaciones positivas.
- [ ] Verificar controles explícitos de voz, meta-lenguaje, utilidad por frase, primer escaneo, segundo CV, genericidad, anti-IA, factualidad, no expansión y regresión tras auditoría.
- [ ] Revisar ortografía española y conservar el documento en `en_prueba`.

## Task 4 — Implantar verificación ejecutable y tests T13–T18

- [ ] Añadir o adaptar un verificador determinista para el texto visible de la carta: lenguaje defensivo, voz de sistema/auditor, meta-análisis, señales de IA, utilidad mínima y estado resultante.
- [ ] Ampliar `tests/test_playbook_generar_contenido_carta_presentacion.py` con comprobaciones de comportamiento, no solo de encabezados, para T13, T14, T15, T16, T17 y T18.
- [ ] Mantener las regresiones de factualidad, privacidad, no expansión, anti-segundo-CV, anonimato de la empresa y ausencia de DOCX/PDF.

## Task 5 — Regenerar `CAND-2026-020` desde cero

- [ ] Redactar un nuevo `contenido-carta-presentacion.md` a partir del guion aprobado y de las fuentes canónicas, usando la estructura v1.1 del template.
- [ ] Registrar las ejecuciones del redactor, primera lectura recruiter, auditoría factual, correcciones contractuales y segunda lectura recruiter.
- [ ] Incluir una única carta consolidada visible, en voz del candidato, natural, factual y sin restricciones internas ni lenguaje meta.
- [ ] Actualizar la evaluación del gate con versión de contenido v1.1.0, resultado técnico apto/recomendación aprobar y decisión humana pendiente, conservando el antecedente histórico de no aprobado.

## Task 6 — Sincronizar trazabilidad PCS y candidatura

- [ ] Actualizar únicamente las filas/estados necesarios de `candidatura.md`, la sesión PCS abierta y `.pcs/estado/estado-actual.md` para reflejar la regeneración v1.1 y el gate de composición pendiente.
- [ ] No alterar la estrategia de candidatura, el guion aprobado, la composición ni la presentación.

## Task 7 — Verificación final y auto-revisión

- [ ] Ejecutar tests específicos y `python -m unittest discover -s tests -v`.
- [ ] Ejecutar el verificador sobre `CAND-2026-020`, comprobar conteo de palabras y ausencia de DOCX/PDF/LaTeX nuevos.
- [ ] Ejecutar `git diff --check` y revisar manualmente el diff de todos los archivos de esta tarea.
- [ ] Contrastar el resultado contra cada requisito del prompt y declarar incidencias abiertas, sin promover automáticamente los documentos fuera de `en_prueba`.
