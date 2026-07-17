# Diseño: versionado funcional de Carrera AI

## Estado del diseño

Diseño aprobado durante la sesión de brainstorming del 17 de julio de 2026.

Este documento define el sistema que deberá gobernar el versionado funcional de `Carrera AI`. No materializa todavía el documento canónico de versiones, el flujo operativo, las revisiones del SPEC ni los cambios de continuidad PCS.

## Problema que se quiere resolver

El proyecto ha evolucionado mediante varios planteamientos, pilotos, playbooks y cambios de objetivo. Esa evolución está distribuida entre el historial de Git, el README, el SPEC, el estado PCS y varias sesiones abiertas. Como consecuencia:

- conviven versiones globales implícitas y versiones explícitas de playbooks;
- algunas sesiones acumulan trabajo perteneciente a etapas funcionales distintas;
- no existe una fuente única que declare la versión global vigente;
- no hay un procedimiento documentado para abrir, promover, completar o abandonar una versión;
- una versión de un componente puede confundirse con la versión del proyecto;
- el SPEC puede evolucionar sin un número de revisión ni un historial interno de cambios.

El diseño debe separar la evolución del producto, la evolución de sus componentes y la continuidad operativa registrada mediante PCS.

## Principios acordados

1. La versión global cambia por un hito funcional del producto, no por cada modificación documental o metodológica.
2. `Carrera AI` y sus componentes tienen numeraciones independientes.
3. La persona decide el objetivo, el alcance y el estado de una versión.
4. PCS no define la versión: registra la decisión funcional, su vigencia y su trazabilidad.
5. Las sesiones conservan historia y trabajo, pero no son fuentes de verdad de la versión.
6. Una versión global completada conserva congelados su objetivo, alcance y composición.
7. Los números expresan hitos funcionales y no tienen que formar una secuencia consecutiva.
8. La documentación funcional en español debe someterse a revisión ortográfica antes de considerarse terminada.

## Capas de versionado

### Versión global del producto

La versión global identifica una etapa coherente de `Carrera AI`: su objetivo funcional, alcance, exclusiones, criterio de finalización y composición de componentes.

Usa el formato `MAYOR.MENOR`.

- `MAYOR` cambia cuando se transforma el modelo funcional central, el resultado principal o la forma fundamental de producirlo.
- `MENOR` cambia cuando se incorpora un hito funcional relevante sin sustituir el modelo central de la generación vigente.
- No existen versiones globales de parche. Las correcciones y mejoras pequeñas pertenecen a los componentes o a las revisiones documentales.

Los números intermedios no representan porcentajes de avance. Por ejemplo, `2.5` identifica un hito funcional dentro de la generación `2.x`; no significa que el proyecto esté a mitad de camino hacia `3.0`.

### Versiones de componentes

Los componentes funcionales usan versionado semántico `MAYOR.MENOR.PARCHE`.

- `MAYOR`: cambio incompatible del propósito, las entradas, las salidas o las garantías del componente.
- `MENOR`: capacidad nueva compatible con el contrato existente.
- `PARCHE`: corrección o precisión operativa que no amplía la capacidad.

Una modificación de un concepto, patrón o plantilla puede provocar una nueva versión del componente que lo utiliza, pero esos documentos auxiliares no reciben necesariamente una versión propia.

### Revisión del SPEC

`docs/DOCUMENTO_SPEC_CARRERA_AI.md` define el producto global y no es un componente. Debe declarar:

```yaml
version_producto: "2.0"
revision_spec: 1
estado: vigente
fecha_revision: 2026-07-17
```

El SPEC mantendrá un historial interno con el número de revisión, el cambio, el motivo, el origen y el impacto sobre la versión global. Una modificación que cambie el objetivo central no se resolverá aumentando solo `revision_spec`: activará el flujo de cambio de versión global.

## Fuente de verdad y documentos relacionados

### Documento canónico

`docs/VERSIONADO_CARRERA_AI.md` será la fuente de verdad de la versión global. Contendrá:

1. versión global vigente;
2. objetivo, alcance y exclusiones;
3. criterio de finalización;
4. matriz de componentes;
5. historial de versiones globales;
6. versiones futuras candidatas;
7. reglas resumidas de versionado;
8. trazabilidad hacia decisiones, sesiones, evidencias y revisiones del SPEC.

### Flujo operativo

`docs/FLUJO_CAMBIO_VERSION_CARRERA_AI.md` documentará todas las tareas necesarias para abrir, promover, completar o abandonar una versión. Será un procedimiento funcional local de `Carrera AI`, no gobernanza universal de PCS Core.

### Función de las demás superficies

