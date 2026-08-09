# Plan de implementación: validación formal de contenido del CV

> **Para ejecutar:** usar `superpowers:executing-plans` o `superpowers:subagent-driven-development` en una rama aislada.

**Objetivo:** validar formalmente el contrato `PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA` con los casos CAND-2026-020 (Lidl) y CAND-2026-019 (ASIC), sin generar CV, carta ni otros documentos productivos.

**Alcance:** exclusivamente el paso «guion de CV aprobado → `datos-generacion.json` auditable» y su validación estructural, semántica y de frontera. No incluye composición, maquetación, generación DOCX/PDF/TeX, carta de presentación, envío ni modificación de candidaturas históricas.

**Estado previo conocido:** los dos guiones existentes declaran versiones anteriores (`PLAYBOOK_GUION_ADAPTACION_CV` 1.0.0 y plantilla 2) mientras el contrato vigente exige 1.0.1 y plantilla 2.1. Sus aprobaciones actuales de `GATE-GUION-CV-CONTENIDO` no podrán reutilizarse después de regenerarlos. La plantilla canónica para esta prueba es `TEMPLATE_DATOS_GENERACION_CV_v1_FINAL.json` (schema/template 1.2); el playbook aún referencia erróneamente la plantilla 1.1.

## Restricciones globales

- Mantener el alcance exclusivo sobre el CV y la frontera: `datos-generacion.json` no contiene carta ni decisiones de composición.
- No alterar hechos, candidatura, análisis, oferta, estado de presentación ni datos-core salvo que una prueba detecte una contradicción factual real; esa situación se detendrá y se elevará al usuario.
- No reutilizar una decisión humana de gate de una versión anterior del guion: la re-evaluación técnica deja la decisión humana pendiente.
- Regenerar los guiones completos, nunca parchear el resultado previo.
- Los JSON generados serán fixtures de validación aislados; no serán `datos-generacion.json` productivos dentro de una candidatura.
- Reutilizar las referencias factuales existentes y conservar la trazabilidad de cada unidad de contenido.
- No modificar documentación histórica ni los CV/carta heredados.

## Tarea 1: reconciliar el contrato documental de la fase

**Archivos:**
- Modificar: `docs/ideas-y-debates/mejoras-job-up/PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA.md`
- Opcionalmente modificar: `docs/ideas-y-debates/mejoras-job-up/TEMPLATE_DATOS_GENERACION_CV_v1_FINAL.json` solo si una comprobación objetiva descubre una incoherencia interna.
- Añadir o modificar: `tests/test_playbook_generar_contenido_cv.py`

**Pasos:**
1. Cambiar la referencia del playbook a `TEMPLATE_DATOS_GENERACION_CV_v1_FINAL.json` y fijar schema/template esperados en 1.2.
2. Revisar el template 1.2 frente al playbook: metadatos, alcance CV, trazabilidad, cobertura, restricciones, léxico, primer escaneo y prohibición de decisiones de composición.
3. Añadir comprobaciones automatizadas de coherencia entre ambos documentos y de ausencia de rutas/estructuras de carta.

**Verificación:** `python -m unittest tests.test_playbook_generar_contenido_cv`.

## Tarea 1b: sincronizar la plantilla física del guion con el contrato 2.1

**Archivos:**
- Modificar: `docs/ideas-y-debates/mejoras-job-up/TEMPLATE_GUION_ADAPTACION_CV_v2.md`
- Ampliar: `tests/test_playbook_guion_adaptacion_cv.py`

**Pasos:**
1. Sustituir la plantilla física obsoleta (versión 2) por el contrato 2.1 ya incorporado en `PLAYBOOK_GUION_ADAPTACION_CV`.
2. Incluir `idioma_cv` y su autoridad explícita, y asegurar que la plantilla, el playbook y las futuras instancias declaran las mismas versiones.
3. Añadir una comprobación automatizada que impida una nueva divergencia entre el playbook y la plantilla física.

**Verificación:** `python -m unittest tests.test_playbook_guion_adaptacion_cv`.

## Tarea 2: regenerar los guiones de los dos casos de control

