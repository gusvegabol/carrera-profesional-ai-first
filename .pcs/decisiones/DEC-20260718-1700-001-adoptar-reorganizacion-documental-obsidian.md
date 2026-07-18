---
id: DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian
titulo: Adoptar la reorganización documental y la nueva bóveda Obsidian
estado: vigente
fecha_registro: 2026-07-18
fecha_adopcion: 2026-07-18
fecha_vigencia: 2026-07-18
tipo: decision
host: carrera-ai
---

# DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian — Adoptar la reorganización documental y la nueva bóveda Obsidian

## Enunciado de la decisión

Se adopta la reorganización documental de Carrera AI y una única bóveda de Obsidian con configuración nueva y limpia en la raíz del repositorio. Antes de retirar las configuraciones heredadas, deberá existir una copia externa completa y verificada del proyecto.

La implantación retirará las cinco rutas heredadas: `boveda-entrevista-profesional/.obsidian/`, `boveda-entrevista-profesional/.obsidian-agent/`, `boveda-entrevista-profesional/.vault-operator/`, `obsilo-shared/` y `vault-operator-shared/`. La migración documental se realizará con Git por bloques previamente aprobados y no se utilizará Obsidian CLI.

Esta decisión autoriza exclusivamente el inventario, la copia externa, la configuración limpia y la migración por bloques validada. Cada aprobación posterior de clasificación decidirá el destino de su bloque documental; no queda absorbida ni sustituida por esta decisión de implantación.

## Motivo

Una bóveda raíz única facilitará la lectura y navegación de la documentación viva sin alterar la autoridad de PCS, del SPEC, del versionado funcional ni de los playbooks. La configuración limpia y la retirada controlada del entorno heredado evitan mantener bóvedas anidadas o trasladar configuraciones, plugins e historiales que puedan condicionar la nueva arquitectura.

## Contexto

La propuesta de uso transversal de Obsidian se debatió en la sesión de origen y se concretó en el diseño aprobado de reorganización documental. El diseño exige trazabilidad Git, clasificación humana por bloques, corrección de enlaces tras cada movimiento y una copia externa recuperable antes de cualquier eliminación.

## Alternativas descartadas

- Mantener la bóveda localizada en `boveda-entrevista-profesional/`.
- Abrir la raíz sin una política de exclusiones y clasificación.
- Crear una bóveda espejo que duplique la documentación del repositorio.
- Migrar la configuración, los plugins, los historiales o los datos heredados a la nueva bóveda.

## Impacto esperado

- Una única superficie de navegación para la documentación viva del repositorio.
- Separación visible entre documentación viva, continuidad PCS, trabajo en curso e histórico.
- Migración reversible y trazable mediante copia externa y Git.
- Eliminación de configuraciones Obsidian anidadas antes de inicializar la bóveda raíz.

## Alcance

La decisión afecta a la implantación documentada en la [especificación aprobada](../../docs/superpowers/specs/2026-07-18-reorganizacion-documental-obsidian-design.md). No autoriza eliminar documentación, mover archivos sin aprobación de bloque, alterar la estructura o gobernanza de `.pcs/`, ni instalar Vault Operator o Local REST API MCP durante la reorganización.

## Relaciones

- Sesión de origen: [debate sobre Obsidian en todo el proyecto](../sesiones/sesion-20260717-1930-debate-obsidian-proyecto-completo.md).
- Especificación aprobada: [diseño de reorganización documental y nueva bóveda Obsidian](../../docs/superpowers/specs/2026-07-18-reorganizacion-documental-obsidian-design.md).
- Acción de implantación: [ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian](../acciones/ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian.md).
- Estado operativo: [estado actual](../estado/estado-actual.md).
- Decisión anterior o sustituida: ninguna.

## Revisión futura

Revisar esta decisión si una aprobación posterior de clasificación revela que el modelo por bloques no permite preservar la trazabilidad, si falla la restauración desde la copia externa o si se propone cambiar el alcance de las rutas técnicas excluidas.
