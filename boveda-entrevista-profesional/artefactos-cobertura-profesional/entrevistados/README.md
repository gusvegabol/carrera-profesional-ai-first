# README — entrevistados

## Estado de este documento

Primer README específico de subcarpeta dentro de `artefactos-cobertura-profesional/` — el resto de subcarpetas (`mapas/`, `checkpoints/`, `inmersiones/`, `competencias/`, `sesiones/`) todavía documentan sus peculiaridades solo en el `README.md` general de la carpeta padre. Si se decide que cada subcarpeta debe tener el suyo propio (punto pendiente de la revisión de Gustavo, incluida la posible tabla de histórico al final de cada README), este documento sirve de primer ejemplo a replicar, no como formato ya cerrado.

## Contenido

Un fichero por persona entrevistada — `ENTREVISTADO_<id_entrevistado>.md`, usando la plantilla `templates/TEMPLATE_ENTREVISTADO.md`.

Solo tres campos: `id_entrevistado`, `alias`, `fecha_creacion`. Deliberadamente mínimo — no se guarda nombre real, contexto vital, ni ningún otro dato mientras el proyecto siga en fase de validar si la entrevista funciona. Ampliar este fichero es una decisión explícita futura, no algo que deba crecer por inercia.

## Creación

Manual, no automática. En esta fase, Gustavo crea el fichero y asigna el alias directamente — no hay pregunta de apertura de sesión que lo pida ni lógica del playbook que lo genere. La asignación automática de alias (vía frontend, con datos adicionales en JSON o SQLite) pertenece a una etapa posterior del proyecto, fuera de alcance de esta carpeta.

## Numeración

`id_entrevistado` sigue el esquema ya documentado en el `README.md` de `artefactos-cobertura-profesional/` — contador global `ENT-<nnn>`, 3 dígitos, ceros a la izquierda, registrado en `artefactos-cobertura-profesional/_contadores.md`. Es el único identificador de todo el sistema que no es anidado; todos los demás (mapa, zona, intento) cuelgan de este.

## Relación con otras carpetas

No mantiene lista de mapas asociados — se consulta filtrando por `id_entrevistado` en el frontmatter de `mapas/`, evitando una lista redundante que podría desincronizarse del contenido real.

## Fuente base

Redactado por Claude, 2026-07-06, tras decisión de Gustavo de mantener este fichero deliberadamente mínimo mientras el proyecto sigue en fase de validación.
