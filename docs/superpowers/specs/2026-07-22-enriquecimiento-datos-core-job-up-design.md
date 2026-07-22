# Diseño — Enriquecimiento factual y posicionamiento de Job-up

**Fecha:** 2026-07-22
**Estado:** aprobado para documentación; pendiente de revisión de la especificación

## Propósito

Enriquecer la fuente factual de Job-up con evidencia reciente de dirección ejecutiva en Herfrailes S. L. y ajustar los materiales de candidatura espontánea para presentar un perfil de Dirección, Administración y Operaciones. El resultado evitará tanto el sesgo hacia RR. HH. como la exposición de experiencia política en las candidaturas.

## Alcance

- Incorporar en [[datos-core-busqueda]] los logros `HER-04` y `HER-05`, y una versión prudente de `HER-06` centrada en liderazgo directo y canales de comunicación.
- Incorporar la escala y evolución de Herfrailes, y los límites de atribución entre la contribución individual, el Consejo de Dirección y la central SPAR.
- Mantener la experiencia municipal como histórico factual, pero excluirla de los perfiles objetivo, de los logros seleccionables por defecto y de los materiales de candidatura.
- Reorientar los perfiles objetivo hacia Dirección, Administración y Operaciones.
- Actualizar la selección factual y los modelos de email para que destaquen dirección ejecutiva conectada con personas, procesos, sistemas y operaciones.
- Establecer tratamiento formal para empresas e intermediarios y tratamiento profesional cercano para contactos personales.

## Fuera de alcance

- Exponer en el CV, emails o selección factual la actividad política, la concejalía o el Ayuntamiento de Gáldar.
- Incluir parentescos, composición familiar de la propiedad u otra información de gobernanza sensible en la fuente factual general o en las candidaturas.
- Convertir hipótesis de reclutamiento, encuadres persuasivos o motivaciones personales en hechos de [[datos-core-busqueda]].
- Usar afirmaciones de reducción de costes, continuidad operativa u otros efectos no respaldados por evidencia factual.
- Enviar, compartir o publicar materiales sin aprobación humana explícita.

## Diseño de la información factual

[[datos-core-busqueda]] conservará únicamente hechos verificables, sus límites y las precauciones de atribución. Los nuevos logros especificarán qué acción realizó Gustavo, qué resultado puede atribuirse razonablemente y qué decisiones fueron colegiadas o dependieron del mercado.

La experiencia municipal podrá mantenerse en el histórico para preservar la trayectoria completa, pero no alimentará perfiles, logros por defecto, plantillas ni materiales entregables de Job-up.

Los encuadres sobre el periodo posterior a Herfrailes o sobre expectativas retributivas se tratarán como redacción opcional de candidatura, nunca como evidencia laboral. Solo se usarán después de una validación expresa de Gustavo para el caso concreto.

## Diseño de los materiales de candidatura

El CV maestro y los emails presentarán una identidad de dirección ejecutiva y operativa: capacidad para coordinar personas, procesos, sistemas y logística, demostrada con resultados concretos y verificables.

- `HER-04` podrá respaldar liderazgo, organización del trabajo y mejora operativa.
- `HER-05` podrá respaldar análisis de datos para decisiones operativas, sin atribuir la decisión colegiada de expansión.
- `HER-06` quedará fuera del uso predeterminado; solo podrá emplearse de forma breve en candidaturas donde la gestión de personas sea relevante y sin detalles de conflictos, personas o situaciones sensibles.
- La experiencia anterior se resumirá por defecto y se ampliará únicamente cuando aporte evidencia necesaria para la oportunidad concreta.

Para empresas e intermediarios, los emails utilizarán un tratamiento formal coherente. Para contactos personales, utilizarán un tratamiento profesional cercano. El email para una empresa concreta dejará un espacio para relacionar el contacto con un reto, proyecto o contexto real de esa empresa, sin inventarlo.

## Controles de calidad

- Las acciones que aparezcan en CV, email o carta se redactarán en primera persona.
- Cada afirmación se rastreará a [[datos-core-busqueda]] y respetará sus límites de atribución.
- Se comprobará que CV y emails no contengan referencias a gestión pública, actividad política, concejalía, Ayuntamiento de Gáldar ni información familiar sensible.
- Se verificará la coherencia entre los tres perfiles objetivo y el posicionamiento ejecutivo-operativo.
- Se revisarán explícitamente la ortografía española y la ausencia de formulaciones infladas antes de entregar los materiales.

## Criterios de aceptación

- La fuente factual contiene evidencia suficiente para sostener un perfil de dirección ejecutiva y operaciones, sin mezclar hechos con narrativa persuasiva.
- La experiencia política no aparece en ningún material de candidatura espontánea.
- Los emails usan el registro acordado para cada audiencia y proponen un siguiente paso concreto sin presuponer una necesidad de la empresa.
- Las nuevas afirmaciones mantienen la atribución individual, colegiada y contextual correcta.

## Relaciones

- Especificación base: [[2026-07-22-cv-maestro-candidatura-espontanea-design]].
- Fuente factual: [[datos-core-busqueda]].
- Materiales afectados: [[presentacion-espontanea/seleccion-factual]] y [[presentacion-espontanea/email-presentacion]].
- Rama operativa: `Job-up`.
