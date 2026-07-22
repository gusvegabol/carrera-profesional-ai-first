# Flujo de investigación GitHub

## Propósito

Este documento define el flujo operativo obligatorio para investigar
repositorios de GitHub dentro de Carrera AI-First.

Su función es asegurar que la investigación avance desde una pregunta concreta
hacia una conclusión trazable, sin saltar directamente de un repositorio
interesante a una integración o a una decisión metodológica.

Este es un flujo documental local. No sustituye la gobernanza PCS, no crea
acciones o decisiones por sí solo y no autoriza instalaciones, forks ni
integraciones de código.

## Recorrido general

```text
Pregunta concreta
    ↓
Selección justificada del repositorio
    ↓
Ficha técnica comparable
    ↓
Comparación con repositorios relacionados
    ↓
Recomendación de componentes y experimentos
    ↓
Experimento mínimo autorizado, si procede
    ↓
Resultado y aprendizaje
    ↓
Decisión preliminar de investigación
    ↓
Decisión PCS posterior, solo si se requiere
```

Cada etapa debe dejar su evidencia en el documento correspondiente antes de
avanzar a la siguiente.

## Documentos del flujo

| Etapa | Documento | Función |
| --- | --- | --- |
| Marco | [`INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md`](./INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md) | Define el propósito, el alcance, las categorías y las preguntas generales. |
| Orientación | [`README.md`](./README.md) | Explica la estructura y las reglas de trabajo. |
| Análisis | [`fichas/TEMPLATE_FICHA_REPOSITORIO.md`](./fichas/TEMPLATE_FICHA_REPOSITORIO.md) | Estructura la revisión de un repositorio. |
| Comparación | [`comparativas/MATRIZ_COMPARATIVA_REPOSITORIOS.md`](./comparativas/MATRIZ_COMPARATIVA_REPOSITORIOS.md) | Compara fichas de una misma área. |
| Recomendación | [`comparativas/RECOMENDACION_COMPONENTES_Y_EXPERIMENTOS.md`](./comparativas/RECOMENDACION_COMPONENTES_Y_EXPERIMENTOS.md) | Convierte la comparación en propuestas acotadas. |
| Prueba | `experimentos/EXP-.../` | Conserva la hipótesis, el procedimiento y el resultado de un experimento. |
| Continuidad | `.pcs/sesiones/` | Registra la continuidad de la investigación según PCS. |
| Decisión formal | `.pcs/decisiones/` | Registra decisiones que excedan la recomendación preliminar. |

## Etapas obligatorias

### 1. Formular la pregunta

Antes de analizar un repositorio debe escribirse qué queremos aprender o qué
problema de Carrera AI-First queremos resolver.

La pregunta debe indicar, cuando sea posible:

- la necesidad funcional;
- el componente o patrón que queremos explorar;
- el límite de la investigación;
- qué resultado cambiaría nuestra valoración.

No se abre una ficha solo porque un repositorio sea popular, reciente o
tecnológicamente atractivo.

### 2. Seleccionar y justificar el repositorio

La selección debe indicar por qué el repositorio pertenece a la pregunta y a
qué categoría de la investigación corresponde.

En esta etapa se comprueba de forma inicial:

- que el repositorio existe;
- cuál es su propósito declarado;
- qué relación aparente tiene con la pregunta;
- si hay una razón inicial para priorizarlo.

Esta comprobación inicial no equivale a una auditoría técnica.

### 3. Completar la ficha técnica

La ficha debe crearse a partir de
[`TEMPLATE_FICHA_REPOSITORIO.md`](./fichas/TEMPLATE_FICHA_REPOSITORIO.md).

Debe distinguir claramente:

- hechos observados en el repositorio;
- inferencias sobre su posible utilidad;
- recomendaciones para Carrera AI-First;
- aspectos todavía no comprobados.

También debe registrar dos datos que gobiernan la interpretación posterior:

- **objeto estudiado:** idea, patrón, modelo de datos, componente, código o
  flujo;
- **nivel de evidencia:** lectura documental, inspección técnica, experimento
  ejecutado o integración validada.

No se cierra una ficha si faltan licencia, dependencias, coste, riesgo de
desvío o una decisión preliminar justificada.

### 4. Incorporar la ficha a una comparación

