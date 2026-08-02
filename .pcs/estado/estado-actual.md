---
id: estado-actual
titulo: carrera-profesional-ai-first
estado: vigente
fecha_actualizacion: 2026-08-01
ultima_sesion_relacionada: sesion-20260801-2040-job-up
host: carrera-ai
---

# estado-actual

## Situación actual

Carrera AI 2.0 está en desarrollo sobre la versión base 1.6. Su objetivo es validar con una persona el recorrido cobertura profesional → inmersión en profundidad → evidencias → síntesis de trayectoria → Perfil Profesional Accionable integral y revisable.

La fuente funcional de verdad sobre la versión global es `docs/VERSIONADO_CARRERA_AI.md`. El SPEC conserva la definición del producto, mientras PCS registra la continuidad operativa y la decisión humana que adoptó el modelo de versionado.

ESCO permanece como investigación paralela fuera del criterio de finalización de 2.0 y como candidata provisional a una posible 2.5, que no está abierta.

La orientación local de `carrera-ai` ha completado su migración a PCS 2.0. `README.md` y `AGENTS.md` aplican el paquete documental vigente, las reglas PCS 1.0 se han retirado de la capa `.codex/` activa y se conservan las skills operativas de Job-up junto con la skill local `pcs-obsidian-corrige-links`. El registro central está cerrado en `pcs_version: "2.0"` y `status: vigente`. La segunda pasada se clasificó como C y confirmó la idempotencia del flujo sin nuevas escrituras en el host.

Se ha formalizado y materializado la retirada de Graphify de `carrera-ai` mediante `DEC-20260717-1058-001-retirada-graphify-carrera-ai`, siguiendo la decisión de referencia de PCS Core `DEC-20260715-0004-retirada-graphify-pcs-host`. La decisión local sustituye a `DEC-20260713-1344-001-integrar-graphify-tres-corpus`. La sesión de trabajo `sesion-20260717-1058-retirada-graphify-carrera-ai` registra la eliminación y quedó cerrada el 2026-07-17 tras completar la verificación.

La razón operativa es que el coste de tiempo y recursos de la extracción semántica resulta desproporcionado para el ritmo documental del host y que las salidas dependen de modelos que no siempre generan estructuras válidas. La localización y verificación de relaciones documentales se realiza directamente sobre las fuentes Markdown y sus enlaces. Se han eliminado los tres directorios de salida, el script de ejecución, las configuraciones específicas y las instrucciones operativas asociadas.

El trabajo vigente del host permanece en la revisión metodológica de la entrevista de cobertura profesional. `docs/DOCUMENTO_SPEC_CARRERA_AI.md` sigue definiendo el producto y se ha alineado de forma acotada con Carrera AI 2.0. El núcleo metodológico y el Perfil Profesional Accionable continúan siendo el marco para diseñar la cobertura de trayectorias profesionales sin sustituir el playbook de profundidad existente.

Por [[DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo]], Carrera AI incorpora una rama operativa de búsqueda de empleo dentro del mismo host, denominada **Job-up**. Su finalidad es preparar con rapidez CV adaptados, cartas de presentación y candidaturas revisables a partir de información profesional factual. Esta rama no modifica el SPEC, los playbooks ni la investigación metodológica de entrevista; ambas líneas siguen separadas.

