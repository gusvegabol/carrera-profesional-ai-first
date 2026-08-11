---
id: estado-actual
titulo: carrera-profesional-ai-first
estado: vigente
fecha_actualizacion: 2026-08-11
ultima_sesion_relacionada: sesion-20260805-1757-job-up
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

Job-up mantiene actualmente veinte expedientes de candidatura registrados. Los estados detallados y los documentos asociados viven en `boveda-entrevista-profesional/busqueda-empleo/seguimiento/seguimiento-candidaturas.md` y en las carpetas de cada candidatura. CAND-2026-012 fue presentada a Grupo Miguel León mediante Indeed y su web oficial el 2026-07-29. CAND-2026-014 fue presentada correctamente en el portal de ALDI el 2026-07-29. CAND-2026-015 se registró como enviada porque InfoJobs mostraba «Inscrito», sin generar documentación Job-up. CAND-2026-016 fue presentada por LinkedIn, la web de Grupo Run Run y un mensaje directo; CAND-2026-017 fue presentada en la web oficial de Lidl. CAND-2026-018 se eliminó íntegramente por instrucción expresa y no forma parte del seguimiento. CAND-2026-002 se actualizó a rechazada porque InfoJobs mostraba «Descartado». CAND-2026-011 permanece detenida porque la empresa comunicó el cierre de la oferta aunque Indeed aún la mostraba abierta; CAND-2026-013 permanece detenida porque la oferta ya no estaba disponible en la web de ALDI. CAND-2026-022 quedó detenida y no recomendada por falta de experiencia en administración de fincas y por inglés básico frente al requisito avanzado.

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

Mantener dos líneas separadas: evaluar si la arquitectura recomendada de doble pasada debe orientar el primer piloto de cobertura profesional, y operar Job-up para valorar ofertas y producir candidaturas revisables cuando la persona responsable lo autorice. En Job-up, continuar valorando ofertas concretas y refinando la redacción de la experiencia profesional para que sea más concreta y orientada al puesto, sin perder trazabilidad factual. El flujo modular CV-only produce CV en DOCX, PDF y LaTeX; la carta tiene ahora su módulo independiente probado, aunque la generación final sigue separada y requiere revisión humana. La sesión `sesion-20260730-1345-job-up` quedó cerrada al iniciar el nuevo bloque, la sesión `sesion-20260730-2038-job-up` quedó cerrada el 2026-07-31 y la sesión `sesion-20260731-1118-job-up` quedó cerrada tras actualizar y verificar el flujo documental. La reorganización documental, la limpieza de temporales y la bóveda raíz de Obsidian ya están consolidadas.

Job-up incorpora como línea prioritaria de evolución una futura **UI de configuración de candidatura**, pendiente de diseño y todavía sin implementación. Su objetivo es hacer descubribles las opciones configurables —por ejemplo, carta, fotografía, URL/contexto corporativo y aplicación de cultura al CV o a la carta— para que la persona usuaria no tenga que conocer ni recordar su catálogo. La hipótesis inicial es una experiencia guiada y adaptativa que persista las decisiones en una configuración estructurada consumible por la orquestación; la UI será la interfaz humana y el YAML/configuración será el contrato operativo, no su sustituto. Esta línea no modifica ni invalida el flujo modular actual.

El flujo modular CV-only de creación documental está implementado y verificado técnicamente. La prueba real se ejecutó con CAND-2026-020 y CAND-2026-019: cada caso produjo `cv.docx`, `cv.pdf` y `cv.tex`, con fotografía por defecto, textos completos y una página. La autorización de datos privados quedó registrada por candidatura: nombre, apellido 1, email y teléfono incluidos; apellido 2, LinkedIn y ubicación omitidos. También está implantado el control posterior `revision-humana-cv.md` → `PLAYBOOK_VEREDICTO_FINAL_CV` → `GATE-VEREDICTO-CV`, con huella SHA-256 e invalidación por regeneración. Las revisiones humanas de ambos PDF se registraron el 2026-08-08 y los veredictos quedaron completados. El 2026-08-09, CAND-2026-020 obtuvo el gate CV `aprobado`; tras completar su carta, su estado vigente es `documentalmente_completa` y `presentada: false`. CAND-2026-019 mantiene el gate CV `bloqueado` y permanece detenida. Ninguna se ha enviado.

La sesión [[sesion-20260801-2040-job-up]] quedó cerrada el 2026-08-02 tras consolidar el bloque delimitado de mejora arquitectónica de Job-up. Durante el bloque se generó la SPEC de arquitectura modular v0.2.0, que sustituye a la 0.1.0. La SPEC está en `borrador_operativo`, no sustituye el estado PCS ni las decisiones formales, y fija como siguiente maduración la validación de `candidatura.md` y el diseño posterior de `PLAYBOOK_GUION_ADAPTACION_CV`; `datos-generacion.json` y la skill directora final quedan deliberadamente pospuestos.

