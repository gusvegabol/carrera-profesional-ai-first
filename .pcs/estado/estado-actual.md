---
id: estado-actual
titulo: carrera-profesional-ai-first
estado: vigente
fecha_actualizacion: 2026-07-18
ultima_sesion_relacionada: sesion-20260717-1930-debate-obsidian-proyecto-completo
host: carrera-ai
---

# estado-actual

## Situación actual

Carrera AI 2.0 está en desarrollo sobre la versión base 1.6. Su objetivo es validar con una persona el recorrido cobertura profesional → inmersión en profundidad → evidencias → síntesis de trayectoria → Perfil Profesional Accionable integral y revisable.

La fuente funcional de verdad sobre la versión global es `docs/VERSIONADO_CARRERA_AI.md`. El SPEC conserva la definición del producto, mientras PCS registra la continuidad operativa y la decisión humana que adoptó el modelo de versionado.

ESCO permanece como investigación paralela fuera del criterio de finalización de 2.0 y como candidata provisional a una posible 2.5, que no está abierta.

La orientación local de `carrera-ai` ha completado su migración a PCS 2.0. `README.md` y `AGENTS.md` aplican el paquete documental vigente, las reglas PCS 1.0 se han retirado de la capa `.codex/` activa y se conserva únicamente la skill local `pcs-obsidian-corrige-links`. El registro central está cerrado en `pcs_version: "2.0"` y `status: vigente`. La segunda pasada se clasificó como C y confirmó la idempotencia del flujo sin nuevas escrituras en el host.

Se ha formalizado y materializado la retirada de Graphify de `carrera-ai` mediante `DEC-20260717-1058-001-retirada-graphify-carrera-ai`, siguiendo la decisión de referencia de PCS Core `DEC-20260715-0004-retirada-graphify-pcs-host`. La decisión local sustituye a `DEC-20260713-1344-001-integrar-graphify-tres-corpus`. La sesión de trabajo `sesion-20260717-1058-retirada-graphify-carrera-ai` registra la eliminación y quedó cerrada el 2026-07-17 tras completar la verificación.

La razón operativa es que el coste de tiempo y recursos de la extracción semántica resulta desproporcionado para el ritmo documental del host y que las salidas dependen de modelos que no siempre generan estructuras válidas. La localización y verificación de relaciones documentales se realiza directamente sobre las fuentes Markdown y sus enlaces. Se han eliminado los tres directorios de salida, el script de ejecución, las configuraciones específicas y las instrucciones operativas asociadas.

El trabajo vigente del host permanece en la revisión metodológica de la entrevista de cobertura profesional. `docs/DOCUMENTO_SPEC_CARRERA_AI.md` sigue definiendo el producto y se ha alineado de forma acotada con Carrera AI 2.0. El núcleo metodológico y el Perfil Profesional Accionable continúan siendo el marco para diseñar la cobertura de trayectorias profesionales sin sustituir el playbook de profundidad existente.

Se han elaborado cuatro propuestas para que una IA cubra toda la vida profesional de una persona, dos conservadoras y dos innovadoras. El informe `docs/Ideas debate - como afrontar entrevista cobertura profesional/05_Evaluacion_experta_y_recomendacion_de_enfoque.md` las compara con una rúbrica equilibrada y recomienda, de forma debatible, usar la Idea 2, doble pasada de panorama e inmersión selectiva, como arquitectura base de un primer piloto.

La recomendación requiere complementar esa arquitectura con la conversación no lineal, las anclas y los retornos opcionales de la Idea 1, y con un registro ligero de hipótesis, evidencia, límites y corrección por la persona de la Idea 4. El atlas relacional de la Idea 3 queda como posible evolución posterior, no como requisito del MVP. ESCO mantiene el papel de correspondencia candidata posterior, trazable y revisable; no prueba competencias individuales ni certifica a la persona.

También existe una presentación HTML autónoma para explicar la propuesta a personas no expertas: `docs/Ideas debate - como afrontar entrevista cobertura profesional/06_Presentacion_propuesta_recomendada.html`. Resume el problema, la doble pasada, sus garantías y el piloto propuesto.

Como línea documental transversal pendiente de decisión, se ha abierto `sesion-20260717-1930-debate-obsidian-proyecto-completo` y se ha elaborado `docs/PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.md`, junto con su presentación. La propuesta compara cuatro alternativas y recomienda debatir una bóveda Obsidian gobernada en la raíz del repositorio, con exclusiones explícitas, enlaces con ruta completa cuando haya nombres duplicados y una migración reversible. No es una decisión formal, no crea una acción de implantación ni autoriza mover, borrar o reconfigurar directorios.