**Archivos:**
- Modificar: `.../CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/guion-adaptacion-cv.md`
- Modificar: `.../CAND-2026-019-asic-consultores-responsable-automatizacion-ia/guion-adaptacion-cv.md`
- Modificar: sus dos `evaluacion-gate-guion-cv-contenido.md`
- Ampliar: `tests/test_playbook_guion_adaptacion_cv.py`

**Pasos:**
1. Regenerar ambos guiones desde las candidaturas aptas, con `version_playbook: 1.0.1`, `version_template: 2.1` e `idioma_cv` explícito.
2. Resolver la incoherencia ASIC: M-008/GSC-01 se asigna a `SEC-04`, que es donde reside la evidencia en la arquitectura narrativa.
3. Re-evaluar técnicamente el gate de salida de cada guion. Registrar recomendación, pero marcar `decision_humana: pendiente` y `estado_gate: pendiente` porque la versión del guion cambió.
4. Añadir pruebas de versión, idioma y ubicación de GSC-01.

**Verificación:** `python -m unittest tests.test_playbook_guion_adaptacion_cv`.

## Tarea 3: implantar el validador y los fixtures controlados del contenido CV

**Archivos:**
- Añadir: un módulo de validación acotado bajo `scripts/` o `tests/`.
- Añadir: fixtures aislados bajo `tests/fixtures/` o un directorio equivalente ignorado/documentado.
- Añadir: `tests/test_validacion_datos_generacion_cv.py`.

**Pasos:**
1. Crear una carga de guion y JSON que valide IDs C-NNN/B-NNN únicos, referencias M-NNN existentes, sección correcta, origen factual, exclusión de contenido `omitir`, continuidad sin mapas M, cobertura obligatoria, restricciones, léxico, idioma, placeholders y prohibición de carta/composición.
2. Crear fixtures positivos para Lidl y ASIC sin escribir en sus carpetas de candidatura.
3. Crear fixtures negativos: duplicados, M inexistente, M en sección errónea, contenido omitido, mapa omitido no materializado, continuidad con M, restricción incumplida, léxico prohibido, idioma ausente, placeholder y decisión de carta/composición.
4. Añadir una prueba de compositor pasivo: solo puede consumir orden, bloques y textos del JSON; no puede requerir ni reinterpretar candidatura ni guion.

**Verificación:** `python -m unittest tests.test_validacion_datos_generacion_cv`.

## Tarea 4: ejecutar la validación formal y documentar el dictamen técnico

**Archivos:**
- Añadir: informe de validación en `docs/ideas-y-debates/mejoras-job-up/` o en la carpeta de pruebas, sin tocar estados productivos.
- Modificar solo tras evidencia suficiente: `.pcs/estado/estado-actual.md` y la sesión PCS abierta.

**Pasos:**
1. Ejecutar la batería completa y revisar los resultados esperados de los dos casos positivos y todos los negativos.
2. Preparar el dictamen técnico de aptitud de la plantilla y el playbook, especificando que el paso productivo queda condicionado a las nuevas aprobaciones humanas de `GATE-GUION-CV-CONTENIDO`.
3. Actualizar PCS con evidencia, no con una aprobación inferida.

**Verificación:** `python -m unittest discover -s tests` y `git diff --check`.

## Punto de decisión humana obligatorio

Tras completar la Tarea 2, solicitar la decisión del usuario sobre los dos nuevos `GATE-GUION-CV-CONTENIDO`. Hasta esa aprobación no se ejecutará el playbook sobre candidaturas reales. Las pruebas con fixtures podrán verificar el contrato de forma aislada, pero no sustituyen el gate de una candidatura.

## Criterio de cierre

La validación queda técnicamente cerrada si el contrato 1.2 está reconciliado, los dos guiones están regenerados y técnicamente conformes, ambos fixtures positivos pasan, todos los negativos fallan por la causa esperada, el compositor pasivo puede operar sin reabrir decisiones y la batería completa no introduce regresiones. La habilitación productiva de cada candidatura requiere, además, su aprobación humana de gate.
