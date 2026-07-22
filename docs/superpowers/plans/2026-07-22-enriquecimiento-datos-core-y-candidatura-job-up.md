# Enriquecimiento de datos core y candidatura Job-up — Plan de ejecución

> **Para agentes de ejecución:** SUBSKILL REQUERIDA: usar `superpowers:subagent-driven-development` para ejecutar este plan tarea por tarea. Los pasos usan sintaxis de casilla (`- [ ]`) para el seguimiento.

**Objetivo:** incorporar la evidencia ejecutiva validada y rehacer el CV maestro, su PDF y los emails de candidatura espontánea para su revisión humana.

**Arquitectura:** `datos-core-busqueda.md` conservará hechos, límites y atribuciones. `seleccion-factual.md` será la selección no política y ejecutiva que alimenta el CV y los emails. El DOCX y PDF presentarán una única identidad de Dirección, Administración y Operaciones; el email modular aplicará el registro formal o cercano acordado.

**Tecnologías:** Markdown, DOCX, PDF y las herramientas de validación estructural y visual del entorno.

## Restricciones globales

- Mantener como perfiles objetivo: Dirección, Administración y Operaciones; no gestión pública.
- Conservar la experiencia municipal solo como histórico factual y excluirla de selección factual, CV, PDF y emails.
- No incluir parentescos, composición familiar, detalles de conflictos laborales ni afirmaciones no verificadas.
- Mantener la atribución correcta entre acciones individuales, decisiones colegiadas y contexto de mercado.
- Redactar las acciones de candidatura en primera persona y revisar explícitamente la ortografía española.
- Mantener el CV en español y con dos páginas; no enviar ni compartir ningún material.
- No usar LibreOffice mediante automatización para abrir documentos; validar el DOCX con herramientas estructurales y el PDF con Poppler.

---

### Task 1: Actualizar la fuente factual y la selección ejecutiva

**Archivos:**
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda.md`
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/seleccion-factual.md`
- Fuente de contraste: `boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda-v3.md`

**Consume:** las decisiones del diseño `2026-07-22-enriquecimiento-datos-core-job-up-design.md`.

**Produce:** un banco factual con `HER-04`, `HER-05`, una versión prudente de `HER-06`, escala de Herfrailes y perfiles sin gestión pública; una selección factual lista para el CV y emails.

- [ ] Incorporar solo los hechos verificables de `HER-04`, `HER-05` y `HER-06`; trasladar los detalles sensibles de `HER-06` a una precaución de uso y no a texto candidatable.
- [ ] Añadir la escala de Herfrailes y los límites de atribución a central SPAR y Consejo de Dirección.
- [ ] Eliminar la gestión pública de perfiles objetivo, logros seleccionables por defecto y plantillas; preservar el histórico municipal sin usarlo en la selección factual.
- [ ] Excluir parentescos, encuadres salariales y narrativas persuasivas de la fuente factual.
- [ ] Revisar referencias, exclusiones políticas, atribuciones y ortografía.
- [ ] Ejecutar comprobaciones de búsqueda para confirmar que la selección factual no contiene `Gáldar`, `Concejal`, `GAL-01`, `gestión pública`, `Ayuntamiento`, `Titulación Universitaria` ni la formulación antigua de Granintra.
- [ ] Confirmar mediante diff que los nuevos hechos y límites de atribución están presentes.
- [ ] Registrar un commit con solo los archivos de esta tarea.

### Task 2: Rehacer CV maestro DOCX y PDF

**Archivos:**
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/cv-maestro.docx`
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/cv-maestro.pdf`
- Consume: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/seleccion-factual.md`

**Produce:** un CV maestro en español, de dos páginas, con identidad de dirección ejecutiva y operaciones y PDF equivalente.

- [ ] Sustituir el resumen centrado en RR. HH. por un posicionamiento de dirección ejecutiva que conecte personas, procesos, sistemas y operaciones.
- [ ] Incluir resultados verificables de aprovisionamiento, mantenimiento de vehículos, organización del trabajo y análisis de datos, sin atribuir decisiones colegiadas ni efectos no medidos.
- [ ] Mantener las acciones en primera persona y la formación como “Máster en Inteligencia Artificial con Certificación Universitaria”, en curso.
- [ ] Excluir experiencia política, gestión pública, Ayuntamiento de Gáldar, concejalía, parentescos y detalles sensibles de conflictos.
- [ ] Mantener el diseño existente cuando no impida el nuevo contenido; el resultado final debe tener dos páginas legibles.
- [ ] Validar estructura y texto del DOCX; validar que el PDF contiene el contenido actualizado y tiene exactamente dos páginas.
- [ ] Renderizar el PDF a PNG mediante Poppler e inspeccionar visualmente ambas páginas para confirmar legibilidad, ausencia de solapamientos y jerarquía clara.
- [ ] Revisar ortografía española y registrar un commit con el DOCX y PDF.

### Task 3: Rehacer los modelos de email y realizar la validación transversal

**Archivos:**
- Modificar: `boveda-entrevista-profesional/busqueda-empleo/presentacion-espontanea/email-presentacion.md`
- Validar: `datos-core-busqueda.md`, `presentacion-espontanea/seleccion-factual.md`, `presentacion-espontanea/cv-maestro.docx` y `presentacion-espontanea/cv-maestro.pdf`

**Produce:** tres emails breves, coherentes con el CV y listos para revisión: empresa, intermediario y contacto personal.

- [x] Reemplazar la enumeración de tareas por un núcleo de dirección ejecutiva y operativa con dos o tres resultados verificables.
- [x] Para empresa e intermediario, usar trato formal coherente de principio a fin; para contacto personal, trato profesional cercano.
- [x] Incorporar una apertura personalizable para empresas que se base en un reto, proyecto o contexto real y comprobable, sin afirmar conocimiento no verificado.
- [x] Cerrar con una invitación concreta y respetuosa a una conversación breve, sin prometer aportaciones no demostradas.
- [x] Mantener la exclusión política, la primera persona y la posibilidad de convertir el cuerpo en carta formal si se solicita.
- [x] Ejecutar búsquedas transversales de exclusiones y de formas verbales en tercera persona candidatable; revisar ortografía española.
- [x] Confirmar coherencia textual entre los hechos del CV, la selección factual y los emails.
- [x] Registrar un commit con el email y actualizar las casillas de este plan.

### Task 4: Revisión final de los materiales preparados

**Archivos:**
- Validar: todos los archivos modificados por las tareas 1 a 3.

**Produce:** evidencia de que los materiales quedan listos para revisión humana, sin envío ni publicación.

- [ ] Revisar el diff completo desde la base de la rama y comprobar que no introduce datos privados, gestión pública o atribuciones incorrectas.
- [ ] Repetir las comprobaciones de exclusión, las verificaciones de dos páginas y la inspección visual del PDF final.
- [ ] Verificar la ortografía de los documentos Markdown y la correspondencia del PDF con el DOCX.
- [ ] Dejar los materiales sin enviar y sin compartir; no realizar ninguna acción externa.
- [ ] Registrar el resultado de revisión en el último commit o en el informe de revisión de la rama.
