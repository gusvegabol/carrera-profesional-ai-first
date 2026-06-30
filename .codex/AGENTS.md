---
id: codex-agents-pcs
titulo: AGENTS.md — Instrucciones operativas para CODEX en PCS
tipo: instrucciones_codex
sistema: PCS
version: 0.2.4
estado: borrador_operativo
fecha_creacion: 2026-05-23
fecha_ultima_actualizacion: 2026-05-25
autor: Gustavo Vega / ChatGPT
ubicacion: .codex/AGENTS.md
compatibilidad_obsidian: true
compatibilidad_codex: true
documentos_base:
  - README.md
  - INDEX.md
  - core/SEMANTICA_NUCLEAR_PCS.md
  - core/REGLAS_GOBERNANZA_DOCUMENTAL.md
  - core/FLUJO_OPERATIVO_MINIMO.md
  - core/PLAN_CONSTRUCCION_PCS.md
  - core/PROTOCOLO_APLICACION_PCS.md
documentos_condicionales:
  hosts:
    - hosts/hosts.yaml
    - core/FLUJO_CONFIGURACION_HOSTS_PCS.md
control_version:
  esquema: semver
  version_actual: 0.2.4
  ultima_revision: 2026-05-25
  criterio_incremento:
    major: cambios incompatibles en reglas base o comportamiento esperado de CODEX
    minor: nuevas secciones operativas o ampliaciones relevantes
    patch: correcciones menores, redaccion, enlaces o aclaraciones
historial:
  - version: 0.1.0
    fecha: 2026-05-23
    cambio: Creacion inicial del fichero de instrucciones residentes para CODEX.
  - version: 0.2.0
    fecha: 2026-05-23
    cambio: Se anade la regla operativa de hosts y anfitriones PCS y se corrige el frontmatter YAML para compatibilidad con Obsidian.
  - version: 0.2.1
    fecha: 2026-05-23
    cambio: Correccion de formato YAML y limpieza de escapes Markdown innecesarios.
  - version: 0.2.2
    fecha: 2026-05-23
    cambio: Se añade la regla de validacion YAML y frontmatter con PyYAML para CODEX.
  - version: 0.2.3
    fecha: 2026-05-24
    cambio: Se integra la distincion entre sesion de chat, sesion de trabajo PCS y host de trabajo declarado.
  - version: 0.2.4
    fecha: 2026-05-25
    cambio: Se añade la validacion de vocabulario controlado para entidades operativas y sus plantillas.
---

# AGENTS.md — Instrucciones operativas para CODEX en PCS

## 1. Propósito

Este fichero define las instrucciones residentes que CODEX debe seguir cuando trabaje dentro del repositorio Project Continuity System (PCS).

Su función es actuar como capa de entrada operativa para evitar repetir en cada chat las reglas básicas del proyecto.

CODEX debe tratar este documento como instrucciones de trabajo del repositorio, pero no como sustituto de los documentos canónicos del PCS.

---

## 2. Identidad del proyecto

Project Continuity System (PCS) es un sistema reutilizable de continuidad, gobernanza y trazabilidad para proyectos asistidos por IA.

PCS no pertenece a un proyecto concreto.

Debe diseñarse como sistema transversal reutilizable para múltiples proyectos anfitriones.

El objetivo del PCS es evitar la pérdida de:

- contexto;
- estado operativo;
- decisiones;
- acciones;
- trazabilidad;
- continuidad entre sesiones.

---

## 3. Documentos que CODEX debe leer antes de actuar

Antes de planificar, crear, modificar o eliminar documentos, CODEX debe leer, como mínimo:

1. README.md
2. INDEX.md
3. core/SEMANTICA_NUCLEAR_PCS.md
4. core/REGLAS_GOBERNANZA_DOCUMENTAL.md
5. core/FLUJO_OPERATIVO_MINIMO.md

Si la tarea afecta a construcción del sistema, también debe leer:

6. core/PLAN_CONSTRUCCION_PCS.md

Si la tarea afecta a aplicación de PCS en un proyecto anfitrión, también debe leer:

7. core/PROTOCOLO_APLICACION_PCS.md
8. core/FLUJO_HUMANO_CHATGPT_CODEX_PCS.md

Si la tarea afecta a hosts o anfitriones PCS, también debe leer:

9. hosts/hosts.yaml, si existe
10. core/FLUJO_CONFIGURACION_HOSTS_PCS.md

Si la tarea afecta a una entidad concreta, debe leer además el documento de entidad correspondiente:

- core/ENTIDAD_SESION.md
- core/ENTIDAD_ACCION.md
- core/ENTIDAD_DECISION.md
- core/ENTIDAD_ESTADO_PROYECTO.md

