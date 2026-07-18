# Evaluación posterior de Vault Operator y Local REST API MCP

## Necesidad que resolvería cada plugin

- **Vault Operator:** evaluar si aporta operaciones repetibles de gestión de la bóveda que justifiquen su configuración específica por carpeta.
- **Local REST API MCP:** evaluar si permite una integración local útil con Obsidian para tareas concretas de lectura o automatización asistida.

## Datos y rutas que crearía

Ambos plugins se instalarían como configuraciones nuevas de la bóveda raíz. Sus rutas técnicas están previstas en `.gitignore`; no se reutilizarán datos, configuraciones ni directorios compartidos de la bóveda anterior.

## Riesgos de privacidad y mantenimiento

- Exposición local de notas o metadatos a procesos que no sean necesarios para el objetivo aprobado.
- Dependencia de configuraciones por carpeta que dificulten una futura reorganización.
- Coste de mantenimiento, actualizaciones y diagnóstico superior al beneficio de uso real.

## Prueba mínima reversible

1. Definir una única tarea concreta que no pueda resolverse cómodamente con Obsidian y Hide Folders.
2. Instalar solo el plugin necesario en la bóveda raíz, con configuración nueva y sin migrar datos heredados.
3. Probarlo sobre un conjunto mínimo de notas no sensibles.
4. Documentar el beneficio observado, los datos creados y el coste de mantenimiento.
5. Retirar el plugin y sus datos si no supera el criterio acordado.

## Decisión requerida

Decidir por separado para cada plugin si su beneficio justifica una instalación limpia y mantenible. Esta nota no autoriza instalar, configurar ni mover ningún plugin.