- `README.md`: muestra un resumen de la versión global vigente y enlaza al documento canónico.
- `DOCUMENTO_SPEC_CARRERA_AI.md`: define el producto y mantiene su revisión documental.
- `.pcs/estado/estado-actual.md`: refleja el trabajo operativo dentro de la versión, pero no decide cuál es.
- Sesiones PCS: registran el trabajo, el razonamiento y las evidencias.
- Decisiones PCS: registran decisiones funcionales aprobadas por la persona.
- Acciones PCS: organizan la materialización cuando sea necesario.

La formulación correcta es «decisión funcional de Carrera AI registrada mediante una entidad de decisión PCS». La decisión pertenece al proyecto; PCS aporta identidad, trazabilidad, vigencia y relaciones con sesiones, acciones y estado.

## Estados de una versión global

- `propuesta`: hito en debate; todavía no es versión vigente.
- `en_desarrollo`: objetivo y alcance aprobados; existe trabajo activo para satisfacerlos.
- `candidata_a_cierre`: se considera alcanzado el criterio de finalización y queda pendiente la validación final.
- `completada`: existe evidencia y aprobación suficientes para considerar alcanzado el objetivo.
- `abandonada`: se cierra sin alcanzar su objetivo.

`abandonada` describe el resultado de la versión. Una versión abandonada no puede declarar `continuada_en`.

`Vigente` no es un estado adicional de la versión global. El documento canónico designa una única versión global actual, que puede estar `en_desarrollo`, `candidata_a_cierre` o `completada` mientras no se abra su sucesora.

## Base y continuidad

Cada versión global declara:

```yaml
version: "2.0"
version_base: "1.6"
estado: "en_desarrollo"
continuada_en:
```

Reglas:

1. `version_base` debe apuntar a una versión `completada`.
2. `0.0` es la raíz anterior a cualquier versión funcional completada y no necesita `version_base`.
3. Varios intentos abandonados pueden compartir la misma versión base.
4. Una versión abandonada deja `continuada_en` vacío.
5. Si `A.continuada_en = B`, entonces `B.version_base = A`.
6. Una versión completada puede señalar como continuación una versión que todavía esté `en_desarrollo`.
7. Un número no utilizado permanece libre y no se asigna retrospectivamente para eliminar huecos.

Ejemplo de ramas abandonadas desde la raíz:

```yaml
version: "0.4"
version_base: "0.0"
estado: "abandonada"
continuada_en:
```

## Genealogía histórica aprobada

La reconstrucción es retrospectiva: los números no se declararon en cada momento, pero los hitos funcionales están respaldados por el historial del proyecto y por información aportada por el usuario.

| Versión | Nombre o hito | Estado | Resultado |
| --- | --- | --- | --- |
| `0.0` | Base inicial | raíz | Punto de partida anterior a una versión funcional completada. |
| `0.1` | `app-carrera-profesional` | abandonada | Aplicación Python con IA local; el coste del frontend inacabado impedía llegar al núcleo del proyecto. |
| `0.2` | Número no utilizado | — | Quedó libre deliberadamente. |
| `0.3` | `app-carrera-profesional-c#` | abandonada | Sustituyó el frontend Python por C# y repitió el coste excesivo de desarrollar la interfaz. |
| `0.4` | `app-carrera-bóveda-conocimiento` | abandonada | Probó Obsidian y una IA local de gobernanza; mantener prompts y guardarraíles resultó demasiado costoso. |
| `1.0` | Carrera Profesional AI-First | completada | Definió el sistema AI-First gobernado mediante ChatGPT sin desarrollar una aplicación propia. |
| `1.1` | Delimitación del primer MVP | completada | Fijó el primer resultado útil, las entradas, las salidas y las exclusiones. |
| `1.2` | Entrevista profesional como núcleo | completada | Reorientó el MVP hacia la entrevista profunda como capacidad principal. |
| `1.3` | Primera metodología ejecutable | completada | Consolidó bóveda, conceptos, patrones, salvaguardas y playbook de profundidad. |
| `1.4` | Primera validación empírica | completada | Una entrevista produjo una competencia con evidencia y validación de la persona. |
| `1.5` | Validación mediante varios pilotos | completada | Amplió la evidencia y refinó el método ante tensiones diferentes. |
| `1.6` | Cierre del MVP-A | completada | Validó la hipótesis mínima de profundidad e identificó empíricamente su límite de cobertura. |
| `2.0` | Perfil Profesional Accionable | en desarrollo | Busca integrar cobertura, profundidad, evidencias y síntesis de trayectoria. |

La línea funcional válida es:

