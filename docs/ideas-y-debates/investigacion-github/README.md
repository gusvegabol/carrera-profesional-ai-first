# Investigación GitHub para Carrera AI-First

## Propósito

Esta carpeta reúne la investigación técnica de repositorios de GitHub que
puedan aportar ideas, componentes, modelos de datos, prompts o patrones de
flujo útiles para Carrera AI-First.

La investigación no busca encontrar un clon completo del proyecto ni justificar
una integración por el mero hecho de que un repositorio sea atractivo. Su
objetivo es identificar qué merece la pena reutilizar, qué conviene estudiar y
qué debe descartarse para proteger el alcance de la MVP.

El documento de referencia de la investigación es
[`INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md`](./INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md).

## Estructura

```text
investigacion-github/
├── README.md
├── FLUJO_INVESTIGACION_GITHUB.md
├── INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md
├── fichas/
│   ├── noamseg-interview-coach-skill.md
│   ├── wespiper-pyresume.md
│   ├── xitanggg-open-resume.md
│   ├── langchain-ai-langgraph.md
│   ├── fareedkhan-langgraph-long-memory.md
│   ├── krishna77ux-orbit-ai.md
│   ├── luillyfe-resume-insights.md
│   └── srbhr-resume-matcher.md
├── comparativas/
│   ├── MATRIZ_COMPARATIVA_REPOSITORIOS.md
│   └── RECOMENDACION_COMPONENTES_Y_EXPERIMENTOS.md
└── experimentos/
    ├── EXP-001-entrevista-y-storybank/
    ├── EXP-002-importacion-de-cv/
    ├── EXP-003-memoria-y-continuidad/
    └── EXP-004-visualizacion-de-cobertura/
```

### Función de cada zona

- `fichas/` contiene una ficha comparable por repositorio.
- `comparativas/` reúne las matrices y síntesis que cruzan varios análisis.
- `experimentos/` contiene pruebas técnicas pequeñas, reproducibles y con un
  resultado verificable.
- `FLUJO_INVESTIGACION_GITHUB.md` define el flujo obligatorio que conecta las
  preguntas, fichas, comparativas, recomendaciones y experimentos.
- `INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md` conserva el marco general, la
  selección inicial, los criterios y las preguntas que la investigación debe
  responder.
- `README.md` explica cómo navegar y trabajar en esta investigación.

Las decisiones formales se registran en `.pcs/decisiones/` y la continuidad de
la investigación en `.pcs/sesiones/`. Esta carpeta no duplica esos registros.

## Cómo abordaremos la investigación

El uso de [`FLUJO_INVESTIGACION_GITHUB.md`](./FLUJO_INVESTIGACION_GITHUB.md) es
obligatorio para toda línea de esta investigación. No se debe pasar de la
selección de un repositorio a una recomendación o experimento sin recorrer y
documentar las etapas que correspondan.

El flujo es local y documental: no sustituye la gobernanza PCS ni autoriza por
sí solo instalaciones, forks, integraciones o cambios metodológicos.

### 1. Partir de una pregunta de Carrera AI-First

Cada análisis debe comenzar con una necesidad concreta, por ejemplo:

- mejorar la entrevista y el registro de historias;
- importar información previa sin convertir el CV en el centro del sistema;
- conservar memoria y continuidad sin sobrediseñar;
- representar la cobertura profesional;
- preparar una salida o una fase futura de adecuación profesional.

No se analizará un repositorio únicamente porque use tecnologías conocidas o
porque tenga una interfaz atractiva.

### 2. Crear una ficha técnica comparable

Cada ficha de `fichas/` debe cubrir, como mínimo:

1. repositorio, enlace y fecha de revisión;
2. problema que resuelve;
3. lenguaje, stack y dependencias;
4. licencia y condiciones relevantes;
5. estructura y calidad observable;
6. modelo de datos, prompts o flujos destacables;
7. componentes potencialmente separables;
8. diferencias con Carrera AI-First;
9. coste y riesgo de integración;
10. valor de aprendizaje;
11. experimento mínimo propuesto;
12. decisión preliminar.

La decisión preliminar solo podrá ser una de estas:

- `reutilizar`;
- `prototipar`;
- `estudiar como referencia`;
- `posponer`;
- `descartar`.

### 3. Investigar por bloques

El orden inicial recomendado es:

1. entrevista y *storybank*;
2. importación y parsing de CV;
3. memoria, continuidad y checkpoints;
4. visualización de cobertura y brechas;
5. extracción documental y adecuación profesional como líneas posteriores.

Este orden mantiene la investigación cerca del foco actual y retrasa las
capas que podrían desviar la MVP.

### 4. Proponer experimentos pequeños

Un experimento debe responder una pregunta concreta con el menor coste
razonable. Cada carpeta de `experimentos/` deberá indicar:

- hipótesis;
- alcance y exclusiones;
- repositorio o componente probado;
- datos de prueba permitidos;
- procedimiento;
- resultado observable;
- problemas encontrados;
- conclusión;
- siguiente decisión posible.

No se instalarán dependencias, se harán forks ni se integrará código solo por
abrir una ficha. Esas acciones requieren una autorización y un alcance
concretos.

### 5. Comparar antes de recomendar

Cuando existan varias fichas de una misma área, se actualizará la matriz de
`comparativas/` atendiendo a:

- encaje funcional;
- reutilización real;
- calidad arquitectónica;
- madurez;
- dependencias;
- licencia;
- coste de integración;
- riesgo de desvío;
- valor de aprendizaje.

La recomendación deberá separar siempre tres posibilidades distintas:

1. adoptar una idea o patrón;
2. probar un componente;
3. integrar código en Carrera AI-First.

La primera no implica automáticamente la segunda ni la tercera.

## Límites de la investigación

- No modifica por sí sola el SPEC, los playbooks ni el alcance de Carrera AI
  2.0.
- No convierte una selección preliminar en una recomendación definitiva.
- No anticipa una arquitectura multiagente sin evidencia experimental.
- No convierte el CV en la fuente principal del Perfil Profesional
  Accionable.
- No trata una licencia permisiva como garantía de calidad o de integración.
- No almacena información profesional real de una persona en los experimentos
  sin autorización específica.
- No copia repositorios completos dentro de esta carpeta; se documentan sus
  fuentes, hallazgos y resultados.

## Resultado esperado

La investigación estará suficientemente madura cuando permita responder:

- qué no merece la pena construir desde cero;
- qué componentes son realmente separables;
- qué modelos de datos pueden inspirar el perfil;
- qué patrones refuerzan la entrevista actual;
- qué experimentos ofrecen más aprendizaje con menor coste;
- qué debe entrar en la MVP, qué queda para después y qué debe descartarse.

El resultado no será una lista de repositorios interesantes, sino una base
trazable para tomar decisiones técnicas prudentes.

## Estado actual

La selección inicial ya está convertida en ocho fichas técnicas comparables.
Estas fichas contienen decisiones preliminares y niveles de evidencia
documentales; todavía no autorizan instalación, ejecución ni integración de
código.

El siguiente gesto recomendado es completar la matriz comparativa y, a partir
de ella, la recomendación de componentes y experimentos. `EXP-001-entrevista-y-
`storybank` sigue pendiente de delimitación antes de cualquier ejecución.
