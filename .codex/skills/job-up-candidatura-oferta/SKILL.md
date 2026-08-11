---
name: job-up-candidatura-oferta
description: Use when the user explicitly provides a job offer by accessible URL, Markdown file, or pasted text and wants to prepare a traceable Job-up application.
---

# Job-up: candidatura por oferta

## Propósito y límites

Esta skill es el punto de entrada de una candidatura basada en una oferta. Su
responsabilidad es orquestar el flujo documental, conservar la trazabilidad,
comprobar las salidas de cada fase y detenerse ante cualquier bloqueo. Las
reglas editoriales, técnicas y de evaluación pertenecen a los playbooks
canónicos; esta skill no las duplica.

No inicia ni cierra sesiones PCS por sí misma. Si no existe una única sesión
Job-up abierta, debe pedir confirmación explícita para invocar
`job-up-inicia-sesion` y volver a comprobar la sesión antes de continuar.

No inicia sesión en portales, no navega por canales externos, no completa
formularios, no usa credenciales, no presta consentimientos y no realiza
envíos. La presentación externa queda fuera del flujo documental y siempre la
realiza la persona responsable.

## Entradas admitidas

Acepta exactamente una de estas entradas:

1. URL pública accesible.
2. Fichero Markdown aportado por la persona usuaria.
3. Texto completo de la oferta pegado en la conversación.

Si la URL no es accesible, solicita el fichero o el texto alternativo. No
convierte una oferta en autorización para crear una sesión ni para usar datos
privados.

## Flujo canónico

La skill debe seguir este orden y registrar la salida de cada fase:

```text
oferta
→ análisis de oferta
→ candidatura
→ rama CV: guion → contenido → composición → veredicto
→ rama carta, cuando la candidatura la requiera:
  guion → contenido → composición → veredicto
→ candidatura documentalmente completa
```

### 1. Oferta y sesión

- Registrar procedencia, fecha y texto completo de la oferta.
- Aplicar `PLAYBOOK_ANALISIS_OFERTA.md` y crear el análisis con
  `TEMPLATE_ANALISIS_OFERTA.md`.
- Resolver una única sesión Job-up siguiendo `job-up-inicia-sesion`; ante
  varias sesiones o una selección incierta, detenerse y pedir elección humana.
- Crear la ficha con `TEMPLATE_CANDIDATURA.md` y aplicar
  `PLAYBOOK_CANDIDATURA.md` y `PLAYBOOK_CANDIDATURA_POR_OFERTA.md`.
- No consultar datos privados hasta comprobar autorización escrita específica
  para la misma candidatura.

### 2. Rama CV

Seguir los contratos en este orden, sin copiar su lógica dentro de la skill:

1. `PLAYBOOK_GUION_ADAPTACION_CV.md` con `TEMPLATE_GUION_ADAPTACION_CV.md`.
2. `PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA.md` con
   `TEMPLATE_DATOS_GENERACION_CV.json` **schema 1.2**.
3. `PLAYBOOK_COMPONER_CV.md`, que produce únicamente `cv.docx`, `cv.pdf` y
   `cv.tex` mediante el compositor vigente.
4. Revisión humana y `PLAYBOOK_VEREDICTO_FINAL_CV.md`.

La skill solo puede avanzar cuando el gate de la fase anterior está aprobado
y no existe una contradicción factual o de privacidad.

### 3. Rama carta

Cuando la candidatura requiera carta, seguirla como rama independiente:

1. `PLAYBOOK_GUION_CARTA_PRESENTACION.md` con
   `TEMPLATE_GUION_CARTA_PRESENTACION.md`.
2. `PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION.md` con
   `TEMPLATE_CONTENIDO_CARTA_PRESENTACION.md`.
3. `PLAYBOOK_COMPONER_CARTA_PRESENTACION.md` con
   `TEMPLATE_COMPOSICION_CARTA_PRESENTACION.md`, produciendo
   `carta-presentacion.docx` y `carta-presentacion.pdf`.
4. Revisión humana y `PLAYBOOK_VEREDICTO_FINAL_CARTA.md`.

La carta no consume el contrato JSON CV-only ni se genera en la misma fase que
el CV. Cada rama conserva su contenido, composición y veredicto propios.

## Resolución previa y transiciones

Antes de cerrar `GATE-CANDIDATURA-GUION`, el playbook de candidatura debe
resolver cualquier requisito relevante de la oferta que no tenga evidencia
factual o preferencia reutilizable suficiente. Se distingue entre hechos
reutilizables (por ejemplo, `vehículo propio`), preferencias/disponibilidad
reutilizables (por ejemplo, movilidad territorial) y decisiones específicas de
la oferta (por ejemplo, aceptar un desplazamiento concreto). La ausencia de un
dato necesario se pregunta una sola vez antes del gate y se registra en la
fuente que corresponda.

Tras identificar la empresa, el contexto corporativo útil se localiza o se
solicita antes de cerrar decisiones que puedan verse afectadas. Ese contexto
sirve para interpretar la oferta y ajustar el lenguaje; nunca se convierte en
evidencia profesional ni en afinidad personal inventada.

Cuando un gate aprobado tiene una siguiente acción determinista, no falta
ningún dato ni decisión, no se requiere revisión humana y no hay acción
irreversible, la skill continúa automáticamente con el playbook siguiente. Solo
se detiene ante una decisión humana real, dato o autorización faltante, revisión
humana, bloqueo técnico o acción irreversible.