```text
0.0
├── 0.1 abandonada
├── 0.3 abandonada
├── 0.4 abandonada
└── 1.0 → 1.1 → 1.2 → 1.3 → 1.4 → 1.5 → 1.6 → 2.0 en desarrollo
```

Los aprendizajes de una versión abandonada pueden explicarse en el historial narrativo, pero no la convierten en parte de la línea `continuada_en`.

## Versión global actual

`Carrera AI 2.0` está `en_desarrollo`.

Su objetivo funcional es producir y validar con una persona un primer Perfil Profesional Accionable integral y revisable mediante el recorrido:

```text
cobertura profesional
→ inmersión en profundidad
→ evidencias
→ síntesis de trayectoria
→ Perfil Profesional Accionable
```

El criterio de finalización exige ejecutar y validar ese recorrido completo con una persona que pueda revisar, corregir y reconocer como fiel el perfil resultante.

La correspondencia candidata con ESCO queda fuera del criterio de finalización de `2.0`. La investigación puede avanzar en paralelo sin bloquear ni alterar esta versión. Su integración es un posible hito funcional posterior, candidato provisional a `2.5`; esa versión no podrá abrirse formalmente hasta que `2.0` esté completada.

## Componentes funcionales

Un componente es una unidad funcional identificable, utilizable y validable de manera independiente, con propósito, entradas, salidas y contrato de comportamiento propios.

Componentes reconocidos o previstos:

- playbook de entrevista de profundidad;
- playbook de cobertura profesional;
- estructura o contrato del Perfil Profesional Accionable;
- integración ESCO, cuando deje de ser investigación y tenga contrato propio.

No son componentes independientes:

- conceptos;
- patrones de preguntas;
- fricciones y antipatrones;
- plantillas;
- ejemplos;
- fuentes;
- documentación auxiliar.

Estados de las versiones de componentes:

- `borrador`;
- `en_validacion`;
- `vigente`;
- `descartada`;
- `retirada`.

La versión no expresa por sí sola el grado de validación. Un componente `1.0.0` puede seguir siendo un borrador.

## Composición actual de Carrera AI 2.0

| Componente | Versión | Estado | Papel en `2.0` | Requisito para el cierre |
| --- | --- | --- | --- | --- |
| Entrevista de profundidad | `1.3.2` | `vigente` | Obtener competencias con evidencia. | Funcionar dentro del recorrido integral. |
| Cobertura profesional | `1.0.0` | `borrador` | Recorrer y organizar la trayectoria. | Alcanzar una versión validada. |
| Perfil Profesional Accionable | pendiente | no formalizado | Integrar la salida final. | Disponer de contrato y primera versión validada. |
| ESCO | no es componente activo | investigación | Fuera del alcance de `2.0`. | No bloquea el cierre. |

Mientras `2.0` esté `en_desarrollo`, las versiones de los componentes pueden cambiar sin alterar la versión global si respetan su objetivo y alcance. Al pasar a `candidata_a_cierre`, se fijarán las versiones exactas. Al declararse `completada`, la composición quedará congelada.

Una mejora posterior de un componente no modificará retrospectivamente una versión global completada.

## Relación entre versiones y sesiones

Cada sesión pertenece como máximo a una versión global. Una sesión puede trabajar con varios componentes, pero no representa la versión del proyecto.

Cuando cambia la versión global se revisan todas las sesiones abiertas:

- una sesión vinculada a la versión que termina se cierra si su objetivo ha concluido;
- si su trabajo debe continuar, se cierra y se abre una sesión sucesora para la nueva versión;
- una sesión paralela sin versión global asignada puede permanecer abierta;
- una sesión de infraestructura o gobernanza puede permanecer abierta si su alcance no depende de la versión;
- una sesión obsoleta se cierra dejando constancia del resultado.

No se cambia retroactivamente `version_global_contexto` para trasladar una sesión entre versiones.

Aplicación a las sesiones actuales:

- `sesion-20260630-alcance-mvp-carrera-ai` pertenece históricamente a `1.x` y no debe acumular trabajo de `2.0`.
- `sesion-20260705-concepto-cobertura-profesional-carrera-ai` pertenece al desarrollo metodológico de cobertura dentro de `2.0`.
- `sesion-20260712-adaptacion-funcional-desde-dentro-carrera-ai` es la sesión activa de este diseño y pertenece a `2.0`.
- `sesion-20260710-2347-investigacion-operativa-esco-carrera-ai` es investigación paralela. Si se abre formalmente `2.5`, deberá cerrarse y dar paso a una sesión de integración vinculada a esa versión.

## Flujo de cambio de versión

### Abrir una versión

