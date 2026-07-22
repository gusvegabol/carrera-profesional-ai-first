# Investigación GitHub para Carrera AI-First

**Estado:** primera versión de investigación media  
**Fecha:** 20 de julio de 2026  
**Objetivo:** localizar repositorios de GitHub cuyas ideas, arquitecturas o componentes puedan acelerar Carrera AI-First sin buscar un clon completo ni realizar un fork integral.

---

## 1. Enfoque de la investigación

Carrera AI-First tiene un núcleo distinto al de la mayoría de aplicaciones de orientación laboral: reconstruir la trayectoria profesional mediante entrevista, obtener evidencias verificables, identificar competencias y construir progresivamente una cobertura profesional accionable.

Por ello, los repositorios se estudian como posibles fuentes de:

- patrones de entrevista conversacional;
- extracción y estructuración de información profesional;
- análisis de currículums;
- identificación y comparación de competencias;
- memoria persistente entre sesiones;
- orquestación de agentes o flujos;
- generación de perfiles, informes y mapas;
- arquitectura, interfaz o experiencia de usuario reutilizable.

No se busca encontrar una aplicación idéntica a Carrera AI-First. La pregunta principal es:

> ¿Qué partes ya resueltas por otros proyectos pueden reutilizarse, adaptarse o servir como referencia para avanzar más rápido?

---

## 2. Criterios de evaluación

Cada repositorio se valorará según los siguientes criterios:

1. **Encaje funcional:** qué problema de Carrera AI-First ayuda a resolver.
2. **Reutilización real:** posibilidad de extraer código, esquemas, prompts, modelos de datos o flujos.
3. **Calidad arquitectónica:** claridad, modularidad y facilidad de adaptación.
4. **Madurez:** documentación, actividad, pruebas y estabilidad.
5. **Dependencias:** servicios, modelos, proveedores o infraestructura requeridos.
6. **Licencia:** condiciones para reutilizar o modificar el código.
7. **Coste de integración:** esfuerzo necesario para incorporarlo.
8. **Riesgo de desvío:** posibilidad de introducir complejidad innecesaria en la MVP.
9. **Valor de aprendizaje:** utilidad aunque finalmente no se integre.
10. **Decisión preliminar:** reutilizar, prototipar, estudiar como referencia o descartar.

---

## 3. Categorías de búsqueda

### 3.1 Entrevista profesional con IA

Repositorios que conduzcan entrevistas, generen preguntas dinámicas, evalúen respuestas o mantengan un historial de evidencias.

### 3.2 Extracción y estructuración del perfil

Proyectos que conviertan texto libre, currículums o conversaciones en datos estructurados: experiencias, funciones, logros, herramientas y competencias.

### 3.3 Análisis de competencias y adecuación profesional

Sistemas que comparen perfiles con puestos, detecten carencias o construyan mapas de capacidades.

### 3.4 Memoria y continuidad

Arquitecturas para mantener estado, historial y memoria de largo plazo entre entrevistas o sesiones.

### 3.5 RAG y consulta de la bóveda profesional

Repositorios que permitan consultar evidencias, documentos y artefactos producidos durante la entrevista.

### 3.6 Agentes y orquestación

Sistemas que coordinen tareas como entrevistar, validar evidencias, estructurar datos, clasificar competencias y generar informes.

### 3.7 Currículum, informes y representación final

Herramientas para transformar el perfil profesional en CV, informes, mapas, storybanks u otros productos finales.

---

## 4. Primera selección de repositorios

Esta primera tanda no constituye todavía una recomendación definitiva. Sirve para identificar familias de soluciones y decidir qué repositorios merecen una revisión técnica más profunda.

---

### 4.1 `redjules/ai-career-coach`

**Repositorio:** https://github.com/redjules/ai-career-coach

**Qué hace**

Plataforma de orientación profesional con información sectorial, creación de currículums y cartas de presentación, y preparación interactiva de entrevistas.

**Posible encaje en Carrera AI-First**

- referencia de experiencia de usuario;
- organización de funciones de orientación profesional;
- generación de documentos a partir de un perfil;
- separación entre análisis, preparación y producción de resultados.

**Qué no cubre directamente**

Su orientación principal parece estar en ayudar a buscar empleo y preparar candidaturas, no en reconstruir mediante entrevista una trayectoria profesional con evidencias.

**Valor preliminar**

