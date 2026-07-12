# Evaluación experta y recomendación de enfoque

## 1. Mandato, fuentes y límite de la evaluación

Este documento evalúa cuatro propuestas para que una IA entreviste a una persona y construya la primera versión útil de su Perfil Profesional Accionable. El evaluador adopta el papel de especialista en entrevista profesional, evidencia conductual, reconocimiento de aprendizajes previos, diseño conversacional IA-persona y ESCO.

El objetivo no es declarar una verdad metodológica definitiva ni adoptar un playbook. Es recomendar un enfoque inicial debatible que satisfaga los objetivos de [Carrera AI](../DOCUMENTO_SPEC_CARRERA_AI.md): comprender una trayectoria completa, generar información profesional útil, vincular inferencias con evidencias y conservar incertidumbre, validación humana y correspondencias ESCO candidatas. El informe no certifica competencias ni convierte una correspondencia ESCO en prueba individual.

Las fuentes obligatorias son las cuatro propuestas: [Idea 1](<01_Conservadora_linea_de_vida_flexible_y_reconstruible.md>), [Idea 2](<02_Conservadora_doble_pasada_panorama_e_inmersion_selectiva.md>), [Idea 3](<03_Innovadora_atlas_conversacional_de_episodios_transiciones_y_capacidades.md>) e [Idea 4](<04_Innovadora_dossier_de_hipotesis_contrastables_y_evidencia_progresiva.md>). Para interpretar sus fundamentos se usan [BEI y Synergogy](<../Núcleo Metodológico del Playbook/What_is_BEI_Synergogy.md>), [orientación narrativa](<../Núcleo Metodológico del Playbook/Narrative career counseling - My career story and pictorial narratives.md>), [RPL](<../Núcleo Metodológico del Playbook/Recognition of Prior Learning_Guidelines RPLpdf.md>), [SFIA](<../Núcleo Metodológico del Playbook/How SFIA works - Levels of responsibility and skills.md>), [ESCO](<../Núcleo Metodológico del Playbook/ESCO_Booklet.md>) y [Perfil Profesional Accionable y equivalencia ESCO](<../Núcleo Metodológico del Playbook/PERFIL_PROFESIONAL_ACCIONABLE_Y_EQUIVALENCIA_ESCO.md>).

