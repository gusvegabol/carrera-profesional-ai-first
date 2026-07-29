# Job-up: búsqueda de empleo

## Modelo mental de Job-up

Job-up es la rama operativa de Carrera AI para preparar candidaturas de empleo
trazables a partir de información factual. Su misión es convertir una oferta o
una oportunidad concreta en un paquete documental revisable por la persona
candidata, sin enviar candidaturas ni contactar con empresas.

Job-up cubre el análisis de ofertas, la selección factual, la preparación de
CV, cartas y demás artefactos, el seguimiento y la entrega en
`pendiente_de_aprobacion`. No sustituye la entrevista metodológica ni amplía
su alcance a investigación de empresas, networking o relaciones profesionales.

### Límites de trabajo

- La evidencia factual procede de la [fuente factual de búsqueda](fuentes/datos-core-busqueda.md); si falta un dato, se declara el límite y no se completa por inferencia.
- Toda afirmación debe respetar la atribución individual, las decisiones colegiadas y los requisitos no acreditados.
- La compuerta de datos privados exige una autorización específica para la candidatura. Puede reutilizarse una autorización escrita en la ficha privada solo para esa misma candidatura; no se copian ni se propagan datos no autorizados.
- La revisión y aprobación humana son obligatorias antes de cualquier envío o contacto externo.

### Arquitectura de la rama

```text
busqueda-empleo/
├─ README.md
├─ fuentes/
├─ proceso/plantillas/
├─ seguimiento/
├─ candidaturas/
├─ presentacion-espontanea/
└─ certificados-formacion/
```

Las candidaturas son expedientes operativos y no llevan versionado documental
trazable. Las fuentes y plantillas sí mantienen su versión en frontmatter. El
histórico es global y conserva documentos sustituidos junto con su ruta de
procedencia.

## Uso operativo de Job-up

### Cómo empezar y entradas disponibles

Abre este README, identifica el tipo de trabajo y usa la skill correspondiente:

- `job-up-inicia-sesion`: abre explícitamente un bloque Job-up y gestiona su ciclo PCS.
- `job-up-candidatura-oferta`: prepara una candidatura a partir de una oferta.
- `job-up-genera-cv-empresa`: prepara una presentación espontánea para una empresa concreta.

Una oferta puede entrar mediante cualquiera de estas modalidades:

1. URL accesible públicamente.
2. Fichero Markdown de estructura libre aportado por la persona usuaria.
3. Texto de la oferta copiado y pegado en el chat.

Si la URL no es accesible, puede utilizarse cualquiera de las otras dos
modalidades. Si no existe una sesión Job-up abierta, la skill de oferta pedirá
permiso antes de invocar `job-up-inicia-sesion`; la entrega de una oferta no
autoriza por sí sola la creación de una sesión PCS.

### Mapa de carpetas y enlaces canónicos

- [Fuentes](fuentes/): [datos core](fuentes/datos-core-busqueda.md) y [datos privados de candidatura](fuentes/datos-privados-candidatura.md).
- [Proceso y plantillas](proceso/plantillas/): [análisis de oferta](proceso/plantillas/TEMPLATE_ANALISIS_OFERTA.md), [ficha de candidatura](proceso/plantillas/TEMPLATE_CANDIDATURA.md), [guion de adaptación](proceso/plantillas/TEMPLATE_GUION_ADAPTACION_CV.md) y [veredicto final](proceso/plantillas/TEMPLATE_VEREDICTO_FINAL_CV.md).
- [Seguimiento](seguimiento/seguimiento-candidaturas.md): estados, fechas, documentos y bloqueos.
- [Candidaturas](candidaturas/): expedientes concretos y sus artefactos.
- [Presentación espontánea](presentacion-espontanea/README.md): materiales no vinculados a una oferta.
- [Playbook de candidatura por oferta](../../docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA_v1_0_0.md): procedimiento metodológico canónico vigente hasta su migración al nombre estable.

### Flujo operativo

1. Clasificar la petición y registrar la procedencia de la oferta.
2. Resolver una única sesión Job-up abierta; ante ambigüedad, pedir elección.
3. Analizar la oferta y seleccionar un perfil, evidencias y logros respaldados.
4. Aplicar la compuerta de privacidad antes de consultar datos privados.
5. Preparar los documentos y completar el veredicto final.
6. Actualizar la ficha y el seguimiento de la candidatura.
7. Entregar el paquete en `pendiente_de_aprobacion`, sin enviar ni contactar.

### Matriz de artefactos

| Artefacto | Candidatura por oferta | Presentación espontánea |
| --- | --- | --- |
| Análisis de oferta | Obligatorio | No aplica |
| Ficha de candidatura | Obligatoria | Según destinatario concreto |
| Guion de adaptación | Obligatorio | Selección factual general |
| Veredicto final | Obligatorio antes de aprobar | Revisión proporcional |
| CV DOCX y PDF | Obligatorios | Base obligatoria |
| CV LaTeX | Previsto según el proceso | Previsto para futuras versiones |
| Carta DOCX y PDF | Según el canal | Solo si la solicita el destinatario |
| Email de presentación | Según el canal | Base obligatoria |

### Trazabilidad, PCS e histórico

El [seguimiento de candidaturas](seguimiento/seguimiento-candidaturas.md)
refleja el estado vivo y los documentos asociados. PCS conserva las sesiones,
decisiones, acciones y el estado operativo; Job-up no duplica ese ciclo en este
README. La [sesión de origen](../../.pcs/sesiones/sesion-20260721-1651-tension-carrera-ai-y-busqueda-de-trabajo.md), la [decisión de crear la rama](../../.pcs/decisiones/DEC-20260721-1651-001-crear-rama-operativa-busqueda-empleo.md) y la [acción de activación](../../.pcs/acciones/ACC-20260721-1651-001-activar-rama-operativa-busqueda-empleo-fase-1.md) documentan la trazabilidad inicial.

`INICIO_SESION_WORK.md` ya no es una entrada operativa paralela. Su contenido
histórico se conserva en [historico](../../historico/boveda-entrevista-profesional/busqueda-empleo/INICIO_SESION_WORK.md); la orientación conceptual queda aquí y el ciclo exacto de sesiones corresponde a `job-up-inicia-sesion`.