Cuando existan dos o más repositorios relacionados, sus fichas se incorporan a
[`MATRIZ_COMPARATIVA_REPOSITORIOS.md`](./comparativas/MATRIZ_COMPARATIVA_REPOSITORIOS.md).

La comparación debe usar los mismos criterios y escalas. No se utilizará la
matriz para ocultar diferencias de alcance ni para convertir una puntuación en
una decisión automática.

Si solo existe un repositorio, puede elaborarse una comparación provisional
contra la situación actual de Carrera AI-First, dejando constancia de que no
es una comparación entre alternativas equivalentes.

### 5. Formular la recomendación

Los resultados de la comparación se trasladan a
[`RECOMENDACION_COMPONENTES_Y_EXPERIMENTOS.md`](./comparativas/RECOMENDACION_COMPONENTES_Y_EXPERIMENTOS.md).

La recomendación debe separar:

1. ideas o patrones que merece la pena adoptar conceptualmente;
2. componentes que merece la pena probar;
3. código que podría integrarse, solo tras una revisión y autorización
   específicas.

Las decisiones preliminares posibles son:

- `reutilizar`;
- `prototipar`;
- `estudiar como referencia`;
- `posponer`;
- `descartar`.

### 6. Diseñar el experimento mínimo

Solo se propone un experimento cuando existe una incertidumbre que la lectura
documental no puede resolver.

El experimento debe definir:

- una hipótesis;
- un alcance pequeño;
- exclusiones explícitas;
- datos sintéticos o autorizados;
- procedimiento reproducible;
- criterio de éxito o resultado observable;
- coste y riesgos.

La carpeta del experimento se crea dentro de `experimentos/` y no debe incluir
datos profesionales reales sin autorización específica.

### 7. Ejecutar y documentar el resultado

El resultado debe separar:

- lo que ocurrió;
- la evidencia obtenida;
- los problemas encontrados;
- lo que aprendimos;
- lo que sigue sin resolverse.

Un experimento desfavorable también es un resultado válido si responde a la
hipótesis y evita una integración innecesaria.

### 8. Cerrar la recomendación preliminar

Después del experimento, se actualiza la ficha, la matriz o la recomendación,
según corresponda, y se establece una conclusión preliminar:

- continuar investigando;
- prototipar de nuevo con ajustes;
- reutilizar un patrón;
- mantener como referencia;
- posponer;
- descartar.

La conclusión debe indicar qué evidencia la sustenta y qué parte queda fuera
de la conclusión.

No se debe presentar `estudiar como referencia` como una integración parcial:
significa conservar el aprendizaje sin probar ni incorporar el objeto. La
decisión `prototipar` requiere un experimento; `reutilizar` requiere evidencia
suficiente de que el patrón o componente es separable y adecuado.

### 9. Elevar a PCS cuando proceda

Si la investigación sugiere modificar el alcance, adoptar un componente,
autorizar una integración o tomar una decisión que afecte a la continuidad del
host, se detiene la interpretación local y se utiliza el flujo PCS
correspondiente.

La investigación no convierte automáticamente una recomendación en una
decisión formal, no modifica el SPEC ni actualiza un playbook por inferencia.

## Puertas de control

No se debe avanzar si ocurre alguna de estas situaciones:

- no existe una pregunta concreta;
- la fuente o el repositorio no puede verificarse;
- la licencia no está clara para el uso previsto;
- la ficha mezcla hechos con inferencias sin distinguirlos;
- el experimento requiere datos o permisos no disponibles;
- el resultado no tiene un criterio observable;
- se pretende integrar código sin autorización específica;
- la recomendación contradice una fuente metodológica o una decisión PCS
  vigente.

Ante una contradicción normativa o metodológica, se debe detener el flujo y
resolver la autoridad aplicable antes de continuar.

## Criterio de finalización de una línea

Una línea de investigación puede considerarse cerrada cuando:

- la pregunta ha recibido una respuesta suficientemente sustentada;
- las fichas y comparaciones relevantes están completas;
- el experimento se ha ejecutado o se ha justificado por qué no procede;
- la recomendación indica qué adoptar, probar, conservar como referencia,
  posponer o descartar;
- se han registrado los límites y las incertidumbres;
- se ha determinado si hace falta o no una decisión PCS posterior.

Cerrar una línea no implica integrar nada ni adoptar una metodología nueva.
