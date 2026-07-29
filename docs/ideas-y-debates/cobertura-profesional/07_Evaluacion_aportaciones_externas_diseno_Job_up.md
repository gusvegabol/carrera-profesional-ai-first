---
id: evaluacion-aportaciones-externas-diseno-job-up
titulo: Evaluación de aportaciones externas al diseño de Job-up
estado: debate_abierto
fecha: 2026-07-29
ambito: job-up
fuente: revisión externa del plan de implantación
---

# Evaluación de aportaciones externas al diseño de Job-up

## Propósito y estado

Este documento conserva cinco recomendaciones recibidas durante la revisión
externa del diseño y plan de Job-up, junto con una evaluación razonada. No es
por sí mismo una decisión PCS ni una fuente de gobernanza. Tras las
resoluciones explícitas de la persona responsable, los acuerdos aplicables se
han incorporado a la especificación aprobada y al plan de implantación. Cada
propuesta se ha valorado de forma independiente antes de adoptarla, adaptarla o
descartarla.

El criterio de evaluación es reforzar la seguridad, la claridad y la capacidad
de evolución de Job-up sin duplicar autoridades, fragmentar prematuramente la
documentación ni automatizar cambios que requieren aprobación humana.

---

## 1. Protocolo de triage de privacidad

### Recomendación recibida

Incorporar un «Protocolo de Alerta de Privacidad» en el README y las skills.
Cuando se detecte información sensible sin consentimiento explícito para una
candidatura, se marcaría con `[ALERTA_PRIVACIDAD]` y la ejecución se detendría
hasta que la persona usuaria confirme autorización.

### Respuesta y evaluación

La aportación identifica correctamente un riesgo real: la regla actual de
«pedir autorización» necesita ser operativa, verificable y común a todas las
entradas de Job-up. Es una mejora sustantiva.

No conviene, sin embargo, adoptar literalmente la etiqueta propuesta ni la
idea de que la detección impide todo procesamiento. El agente necesita leer lo
mínimo para identificar que existe un dato sensible, y repetir una etiqueta al
lado del dato puede aumentar su exposición. Además, no toda información
personal aportada directamente por la persona usuaria es inválida: puede haber
sido compartida intencionadamente, pero no autorizada aún para incorporarla a
una candidatura concreta.

La mejora de fondo debe ser una **compuerta de uso de datos privados**, no una
etiqueta de contenido. La futura regla debería distinguir:

1. **Dato factual profesional:** puede emplearse si procede de la fuente
   factual autorizada de Job-up.
2. **Dato privado aportado para una candidatura concreta:** se puede consultar
   y usar solo después de que la persona usuaria confirme expresamente su uso
   para ese expediente.
3. **Dato privado no solicitado o con autorización ambigua:** no se copia,
   no se incorpora a documentos ni se propaga; se solicita una confirmación
   mínima de uso antes de continuar con la parte que lo requiera.

La detención debe ser proporcional: se bloquea la preparación que necesite el
dato privado, no el análisis público o factual de la oferta que pueda hacerse
sin él. El expediente debe registrar el bloqueo de autorización sin reproducir
el dato sensible.

### Posición inicial

**Adoptar la necesidad, reformular el mecanismo.** Se propone añadir una
compuerta de autorización de datos privados al diseño de README y skills, con
un registro mínimo de autorización o bloqueo. No se propone usar la etiqueta
`[ALERTA_PRIVACIDAD]` ni detener trabajo independiente de esos datos.

### Pregunta para decidir

¿La autorización debe ser una confirmación explícita en el chat para cada
candidatura o puede reutilizarse una autorización escrita previamente en la
ficha privada del expediente?

### Resolución de la persona responsable

Puede reutilizarse una autorización escrita previamente en la ficha privada
del expediente. Esa autorización debe estar delimitada de forma expresa a la
candidatura correspondiente; no constituye autorización global para otras
ofertas, empresas ni usos posteriores.

---

## 2. Ciclo de vida de los artefactos

### Recomendación recibida

Asignar a cada artefacto operativo un campo YAML `estado` con los valores
`borrador`, `pendiente_aprobacion`, `activo`, `completado` y `archivado`, y
trasladar automáticamente al histórico lo archivado o sustituido.

### Respuesta y evaluación

La recomendación acierta al señalar que el estado de un artefacto y su relación
con el histórico necesitan reglas explícitas. No obstante, un único vocabulario
para todos los documentos confundirá categorías diferentes:

- un playbook tiene versiones `vigente` y `retirada`;
- una candidatura tiene estados de preparación, aprobación, presentación o
  cierre;
- una fuente factual puede estar vigente sin estar «activa» en el sentido de
  una candidatura;
- un documento completado continúa siendo evidencia útil del expediente y no
  debe pasar por ello al histórico.

Tampoco es adecuado automatizar el traslado a `historico/`. La organización
aprobada exige confirmación humana para archivar, preservación de la ruta de
procedencia y una razón explícita. Un estado describe la situación de un
artefacto; no autoriza por sí solo una operación de movimiento irreversible.

