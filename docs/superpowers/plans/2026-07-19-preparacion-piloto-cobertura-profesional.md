# Preparación del piloto real de cobertura profesional — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans or superpowers:subagent-driven-development to implement this plan task-by-task.

**Goal:** Dejar preparado el paquete documental y operativo mínimo para ejecutar un piloto real de la doble pasada de cobertura profesional.

**Architecture:** Mantener el playbook de cobertura profesional como orquestador y reutilizar el playbook de entrevista profesional v1.3.2 para una única inmersión profunda por sesión. Separar el protocolo experimental de las decisiones metodológicas formales y de la memoria PCS.

**Tech Stack:** Markdown, plantillas YAML existentes y documentación local del repositorio.

## Global Constraints

- No modificar `.pcs/` ni crear una sesión PCS por preparar el piloto.
- No presentar la doble pasada como método adoptado o validado.
- No modificar el SPEC funcional por inferencia.
- Mantener la ortografía española en toda documentación nueva o modificada.
- Preservar el cambio local preexistente en `docs/metodologia/playbooks/PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_0.md`.
- No crear artefactos de una persona real hasta recibir autorización, participante y alcance de datos.

---

### Task 1: Revisar la coherencia del kit de plantillas

**Files:**
- Review: `docs/templates/artefactos-cobertura-profesional/TEMPLATE_ENTREVISTADO.md`
- Review: `docs/templates/artefactos-cobertura-profesional/TEMPLATE_MAPA.md`
- Review: `docs/templates/artefactos-cobertura-profesional/TEMPLATE_SESION.md`
- Review: `docs/templates/artefactos-cobertura-profesional/TEMPLATE_CHECKPOINT.md`
- Review: `docs/templates/artefactos-cobertura-profesional/TEMPLATE_INMERSION.md`
- Review: `docs/templates/artefactos-cobertura-profesional/TEMPLATE_COMPETENCIA.md`

- [ ] Confirmar que los seis tipos de artefacto cubren el flujo del piloto.
- [ ] Registrar las inconsistencias de nomenclatura sin imponer una convención global.
- [ ] Determinar si alguna inconsistencia impide usar el kit en un piloto manual.

### Task 2: Fijar la lista de decisiones humanas de entrada

**Files:**
- Modify: `docs/superpowers/specs/2026-07-19-preparacion-piloto-cobertura-profesional-design.md`

- [ ] Mantener separadas las decisiones de autorización, participante, alcance de datos, identificadores y revisión de salida.
- [ ] No rellenar esos valores por inferencia.
- [ ] Mantener el documento como contrato provisional hasta que exista un piloto autorizado.

### Task 3: Preparar el checklist prepiloto

**Files:**
- Create: `docs/trabajo-en-curso/diseno/CHECKLIST_PREPILOTO_COBERTURA_PROFESIONAL.md`

- [ ] Incluir preparación de consentimiento, alcance, registro inicial y copia de trabajo de plantillas.
- [ ] Incluir controles durante la sesión: tiempo declarado, selección de zona, máximo de prevalidaciones e inmersiones.
- [ ] Incluir controles de cierre: límites, correcciones, incidencias y siguiente exploración.
- [ ] Separar tareas que puede realizar el agente de decisiones que requieren al responsable.

### Task 4: Preparar la matriz de evaluación

**Files:**
- Create: `docs/trabajo-en-curso/diseno/MATRIZ_EVALUACION_PILOTO_COBERTURA_PROFESIONAL.md`

- [ ] Convertir los criterios del contrato en preguntas observables.
- [ ] Definir evidencias mínimas para cobertura, prudencia, control, continuidad y utilidad.
- [ ] Evitar métricas que confundan aceptación textual con validez metodológica.
- [ ] Incluir una conclusión posible de continuar, modificar o descartar.

### Task 5: Verificar el paquete y comunicar el bloqueo de ejecución

**Files:**
- Review: all files created or modified by Tasks 1–4.

- [ ] Verificar enlaces, ortografía y ausencia de placeholders operativos.
- [ ] Comprobar que no se han modificado `.pcs/` ni el playbook con cambios preexistentes.
- [ ] Confirmar que el paquete queda listo para preparar el primer caso.
- [ ] Solicitar al responsable únicamente las decisiones necesarias para crear el primer artefacto real y abrir la primera sesión.