Job-up mantiene actualmente diecisiete candidaturas registradas: tres rechazadas (`CAND-2026-001`, `CAND-2026-002` y `CAND-2026-009`), once enviadas (`CAND-2026-003`, `CAND-2026-004`, `CAND-2026-005`, `CAND-2026-007`, `CAND-2026-008`, `CAND-2026-010`, `CAND-2026-012`, `CAND-2026-014`, `CAND-2026-015`, `CAND-2026-016` y `CAND-2026-017`), una presentación espontánea pendiente de aprobación (`CAND-2026-006`) y dos detenidas por cierre o indisponibilidad de oferta (`CAND-2026-011` y `CAND-2026-013`). CAND-2026-012 fue presentada a Grupo Miguel León mediante Indeed y su web oficial el 2026-07-29. CAND-2026-014 fue presentada correctamente en el portal de ALDI el 2026-07-29. CAND-2026-015 se registró como enviada porque InfoJobs mostraba «Inscrito», sin generar documentación Job-up. CAND-2026-016 fue presentada por LinkedIn, la web de Grupo Run Run y un mensaje directo; CAND-2026-017 fue presentada en la web oficial de Lidl. CAND-2026-018 se eliminó íntegramente por instrucción expresa y no forma parte del seguimiento. CAND-2026-002 se actualizó a rechazada porque InfoJobs mostraba «Descartado». CAND-2026-011 permanece detenida porque la empresa comunicó el cierre de la oferta aunque Indeed aún la mostraba abierta; CAND-2026-013 permanece detenida porque la oferta ya no estaba disponible en la web de ALDI. Los estados detallados y los documentos asociados viven en `boveda-entrevista-profesional/busqueda-empleo/seguimiento/seguimiento-candidaturas.md` y en las carpetas de cada candidatura.

La continuidad de Job-up se mantendrá en este estado, en las acciones y decisiones vigentes y en sus documentos operativos. Se ha adoptado que las sesiones PCS no permanezcan abiertas indefinidamente para representar una línea de trabajo de larga duración: cada bloque concreto de trabajo tendrá una sesión delimitada, que se consolidará o cerrará al dejar de estar en edición. Esta convención queda formalizada en [[DEC-20260724-1956-001-delimitar-sesiones-job-up]].

La reorganización documental y la consolidación operativa reciente de Job-up se
implantaron en `main`; la reorganización quedó integrada mediante el commit
`55aaeb5` y el bloque posterior de candidaturas, plantillas y skills quedó
consolidado en `0366611`. El README de
`boveda-entrevista-profesional/busqueda-empleo/` es la referencia funcional
única; las fuentes, plantillas y seguimiento viven en sus áreas funcionales;
`INICIO_SESION_WORK.md` quedó en `historico/`; y el playbook vigente usa nombre
estable con versión YAML. Las tres skills de Job-up están renombradas y la
skill `job-up-candidatura-oferta` acepta URL, fichero Markdown o texto pegado.

La sesión [[sesion-20260724-2004-candidaturas-job-up]] quedó consolidada y cerrada el 2026-07-27. La sesión [[sesion-20260727-2109-busqueda-empleo]] quedó cerrada el 2026-07-28 tras finalizar el bloque delimitado de búsqueda de empleo del 2026-07-27. La continuidad de Job-up se mantiene en el estado operativo, en sus documentos operativos y, para cada nuevo bloque de trabajo, en una sesión PCS delimitada.

El flujo de adaptación por oferta ya incorpora análisis de nivel y sobrecualificación, palabras clave, requisitos no acreditados, guion narrativo, control de arrastre entre candidaturas, validación documental de CV de hasta dos páginas y carta de una página, y un veredicto final previo a la aprobación humana. Si un documento supera su límite, el flujo conserva los artefactos, informa de la ruta y espera una decisión humana explícita antes de continuar. Las rutas de entrada con `\\` se normalizan al ejecutar, mientras que los datos persistidos mantienen `/` como formato canónico. La ficha `candidatura.md` debe inventariar todos los documentos operativos de su carpeta —incluidos CV en DOCX, PDF y LaTeX— y actualizarse al crear, añadir, sustituir o eliminar un artefacto. Los CV y cartas se generan desde templates comunes, con fotografía por defecto, preservación del formato del template, contenido justificado y sin arrastre de pies de página de plantilla. La conversión DOCX→PDF usa `soffice.com` directo con perfil aislado y no debe reintentarse ni abrir una segunda instancia si aparece el error de `bootstrap.ini`; la validación estructural usa OOXML y la revisión visual solo se declara cuando se ejecuta efectivamente.