La sesión [[sesion-20260805-1757-job-up]] está abierta como bloque delimitado de Job-up y se relaciona con [[sesion-20260801-2040-job-up]]. Durante ella se implementó el diseño vigente v0.3.4 de `PLAYBOOK_GUION_ADAPTACION_CV`, el contrato de contenido 1.2, el compositor CV-only y el nuevo veredicto final CV: SPEC sincronizada, playbooks y templates creados, guiones y evaluaciones completados para `CAND-2026-020` y `CAND-2026-019`, y ambos CV generados y verificados técnicamente. Tras la regeneración de los guiones 1.0.1 con plantilla 2.1, la persona responsable aprobó ambos `GATE-GUION-CV-CONTENIDO` el 2026-08-07. Los dos `GATE-CONTENIDO-CV-COMPOSICION` fueron aprobados el 2026-08-07 y la ejecución productiva posterior generó exclusivamente los tres artefactos CV. La autorización de datos privados se resolvió el 2026-08-08 y los CV se regeneraron con los campos autorizados. Las revisiones humanas de ambos PDF se registraron el 2026-08-08 y los veredictos se completaron: Lidl `apto_para_presentacion` y ASIC `no_competitivo`. El 2026-08-09 el gate de Lidl fue aprobado y el de ASIC bloqueado. En `CAND-2026-019` se sincronizó la FP de Técnico Administrativo no finalizada y se archivó el guion mixto y el veredicto final históricos antes de regenerar el flujo CV-only. `DEF-ARQ-001` permanece abierto. La SPEC v0.4.0 continúa en `borrador_operativo`; `INC-004` queda resuelto en su vacío contractual, aunque la excepción sin fotografía sigue bloqueada. La implantación base está fusionada localmente en `main` (`f036c92`) y el registro posterior de tareas quedó confirmado en `dc7d91e`; la sincronización actual de SPEC, playbooks, paquete y verificador mantiene cambios locales pendientes de commit y no se ha hecho `push`. El 2026-08-09 se comprobó que Indeed redirige al portal de empleo de Lidl; el formulario no forma parte de la precondición del paquete y la presentación queda bajo responsabilidad de la persona responsable. Además, el portal de Lidl muestra 25.000–29.000 € frente a 18.800–21.000 € en Indeed; la discrepancia queda registrada con procedencia y no se normaliza.

El 2026-08-09 se probó el módulo independiente de carta de presentación con CAND-2026-020. `PLAYBOOK_GUION_CARTA_PRESENTACION` v1.0.0 y `TEMPLATE_GUION_CARTA_PRESENTACION.md` v1.0.0 quedaron marcados como probados; se generaron `guion-carta-presentacion.md` y su evaluación de `GATE-GUION-CARTA-CONTENIDO`. Tras la respuesta del usuario, el guion se regeneró completamente: no hay motivación ni relación previa con Lidl, y se incorporó la fuente oficial autorizada. El guion conserva la estrategia común, separa Lidl de Indeed y limita la relación con el CV a complementar su evidencia.

El contrato superó las pruebas T1–T9, incluido el caso sintético de empresa anónima y los controles de URL, motivación, afinidad cultural, keywords sin evidencia, segundo CV y genericidad. El contrato queda `apto_para_implantacion`. La persona responsable aprobó humanamente `GATE-GUION-CARTA-CONTENIDO` para CAND-2026-020 el 2026-08-09. Esa aprobación solo permite pasar al diseño de la futura fase de generación del contenido de la carta; la carta final, su revisión, su veredicto y la presentación siguen pendientes.

El 2026-08-09 la primera revisión humana del contenido de carta quedó `no_aprobado`/`requiere_correccion` por lenguaje defensivo visible. Después se implantó el contrato v1.1.0 del playbook y template, ambos en `en_prueba`, con los tres roles obligatorios y la segunda lectura recruiter. Se regeneró completamente `contenido-carta-presentacion.md` desde las fuentes canónicas: formulaciones positivas, sin nuevas evidencias ni cambios de alcance, motivación personal ausente, cultura solo contextual y privacidad conforme. La evaluación técnica de `GATE-CONTENIDO-CARTA-COMPOSICION` quedó `apto` y la persona responsable aprobó humanamente ese gate el 2026-08-10. La aprobación autorizó la composición posterior; la decisión anterior se conserva como antecedente. Se añadió el verificador determinista y las pruebas T19–T22, manteniendo las regresiones anteriores.

