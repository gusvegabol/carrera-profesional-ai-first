# Validación de presentación de candidatura — Plan de implementación

> **Para agentes:** ejecutar este plan tarea a tarea con puntos de verificación. La presentación externa permanece fuera de alcance.

**Objetivo:** implantar el contrato documental de validación de presentación y probarlo con CAND-2026-020 sin enviar la candidatura.

**Arquitectura:** `paquete-presentacion.md` será la entrada. El nuevo playbook inspeccionará integridad, identidad, versiones, canal, campos y pendientes humanos; producirá `evaluacion-presentacion-candidatura.md` y dejará el gate de presentación en `pendiente` o `bloqueado` según el resultado. El gate, la orden humana y el envío permanecerán separados.

**Tecnologías:** Markdown/YAML, Obsidian, pruebas `unittest`, inspección reversible del portal Lidl.

## Restricciones globales

- No presentar, enviar, confirmar ni marcar `presentada: true`.
- No modificar CV, carta, contenido semántico, guiones ni veredictos previos.
- No inventar respuestas de formulario; los datos personales solo se usan si están autorizados.
- Mantener `GATE-CANDIDATURA-PRESENTACION` separado de `presentada`.
- Conservar las menciones históricas y modificar únicamente estados vivos.

---

### Tarea 1: Contrato y pruebas documentales

**Archivos:**
- Crear: `docs/ideas-y-debates/mejoras-job-up/PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA.md`
- Crear: `docs/ideas-y-debates/mejoras-job-up/TEMPLATE_EVALUACION_PRESENTACION_CANDIDATURA.md`
- Crear: `tests/test_validar_presentacion_candidatura.py`

**Interfaces:**
- Entrada: `paquete-presentacion.md` y fuentes aprobadas de la candidatura.
- Salida: `evaluacion-presentacion-candidatura.md` con resultado `APTA_PARA_PRESENTACION`, `APTA_CON_PENDIENTES_HUMANOS` o `BLOQUEADA`.

- [ ] Escribir pruebas fallidas que exijan los metadatos del playbook, las seis dimensiones, la frontera de no presentación, los tres resultados y los doce casos T01–T12.
- [ ] Ejecutar `python -m unittest tests/test_validar_presentacion_candidatura.py` y confirmar que falla porque los dos documentos todavía no existen.
- [ ] Crear el playbook y el template con el contrato exacto del prompt, la clasificación de hallazgos, el resultado determinista, la trazabilidad y el control explícito de no presentación.
- [ ] Ejecutar las pruebas documentales y confirmar que pasan.

### Tarea 2: Apertura controlada del gate

**Archivos:**
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/candidatura.md`
- Modificar: `.../paquete-presentacion.md`
- Modificar: `.pcs/sesiones/sesion-20260805-1757-job-up.md`
- Modificar: `.pcs/estado/estado-actual.md`
- Modificar: `docs/ideas-y-debates/mejoras-job-up/SPEC-Arquitectura-modular-generación-candidatura-v0-4-0.md`

- [ ] Verificar las precondiciones vivas: CV y carta aprobados, paquete `listo_para_gate`, gate de presentación `no_abierto`, `presentada: false`.
- [ ] Registrar el paso inicial a `GATE-CANDIDATURA-PRESENTACION: pendiente` sin aprobarlo ni marcar presentación.
- [ ] Actualizar solo los resúmenes vivos y distinguir paquete preparado, gate pendiente y envío no realizado.

### Tarea 3: Validación real del canal y artefacto

**Archivos:**
- Crear: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-020-lidl-responsable-turno-tienda-tamaraceite/evaluacion-presentacion-candidatura.md`

- [ ] Inspeccionar de forma reversible el canal Lidl desde la oferta/portal, sin iniciar sesión ni enviar.
- [ ] Registrar artefactos, identidad, versiones, compatibilidad, campos visibles, preguntas, respuestas preparables y pendientes humanos.
- [ ] Determinar el resultado real y el estado final del gate según las reglas del playbook.
- [ ] Confirmar en el artefacto que no hubo acción irreversible y que `presentada: false`.

### Tarea 4: Verificación y cierre de implementación

- [ ] Ejecutar pruebas específicas, pruebas del paquete y suite completa.
- [ ] Ejecutar comprobación sintáctica y `git diff --check`.
- [ ] Comprobar referencias y estados vivos de gates.
- [ ] Actualizar PCS con resultado, bloqueantes, pendientes humanos, pruebas y siguiente paso.
- [ ] Revisar ortografía española y entregar informe operativo sin iniciar presentación.