Si la tarea usa una plantilla, debe leer la plantilla correspondiente en templates/.

---

## 4. Jerarquía documental

La jerarquía de autoridad documental del PCS es:

1. README.md
2. INDEX.md
3. core/SEMANTICA_NUCLEAR_PCS.md
4. core/REGLAS_GOBERNANZA_DOCUMENTAL.md
5. core/FLUJO_OPERATIVO_MINIMO.md
6. core/PROTOCOLO_APLICACION_PCS.md
7. Documentos de entidades en core/
8. Flujos operativos específicos en core/
9. Plantillas en templates/
10. Guías en docs/
11. Ejemplos en examples/
12. Registro de hosts en hosts/
13. Documentos operativos en .pcs/
14. Prompts auxiliares en prompts/

Si CODEX detecta contradicción entre documentos, debe detenerse y comunicarla antes de modificar nada, salvo que la tarea consista explícitamente en resolver esa contradicción.

---

## 5. Principios nucleares obligatorios

CODEX debe respetar siempre estos principios:

1. Las sesiones son históricas.
2. Las sesiones no son estado operativo vivo.
3. El estado operativo debe residir en entidades específicas.
4. Las acciones representan trabajo accionable.
5. Las decisiones representan determinaciones estables.
6. ESTADO_PROYECTO resume el presente operativo.
7. Toda modificación relevante debe ser trazable.
8. La gobernanza documental va antes que la automatización.
9. Markdown es el formato base del sistema.
10. La simplicidad estructural tiene prioridad sobre la complejidad prematura.

---

## 6. Separación obligatoria entre historia y estado

CODEX no debe inferir estado operativo vivo únicamente desde sesiones históricas.

CODEX no debe confundir una sesion de chat con una sesion de trabajo PCS.

Una SESION puede registrar:

- lo ocurrido;
- contexto;
- razonamientos;
- capa episódica;
- capa semántica;
- acciones derivadas;
- decisiones derivadas;
- documentos afectados;
- rehidratación futura.

Pero una SESION no debe actuar como:

- lista viva de tareas;
- estado actual del proyecto;
- decisión formal;
- backlog operativo;
- fuente única de verdad del presente.

El estado vivo debe mantenerse en:

- acciones;
- decisiones vigentes;
- estado de proyecto;
- problemas, si existieran en fases futuras.

---

## 7. Flujo operativo mínimo obligatorio

Cuando CODEX ejecute trabajo documental relevante dentro de PCS, debe seguir este flujo:

1. Leer contexto base.
2. Identificar la tarea y su alcance.
3. Identificar documentos afectados.
4. Determinar si existe o debe existir una sesión documental.
5. Separar contenido histórico, operativo y normativo.
6. Crear o actualizar acciones si hay trabajo pendiente trazable.
7. Crear o actualizar decisiones si hay determinaciones estables.
8. Actualizar ESTADO_PROYECTO si cambió el presente operativo.
9. Actualizar INDEX.md si cambió la estructura documental oficial.
10. Preparar rehidratación futura cuando se cierre o consolide una sesión.
11. Validar que no se mezclan historia, estado, acciones y decisiones.

---

## 8. Regla de sesiones

Cuando una tarea implique una intervención de trabajo relevante, CODEX debe crear o actualizar una sesión en:

```text
.pcs/sesiones/
```

La sesión debe basarse en:

```text
templates/TEMPLATE_SESION.md
```

Una sesión debe incluir, como mínimo:

- identificación;
- contexto inmediato;
- objetivo;
- capa episódica;
- capa semántica;
- ideas y líneas cognitivas abiertas;
- acciones derivadas;
- decisiones derivadas;
- documentos afectados;
- rehidratación futura;
- trazabilidad;
- checklist de consolidación.

CODEX no debe dejar una sesión como sustituto de acciones, decisiones o estado operativo.

Si el usuario solo declara un host, CODEX debe devolver una rehidratacion minima y no abrir ni actualizar una sesion PCS solo por esa frase.

---

## 9. Regla de acciones

Cuando exista trabajo concreto que requiera seguimiento, CODEX debe crear o actualizar una acción en:

```text
.pcs/acciones/
```

La acción debe basarse en:

```text
templates/TEMPLATE_ACCION.md
```

Una acción debe tener:

- estado;
- prioridad;
- origen;
- criterio de cierre;
- fecha de creación;
- fecha de actualización;
- relación con sesión o decisión cuando corresponda.

Estados válidos:

- pendiente;
- en curso;
- bloqueada;
- completada;
- cancelada.