Job-up incorpora además un veredicto final del CV que evalúa primero la integridad factual y de privacidad y, solo después, cinco criterios de calidad de 1 a 5: primer escaneo, encaje competitivo, cobertura ATS respaldada, fuerza de la experiencia y adecuación narrativa. La decisión resultante no sustituye la aprobación humana. CAND-2026-004 es la primera aplicación, con integridad `apta`, media 4,0 y resultado `revisar_antes_de_aprobar`. La investigación contextual de empresa o sector es opcional y posterior al veredicto; requiere autorización de la persona responsable y mostrar previamente las URL propuestas. Si esa investigación justifica un ajuste de lenguaje corporativo, debe aplicarse de forma coherente al CV y a la carta de presentación. En CAND-2026-004 se investigó la fuente oficial de Globaenergy y se incorporó, con autorización expresa, ese ajuste de tono en ambos documentos sin añadir experiencia no acreditada.

En paralelo, la investigación GitHub dispone ya de estructura, flujo obligatorio,
templates de fichas y comparativas. La calibración inicial se completó con la
ficha de `noamseg/interview-coach-skill` y la primera selección ya cuenta con
ocho fichas técnicas. Sus decisiones son preliminares y se mantienen dentro del
flujo documental; no se ha autorizado instalación, ejecución ni integración de
repositorios, ni se ha creado una acción o decisión PCS derivada.

Se han elaborado cuatro propuestas para que una IA cubra toda la vida profesional de una persona, dos conservadoras y dos innovadoras. El informe `docs/trabajo-en-curso/debates/05_Evaluacion_experta_y_recomendacion_de_enfoque.md` las compara con una rúbrica equilibrada y recomienda, de forma debatible, usar la Idea 2, doble pasada de panorama e inmersión selectiva, como arquitectura base de un primer piloto.

La recomendación requiere complementar esa arquitectura con la conversación no lineal, las anclas y los retornos opcionales de la Idea 1, y con un registro ligero de hipótesis, evidencia, límites y corrección por la persona de la Idea 4. El atlas relacional de la Idea 3 queda como posible evolución posterior, no como requisito del MVP. ESCO mantiene el papel de correspondencia candidata posterior, trazable y revisable; no prueba competencias individuales ni certifica a la persona.

También existe una presentación HTML autónoma para explicar la propuesta a personas no expertas: `docs/ideas-y-debates/cobertura-profesional/06_Presentacion_propuesta_recomendada.html`. Resume el problema, la doble pasada, sus garantías y el piloto propuesto.

Se ha adoptado e implantado la reorganización documental y una nueva bóveda Obsidian en la raíz mediante [DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian](../decisiones/DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian.md), a partir del [diseño aprobado](../../docs/superpowers/specs/2026-07-18-reorganizacion-documental-obsidian-design.md) y de la sesión de debate. La [acción de implantación](../acciones/ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian.md) está completada: se verificó la copia externa, se retiraron las configuraciones heredadas, se inicializó manualmente la bóveda raíz, se migraron los bloques aprobados a `docs/` e `historico/` y la persona responsable validó la navegación final en Obsidian.

Históricamente, la documentación de Graphify se mantuvo separada en tres corpus documentales: `.pcs/`, `docs/` y `boveda-entrevista-profesional/`. Esa organización quedó formalizada en `DEC-20260713-1344-001-integrar-graphify-tres-corpus`, ahora sustituida por la decisión de retirada. La decisión histórica afectaba únicamente a la indexación y recuperación de contexto; no adoptaba un playbook, no modificaba el SPEC ni convertía los artefactos del grafo en fuentes normativas.

Se ha cerrado `sesion-20260713-1344-integracion-operacion-graphify-carrera-ai.md` tras dejar trazada la línea histórica de integración, sus límites y la revisión futura de utilidad. Sus conclusiones quedan superadas operativamente por la retirada de Graphify. El estado actual, las decisiones vigentes y las fuentes documentales conservan su autoridad.

También se creó el repositorio GitHub `gusvegabol/carrera-profesional-ai-first` y quedó cerrada la sesión operativa asociada a su incorporación. El trabajo local puede sincronizarse ya con ese remoto bajo la cuenta personal conectada.

La utilidad de esa separación y de Graphify queda superada por la decisión de retirada. Una necesidad futura de análisis semántico solo podrá reabrirse mediante una decisión concreta y aprobada. La recomendación metodológica de doble pasada sigue siendo debatible y no ha sido adoptada como playbook.

