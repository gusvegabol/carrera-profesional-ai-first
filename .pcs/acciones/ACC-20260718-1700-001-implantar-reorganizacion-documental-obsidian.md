---
id: ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian
titulo: Implantar la reorganización documental de Obsidian
estado: completada
prioridad: alta
responsable: Persona responsable y Codex
fecha_creacion: 2026-07-18
fecha_actualizacion: 2026-07-18
tipo: accion
host: carrera-ai
---

# ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian — Implantar la reorganización documental de Obsidian

## Descripción

Implantar por bloques la reorganización documental aprobada: inventariar y clasificar los documentos, verificar una copia externa completa, retirar el entorno heredado, inicializar manualmente la bóveda raíz y migrar únicamente los bloques aprobados mediante Git, con sus enlaces comprobados.

## Origen

- Sesión de origen: [debate sobre Obsidian en todo el proyecto](../sesiones/sesion-20260717-1930-debate-obsidian-proyecto-completo.md).
- Decisión de origen: [adopción de la reorganización documental y la nueva bóveda Obsidian](../decisiones/DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian.md).
- Especificación aprobada: [diseño de reorganización documental y nueva bóveda Obsidian](../../docs/superpowers/specs/2026-07-18-reorganizacion-documental-obsidian-design.md).

## Seguimiento

- Progreso: la copia externa completa se verificó en `D:\carrera-profesional-ai-first`; se retiraron las cinco rutas heredadas; la bóveda raíz se creó manualmente con Hide Folders; el mapa fue aprobado por bloques y sus movimientos se registraron mediante Git.
- Validación final: la persona responsable confirmó en Obsidian la visibilidad de las notas vivas, la exclusión de las rutas técnicas e históricas y la navegación de los enlaces revisados.
- Estado de cierre: todos los criterios se han cumplido; no quedan dependencias dentro del alcance de esta acción.

## Evidencia de avance

- Estructura, plantillas y política Git: `d7b1e71`.
- Mapa de clasificación aprobado: `15482ef` y `6366891`.
- Migración documental por bloques: `51b9f52`, `154884a`, `c20b6fc`, `9303a48`, `8407597` y `828dd0c`.
- La modificación local de `PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_0.md` permanece fuera de los commits de migración.
- Validación visual final de la bóveda raíz: confirmada por la persona responsable el 2026-07-18.

## Criterio de cierre

- Copia externa completa verificada.
- No quedan configuraciones Obsidian anidadas.
- Bóveda raíz inicializada y Hide Folders configurado manualmente.
- Mapa de clasificación aprobado por bloques.
- Movimientos Git y enlaces verificados para todos los bloques aprobados.
- Histórico separado y rutas técnicas excluidas de la navegación.

## Relaciones

- Sesión relacionada: [debate sobre Obsidian en todo el proyecto](../sesiones/sesion-20260717-1930-debate-obsidian-proyecto-completo.md).
- Decisión relacionada: [DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian](../decisiones/DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian.md).
- Estado de proyecto: [estado actual](../estado/estado-actual.md).
