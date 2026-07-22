# Ficha técnica: `Krishna77-ux/Orbit.AI`

## Identificación

**Repositorio:** `Krishna77-ux/Orbit.AI`  
**URL:** <https://github.com/Krishna77-ux/Orbit.AI>  
**Fecha de revisión:** 2026-07-20  
**Última actividad observada:** no comprobada con fecha exacta; el repositorio muestra 41 commits.  
**Licencia:** software propietario; el README declara todos los derechos reservados.  
**Área funcional:** visualización de carrera, brechas y plataforma de orientación.  
**Objeto estudiado:** ideas de representación visual y recorrido de producto; no código.  
**Nivel de evidencia:** inspección técnica documental; demo no evaluada.  
**Estado de la ficha:** revisada

## Pregunta de investigación

¿Qué formas de visualizar cobertura, brechas y opciones profesionales pueden
ayudar a una persona a comprender su trayectoria sin presentar una precisión
falsa ni reutilizar código propietario?

## Problema que resuelve

Orbit AI se presenta como una plataforma de carrera con análisis de CV,
puntuación ATS, extracción de habilidades, rutas de aprendizaje, preparación
de entrevistas, brechas de habilidades, árbol interactivo de carreras,
matching de puestos y tutoría.

## Relación con Carrera AI-First

Su interés está limitado a estudiar:

- la visualización de una red o árbol de opciones;
- la presentación de brechas y caminos posibles;
- la secuencia de onboarding y salidas explicables;
- cómo mostrar una síntesis sin convertirla en una decisión automática.

## Stack y arquitectura

**Frontend:** React 18, Vite, Tailwind, React Router, React Flow y Framer
Motion.  
**Backend:** Node.js/Express, MongoDB/Mongoose, extracción PDF, autenticación y
servicios de IA.  
**Servicios:** Groq, SambaNova, MongoDB Atlas, Vercel y Razorpay, según el
README.  
**Arquitectura:** aplicación full-stack con frontend, backend, base de datos,
subida de PDF y servicios de análisis.

## Componentes potencialmente reutilizables

| Tipo | Componente o patrón | Ubicación | Qué aporta | ¿Separable? |
| --- | --- | --- | --- | --- |
| UX | Career Orbit Tree | README y frontend | Idea de visualización de rutas y opciones. | sí, como referencia |
| UX | Skills Gap Analyzer | README | Referencia para mostrar brechas. | sí, como referencia |
| Flujo | Onboarding guiado | README | Secuencia inicial de orientación. | sí |
| Producto | Informe exportable | README | Referencia de salida comunicable. | sí, como referencia |

## Modelo de datos, prompts y flujos

El producto parece organizarse alrededor de perfil de CV, habilidades,
objetivos, brechas, rutas y recomendaciones. No se ha auditado el código ni se
ha confirmado que su modelo distinga hechos, evidencias, hipótesis y límites
como exige Carrera AI-First.

## Diferencias y límites frente a Carrera AI-First

- El código es propietario y no debe reutilizarse sin permiso.
- El enfoque parte del CV y de matching, mientras Carrera AI-First prioriza la
  entrevista y la reconstrucción de la trayectoria.
- La visualización de rutas puede dar una sensación de determinismo que nuestro
  perfil debe evitar.
- La plataforma incluye pagos, autenticación y servicios que están fuera de la
  MVP.

## Evaluación

| Criterio | Puntuación | Justificación |
| --- | ---: | --- |
| Encaje funcional | 3/5 | La visualización y las brechas son relevantes, pero el producto es más amplio. |
| Reutilización real | 1/5 | El README declara software propietario. |
| Calidad arquitectónica | 3/5 | Stack identificable y full-stack, pero sin auditoría interna. |
| Madurez | 3/5 | 41 commits y demo descrita; no hay evidencia suficiente de estabilidad. |
| Dependencias | 2/5 | Muchas dependencias externas y servicios. |
| Licencia | 0/5 | No ofrece una licencia de reutilización; declara derechos reservados. |
| Coste de integración | 1/5 | No procede integrar código propietario. |
| Riesgo de desvío | 2/5 | Alto por alcance de plataforma y matching. |
| Valor de aprendizaje | 4/5 | La visualización puede inspirar una exploración local. |

## Riesgos

- **Licencia:** no reutilizar código, assets ni implementación sin autorización.
- **Producto:** sobredimensionar Carrera AI-First con cuentas, pagos y matching.
- **Interpretación:** convertir una visualización de opciones en recomendación
  cerrada.
- **Privacidad:** plataforma full-stack con CV y datos de usuario.

## Experimento mínimo propuesto

**Hipótesis:** una representación visual mínima de zonas exploradas, pendientes
 y opciones puede mejorar la comprensión de la cobertura.

**Alcance:** estudiar el concepto de Orbit Tree y traducirlo a una maqueta
documental o visual propia, sin copiar diseño ni código.

**Exclusiones:** no clonar, no reutilizar assets, no ejecutar el backend y no
usar datos personales.

**Resultado observable:** decisión sobre si una visualización mínima aporta
utilidad sin crear falsa precisión.

**Coste estimado:** medio si se crea una maqueta; bajo si se limita al análisis.

## Resultado del experimento

**Resultado:** pendiente.  
**Evidencia:** pendiente de crear un experimento de visualización.  
**Problemas encontrados:** software propietario y alcance full-stack.  
**Aprendizaje:** su valor es exclusivamente inspiracional hasta nueva evidencia.

## Decisión preliminar

**Decisión:** estudiar como referencia.

**Justificación:** ofrece ideas de representación de brechas y rutas, pero no es
un candidato de reutilización ni de integración.

**Qué podría incorporarse:** una idea propia de visualización de cobertura y
opciones, sometida a revisión humana.

**Qué no debe incorporarse:** código, assets, scoring, matching o arquitectura
de plataforma.

**Siguiente paso:** decidir si la visualización merece un experimento propio.

## Trazabilidad

- Documento general: [`INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md`](../INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md).
- Flujo: [`FLUJO_INVESTIGACION_GITHUB.md`](../FLUJO_INVESTIGACION_GITHUB.md).
- Sesión PCS: `sesion-20260720-1242-investigacion-github-carrera-ai-first`.

## Fuentes consultadas

- [Repositorio y README](https://github.com/Krishna77-ux/Orbit.AI).
- [Sección de licencia del README](https://github.com/Krishna77-ux/Orbit.AI#license).

## Revisión final

- [x] Licencia comprobada.
- [x] Hechos, inferencias y recomendaciones separados.
- [x] Objeto y nivel de evidencia registrados.
- [x] Riesgo de desvío evaluado.
- [x] No se presenta la ficha como autorización de integración.
