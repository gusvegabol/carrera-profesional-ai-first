# Diseño — proceso de CV adaptados por oferta

**Fecha:** 2026-07-21  
**Estado:** aprobado para revisión de la especificación

## Propósito

Definir una rama operativa dentro de Carrera AI que permita convertir una oferta de empleo en un CV y una carta de presentación adaptados, revisables y trazables. La rama reduce el tiempo de candidatura sin modificar la investigación metodológica de entrevista.

## Límites de alcance

- La rama consume [[datos-core-busqueda]] como fuente factual profesional.
- No modifica el SPEC, los playbooks ni los criterios de validación de la entrevista.
- No infiere responsabilidades, titulaciones, niveles de idioma, tecnologías vigentes ni métricas que no estén confirmadas.
- Las candidaturas nunca se envían sin aprobación humana por lote.
- Los datos personales de contacto se mantienen fuera de la matriz profesional.

## Arquitectura por fases

### Fase 1 — Preparación desde texto de oferta

La persona responsable pega el texto completo de una oferta. El proceso extrae puesto, empresa, salario, modalidad, zona geográfica, jornada, contrato, requisitos y funciones. Clasifica el encaje funcional como fuerte, parcial o descartado; solo se descarta automáticamente cuando no encaja con ninguno de los tres perfiles.

Para cada oferta con encaje, propone un perfil principal, uno secundario, de tres a cinco logros pertinentes y las afirmaciones que deben evitarse. Genera un CV y una carta de presentación en DOCX editable y PDF. No inicia ni envía una candidatura en esta fase.

### Fase 2 — Asistencia en Chrome sobre páginas abiertas

La persona responsable abre un portal o búsqueda en Chrome. ChatGPT Work analiza la página activa, activa filtros si el portal los ofrece o evalúa las ofertas visibles si no existen. Construye una lista de aprobación por lote y, solo después de aprobarla, puede completar formularios y adjuntar los documentos correspondientes.

Si el portal muestra un CAPTCHA, una pregunta abierta, una evaluación, un campo obligatorio desconocido, una contradicción factual o un requisito no cubierto, esa candidatura se detiene y queda marcada para revisión.

### Fase 3 — Acceso a portales priorizados

Una skill o conector, sujeto a diseño y validación posteriores, podrá consultar los portales de empleo seleccionados sin que la persona responsable los abra uno a uno. Conserva la misma lógica de encaje, aprobación por lote, límites de datos y registro que las fases anteriores.

## Datos y artefactos

| Artefacto | Responsabilidad |
| --- | --- |
| `boveda-entrevista-profesional/busqueda-empleo/datos-core-busqueda.md` | Fuente factual de perfiles, logros, trayectoria, competencias y formación |
| `boveda-entrevista-profesional/busqueda-empleo/datos-privados-candidatura.md` | Datos de contacto y otros datos necesarios para formularios; acceso limitado al momento de preparar o enviar una candidatura |
| `boveda-entrevista-profesional/busqueda-empleo/seguimiento-candidaturas.md` | Registro de ofertas analizadas, duplicados, estados, fechas, enlaces, documentos usados y bloqueos |
| Carpeta por candidatura | CV DOCX, CV PDF, carta DOCX y carta PDF vinculados a la entrada de seguimiento |

## Flujo operativo

1. Recibir el texto de la oferta o analizar la página activa en Chrome.
2. Extraer los campos relevantes y contrastarlos con los tres perfiles de la matriz.
3. Mostrar el nivel de encaje y las condiciones visibles: tipo de oferta, salario, modalidad, zona geográfica, jornada y contrato.
4. Seleccionar evidencia factual y generar los documentos adaptados.
5. Registrar la oferta como preparada, pendiente de aprobación, aprobada, enviada, detenida, duplicada o fallida.
6. Agrupar candidaturas en un lote. La persona responsable aprueba el lote antes de cualquier envío.
7. Detener y solicitar revisión humana ante información incompleta, inconsistente o no confirmada.

## Reglas de selección

- Los tres perfiles permanecen disponibles y ninguno tiene prioridad permanente.
- Las ofertas con encaje parcial se muestran, debidamente marcadas.
- La falta de encaje con los tres perfiles es el único descarte automático inicial.
- Salario, modalidad, zona, jornada y contrato se presentan para decisión humana; no se usan como exclusión automática mientras no se adopte otra regla.
- El registro de seguimiento evita duplicar candidaturas y no permite reenviar una oferta sin una nueva aprobación humana.

## Privacidad y controles

- La matriz profesional no almacena datos de contacto ni credenciales.
- La ficha privada solo se usa cuando una candidatura aprobada necesita completar un formulario.
- La salida externa se limita a las ofertas incluidas en un lote aprobado.
- No se sortean CAPTCHA, evaluaciones o mecanismos de seguridad.
- Cada detención deja un motivo visible en el seguimiento para que la persona responsable decida el siguiente paso.

## Validación

La fase 1 se considerará lista cuando una oferta pegada permita producir un CV y una carta en DOCX y PDF, con perfil, logros y afirmaciones rastreables hasta [[datos-core-busqueda]]. También deberá crear una entrada de seguimiento sin duplicar otra candidatura.

Las fases 2 y 3 no se activarán hasta verificar la capacidad real de ChatGPT Work en Chrome o del conector elegido, respectivamente, y hasta confirmar que el proceso conserva la aprobación humana por lote.

## Fuera de alcance

- Rediseñar la metodología de entrevista.
- Alterar el SPEC o los playbooks por necesidades de candidatura.
- Enviar candidaturas sin aprobación humana.
- Declarar competencias o resultados no evidenciados.
- Resolver automáticamente preguntas abiertas, evaluaciones o requisitos que necesiten criterio humano.
