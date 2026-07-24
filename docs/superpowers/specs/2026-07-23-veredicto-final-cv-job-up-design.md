# Diseño — veredicto final del CV en Job-up

**Fecha:** 2026-07-23
**Estado:** pendiente de revisión de la persona responsable

## Propósito

Incorporar al flujo de Job-up una revisión final del contenido del CV adaptado a una oferta. El veredicto debe elevar la calidad narrativa y la adecuación al puesto sin permitir que una redacción persuasiva contradiga la fuente factual, los permisos de privacidad o las restricciones ya vigentes.

El veredicto no sustituye la aprobación humana ni autoriza un envío. Su salida sirve para decidir si el CV requiere corrección, puede revisarse o queda listo para la aprobación humana.

## Alcance

- Evaluar el CV después de la generación documental y antes de registrar la candidatura como `pendiente_de_aprobacion`.
- Adaptar los cinco prompts aportados a cinco criterios homogéneos de evaluación, puntuados de 1 a 5.
- Separar los controles no negociables de integridad de la valoración de calidad.
- Registrar el resultado en la carpeta de cada candidatura y referenciarlo desde la ficha de candidatura.
- Producir recomendaciones de mejora específicas y rastreables, sin reescribir automáticamente el CV ni generar hechos nuevos.

## Fuera de alcance

- Enviar candidaturas o sustituir la aprobación humana.
- Convertir la investigación externa de empresa o sector en una condición para emitir el veredicto inicial.
- Inferir experiencia, métricas, competencias, idiomas, titulaciones, tecnologías actuales o responsabilidades no incluidas en [[datos-core-busqueda]].
- Convertir una nota alta en autorización para ignorar requisitos no acreditados de la oferta.
- Evaluar diseño visual más allá de los controles documentales ya establecidos en el playbook.

## Modelo de veredicto compuesto

El veredicto consta de tres capas que se resuelven en este orden.

### 1. Integridad — puerta de seguridad

La integridad se expresa como `apta` o `no_apta`, sin puntuación ni promedio. Se marca `no_apta` si el CV contiene cualquiera de estas incidencias:

- una afirmación que no puede rastrearse a [[datos-core-busqueda]];
- datos privados no autorizados para esa candidatura;
- histórico municipal restringido o actividad independiente no autorizada;
- responsabilidad colegiada presentada como decisión individual;
- titulación, idioma, tecnología, métrica o nivel de dominio superior a lo documentado;
- requisito de la oferta presentado como cumplido cuando solo está ausente o parcialmente acreditado.

Una integridad `no_apta` detiene el veredicto de salida: el resultado será `corregir antes de revisar`, aunque se mantengan las notas de calidad como diagnóstico.

### 2. Calidad — cinco criterios de 1 a 5

| Criterio | Prompt de origen adaptado | Pregunta de veredicto |
| --- | --- | --- |
| Primer escaneo y posicionamiento | validación 1 | ¿En los primeros diez segundos se entiende el puesto objetivo, la propuesta de valor y la razón para continuar leyendo? |
| Encaje competitivo | validación 2 | ¿La selección de experiencia y logros responde a la oferta y evita un perfil genérico, desenfocado o innecesariamente sobredimensionado? |
| Cobertura ATS respaldada | validación 3 | ¿Las palabras clave útiles de la oferta están presentes de manera natural y siempre respaldadas por hechos documentados? |
| Fuerza de la experiencia | validación 4 | ¿Cada bloque relevante expresa contribución, contexto y resultado verificable, en vez de enumerar responsabilidades genéricas? |
| Adecuación narrativa | validación 5 | ¿El resumen, las competencias y el tono se ajustan al nivel y contexto explícito de la oferta sin simular conocimiento de la empresa o del sector? |

La escala tiene el mismo significado en todos los criterios:

| Nota | Significado operativo |
| --- | --- |
| 1 | Deficiente: no comunica el criterio o crea una lectura claramente desfavorable. Requiere reescritura. |
| 2 | Débil: hay una base factual útil, pero permanece genérica, desordenada, poco relevante o insuficiente. Requiere corrección prioritaria. |
| 3 | Correcta: cumple el mínimo para el puesto, pero la evidencia o la formulación todavía puede ser más específica, clara o competitiva. |
| 4 | Sólida: resulta clara, pertinente y creíble; solo admite mejoras de precisión o economía verbal. |
| 5 | Excelente: comunica con rapidez una propuesta de valor específica, diferenciada y plenamente respaldada para esa oferta. |

Cada criterio debe incluir obligatoriamente: nota, evidencia observada en el CV, debilidad concreta, mejora prioritaria y límite factual que no puede superarse durante la mejora.

### 3. Decisión — salida operativa

La decisión se calcula con las siguientes reglas, sin usar la media como puerta de salida:

| Resultado | Regla |
| --- | --- |
| `corregir_antes_de_revisar` | Integridad `no_apta`, o una o más notas de 1 o 2. |
| `revisar_antes_de_aprobar` | Integridad `apta`, todas las notas al menos de 3 y alguna nota de 3. |
| `lista_para_aprobacion_humana` | Integridad `apta` y las cinco notas son de 4 o 5. |

