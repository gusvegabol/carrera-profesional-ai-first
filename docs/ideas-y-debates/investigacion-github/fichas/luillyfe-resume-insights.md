# Ficha técnica: `luillyfe/resume-insights`

## Identificación

**Repositorio:** `luillyfe/resume-insights`  
**URL:** <https://github.com/luillyfe/resume-insights>  
**Fecha de revisión:** 2026-07-20  
**Última actividad observada:** no comprobada con fecha exacta; el repositorio muestra 15 commits.  
**Licencia:** MIT.  
**Área funcional:** parsing documental, extracción y visualización.  
**Objeto estudiado:** pipeline PDF → extracción → modelo estructurado → interfaz.  
**Nivel de evidencia:** inspección técnica documental; aplicación no ejecutada.  
**Estado de la ficha:** revisada

## Pregunta de investigación

¿Qué partes de un pipeline de extracción y revisión de un CV pueden servir para
importar contexto sin confundir análisis documental con entrevista de
trayectoria?

## Problema que resuelve

Resume Insights procesa CV en PDF, usa LlamaParse y LlamaIndex para dividir e
indexar documentos, Gemini para extracción y análisis, Pydantic para modelos y
Streamlit para mostrar habilidades y matching.

## Relación con Carrera AI-First

Puede aportar una referencia de pipeline:

```text
PDF → parsing → indexación → extracción estructurada → revisión visual
```

La relación con Carrera AI-First es lateral: preparar contexto inicial,
visualizar resultados provisionales y señalar qué debe confirmarse en la
entrevista.

## Stack y arquitectura

**Lenguaje:** Python.  
**Tecnologías:** LlamaIndex, LlamaParse, Gemini, Streamlit y Pydantic.  
**Servicios externos:** Google Gemini y Llama Cloud requieren claves API según
el README.  
**Arquitectura:** aplicación Streamlit con procesamiento de documento,
indexación vectorial, extracción de campos, análisis de habilidades y matching.

## Componentes potencialmente reutilizables

| Tipo | Componente o patrón | Ubicación | Qué aporta | ¿Separable? |
| --- | --- | --- | --- | --- |
| Flujo | Pipeline de procesamiento documental | `README.md` y `app.py` | Secuencia comprensible de extracción a revisión. | sí, como referencia |
| Modelo | `Candidate` y `JobSkill` | código y README | Modelos estructurados para resultados provisionales. | parcial |
| UI | Visualización de habilidades | Streamlit | Referencia para revisión, no para validación automática. | sí |
| Esquema | `output_schema.json` | raíz | Puede inspirar contratos de salida. | parcial |

## Modelo de datos, prompts y flujos

El README identifica modelos Pydantic para candidato y habilidades relevantes,
además de un esquema JSON de salida. El flujo indexa el documento y extrae
nombre, correo, edad y habilidades.

Carrera AI-First necesitaría excluir o controlar campos sensibles y añadir
origen, evidencia, estado, confianza y validación humana.

## Diferencias y límites frente a Carrera AI-First

- Depende de servicios externos y claves API para parsing y generación.
- Extrae información de CV, no experiencia tácita ni trayectoria completa.
- El matching de habilidades pertenece a una capa posterior y puede crear
  inferencias fuertes.
- La visualización no demuestra la calidad de la extracción.

## Evaluación

| Criterio | Puntuación | Justificación |
| --- | ---: | --- |
| Encaje funcional | 3/5 | Aporta un pipeline documental, no la entrevista central. |
| Reutilización real | 3/5 | Hay modelos y esquema identificables, pero con dependencia de servicios. |
| Calidad arquitectónica | 3/5 | Tiene tests, esquema y carpetas, aunque requiere auditoría interna. |
| Madurez | 3/5 | 15 commits y documentación clara; proyecto pequeño. |
| Dependencias | 2/5 | LlamaParse, LlamaIndex, Gemini y claves externas. |
| Licencia | 5/5 | MIT. |
| Coste de integración | 2/5 | Coste y privacidad de servicios externos son relevantes. |
| Riesgo de desvío | 3/5 | Puede desplazar el foco hacia CV y matching. |
| Valor de aprendizaje | 4/5 | Clarifica contratos de extracción y revisión. |

## Riesgos

- **Privacidad:** CV y datos personales pasan potencialmente por servicios
  externos.
- **Dependencias:** cambios de APIs y costes de proveedores.
- **Calidad:** las salidas estructuradas deben comprobarse contra fuentes.
- **Desvío:** convertir la extracción en el flujo principal.

## Experimento mínimo propuesto

**Hipótesis:** un contrato de salida explícito puede hacer que una importación
documental sea revisable y útil como preparación de entrevista.

**Alcance:** comparar `Candidate`, `JobSkill` y `output_schema.json` con el
modelo de evidencias y preguntas pendientes de Carrera AI-First.

**Exclusiones:** no enviar documentos a Gemini o Llama Cloud, no ejecutar la
aplicación y no usar datos reales.

**Resultado observable:** lista de campos aprovechables, campos sensibles que
deben excluirse y campos que faltan para trazabilidad.

**Coste estimado:** bajo; análisis documental.

## Resultado del experimento

**Resultado:** pendiente.  
**Evidencia:** pendiente de definir dentro de `EXP-002-importacion-de-cv/`.  
**Problemas encontrados:** dependencias externas y riesgo de datos sensibles.  
**Aprendizaje:** el esquema de salida es más interesante que la UI completa.

## Decisión preliminar

**Decisión:** estudiar como referencia.

**Justificación:** permite comparar un pipeline claro, pero no compensa aún el
coste y riesgo de servicios externos.

**Qué podría incorporarse:** la idea de contrato de salida y revisión de
extracciones.

**Qué no debe incorporarse:** el matching automático ni el envío de CV real a
servicios externos sin autorización y control de privacidad.

**Siguiente paso:** comparar su esquema con el contrato local de evidencias.

## Trazabilidad

- Documento general: [`INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md`](../INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md).
- Flujo: [`FLUJO_INVESTIGACION_GITHUB.md`](../FLUJO_INVESTIGACION_GITHUB.md).
- Sesión PCS: `sesion-20260720-1242-investigacion-github-carrera-ai-first`.

## Fuentes consultadas

- [Repositorio y README](https://github.com/luillyfe/resume-insights).
- [LICENSE](https://github.com/luillyfe/resume-insights/blob/main/LICENSE).

## Revisión final

- [x] Licencia comprobada.
- [x] Hechos, inferencias y recomendaciones separados.
- [x] Objeto y nivel de evidencia registrados.
- [x] Riesgo de desvío evaluado.
- [x] No se presenta la ficha como autorización de integración.