- **Reutilización:** baja o media.
- **Inspiración funcional:** alta.
- **Prioridad de revisión:** media.

**Decisión preliminar:** estudiar como referencia de producto, no como núcleo de Carrera AI-First.

---

### 4.2 `noamseg/interview-coach-skill`

**Repositorio:** https://github.com/noamseg/interview-coach-skill

**Qué hace**

Skill de coaching de entrevistas que cubre análisis de ofertas, optimización de currículum, simulaciones, evaluación de respuestas, diagnóstico de puntos débiles y creación de un banco de historias profesionales.

**Posible encaje en Carrera AI-First**

- creación y recuperación de un *storybank*;
- evaluación multidimensional de respuestas;
- detección de debilidades o falta de evidencia;
- comandos o flujos especializados;
- separación entre análisis, práctica y retroalimentación.

**Elemento especialmente relevante**

El concepto de banco de historias puede tener relación directa con los casos profesionales y evidencias que Carrera AI-First obtiene durante sus entrevistas.

**Riesgo**

Está orientado a preparar entrevistas de selección, mientras Carrera AI-First entrevista para descubrir y representar el valor profesional de la persona.

**Valor preliminar**

- **Reutilización:** media.
- **Inspiración metodológica:** alta.
- **Prioridad de revisión:** alta.

**Decisión preliminar:** revisar en profundidad sus estructuras de evaluación y su storybank.

---

### 4.3 `jennifer88huang/interview-skills`

**Referencia:** localizado en la categoría GitHub `ai-interviews`.

**Qué hace**

Genera preguntas personalizadas a partir de una oferta y un currículum para practicar entrevistas laborales.

**Posible encaje en Carrera AI-First**

- generación contextual de preguntas;
- adaptación de la entrevista al perfil;
- patrones de interacción;
- evaluación de respuestas.

**Limitación**

Parte de un currículum y una oferta concreta. Carrera AI-First debe poder descubrir información que aún no existe en el CV y explorar zonas desconocidas de la trayectoria.

**Valor preliminar**

- **Reutilización:** baja o media.
- **Inspiración para preguntas dinámicas:** media.
- **Prioridad de revisión:** media.

**Decisión preliminar:** estudiar los mecanismos de personalización, no adoptar su objetivo funcional.

---

### 4.4 `srbhr/Resume-Matcher`

**Repositorio:** https://github.com/srbhr/resume-matcher

**Qué hace**

Analiza un currículum frente a una descripción de puesto y genera recomendaciones, contenido adaptado y cartas de presentación.

**Posible encaje en Carrera AI-First**

- transformación del perfil profesional en una candidatura;
- comparación perfil–puesto;
- detección de palabras clave;
- posible salida futura de cobertura profesional;
- arquitectura de carga, análisis y generación documental.

**Qué no resuelve**

No descubre la trayectoria profesional mediante entrevista ni valida evidencias.

**Valor preliminar**

- **Reutilización:** media para fases futuras.
- **Valor para la MVP actual:** bajo.
- **Prioridad de revisión:** media-baja.

**Decisión preliminar:** reservar para la capa de explotación del perfil, no para el núcleo de entrevista.

---

### 4.5 `xitanggg/open-resume`

**Repositorio:** https://github.com/xitanggg/open-resume

**Qué hace**

Constructor y analizador de currículums de código abierto.

**Posible encaje en Carrera AI-First**

- parser de currículum;
- modelo estructurado de datos profesionales;
- edición y visualización del perfil;
- exportación final;
- interfaz para revisar información antes de producir un CV.

**Elemento especialmente relevante**

Puede servir como referencia para definir qué parte del perfil profesional debe ser editable por la persona y cómo convertir datos estructurados en un documento final.

**Valor preliminar**

- **Reutilización:** media o alta en módulos concretos.
- **Valor para entrevista:** bajo.
- **Valor para representación final:** alto.
- **Prioridad de revisión:** alta.

**Decisión preliminar:** revisar su modelo de datos, parser y generación de currículum.

---

### 4.6 `wespiper/pyresume`

**Repositorio:** https://github.com/wespiper/pyresume

**Qué hace**

Parser en Python para extraer datos estructurados desde currículums PDF, DOCX y TXT.

**Posible encaje en Carrera AI-First**

- importar un CV como fuente inicial;
- precargar empresas, puestos, fechas y educación;
- reducir preguntas redundantes;
- contrastar la entrevista con información documental;
- convertir documentos existentes en datos de entrada.