CEDEFOP distingue identificación, documentación, evaluación y certificación de los aprendizajes previos; esta recomendación solo pretende apoyar las dos primeras, no certificar competencias. [CEDEFOP](https://www.cedefop.europa.eu/en/tools/validation-non-formal-informal-learning/eu-guidelines/2023/22-four-phases-validation) ESCO aporta una clasificación de ocupaciones, conocimientos y habilidades, pero no prueba por sí misma la capacidad individual. [Comisión Europea, ESCO](https://esco.ec.europa.eu/en/classification/occupation_main)

## 2. Rúbrica equilibrada

Cada criterio se puntúa de `0` a `5` y pesa lo mismo. La puntuación es una herramienta comparativa, no un resultado empírico.

| Puntuación | Significado |
| --- | --- |
| 5 | El mecanismo es explícito, operativo, verificable y contempla sus riesgos. |
| 4 | El mecanismo es sólido, aunque mantiene una limitación operativa concreta. |
| 3 | El criterio está presente, pero depende de decisiones aún no resueltas. |
| 2 | La respuesta es indirecta o insuficiente. |
| 0-1 | El enfoque lo ignora o entra en conflicto con él. |

Los criterios son:

1. Cobertura de trayectorias no lineales.
2. Calidad y trazabilidad de la evidencia.
3. Adaptación responsable de métodos humanos a una IA.
4. Carga y control de la persona entrevistada.
5. Viabilidad para el MVP.
6. Privacidad y prudencia.
7. Validación, corrección y manejo de incertidumbre.

## 3. Evaluación de las ideas

### Idea 1: Línea de vida flexible y reconstruible

Su mayor aportación es separar el orden del relato del orden de la representación temporal. Las anclas, el retorno opcional y los estados `registrada`, `explorada`, `pendiente`, `no aplicable` u `omitida` tratan los saltos como información en vez de como errores. Esto responde especialmente bien a trayectorias con simultaneidades, rupturas y transiciones. [Idea 1](<01_Conservadora_linea_de_vida_flexible_y_reconstruible.md>)

También adapta bien los métodos humanos: STAR queda como lente opcional, la IA debe reflejar y pedir confirmación, y no puede inferir motivación, sinceridad o competencia por estilo, tono o silencios. Su límite es que la metáfora temporal puede volver a dominar la conversación si no se controla; además, la trazabilidad de cada inferencia no está tan formalizada como en la Idea 4.

**Dictamen:** excelente salvaguarda de no linealidad y de control de la persona; no basta por sí sola para gobernar la profundidad de evidencia en un MVP.

### Idea 2: Doble pasada, panorama e inmersión selectiva

La propuesta separa conscientemente dos objetivos que compiten: registrar toda la trayectoria y obtener evidencia conductual suficiente. El panorama abierto recoge bloques, actividades formales e informales, herramientas y preguntas pendientes; la inmersión, elegida por la persona, profundiza en uno o dos episodios mediante STAR simple. [Idea 2](<02_Conservadora_doble_pasada_panorama_e_inmersion_selectiva.md>)

Esta separación se alinea con el Perfil Profesional Accionable: no todas las capas tienen que completarse en una sesión, pero las competencias deben conservar evidencia, límites y estado de validación. [Perfil Profesional Accionable y equivalencia ESCO](<../Núcleo Metodológico del Playbook/PERFIL_PROFESIONAL_ACCIONABLE_Y_EQUIVALENCIA_ESCO.md>) También mantiene la distinción RPL entre identificar y documentar, por un lado, y evaluar o certificar, por otro. [CEDEFOP](https://www.cedefop.europa.eu/en/tools/validation-non-formal-informal-learning)

Sus límites son previsibles y gestionables: la segunda pasada puede privilegiar episodios fáciles de relatar, y la división en dos momentos puede rigidizarse si la IA no permite que la conversación alterne libremente entre panorama y detalle. La Idea 1 y la Idea 4 corrigen precisamente ambos riesgos.

**Dictamen:** la mejor arquitectura base para un MVP porque ordena cobertura, evidencia y carga conversacional sin prometer profundidad homogénea donde no existe.

### Idea 3: Atlas conversacional de episodios, transiciones y capacidades

Es el enfoque más potente para representar trayectorias no lineales. Un atlas de episodios, contextos, recursos y relaciones puede hacer visibles simultaneidades, bifurcaciones, transferencias y retornos que una línea temporal simplifica. Su propuesta de que toda relación tenga origen, evidencia, confianza y estado evita que la IA convierta una asociación plausible en hecho. [Idea 3](<03_Innovadora_atlas_conversacional_de_episodios_transiciones_y_capacidades.md>)

La orientación narrativa respalda atender a significado, transiciones y agencia, pero no autoriza a la IA a interpretar una historia de manera autónoma. [Orientación narrativa](<../Núcleo Metodológico del Playbook/Narrative career counseling - My career story and pictorial narratives.md>) La Idea 3 reconoce este límite y exige validación de la persona.

Su desventaja es la viabilidad: incluso una visualización mínima de nodos y relaciones puede aumentar carga cognitiva, complejidad de producto y falsa sensación de precisión. El riesgo no es conceptual, sino de introducir demasiada arquitectura antes de demostrar la utilidad de la entrevista.

**Dictamen:** mejor candidato para evolución posterior, no para definir el núcleo del primer MVP.

### Idea 4: Dossier de hipótesis contrastables y evidencia progresiva

Es la propuesta más fuerte para impedir que la IA convierta un relato persuasivo en una competencia inflada. Cada afirmación candidata conserva base declarada, alcance, límites, evidencia adicional o contraejemplo y estado decidido por la persona. Esto materializa los requisitos de trazabilidad, prudencia, explicabilidad y validación del SPEC. [Idea 4](<04_Innovadora_dossier_de_hipotesis_contrastables_y_evidencia_progresiva.md>) [Carrera AI](../DOCUMENTO_SPEC_CARRERA_AI.md)

Es coherente con BEI, que busca hechos conductuales, y con SFIA, que relaciona capacidad con responsabilidad y contexto; no convierte ninguno de esos marcos en una certificación automática. [BEI y Synergogy](<../Núcleo Metodológico del Playbook/What_is_BEI_Synergogy.md>) [SFIA](<../Núcleo Metodológico del Playbook/How SFIA works - Levels of responsibility and skills.md>)

Su límite está en la experiencia: si se presentan demasiadas hipótesis o contraejemplos, la conversación puede sentirse defensiva, evaluativa o fatigante. Su valor máximo aparece al aplicarse solo a las afirmaciones que van a alimentar competencias, narrativas u opciones relevantes, no a cada frase.

**Dictamen:** mecanismo de seguridad metodológica imprescindible, pero no estructura suficiente por sí mismo para garantizar la cobertura de toda una vida profesional.

## 4. Matriz comparativa

Cada cifra enlaza con la fuente principal que la justifica. La suma máxima es `35`.

| Idea | No linealidad | Evidencia | IA responsable | Carga y control | MVP | Privacidad y prudencia | Validación | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [1](<01_Conservadora_linea_de_vida_flexible_y_reconstruible.md>) | 5 | 4 | 5 | 5 | 5 | 4 | 4 | **32** |
| [2](<02_Conservadora_doble_pasada_panorama_e_inmersion_selectiva.md>) | 4 | 5 | 5 | 5 | 5 | 4 | 4,5 | **32,5** |
| [3](<03_Innovadora_atlas_conversacional_de_episodios_transiciones_y_capacidades.md>) | 5 | 4 | 5 | 3 | 3 | 4 | 4 | **28** |
| [4](<04_Innovadora_dossier_de_hipotesis_contrastables_y_evidencia_progresiva.md>) | 4 | 5 | 5 | 3 | 4 | 5 | 5 | **31** |

La Idea 2 obtiene la puntuación más alta. No supera a la Idea 1 en tratamiento de la no linealidad, por lo que la recomendación queda condicionada a incorporar sus salvaguardas conversacionales. Su ventaja proviene de separar explícitamente cobertura y profundidad, y de que la persona elija qué episodios explorar antes de convertirlos en competencias candidatas. Dado que la primera versión útil necesita cubrir trayectoria y demostrar que puede extraer competencias defendibles, se adopta la **Idea 2 como base**, condicionada por los complementos requeridos que siguen.

## 5. Recomendación: Idea 2 con complementos delimitados

### Ganadora: Idea 2 como arquitectura base

La doble pasada ofrece la mejor relación entre alcance, rigor y viabilidad. El panorama evita que la entrevista se reduzca a los empleos más fáciles de contar; la inmersión selectiva evita que una cobertura amplia produzca solo etiquetas y tareas. La elección de uno o dos episodios mantiene la carga del MVP bajo control y permite probar el valor de la evidencia conductual sin convertir toda sesión en una inmersión profunda.

### Complementos requeridos para el MVP

1. **De la Idea 1: conversación libre, estructura reconstruible.** El panorama no debe ejecutarse como una cronología obligatoria. La persona podrá empezar donde quiera; la IA conservará anclas, hilos aplazados y estados de cobertura, y pedirá permiso antes de retomar un tema. Esto corrige el principal riesgo de rigidez de la Idea 2.

2. **De la Idea 4: registro ligero de afirmaciones candidatas.** Para cada competencia, herramienta relevante, patrón o opción profesional que vaya a aparecer en el perfil, se registrarán origen, evidencia, alcance o límite, confianza y estado de la persona: `aceptada`, `corregida`, `rechazada` o `pendiente`. No se abrirá una hipótesis por cada frase. Esto corrige el riesgo de que STAR simple produzca inferencias demasiado fuertes.

3. **De la Idea 4: salida y privacidad bajo control de la persona.** La persona podrá decidir qué información sensible se excluye de la salida, qué evidencia queda pendiente y qué afirmaciones no desea incorporar. Las correspondencias ESCO permanecerán como candidatas justificadas, nunca como prueba de competencia individual. [Perfil Profesional Accionable y equivalencia ESCO](<../Núcleo Metodológico del Playbook/PERFIL_PROFESIONAL_ACCIONABLE_Y_EQUIVALENCIA_ESCO.md>)

### Complementos opcionales para evolución

1. **De la Idea 3: mapa de relaciones no visible por defecto.** Tras validar el MVP, se puede experimentar con un atlas interno de episodios y conexiones para facilitar reanudación de sesiones y detectar zonas poco exploradas. Solo deberá mostrarse a la persona si aumenta comprensión y control; una relación no validada no podrá alimentar una narrativa ni una competencia.

2. **De la Idea 1: visualización de línea de trayectoria.** Puede ofrecerse como revisión editable posterior, no como interfaz que imponga orden durante la conversación.

## 6. Implicaciones para un primer piloto

El piloto debe probar una entrevista, no un sistema de clasificación cerrado. El flujo recomendado es:

1. Explicar propósito, límites, control de datos y que no se trata de un test ni de una certificación.
2. Abrir un panorama libre de trayectoria y registrar anclas, contexto, actividades, herramientas, uso de IA, preferencias, restricciones y preguntas pendientes.
3. Reconciliar periódicamente el mapa provisional, aceptar correcciones y marcar zonas no exploradas sin rellenarlas por inferencia.
4. Permitir que la persona seleccione uno o dos episodios para inmersión; usar STAR simple solo cuando resulte útil y aceptar respuestas parciales.
5. Crear el registro ligero de afirmaciones candidatas para la información que vaya a componer el Perfil Profesional Accionable.
6. Cerrar con una revisión diferenciada de hechos, evidencia, inferencias candidatas, límites, preguntas pendientes y posibles correspondencias ESCO.

Las medidas del piloto deben incluir cobertura reconocida por la persona, proporción de afirmaciones con origen y límite documentados, correcciones o rechazos de la IA, percepción de control y carga, y utilidad de la primera narrativa profesional. Una alta aceptación de una formulación no debe interpretarse por sí sola como validez: puede reflejar fluidez del texto o asentimiento.

## 7. Preguntas abiertas

1. ¿La inmersión selectiva ocurre en la misma sesión o se ofrece como siguiente cita para reducir fatiga?
2. ¿Qué evidencia mínima permite elevar una afirmación desde `candidata` a `validada por la persona` sin confundir esa validación con certificación?
3. ¿Qué campos del registro de afirmaciones deben ser visibles, editables o eliminables por la persona?
4. ¿Cómo se determinará que una zona de trayectoria está suficientemente cubierta para el objetivo de una sesión concreta?
5. ¿Qué señal empírica justificaría introducir el atlas de relaciones como evolución de producto?

## 8. Conclusión

La recomendación es adoptar la **Idea 2, Doble pasada: panorama e inmersión selectiva**, como enfoque de entrevista para el primer MVP de cobertura profesional. No debe aplicarse de forma aislada: requiere la libertad de recorrido y los estados de cobertura de la Idea 1, junto con el registro limitado y corregible de hipótesis de la Idea 4. El atlas de la Idea 3 conserva valor estratégico, pero debe esperar a que un piloto demuestre que su complejidad mejora la comprensión de la persona más de lo que aumenta su carga.

Esta conclusión es una propuesta de diseño basada en fuentes y criterios explícitos. Sigue pendiente de contraste con entrevistas reales antes de convertirse en una decisión metodológica estable.
