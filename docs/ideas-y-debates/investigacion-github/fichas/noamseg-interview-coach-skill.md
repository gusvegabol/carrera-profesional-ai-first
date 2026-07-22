# Ficha técnica: `noamseg/interview-coach-skill`

## Identificación

**Repositorio:** `noamseg/interview-coach-skill`  
**URL:** <https://github.com/noamseg/interview-coach-skill>  
**Fecha de revisión:** 2026-07-20  
**Última actividad observada:** no comprobada con fecha exacta en esta revisión; el repositorio muestra 75 commits y una hoja de ruta con las versiones v1, v2 y v3 como entregadas.  
**Licencia:** MIT; exige conservar el aviso de copyright y la licencia en las copias o partes sustanciales.  
**Área funcional:** entrevista profesional, storybank, continuidad, evaluación y generación de salidas de búsqueda de empleo.  
**Objeto estudiado:** ideas, patrones y modelos documentales; no código integrado.  
**Nivel de evidencia:** inspección técnica documental; experimento todavía no ejecutado.  
**Estado de la ficha:** revisada para calibración

## Pregunta de investigación

¿Qué patrones de entrevista, organización de historias, continuidad y
recomendación del siguiente paso podrían reforzar Carrera AI-First sin
convertirla en un sistema de preparación de entrevistas ni introducir una
arquitectura compleja?

## Problema que resuelve

El repositorio ofrece un coach de entrevistas basado en archivos de
instrucciones para Claude Code, Codex u otros entornos con acceso al sistema de
archivos. Cubre preparación, práctica, análisis de transcripciones, gestión de
historias, seguimiento de resultados y otras etapas de búsqueda de empleo.

Su propuesta combina comandos especializados, puntuación multidimensional,
diagnóstico de causas y un estado persistente en `coaching_state.md`.