## Foco operativo

Mantener dos líneas separadas: evaluar si la arquitectura recomendada de doble pasada debe orientar el primer piloto de cobertura profesional, y operar Job-up para valorar ofertas y producir candidaturas revisables cuando la persona responsable lo autorice. En Job-up, continuar valorando ofertas concretas y refinando la redacción de la experiencia profesional para que sea más concreta y orientada al puesto, sin perder trazabilidad factual. Toda nueva candidatura documental debe incluir CV en DOCX, PDF y LaTeX, además de carta en DOCX y PDF, salvo que el flujo determine que solo procede registrar un estado externo. La sesión `sesion-20260730-1345-job-up` quedó cerrada al iniciar el nuevo bloque, la sesión `sesion-20260730-2038-job-up` quedó cerrada el 2026-07-31 y la sesión `sesion-20260731-1118-job-up` quedó cerrada tras actualizar y verificar el flujo documental. La reorganización documental, la limpieza de temporales y la bóveda raíz de Obsidian ya están consolidadas.

El nuevo flujo de creación documental para candidaturas por oferta está implementado y verificado técnicamente. Queda pendiente realizar una prueba real completa con una candidatura de oferta: generar los cinco artefactos, revisar visualmente el resultado y confirmar su aprobación humana. Este debe ser el primer trabajo de Job-up al iniciar una nueva sesión de Work.

La sesión [[sesion-20260801-2040-job-up]] quedó cerrada el 2026-08-02 tras consolidar el bloque delimitado de mejora arquitectónica de Job-up. Durante el bloque se generó la SPEC de arquitectura modular v0.2.0, que sustituye a la 0.1.0. La SPEC está en `borrador_operativo`, no sustituye el estado PCS ni las decisiones formales, y fija como siguiente maduración la validación de `candidatura.md` y el diseño posterior de `PLAYBOOK_GUION_ADAPTACION_CV`; `datos-generacion.json` y la skill directora final quedan deliberadamente pospuestos.

Según la SPEC v0.2.0, `candidatura.md` se encuentra en `en_prueba`: antes de validarla deben comprobarse responsabilidad, trazabilidad, separación de estados, economía documental, inventario de artefactos y ausencia de defectos estructurales; después debe decidirse si CAND-2026-019 basta o si hace falta un segundo caso por variedad. Los defectos deberán clasificarse como caso, playbook, template, datos core, arquitectura o composición para extraer mejoras generalizables.

Se ha abierto además la sesión `sesion-20260721-1644-perfiles-sinteticos-para-evaluar-entrevistas` para debatir un posible banco de perfiles sintéticos que acelere la prueba de los playbooks. Es una línea abierta de investigación metodológica: no autoriza simulaciones, cambios de playbook ni sustituye la validación con personas reales.

La sesión [[sesion-20260721-1651-tension-carrera-ai-y-busqueda-de-trabajo]] deliberó la tensión entre el desarrollo metodológico de Carrera AI y la prioridad personal de búsqueda de empleo. Su resultado vigente es no pausar ni bifurcar el host, sino establecer una rama operativa interna y separada para búsqueda de empleo. [[ACC-20260721-1651-001-activar-rama-operativa-busqueda-empleo-fase-1]] quedó completada con una candidatura real preparada y validada; las fases posteriores de asistencia en Chrome o acceso mediante conectores requieren su propio diseño y validación antes de ejecutarse.

## Aprendizajes de la primera prueba real de cobertura profesional

La primera prueba real del 2026-07-20 mostró que la arquitectura puede ampliar el mapa profesional sin imponer una cronología, permitir que la persona elija dónde profundizar y producir una competencia con evidencia concreta y validación explícita. También mantuvo visibles las zonas pendientes y los límites de lo explorado.

La evaluación detectó que, antes de repetir la prueba, debe conservarse la transcripción verbatim desde el inicio, aplicarse la ruta canónica de templates antes de generar artefactos, utilizarse el template específico de evaluación, aclararse mejor qué detalles se buscan y qué significa el valor profesional, y reservarse un cierre explícito para revisar la utilidad del mapa.