Se ha abierto además la sesión `sesion-20260721-1644-perfiles-sinteticos-para-evaluar-entrevistas` para debatir un posible banco de perfiles sintéticos que acelere la prueba de los playbooks. Es una línea abierta de investigación metodológica: no autoriza simulaciones, cambios de playbook ni sustituye la validación con personas reales.

Registro histórico de la etapa posterior a la recomposición y anterior a la nueva revisión humana (2026-08-10): la sesión PCS `sesion-20260805-1757-job-up` quedó sincronizada tras implantar el contrato v1.1.0 de generación de carta, regenerar CAND-2026-020 desde cero y verificar 124 pruebas. El contenido de carta era técnicamente `apto`, `GATE-CONTENIDO-CARTA-COMPOSICION` estaba aprobado humanamente y la composición produjo DOCX/PDF equivalentes, legibles y de una página. En ese momento, la aprobación anterior de `GATE-CARTA-REVISION-HUMANA` se conservaba como antecedente y el veredicto final de carta aún no estaba diseñado; ese estado quedó superado por la revisión humana posterior y la implantación del veredicto final.

Auditoría del 2026-08-10: la afirmación sobre negociación con proveedores durante los tres primeros años era factual, pero no estaba autorizada por ningún `A-NNN` del guion; además, HER-10 figuraba como evidencia factual sin una decisión editorial A-NNN que la cubriera. Se reforzaron playbook, template, verificador y pruebas T19–T22 con un conjunto cerrado de afirmaciones autorizadas. CAND-2026-020 se regeneró desde cero sin esas afirmaciones; el verificador devuelve autorización editorial y trazabilidad factual `aptas`. Las 124 pruebas del repositorio pasan. La persona responsable aprobó humanamente el gate de composición; la composición y los gates posteriores siguen fuera de alcance.

Registro histórico de composición de carta del 2026-08-10, anterior a la decisión humana posterior: se normalizaron a `en_prueba` `PLAYBOOK_COMPONER_CARTA_PRESENTACION.md` y `TEMPLATE_COMPOSICION_CARTA_PRESENTACION.md`; se creó `scripts/job-up/componer_carta_presentacion.py` con extracción cerrada, composición DOCX/PDF, comparación semántica, privacidad, orden, cifras y clasificación de incidencias. CAND-2026-020 produjo los dos documentos y `evaluacion-composicion-carta-presentacion.md`: fuente, DOCX y PDF eran equivalentes, el PDF tenía una página y la revisión visual no detectó defectos. La limitación de `pdf2image` quedó registrada como no bloqueante por haberse usado un renderizador alternativo. En esa etapa, la revisión aún no estaba registrada y el gate estaba `pendiente`; posteriormente la persona responsable revisó y aprobó la nueva representación.

La sesión [[sesion-20260721-1651-tension-carrera-ai-y-busqueda-de-trabajo]] deliberó la tensión entre el desarrollo metodológico de Carrera AI y la prioridad personal de búsqueda de empleo. Su resultado vigente es no pausar ni bifurcar el host, sino establecer una rama operativa interna y separada para búsqueda de empleo. [[ACC-20260721-1651-001-activar-rama-operativa-busqueda-empleo-fase-1]] quedó completada con una candidatura real preparada y validada; las fases posteriores de asistencia en Chrome o acceso mediante conectores requieren su propio diseño y validación antes de ejecutarse.

## Aprendizajes de la primera prueba real de cobertura profesional

La primera prueba real del 2026-07-20 mostró que la arquitectura puede ampliar el mapa profesional sin imponer una cronología, permitir que la persona elija dónde profundizar y producir una competencia con evidencia concreta y validación explícita. También mantuvo visibles las zonas pendientes y los límites de lo explorado.

La evaluación detectó que, antes de repetir la prueba, debe conservarse la transcripción verbatim desde el inicio, aplicarse la ruta canónica de templates antes de generar artefactos, utilizarse el template específico de evaluación, aclararse mejor qué detalles se buscan y qué significa el valor profesional, y reservarse un cierre explícito para revisar la utilidad del mapa.

La evaluación consolidada está en [[artefactos-cobertura-profesional/evaluaciones/EVALUACION_PILOTO_ENT-001-M01_2026-07-20]]. La conclusión experimental es `Modificar`: la arquitectura muestra valor, pero requiere esas correcciones antes de repetirse. No constituye adopción formal de la doble pasada como metodología.

El segundo caso real, `ENT-002-M01`, se ejecutó el 2026-07-21 después de aplicar esas correcciones: conservó transcripción verbatim desde la apertura, empleó los templates canónicos de entrevistado, mapa, sesión, inmersión, competencia y evaluación, y mantuvo una separación explícita entre hechos, formulación y límites. La persona participante, bajo el alias `Carmen`, validó el resumen, autorizó la conservación sin límite temporal de la muestra y aprobó excluir datos identificables innecesarios. La evaluación `EVALUACION_PILOTO_ENT-002-M01_2026-07-21` concluye experimentalmente `Continuar`: el mapa parcial fue útil y reconocido por la persona, pero el resultado no certifica competencias ni adopta formalmente la doble pasada.