CODEX no debe crear acciones vagas, imposibles de cerrar o duplicadas.

---

## 10. Regla de decisiones

Cuando exista una determinación estable, CODEX debe crear o actualizar una decisión en:

```text
.pcs/decisiones/
```

La decisión debe basarse en:

```text
templates/TEMPLATE_DECISION.md
```

Una decisión debe registrar:

- qué se decidió;
- motivo;
- contexto;
- alternativas descartadas;
- impacto esperado;
- alcance;
- vigencia;
- relaciones con sesiones, acciones o decisiones previas.

Estados válidos:

- propuesta;
- vigente;
- sustituida;
- archivada.

CODEX no debe esconder decisiones importantes dentro de sesiones.

---

## 11. Regla de estado de proyecto

Cuando cambie el presente operativo del proyecto, CODEX debe crear o actualizar el estado correspondiente en:

```text
.pcs/estado/
```

El estado debe basarse en:

```text
templates/TEMPLATE_ESTADO_PROYECTO.md
```

ESTADO_PROYECTO debe ser:

- breve;
- vivo;
- accionable;
- consultable rápidamente;
- trazable hacia sesiones, acciones y decisiones.

No debe convertirse en crónica histórica ni absorber el detalle completo de sesiones anteriores.

---

## 12. Aplicación de PCS en proyectos anfitriones

Cuando PCS se aplique a un proyecto anfitrión, CODEX debe respetar esta separación:

- El repositorio project-continuity-system contiene el sistema PCS reutilizable.
- La carpeta .pcs/ dentro de un proyecto anfitrión contiene la memoria operativa PCS de ese proyecto.
- PCS no debe invadir ni reorganizar la estructura propia del proyecto anfitrión salvo instrucción explícita del usuario.

En un proyecto anfitrión, CODEX solo debe gobernar por defecto:

```text
.pcs/
```

No debe modificar por iniciativa propia:

- src/
- tests/
- docs/ propios del anfitrión;
- README.md propio del anfitrión;
- documentación funcional o técnica no perteneciente a PCS;
- configuración de la aplicación anfitriona.

Salvo que el usuario lo pida explícitamente.

---

## 13. Regla de hosts y anfitriones PCS

Cuando CODEX trabaje con hosts o anfitriones PCS, debe leer:

- hosts/hosts.yaml, si existe.
- core/FLUJO_CONFIGURACION_HOSTS_PCS.md.
- core/FLUJO_HUMANO_CHATGPT_CODEX_PCS.md, si la tarea afecta a la interfaz conversacional o a la rehidratacion minima.

CODEX no debe inferir un host de trabajo declarado global.

Debe pedir o identificar siempre el ámbito operativo concreto antes de actuar.

Si el usuario solo dice "Vamos a trabajar con el host XXXXX", debe resolver el alias, consultar el estado disponible y devolver una rehidratacion minima sin abrir ni actualizar una sesion PCS por esa frase.

CODEX debe usar alias como identificador operativo humano del anfitrión.

CODEX no debe pedir ni editar host_id manualmente.

CODEX no debe editar hosts/hosts.yaml fuera de los flujos definidos.

CODEX no debe cambiar el nombre fijo de la carpeta .pcs.

Si el flujo de hosts no está definido, no existe o entra en contradicción con documentos nucleares, CODEX debe detenerse y pedir aclaración.

---

## 14. Carpeta prompts/

La carpeta prompts/ puede usarse para documentos temporales de transferencia a CODEX, como prompts largos, instrucciones de ejecución o textos preparados para copiar en otro chat.

Reglas:

1. prompts/ no forma parte del núcleo canónico del PCS.
2. prompts/ no debe tratarse como fuente normativa.
3. prompts/ no sustituye sesiones, acciones, decisiones ni estado.
4. Los documentos de prompts/ deben considerarse auxiliares y operativos.
5. Si un prompt contiene una decisión estable, debe formalizarse como DECISION.
6. Si un prompt contiene trabajo pendiente, debe derivarse a ACCION.
7. Si un prompt contiene contexto histórico relevante, debe quedar trazado en SESION.
8. Si CODEX debe entregar un prompt completo para otra ejecucion, ese contenido debe vivir en un nuevo documento canvas Markdown y el chat solo debe resumirlo.

---

## 15. Creación y modificación de documentos oficiales

Antes de crear un documento oficial nuevo, CODEX debe comprobar:

1. Qué problema resuelve.
2. Si es reutilizable.
3. Si pertenece a core/, templates/, docs/, examples/ o .pcs/.
4. Si duplica contenido existente.
5. Si debería ser una sección de otro documento.
6. Si debe aparecer en INDEX.md.
7. Qué documentos deben referenciarlo.

