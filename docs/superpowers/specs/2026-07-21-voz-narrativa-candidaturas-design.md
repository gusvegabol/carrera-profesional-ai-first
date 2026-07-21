# Diseño — Voz narrativa de candidaturas

## Objetivo

Evitar que los CV y las cartas de presentación copien literalmente la tercera persona de la matriz factual [[datos-core-busqueda]].

## Decisión de diseño

La matriz factual conserva la tercera persona, porque documenta hechos comprobables. Los documentos de candidatura transforman esa evidencia a la voz de la persona candidata sin modificar su alcance factual.

## Regla de transformación

1. Los verbos de acciones realizadas por la persona candidata se redactan en primera persona: «Diseñé», «Automaticé», «Clasifiqué».
2. Se mantiene la tercera persona cuando el sujeto no es la persona candidata, por ejemplo: «el personal pasó a recibir…» o «las decisiones correspondían al Consejo de Dirección».
3. La transformación solo cambia la voz narrativa. No permite añadir responsabilidades, métricas, titulaciones, tecnologías ni resultados no respaldados por la matriz.
4. El CV puede usar encabezados o descriptores nominales; no puede describir la experiencia de la persona candidata mediante verbos de acción en tercera persona.
5. La carta de presentación se redacta en primera persona.

## Control previo a la producción

Antes de generar DOCX y PDF, el proceso debe revisar cada afirmación de logro seleccionada y confirmar:

- sujeto de la acción identificado;
- primera persona cuando el sujeto es la persona candidata;
- tercera persona solo para otros sujetos;
- trazabilidad de la frase a [[datos-core-busqueda]].

## Alcance

Se modifica únicamente el playbook operativo y su lista de control. No se modifica la matriz factual ni la metodología de investigación de entrevista.

## Criterio de aceptación

El playbook debe contener la regla de transformación y una comprobación final que impida generar un CV con verbos de acción de la persona candidata en tercera persona.