## Actualización operativa Job-up — 2026-08-10 (estado previo a la validación de presentación)

Se implantaron y probaron `PLAYBOOK_VEREDICTO_FINAL_CARTA` y
`TEMPLATE_VEREDICTO_FINAL_CARTA`, ambos v1.0.0 en `en_prueba`, junto con el
verificador determinista y las pruebas T01–T17. Se registró la decisión humana
sobre `GATE-VEREDICTO-CARTA` (`aprobado`, 2026-08-10) sin reevaluar ni
regenerar la carta. CAND-2026-020 conserva `APTA`, valor incremental `medio`,
recomendación `incluir`, sin bloqueantes ni reservas relevantes. La rama de
carta queda cerrada y el paquete documental queda `listo_para_gate`. No se
modificaron carta, CV, contenido ni guion, no se abrió
`GATE-CANDIDATURA-PRESENTACION` y `presentada` permanece en `false`. Antes de
promover el playbook a `vigente` faltan casos independientes de reserva o
bloqueo y preferiblemente otro caso positivo.

## Registro histórico: validación operativa de presentación — 2026-08-11

Se creó `PLAYBOOK_VALIDAR_PRESENTACION_CANDIDATURA` v1.0.0 y su template. La
persona responsable abrió `GATE-CANDIDATURA-PRESENTACION` en `pendiente` para
CAND-2026-020. La oferta Lidl está disponible y el canal conduce al portal
SuccessFactors; la inspección reversible no inició sesión, no introdujo datos,
no aceptó consentimientos y no envió nada.

La evaluación de presentación resultó `APTA_CON_PENDIENTES_HUMANOS`: CV, carta,
identidad y versiones son conformes, pero la cuenta, contraseña, residencia,
visibilidad del perfil y aceptación de términos requieren intervención humana.
El gate continúa `pendiente` y `presentada` continúa en `false`.

## Cierre arquitectónico documental — 2026-08-11

La reorganización aprobada cierra el flujo vigente en la producción y aprobación
de documentos. Los playbooks maduros viven en `docs/metodologia/playbooks/` y
las plantillas maduras en `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/`.
Los documentos de presentación se conservan únicamente en
`docs/ideas-y-debates/mejoras-job-up/futuro/presentacion/`; los artefactos de
presentación de CAND-2026-020 se mantienen en `historico/`.

El estado vigente de CAND-2026-020 es `documentalmente_completa`, con CV y
carta finales aprobados y `presentada: false`. No existe una dependencia activa
de `GATE-CANDIDATURA-PRESENTACION`, de un paquete de presentación ni de un
formulario. CAND-2026-019 permanece detenida por su gate CV bloqueado.

La presentación externa, las credenciales, los formularios y cualquier envío
son líneas futuras y responsabilidad de la persona responsable. No se inicia
sesión, no se introducen datos y no se cambia `presentada` desde este flujo.

## Política de fotografía CV/carta — 2026-08-11

La auditoría contractual detectó una regla antigua que trataba la fotografía
como elemento obligatorio común de CV y carta. Se corrigieron las fuentes
operativas para reflejar la política vigente:

- CV: fotografía incluida por defecto, salvo exclusión humana expresa.
- Carta: fotografía no incluida por defecto; solo mediante decisión o
  configuración humana expresa específica para esa carta.

La autorización de fotografía en `control.datos_privados` confirma su
disponibilidad y uso autorizado para el CV, pero no implica renderizado en la
carta. El compositor de carta se mantiene sin carga ni inserción de imágenes.
CAND-2026-020 no se regeneró: su carta sin fotografía sigue siendo conforme,
con `APTA`, gate aprobado y estado `documentalmente_completa`.

## Alineación de la skill real de Job-up — 2026-08-11

La certificación previa del entorno E2E detectó que
`.codex/skills/job-up-candidatura-oferta/SKILL.md` seguía describiendo el
contrato histórico de generación conjunta, fotografía compartida y cierre
`pendiente_de_aprobacion`. La skill se reescribió como orquestador del flujo
documental vigente: análisis, candidatura, rama CV, rama independiente de
carta y cierre `documentalmente_completa`.

La skill referencia ahora los playbooks canónicos de
`docs/metodologia/playbooks/` y el contrato CV-only 1.2 de
`TEMPLATE_DATOS_GENERACION_CV.json`. La fotografía del CV y la carta permanece
separada y la presentación externa continúa fuera del alcance.