**Riesgo**

Un parser puede inducir a tratar el CV como fuente de verdad cuando Carrera AI-First busca descubrir información que normalmente no aparece en él.

**Valor preliminar**

- **Reutilización:** potencialmente alta.
- **Complejidad de integración:** baja o media.
- **Prioridad de revisión:** alta.

**Decisión preliminar:** candidato claro para una prueba técnica de importación inicial.

---

### 4.7 `luillyfe/resume-insights`

**Repositorio:** https://github.com/luillyfe/resume-insights

**Qué hace**

Analiza currículums PDF mediante LlamaIndex, Gemini y Streamlit para extraer y mostrar información relevante.

**Posible encaje en Carrera AI-First**

- ejemplo de extracción asistida por LLM;
- combinación de parsing documental y análisis semántico;
- interfaz rápida para prototipos;
- presentación de información estructurada al usuario.

**Valor preliminar**

- **Reutilización:** media.
- **Valor como prototipo:** alto.
- **Prioridad de revisión:** media.

**Decisión preliminar:** estudiar como ejemplo sencillo de pipeline documento → extracción → revisión.

---

### 4.8 `langchain-ai/langgraph`

**Repositorio:** https://github.com/langchain-ai/langgraph

**Qué hace**

Framework de orquestación para agentes con estado, memoria de corto y largo plazo, persistencia y flujos controlados mediante grafos.

**Posible encaje en Carrera AI-First**

- entrevista como máquina de estados;
- checkpoints;
- interrupción y reanudación;
- memoria entre sesiones;
- separación de agentes especializados;
- trazabilidad del flujo;
- validación antes de avanzar;
- recuperación de contexto profesional.

**Riesgo**

Puede introducir más complejidad de la necesaria para una MVP que todavía puede ejecutarse con un flujo más sencillo.

**Valor preliminar**

- **Reutilización:** alta si se adopta una arquitectura agéntica.
- **Riesgo de sobrediseño:** alto.
- **Prioridad de revisión:** alta, pero con disciplina MVP.

**Decisión preliminar:** estudiar como arquitectura futura y usar solo si resuelve una necesidad ya demostrada.

---

### 4.9 `langchain-ai/langgraph-supervisor-py`

**Repositorio:** https://github.com/langchain-ai/langgraph-supervisor-py

**Qué hace**

Biblioteca para crear sistemas jerárquicos multiagente con un supervisor que coordina agentes especializados y puede utilizar memoria.

**Posible encaje en Carrera AI-First**

Podría coordinar agentes como:

- entrevistador;
- verificador de evidencia;
- extractor de competencias;
- clasificador ESCO;
- generador de mapa profesional;
- auditor de cobertura;
- redactor de resultados.

**Riesgo**

La división en muchos agentes puede parecer elegante, pero aumentar coste, latencia, dificultad de depuración y comportamiento emergente.

**Valor preliminar**

- **Reutilización inmediata:** baja.
- **Inspiración arquitectónica:** alta.
- **Prioridad de revisión:** media.

**Decisión preliminar:** no incorporar en la MVP; conservar como referencia para una arquitectura modular posterior.

---

### 4.10 `FareedKhan-dev/langgraph-long-memory`

**Repositorio:** https://github.com/FareedKhan-dev/langgraph-long-memory

**Qué hace**

Ejemplo de memoria de largo plazo para sistemas agénticos o RAG construidos con LangGraph.

**Posible encaje en Carrera AI-First**

- recordar información confirmada de la persona;
- separar memoria de sesión y memoria profesional persistente;
- recuperar evidencias previas;
- evitar repetir preguntas;
- mantener continuidad entre inmersiones;
- distinguir hechos confirmados, inferencias y temas pendientes.

**Elemento especialmente relevante**

Carrera AI-First necesita una memoria controlada, trazable y revisable. El patrón técnico puede ser útil, aunque el modelo de datos profesional deberá diseñarse específicamente.

**Valor preliminar**

- **Reutilización:** media.
- **Valor conceptual:** alto.
- **Prioridad de revisión:** alta.

**Decisión preliminar:** estudiar sus patrones de memoria y compararlos con los artefactos y checkpoints actuales.

---

### 4.11 `langchain-ai/rag-research-agent-template`

**Repositorio:** https://github.com/langchain-ai/rag-research-agent-template