La mejora de fondo es un **modelo de ciclo de vida por tipo documental**:

| Tipo de documento | Estado recomendado | Paso al histórico |
| --- | --- | --- |
| Playbook versionado | `vigente` / `retirada` | Al ser sustituido, con copia histórica y trazabilidad Git. |
| Registro de candidatura | Estados propios del proceso, incluido `pendiente_de_aprobacion` | No por completarse; permanece en su expediente salvo decisión posterior. |
| Fuente factual | Estado de vigencia y fecha de revisión, si se necesita | Solo cuando sea sustituida o deje de ser aplicable, con decisión humana. |
| Plantilla | `vigente` / `retirada` | Cuando una sustitución aprobada la haga obsoleta. |

### Posición inicial

**Adoptar el principio, rechazar el esquema universal y el archivado
automático.** El control de versión se limitará a fuentes y plantillas, según
su propio tipo documental. El modelo de ciclo de vida de los demás artefactos
debe diseñarse después por tipos documentales, sin adelantarlo como una
migración masiva.

### Pregunta para decidir

¿Quieres que el siguiente diseño limitado cubra primero el ciclo de vida de
las candidaturas, o el de fuentes y plantillas?

### Resolución de la persona responsable

Las candidaturas no requieren versionado trazable: no mejora su gestión y
añadiría complejidad sin valor operativo. El control de versión se limitará a
fuentes y plantillas, cada una según su propio tipo documental. Esta resolución
refuerza que completar o cerrar una candidatura no autoriza por sí mismo su
traslado a `historico/`.

---

## 3. Separación entre arquitectura y operación

### Recomendación recibida

Extraer «Modelo mental», «Límites» y «Matriz de artefactos» a
`docs/superpowers/job-up/architecture/` y convertir el README de Job-up en un
panel de control operativo de enlaces y pasos.

### Respuesta y evaluación

La preocupación por el crecimiento del README es legítima. Sin una frontera
clara, un documento de entrada puede convertirse en una mezcla difícil de
mantener. La recomendación aporta una señal útil: hay que diseñar el README de
modo que pueda escindirse en el futuro sin cambiar el punto de entrada.

La extracción propuesta es prematura y contradice la decisión ya aprobada de
mantener un único README como referencia funcional de Job-up. Separar ahora
los conceptos obliga a humanos y agentes a saltar entre documentos antes de
que la complejidad lo justifique. Además, `docs/superpowers/` es memoria de
diseño y planificación, no el lugar de documentación funcional cotidiana.

La mejora de fondo es definir una **frontera de extracción**, no crearla aún.
El README conservará dos capas explícitas: modelo mental y uso operativo. Se
podrá extraer la primera a `docs/arquitectura/` —no a `docs/superpowers/`— si
se cumplen conjuntamente estos criterios:

1. la capa conceptual necesita varias secciones que no sirven para operar
   diariamente;
2. su mantenimiento obliga a navegar repetidamente por un documento demasiado
   largo para ser una entrada útil;
3. existe una arquitectura de Job-up estable que merece una fuente propia;
4. el README puede seguir explicando el propósito y enlazar al detalle sin
   perder autonomía como punto de entrada.

### Posición inicial

**Adoptar la frontera de extracción, no la separación actual.** El plan debe
exigir un README internamente estructurado y dejar documentado el umbral para
extraer arquitectura cuando el crecimiento lo justifique.

### Pregunta para decidir

¿Quieres fijar desde ahora una señal cuantitativa orientativa —por ejemplo,
longitud o número de secciones— además de los criterios cualitativos?

### Resolución de la persona responsable

El README se estructurará desde la primera implantación con una frontera clara
entre «Modelo mental de Job-up» y «Uso operativo de Job-up». Esa organización
debe permitir extraer en el futuro la arquitectura conceptual sin rehacer el
resto del documento ni cambiar el README como punto de entrada. No se fija por
ahora un umbral cuantitativo: la extracción dependerá del crecimiento y de los
criterios cualitativos ya definidos.

---

## 4. Creación de sesión previa confirmación

### Recomendación recibida

Permitir que `job-up-candidatura-oferta` cree una sesión Job-up si no hay una
abierta, tras pedir una confirmación humana de «Sí/No».

### Respuesta y evaluación

La recomendación intenta reducir una fricción real: recibir una oferta y tener
que invocar después otra skill para abrir el contexto de trabajo. Sin embargo,
la solución mezcla responsabilidades que el diseño aprobó separar.

`job-up-inicia-sesion` gobierna el ciclo PCS: identifica y cierra sesiones
anteriores cuando procede, crea la nueva sesión y actualiza la traza mínima del
estado. Dar esa capacidad a la skill de oferta duplicaría una lógica sensible,
podría generar divergencias en los cierres y convertir una petición de análisis
en una mutación de PCS de mayor alcance.

Una confirmación «Sí/No» no elimina esa duplicidad ni informa suficientemente
de qué sesiones se cerrarán, cuál será la relación de continuidad o qué estado
se actualizará. Por tanto, no proporciona el mismo nivel de gobernanza que la
skill de inicio.