Se añadieron las regresiones `T-SKILL-01` a `T-SKILL-07`; la prueba E2E real
queda pendiente y todavía no se ha ejecutado ninguna skill ni se ha creado una
nueva candidatura.

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
- Diseñar posteriormente la UI de configuración de candidatura: catálogo de opciones, defaults y decisiones humanas, dependencias condicionales, contrato persistente, comportamiento guiado/adaptativo y posición exacta en la arquitectura Job-up. La línea tiene prioridad alta, está pendiente de diseño y no autoriza todavía implementación.
- Mantener CAND-2026-020 como `documentalmente_completa` y `presentada: false`; la presentación externa queda fuera del alcance actual y no debe iniciarse desde Job-up. Mantener CAND-2026-019 detenida por gate CV bloqueado.
- Mantener bloqueada la excepción sin fotografía del CV hasta que exista una decisión expresa y aprobada; la carta conserva su ausencia de fotografía por defecto. La futura configuración podrá separar ambas decisiones, pero no se implementa ahora.
- Evaluar por separado si Vault Operator o Local REST API MCP aportan valor a la bóveda ya consolidada, sin reinstalar configuraciones heredadas.
- Mantener separadas la cobertura, la profundidad y la correspondencia ESCO mientras no exista una decisión posterior que cambie ese alcance.
- No tratar la evaluación como validación con personas ni actualizar el SPEC o el playbook de profundidad por inferencia.
- Validar finalmente el flujo documental y cerrar la sesión PCS cuando no queden observaciones sobre la separación CV/carta.

## Acciones abiertas relevantes

- La preparación documental del piloto real está completada en `docs/superpowers/specs/2026-07-19-preparacion-piloto-cobertura-profesional-design.md`, `docs/trabajo-en-curso/diseno/CHECKLIST_PREPILOTO_COBERTURA_PROFESIONAL.md` y `docs/trabajo-en-curso/diseno/MATRIZ_EVALUACION_PILOTO_COBERTURA_PROFESIONAL.md`. Se han ejecutado los casos `ENT-001` y `ENT-002`; cada caso nuevo sigue condicionado a sus propias decisiones explícitas de autorización, alcance, conservación, identificador y revisión.
- `ACC-20260717-1642-001-materializar-versionado-carrera-ai` quedó completada; no deja trabajo abierto dentro de su alcance.
- No queda trabajo abierto para materializar la retirada de Graphify; la eliminación y las comprobaciones permanecen registradas históricamente en `sesion-20260717-1058-retirada-graphify-carrera-ai`.
- Es candidata a acción futura la definición del primer piloto, condicionada a una decisión explícita sobre la recomendación metodológica.
- [[ACC-20260721-1651-001-activar-rama-operativa-busqueda-empleo-fase-1]] está completada. Las fases de asistencia en Chrome y conectores de portales no son acciones autorizadas todavía.
- La prueba real del flujo modular CV-only, la emisión de veredictos y la decisión de gates CV están completadas para CAND-2026-020 y CAND-2026-019: Lidl aprobado; ASIC bloqueado. CAND-2026-020 tiene aprobados el CV, `GATE-GUION-CARTA-CONTENIDO`, `GATE-CONTENIDO-CV-COMPOSICION`, `GATE-CARTA-REVISION-HUMANA` y `GATE-VEREDICTO-CARTA` (aprobado humanamente el 2026-08-10). `PLAYBOOK_VEREDICTO_FINAL_CARTA` v1.0.0 está implantado en prueba. La validación de presentación pertenece únicamente a la línea futura; no existe gate de presentación activo en el flujo vigente.
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

## Actualización Job-up — CAND-2026-021 — 2026-08-11

Se inició la candidatura de OBRAMAT «ALMACÉN JINÁMAR — Coordinador/a de línea
de Cajas Evolutivo/a» a partir de su oferta oficial. Se verificó la fuente
completa y se crearon `candidatura.md` y `analisis-oferta.md` en el expediente
`CAND-2026-021`. La decisión inicial es `preparar_con_advertencias`: hay
experiencia relevante en operaciones de tienda, cajas, atención al cliente,
cuadres y coordinación, y el vehículo propio exigido está confirmado.

La autorización privada queda limitada a nombre, apellido 1, email, teléfono,
LinkedIn y fotografía, todos autorizados expresamente el 2026-08-11. La persona
responsable confirmó además que dispone de vehículo propio; se mantienen como
advertencias la movilidad por Canarias y los sistemas de caja específicos de
OBRAMAT. La sesión PCS reutilizada es `sesion-20260805-1757-job-up`.
`GATE-CANDIDATURA-GUION` y `GATE-GUION-CV-CONTENIDO` fueron aprobados
humanamente el 2026-08-11; ambos permitieron generar el guion y el contenido
estructurado.

