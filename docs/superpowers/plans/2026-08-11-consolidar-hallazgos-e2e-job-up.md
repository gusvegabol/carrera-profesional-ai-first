# Consolidar hallazgos E2E de Job-up — Plan de implementación

> **Para agentes:** ejecutar este plan tarea a tarea con puntos de verificación. La presentación externa permanece fuera de alcance y no se crea CAND-2026-022.

**Objetivo:** convertir los hallazgos E2E reales de CAND-2026-021 en reglas canónicas, correcciones técnicas, regresiones automatizadas y documentación alineada, dejando el flujo listo para una nueva prueba real.

**Arquitectura:** la skill será una orquestadora que remite a playbooks y no duplica contratos. El cierre activo termina en `documentalmente_completa` con `presentada: false`; cualquier validación de presentación queda únicamente en `futuro/presentacion/`. Los datos reutilizables se separan de decisiones específicas de candidatura.

**Tech Stack:** Markdown/YAML, Python, `unittest`, `python-docx`, OOXML, Poppler/pypdfium2 para QA visual y comprobaciones de rutas canónicas.

## Restricciones globales

- No crear CAND-2026-022 ni ejecutar una nueva oferta.
- No modificar el contenido semántico aprobado de CAND-2026-021.
- No iniciar sesión, cargar archivos, aceptar consentimientos ni enviar candidaturas.
- CV: fotografía incluida por defecto; solo se excluye por decisión humana expresa.
- `documentalmente_completa` es el final del flujo activo y mantiene `presentada: false`.
- La cultura empresarial es contexto, nunca evidencia ni afinidad personal.
- Los gates aprobados con siguiente acción determinista no generan pausas redundantes.

---

### Tarea 1: Crear regresiones E2E antes de corregir contratos

**Archivos:**
- Modificar: `tests/test_job_up_candidatura_oferta_skill.py`
- Modificar: `tests/test_candidatura_documental_completa.py`
- Modificar: `tests/test_componer_carta_presentacion.py`
- Crear: `tests/test_hallazgos_e2e_job_up.py`

**Interfaces:**
- Las pruebas comprobarán defaults de fotografía, datos core, preguntas previas al gate, cultura temprana, transiciones deterministas, hard wrapping, revisión visual, identidad dinámica y cierre documental.

- [ ] Escribir pruebas que reproduzcan cada defecto observado y fallen contra el contrato actual.
- [ ] Ejecutar `python -m unittest tests.test_hallazgos_e2e_job_up -v` y registrar los fallos esperados.

### Tarea 2: Corregir fotografía por defecto y autorización

**Archivos:**
- Modificar: `.codex/skills/job-up-candidatura-oferta/SKILL.md`
- Modificar: `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md`
- Modificar: `docs/boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/GUIA_FORMATO_CV_Y_CARTA.md` si la ruta canónica lo requiere
- Modificar: `tests/test_fotografia_cv_carta.py`

**Interfaces:**
- La orquestación debe interpretar ausencia de exclusión fotográfica como `incluir` para el CV y no generar pregunta, pendiente ni bloqueo.

- [ ] Declarar el default en la skill y playbook, remitiendo al contrato visual.
- [ ] Añadir el caso exacto de autorización de cinco datos sin mención de foto.
- [ ] Ejecutar las pruebas de fotografía y skill.

### Tarea 3: Persistir vehículo propio y separar movilidad

**Archivos:**
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/fuentes/datos-core-busqueda.md`
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-021-obramat-coordinador-linea-cajas/candidatura.md` solo para sincronizar evidencia ya registrada
- Modificar: `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md`
- Modificar: `.codex/skills/job-up-candidatura-oferta/SKILL.md`
- Modificar: `tests/test_hallazgos_e2e_job_up.py`

**Interfaces:**
- Data Core contendrá un hecho reutilizable `vehiculo_propio: confirmado` con fuente humana y fecha.
- Movilidad territorial se resolverá como disponibilidad/preferencia antes de `GATE-CANDIDATURA-GUION`; la aceptación de una movilidad concreta quedará en la candidatura si procede.

- [ ] Ubicar vehículo propio en la sección semántica existente de movilidad/disponibilidad.
- [ ] Incorporar la regla de pregunta previa al gate para movilidad relevante sin evidencia.
- [ ] Añadir pruebas de reutilización y de bloqueo previo al gate.

### Tarea 4: Hacer temprana la disponibilidad de contexto cultural

**Archivos:**
- Modificar: `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md`
- Modificar: `.codex/skills/job-up-candidatura-oferta/SKILL.md`
- Modificar: `tests/test_hallazgos_e2e_job_up.py`

**Interfaces:**
- La cultura se localiza o solicita tras identificar la empresa y antes de cerrar decisiones afectadas; se conserva como contexto con procedencia.

- [ ] Añadir la fase de contexto corporativo temprano y su fallback.
- [ ] Prohibir convertir cultura en afinidad personal o evidencia profesional.
- [ ] Añadir prueba de disponibilidad antes del guion cuando sea útil.

### Tarea 5: Eliminar pausas redundantes de transiciones deterministas

