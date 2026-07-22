# Ficha técnica: `FareedKhan-dev/langgraph-long-memory`

## Identificación

**Repositorio:** `FareedKhan-dev/langgraph-long-memory`  
**URL:** <https://github.com/FareedKhan-dev/langgraph-long-memory>  
**Fecha de revisión:** 2026-07-20  
**Última actividad observada:** no comprobada con fecha exacta; el repositorio muestra 2 commits.  
**Licencia:** MIT.  
**Área funcional:** memoria de corto y largo plazo.  
**Objeto estudiado:** modelo conceptual y notebook de memoria persistente.  
**Nivel de evidencia:** inspección técnica documental; notebook no ejecutado.  
**Estado de la ficha:** revisada

## Pregunta de investigación

¿Qué separación entre memoria de sesión y memoria entre sesiones puede ayudar a
razonar sobre continuidad sin duplicar la memoria documental y PCS que ya usa
Carrera AI-First?

## Problema que resuelve

El repositorio presenta una implementación de memoria de largo plazo sobre
LangGraph. Distingue memoria de hilo o sesión, checkpoints y memoria
transversal entre hilos, almacenada como documentos JSON organizados por
namespaces y claves.

## Relación con Carrera AI-First

Puede servir para comparar:

- contexto temporal de una conversación;
- datos que deben sobrevivir entre sesiones;
- separación entre memoria de trabajo y memoria duradera;
- actualización mediante feedback humano.

La comparación es especialmente útil para evitar que una memoria técnica
oculte o sustituya los artefactos de continuidad.

## Stack y arquitectura

**Lenguajes:** Python en un notebook.  
**Tecnologías:** LangGraph y sus capas de persistencia/Store.  
**Arquitectura:** memoria de hilo para el contexto corto y memoria entre hilos
para preferencias, decisiones y hechos persistentes; el README explica
almacenamiento por namespaces y claves.  
**Madurez observable:** 2 commits, 54 estrellas y 14 forks; el repositorio es
principalmente un notebook explicativo.

## Componentes potencialmente reutilizables

| Tipo | Componente o patrón | Ubicación | Qué aporta | ¿Separable? |
| --- | --- | --- | --- | --- |
| Modelo | Memoria de hilo frente a memoria entre hilos | `README.md` y `code.ipynb` | Distingue continuidad inmediata de continuidad duradera. | sí, como referencia |
| Modelo | Namespaces y claves | `code.ipynb` | Organización de recuerdos persistentes. | parcial |
| Flujo | Feedback humano que actualiza memoria | notebook | Relaciona corrección con actualización controlada. | sí |
| Patrón | Store separado del checkpoint | explicación LangGraph | Ayuda a no mezclar estado de ejecución con memoria duradera. | sí |

## Modelo de datos, prompts y flujos

El modelo usa documentos JSON persistentes para recuerdos de largo plazo y
separa esos datos de los checkpoints de una conversación. También incluye
esquemas y prompts dentro de un flujo de agente de ejemplo.

Para Carrera AI-First, el aprendizaje principal es semántico: no todo lo que
se conserva para reanudar una conversación debe convertirse en memoria
permanente de la persona.

## Diferencias y límites frente a Carrera AI-First

- El repositorio está diseñado para agentes y no para entrevistas de
  trayectoria profesional.
- Un JSON persistente no resuelve por sí solo consentimiento, minimización,
  revisión o retirada de información.
- El notebook ofrece una demostración, no evidencia de producción.
- LangGraph añade una dependencia que no está justificada para la MVP actual.

## Evaluación

| Criterio | Puntuación | Justificación |
| --- | ---: | --- |
| Encaje funcional | 4/5 | La separación de memorias es relevante para continuidad. |
| Reutilización real | 3/5 | Los patrones son claros; el notebook no es un componente aislado listo para usar. |
| Calidad arquitectónica | 3/5 | La explicación es útil, pero la evidencia de ingeniería es limitada. |
| Madurez | 2/5 | 2 commits y formato de notebook. |
| Dependencias | 2/5 | Depende de LangGraph y de su modelo de persistencia. |
| Licencia | 5/5 | MIT. |
| Coste de integración | 3/5 | Estudiar el patrón es barato; integrar la infraestructura no. |
| Riesgo de desvío | 3/5 | Puede crear una memoria paralela al sistema documental. |
| Valor de aprendizaje | 5/5 | Aclara una distinción importante para continuidad. |

## Riesgos

- **Privacidad:** persistir datos de trayectoria entre sesiones exige reglas
  explícitas.
- **Semántica:** mezclar checkpoint, memoria y estado PCS.
- **Madurez:** poca actividad observable y dependencia de una demostración.
- **Desvío:** sobrediseñar memoria antes de validar qué necesita conservarse.

## Experimento mínimo propuesto

**Hipótesis:** separar memoria de sesión, checkpoint y memoria permanente
reduce ambigüedades en la reanudación de Carrera AI-First.

**Alcance:** construir una tabla de correspondencias entre las capas del
notebook y los artefactos locales.

**Exclusiones:** no ejecutar el notebook, no conectar una base de memoria y no
usar datos reales.

**Resultado observable:** reglas locales sobre qué información puede ser
temporal, qué debe quedar en un checkpoint y qué requiere consolidación.

**Coste estimado:** bajo; estudio documental.

## Resultado del experimento

**Resultado:** pendiente.  
**Evidencia:** pendiente de delimitar `EXP-003-memoria-y-continuidad/`.  
**Problemas encontrados:** la demostración no permite valorar robustez de
producción.  
**Aprendizaje:** la distinción semántica es más valiosa que la implementación
concreta.

## Decisión preliminar

**Decisión:** estudiar como referencia.

**Justificación:** aporta un vocabulario útil para separar continuidad corta y
larga, pero no justifica crear todavía una memoria técnica adicional.

**Qué podría incorporarse:** la distinción entre contexto de sesión,
checkpoint y memoria consolidada.

**Qué no debe incorporarse:** su Store como sustituto de `.pcs/` o de los
artefactos de la bóveda.

**Siguiente paso:** comparar sus capas con la arquitectura documental actual.

## Trazabilidad

- Documento general: [`INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md`](../INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md).
- Flujo: [`FLUJO_INVESTIGACION_GITHUB.md`](../FLUJO_INVESTIGACION_GITHUB.md).
- Sesión PCS: `sesion-20260720-1242-investigacion-github-carrera-ai-first`.

## Fuentes consultadas

- [Repositorio y README](https://github.com/FareedKhan-dev/langgraph-long-memory).
- [LICENSE](https://github.com/FareedKhan-dev/langgraph-long-memory/blob/main/LICENSE).

## Revisión final

- [x] Licencia comprobada.
- [x] Hechos, inferencias y recomendaciones separados.
- [x] Objeto y nivel de evidencia registrados.
- [x] Riesgo de desvío evaluado.
- [x] No se presenta la ficha como autorización de integración.