`datos-generacion.json` se generó conforme al contrato CV-only 1.2. `GATE-CONTENIDO-
CV-COMPOSICION` fue aprobado humanamente el 2026-08-11 y permitió componer los
artefactos finales del CV.

La persona responsable aprobó ese gate el 2026-08-11 y se compusieron `cv.docx`,
`cv.pdf` y `cv.tex`. El PDF tiene una página, la fotografía autorizada aparece
y la huella SHA-256 quedó registrada en `revision-humana-cv.md`. La persona
responsable revisó el PDF y aprobó la revisión humana el 2026-08-11. Se generó
`veredicto-final-cv.md` con resultado `apto_para_presentacion` y recomendación de
aprobar `GATE-VEREDICTO-CV`. La persona responsable aprobó ese gate el
2026-08-11. La presentación, la carta y cualquier envío externo siguen fuera
de alcance. Para la rama independiente de carta se registraron las respuestas
humanas: ninguna motivación específica, conocimiento de OBRAMAT únicamente
como cliente y una razón profesional factual basada en experiencia de
supermercados, atención, caja y coordinación. Se consultó la URL oficial
`https://conoce.obramat.es/` como contexto corporativo. El guion y la evaluación
de `GATE-GUION-CARTA-CONTENIDO` están preparados con recomendación IA de
aprobar. La persona responsable aprobó humanamente ese gate el 2026-08-11,
autorizando únicamente el avance a la generación del contenido semántico de la
carta. Después se generaron `contenido-carta-presentacion.md` y su evaluación
de `GATE-CONTENIDO-CARTA-COMPOSICION`. El contenido es técnicamente `apto` y la
recomendación IA es aprobar. La persona responsable aprobó humanamente
`GATE-CONTENIDO-CARTA-COMPOSICION` el 2026-08-11, autorizando únicamente el
avance a composición. La composición produjo `carta-presentacion.docx` y
`carta-presentacion.pdf` en una página, con equivalencia semántica y revisión
visual técnica inicial apta, pero la persona responsable bloqueó la revisión
por formato del texto el 2026-08-11. Quedan abiertas la justificación del
cuerpo, fecha/asunto y alineación tipográfica con la guía; el contenido
semántico no se modifica.

### Corrección de composición de carta — CAND-2026-021 — 2026-08-11

Se corrigió el defecto principal de composición detectado: las líneas físicas
consecutivas de `contenido-carta-presentacion.md` se unen con espacios para
formar párrafos semánticos y ya no se generan saltos manuales de Word por cada
línea fuente. El cuerpo narrativo se justifica después de reconstruir los
párrafos. Fecha y asunto se incorporan únicamente porque la guía vigente los
exige y se derivan de forma determinista de la fecha de generación, el puesto y
la empresa confirmados. La cabecera se ajustó a la jerarquía contractual de
18/11/10,5 pt.

Se regeneraron `carta-presentacion.docx`, `carta-presentacion.pdf` y su
evaluación desde `contenido-carta-presentacion.md`, sin modificar su contenido
semántico. La prueba de regresión para hard wrapping pasa, el DOCX no contiene
`<w:br/>` espurios en el cuerpo, el PDF tiene una página y la revisión visual
del PNG renderizado confirma ausencia de cortes o solapamientos. `GATE-CARTA-
REVISION-HUMANA` permanece bloqueado hasta la nueva revisión humana de ambos
artefactos; no se abre ningún gate de presentación.

### Aprobación humana de revisión de carta — CAND-2026-021 — 2026-08-11

La persona responsable revisó y aprobó los nuevos DOCX y PDF de la carta.
`GATE-CARTA-REVISION-HUMANA` queda registrado como `decision_humana: aprobado`
y `estado_gate: aprobado`. La carta queda habilitada exclusivamente para el
diseño o ejecución posterior del veredicto final; no se ha iniciado esa fase,
no se ha abierto `GATE-CANDIDATURA-PRESENTACION` y `presentada` continúa en
`false`.

### Veredicto final de carta — CAND-2026-021 — 2026-08-11

Se ejecutó `PLAYBOOK_VEREDICTO_FINAL_CARTA` sobre la carta ya aprobada. Los
tres roles independientes —recruiter, responsable editorial/documental y
auditor de coherencia— no detectaron bloqueantes ni reservas relevantes. El
resultado técnico es `APTA`, con valor incremental `medio` frente al CV y
recomendación de inclusión `incluir`. `GATE-VEREDICTO-CARTA` queda
`pendiente` de decisión humana; no se ha abierto `GATE-CANDIDATURA-
PRESENTACION` y `presentada` continúa en `false`.

### Aprobación humana del veredicto de carta — CAND-2026-021 — 2026-08-11