Fuente: [README del repositorio](https://github.com/noamseg/interview-coach-skill#readme).

## Relación con Carrera AI-First

La relación más útil no está en copiar el coach completo, sino en estudiar
patrones laterales que pueden complementar la cobertura profesional y la
inmersión:

- organización de historias profesionales en un *storybank*;
- extracción de temas narrativos comunes;
- trazabilidad de patrones, evidencias y resultados a lo largo del tiempo;
- recomendación de un siguiente paso según el estado actual;
- uso de un archivo persistente para continuidad entre sesiones;
- separación entre puntuación, diagnóstico y ejercicio posterior.

El repositorio trabaja principalmente con preparación para entrevistas y
búsqueda activa de empleo. Carrera AI-First tiene un alcance anterior y más
amplio: reconstruir la trayectoria profesional completa antes de generar
narrativas u opciones.

## Stack y arquitectura

**Lenguajes:** Markdown y archivos de instrucciones; no se ha identificado en
la revisión una aplicación tradicional con backend propio.  
**Frameworks y librerías principales:** no se ha comprobado un framework de
ejecución; el núcleo se organiza como una skill para Claude Code/Codex.  
**Servicios o proveedores externos:** requiere un entorno compatible con la
skill y, según el modo de uso descrito, un plan de Claude o ChatGPT de pago.  
**Infraestructura necesaria:** sistema de archivos local y un archivo de estado
persistentemente actualizado.  
**Estructura arquitectónica observada:** un `SKILL.md` central, un directorio
`references/commands/` con flujos por comando y módulos transversales para
rúbricas, storybank, calibración, procesamiento de transcripciones y ejemplos.

Fuentes: [estructura del repositorio](https://github.com/noamseg/interview-coach-skill#repository-structure) y
[SKILL.md](https://raw.githubusercontent.com/noamseg/interview-coach-skill/main/SKILL.md).

## Componentes potencialmente reutilizables

| Tipo | Componente o patrón | Ubicación | Qué aporta | ¿Separable? |
| --- | --- | --- | --- | --- |
| Modelo de datos | Estado persistente de continuidad | `coaching_state.md` y `references/coaching-state-schema.md` | Conserva progreso, historias, patrones y pendientes entre sesiones. | parcial |
| Flujo | Triage antes de aplicar una plantilla | `SKILL.md` y referencias de comandos | Permite adaptar el siguiente paso a lo que revela la persona. | sí |
| Modelo | Storybank con ajuste de uso | `references/storybank-guide.md` y `references/story-mapping-engine.md` | Organiza historias, encaje, frescura, reutilización y huecos. | parcial |
| Patrón | Extracción de identidad narrativa | `README.md` y referencias de historias | Busca temas comunes sin reducir toda la trayectoria a una sola etiqueta. | sí |
| Flujo | Recomendación prescriptiva del siguiente paso | `SKILL.md` y protocolos de inicio/cierre | Convierte el estado actual en una orientación operativa concreta. | sí |
| Patrón | Etiquetado de confianza y exigencia de evidencia | `SKILL.md` y referencias de análisis | Limita afirmaciones no sustentadas y hace visible la incertidumbre. | sí |
| Arquitectura documental | Comandos especializados y módulos transversales | `references/commands/` y archivos de referencia | Separa flujos específicos de reglas compartidas. | sí, como referencia |

## Modelo de datos, prompts y flujos

### Modelo de datos

El elemento central es `coaching_state.md`, que funciona como memoria de
trabajo persistente. El README indica que reúne storybank, puntuaciones,
patrones, progreso de ejercicios, ciclos de entrevistas, inteligencia de
entrevistas y calibración.

Este patrón puede inspirar una continuidad ligera, pero no debe sustituir los
artefactos y checkpoints que Carrera AI-First ya utiliza para separar estado,
evidencia, límites y validación humana.

### Prompts o instrucciones

`SKILL.md` establece una jerarquía de prioridades: estado de sesión, triage,
evidencia, secuenciación de una pregunta cada vez y cumplimiento de esquemas.
Las instrucciones específicas se cargan desde referencias por comando.

El patrón más transferible es la separación entre reglas globales, módulos
transversales y protocolos específicos, no la adopción literal de sus rúbricas
de entrevista.

### Flujo de uso

El sistema parte de un `kickoff`, carga o crea el estado, ejecuta comandos
especializados y recomienda un siguiente paso según el estado. Guarda cambios
durante los flujos relevantes y al terminar la sesión.

Para Carrera AI-First, la adaptación tendría que empezar por el mapa de
cobertura y las zonas pendientes, no por un perfil de búsqueda de empleo ni por
la preparación de una candidatura.

## Diferencias y límites frente a Carrera AI-First

- Está centrado en el ciclo de búsqueda y entrevista laboral, no en la
  reconstrucción completa de la trayectoria.
- Su sistema de puntuación y diagnóstico podría introducir una experiencia
  evaluativa que no corresponde al objetivo de cobertura profesional.
- El `coaching_state.md` es una memoria propia del producto y no equivale al
  estado PCS ni a los artefactos canónicos del piloto.
- La riqueza de sus 23 comandos y módulos excede claramente lo necesario para
  validar la MVP de Carrera AI-First.
- Algunas funcionalidades, como adecuación a puestos, optimización de CV o
  inteligencia de empresas, pertenecen a fases distintas del producto local.

## Evaluación

| Criterio | Puntuación | Justificación |
| --- | ---: | --- |
| Encaje funcional | 4/5 | Aporta patrones cercanos a entrevista, evidencia narrativa y continuidad, aunque su objetivo principal es distinto. |
| Reutilización real | 3/5 | La reutilización más clara es conceptual y documental; la separación de código no es el objetivo principal del repositorio. |
| Calidad arquitectónica | 4/5 | Presenta una separación visible entre skill central, comandos, módulos transversales y ejemplos. |
| Madurez | 4/5 | Muestra documentación amplia, 75 commits y una hoja de ruta por versiones; no se ha realizado una auditoría de pruebas ni de todas las referencias. |
| Dependencias | 4/5 | El modelo basado en archivos reduce infraestructura, aunque depende del entorno de ejecución y del proveedor de modelo. |
| Licencia | 5/5 | La licencia MIT es clara para estudiar y adaptar, conservando sus avisos. |
| Coste de integración | 4/5 | Un experimento conceptual o documental es barato; integrar su sistema completo tendría un coste alto. |
| Riesgo de desvío | 3/5 | La amplitud del producto puede arrastrar la MVP hacia coaching de entrevistas, scoring y matching. |
| Valor de aprendizaje | 5/5 | Es especialmente útil para estudiar continuidad, storybank, triage y diseño de flujos. |

## Riesgos

- **Dependencias:** el funcionamiento presupone un entorno compatible con las
  instrucciones y acceso a un modelo; debe comprobarse qué partes son
  realmente portables.
- **Calidad o mantenimiento:** la documentación es extensa, pero esta ficha no
  ha auditado todavía cobertura de pruebas, consistencia interna ni resultados
  empíricos.
- **Licencia:** el uso exige conservar el aviso de copyright y la licencia MIT.
- **Privacidad:** el sistema está diseñado para almacenar CV, transcripciones,
  historias y resultados; Carrera AI-First tendría que aplicar su propio
  contrato de minimización y conservación.
- **Desvío de la MVP:** su amplitud puede incentivar una plataforma de coaching
  de búsqueda de empleo antes de validar la entrevista de cobertura.

## Experimento mínimo propuesto

**Hipótesis:** el patrón de `storybank` y la recomendación del siguiente paso
pueden complementar la cobertura profesional si se subordinan al mapa,
evidencias y límites de Carrera AI-First.

**Alcance:** comparar sus estructuras documentales de historias, continuidad y
triage con los artefactos actuales de cobertura profesional.

**Exclusiones:** no instalar el repositorio, no renombrar `SKILL.md`, no
ejecutar el coach completo, no usar datos profesionales reales y no adoptar sus
rúbricas de puntuación.

**Datos de prueba:** un caso sintético con dos episodios profesionales, una
transición y una pregunta pendiente.

**Procedimiento:**

1. Extraer de la documentación del repositorio los campos y estados mínimos de
   `coaching_state.md`, storybank y recomendación del siguiente paso.
2. Mapearlos contra el mapa de cobertura, checkpoint, inmersión y ficha de
   competencia de Carrera AI-First.
3. Identificar qué patrón puede incorporarse sin duplicar artefactos ni crear
   una capa de scoring.

**Resultado observable:** una tabla de correspondencias con tres salidas:
   adoptar como patrón, mantener separado o descartar.

**Coste estimado:** bajo; documental y comparativo.

## Resultado del experimento

**Resultado:** pendiente.  
**Evidencia:** pendiente de crear `experimentos/EXP-001-entrevista-y-storybank/`.  
**Problemas encontrados:** la documentación disponible permite formular el
experimento, pero no demostrar todavía la separabilidad real de los componentes.  
**Aprendizaje:** la ficha confirma que el repositorio es más valioso como
referencia de patrones que como candidato inmediato a integración completa.

## Decisión preliminar

**Decisión:** estudiar como referencia.

**Justificación:** presenta patrones relevantes para continuidad, storybank,
triage y recomendación de próximos pasos, pero su orientación a coaching de
entrevistas y su amplitud hacen prematura una integración directa.

La decisión no autoriza probar el repositorio ni incorporar código. Solo
autoriza conservar y comparar sus patrones como aprendizaje para el diseño
local.

**Qué podría incorporarse:** un patrón ligero de registro de historias, una
regla de triage contextual y una recomendación de siguiente paso basada en el
estado de cobertura.

**Qué no debe incorporarse:** su sistema completo de 23 comandos, su scoring
multidimensional, el matching de puestos y la memoria como sustituto de PCS o
de los artefactos del piloto.

**Siguiente paso:** ejecutar el experimento documental `EXP-001` y revisar si
algún campo del storybank aporta valor que no esté cubierto por los artefactos
actuales.

## Trazabilidad

- Documento general: [`INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md`](../INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md).
- Flujo de investigación: [`FLUJO_INVESTIGACION_GITHUB.md`](../FLUJO_INVESTIGACION_GITHUB.md).
- Sesión PCS relacionada: `sesion-20260720-1242-investigacion-github-carrera-ai-first`.
- Experimento relacionado: `experimentos/EXP-001-entrevista-y-storybank/`.
- Decisión PCS relacionada: no aplica; esta es una decisión preliminar de investigación.

## Revisión final

- [x] La licencia se ha comprobado en la fuente del repositorio.
- [x] Las afirmaciones técnicas principales tienen una referencia o evidencia.
- [x] Se han separado hechos, inferencias y recomendaciones.
- [x] Se ha distinguido adoptar una idea, probar un componente e integrar código.
- [x] Se ha evaluado el riesgo de desvío de la MVP.
- [x] No se han tratado resultados preliminares como decisiones formales.

## Fuentes consultadas

- [Repositorio en GitHub](https://github.com/noamseg/interview-coach-skill).
- [README](https://github.com/noamseg/interview-coach-skill#readme).
- [`SKILL.md`](https://raw.githubusercontent.com/noamseg/interview-coach-skill/main/SKILL.md).
- [`LICENSE`](https://raw.githubusercontent.com/noamseg/interview-coach-skill/main/LICENSE).
- [`VERSIONS.md`](https://raw.githubusercontent.com/noamseg/interview-coach-skill/main/VERSIONS.md).