La mejora de fondo es hacer el traspaso menos friccional sin fusionar las dos
responsabilidades. Cuando no haya una única sesión abierta,
`job-up-candidatura-oferta` debe detenerse y devolver un siguiente gesto
concreto: indicar que se invoque `job-up-inicia-sesion`, explicar que abrirá el
bloque PCS necesario y conservar la oferta aportada como entrada pendiente de
vinculación. No se crea sesión ni se modifica el estado hasta la invocación
explícita de la skill de inicio.

### Posición inicial

**Rechazar la creación automática de sesión y adoptar una derivación asistida.**
La separación entre launcher y skill especializada protege la coherencia del
ciclo PCS. La mejora admisible consiste en presentar una instrucción de
continuación inequívoca, no en ejecutar la mutación desde la skill de oferta.

### Pregunta para decidir

¿El traspaso debe limitarse a explicar el siguiente comando o debe incluir un
resumen no persistente de la oferta que el usuario pueda reutilizar al iniciar
la sesión?

### Resolución de la persona responsable

Se sustituye la regla anterior por este comportamiento:

1. Si hay varias sesiones Job-up abiertas o no puede determinarse una única
   sesión adecuada, la IA pide a la persona usuaria que elija la sesión a la
   que debe vincularse el trabajo.
2. Si no hay ninguna sesión Job-up abierta, la IA lo informa y pregunta si
   desea ejecutar en ese momento `job-up-inicia-sesion`.
3. Solo tras una respuesta afirmativa explícita se invoca
   `job-up-inicia-sesion`; la skill de oferta no crea directamente la sesión
   ni reproduce su lógica PCS.

Así se elimina una fricción evitable, pero se conserva una única autoridad
operativa para abrir sesiones y actualizar su trazabilidad.

---

## 5. Investigación y networking

### Recomendación recibida

Añadir una tercera columna «Investigación/Networking» a la matriz de
artefactos, con análisis de empresa sin oferta y seguimiento de contactos que
no son candidaturas directas.

### Respuesta y evaluación

La observación revela una necesidad potencial válida: Job-up puede generar
valor antes de que exista una oferta y algunas relaciones profesionales no
encajan en una candidatura ni en una presentación espontánea. Nombrar ese
espacio evita que se fuerce una actividad de investigación dentro de un
expediente de candidatura.

No basta, sin embargo, con añadir una columna a la matriz. «Investigación» y
«networking» son procesos distintos, con objetos, estados y límites propios.
La investigación puede ser documental y sin contacto; el networking introduce
personas, datos personales, consentimiento y posibles acciones externas. Una
única categoría ocultaría precisamente las salvaguardas que la propuesta busca
mejorar.

La mejora de fondo es abrir una línea de diseño futura denominada, de forma
provisional, **investigación de empresas y relaciones profesionales**. Antes de
integrarla en Job-up deberá definir:

1. qué resultado produce cada subflujo;
2. qué datos de empresa y de contacto puede conservar;
3. qué autorización exige cualquier comunicación externa;
4. qué artefactos son registros vivos y cuáles son expedientes cerrados;
5. si comparte el seguimiento de candidaturas o requiere un registro separado.

Mientras no exista ese diseño, una presentación espontánea dirigida a una
empresa concreta seguirá usando su proceso actual. La mera investigación de
empresa no se registrará como candidatura ni como contacto de networking.

### Posición inicial

**Adoptar la necesidad como línea futura, no añadir aún una tercera columna.**
Se evita así ampliar la primera implantación con un subsistema que requiere su
propio diseño, controles de privacidad y reglas de contacto.

### Pregunta para decidir

¿Quieres abrir esta línea futura como una sesión PCS independiente o dejarla
solo registrada como posibilidad de evolución de Job-up hasta que surja un
caso de uso real?

### Resolución de la persona responsable

Se crea una sesión PCS independiente y en pausa para conservar esta línea de
trabajo. No autoriza investigación, registro de contactos, comunicaciones
externas ni cambios en la primera implantación de Job-up.

Sesión creada: [[sesion-20260729-1614-investigacion-empresas-relaciones-profesionales]].

---

## Síntesis provisional

| Aportación | Elemento valioso | Posición inicial |
| --- | --- | --- |
| Triage de privacidad | Hacer verificable la autorización de datos privados | Adoptar, reformulado como compuerta de uso. |
| Ciclo de vida de artefactos | Distinguir estado y conservación histórica | Adoptar por tipo documental; sin automatismo. |
| Arquitectura y operación | Preparar el README para crecer | Mantener README único y definir umbral de extracción. |
| Auto-sesión | Reducir fricción entre oferta y contexto PCS | Rechazar mutación automática; adoptar derivación asistida. |
| Investigación y networking | Reconocer actividad previa o lateral a la candidatura | Registrar como línea futura de diseño. |

## Próximo paso sugerido

Resolver primero la propuesta 1. Su definición condiciona cualquier flujo que
use datos privados, incluidas las tres modalidades de entrada de una oferta.