La persona responsable aprobó `GATE-VEREDICTO-CARTA`. El resultado de la carta
queda `APTA`, con recomendación de inclusión y valor incremental medio. La
candidatura queda documentalmente preparada, pero la presentación externa sigue
fuera del flujo: `GATE-CANDIDATURA-PRESENTACION` no se abre automáticamente y
`presentada` continúa en `false`.

### Consolidación E2E y cierre de arquitectura — CAND-2026-021 — 2026-08-11

La prueba E2E real de OBRAMAT terminó correctamente en `documentalmente_completa`:
CV aprobado, carta aprobada, `GATE-VEREDICTO-CV` aprobado,
`GATE-CARTA-REVISION-HUMANA` aprobado y `GATE-VEREDICTO-CARTA` aprobado;
`presentada: false` y sin paquete ni módulo activo de presentación.

Se consolidaron como reglas generales los hallazgos E2E-01..E2E-10: fotografía
del CV por defecto sin pregunta, vehículo propio persistido en Data Core,
movilidad resuelta antes de `GATE-CANDIDATURA-GUION`, contexto corporativo
temprano, continuidad automática tras gates deterministas, hard wrapping sin
saltos manuales, separación entre render generado e inspección visual real,
identidad dinámica, cierre documental sin presentación y recomendación editorial
de inclusión de carta sin semántica de paquete.

Se alinearon skill, playbooks, templates, compositor, Data Core, seguimiento,
SPEC y pruebas de regresión. No se modificó el contenido semántico aprobado de
CAND-2026-021.

### Actualización factual posterior — CAND-2026-021 — 2026-08-11

Después del cierre documental, la persona responsable informó que presentó
manualmente la candidatura de OBRAMAT. El expediente y el seguimiento reflejan
ahora `presentada: true` como hecho posterior al flujo; la fecha y el canal no
constan en los registros locales. Esta actualización no abre ningún módulo de
presentación ni modifica la arquitectura: el flujo documental terminó en
`documentalmente_completa` y cualquier artefacto de veredicto que conserve
`presentada: false` representa el estado comprobado en el momento de su emisión.

### Nueva oferta no recomendada — CAND-2026-022 — 2026-08-11

Se consultó en InfoJobs la oferta «Administrativo/a — Departamento de
Administración de Fincas» de GRUPO ATLANTIS MULTISERVICIOS, SOCIEDAD LIMITADA.
La URL y el texto completo se conservaron en el expediente de
`CAND-2026-022`.

La persona responsable confirmó que no tiene experiencia en administración de
fincas ni asistencia a juntas de propietarios y que su inglés no es avanzado.
Ambos datos contradicen requisitos centrales de la oferta: experiencia literal
en juntas y administración de fincas, y nivel de inglés avanzado. El encaje se
clasificó como `sin_encaje` y la decisión estratégica como `no_recomendada`.

Solo se crearon `oferta-fuente.md` y `analisis-oferta.md`. No se creó
`candidatura.md`, guion, contenido, CV, carta, veredicto ni paquete; tampoco se
consultaron datos privados ni se realizó ninguna acción externa. La candidatura
queda detenida en la fase de análisis y no se abre ningún gate posterior.

### Nueva oferta en preparación — CAND-2026-023 — 2026-08-11

Se consultó en InfoJobs la oferta «Auxiliar administrativo/a SIN EXPERIENCIA»
de ESTUDIO SANTA LUCIA DE TIRAJANA, S. L., para una oficina de Tecnocasa en
Gáldar. No existe duplicidad con los expedientes anteriores y se reutilizó la
sesión PCS abierta.

El encaje se clasificó como `parcial_condicionado`: la experiencia en gestión
administrativa, documentación, Excel, organización y mejora de procesos es
transferible, y la oferta no exige experiencia previa. Se seleccionó
preliminarmente Administración como perfil principal y Operaciones/mejora de
procesos como secundario.

