# Frontera CV → candidatura completa → presentación Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Separar contractualmente la validación exclusiva del CV del gate de candidatura completa y evitar que un CV aprobado implique que la candidatura esté lista para enviarse.

**Architecture:** `GATE-VEREDICTO-CV` valida únicamente el CV y sus evidencias. Un nuevo `paquete-presentacion.md` declara el canal, los artefactos requeridos y su estado. `GATE-CANDIDATURA-PRESENTACION` valida ese paquete completo; solo una instrucción humana posterior puede ordenar el envío y convertir `presentada` en un hecho.

**Tech Stack:** Markdown, YAML frontmatter, plantillas de candidatura, pruebas `unittest` y memoria operativa PCS.

## Global Constraints

- La carta, el email y las respuestas de formulario permanecen fuera del flujo CV-only hasta que exista su módulo propio.
- `presentada: true` solo puede registrarse con evidencia de envío real; nunca por inferencia ni por aprobación de un gate.
- La IA no aprueba gates humanos, no ordena el envío y no completa formularios externos sin instrucción explícita.
- La SPEC conserva la estrategia común en `candidatura.md` y separa los adaptadores por artefacto.
- Toda documentación en español debe conservar ortografía española y enlaces internos válidos.

---

### Task 1: Fijar el contrato arquitectónico en la SPEC

**Files:**
- Modify: `docs/ideas-y-debates/mejoras-job-up/SPEC-Arquitectura-modular-generación-candidatura-v0-4-0.md`
- Test: `tests/test_playbook_guion_adaptacion_cv.py`

- [ ] **Step 1: Registrar el defecto arquitectónico**

Añadir un defecto abierto que explique que el gate del CV no puede autorizar una candidatura completa cuando carta/email/formulario, canal y paquete final no están definidos.

- [ ] **Step 2: Definir los dos gates**

Documentar:

```yaml
GATE-VEREDICTO-CV:
  alcance: cv_exclusivo
GATE-CANDIDATURA-PRESENTACION:
  alcance: paquete_completo_y_canal
```

Declarar `GATE-VEREDICTO-CV-PRESENTACION` como nombre histórico/deprecado, no como gate activo.

- [ ] **Step 3: Definir el paquete y la transición**

Especificar `paquete-presentacion.md`, sus estados (`pendiente_de_preparacion`, `incompleto`, `listo_para_gate`, `presentado`) y la regla `presentada: false → true` solo con evidencia de canal, fecha y confirmación humana.

- [ ] **Step 4: Documentar el impacto en los casos actuales**

Registrar que CAND-2026-020 tiene el CV validado y el gate CV aprobado, pero no tiene todavía paquete completo; CAND-2026-019 permanece detenida por su resultado no competitivo.

### Task 2: Actualizar playbooks y templates

**Files:**
- Modify: `docs/ideas-y-debates/mejoras-job-up/PLAYBOOK_VEREDICTO_FINAL_CV.md`
- Modify: `docs/ideas-y-debates/mejoras-job-up/TEMPLATE_VEREDICTO_FINAL_CV.md`
- Modify: `docs/ideas-y-debates/mejoras-job-up/PLAYBOOK_CANDIDATURA.md`
- Modify: `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md`
- Modify: `docs/ideas-y-debates/mejoras-job-up/TEMPLATE_CANDIDATURA_v2.md`
- Create: `docs/ideas-y-debates/mejoras-job-up/TEMPLATE_PAQUETE_PRESENTACION.md`

- [ ] **Step 1: Convertir el playbook de veredicto en CV-only**

Cambiar el gate activo a `GATE-VEREDICTO-CV`, prohibir que el resultado autorice carta, email, formulario o envío, y conservar la decisión humana solo como validación del CV.

- [ ] **Step 2: Añadir contrato del paquete**

Crear la plantilla con canal, URL/origen, artefactos requeridos, artefactos disponibles, revisiones, decisión del gate completo y evidencia de envío.

- [ ] **Step 3: Corregir las transiciones de candidatura**