**Qué hace**

Plantilla para construir un agente de investigación con RAG y LangGraph.

**Posible encaje en Carrera AI-First**

- consulta de la bóveda profesional;
- búsqueda entre entrevistas y evidencias;
- generación de respuestas fundamentadas;
- informes de trayectoria;
- recuperación de competencias y casos relacionados.

**Limitación**

Es una plantilla de investigación genérica. El reto central seguirá siendo el modelo de datos, la calidad de los artefactos y las reglas de recuperación.

**Valor preliminar**

- **Reutilización:** media.
- **Valor futuro:** alto.
- **Prioridad de revisión:** media.

**Decisión preliminar:** considerar cuando exista suficiente contenido estructurado en la bóveda.

---

### 4.12 `Krishna77-ux/Orbit.AI`

**Repositorio:** https://github.com/Krishna77-ux/Orbit.AI

**Qué hace**

Plataforma de orientación profesional que analiza currículums, detecta carencias de competencias, construye itinerarios de aprendizaje, genera preguntas y visualiza la trayectoria profesional.

**Posible encaje en Carrera AI-First**

- visualización del mapa profesional;
- detección de brechas;
- itinerarios de aprendizaje;
- experiencia de producto;
- conexión entre perfil, objetivos y acciones;
- representación visual de la trayectoria.

**Limitación**

Parece partir del currículum y de análisis automatizados, no de una entrevista de descubrimiento profundo con trazabilidad de evidencias.

**Valor preliminar**

- **Reutilización:** media.
- **Inspiración de producto:** alta.
- **Prioridad de revisión:** alta.

**Decisión preliminar:** revisar especialmente la visualización, el modelo de brechas y la navegación del producto.

---

## 5. Tabla resumen inicial

| Repositorio | Área principal | Valor para Carrera AI-First | Prioridad | Decisión preliminar |
|---|---|---:|---:|---|
| `noamseg/interview-coach-skill` | Entrevista y storybank | Alto | Alta | Revisar en profundidad |
| `wespiper/pyresume` | Parsing de CV | Alto | Alta | Probar importación |
| `xitanggg/open-resume` | Parser y CV final | Alto | Alta | Revisar modelo de datos |
| `langchain-ai/langgraph` | Estado y orquestación | Alto, con riesgo | Alta | Referencia arquitectónica |
| `FareedKhan-dev/langgraph-long-memory` | Memoria persistente | Alto | Alta | Estudiar patrones |
| `Krishna77-ux/Orbit.AI` | Mapa y brechas | Alto como inspiración | Alta | Revisar UX y modelo |
| `redjules/ai-career-coach` | Plataforma de carrera | Medio | Media | Referencia de producto |
| `jennifer88huang/interview-skills` | Preguntas personalizadas | Medio | Media | Estudiar personalización |
| `luillyfe/resume-insights` | Extracción con LLM | Medio | Media | Referencia de prototipo |
| `langgraph-supervisor-py` | Multiagente | Medio-futuro | Media | No usar en la MVP |
| `rag-research-agent-template` | Consulta RAG | Medio-futuro | Media | Usar cuando exista corpus |
| `srbhr/Resume-Matcher` | Adecuación a puestos | Futuro | Media-baja | Capa de explotación |

---

## 6. Hallazgos iniciales

### 6.1 No aparece todavía un clon directo de Carrera AI-First

Los proyectos encontrados suelen comenzar por uno de estos elementos:

- un currículum ya elaborado;
- una oferta de empleo concreta;
- preparación para una entrevista;
- optimización ATS;
- generación de documentos;
- detección automática de brechas.

Carrera AI-First parte de un problema anterior: descubrir, validar y estructurar el valor profesional de una persona incluso cuando ella no sabe expresarlo o no lo ha documentado.

Esta diferencia debe conservarse como criterio central para no desviar el proyecto.

### 6.2 El mayor valor puede estar en componentes laterales

Los componentes con más posibilidades de reutilización son:

- importación y parsing de CV;
- storybank de casos profesionales;
- memoria persistente y checkpoints;
- flujos de entrevista con estado;
- estructuras de evaluación;
- modelos de datos para experiencia y competencias;
- visualización de mapas;
- consulta RAG de la bóveda;
- generación de productos derivados.

### 6.3 La arquitectura multiagente no debe anticiparse