CODEX no debe crear documentos nuevos solo porque parezcan útiles.

---

## 16. Regla de INDEX.md

CODEX debe actualizar INDEX.md cuando:

- cree un documento oficial;
- elimine un documento oficial;
- mueva un documento oficial;
- cambie el estado documental de un documento oficial;
- cambie la estructura real del repositorio.

CODEX no debe actualizar INDEX.md para reflejar documentos temporales, borradores auxiliares o prompts operativos salvo que el usuario lo indique.

---

## 17. Markdown limpio y enlaces

CODEX debe usar Markdown limpio, legible y compatible con Obsidian.

Reglas:

1. No usar comillas invertidas en títulos o nombres enlazables.
2. No escribir encabezados como código.
3. Reservar comillas invertidas para comandos, rutas técnicas o fragmentos de código.
4. Mantener nombres de documentos y encabezados navegables.
5. Usar enlaces claros y estables.
6. No crear enlaces a documentos inexistentes salvo que estén marcados como pendientes.

Correcto:

```markdown
## Entidad SESION
```

Incorrecto:

```markdown
## `Entidad SESION`
```

---

## 17.1 Validacion de YAML y frontmatter

Cuando debas validar YAML o frontmatter en documentos Markdown, usa directamente Python con PyYAML como metodo preferente.

No pierdas tiempo buscando validadores YAML en PowerShell ni intentando comandos no garantizados del entorno.

Procedimiento recomendado:

1. Usar una invocacion minima y determinista, acotada al archivo o bloque realmente afectado.

   Si el documento es Markdown con frontmatter, extraer y validar solo el frontmatter necesario.

   No validar masivamente archivos no afectados.

2. En PowerShell, comprobar primero como se resuelve Python:

   - si `python` aparece como `Application` y no hay senales de envoltorio problematico, puede usarse;
   - si `python` aparece como `Function`, preferir una via mas determinista:
     - primero, la ruta absoluta a `python.exe` si ya esta identificada y es estable;
     - despues, `py`;
     - usar `python` solo si no hay alternativa razonable.

3. Comprobar primero si PyYAML esta disponible con la misma via elegida:

   `C:\ruta\python.exe -c "import yaml; print('PyYAML disponible')"`

   o:

   `py -c "import yaml; print('PyYAML disponible')"`

4. Para validar un bloque YAML o frontmatter, usar un script Python minimo con `yaml.safe_load`.

   Hacer un unico intento automatico rapido.

5. Si PyYAML no esta instalado, informar claramente del bloqueo y proponer:

   `py -m pip install pyyaml`

6. Si hay timeout, bloqueo, quoting fragil, error del shell o fallo de entorno, no repetir indefinidamente.

   Registrar el comando exacto usado.

   Aplicar verificacion textual degradada y declararlo explicitamente en el informe.

   Si el YAML es critico y no pudo validarse automaticamente, dejar riesgo explicito.

7. No modificar documentos solo porque el validador no este disponible.

8. Si la validacion falla, indicar:
   - archivo afectado;
   - error YAML;
   - linea aproximada si esta disponible;
   - correccion propuesta.

Esta regla existe para evitar ciclos innecesarios buscando herramientas de validacion en PowerShell cuando el metodo preferente del proyecto es PyYAML.

---

## 18. Límites durante PCS 1.0

Durante PCS 1.0, CODEX no debe introducir sin autorización explícita:

- automatizaciones avanzadas;
- agentes multiagente;
- dashboards;
- bases vectoriales;
- sistemas RAG;
- cron jobs;
- integraciones MCP;
- APIs;
- scripts complejos;
- nuevas entidades nucleares.

PCS 1.0 llega hasta sesión consolidada y validación del flujo operativo mínimo.

---

## 19. Fase activa

La fase activa debe determinarse leyendo:

```text
core/PLAN_CONSTRUCCION_PCS.md
```

CODEX no debe ejecutar tareas de fases futuras si las fases previas no están suficientemente estables.

Si una tarea parece pertenecer a una fase futura, CODEX debe indicarlo y proponer una alternativa compatible con la fase actual.

---

## 20. Planificación antes de actuar

Antes de modificar archivos, CODEX debe:

1. Explicar brevemente qué entiende de la tarea.
2. Identificar documentos afectados.
3. Indicar si creará, modificará o solo revisará.
4. Señalar riesgos de gobernanza.
5. Proponer un plan corto.
6. Esperar confirmación cuando el cambio sea estructural o pueda afectar a documentos canónicos.

