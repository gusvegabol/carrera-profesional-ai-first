# Idea conservadora - Línea de vida flexible y reconstruible

## Tesis

La entrevista de cobertura puede conservar una estructura temporal porque la trayectoria necesita contexto, pero no debe imponer un orden de conversación. La IA construye una línea de vida profesional **provisional y revisable** mientras deja que la persona empiece por el recuerdo que considere más importante, reciente, difícil o fácil de explicar.

La unidad de trabajo no es el puesto ni una respuesta aislada: es una **etapa o episodio** vinculado a un contexto, unas acciones, unas herramientas, unos resultados, unos aprendizajes y unas dudas. La cronología se completa como resultado de la conversación; no es una ruta que la persona deba recorrer de principio a fin.

## Problema que resuelve

Una entrevista cronológica clásica aporta orden, pero suele fallar con trayectorias discontinuas: simultaneidad de empleo y estudios, empleos breves, trabajo familiar, periodos de cuidado, actividad autónoma, cambios de sector o aprendizaje informal. También puede hacer que la persona recuerde primero lo más significativo y no lo más antiguo.

Esta propuesta mantiene la ventaja de una línea temporal para comprender evolución y transiciones, pero separa dos cosas que suelen confundirse:

- El **orden en que se conversa**, que pertenece a la persona.
- El **orden en que se representa la trayectoria**, que la IA propone y la persona valida.

Esto responde al requisito de Carrera AI de capturar etapas, simultaneidades, rupturas, retornos y reconversiones sin convertir la trayectoria en un CV. También conserva la trazabilidad: una competencia candidata nunca se deriva de un hueco temporal, sino de un episodio y de evidencia asociada. [Especificación de Carrera AI](../../DOCUMENTO_SPEC_CARRERA_AI.md)

## Recorrido de entrevista

### 1. Apertura con control explícito

La IA explica que no se trata de un test ni de una entrevista de selección. Pide permiso para ir construyendo un borrador de trayectoria y aclara que se puede empezar por cualquier punto, corregir fechas aproximadas, omitir temas o volver atrás.

Pregunta de apertura posible: «¿Por qué momento de tu vida profesional te resulta más fácil empezar hoy: uno reciente, un cambio importante o el primer trabajo que recuerdes?»

### 2. Captura por anclas, no por fechas obligatorias

Cada recuerdo abre un ancla: un empleo, una formación, una actividad autónoma, una responsabilidad familiar con componente laboral, un proyecto, una transición o una interrupción que la persona considere relevante. La IA registra el periodo como exacto, aproximado o desconocido; no presiona para completar la fecha.

Para cada ancla, pregunta de forma ligera: contexto, papel de la persona, tareas reales, herramientas, responsabilidades, una situación representativa, resultado o aprendizaje, y evidencia disponible. Si la respuesta deriva hacia otra etapa, la IA la sigue y crea una nueva ancla relacionada.

### 3. Reconciliación periódica del mapa

Después de dos o tres anclas, la IA muestra o verbaliza una síntesis breve: «Por ahora veo estas etapas y una posible relación entre ellas. ¿Qué falta, sobra o está situado de forma incorrecta?» La persona puede cambiar el nombre de una etapa, unir dos periodos, declarar que una relación no existe o dejar algo pendiente.

### 4. Barrido de cobertura sin interrogatorio lineal

Cuando el relato se estabiliza, la IA pregunta únicamente por zonas no cubiertas: formación durante el empleo, actividades paralelas, cambios de sector, periodos sin empleo formal, trabajo no remunerado, herramientas o uso de IA, preferencias actuales y restricciones. Cada pregunta se justifica con el objetivo de no invisibilizar experiencia, no con una exigencia de completar un formulario.

### 5. Cierre por estado, no por apariencia de completitud

La salida clasifica cada zona como `registrada`, `explorada`, `pendiente`, `no aplicable` u `omitida por decisión de la persona`. De esta forma, un perfil no parece completo solo porque la línea temporal tenga pocos huecos visuales.

## Cómo se comporta la IA ante respuestas no lineales

La IA mantiene un estado conversacional separado de la representación temporal. Como mínimo conserva: hilo actual, anclas creadas, relaciones propuestas, lagunas conocidas, preguntas aplazadas y formulaciones que la persona ha corregido.

Cuando la persona salta a otro momento, la respuesta adecuada es: reconocer el salto, capturar el nuevo episodio, conservar el hilo anterior como aplazado y pedir permiso antes de retomarlo. Ejemplo: «Esto parece importante para entender el cambio posterior. Lo incorporo como una etapa aparte; cuando te venga bien, podemos volver al trabajo en la asesoría o dejarlo pendiente.»