La evaluación consolidada está en [[artefactos-cobertura-profesional/evaluaciones/EVALUACION_PILOTO_ENT-001-M01_2026-07-20]]. La conclusión experimental es `Modificar`: la arquitectura muestra valor, pero requiere esas correcciones antes de repetirse. No constituye adopción formal de la doble pasada como metodología.

El segundo caso real, `ENT-002-M01`, se ejecutó el 2026-07-21 después de aplicar esas correcciones: conservó transcripción verbatim desde la apertura, empleó los templates canónicos de entrevistado, mapa, sesión, inmersión, competencia y evaluación, y mantuvo una separación explícita entre hechos, formulación y límites. La persona participante, bajo el alias `Carmen`, validó el resumen, autorizó la conservación sin límite temporal de la muestra y aprobó excluir datos identificables innecesarios. La evaluación `EVALUACION_PILOTO_ENT-002-M01_2026-07-21` concluye experimentalmente `Continuar`: el mapa parcial fue útil y reconocido por la persona, pero el resultado no certifica competencias ni adopta formalmente la doble pasada.

## Próximos pasos

- Para iniciar cada nuevo caso real de cobertura profesional, el responsable debe confirmar de forma explícita: autorización experimental, persona participante, alcance, conservación de datos, identificador y forma de revisión de la salida. Los casos `ENT-001` y `ENT-002` ya cuentan con esas decisiones para su propio alcance.
- Aplicar `docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md` en cualquier futura transición de versión.
- Revisar la evaluación experta y la presentación con las personas que deban debatir el enfoque.
- Completar la matriz comparativa de la investigación GitHub a partir de las ocho fichas, usando el flujo obligatorio y la calibración de `noamseg/interview-coach-skill`.
- Formular la recomendación de componentes y experimentos antes de ejecutar cualquier prueba.
- Delimitar `EXP-001-entrevista-y-storybank` antes de ejecutarlo y mantenerlo separado de cualquier integración de código.
- Decidir explícitamente si se adopta, modifica o descarta la recomendación para el primer piloto.
- Si se adopta, definir el contrato del piloto: muestra de entrevistas, salida inicial revisable, control de privacidad, criterios de corrección y señales de utilidad.
- Conservar y reutilizar el flujo validado de adaptación por oferta para futuras candidaturas, manteniendo el índice documental completo, la cabecera de CV con espacio para fotografía y la aprobación humana antes de cualquier envío.
- Realizar como siguiente trabajo de Job-up una prueba real del nuevo flujo de creación documental con una candidatura de oferta, incluyendo la revisión visual y la aprobación humana de los artefactos generados.
- Leer la SPEC v0.2.0 al iniciar el próximo bloque de Job-up; revisar y probar `candidatura.md`, confirmar su cierre o ajustes necesarios y, solo después, diseñar y probar `PLAYBOOK_GUION_ADAPTACION_CV`.
- Evaluar por separado si Vault Operator o Local REST API MCP aportan valor a la bóveda ya consolidada, sin reinstalar configuraciones heredadas.
- Mantener separadas la cobertura, la profundidad y la correspondencia ESCO mientras no exista una decisión posterior que cambie ese alcance.
- No tratar la evaluación como validación con personas ni actualizar el SPEC o el playbook de profundidad por inferencia.

## Acciones abiertas relevantes

