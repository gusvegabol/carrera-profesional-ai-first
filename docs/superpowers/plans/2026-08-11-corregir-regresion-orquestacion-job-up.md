# Corregir regresión de orquestación Job-up — Plan de implementación

> **Para agentes:** ejecutar este plan tarea a tarea con puntos de verificación. No hacer commit, merge ni PR en esta tarea.

**Objetivo:** hacer verificable y determinista la continuidad desde `GATE-CARTA-REVISION-HUMANA = aprobado` hasta `PLAYBOOK_VEREDICTO_FINAL_CARTA`, sin pausa humana intermedia.

**Arquitectura:** la skill y el playbook conservarán la regla normativa, pero la decisión de transición se expresará también en un helper pequeño y puro que recibe el estado de una candidatura y devuelve la siguiente acción o la parada humana real. La prueba E2E llamará a ese helper con el estado posterior a la revisión humana y fallará si devuelve una pausa redundante. No se modifica ningún documento semántico de CAND-2026-023.

**Tech Stack:** Markdown, Python 3, `unittest`, `compileall`.

## Restricciones globales

- No iniciar una nueva candidatura ni regenerar CAND-2026-023.
- No modificar contenido semántico, CV, carta ni veredictos aprobados de CAND-2026-023.
- No hacer commit, merge ni PR.
- La presentación externa, formularios y credenciales permanecen fuera de alcance.
- `documentalmente_completa` mantiene `presentada: false`.
- Un gate aprobado solo se pausa si falta dato, decisión, revisión humana, autorización o existe acción irreversible/bloqueo técnico.

---

### Tarea 1: Crear la prueba de regresión efectiva

**Archivos:**
- Modificar: `tests/test_hallazgos_e2e_job_up.py`
- Crear: `scripts/job-up/orquestar_transiciones.py` (solo se importará después de comprobar el fallo)

**Interfaces:**
- La prueba usará `siguiente_accion_carta(estado: dict[str, object]) -> str`.
- Para `GATE-CARTA-REVISION-HUMANA = aprobado`, carta compuesta aprobada y ausencia de datos pendientes, la acción esperada será `PLAYBOOK_VEREDICTO_FINAL_CARTA`.

- [x] Añadir un test que modele el estado real posterior a la revisión y exija la acción del playbook, no una frase declarativa.
- [x] Ejecutar solo ese test y comprobar que falla porque el helper todavía no existe.

### Tarea 2: Implementar la decisión mínima de transición

**Archivos:**
- Crear: `scripts/job-up/orquestar_transiciones.py`
- Modificar: `.codex/skills/job-up-candidatura-oferta/SKILL.md`
- Modificar: `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md`
- Modificar: `docs/metodologia/playbooks/PLAYBOOK_COMPONER_CARTA_PRESENTACION.md`
- Modificar: `docs/metodologia/playbooks/PLAYBOOK_VEREDICTO_FINAL_CARTA.md`

**Interfaces:**
- `siguiente_accion_carta(estado: dict[str, object]) -> str` devuelve una de estas constantes: `PLAYBOOK_COMPONER_CARTA_PRESENTACION`, `PLAYBOOK_VEREDICTO_FINAL_CARTA`, `ESPERAR_DECISION_HUMANA`, `CIERRE_DOCUMENTAL` o `BLOQUEO_TECNICO`.
- No ejecuta playbooks ni modifica expedientes; representa la selección determinista que la orquestación debe realizar.

- [x] Implementar primero las precondiciones de composición y veredicto; devolver `ESPERAR_DECISION_HUMANA` solo para gates humanos pendientes o entradas incompletas.
- [x] Priorizar el veredicto cuando `GATE-CARTA-REVISION-HUMANA` está aprobado y el contenido/composición son válidos.
- [x] Devolver `CIERRE_DOCUMENTAL` solo con veredicto de carta y CV aprobados, `presentada: false` y sin módulo de presentación activo.
- [x] Añadir a la skill y a los playbooks una tabla de transición que remita a la decisión efectiva y prohíba anunciar el veredicto como “siguiente paso” mientras se espera innecesariamente.

### Tarea 3: Auditar transiciones vecinas y proteger el falso positivo

**Archivos:**
- Modificar: `tests/test_hallazgos_e2e_job_up.py`
- Modificar: `tests/test_job_up_candidatura_oferta_skill.py`

- [x] Añadir el caso `GATE-CONTENIDO-CARTA-COMPOSICION = aprobado` → `PLAYBOOK_COMPONER_CARTA_PRESENTACION`.
- [x] Añadir el caso de gate de revisión pendiente → `ESPERAR_DECISION_HUMANA`.
- [x] Añadir el caso de veredicto de carta aprobado y CV aprobado → `CIERRE_DOCUMENTAL`, manteniendo `presentada: false`.
- [x] Sustituir la aserción normativa aislada por una aserción sobre el helper y conservar una comprobación documental de la regla.

### Tarea 4: Registrar E2E-REGRESSION-01 y verificar

**Archivos:**
- Modificar: `.pcs/estado/estado-actual.md`
- Modificar: `.pcs/sesiones/sesion-20260805-1757-job-up.md`

- [x] Registrar causa raíz, falso positivo, corrección y nombre exacto de la prueba.
- [x] Confirmar CAND-2026-023 intacta, `documentalmente_completa`, con ambos gates aprobados y `presentada: false`.
- [x] Ejecutar pruebas específicas de transición y E2E Job-up.
- [x] Ejecutar `python -m unittest discover -s tests`.
- [x] Ejecutar `python -m compileall scripts tests`.
- [x] Ejecutar `git diff --check` y buscar referencias activas reintroducidas a presentación.

---