Históricamente, la documentación de Graphify se mantuvo separada en tres corpus documentales: `.pcs/`, `docs/` y `boveda-entrevista-profesional/`. Esa organización quedó formalizada en `DEC-20260713-1344-001-integrar-graphify-tres-corpus`, ahora sustituida por la decisión de retirada. La decisión histórica afectaba únicamente a la indexación y recuperación de contexto; no adoptaba un playbook, no modificaba el SPEC ni convertía los artefactos del grafo en fuentes normativas.

Se ha cerrado `sesion-20260713-1344-integracion-operacion-graphify-carrera-ai.md` tras dejar trazada la línea histórica de integración, sus límites y la revisión futura de utilidad. Sus conclusiones quedan superadas operativamente por la retirada de Graphify. El estado actual, las decisiones vigentes y las fuentes documentales conservan su autoridad.

También se creó el repositorio GitHub `gusvegabol/carrera-profesional-ai-first` y quedó cerrada la sesión operativa asociada a su incorporación. El trabajo local puede sincronizarse ya con ese remoto bajo la cuenta personal conectada.

La utilidad de esa separación y de Graphify queda superada por la decisión de retirada. Una necesidad futura de análisis semántico solo podrá reabrirse mediante una decisión concreta y aprobada. La recomendación metodológica de doble pasada sigue siendo debatible y no ha sido adoptada como playbook.

## Foco operativo

Evaluar y decidir si la arquitectura recomendada de doble pasada, junto con sus salvaguardas requeridas, debe orientar el primer piloto de cobertura profesional. La propuesta de uso transversal de Obsidian permanece como línea secundaria de debate y no desplaza este foco metodológico.

## Próximos pasos

- Aplicar `docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md` en cualquier futura transición de versión.
- Revisar la evaluación experta y la presentación con las personas que deban debatir el enfoque.
- Decidir explícitamente si se adopta, modifica o descarta la recomendación para el primer piloto.
- Si se adopta, definir el contrato del piloto: muestra de entrevistas, salida inicial revisable, control de privacidad, criterios de corrección y señales de utilidad.
- Decidir explícitamente si se adopta, modifica o descarta la propuesta de uso transversal de Obsidian; si se aprobara, abrir una acción acotada de inventario, respaldo y prueba piloto antes de cualquier migración.
- Mantener separadas la cobertura, la profundidad y la correspondencia ESCO mientras no exista una decisión posterior que cambie ese alcance.
- No tratar la evaluación como validación con personas ni actualizar el SPEC o el playbook de profundidad por inferencia.

## Acciones abiertas relevantes

- `ACC-20260717-1642-001-materializar-versionado-carrera-ai` quedó completada; no deja trabajo abierto dentro de su alcance.
- No queda trabajo abierto para materializar la retirada de Graphify; la eliminación y las comprobaciones permanecen registradas históricamente en `sesion-20260717-1058-retirada-graphify-carrera-ai`.
- Es candidata a acción futura la definición del primer piloto, condicionada a una decisión explícita sobre la recomendación metodológica.
- No existe una acción abierta para implantar el uso transversal de Obsidian; cualquier implantación queda condicionada a una decisión explícita posterior.

## Decisiones vigentes relevantes

- `DEC-20260717-1642-001-versionado-funcional-carrera-ai` adopta el modelo global/componente, declara Carrera AI 2.0 en desarrollo y separa ESCO como investigación paralela no bloqueante.

- `DEC-20260717-1058-001-retirada-graphify-carrera-ai` retira Graphify de la operación de `carrera-ai` y sustituye la decisión local anterior de mantener tres corpus Graphify.

- `hosts/hosts.yaml` registra `carrera-ai` como host PCS.
- La carpeta `.pcs/` conserva la memoria operativa local; el estado actual vive en este documento y no en una sesión histórica.
- `docs/VERSIONADO_CARRERA_AI.md` gobierna la versión global y `docs/DOCUMENTO_SPEC_CARRERA_AI.md` conserva la autoridad sobre la definición del producto.
- `DEC-20260713-1344-001-integrar-graphify-tres-corpus` queda como decisión sustituida por la retirada de Graphify.
- `PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA` sigue gobernando la profundidad.
- Cobertura y profundidad son capas complementarias; la cobertura no sustituye el playbook de profundidad.
- La recomendación de doble pasada es un resultado debatible de evaluación, no una decisión formal ni un playbook adoptado.
- ESCO solo puede entrar más adelante como correspondencia candidata, explicable y revisable.
- No hay decisión vigente sobre el uso transversal de Obsidian; `docs/PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.md` es una propuesta para debate.