La media aritmética, redondeada a una cifra decimal, se conserva únicamente como indicador comparativo entre versiones de la misma candidatura. No modifica el resultado anterior ni puede compensar una incidencia de integridad.

## Artefacto de veredicto

Cada candidatura tendrá un archivo `veredicto-final-cv.md` junto al CV. Su estructura será:

1. Identificación de candidatura, oferta, versión de CV y fecha de evaluación.
2. Resultado de integridad y lista de incidencias, si existen.
3. Tabla de los cinco criterios, con nota, evidencia, debilidad, mejora y límite factual.
4. Media orientativa y decisión de salida.
5. Cambios requeridos o recomendados antes de la siguiente versión.
6. Trazabilidad a [[datos-core-busqueda]], análisis de oferta y guion de adaptación.

El archivo debe poder leerse sin abrir el CV y no contendrá datos privados adicionales a los ya autorizados para la candidatura.

## Flujo de datos y uso

1. El proceso genera el CV desde el análisis de oferta, el guion de adaptación y la matriz factual.
2. Se ejecutan primero los controles de integridad contra esos tres artefactos y la autorización de datos privados.
3. Se aplican las cinco reglas de calidad al contenido del CV y al texto completo de la oferta.
4. Se registra el veredicto en `veredicto-final-cv.md`.
5. Si el resultado es `corregir_antes_de_revisar`, se corrige el CV y se repite el veredicto para la nueva versión.
6. Si el resultado es `revisar_antes_de_aprobar` o `lista_para_aprobacion_humana`, la persona responsable revisa el CV y decide si procede aprobarlo; el playbook sigue prohibiendo el envío automático.

### Mejora opcional: investigación contextual posterior

Después de emitir el veredicto inicial, el proceso puede ofrecer una investigación contextual sobre la empresa, el sector o ambos. No modifica ni retrasa el veredicto inicial.

1. El proceso informa a la persona responsable de qué se investigaría y muestra las URL o tipos de fuente propuestos antes de consultar nada.
2. La persona responsable autoriza o rechaza la consulta para esa candidatura concreta.
3. Si se autoriza, se consultan fuentes públicas pertinentes —por ejemplo, web corporativa, página de empresa en LinkedIn, descripción institucional o publicación de la oferta— y se registran las URL efectivamente usadas.
4. La investigación produce recomendaciones opcionales de vocabulario, tono, prioridades o ejemplos relevantes. No añade hechos al CV ni cambia el resultado de integridad.
5. Si se propone una revisión del CV a partir de ese contexto, se genera una nueva versión y se repite el veredicto completo; la persona responsable conserva la decisión final.

La investigación no atribuye a la empresa valores, prácticas, cultura o expectativas que no estén respaldados por una fuente identificada. La ausencia de fuentes suficientes se registra como «sin contexto externo verificado», no como una nota baja del CV.

## Integración documental

- [[PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0]] incorporará el veredicto después de la revisión factual y antes del registro final de estado.
- [[TEMPLATE_CANDIDATURA]] añadirá el enlace al veredicto, la decisión y la versión evaluada.
- Se creará [[TEMPLATE_VEREDICTO_FINAL_CV]] como plantilla de la instancia por candidatura.
- [[seguimiento-candidaturas]] podrá conservar la decisión de veredicto en observaciones, sin sustituir el estado formal de la candidatura.

## Manejo de errores y límites

- Si no se puede rastrear una frase del CV, se registra como incidencia de integridad y no se resuelve por suposición.
- Si una palabra clave no tiene respaldo factual, se registra como requisito no acreditado; no se añade al CV para mejorar ATS.
- Si la oferta no identifica empresa o sector con suficiente detalle, el criterio de adecuación narrativa se evalúa contra el texto de la oferta. La investigación contextual posterior solo se ofrece cuando pueda identificar fuentes públicas pertinentes.
- Si el CV aún no tiene autorización de datos privados, puede evaluarse con marcadores; la falta de autorización solo es incidencia si se han incorporado datos no autorizados.

## Criterios de aceptación

- Existe una plantilla reutilizable de veredicto con los cinco criterios y la escala 1–5 definida en esta spec.
- El playbook exige comprobar la integridad antes de interpretar la calidad.
- Ninguna nota, media o recomendación puede autorizar una afirmación no respaldada ni un envío.
- Cada candidatura puede registrar una versión evaluada, una decisión y mejoras concretas.
- La decisión distingue corrección obligatoria, revisión humana y preparación para aprobación.
- Una candidatura de prueba demuestra que los cinco criterios producen evidencia, mejoras y límites factuales concretos.
- La investigación contextual solo se inicia después del veredicto inicial, con autorización expresa y con las URL propuestas visibles antes de consultarlas.

## Relaciones

- Rama operativa: Job-up.
- Fuente factual: [[datos-core-busqueda]].
- Flujo de producción: [[PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0]].
- Diseño previo: `docs/superpowers/specs/2026-07-21-proceso-cv-adaptados-oferta-design.md`.
- Sesión operativa: [[sesion-20260722-1131-job-up]].