Si el usuario solo declara un host, CODEX debe resolver el alias, consultar el estado correspondiente y devolver una rehidratacion minima antes de continuar.

Para cambios menores y claramente solicitados, puede actuar directamente manteniendo trazabilidad.

---

## 21. Validación antes de cerrar una tarea

Antes de dar una tarea por terminada, CODEX debe comprobar:

- que respetó la semántica nuclear;
- que no mezcló historia con estado;
- que no creó documentos fuera de estructura;
- que no duplicó entidades;
- que actualizó INDEX.md si correspondía;
- que las acciones tienen criterio de cierre;
- que las decisiones tienen vigencia clara;
- que ESTADO_PROYECTO no se convirtió en crónica;
- que las sesiones no quedaron como estado vivo;
- que los enlaces y encabezados son limpios;
- que el resultado es reutilizable y trazable;
- que no se ha inferido un host de trabajo declarado global;
- que no se ha confundido una sesion de chat con una sesion de trabajo PCS;
- que los valores usados en campos controlados pertenecen al vocabulario declarado en la entidad canónica y en su plantilla;
- que hosts/hosts.yaml no se ha editado fuera del flujo definido.

---

## 22. Informe final obligatorio

Al terminar una intervención, CODEX debe responder con un informe breve que incluya:

1. Documentos leídos.
2. Documentos creados.
3. Documentos modificados.
4. Sesión creada o actualizada.
5. Acciones creadas o actualizadas.
6. Decisiones creadas o actualizadas.
7. ESTADO_PROYECTO actualizado o no.
8. INDEX.md actualizado o no.
9. Hosts o anfitriones afectados, si aplica.
10. Riesgos, dudas o contradicciones detectadas.
11. Próximo paso recomendado.

Si no realizó alguna de estas operaciones, debe indicarlo como no aplica o no realizado.

---

## 23. Regla de detención

CODEX debe detenerse y pedir aclaración si detecta:

- contradicción entre documentos nucleares;
- riesgo de modificar estructura canónica sin autorización;
- posible creación de entidad nueva no aprobada;
- mezcla entre reglas universales y necesidades de un proyecto anfitrión;
- ambigüedad sobre si una información es sesión, acción, decisión o estado;
- instrucción del usuario que contradiga la semántica nuclear vigente;
- ambigüedad sobre el anfitrión operativo concreto;
- intento de editar hosts/hosts.yaml sin seguir el flujo definido;
- intento de modificar manualmente host_id;
- intento de cambiar el nombre fijo de .pcs.

---

## 24. Regla de prioridad

Cuando exista tensión entre varias opciones, CODEX debe priorizar:

1. Continuidad entre sesiones.
2. Claridad operativa.
3. Trazabilidad histórica.
4. Separación entre contexto y estado.
5. Reutilización transversal.
6. Mantenibilidad.
7. Simplicidad estructural.
8. Automatización futura.
9. Legibilidad humana.

---

## 25. Regla final

CODEX no debe comportarse como un generador libre de documentos.

Debe comportarse como un agente documental disciplinado dentro del PCS.

Su tarea principal no es producir más contenido.

Su tarea principal es mantener continuidad, gobernanza y trazabilidad sin romper la semántica del sistema.

---

## Control de versiones

| Versión | Fecha      | Estado             | Cambio principal                                                                                                          |
| ------- | ---------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| 0.1.0   | 2026-05-23 | Borrador operativo | Creación inicial del fichero de instrucciones residentes para CODEX.                                                      |
| 0.2.0   | 2026-05-23 | Borrador operativo | Se añade la regla operativa de hosts y anfitriones PCS y se corrige el frontmatter YAML para compatibilidad con Obsidian. |
| 0.2.1   | 2026-05-23 | Borrador operativo | Corrección de formato YAML y limpieza de escapes Markdown innecesarios.                                                  |
| 0.2.2   | 2026-05-23 | Borrador operativo | Se añade la regla de validacion YAML y frontmatter con PyYAML para CODEX.                                               |
| 0.2.3   | 2026-05-24 | Borrador operativo | Se integra la distinción entre sesión de chat, sesión de trabajo PCS y host de trabajo declarado.                       |
| 0.2.4   | 2026-05-25 | Borrador operativo | Se añade la validación de vocabulario controlado para entidades operativas y sus plantillas.                            |

## Criterio de versionado

Este documento usa versionado semántico:

- MAJOR: cambios incompatibles en reglas base o comportamiento esperado de CODEX.
- MINOR: nuevas secciones operativas o ampliaciones relevantes.
- PATCH: correcciones menores, redacción, enlaces o aclaraciones.
