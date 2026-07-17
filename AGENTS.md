# AGENTS — carrera-profesional-ai-first

## Propósito

Este repositorio corresponde al host `carrera-ai`.

Su propósito local es desarrollar y revisar el enfoque de entrevista que permita construir un Perfil Profesional Accionable a partir de la trayectoria profesional completa de una persona.

Flujo operativo vigente: flujo PCS 2.0 (`Usuario -> Work -> Usuario`).

## Relación con PCS

Ruta del Core activo:

`C:/Users/gusve/Documents/Apps/project-continuity-system`

El Core actúa como fuente normativa común. Este repositorio conserva su contexto local y su memoria operativa vive en `./.pcs/`.

Cuando una tarea afecte gobernanza PCS, sesiones, acciones, decisiones, estado, hosts o comandos `pcs::`, el agente debe consultar como referencia viva:

`C:/Users/gusve/Documents/Apps/project-continuity-system/core/CONTRATO_CANONICO_GOBERNANZA_HOSTS.md`

## Qué consultar primero

Al aterrizar en este host, el agente debería consultar primero:

- `README.md`
- `AGENTS.md`
- `./.pcs/estado/estado-actual.md`, si existe
- `./docs/AGENTS.md`
- `./docs/VERSIONADO_CARRERA_AI.md` y `./docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md`, cuando la tarea afecte al versionado funcional
- `./docs/DOCUMENTO_SPEC_CARRERA_AI.md`
- `./docs/Núcleo Metodológico del Playbook/idea-central.md`
- `./docs/Ideas debate - como afrontar entrevista cobertura profesional/05_Evaluacion_experta_y_recomendacion_de_enfoque.md`, cuando la tarea afecte al debate metodológico actual

## Regla universal de ortografía española

Cuando el agente redacte o modifique documentación en español, debe conservar la ortografía española, incluidas tildes, diéresis, eñes y signos de apertura de interrogación y exclamación cuando correspondan.

Antes de dar por terminada cualquier documentación redactada en español, debe revisarla explícitamente desde el punto de vista ortográfico y corregir los errores detectados.

## Rehidratación mínima obligatoria

Si el usuario declara el host o pide retomar trabajo desde contexto general, el agente debe:

1. resolver el alias `carrera-ai` en `C:/Users/gusve/Documents/Apps/project-continuity-system/hosts/hosts.yaml`;
2. consultar `./.pcs/estado/estado-actual.md`, si existe;
3. revisar `./.pcs/sesiones/` abiertas o útiles solo si el estado no basta para responder;
4. devolver un resumen breve de situación, acciones abiertas relevantes, decisiones vigentes condicionantes, riesgos y siguiente gesto recomendado;
5. no abrir ni actualizar una sesión PCS solo por esa declaración.

## Consulta documental proporcional

Para preguntas metodológicas o de debate, priorizar en este orden:

1. `./docs/DOCUMENTO_SPEC_CARRERA_AI.md` para objetivos y límites funcionales;
2. `./docs/Núcleo Metodológico del Playbook/` para fundamentos y marcos metodológicos;
3. `./docs/Ideas debate - como afrontar entrevista cobertura profesional/` para propuestas, evaluación y presentación del enfoque.

Si existe contradicción, debe señalarse expresamente y prevalece la fuente de mayor autoridad dentro de ese orden.

## Comandos PCS en Work

Si una petición comienza por `pcs::`, el agente debe encaminarla sin reproducir sus flujos en este documento. Debe consultar, en este orden:

1. `C:/Users/gusve/Documents/Apps/project-continuity-system/prompts/work-comandos/INDEX_COMANDOS.md`
2. `C:/Users/gusve/Documents/Apps/project-continuity-system/prompts/work-comandos/COMANDOS_GOBERNANZA.md`
3. el documento de flujo específico indicado por el índice

Si el comando no figura en el índice o el alias indicado no existe en `hosts/hosts.yaml`, el agente debe avisar y detenerse sin realizar cambios.

## Regla de degradación

Si faltan artefactos locales, el agente debe degradar en este orden:

1. intentar `./.pcs/estado/estado-actual.md`;
2. si falta, revisar sesiones abiertas o útiles en `./.pcs/sesiones/`;
3. si falta `./.pcs/`, declarar explícitamente que no existe memoria operativa local suficiente;
4. si falta el Core activo o `hosts/hosts.yaml`, declarar el límite de resolución de alias y no inventar contexto.

## Límites locales

- No tratar una sesión como estado vivo.
- No inventar contexto funcional no documentado.
- No modificar `./docs/DOCUMENTO_SPEC_CARRERA_AI.md` por inferencia no verificada.
- No convertir una recomendación metodológica en decisión formal sin soporte documental y sin la capa PCS correspondiente.
- No editar `hosts/hosts.yaml` fuera del flujo guiado del Core.
- No duplicar dentro del host la gobernanza universal del PCS.
- No usar `./.tmp/` como fuente de verdad; solo puede leerse o escribirse cuando el usuario autorice de forma explícita una subruta concreta.

## Regla de detención

El agente debe detenerse y pedir aclaración si detecta:

- contradicción entre fuentes que gobiernan la misma afirmación;
- ambigüedad entre metodología, propuesta, decisión y estado PCS;
- necesidad de modificar gobernanza común del Core desde el host sin instrucción explícita;
- falta de memoria local suficiente para reconstruir estado sin inventarlo;
- petición de cambiar el nombre de `.pcs` o de editar `hosts/hosts.yaml` al margen del flujo guiado.
