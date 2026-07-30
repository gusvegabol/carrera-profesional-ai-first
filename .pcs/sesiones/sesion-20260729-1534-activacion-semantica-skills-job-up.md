---
id: sesion-20260729-1534-activacion-semantica-skills-job-up
titulo: Activación semántica de las skills de Job-up
inicio: 2026-07-29 15:34
cierre: 2026-07-30T13:45:41+01:00
estado: cerrada
tipo: sesion
host: carrera-ai
sesion_relacionada: sesion-20260729-1320-organizacion-documentacion-job-up
---

# Sesión — Activación semántica de las skills de Job-up

## 1. Contexto mínimo

La reorganización documental de Job-up contempla tres skills: `job-up-inicia-sesion`, `job-up-genera-cv-empresa` y `job-up-candidatura-oferta`. El diseño vigente mantiene `allow_implicit_invocation: false` para las tres.

Surge la necesidad de decidir si, una vez renombradas, deben poder iniciarse también mediante peticiones en lenguaje natural, además de por invocación directa.

Esta sesión se crea en pausa para retomar esa decisión sin interrumpir la sesión de diseño documental de Job-up.

## 2. Objetivo operativo

Definir la política de activación semántica de las skills de Job-up, sus descripciones de descubrimiento y sus límites de seguridad y desambiguación.

## 3. Capa episódica

### Hechos observables

- Las configuraciones actuales de las dos skills existentes usan `allow_implicit_invocation: false`.
- La activación semántica requiere una política explícita que la permita y metadatos que describan con precisión cada intención.
- La futura skill `job-up-candidatura-oferta` debe seguir exigiendo una única sesión PCS de Job-up ya abierta; la activación semántica no debe abrirla por sí misma.

### Resultado de la sesión

No se adopta ni se implementa todavía ninguna política. El análisis se difiere deliberadamente a esta sesión pausada.

## 4. Capa semántica

### Pregunta de diseño

¿Deben las skills de Job-up responder a intenciones expresadas de forma natural —por ejemplo, «quiero trabajar una oferta»— o requerir siempre una llamada explícita a la skill?

### Fuentes a consultar al retomar

- [[docs/superpowers/specs/2026-07-29-organizacion-documental-job-up-design]]: sección de skills de Job-up.
- [[sesion-20260729-1320-organizacion-documentacion-job-up]]: decisiones de organización y flujo de entrada.
- Configuraciones `agents/openai.yaml` y `SKILL.md` de las skills actuales en `.codex/skills/`.

## 5. Decisiones y acciones PCS

No se crean decisiones ni acciones PCS en esta sesión. La elección de política queda pendiente de análisis y aprobación explícita.

## 6. Líneas de exploración al retomar

- Comparar activación exclusivamente explícita frente a activación semántica controlada.
- Definir frases de activación y exclusiones para cada skill.
- Evitar solapamientos entre iniciar una sesión, trabajar una oferta, generar un CV y realizar una presentación espontánea.
- Establecer una batería breve de ejemplos positivos, ambiguos y negativos para comprobar el comportamiento esperado.
- Mantener las salvaguardas de contexto PCS, datos privados y aprobación humana definidas para Job-up.

## 7. Rehidratación de la sesión

1. Leer esta sesión y la especificación de organización documental de Job-up.
2. Revisar las configuraciones reales de las skills antes de proponer cambios.
3. Acordar la política antes de modificar `allow_implicit_invocation`, nombres, descripciones o rutas.
4. Si se aprueba un cambio, actualizar la especificación y las skills de forma coordinada.

## 8. Checklist de reanudación

- [ ] Revisar la política actual de activación de cada skill.
- [ ] Proponer y acordar la política de activación semántica.
- [ ] Definir ejemplos de invocación y desambiguación.
- [ ] Actualizar el diseño y las configuraciones aprobadas.
- [ ] Verificar el comportamiento resultante.

## 9. Trazabilidad

- Sesión relacionada: [[sesion-20260729-1320-organizacion-documentacion-job-up]].
- Estado histórico previo: en pausa; no representa estado operativo vivo ni modifica el seguimiento PCS.

## Cierre documental

Sesión cerrada al iniciar el nuevo bloque Job-up del 2026-07-30. La línea cognitiva queda conservada como historial y no se adopta ninguna política pendiente.