1. Detectar el hito funcional en una sesión.
2. Clasificar si el cambio afecta a un componente, al alcance vigente o al objetivo global.
3. Comprobar que la versión base está completada o es `0.0`.
4. Definir número, objetivo, alcance, exclusiones, criterio de finalización, componentes y evidencia esperada.
5. Revisar las sesiones abiertas y decidir su cierre, sucesión o continuidad paralela.
6. Obtener aprobación humana.
7. Registrar la decisión funcional mediante PCS.
8. Actualizar documento canónico, README, SPEC y estado operativo.
9. Abrir la sesión inicial vinculada a la nueva versión.
10. Verificar coherencia y trazabilidad.

### Promover a candidata a cierre

1. Comprobar el criterio de finalización.
2. Fijar las versiones exactas de los componentes.
3. Confirmar estados y evidencias.
4. Congelar provisionalmente la composición.
5. Revisar contradicciones documentales.
6. Registrar la aprobación y actualizar el estado.

### Completar una versión

1. Confirmar la validación humana.
2. Marcar la versión como `completada`.
3. Congelar objetivo, alcance y composición.
4. Cerrar o suceder las sesiones correspondientes.
5. Actualizar documento canónico, README, SPEC y estado PCS.
6. Registrar evidencias y decisión de cierre.
7. Ejecutar las comprobaciones finales.

### Abandonar una versión

1. Registrar el motivo.
2. Mantener `continuada_en` vacío.
3. Identificar la última versión completada disponible.
4. Cerrar las sesiones vinculadas o documentar su destino.
5. Separar los aprendizajes reutilizables de la línea de continuidad.
6. Actualizar documento canónico, README, SPEC y estado.
7. Iniciar cualquier nuevo intento desde la última versión completada.

Si una versión en desarrollo cambia tanto que persigue otro objetivo, no se reescribe retrospectivamente: se abandona y la nueva propuesta parte de la última versión completada.

## Validaciones y condiciones de parada

Antes de abrir, promover, completar o abandonar una versión se comprobará:

- existe una sola versión global vigente;
- el número de versión es único;
- la versión base existe y está completada, salvo `0.0`;
- una versión abandonada no declara continuación;
- base y continuación son recíprocas cuando ambas existen;
- una versión completada mantiene congelados objetivo, alcance y composición;
- todos los componentes requeridos existen y tienen versión exacta;
- los componentes han alcanzado el estado exigido para el cierre;
- el SPEC declara la misma versión global que el documento canónico;
- README, estado PCS y sesiones no contradicen al documento canónico;
- cada sesión pertenece como máximo a una versión global;
- título, contenido y nombre de cada componente declaran la misma versión;
- los enlaces y referencias añadidos resuelven correctamente;
- la documentación en español ha sido revisada ortográficamente.

Si falla una comprobación:

1. no se materializa la transición;
2. se informa de la contradicción concreta;
3. no se corrige mediante una interpretación automática;
4. la propuesta permanece abierta hasta que la persona resuelva el conflicto.

La contradicción actual entre el título `v2.0.0` y la mención interna a `v1.0.4` de `DEFINICION_MVP_PLAYBOOK_COBERTURA_PROFESIONAL_v2_0_0.md` es un ejemplo de incidencia que deberá corregirse antes de considerar apto ese componente para el cierre global.

## Límites de la futura implementación

- No se modificará PCS Core para materializar este sistema local.
- No se convertirá el versionado funcional de Carrera AI en una regla universal para otros hosts.
- No se renombrarán retrospectivamente todos los documentos para incluir la versión global.
- No se asignarán versiones propias a cada nota auxiliar.
- No se abrirá formalmente `2.5` mientras `2.0` no esté completada.
- No se cerrarán todas las sesiones de forma indiscriminada durante una transición.
- No se reinterpretarán las versiones abandonadas como versiones completadas por haber producido aprendizajes útiles.

## Criterios de aceptación de la futura implementación

La implementación se considerará correcta cuando:

1. exista una fuente única que declare `Carrera AI 2.0 — en desarrollo`;
2. la genealogía `0.0`, `0.1`, `0.3`, `0.4`, `1.0-1.6` y `2.0` sea consultable y coherente;
3. README, SPEC, estado PCS y sesiones apunten a la versión correcta sin competir como fuentes de verdad;
4. la composición de `2.0` distinga profundidad, cobertura, Perfil Profesional Accionable y la exclusión de ESCO;
5. el flujo operativo enumere todas las tareas de apertura, promoción, cierre y abandono;
6. las sesiones queden delimitadas por versión global sin perder líneas paralelas legítimas;
7. las validaciones detecten contradicciones de versión antes de materializar una transición;
8. toda la documentación nueva o modificada conserve la ortografía española y enlaces verificables.