**Archivos:**
- Modificar: `.codex/skills/job-up-candidatura-oferta/SKILL.md`
- Modificar: `docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md`
- Modificar: `tests/test_hallazgos_e2e_job_up.py`

**Interfaces:**
- Tras un gate aprobado, sin dato nuevo, decisión nueva, revisión humana o acción irreversible, la skill continuará al siguiente playbook.

- [ ] Documentar la regla general y sus excepciones.
- [ ] Cubrir composición tras `GATE-CONTENIDO-CARTA-COMPOSICION` y veredicto tras `GATE-CARTA-REVISION-HUMANA`.

### Tarea 6: Consolidar composición visual e identidad dinámica

**Archivos:**
- Modificar: `scripts/job-up/componer_carta_presentacion.py`
- Modificar: `tests/test_componer_carta_presentacion.py`
- Modificar: `docs/metodologia/playbooks/PLAYBOOK_COMPONER_CARTA_PRESENTACION.md`
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_COMPOSICION_CARTA_PRESENTACION.md`

**Interfaces:**
- Hard wrapping: líneas consecutivas no vacías se unen con espacios; líneas vacías separan párrafos; no se generan `<w:br/>` espurios.
- La evaluación distingue `render_generado` de `render_inspeccionado` y solo declara inspección visual con evidencia de PNG revisado.
- Identidad, datos autorizados, fecha, asunto y jerarquía visual se derivan dinámicamente.

- [ ] Alinear playbook/template con la implementación ya corregida.
- [ ] Añadir una evidencia explícita de inspección visual al resultado técnico.
- [ ] Mantener pruebas de equivalencia, ausencia de saltos e identidad CAND-A/CAND-B.

### Tarea 7: Cerrar el flujo activo en documentalmente_completa

**Archivos:**
- Modificar: `.codex/skills/job-up-candidatura-oferta/SKILL.md`
- Modificar: `docs/metodologia/playbooks/PLAYBOOK_VEREDICTO_FINAL_CV.md`
- Modificar: `docs/metodologia/playbooks/PLAYBOOK_VEREDICTO_FINAL_CARTA.md`
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_VEREDICTO_FINAL_CARTA.md`
- Modificar: `docs/metodologia/playbooks/README_JOB_UP.md`
- Modificar: `docs/ideas-y-debates/mejoras-job-up/SPEC-Arquitectura-modular-generación-candidatura-v0-4-0.md`
- Modificar: `tests/test_hallazgos_e2e_job_up.py`

**Interfaces:**
- No hay módulo activo posterior a la aprobación de CV/carta. Los artefactos de presentación permanecen en `futuro/presentacion/`.

- [ ] Retirar referencias operativas a paquete/gate de presentación sin borrar historia válida.
- [ ] Cambiar la siguiente acción de los veredictos a cierre documental y nueva prueba real futura.
- [ ] Añadir pruebas de fin documental y `presentada: false`.

### Tarea 8: Resolver semántica de recomendación de carta

**Archivos:**
- Modificar: `docs/metodologia/playbooks/PLAYBOOK_VEREDICTO_FINAL_CARTA.md`
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/TEMPLATE_VEREDICTO_FINAL_CARTA.md`
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/CAND-2026-021-obramat-coordinador-linea-cajas/veredicto-final-carta.md`
- Modificar: `tests/test_hallazgos_e2e_job_up.py`

**Interfaces:**
- Sustituir `recomendacion_inclusion_paquete` por `recomendacion_inclusion_carta` cuando represente la utilidad editorial de adjuntar la carta al conjunto documental; no se ligará a un paquete de presentación.

- [ ] Documentar la decisión y actualizar el caso real.
- [ ] Mantener compatibilidad histórica solo en artefactos archivados.

### Tarea 9: Consolidar documentación, SPEC y PCS

**Archivos:**
- Modificar: `docs/ideas-y-debates/mejoras-job-up/SPEC-Arquitectura-modular-generación-candidatura-v0-4-0.md`
- Modificar: `.pcs/estado/estado-actual.md`
- Modificar: `.pcs/sesiones/sesion-20260805-1757-job-up.md`
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/README.md`
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/seguimiento/seguimiento-candidaturas.md`

**Interfaces:**
- La SPEC registrará reglas arquitectónicas, no un log de bugs. PCS conservará causas, correcciones, pruebas y estado final.

- [ ] Registrar los diez hallazgos E2E y sus reglas canónicas.
- [ ] Confirmar CAND-2026-021 documentalmente completa y sin paquete activo.
- [ ] Confirmar que CAND-2026-022 no existe.

### Tarea 10: Verificación final

- [ ] Ejecutar `python -m unittest discover -s tests`.
- [ ] Ejecutar `python -m compileall scripts tests`.
- [ ] Ejecutar `git diff --check`.
- [ ] Buscar referencias residuales y clasificarlas como activas, históricas o futuras.
- [ ] Verificar rutas canónicas y estado de CAND-2026-021.
- [ ] Emitir veredicto `JOB-UP LISTO PARA NUEVA PRUEBA E2E REAL` solo si todo pasa.
