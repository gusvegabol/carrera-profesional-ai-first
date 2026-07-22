# Diseño — CV maestro para candidatura espontánea

**Fecha:** 2026-07-22
**Estado:** aprobado para documentación

## Propósito

Definir los materiales de Job-up para presentar una candidatura espontánea por correo electrónico, sin depender de una oferta concreta. El resultado permitirá compartir una presentación profesional coherente con empresas conocidas, intermediarios de colocación y contactos personales.

## Alcance

- Crear un CV maestro de dos páginas, en español, que integre Dirección (Management), Administración y Operaciones.
- Crear un email breve y modular para tres destinatarios: empresa concreta, intermediario de colocación y contacto personal.
- Permitir convertir el cuerpo del email en una carta formal si el destinatario la solicita, sin alterar sus afirmaciones factuales.

## Fuera de alcance

- Adaptar una candidatura a una oferta o empresa concreta.
- Crear una carta adjunta por defecto.
- Modificar el SPEC o los playbooks de investigación de entrevista.
- Incluir afirmaciones, responsabilidades, métricas, titulaciones, idiomas o competencias no respaldadas por [[datos-core-busqueda]].
- Enviar emails o compartir documentos sin aprobación humana explícita.

## Diseño de materiales

### CV maestro

El CV tendrá dos páginas y la siguiente estructura:

1. Encabezado profesional y datos de contacto autorizados.
2. Titular profesional integrador.
3. Resumen de valor breve.
4. Áreas de contribución: Dirección (Management), Administración y Operaciones.
5. Experiencia profesional en orden cronológico, con logros y responsabilidades factuales, claramente trazables y redactados en primera persona cuando la acción corresponda a la persona candidata.
6. Competencias, herramientas, formación e idiomas únicamente cuando estén confirmados.

La identidad profesional se presentará de forma integrada. Las tres áreas serán visibles, pero no se redactarán como tres CV independientes ni se priorizará permanentemente una de ellas.

### Email modular

El email incluirá asunto, saludo, apertura, propuesta de valor de tres o cuatro líneas, cierre y referencia al CV adjunto. Tendrá tres variantes de apertura y cierre:

- Empresa concreta: interés por aportar a esa organización, sin afirmar conocimiento no verificado de sus necesidades.
- Intermediario de colocación: síntesis clara de los tres ámbitos profesionales y disponibilidad para oportunidades compatibles.
- Contacto personal: petición respetuosa de difusión o conexión con organizaciones donde el perfil pueda aportar valor.

El mismo cuerpo factual podrá convertirse en carta formal si se solicita, cambiando solo el formato, el saludo y el cierre.

## Flujo de preparación y uso

1. Consultar [[datos-core-busqueda]] para seleccionar exclusivamente información profesional factual.
2. Consultar [[datos-privados-candidatura]] solo cuando la preparación del CV o del email requiera datos de contacto autorizados.
3. Crear el CV maestro editable y su versión PDF.
4. Crear la plantilla de email con sus tres variantes de destinatario.
5. Para un destinatario concreto, adaptar únicamente el asunto, el saludo, la apertura y las líneas de valor necesarias, conservando el CV maestro como base.
6. Revisar los materiales antes de compartirlos y solicitar aprobación humana explícita antes de cualquier envío.

## Controles de calidad y privacidad

- Cada afirmación profesional debe poder rastrearse hasta [[datos-core-busqueda]].
- Las acciones realizadas por la persona candidata se redactarán en primera persona, por ejemplo: «Conseguí», «Reformulé», «Automaticé» o «Clasifiqué». No se usarán formas en tercera persona como «Consiguió», «Reformuló», «Automatizó» o «Clasificó» para describir esas acciones.
- El CV no excederá dos páginas.
- Los datos de contacto se incorporarán solo cuando hayan sido autorizados para el material correspondiente.
- El email no se enviará, ni se compartirá el CV, sin una instrucción explícita de la persona responsable.
- Si falta evidencia para una afirmación o existe una contradicción factual, la afirmación se excluirá y se solicitará revisión.

## Criterios de aceptación

- El CV expresa una identidad profesional única y reconoce con claridad Dirección (Management), Administración y Operaciones.
- Las acciones de la persona candidata están redactadas en primera persona y conservan su trazabilidad factual.
- El documento funciona como presentación general para los tres canales definidos.
- El email dispone de tres variantes y puede transformarse en carta formal sin añadir contenido factual.
- El CV y el email respetan el límite de idioma español, el máximo de dos páginas del CV, la trazabilidad factual y la aprobación humana previa al envío.

## Relaciones

- Rama operativa: `Job-up`.
- Fuente factual: [[datos-core-busqueda]].
- Datos de contacto autorizados: [[datos-privados-candidatura]].
- Decisión de alcance: [[DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo]].
- Sesión de trabajo: [[sesion-20260722-1131-job-up]].
