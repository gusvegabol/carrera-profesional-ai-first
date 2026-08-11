# Plan: implantar veredicto final de carta

> Plan de implementación para `PLAYBOOK_VEREDICTO_FINAL_CARTA` y su primera
> prueba controlada con `CAND-2026-020`.

## Objetivo

Crear el contrato documental y las comprobaciones técnicas de la fase que
evalúa una carta ya compuesta y aprobada en revisión humana, separando calidad
de conveniencia de inclusión, sin redactar ni presentar la candidatura.

## Pasos

1. **Confirmar precondiciones y límites**
   - Verificar `GATE-CARTA-REVISION-HUMANA: aprobado`, `presentada: false` y
     `GATE-CANDIDATURA-PRESENTACION: no_abierto` en las fuentes canónicas.
   - Revisar SPEC, playbooks y templates relacionados, y registrar cualquier
     ausencia de `SYSTEM_PROMPT.md` o `INSTRUCCIONES_PARA_CHATGPT.md`.

2. **Crear el contrato documental**
   - Crear `PLAYBOOK_VEREDICTO_FINAL_CARTA.md` v1.0.0 en `en_prueba`.
   - Crear `TEMPLATE_VEREDICTO_FINAL_CARTA.md` v1.0.0 en `en_prueba` con las 37
     secciones mínimas y la salida `GATE-VEREDICTO-CARTA`.
   - Mantener los límites de fuentes, independencia de roles, no ampliación y
     no presentación definidos por la SPEC.

3. **Añadir comprobación determinista sin alterar fases previas**
   - Crear un verificador aislado para validar precondiciones, categorías de
     hallazgos, síntesis determinista, valor incremental y transición del gate.
   - No modificar carta, CV, contenido, guion, JSON ni scripts existentes.

4. **Cubrir el contrato con pruebas**
   - Añadir pruebas nuevas para T01–T17, separando controles estructurales
     automatizables de los escenarios semánticos documentados.
   - Ejecutar además regresiones de la suite existente.

5. **Ejecutar el caso real**
   - Evaluar exactamente los artefactos vigentes de `CAND-2026-020` desde los
     tres roles.
   - Generar `veredicto-final-carta.md` sin modificar la carta ni el paquete.
   - Dejar `GATE-VEREDICTO-CARTA` en `pendiente` si el resultado habilita
     decisión humana; no abrir el gate de presentación.

6. **Validar y sincronizar continuidad**
   - Ejecutar pruebas relevantes, `git diff --check`, referencias y nombres de
     gates, y confirmar `presentada: false`.
   - Actualizar únicamente la sesión PCS activa y `estado-actual.md` con el
     nuevo contrato, resultado, pruebas, defectos generalizables y siguiente
     paso contractual.

7. **Informe final**
   - Entregar archivos creados/modificados, resultado del caso, hallazgos,
     valor incremental, recomendación de inclusión, estado exacto del gate,
     pruebas, regresiones, cambios arquitectónicos y siguiente paso.

## Criterio de finalización

El playbook y el template son coherentes, el caso real tiene un veredicto
auditable, las pruebas pasan, el gate humano no se aprueba automáticamente y
no se realiza presentación externa.
