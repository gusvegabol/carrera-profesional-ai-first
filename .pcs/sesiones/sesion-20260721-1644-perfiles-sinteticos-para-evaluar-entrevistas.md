---
id: sesion-20260721-1644-perfiles-sinteticos-para-evaluar-entrevistas
titulo: Perfiles sintéticos para evaluar y mejorar entrevistas
inicio: 2026-07-21 16:44
cierre:
estado: abierta
tipo: sesion
host: carrera-ai
sesion_relacionada: sesion-20260705-concepto-cobertura-profesional-carrera-ai
---

# Sesión PCS — Perfiles sintéticos para evaluar y mejorar entrevistas

## Contexto inmediato

Las pruebas con personas reales han mostrado valor, pero su ciclo completo —entrevista, documentación, evaluación, aprendizaje y nueva prueba— exige un tiempo elevado. Además, todavía no se han probado de forma suficiente la continuidad entre sesiones, la reanudación desde un checkpoint ni determinados casos difíciles de entrevista.

Se propone abrir una línea de debate sobre el uso de perfiles sintéticos: una persona o agente representaría una trayectoria profesional construida para el caso, mientras otra IA aplicaría el playbook de entrevista. El resultado permitiría observar, documentar y repetir el comportamiento del entrevistador con mayor velocidad.

## Objetivo

Deliberar si un conjunto de perfiles sintéticos puede servir como banco de pruebas para acelerar la evaluación y mejora de los playbooks de entrevista, sin confundir sus resultados con validación metodológica obtenida con personas reales.

## Capa episódica

La idea nace al identificar que la disponibilidad y el coste de coordinación con personas limitan la velocidad de aprendizaje del piloto. El caso real `ENT-002` permitió revisar apertura, selección de zona, inmersión y validación de salida, pero no pudo probar reanudación de una segunda sesión ni la recuperación exacta de una inmersión interrumpida.

La propuesta no se ha debatido ni diseñado todavía. Esta sesión solo registra el punto de partida para una futura sesión de Work dedicada a valorar su utilidad, límites y posible protocolo.

## Capa semántica

Los perfiles sintéticos serían un instrumento de ensayo, no sustitutos de la experiencia profesional de personas reales ni evidencia de que una entrevista funcione en condiciones humanas. Podrían permitir construir casos deliberados con trayectorias, contradicciones, huecos, minimización, cambios de tema, reanudaciones y checkpoints, siempre que se mantenga la separación entre:

- prueba de comportamiento del playbook;
- evidencia experimental con perfiles sintéticos;
- validación con personas reales;
- adopción metodológica formal.

## Ideas y líneas cognitivas abiertas

- Definir qué debe contener un perfil sintético para ser útil sin volverlo predecible o artificial.
- Determinar si la simulación debe usar un único agente con guion oculto, agentes separados o intervención humana de revisión.
- Diseñar casos específicos para segunda sesión, tercera sesión, zona parcial y reanudación desde checkpoint.
- Establecer qué métricas de entrevista pueden observarse automáticamente y cuáles requieren revisión humana.
- Identificar riesgos: respuestas demasiado coherentes, sesgo hacia lo que el entrevistador espera, falsa sensación de validación y contaminación entre el perfil y el agente entrevistador.
- Delimitar qué aprendizajes de perfiles sintéticos requieren después confirmación con personas reales.

## Acciones derivadas

No se crea ninguna acción PCS por ahora. La posible definición de un banco de pruebas sintético queda pendiente de debate y alcance explícito.

## Decisiones derivadas

No hay decisión formal. Esta sesión no autoriza crear perfiles, ejecutar simulaciones, modificar playbooks ni sustituir pilotos con personas reales.

## Problemas o bloqueos

- Riesgo de que un perfil sintético responda de un modo demasiado ordenado, cooperativo o conocedor de la estructura de la entrevista.
- Riesgo de optimizar el playbook para casos generados y no para conversaciones humanas reales.
- Falta de criterios acordados para considerar que un caso sintético es suficientemente exigente y auditable.

## Documentos afectados

- `.pcs/sesiones/sesion-20260721-1644-perfiles-sinteticos-para-evaluar-entrevistas.md`
- `.pcs/estado/estado-actual.md`

## Rehidratación futura

- **Dónde quedó el trabajo:** propuesta registrada, sin debate ni diseño iniciado.
- **Leer primero:** `docs/DOCUMENTO_SPEC_CARRERA_AI.md`, `docs/metodologia/playbooks/PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_0.md`, `docs/trabajo-en-curso/diseno/MATRIZ_EVALUACION_PILOTO_COBERTURA_PROFESIONAL.md` y esta sesión.
- **Líneas abiertas a retomar:** alcance de los perfiles sintéticos, modalidad de simulación, casos de continuidad y criterios de validez.
- **Riesgos de malinterpretación:** no presentar resultados sintéticos como validación con personas ni como adopción del método.
- **Siguiente gesto recomendado:** abrir una sesión de Work específica para debatir el diseño mínimo y los límites del banco de pruebas sintético.

## Trazabilidad

- Origen: observación del cuello de botella temporal en los pilotos reales de entrevista.
- Sesión relacionada: `sesion-20260705-concepto-cobertura-profesional-carrera-ai`.
- Estado de proyecto relacionado: `.pcs/estado/estado-actual.md`.
- Cierre: pendiente.