La persona responsable confirmó que acepta presentar una trayectoria directiva
a un puesto auxiliar y valorar el rango publicado de 19.000–24.000 € brutos
anuales. También autorizó para este caso nombre, apellido 1, email, teléfono,
fotografía y ubicación «Las Palmas»; apellido 2 y LinkedIn quedan omitidos.
Se creó `candidatura.md`, se aprobaron humanamente `GATE-CANDIDATURA-GUION`,
`GATE-GUION-CV-CONTENIDO` y `GATE-CONTENIDO-CV-COMPOSICION`, y se generaron
`guion-adaptacion-cv.md`, `datos-generacion.json` conforme al contrato 1.2 y
los artefactos `cv.docx`, `cv.pdf` y `cv.tex`. El PDF tiene una página y la
inspección visual técnica no detectó cortes ni solapamientos. La persona
responsable aprobó la revisión humana del PDF y del DOCX el 2026-08-11; se
registró `revision-humana-cv.md` con la huella del PDF. El veredicto final del
CV quedó como `revisar_antes_de_presentar`, con recomendación IA de no aprobar
por el encaje condicionado y el riesgo de sobrecualificación, pero la persona
responsable aprobó humanamente `GATE-VEREDICTO-CV` el 2026-08-11. El CV queda
autorizado para avanzar; la carta no se ha generado, no se ha realizado ninguna
acción externa y no se inicia la carta automáticamente. La persona responsable
solicitó iniciar el módulo de carta el 2026-08-11. Declaró que no tiene
motivación específica, no conoce ni tiene relación con la empresa y no desea
añadir una razón personal. Se prepararon `guion-carta-presentacion.md`,
`contenido-carta-presentacion.md` y sus evaluaciones; los gates de guion y
contenido fueron aprobados humanamente. Se compusieron
`carta-presentacion.docx` y `carta-presentacion.pdf`; el PDF tiene una página y
la inspección visual real fue apta. Durante la composición se detectó y corrigió
un defecto generalizable del verificador: los asuntos largos partidos en varias
líneas del PDF ya no se interpretan como contenido añadido. La regresión nueva
y la suite específica de composición pasan salvo un test preexistente de
CAND-2026-021 que sigue bloqueado porque esa candidatura figura como presentada.
La persona responsable revisó y aprobó humanamente ambos artefactos y
`GATE-CARTA-REVISION-HUMANA` el 2026-08-11. Se ejecutó el veredicto técnico
final de la carta: resultado `APTA`, valor incremental `medio` y recomendación
`incluir`, sin bloqueantes ni reservas relevantes. `GATE-VEREDICTO-CARTA` fue
aprobado humanamente el 2026-08-11. CAND-2026-023 queda documentalmente
completa, con CV y carta aprobados; la presentación externa sigue fuera de
alcance y la carta no se ha enviado.

### E2E-REGRESSION-01 — Continuidad tras revisión humana de carta — 2026-08-11

La ejecución E2E de `job-up-candidatura-oferta` con CAND-2026-023 detectó una
pausa redundante después de aprobar `GATE-CARTA-REVISION-HUMANA`: la skill
anunció el veredicto técnico como siguiente paso, pero se detuvo aunque no
faltaba ningún dato, decisión, revisión ni autorización. La candidatura estaba
documentalmente completa tras continuar manualmente, por lo que el defecto era
de orquestación y no de contenido.

La causa raíz fue que la regla de continuidad existía solo como texto normativo
en la skill/playbooks. No había una selección ejecutable de transición que
distinguiera entre anunciar un siguiente paso y ejecutarlo. El test anterior
T-E2E-05/T-E2E-06 de `tests/test_hallazgos_e2e_job_up.py` solo buscaba las frases
«gate aprobado» y «continúa automáticamente»; por eso produjo un falso
positivo sin simular el estado posterior al gate ni detectar una respuesta
terminal prematura.

Se corrigió creando `scripts/job-up/orquestar_transiciones.py`, un helper puro
que selecciona composición, veredicto, espera humana, bloqueo o cierre
documental según el estado. La skill y los playbooks remiten ahora a esa tabla
operativa. La nueva cobertura efectiva es
`test_t_e2e_06b_revision_carta_aprobada_selecciona_veredicto_sin_pausa`, junto
con las regresiones vecinas de composición, pausa humana real, cierre sin
presentación y gate bloqueado.

CAND-2026-023 no se regeneró ni se modificó semánticamente: permanece
`documentalmente_completa`, con CV y carta aprobados, `presentada: false` y la
presentación externa fuera de alcance. E2E documental, cierre documental y
ausencia de presentación permanecen PASS.

### Preparación de integración local — 2026-08-11

La auditoría de cierre de `codex/job-up-validar-presentacion` quedó completada.
La continuidad tras `GATE-CARTA-REVISION-HUMANA` se corrigió con
`scripts/job-up/orquestar_transiciones.py`, la skill y los playbooks quedaron
alineados y la regresión dispone de pruebas ejecutables. La suite completa
queda en 186 tests OK; también pasan la compilación de scripts/tests y
`git diff --check`. El siguiente gesto es crear el commit coherente e
integrarlo localmente en `main`. No se hará push, PR, presentación externa ni
nueva candidatura.

### Integración local completada — 2026-08-11

El commit `eff2d2d` se integró en `main` mediante el merge `784eadd`, sin
conflictos. La verificación posterior volvió a ejecutar 186 tests, la
compilación de scripts/tests, `git diff --check` y el smoke test del
orquestador; todo quedó en verde. La rama temporal se eliminó tras confirmar
su integración y no existe un worktree adicional. No se hizo push ni PR.
