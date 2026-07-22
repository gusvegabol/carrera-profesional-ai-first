# Ficha técnica: `srbhr/Resume-Matcher`

## Identificación

**Repositorio:** `srbhr/Resume-Matcher`  
**URL:** <https://github.com/srbhr/Resume-Matcher>  
**Fecha de revisión:** 2026-07-20  
**Última actividad observada:** el repositorio muestra 1.385 commits y una versión publicada 1.2 con fecha visible del 2 de abril de 2026.  
**Licencia:** Apache-2.0.  
**Área funcional:** adecuación de CV a ofertas y generación de candidaturas.  
**Objeto estudiado:** flujo de matching y generación de documentos; no código para la MVP.  
**Nivel de evidencia:** inspección técnica documental; aplicación no ejecutada.  
**Estado de la ficha:** revisada

## Pregunta de investigación

¿Qué patrones de adecuación de un perfil a una oferta pueden ser útiles para
una fase posterior, sin convertir el matching en criterio de validación del
Perfil Profesional Accionable 2.0?

## Problema que resuelve

Resume Matcher crea un CV maestro y lo adapta a cada oferta mediante LLM
locales o remotos. Su flujo incluye cargar CV, pegar una descripción de puesto,
revisar mejoras, generar carta y preparación opcional de entrevista, ajustar la
maquetación y exportar PDF.

## Relación con Carrera AI-First

Su interés es posterior a la construcción del perfil:

- comparar evidencias y competencias con requisitos de una oferta;
- identificar brechas de información o experiencia;
- generar una salida específica para una candidatura;
- estudiar cómo mantener un documento maestro y representaciones derivadas.

No debe entrar en el criterio de finalización de Carrera AI 2.0.

## Stack y arquitectura

**Backend:** FastAPI, Python 3.13+ y LiteLLM.  
**Frontend:** Next.js 16, React 19 y TypeScript.  
**Datos:** TinyDB con almacenamiento JSON.  
**PDF:** Chromium headless mediante Playwright.  
**Modelos:** más de 100 LLM locales o remotos según el README.  
**Despliegue:** Docker y aplicaciones separadas de frontend/backend.

## Componentes potencialmente reutilizables

| Tipo | Componente o patrón | Ubicación | Qué aporta | ¿Separable? |
| --- | --- | --- | --- | --- |
| Flujo | CV maestro → oferta → salida adaptada | README | Modelo de derivación de salidas desde una base estable. | sí, como referencia |
| Modelo | Requisitos de oferta frente a perfil | aplicación y docs | Referencia para una brecha futura. | parcial |
| Salida | Carta, CV y PDF derivados | README | Ejemplo de productos posteriores. | sí, como referencia |
| Infraestructura | Soporte de LLM locales/remotos | LiteLLM | Referencia técnica futura, no necesaria ahora. | parcial |

## Modelo de datos, prompts y flujos

El flujo presupone un CV maestro y una descripción de puesto como entradas. Las
salidas se adaptan al contexto de candidatura y pueden incluir carta,
preparación de entrevista y PDF.

Para Carrera AI-First, cualquier matching futuro debe partir de conceptos
internos y evidencias validadas, mostrar incertidumbre y no convertir la
similitud textual en prueba de competencia.

## Diferencias y límites frente a Carrera AI-First

- Está orientado a candidaturas, no a descubrir y reconstruir la trayectoria.
- El matching automático puede dar una confianza excesiva en una adecuación.
- La generación de CV y cartas queda fuera de la MVP definida.
- Su tamaño y actividad no justifican incorporarlo antes de validar el perfil.

## Evaluación

| Criterio | Puntuación | Justificación |
| --- | ---: | --- |
| Encaje funcional | 2/5 | Pertenece a una fase posterior de explotación del perfil. |
| Reutilización real | 3/5 | Hay patrones interesantes, pero no son necesarios ahora. |
| Calidad arquitectónica | 4/5 | Stack completo, documentación multilingüe y despliegue documentado. |
| Madurez | 5/5 | 1.385 commits, releases y actividad observable. |
| Dependencias | 3/5 | Muchas piezas, aunque con soporte local/remoto. |
| Licencia | 5/5 | Apache-2.0. |
| Coste de integración | 1/5 | Demasiado alto y fuera de la prioridad actual. |
| Riesgo de desvío | 1/5 | Muy alto si se incorpora antes de cerrar 2.0. |
| Valor de aprendizaje | 4/5 | Útil para diseñar una capa futura de salidas orientadas a oferta. |

## Riesgos

- **Alcance:** adelantar matching, CV y cartas antes de validar el perfil.
- **Interpretación:** confundir adecuación a una oferta con competencia
  demostrada.
- **Complejidad:** frontend, backend, PDF, LLM y almacenamiento.
- **Privacidad:** documentos y ofertas pueden contener información sensible.

## Experimento mínimo propuesto

**Hipótesis:** una futura comparación entre perfil y oferta puede detectar
brechas útiles si se basa en evidencias internas y no solo en similitud textual.

**Alcance:** estudiar documentalmente la separación entre CV maestro, oferta y
salidas adaptadas.

**Exclusiones:** no ejecutar matching, no usar ofertas reales y no generar
salidas de candidatura.

**Resultado observable:** contrato futuro de entradas, evidencias, brechas y
salidas; indicación de qué queda fuera de 2.0.

**Coste estimado:** bajo; estudio de alcance.

## Resultado del experimento

**Resultado:** pendiente/posterior.  
**Evidencia:** no procede crear experimento MVP ahora.  
**Problemas encontrados:** alto riesgo de desvío y dependencia de una fase no
prioritaria.  
**Aprendizaje:** el repositorio sirve para delimitar la explotación futura,
no para orientar la entrevista inicial.

## Decisión preliminar

**Decisión:** posponer.

**Justificación:** su valor aparece después de construir y validar el Perfil
Profesional Accionable; introducirlo ahora ampliaría indebidamente el alcance.

**Qué podría incorporarse:** el concepto de documento maestro y salidas
derivadas para una versión futura.

**Qué no debe incorporarse:** matching, generación de candidatura o PDF como
criterio de éxito de 2.0.

**Siguiente paso:** conservar la ficha como referencia de fase posterior y no
abrir experimento hasta que exista una decisión de alcance posterior.

## Trazabilidad

- Documento general: [`INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md`](../INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md).
- Flujo: [`FLUJO_INVESTIGACION_GITHUB.md`](../FLUJO_INVESTIGACION_GITHUB.md).
- Sesión PCS: `sesion-20260720-1242-investigacion-github-carrera-ai-first`.

## Fuentes consultadas

- [Repositorio y README](https://github.com/srbhr/Resume-Matcher).
- [LICENSE](https://github.com/srbhr/Resume-Matcher/blob/main/LICENSE).

## Revisión final

- [x] Licencia comprobada.
- [x] Hechos, inferencias y recomendaciones separados.
- [x] Objeto y nivel de evidencia registrados.
- [x] Riesgo de desvío evaluado.
- [x] No se presenta la ficha como autorización de integración.