Existen repositorios capaces de coordinar varios agentes especializados. Sin embargo, Carrera AI-First debería mantener un flujo simple mientras no se demuestre que un único agente guiado por playbooks y artefactos estructurados resulta insuficiente.

### 6.4 El CV debe ser una fuente, no el centro del sistema

Los parsers pueden ahorrar tiempo y aportar contexto, pero no deben limitar la entrevista a lo que ya aparece en el documento. El CV puede contener omisiones, formulaciones pobres o interpretaciones que Carrera AI-First precisamente intenta superar.

---

## 7. Próxima fase recomendada

La siguiente fase de investigación debería analizar técnicamente entre cinco y ocho repositorios prioritarios:

1. `noamseg/interview-coach-skill`
2. `wespiper/pyresume`
3. `xitanggg/open-resume`
4. `langchain-ai/langgraph`
5. `FareedKhan-dev/langgraph-long-memory`
6. `Krishna77-ux/Orbit.AI`
7. `luillyfe/resume-insights`
8. `srbhr/Resume-Matcher`

Para cada uno se revisará:

- licencia;
- lenguaje y stack;
- estructura del repositorio;
- actividad reciente;
- dependencias;
- modelo de datos;
- prompts o flujos;
- componentes separables;
- dificultad de prueba;
- encaje con la MVP actual;
- recomendación final;
- propuesta concreta de experimento, si procede.

---

## 8. Plantilla para las fichas detalladas

### Nombre del repositorio

**URL:**  
**Licencia:**  
**Última actividad observada:**  
**Lenguajes y tecnologías:**  
**Área funcional:**  

#### Problema que resuelve

Descripción breve.

#### Relación con Carrera AI-First

Qué parte del proyecto podría acelerar.

#### Componentes potencialmente reutilizables

- componente;
- modelo;
- prompt;
- flujo;
- interfaz;
- esquema de datos.

#### Diferencias con Carrera AI-First

Qué no resuelve o qué enfoque resulta incompatible.

#### Riesgos

Dependencias, complejidad, licencia, abandono, acoplamiento o desvío de la MVP.

#### Experimento mínimo propuesto

Prueba concreta y barata para comprobar su utilidad.

#### Valoración

- Encaje funcional:
- Reutilización:
- Madurez:
- Coste de integración:
- Valor de aprendizaje:
- Riesgo de desvío:

#### Decisión

**Reutilizar / Prototipar / Estudiar como referencia / Posponer / Descartar**

---

## 9. Decisiones que esta investigación debe permitir

Al finalizar, el documento debería responder:

1. ¿Qué partes de Carrera AI-First no merece la pena construir desde cero?
2. ¿Qué repositorios contienen componentes realmente separables?
3. ¿Qué modelos de datos pueden inspirar el perfil profesional?
4. ¿Cómo implementar continuidad y memoria sin sobrediseñar?
5. ¿Qué patrones de entrevista pueden reforzar el playbook actual?
6. ¿Qué herramientas pueden importar información previa sin condicionar la entrevista?
7. ¿Qué opciones existen para visualizar la cobertura profesional?
8. ¿Qué componentes pertenecen a la MVP y cuáles a fases posteriores?
9. ¿Qué experimentos técnicos ofrecen más aprendizaje con menor coste?
10. ¿Qué repositorios deben descartarse para evitar desviaciones?

---

## 10. Estado del documento

Esta es una **primera versión operativa en ampliación**. La selección inicial
está verificada a nivel de propósito general y sus ocho repositorios prioritarios
ya cuentan con fichas técnicas comparables. La evidencia sigue siendo
principalmente documental: todavía no existe una auditoría completa de código ni
una validación de facilidad real de integración.

La siguiente ampliación deberá completar la matriz comparativa, formular la
recomendación de componentes y experimentos y delimitar los experimentos antes
de ejecutar cualquiera de ellos.

La calibración inicial de este flujo ya se ha realizado con
`noamseg/interview-coach-skill`. La ficha confirmó la utilidad de distinguir el
objeto estudiado, el nivel de evidencia y la decisión preliminar. El repositorio
queda, por ahora, como referencia de patrones de *storybank*, continuidad y
triage; no se ha autorizado su instalación, ejecución ni integración.

La fase de fichas de los repositorios prioritarios queda completada. Se
mantiene `EXP-001-entrevista-y-storybank` como experimento pendiente de
delimitación y ejecución, junto con la matriz comparativa y la recomendación
posterior.