La selección efectiva de la siguiente acción se representa en
`scripts/job-up/orquestar_transiciones.py`. Para la rama de carta, la tabla
operativa es:

| Estado comprobado | Acción de la orquestación |
| --- | --- |
| `GATE-CONTENIDO-CARTA-COMPOSICION = aprobado` y carta aún no compuesta | Ejecutar `PLAYBOOK_COMPONER_CARTA_PRESENTACION` |
| Carta compuesta y `GATE-CARTA-REVISION-HUMANA = pendiente` | Esperar decisión humana |
| `GATE-CARTA-REVISION-HUMANA = aprobado` y `GATE-VEREDICTO-CARTA = pendiente` | Ejecutar `PLAYBOOK_VEREDICTO_FINAL_CARTA` inmediatamente |
| `GATE-VEREDICTO-CARTA = aprobado`, CV aprobado y `presentada: false` | Cerrar como `documentalmente_completa` |

Por tanto, anunciar «siguiente paso: ejecutar el veredicto» y detenerse cuando
la revisión humana de la carta ya está aprobada es una pausa inválida: no hay
una nueva decisión, dato, revisión ni autorización que solicitar.

## Contratos y plantillas operativas

La fuente de cada fase debe localizarse en estas rutas canónicas:

- Playbooks: `docs/metodologia/playbooks/`.
- Templates: `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/`.

Las referencias operativas mínimas son:

```text
docs/metodologia/playbooks/PLAYBOOK_CANDIDATURA_POR_OFERTA.md
docs/metodologia/playbooks/PLAYBOOK_GUION_ADAPTACION_CV.md
docs/metodologia/playbooks/PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA.md
docs/metodologia/playbooks/PLAYBOOK_COMPONER_CV.md
docs/metodologia/playbooks/PLAYBOOK_VEREDICTO_FINAL_CV.md
docs/metodologia/playbooks/PLAYBOOK_GUION_CARTA_PRESENTACION.md
docs/metodologia/playbooks/PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION.md
docs/metodologia/playbooks/PLAYBOOK_COMPONER_CARTA_PRESENTACION.md
docs/metodologia/playbooks/PLAYBOOK_VEREDICTO_FINAL_CARTA.md
```

Los templates correspondientes son:

```text
TEMPLATE_ANALISIS_OFERTA.md
TEMPLATE_CANDIDATURA.md
TEMPLATE_GUION_ADAPTACION_CV.md
TEMPLATE_DATOS_GENERACION_CV.json
TEMPLATE_GUION_CARTA_PRESENTACION.md
TEMPLATE_CONTENIDO_CARTA_PRESENTACION.md
TEMPLATE_COMPOSICION_CARTA_PRESENTACION.md
TEMPLATE_VEREDICTO_FINAL_CV.md
TEMPLATE_VEREDICTO_FINAL_CARTA.md
```

El contrato histórico de generación acoplada no forma parte de esta ruta
operativa. El CV utiliza exclusivamente `TEMPLATE_DATOS_GENERACION_CV.json`
1.2 y la carta utiliza sus templates y playbooks independientes.

## Política de fotografía

La política se hereda de `GUIA_FORMATO_CV_Y_CARTA.md` y de los playbooks
correspondientes:

- CV: fotografía incluida por defecto, salvo exclusión humana expresa.
- La ausencia de mención de fotografía no genera pregunta, pendiente ni bloqueo:
  el CV adopta el valor `incluir` por defecto.
- Carta: la fotografía no se incluye por defecto; solo puede incorporarse
  mediante una decisión o configuración humana específica para esa carta.

La autorización de disponer de una fotografía no autoriza a mostrarla en todos
los artefactos. La fotografía del CV no se propaga conceptualmente a la carta.

## Cierre documental

La candidatura alcanza `documentalmente_completa` cuando se cumplen ambas
condiciones aplicables:

```text
CV con veredicto final aprobado
+ carta con veredicto final aprobado cuando sea requerida
= candidatura documentalmente completa
```

El cierre documental no cambia `presentada: false`. La presentación, los
formularios y cualquier acción externa quedan fuera del flujo y requieren una
decisión posterior de la persona responsable.

## Detenciones obligatorias

Detenerse y registrar el bloqueo cuando ocurra cualquiera de estas
condiciones:

- oferta incompleta o URL inaccesible sin alternativa;
- sesión Job-up ausente, múltiple o ambiguamente seleccionable;
- autorización privada ausente, ambigua o insuficiente;
- contradicción factual no resuelta;
- gate humano pendiente, bloqueado o con corrección obligatoria;
- contrato, template, script o salida requerida inaccesible;
- error técnico del compositor, conversor o verificador;
- intento de convertir el cierre documental en una presentación externa.

No inventar datos, no reutilizar autorizaciones de otra candidatura y no
seleccionar sesiones por recencia o similitud.

## Lista de control de salida

- [ ] La oferta completa y su procedencia están registradas.
- [ ] Existe una única sesión Job-up válida.
- [ ] El análisis y la candidatura están completos y trazables.
- [ ] La rama CV tiene contenido, composición, revisión y veredicto aprobados.
- [ ] La rama carta tiene contenido, composición, revisión y veredicto aprobados cuando procede.
- [ ] La candidatura está `documentalmente_completa` cuando corresponda.
- [ ] `presentada: false` permanece sin cambios.
- [ ] No se inició sesión externa ni se enviaron documentos.