No se deben aplicar tres atajos habituales:

- Inferir que una pausa profesional significa falta de actividad o de capacidad.
- Rellenar una relación causal porque dos episodios están próximos en el tiempo.
- Convertir una narración fluida en evidencia fuerte sin pedir contexto o ejemplo.

## Adaptación de metodologías humanas a IA

La entrevista conductual y STAR no se copian como un guion rígido. Se utilizan como una lente opcional cuando una ancla tiene potencial profesional y la persona acepta profundizar. La IA puede preguntar por situación, acción y resultado, pero debe aceptar respuestas incompletas, lenguaje cotidiano y resultados no cuantificados.

El papel humano de escucha se sustituye por protocolos verificables: reflejo breve de lo entendido, confirmación de la persona, separación entre cita o relato y síntesis de la IA, y registro de incertidumbre. La IA no deduce sinceridad, motivación, competencia o estado emocional del tono, los silencios o la forma de escribir.

La lógica es compatible con BEI, que busca hechos conductuales, y con la validación de aprendizajes previos, que distingue identificación y documentación de una evaluación o certificación posterior. [BEI y Synergogy](<../../fuentes/What_is_BEI_Synergogy.md>) [CEDEFOP: cuatro fases de validación](https://www.cedefop.europa.eu/en/tools/validation-non-formal-informal-learning/eu-guidelines/2023/22-four-phases-validation)

## Datos que produce

Por cada ancla: denominación dada por la persona, periodo y precisión, contexto, actividades, responsabilidades, herramientas, posible uso de IA, episodios asociados, resultados, aprendizajes, evidencia, límites, conexiones propuestas y validación del entrevistado.

Por cada competencia: afirmación en lenguaje humano, experiencias origen, evidencia que la sostiene, fuerza de la evidencia, alcance, contraejemplos o límites, confianza y estado de validación. ESCO solo se plantea después como correspondencia candidata, nunca como la estructura que ordena el relato. [Perfil Profesional Accionable y equivalencia ESCO](<../../metodologia/conceptos/PERFIL_PROFESIONAL_ACCIONABLE_Y_EQUIVALENCIA_ESCO.md>)

## Ventajas debatibles

- Es fácil de explicar a personas y orientadores porque parte de una representación conocida.
- Permite comprobar cobertura de toda la trayectoria sin exigir una conversación lineal.
- Hace visibles transiciones, simultaneidades y periodos que un CV suele borrar.
- Es compatible con sesiones sucesivas: la línea se puede corregir y enriquecer.

## Riesgos y mitigaciones

El riesgo principal es que la IA acabe reconduciendo la conversación hacia la cronología por comodidad. La mitigación es medir cuántas veces interrumpe un relato para pedir una fecha y obligar a que toda pregunta de retorno sea opcional.

Otro riesgo es confundir una línea de vida ordenada con una trayectoria comprendida. La mitigación es exigir, para cada etapa relevante, contexto, acción o aprendizaje y estado de evidencia; una fecha por sí sola no sostiene una competencia.

## Hipótesis para un piloto

Estas métricas son hipótesis de evaluación, no umbrales ya demostrados:

- Porcentaje de anclas que la persona considera correctamente representadas al cierre.
- Número de correcciones voluntarias a la síntesis de la IA.
- Proporción de etapas con al menos un contexto y una actividad concreta, frente a meras etiquetas de puesto.
- Zonas de trayectoria declaradas como pendientes u omitidas, para distinguir cobertura real de silencio.
- Percepción de control de la persona: si pudo cambiar de tema, corregir y decidir qué no compartir.

## Decisiones para debatir

1. ¿La línea temporal debe mostrarse durante la conversación o solo en revisiones periódicas?
2. ¿Qué nivel de detalle mínimo convierte una ancla en experiencia útil sin sobrecargar a la persona?
3. ¿Cómo nombrar periodos no laborales para no imponer categorías ajenas?
4. ¿Cuándo una laguna merece una pregunta y cuándo debe permanecer como pendiente legítimo?

## Fuentes de apoyo

- [DOCUMENTO_SPEC_CARRERA_AI.md](../../DOCUMENTO_SPEC_CARRERA_AI.md)
- [What is BEI Synergogy](<../../fuentes/What_is_BEI_Synergogy.md>)
- [Narrative career counseling](<../../fuentes/Narrative career counseling - My career story and pictorial narratives.md>)
- [Guidelines on Recognition of Prior Learning](<../../fuentes/Recognition of Prior Learning_Guidelines RPLpdf.md>)
- [CEDEFOP, fases de validación](https://www.cedefop.europa.eu/en/tools/validation-non-formal-informal-learning/eu-guidelines/2023/22-four-phases-validation)