- La preparación documental del piloto real está completada en `docs/superpowers/specs/2026-07-19-preparacion-piloto-cobertura-profesional-design.md`, `docs/trabajo-en-curso/diseno/CHECKLIST_PREPILOTO_COBERTURA_PROFESIONAL.md` y `docs/trabajo-en-curso/diseno/MATRIZ_EVALUACION_PILOTO_COBERTURA_PROFESIONAL.md`. Se han ejecutado los casos `ENT-001` y `ENT-002`; cada caso nuevo sigue condicionado a sus propias decisiones explícitas de autorización, alcance, conservación, identificador y revisión.
- `ACC-20260717-1642-001-materializar-versionado-carrera-ai` quedó completada; no deja trabajo abierto dentro de su alcance.
- No queda trabajo abierto para materializar la retirada de Graphify; la eliminación y las comprobaciones permanecen registradas históricamente en `sesion-20260717-1058-retirada-graphify-carrera-ai`.
- Es candidata a acción futura la definición del primer piloto, condicionada a una decisión explícita sobre la recomendación metodológica.
- [[ACC-20260721-1651-001-activar-rama-operativa-busqueda-empleo-fase-1]] está completada. Las fases de asistencia en Chrome y conectores de portales no son acciones autorizadas todavía.
- La prueba real del nuevo flujo de creación documental para una candidatura de oferta sigue pendiente y debe abordarse al iniciar la próxima sesión de Work de Job-up.
- CAND-2026-003, CAND-2026-004 y CAND-2026-005 fueron enviadas mediante InfoJobs y quedan pendientes de respuesta; CAND-2026-002 figura como rechazada/descartada.
- CAND-2026-006 está preparada como presentación espontánea a Randstad y queda pendiente de revisión y aprobación humana antes de compartirla.
- CAND-2026-012 y CAND-2026-014 fueron enviadas y quedan pendientes de respuesta; CAND-2026-015 solo conserva el registro de inscripción externa de InfoJobs.
- `ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian` quedó completada el 2026-07-18. La evaluación de plugins adicionales es una iniciativa independiente.

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
- La investigación GitHub es una línea técnica paralela; sus fichas y decisiones preliminares no modifican por sí solas el SPEC, los playbooks ni el alcance de Carrera AI 2.0.
- ESCO solo puede entrar más adelante como correspondencia candidata, explicable y revisable.
- `DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian` adopta la bóveda raíz limpia y la migración por bloques validados. Las aprobaciones de clasificación de cada bloque continúan siendo decisiones posteriores e independientes.
- [[DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo]] crea la rama operativa de búsqueda de empleo dentro de Carrera AI y preserva la separación respecto de la investigación metodológica de entrevista.
- [[DEC-20260724-1956-001-delimitar-sesiones-job-up]] mantiene Job-up como línea operativa de largo recorrido y establece sesiones PCS delimitadas para cada bloque concreto de trabajo.

## Bloqueos o riesgos

- La recomendación todavía no ha sido aceptada como orientación operativa; convertirla en norma antes del debate sería prematuro.
- Una implementación rígida de las dos pasadas podría volver lineal o evaluativa una conversación que debe admitir saltos, retornos, omisiones y correcciones.
- Un perfil persuasivo con evidencia insuficiente puede inflar capacidades u ocultar incertidumbre; la persona debe poder revisar, matizar, rechazar o retirar información.
- ESCO no debe confundirse con prueba de competencia, cualificación o certificación individual.
- La información de trayectoria profesional es personal y debe limitarse a lo necesario para el propósito de carrera.
- Cualquier instalación futura de plugins debe ser limpia, reversible y evaluarse fuera de la acción de reorganización ya completada.
- La investigación GitHub puede desviar la MVP hacia un sistema de coaching de entrevistas, una arquitectura multiagente o herramientas de CV si no se mantienen los límites del flujo.
- La rama de búsqueda de empleo puede invadir el alcance metodológico de entrevista o automatizar candidaturas con controles insuficientes si no mantiene su frontera y la aprobación humana por lote.
- La calidad narrativa de la experiencia profesional sigue siendo un punto de mejora: las estructuras ya verificadas son utilizables, pero algunas descripciones pueden ganar concreción y naturalidad en futuras iteraciones.
- `.tmp/` queda excluida del uso operativo salvo autorización expresa.

## Referencias históricas y de continuidad