Mantener `en_preparacion` mientras el paquete esté incompleto; permitir `pendiente_de_aprobacion` solo cuando `GATE-CANDIDATURA-PRESENTACION` pueda decidirse; usar `aprobada` sin cambiar `presentada`; usar `enviada` y `presentada: true` únicamente tras confirmación real.

### Task 3: Migrar los casos y artefactos activos

**Files:**
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/candidatura.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/veredicto-final-cv.md`
- Create: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/paquete-presentacion.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-019-asic-consultores-responsable-automatizacion-ia/candidatura.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-019-asic-consultores-responsable-automatizacion-ia/veredicto-final-cv.md`
- Modify: `boveda-entrevista-profesional/busqueda-empleo/seguimiento/seguimiento-candidaturas.md`

- [ ] **Step 1: Renombrar el gate activo en los veredictos**

Usar `GATE-VEREDICTO-CV` en los dos veredictos actuales; conservar la decisión de presentación completa como no emitida.

- [ ] **Step 2: Crear el paquete incompleto de Lidl**

Registrar Indeed como canal de origen, CV disponible, carta/email/formulario no resueltos y `GATE-CANDIDATURA-PRESENTACION: pendiente_de_preparacion`.

- [ ] **Step 3: Revertir la falsa apariencia de candidatura lista**

Dejar CAND-2026-020 en `en_preparacion` con CV validado y paquete pendiente. Mantener CAND-2026-019 `detenida` por gate CV bloqueado.

### Task 4: Añadir pruebas de frontera

**Files:**
- Modify: `tests/test_veredicto_final_cv.py`
- Modify: `tests/test_verificador_veredicto_final_cv.py`

- [ ] **Step 1: Probar nombres y alcances de gates**

Verificar que los artefactos activos usan `GATE-VEREDICTO-CV` y que el contrato distingue `GATE-CANDIDATURA-PRESENTACION`.

- [ ] **Step 2: Probar el bloqueo por paquete incompleto**

Verificar que la ausencia de carta/email/formulario requerido o canal resuelto impide marcar el paquete como listo y no cambia `presentada`.

- [ ] **Step 3: Ejecutar pruebas específicas y suite completa**

Ejecutar:

```text
python -m unittest tests.test_veredicto_final_cv tests.test_verificador_veredicto_final_cv -v
python -m unittest discover -s tests -v
git diff --check
```

### Task 5: Implementar el verificador del paquete

**Files:**
- Create: `scripts/job-up/verificar_paquete_presentacion.py`
- Create: `tests/test_verificador_paquete_presentacion.py`

- [ ] **Step 1: Escribir la prueba negativa de Lidl**

La instancia actual debe devolver bloqueos por canal no confirmado y artefactos de presentación no resueltos, manteniendo `presentada: false`.

- [ ] **Step 2: Implementar las funciones de validación**

Exponer `validar_paquete(paquete_path: Path, candidatura_dir: Path) -> list[str]` y `validar_transicion_presentada(paquete_path: Path, evidencia: dict[str, str]) -> None`. Rechazar estados `presentada: true` sin canal, fecha, ejecutor y confirmación.

- [ ] **Step 3: Ejecutar las pruebas del verificador**

Ejecutar `python -m unittest tests.test_verificador_paquete_presentacion -v` y comprobar que Lidl sigue bloqueado de forma determinista.

### Task 6: Sincronizar PCS y cerrar la implantación documental

**Files:**
- Modify: `.pcs/estado/estado-actual.md`
- Modify: `.pcs/sesiones/sesion-20260805-1757-job-up.md`

- [ ] **Step 1: Registrar la nueva frontera y el defecto resuelto**

Actualizar el estado y la sesión con el diseño aprobado, el paquete incompleto de Lidl y la detención de ASIC.

- [ ] **Step 2: Registrar el siguiente gesto**

Indicar que el siguiente paso es diseñar/preparar la carta, email o formulario que exija el canal, no enviar todavía.

- [ ] **Step 3: Revisar ortografía y enlaces**

Comprobar que la documentación española está corregida y que no se mantienen referencias activas al gate histórico.
