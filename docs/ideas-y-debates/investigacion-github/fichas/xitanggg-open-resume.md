# Ficha técnica: `xitanggg/open-resume`

## Identificación

**Repositorio:** `xitanggg/open-resume`  
**URL:** <https://github.com/xitanggg/open-resume>  
**Fecha de revisión:** 2026-07-20  
**Última actividad observada:** no comprobada con fecha exacta; el repositorio muestra 36 commits.  
**Licencia:** AGPL-3.0.  
**Área funcional:** modelo de datos, parsing y generación de CV.  
**Objeto estudiado:** modelo de datos, importación y representación final.  
**Nivel de evidencia:** inspección técnica documental; experimento no ejecutado.  
**Estado de la ficha:** revisada

## Pregunta de investigación

¿Qué estructura de datos y qué separación entre importación, edición y salida
pueden inspirar las salidas profesionales de Carrera AI-First sin convertir el
producto en un constructor de CV?

## Problema que resuelve

OpenResume combina un constructor de CV y un parser de CV. Su README describe
actualización en tiempo real, diseño profesional, importación desde PDF,
ejecución local en el navegador y comprobación de legibilidad ATS.

## Relación con Carrera AI-First

Puede aportar referencias para:

- separar datos profesionales de sus representaciones finales;
- diseñar importación opcional de un CV existente;
- distinguir un modelo editable de una salida PDF;
- preservar privacidad mediante procesamiento local;
- explorar qué información falta para una salida profesional.

## Stack y arquitectura

**Lenguajes:** TypeScript.  
**Tecnologías:** React, Next.js, Redux Toolkit, Tailwind CSS, Jest y Docker,
según la estructura visible del repositorio y su README.  
**Infraestructura:** aplicación web y procesamiento local en navegador según la
descripción del proyecto.  
**Arquitectura:** aplicación Next/React con estado centralizado para el CV,
parser, edición y generación de PDF.

## Componentes potencialmente reutilizables

| Tipo | Componente o patrón | Ubicación | Qué aporta | ¿Separable? |
| --- | --- | --- | --- | --- |
| Modelo | Estado centralizado del CV | Redux Toolkit | Inspiración para separar modelo editable y salida. | parcial |
| Flujo | Importar PDF → revisar → editar → exportar | README y aplicación | Referencia para una fuente previa revisable. | sí |
| UX | Vista previa en tiempo real | constructor | Referencia de salida, no de entrevista. | sí, como referencia |
| Restricción | Procesamiento local | README | Principio útil para privacidad de documentación previa. | sí |

## Modelo de datos, prompts y flujos

El repositorio se organiza alrededor de un modelo de CV editable, no alrededor
de una trayectoria profesional completa. La aplicación mantiene estado de
formulario, lo presenta en plantillas y genera PDF.

No se ha identificado una estructura equivalente para evidencias, validación
de competencias, preguntas pendientes o zonas no exploradas.

## Diferencias y límites frente a Carrera AI-First

- AGPL-3.0 exige una revisión jurídica antes de reutilizar código o modificarlo
  dentro de un producto distribuido.
- El modelo está centrado en el CV y sus plantillas.
- ATS y formato visual no son el criterio principal de éxito de Carrera AI-First.
- Sus afirmaciones de éxito profesional no constituyen evidencia independiente
  para nuestro producto.

## Evaluación

| Criterio | Puntuación | Justificación |
| --- | ---: | --- |
| Encaje funcional | 3/5 | Aporta importación y representación, pero no entrevista ni perfil completo. |
| Reutilización real | 3/5 | Hay patrones útiles, aunque la licencia y el acoplamiento a una app reducen la reutilización directa. |
| Calidad arquitectónica | 4/5 | Stack y estructura de aplicación claros, con pruebas y estado centralizado visibles. |
| Madurez | 4/5 | 36 commits, sitio público y producto reconocible; falta auditoría completa. |
| Dependencias | 3/5 | Requiere stack web y pipeline de PDF. |
| Licencia | 2/5 | AGPL-3.0 obliga a revisar cuidadosamente cualquier reutilización de código. |
| Coste de integración | 2/5 | Integrar código o modelo implicaría adaptar una aplicación completa. |
| Riesgo de desvío | 3/5 | Puede orientar la MVP hacia CV/ATS y no hacia entrevista. |
| Valor de aprendizaje | 4/5 | Buena referencia para separar modelo, edición y salida. |

## Riesgos

- **Licencia:** AGPL-3.0.
- **Alcance:** sesgo hacia generación de CV y ATS.
- **Privacidad:** aunque declara ejecución local, una adaptación puede cambiar
  el perímetro de datos.
- **Desvío:** dedicar esfuerzo a plantillas antes de validar el perfil.

## Experimento mínimo propuesto

**Hipótesis:** separar modelo profesional y representación final mejora la
trazabilidad de las salidas de Carrera AI-First.

**Alcance:** comparar el modelo de CV descrito por OpenResume con el modelo
conceptual de Perfil Profesional Accionable.

**Exclusiones:** no reutilizar código AGPL, no ejecutar la aplicación y no
evaluar calidad visual como criterio principal.

**Resultado observable:** tabla de campos que pueden reutilizarse, campos que
faltan y campos que deberían derivar de evidencias.

**Coste estimado:** bajo; estudio documental.

## Resultado del experimento

**Resultado:** pendiente.  
**Evidencia:** pendiente de crear un bloque de experimento separado.  
**Problemas encontrados:** la licencia y el enfoque de CV limitan la integración.  
**Aprendizaje:** el mayor valor probable es conceptual, no de código.

## Decisión preliminar

**Decisión:** estudiar como referencia.

**Justificación:** ofrece ideas útiles para modelo editable, importación y
salida, pero la licencia y el foco de producto desaconsejan tratarlo como
componente directo de la MVP.

**Qué podría incorporarse:** separación entre datos y representaciones,
revisión de importaciones y principio de procesamiento local.

**Qué no debe incorporarse:** el constructor completo, la lógica ATS ni código
sin revisión de licencia.

**Siguiente paso:** comparar su modelo con el modelo de Perfil Profesional
Accionable cuando se prepare la matriz de esta categoría.

## Trazabilidad

- Documento general: [`INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md`](../INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md).
- Flujo: [`FLUJO_INVESTIGACION_GITHUB.md`](../FLUJO_INVESTIGACION_GITHUB.md).
- Sesión PCS: `sesion-20260720-1242-investigacion-github-carrera-ai-first`.

## Fuentes consultadas

- [Repositorio y README](https://github.com/xitanggg/open-resume).
- [LICENSE](https://github.com/xitanggg/open-resume/blob/main/LICENSE).

## Revisión final

- [x] Licencia comprobada.
- [x] Hechos, inferencias y recomendaciones separados.
- [x] Objeto y nivel de evidencia registrados.
- [x] Riesgo de desvío evaluado.
- [x] No se presenta la ficha como autorización de integración.