- `docs/superpowers/specs/2026-07-17-versionado-carrera-ai-design.md`: diseño funcional aprobado.
- `sesion-20260717-1642-materializacion-versionado-carrera-ai.md`: sesión técnica cerrada de implementación y validación.
- `sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai.md`: sesión funcional activa de Carrera AI 2.0.
- `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`: sesión abierta que registra el núcleo metodológico, las fases del perfil y la exploración posterior de enfoques.
- `sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md`: línea paralela para investigar correspondencias ESCO candidatas sin bloquear la Fase 1.
- `docs/trabajo-en-curso/debates/01_Conservadora_linea_de_vida_flexible_y_reconstruible.md`.
- `docs/trabajo-en-curso/debates/02_Conservadora_doble_pasada_panorama_e_inmersion_selectiva.md`.
- `docs/trabajo-en-curso/debates/03_Innovadora_atlas_conversacional_de_episodios_transiciones_y_capacidades.md`.
- `docs/trabajo-en-curso/debates/04_Innovadora_dossier_de_hipotesis_contrastables_y_evidencia_progresiva.md`.
- `docs/trabajo-en-curso/debates/05_Evaluacion_experta_y_recomendacion_de_enfoque.md`.
- `docs/ideas-y-debates/cobertura-profesional/06_Presentacion_propuesta_recomendada.html`.
- `docs/ideas-y-debates/investigacion-github/FLUJO_INVESTIGACION_GITHUB.md`: flujo obligatorio de la investigación técnica.
- `docs/ideas-y-debates/investigacion-github/fichas/`: ocho fichas técnicas de la primera selección, incluida `noamseg-interview-coach-skill.md` como calibración.
- `docs/ideas-y-debates/investigacion-github/comparativas/MATRIZ_COMPARATIVA_REPOSITORIOS.md` y `docs/ideas-y-debates/investigacion-github/comparativas/RECOMENDACION_COMPONENTES_Y_EXPERIMENTOS.md`: estructuras comparativas y de recomendación.
- `sesion-20260717-1930-debate-obsidian-proyecto-completo.md`: sesión cerrada de debate, decisión e implantación del uso transversal de Obsidian en el repositorio.
- `historico/docs/PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.md`: alternativas, recomendación debatible y plan reversible para el uso transversal de Obsidian.
- `docs/PRESENTACION_PROPUESTA_USO_TRANSVERSAL_OBSIDIAN_v1_0_0.pptx`: presentación de apoyo para el debate.
- `DEC-20260718-1700-001-adoptar-reorganizacion-documental-obsidian.md`: decisión vigente de implantar la reorganización documental y la nueva bóveda raíz.
- `ACC-20260718-1700-001-implantar-reorganizacion-documental-obsidian.md`: acción completada de inventario, copia externa, configuración limpia y migración por bloques aprobados.
- `DEC-20260710-2308-001-separar-corpus-graphify`: decisión histórica sustituida por la decisión vigente de los tres corpus.
- `DEC-20260713-1344-001-integrar-graphify-tres-corpus`: decisión histórica sustituida sobre los tres corpus y la actualización local con Ollama.
- `sesion-20260713-1344-integracion-operacion-graphify-carrera-ai.md`: sesión cerrada de integración y operación de Graphify.
- `sesion-20260713-1525-publicacion-github-carrera-ai.md`: sesión cerrada de alta del proyecto en GitHub bajo la cuenta personal conectada.
- `sesion-20260717-1058-retirada-graphify-carrera-ai.md`: sesión cerrada de decisión, retirada física y verificación de Graphify.
- [[sesion-20260721-1651-tension-carrera-ai-y-busqueda-de-trabajo]]: sesión de origen de la rama operativa de búsqueda de empleo.
- [[DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo]]: decisión vigente de mantener la rama operativa dentro del host y separada de la investigación de entrevista.
- [[ACC-20260721-1651-001-activar-rama-operativa-busqueda-empleo-fase-1]]: acción completada que validó el flujo inicial de CV y cartas adaptados.
- `docs/ideas-y-debates/mejoras-job-up/SPEC-Arquitectura-modular-generación-candidatura-v0-2-0.md`: SPEC operativa de arquitectura modular, en borrador, para la continuidad de Job-up.
- `run-graphify.bat`, `.pcs/.graphifyignore`, `docs/.graphifyignore` y los tres directorios `graphify-out/`: artefactos eliminados el 2026-07-17.
- `AGENTS.md`, `.pcs/AGENTS.md`, `docs/AGENTS.md` y `.gitignore`: instrucciones limpiadas el 2026-07-17 para retirar el uso operativo de Graphify.