## Bloqueos o riesgos

- La recomendación todavía no ha sido aceptada como orientación operativa; convertirla en norma antes del debate sería prematuro.
- Una implementación rígida de las dos pasadas podría volver lineal o evaluativa una conversación que debe admitir saltos, retornos, omisiones y correcciones.
- Un perfil persuasivo con evidencia insuficiente puede inflar capacidades u ocultar incertidumbre; la persona debe poder revisar, matizar, rechazar o retirar información.
- ESCO no debe confundirse con prueba de competencia, cualificación o certificación individual.
- La información de trayectoria profesional es personal y debe limitarse a lo necesario para el propósito de carrera.
- Mover o eliminar directorios de configuración de Obsidian o de Vault Operator antes de una decisión aprobada podría afectar la recuperación de configuraciones, automatizaciones o referencias locales.
- `.tmp/` queda excluida del uso operativo salvo autorización expresa.

## Referencias históricas y de continuidad

- `docs/superpowers/specs/2026-07-17-versionado-carrera-ai-design.md`: diseño funcional aprobado.
- `sesion-20260717-1642-materializacion-versionado-carrera-ai.md`: sesión técnica cerrada de implementación y validación.
- `sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai.md`: sesión funcional activa de Carrera AI 2.0.
- `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`: sesión abierta que registra el núcleo metodológico, las fases del perfil y la exploración posterior de enfoques.
- `sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md`: línea paralela para investigar correspondencias ESCO candidatas sin bloquear la Fase 1.
- `docs/Ideas debate - como afrontar entrevista cobertura profesional/01_Conservadora_linea_de_vida_flexible_y_reconstruible.md`.
- `docs/Ideas debate - como afrontar entrevista cobertura profesional/02_Conservadora_doble_pasada_panorama_e_inmersion_selectiva.md`.
- `docs/Ideas debate - como afrontar entrevista cobertura profesional/03_Innovadora_atlas_conversacional_de_episodios_transiciones_y_capacidades.md`.
- `docs/Ideas debate - como afrontar entrevista cobertura profesional/04_Innovadora_dossier_de_hipotesis_contrastables_y_evidencia_progresiva.md`.
- `docs/Ideas debate - como afrontar entrevista cobertura profesional/05_Evaluacion_experta_y_recomendacion_de_enfoque.md`.
- `docs/Ideas debate - como afrontar entrevista cobertura profesional/06_Presentacion_propuesta_recomendada.html`.
- `sesion-20260717-1930-debate-obsidian-proyecto-completo.md`: sesión abierta para debatir el uso transversal de Obsidian en el repositorio.
- `docs/PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.md`: alternativas, recomendación debatible y plan reversible para el uso transversal de Obsidian.
- `docs/PRESENTACION_PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.pptx`: presentación de apoyo para el debate.
- `DEC-20260710-2308-001-separar-corpus-graphify`: decisión histórica sustituida por la decisión vigente de los tres corpus.
- `DEC-20260713-1344-001-integrar-graphify-tres-corpus`: decisión histórica sustituida sobre los tres corpus y la actualización local con Ollama.
- `sesion-20260713-1344-integracion-operacion-graphify-carrera-ai.md`: sesión cerrada de integración y operación de Graphify.
- `sesion-20260713-1525-publicacion-github-carrera-ai.md`: sesión cerrada de alta del proyecto en GitHub bajo la cuenta personal conectada.
- `sesion-20260717-1058-retirada-graphify-carrera-ai.md`: sesión cerrada de decisión, retirada física y verificación de Graphify.
- `run-graphify.bat`, `.pcs/.graphifyignore`, `docs/.graphifyignore` y los tres directorios `graphify-out/`: artefactos eliminados el 2026-07-17.
- `AGENTS.md`, `.pcs/AGENTS.md`, `docs/AGENTS.md` y `.gitignore`: instrucciones limpiadas el 2026-07-17 para retirar el uso operativo de Graphify.
