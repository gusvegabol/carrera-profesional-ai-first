---
id: design-playbook-guion-adaptacion-cv
titulo: Diseño — PLAYBOOK_GUION_ADAPTACION_CV
version: 0.3.1
sustituye: 0.3.0
estado_documento: pendiente_aprobacion_humana
nota_estado: |-
  Este valor pertenece a un eje de estado ("documento de diseño de fase")
  todavía no declarado formalmente en el glosario de la SPEC (sección 8 de
  SPEC v0.4.0). Se usa aquí por continuidad, pendiente de registrar ese
  quinto eje cuando se actualice la SPEC.
fecha_version: 2026-08-06
host: carrera-ai
rama: job-up
tipo_documento: diseño_de_fase
fase: PLAYBOOK_GUION_ADAPTACION_CV
artefacto_salida: guion-adaptacion-cv.md
gate_entrada: GATE-CANDIDATURA-GUION
gate_salida: GATE-GUION-CV-CONTENIDO
caso_principal: CAND-2026-020
caso_contraste: CAND-2026-019
spec_referencia: SPEC-Arquitectura-modular-generación-candidatura-v0-4-0.md
defectos_relacionados:
  - DEF-ARQ-001
audiencias:
  - humano
  - agente_ia_planificador
  - agente_ia_ejecutor
---
  
# Diseño — `PLAYBOOK_GUION_ADAPTACION_CV`  
  
## 1. Propósito  
  
`PLAYBOOK_GUION_ADAPTACION_CV` transforma la estrategia común ya aprobada de una candidatura en **decisiones editoriales específicas para el CV**.  
  
Produce:  
  
`guion-adaptacion-cv.md`  
  
Ese artefacto debe permitir que una fase posterior pueda generar el contenido del CV sin tener que:  
  
* volver a interpretar la oferta;  
* volver a decidir si merece la pena competir;  
* reconstruir el posicionamiento;  
* reinterpretar carencias;  
* seleccionar desde cero qué trayectoria mostrar;  
* volver a decidir qué evidencias sostienen el encaje.  
  
El guion:  
  
* no es un borrador de CV;  
* no redacta el CV final;  
* no diseña visualmente el CV;  
* no genera DOCX, PDF o LaTeX;  
* no redefine la estrategia;  
* no modifica hechos.  
  
Su pregunta central es:  
  
> Dada una estrategia de candidatura ya aprobada, ¿qué parte verdadera de la trayectoria profesional debe mostrar este CV, con qué importancia, para demostrar qué, en qué orden y bajo qué límites?  
  
---  
  
# 2. Posición dentro de la arquitectura  
  
El flujo relevante es:  
  
```text  
datos-core-busqueda.md  
 ↓  
analisis-oferta.md  
 ↓  
candidatura.md  
 ↓  
GATE-CANDIDATURA-GUION  
 ↓  
PLAYBOOK_GUION_ADAPTACION_CV  
 ↓  
guion-adaptacion-cv.md  
 ↓  
GATE-GUION-CV-CONTENIDO  
 ↓  
futura fase de generación de contenido del CV  
 ↓  
CV  
```  
  
Responsabilidades:  
  
```text  
candidatura.md  
→ estrategia común de candidatura  
  
guion-adaptacion-cv.md  
→ adaptación editorial específica del CV  
```  
  
`guion-adaptacion-cv.md` no sustituye a `candidatura.md`.  
  
No constituye una segunda fuente estratégica.  
  
---  
  
# 3. Separación de responsabilidades CV/carta  
  
La separación entre CV y carta es una **decisión arquitectónica**, no una incertidumbre.  
  
La decisión que deberá registrarse en la siguiente actualización de la SPEC es:  
  
```text  
ARQ-XX — Separación de responsabilidades CV/carta  
  
PLAYBOOK_GUION_ADAPTACION_CV es exclusivo del CV.  
  
candidatura.md conserva la estrategia común de candidatura  
para los distintos adaptadores documentales.  
  
La existencia futura de un adaptador de carta no modifica  
la responsabilidad de PLAYBOOK_GUION_ADAPTACION_CV.  
  
Estado: vigente.  
```  
  
`ARQ-XX` es un identificador provisional.  
  
La numeración definitiva se resolverá cuando esta decisión se incorpore formalmente a la SPEC.  
  
La arquitectura concreta de la rama de carta **no está decidida**.  
  
Ese aplazamiento se registra formalmente en la sección **32. Registro de incertidumbres** de este documento.  
  
La incertidumbre:  
  
* no bloquea este diseño;  
* no bloquea el plan;  
* no bloquea la implementación de `PLAYBOOK_GUION_ADAPTACION_CV`;  
* no autoriza a Work a diseñar la rama de carta.  
  
---  
  
# 4. Contrato normativo de fase  
  
Esta fase debe poder expresarse mediante los diez campos contractuales establecidos por la arquitectura.  
  
## OBJETIVO  
  
Traducir una estrategia de candidatura aprobada a un mapa editorial específico del CV, completo, factual, trazable y suficientemente determinista para habilitar la fase posterior.  
  
## PRECONDICIONES  
  
* `GATE-CANDIDATURA-GUION: aprobado`;  
* `candidatura.md` existente y vigente;  
* `analisis-oferta.md` resoluble;  
* fuentes factuales autorizadas resolubles;  
* ausencia de bloqueo activo;  
* candidatura no presentada cuando una actualización factual pueda afectar artefactos derivados.  
  
## ENTRADAS  
  
Entrada principal:  
  
* `candidatura.md`.  
  
Referencias autorizadas:  
  
* `datos-core-busqueda.md`;  
* `analisis-oferta.md`;  
* evidencias factuales referenciadas por la candidatura.  
  
## RESPONSABILIDADES  
  
* seleccionar contenido profesional;  
* decidir presencia;  
* decidir obligatoriedad;  
* asignar peso editorial;  
* ordenar;  
* definir nivel de detalle;  
* relacionar contenido con criterios de selección;  
* traducir advertencias a límites de redacción;  
* construir arquitectura editorial;  
* gobernar el primer escaneo;  
* producir un brief cerrado y derivado.  
  
## FUERA_DE_RESPONSABILIDAD  
  
* cambiar estrategia;  
* modificar hechos;  
* incorporar evidencia nueva directamente;  
* decidir arquitectura de carta;  
* redactar CV final;  
* diseñar presentación visual;  
* generar formatos finales;  
* enviar candidatura.  
  
## SALIDA  
  
`guion-adaptacion-cv.md`  
  
## POSTCONDICIONES  
  
La fase siguiente debe conocer de forma explícita:  
  
* qué incluir;  
* qué omitir;  
* qué conservar obligatoriamente;  
* qué priorizar;  
* qué minimizar;  
* qué demostrar;  
* qué evitar;  
* qué límites respetar.  
  
No debe necesitar reconstruir la estrategia.  
  
## DEFECTOS_CRITICOS  
  
Son críticos, entre otros:  
  
* invención factual;  
* reinterpretación estratégica;  
* pérdida de trazabilidad;  
* omisión engañosa;  
* falsa experiencia;  
* alteración de cronología;  
* propagación factual asumida sin contrato arquitectónico;  
* brief que contradiga el cuerpo;  
* aprobación automática del gate por IA;  
* avance a una fase posterior aún no diseñada como si ya fuera ejecutable.  
  
`DEF-ARQ-001` permanece además como defecto arquitectónico abierto relacionado.  
  
## GATE_SIGUIENTE  
  
`GATE-GUION-CV-CONTENIDO`  
  
## CRITERIOS_DE_ACEPTACION  
  
Los definidos en la sección 19.  
  
---  
  
# 5. Principio de responsabilidad  
  
El guion puede tomar:  
  
> decisiones editoriales.  
  
No puede tomar:  
  
> decisiones estratégicas de candidatura.  
  
Frontera:  
  
```text  
candidatura.md  
→ qué queremos demostrar y desde qué posicionamiento  
  
guion-adaptacion-cv.md  
→ qué contenido del CV debe hacerlo visible y con qué jerarquía  
```  
  
Si para construir el guion resulta necesario cambiar:  
  
* la razón para competir;  
* el posicionamiento;  
* una evidencia estratégica;  
* una afirmación excluida;  
* una carencia;  
* un riesgo;  
* un límite;  
  
el problema pertenece a una fase anterior.  
  
---  
  
# 6. Autoridad de las fuentes  
  
## 6.1 `candidatura.md` — autoridad estratégica  
  
Gobierna:  
  
* decisión estratégica;  
* tesis;  
* ángulo;  
* posicionamiento;  
* evidencias prioritarias;  
* advertencias;  
* carencias;  
* afirmaciones excluidas;  
* límites;  
* bloqueos;  
* estado operativo pertinente.  
  
El guion no puede sustituir ni modificar estas decisiones.  
  
---  
  
## 6.2 `datos-core-busqueda.md` — autoridad factual  
  
Gobierna la factualidad profesional.  
  
Puede aportar:  
  
* experiencias;  
* cargos;  
* fechas;  
* responsabilidades;  
* funciones;  
* logros;  
* resultados;  
* métricas;  
* herramientas;  
* tecnologías;  
* formación;  
* certificaciones;  
* competencias demostradas;  
* cronología;  
* otros hechos profesionales autorizados.  
  
Que un dato exista en el core no implica que deba aparecer en el CV.  
  
El guion decide su tratamiento editorial.  
  
---  
  
## 6.3 `analisis-oferta.md` — contexto y trazabilidad  
  
Puede utilizarse para:  
  
* requisitos;  
* responsabilidades;  
* señales de selección;  
* contexto de la oferta;  
* relación entre requisitos y evidencias;  
* comprobación de trazabilidad.  
  
No puede emplearse para reabrir silenciosamente la estrategia ya fijada en `candidatura.md`.  
  
---  
  
## 6.4 Conflicto entre autoridades  
  
Ante una contradicción real entre fuentes:  
  
```text  
datos-core-busqueda.md  
vs  
analisis-oferta.md  
vs  
candidatura.md  
```  
  
el guion debe:  
  
1. detener la decisión afectada;  
2. identificar qué autoridad debe resolverla;  
3. registrar la incidencia;  
4. no elegir la interpretación más conveniente.  
  
---  
  
# 7. Precondiciones operativas  
  
El playbook solo puede iniciar cuando:  
  
```text  
GATE-CANDIDATURA-GUION: aprobado  
```  
  
Además debe comprobar:  
  
* `candidatura.md` existe;  
* el análisis de origen es resoluble;  
* las fuentes factuales necesarias son resolubles;  
* no existe bloqueo activo;  
* el artefacto de candidatura refleja el estado operativo vigente.  
  
Si falla una precondición:  
  
```text  
PLAYBOOK_GUION_ADAPTACION_CV  
→ no inicia  
```  
  
La aprobación del gate de entrada no autoriza:  
  
* generar el CV;  
* generar la carta;  
* presentar la candidatura;  
* alterar el estado a `presentada`.  
  
---  
  
# 8. Qué puede decidir  
  
El playbook puede:  
  
* construir el universo candidato de contenido;  
* seleccionar contenido;  
* omitir contenido;  
* definir obligatoriedad;  
* asignar peso editorial;  
* jerarquizar experiencias;  
* jerarquizar logros;  
* jerarquizar competencias;  
* seleccionar evidencia de apertura;  
* decidir orden editorial;  
* decidir nivel de detalle;  
* relacionar contenido con necesidades de selección;  
* reducir ruido;  
* gestionar sobrecualificación mediante énfasis honesto;  
* trasladar advertencias a restricciones;  
* clasificar léxico;  
* construir el brief derivado.  
  
---  
  
# 9. Qué no puede decidir  
  
No puede:  
  
* modificar hechos;  
* crear experiencia;  
* inventar métricas;  
* inventar responsabilidades;  
* alterar fechas;  
* modificar requisitos de la oferta;  
* cambiar la decisión estratégica;  
* cambiar la tesis;  
* cambiar el posicionamiento;  
* eliminar carencias mediante edición;  
* convertir formación en experiencia;  
* convertir transferibilidad en experiencia literal;  
* convertir automatización en IA;  
* atribuir tecnologías no acreditadas;  
* modificar cargos históricos;  
* ocultar deliberadamente hechos necesarios para interpretar correctamente la trayectoria;  
* redactar el CV definitivo;  
* redactar la carta;  
* diseñar formato visual;  
* producir DOCX, PDF o LaTeX;  
* diseñar la futura infraestructura CV/carta;  
* presentar la candidatura.  
  
---  
  
# 10. Orden normativo de ejecución  
  
El agente debe operar en este orden:  
  
```text  
1. validar precondiciones  
2. cargar estrategia heredada  
3. resolver fuentes factuales  
4. construir universo candidato de contenido  
5. decidir presencia  
6. decidir obligatoriedad  
7. asignar peso editorial  
8. vincular contenido con criterio objetivo  
9. decidir orden y nivel de detalle  
10. construir arquitectura narrativa  
11. definir léxico y límites  
12. generar brief derivado  
13. ejecutar control de primer escaneo  
14. ejecutar control de coherencia  
15. evaluar gate de salida  
```  
  
No debe invertir pasos cuando ello suponga tomar una decisión antes de disponer de la información que la gobierna.  
  
Este orden constituye un **algoritmo normativo de fase**, no una sugerencia.  
  
---  
  
# 11. Universo candidato de contenido  
  
El playbook no debe recorrer indiscriminadamente toda la trayectoria y generar una decisión para cada dato existente.  
  
El universo candidato contiene material que cumpla al menos una de estas condiciones:  
  
1. está señalado estratégicamente por `candidatura.md`;  
2. posee relevancia plausible para un requisito o señal de selección;  
3. es necesario para mantener coherencia factual;  
4. es necesario para mantener coherencia cronológica;  
5. puede afectar materialmente a la percepción profesional;  
6. contiene una advertencia o límite que debe controlarse.  
  
Puede incluir:  
  
* perfil profesional;  
* titular;  
* competencias;  
* experiencias;  
* cargos;  
* funciones;  
* responsabilidades;  
* logros;  
* resultados;  
* métricas;  
* herramientas;  
* tecnologías;  
* formación;  
* certificaciones;  
* idiomas;  
* proyectos;  
* otros contenidos profesionales relevantes.  
  
El playbook no está obligado a utilizar todas las categorías.  
  
---  
  
# 12. Contrato de `guion-adaptacion-cv.md`  
  
## 12.1 Identificación y trazabilidad  
  
Debe registrar:  
  
* candidatura;  
* empresa;  
* puesto;  
* fecha;  
* sesión;  
* `candidatura.md` de origen;  
* análisis de origen;  
* fuentes factuales utilizadas;  
* gate de entrada;  
* estado del gate de salida.  
  
Objetivo:  
  
> poder identificar inequívocamente qué estado estratégico y factual produjo el guion.  
  
---  
  
## 12.2 Instrucción editorial del CV  
  
Debe expresar:  
  
* posicionamiento heredado;  
* mensaje profesional principal;  
* gancho;  
* objetivo del CV;  
* percepción que debe provocar;  
* percepción que debe evitar cuando proceda.  
  
Ejemplo conceptual:  
  
```text  
Posicionamiento:  
Profesional de operaciones de supermercados con experiencia  
demostrada en previsión, stock, organización y mejora de procesos.  
  
Gancho:  
Experiencia práctica resolviendo problemas reales de operación  
mediante previsión, organización, seguimiento y mejora.  
  
Percepción a evitar:  
Perfil excesivamente corporativo y alejado de la operación diaria.  
```  
  
Son instrucciones editoriales.  
  
No son frases destinadas a copiarse literalmente.  
  
---  
  
## 12.3 Mapa de edición  
  
El mapa es el núcleo operativo del guion.  
  
Cada unidad relevante debe evaluar separadamente:  
  
```text  
presencia  
obligatoriedad  
peso_editorial  
```  
  
---  
  
### 12.3.1 Presencia  
  
Valores:  
  
```text  
incluir  
omitir  
```  
  
### `incluir`  
  
El contenido forma parte de este CV.  
  
### `omitir`  
  
El contenido no aparece.  
  
Solo es admisible cuando la omisión:  
  
* no falsifica;  
* no rompe una cronología necesaria;  
* no oculta una carencia que deba permanecer visible;  
* no produce una interpretación engañosa;  
* no elimina contexto imprescindible.  
  
---  
  
### 12.3.2 Obligatoriedad  
  
Valores:  
  
```text  
obligatoria  
opcional  
```  
  
### `obligatoria`  
  
El contenido debe conservarse por:  
  
* continuidad cronológica;  
* coherencia factual;  
* prevención de interpretación engañosa;  
* necesidad estratégica explícita;  
* requisito contractual del futuro CV.  
  
### `opcional`  
  
Su inclusión depende de utilidad editorial.  
  
Regla:  
  
```text  
obligatoriedad: obligatoria  
→ presencia: incluir  
```  
  
Obligatoriedad no determina peso.  
  
---  
  
### 12.3.3 Peso editorial  
  
Para contenido incluido:  
  
```text  
alto  
medio  
bajo  
minimo  
```  
  
### `alto`  
  
Sostiene directamente el posicionamiento o un criterio central.  
  
### `medio`  
  
Aporta evidencia relevante pero secundaria.  
  
### `bajo`  
  
Debe aparecer resumido.  
  
### `minimo`  
  
Solo mantiene contexto, continuidad o información imprescindible.  
  
Es válida esta combinación:  
  
```text  
presencia: incluir  
obligatoriedad: obligatoria  
peso_editorial: minimo  
```  
  
---  
  
### 12.3.4 Criterio objetivo  
  
Todo contenido con peso `alto` o `medio` debe identificar qué ayuda a demostrar.  
  
Puede ser:  
  
* requisito explícito;  
* responsabilidad del puesto;  
* competencia;  
* señal de selección;  
* argumento estratégico heredado.  
  
Ejemplo:  
  
```text  
contenido: previsión y pedidos  
evidencia: HER-03  
criterio_objetivo: disponibilidad / pedidos / inventario  
presencia: incluir  
obligatoriedad: opcional  
peso_editorial: alto  
```  
  
No es necesario recrear la matriz completa de análisis.  
  
Cuando dos contenidos compitan por el mismo peso editorial y ambos estén acreditados, debe priorizarse el que incluya una métrica o resultado cuantificable frente al que sea solo descriptivo. Esto no autoriza inventar una cifra: si no existe métrica acreditada, el contenido cualitativo sigue siendo válido.  
  
---  
  
### 12.3.5 Campos del mapa  
  
Cada unidad considerada debe registrar, cuando resulte aplicable:  
  
```text  
contenido  
tipo  
evidencia  
presencia  
obligatoriedad  
peso_editorial  
criterio_objetivo  
motivo  
funcion_estrategica  
orden  
nivel_detalle  
limitaciones_redaccion  
```  
  
Los campos no aplicables pueden quedar explícitamente como `no_aplica`.  
  
No deben desaparecer silenciosamente si son necesarios para comprender una decisión.  
  
---  
  
## 12.4 Contenido profesional seleccionado  
  
El guion debe determinar qué material sostiene el CV.  
  
Puede incluir:  
  
* perfil;  
* competencias;  
* experiencia;  
* responsabilidades;  
* funciones;  
* logros;  
* métricas;  
* herramientas;  
* tecnologías;  
* formación;  
* certificaciones;  
* idiomas;  
* proyectos.  
  
Para experiencias debe distinguir cuando proceda:  
  
* experiencia con mayor protagonismo;  
* experiencia secundaria;  
* experiencia necesaria para continuidad;  
* contenido a minimizar;  
* logros prioritarios;  
* evidencias de impacto.  
  
No debe redactar todavía las frases finales.  
  
---  
  
## 12.5 Cronología y relevancia  
  
Adaptar no significa reorganizar libremente la trayectoria.  
  
El guion puede decidir:  
  
* peso;  
* detalle;  
* logros destacados;  
* contenidos utilizados en el perfil;  
* prominencia relativa.  
  
Debe preservar una trayectoria comprensible y honesta.  
  
**Contenido de apertura** significa:  
  
> evidencia que debe dominar la percepción inicial.  
  
No significa:  
  
> colocar automáticamente una experiencia antigua antes de la más reciente.  
  
Una alteración posterior de la estructura cronológica requerirá que el formato de CV aplicable lo autorice expresamente.  
  
---  
  
## 12.6 Arquitectura editorial  
  
El guion puede decidir:  
  
* orden funcional de secciones;  
* objetivo de cada sección;  
* qué debe dominar la primera lectura;  
* distribución relativa de profundidad;  
* qué contenido debe comprimirse;  
* qué contenido solo mantiene continuidad;  
* progresión narrativa.  
  
No puede decidir:  
  
* columnas;  
* tipografía;  
* tamaños;  
* colores;  
* márgenes;  
* recursos gráficos.  
  
---  
  
## 12.7 Léxico respaldado  
  
Debe clasificar términos relevantes en tres grupos.  
  
## Utilizables  
  
Existe respaldo factual suficiente.  
  
## Uso condicionado  
  
Solo pueden emplearse:  
  
* con alcance limitado;  
* en contexto concreto;  
* sin extender su significado.  
  
## Prohibidos  
  
No deben utilizarse porque:  
  
* exceden evidencia;  
* alteran seniority;  
* convierten transferibilidad en experiencia;  
* contradicen exclusiones;  
* generan una impresión falsa.  
  
Regla:  
  
> La optimización para ATS nunca autoriza afirmaciones falsas.  
  
---  
  
## 12.8 Carencias, advertencias y límites  
  
Cada riesgo relevante debe transformarse en una instrucción editorial.  
  
Formato:  
  
```text  
elemento:  
riesgo:  
tratamiento:  
permitido:  
prohibido:  
```  
  
Ejemplo:  
  
```text  
elemento:  
FP no finalizada  
  
riesgo:  
presentarla como titulación terminada  
  
tratamiento:  
no utilizarla como credencial terminada  
  
permitido:  
formación realmente acreditada  
  
prohibido:  
presentar título de Técnico Administrativo  
```  
  
---  
  
## 12.9 Control de primer escaneo  
  
El guion debe controlar explícitamente la lectura inicial de recruiter.  
  
Sin depender de diseño visual debe procurar que puedan percibirse rápidamente:  
  
1. qué perfil profesional se presenta;  
2. por qué puede encajar;  
3. cuáles son sus dos o tres señales de evidencia más fuertes;  
4. qué capacidad merece atención inmediata.  
  
El primer escaneo no debe quedar dominado por:  
  
* información secundaria;  
* contenido irrelevante;  
* credenciales débiles;  
* trayectoria que incremente innecesariamente la percepción de sobrecualificación;  
* keywords no sustentadas.  
  
Pregunta de control:  
  
> Si un recruiter dedica inicialmente pocos segundos al CV, ¿la jerarquía editorial le muestra primero la evidencia correcta?  
  
---  
  
## 12.10 Brief cerrado para generación  
  
El guion debe terminar con un brief compacto.  
  
Debe resumir:  
  
* objetivo;  
* posicionamiento;  
* gancho;  
* contenidos prioritarios;  
* evidencias prioritarias;  
* arquitectura narrativa;  
* contenidos a minimizar;  
* restricciones;  
* léxico;  
* riesgos.  
  
---  
  
### 12.10.1 Autoridad del brief  
  
El brief es una **síntesis derivada**.  
  
No constituye otra fuente de autoridad.  
  
No puede:  
  
* crear decisiones;  
* modificar decisiones;  
* eliminar restricciones;  
* reinterpretar posicionamiento;  
* cambiar presencia;  
* cambiar obligatoriedad;  
* cambiar peso.  
  
En caso de discrepancia:  
  
```text  
cuerpo detallado del guion  
> brief  
```  
  
La discrepancia debe corregirse antes del gate.  
  
---  
  
# 13. Tratamiento de incidencias y relación con `DEF-ARQ-001`  
  
## 13.1 Regla arquitectónica previa  
  
`DEF-ARQ-001 — Propagación de cambios factuales` permanece:  
  
```text  
clasificacion: ARQUITECTURA  
estado: abierto  
```  
  
Este diseño **no lo cierra**.  
  
En particular, este playbook no debe presentarse como el contrato arquitectónico general de propagación de nueva evidencia factual.  
  
La responsabilidad local de esta fase se limita a:  
  
1. detectar que existe una novedad factual relevante;  
2. impedir su incorporación directa;  
3. invalidar o bloquear su propia salida cuando proceda;  
4. remitir la situación a la arquitectura de propagación.  
  
Mientras `DEF-ARQ-001` permanezca abierto:  
  
> Work no puede inventar un mecanismo automático de propagación entre `datos-core-busqueda.md`, análisis, candidatura, guiones u otros artefactos derivados.  
  
---  
  
## 13.2 Alcance histórico  
  
La problemática de propagación afecta a candidaturas:  
  
```text  
presentada: false  
```  
  
Una candidatura ya presentada conserva carácter histórico.  
  
Una evidencia descubierta posteriormente no autoriza a reescribir retroactivamente los artefactos históricos de una candidatura presentada.  
  
---  
  
## 13.3 Corrección editorial local  
  
Si:  
  
* los hechos no cambian;  
* la estrategia no cambia;  
* el posicionamiento no cambia;  
* las exclusiones no cambian;  
  
pero una decisión editorial es incorrecta, puede corregirse localmente.  
  
Ejemplos:  
  
* peso incorrecto;  
* orden incorrecto;  
* detalle excesivo;  
* contenido incluido que debería omitirse.  
  
Resultado:  
  
```text  
requiere_correccion  
```  
  
No activa `DEF-ARQ-001`.  
  
---  
  
## 13.4 Evidencia insuficiente  
  
Si una afirmación deseada carece de respaldo:  
  
```text  
no se inventa  
```  
  
Puede:  
  
* eliminarse;  
* limitarse;  
* sustituirse por una formulación sustentada;  
  
si ello no altera la estrategia.  
  
Si la insuficiencia pone en duda:  
  
* posicionamiento;  
* evidencia prioritaria;  
* encaje;  
* tesis;  
* afirmación estratégica;  
  
el guion debe detener la decisión y remitir aguas arriba.  
  
---  
  
## 13.5 Evidencia factual nueva  
  
Si aparece un hecho profesional nuevo que podría modificar:  
  
* análisis;  
* encaje;  
* evidencia;  
* riesgos;  
* estrategia;  
* posicionamiento;  
  
el guion no puede incorporarlo directamente.  
  
Resultado local:  
  
```text  
requiere_actualizacion_factual  
```  
  
Además debe registrar:  
  
```text  
defecto_relacionado: DEF-ARQ-001  
```  
  
El recorrido conceptual esperado continúa siendo:  
  
```text  
datos-core-busqueda.md  
 ↓  
analisis-oferta.md  
 ↓  
candidatura.md  
 ↓  
validación correspondiente  
 ↓  
nuevo guion  
```  
  
Pero este esquema expresa **dependencias lógicas**, no un contrato operativo completo de propagación.  
  
La forma verificable de realizar dicha propagación pertenece a `DEF-ARQ-001` y permanece pendiente de resolución arquitectónica.  
  
---  
  
## 13.6 Evidencia contradictoria  
  
Si aparece contradicción:  
  
```text  
guion  
→ detenido  
```  
  
Resultado:  
  
```text  
requiere_revision_origen  
```  
  
No debe decidir qué fuente “conviene” conservar.  
  
---  
  
## 13.7 Invalidación por cambios aguas arriba  
  
Si cambia materialmente:  
  
* `candidatura.md`;  
* evidencia factual utilizada;  
* análisis relevante;  
* posicionamiento;  
* exclusiones;  
* evidencias prioritarias;  
  
el guion puede perder validez.  
  
Debe pasar como mínimo a:  
  
```text  
GATE-GUION-CV-CONTENIDO  
→ pendiente  
```  
  
Si el cambio afecta hechos o estrategia:  
  
> el guion deberá regenerarse una vez que la propagación aguas arriba haya quedado válidamente resuelta.  
  
Esta regla local de invalidación **no debe interpretarse como resolución de `DEF-ARQ-001`**.  
  
---  
  
# 14. Control de coherencia  
  
Antes de evaluar el gate:  
  
* [ ] `GATE-CANDIDATURA-GUION` está aprobado;  
* [ ] las fuentes son resolubles;  
* [ ] no existe bloqueo activo;  
* [ ] no se ha reabierto estrategia;  
* [ ] todo hecho usado tiene respaldo;  
* [ ] el universo candidato está acotado;  
* [ ] toda unidad relevante tiene tratamiento;  
* [ ] presencia, obligatoriedad y peso son independientes;  
* [ ] lo prioritario sostiene el posicionamiento;  
* [ ] lo prioritario se vincula a criterios objetivos;  
* [ ] las omisiones no deforman trayectoria;  
* [ ] la cronología sigue siendo comprensible;  
* [ ] las exclusiones están protegidas;  
* [ ] las advertencias se traducen en restricciones;  
* [ ] no existen hechos inventados;  
* [ ] el primer escaneo es satisfactorio;  
* [ ] el brief coincide con el cuerpo;  
* [ ] no se ha redactado el CV final;  
* [ ] no se ha diseñado la carta;  
* [ ] la fase posterior no necesita reinterpretar estrategia;  
* [ ] cualquier incidencia factual nueva se ha relacionado correctamente con `DEF-ARQ-001`.  
  
---  
  
# 15. Gate de salida  
  
El gate se denomina:  
  
```text  
GATE-GUION-CV-CONTENIDO  
```  
  
Lectura:  
  
```text  
GATE-  
ORIGEN: GUION-CV  
DESTINO: CONTENIDO  
```  
  
El origen identifica inequívocamente la rama.  
  
No es necesario repetir `CV` en el destino.  
  
La futura rama de carta podría aplicar un patrón simétrico:  
  
```text  
GATE-GUION-CARTA-CONTENIDO  
```  
  
si su diseño posterior así lo aprueba.  
  
Observación pendiente de decisión: el gate de entrada de esta fase, `GATE-CANDIDATURA-GUION`, conserva el nombre genérico con el que fue aprobado antes de que existiera esta especificidad de rama. No se renombra en este documento porque ese gate ya está aprobado y su cambio de nombre no corresponde a este diseño; queda anotado para que la arquitectura decida, cuando exista la rama de carta, si `GATE-CANDIDATURA-GUION` debe mantenerse como gate compartido de ambas ramas o si necesita un equivalente específico por rama.  
  
---  
  
# 16. Qué valida el gate  
  
`GATE-GUION-CV-CONTENIDO` valida únicamente que:  
  
> `guion-adaptacion-cv.md` es una entrada suficientemente completa, factual, estratégica, trazable y determinista para habilitar el siguiente paso arquitectónico de la rama CV.  
  
No valida:  
  
* CV final;  
* carta;  
* maquetación;  
* candidatura completa;  
* envío.  
  
---  
  
# 17. Gate aprobado y fase siguiente  
  
Mientras la futura generación de contenido del CV no esté diseñada:  
  
```text  
GATE-GUION-CV-CONTENIDO: aprobado  
```  
  
autoriza:  
  
> comenzar el diseño de la siguiente fase.  
  
No autoriza todavía:  
  
> ejecutar esa fase.  
  
Patrón:  
  
```text  
fase diseñada  
→ prueba  
→ artefacto  
→ gate  
→ diseño de siguiente fase  
```  
  
---  
  
# 18. Evaluación y decisión humana  
  
La IA puede evaluar.  
  
La aprobación oficial sigue siendo humana.  
  
## 18.1 Resultado de evaluación  
  
```text  
apto  
requiere_correccion  
requiere_revision_origen  
requiere_actualizacion_factual  
bloqueado  
```  
  
## 18.2 Recomendación IA  
  
```text  
aprobar  
no_aprobar  
```  
  
## 18.3 Decisión humana  
  
```text  
pendiente  
aprobado  
bloqueado  
```  
  
Ejemplo:  
  
```text  
resultado_evaluacion: apto  
recomendacion_ia: aprobar  
decision_humana: pendiente  
estado_gate: pendiente  
```  
  
Tras decisión:  
  
```text  
resultado_evaluacion: apto  
recomendacion_ia: aprobar  
decision_humana: aprobado  
estado_gate: aprobado  
```  
  
---  
  
# 19. Criterios de aceptación  
  
Para recomendar aprobación deben cumplirse todos:  
  
* [ ] gate de entrada aprobado;  
* [ ] ausencia de bloqueo;  
* [ ] posicionamiento heredado intacto;  
* [ ] instrucción editorial clara;  
* [ ] universo candidato razonable;  
* [ ] mapa completo;  
* [ ] presencia separada de obligatoriedad;  
* [ ] obligatoriedad separada de peso;  
* [ ] contenido principal vinculado a criterios objetivos;  
* [ ] experiencias y logros prioritarios identificados;  
* [ ] selección trazable;  
* [ ] omisiones materiales justificadas;  
* [ ] ninguna omisión induce a error;  
* [ ] cronología comprensible;  
* [ ] exclusiones protegidas;  
* [ ] léxico respaldado;  
* [ ] ausencia de hechos nuevos incorporados sin propagación;  
* [ ] incidencias factuales nuevas relacionadas con `DEF-ARQ-001`;  
* [ ] primer escaneo competitivo;  
* [ ] brief coherente;  
* [ ] ausencia de redacción final del CV;  
* [ ] ausencia de diseño de carta;  
* [ ] siguiente fase capaz de operar sin reconstruir estrategia.  
  
---  
  
# 20. Postcondiciones  
  
Con gate aprobado debe existir evidencia de que:  
  
1. `guion-adaptacion-cv.md` está completo;  
2. coincide con `candidatura.md`;  
3. mantiene trazabilidad factual;  
4. las decisiones editoriales están cerradas;  
5. la futura fase sabe:  
  
 * qué incluir;  
 * qué omitir;  
 * qué conservar;  
 * qué priorizar;  
 * qué minimizar;  
 * qué demostrar;  
 * qué evitar;  
6. el posicionamiento no requiere reinterpretación;  
7. no existe contenido final del CV;  
8. cualquier problema factual nuevo ha sido detenido y remitido correctamente.  
  
---  
  
# 21. Metadatos mínimos del artefacto  
  
El futuro template deberá incluir frontmatter estructurado.  
  
Mínimo:  
  
```yaml  
id:  
tipo: guion_adaptacion_cv  
version_template:  
candidatura:  
empresa:  
puesto:  
fecha_generacion:  
sesion:  
candidatura_origen:  
analisis_origen:  
fuentes_factuales:  
gate_entrada:  
estado_gate_salida:  
```  
  
El diseño definitivo del schema corresponde a implementación.  
  
Work no debe ampliar el schema sin necesidad derivada de este contrato.  
  
---  
  
# 22. Prueba principal — `CAND-2026-020`  
  
Caso:  
  
```text  
CAND-2026-020  
Lidl Supermercados SAU  
Responsable de turno Tienda 40h Tamaraceite  
```  
  
Es adecuado porque obliga a adaptar una trayectoria amplia hacia un puesto operativo.  
  
---  
  
## 22.1 Contenido a priorizar  
  
La prueba debe poder priorizar:  
  
* operación de supermercados;  
* previsión;  
* pedidos;  
* stock;  
* rotación;  
* mermas;  
* disponibilidad;  
* organización del trabajo;  
* seguimiento de tareas;  
* cuadres de caja;  
* mejora de procesos.  
  
---  
  
## 22.2 Sobrecualificación  
  
Debe:  
  
* conservar cargos reales;  
* conservar continuidad;  
* reducir protagonismo de contenido directivo irrelevante;  
* aumentar evidencia operativa;  
* impedir que la primera percepción sea un perfil alejado de tienda.  
  
No puede:  
  
* falsear cargos;  
* degradar responsabilidades históricas;  
* inventar una trayectoria operativa distinta.  
  
---  
  
## 22.3 Formación  
  
Debe impedir:  
  
* presentar FP no finalizada como titulación;  
* crear equivalencias inexistentes.  
  
---  
  
## 22.4 Caja  
  
`HER-10` puede respaldar:  
  
* cuadres de caja;  
* mejora mediante Excel.  
  
No puede respaldar:  
  
* tesorería;  
* banca;  
* pagos;  
* gestión financiera integral.  
  
---  
  
## 22.5 Compras y proveedores  
  
Puede utilizar hechos acreditados sobre:  
  
* pedidos;  
* proveedores directos;  
* negociación limitada;  
* sistemas acreditados.  
  
No puede convertirlos en:  
  
* política central de compras;  
* negociación corporativa;  
* funciones financieras;  
* responsabilidades no acreditadas.  
  
---  
  
# 23. Estado del caso antes de probar  
  
Antes de generar el guion debe verificarse:  
  
```text  
GATE-CANDIDATURA-GUION: aprobado  
```  
  
Además:  
  
* la siguiente fase debe apuntar al guion;  
* el índice de artefactos debe reflejar el estado vigente;  
* no deben sobrevivir instrucciones anteriores al gate aprobado.  
  
No debe probarse la fase utilizando un artefacto operativamente obsoleto.  
  
---  
  
# 24. Prueba de generalidad  
  
`CAND-2026-020` es el primer caso.  
  
`CAND-2026-019` es el caso posterior de contraste.  
  
El contraste debe probar problemas distintos:  
  
* perfil tecnológico;  
* transferibilidad funcional;  
* carencias de stack;  
* formación no coincidente;  
* riesgo de sobreafirmación;  
* posicionamiento distinto.  
  
La progresión queda definida literalmente:  
  
```text  
CAND-2026-020 superado  
→ PLAYBOOK_GUION_ADAPTACION_CV: en_prueba  
  
CAND-2026-020 + CAND-2026-019 superados  
→ PLAYBOOK_GUION_ADAPTACION_CV: candidata a validada  
```  
  
Superar únicamente `CAND-2026-020` permite:  
  
* implementar;  
* continuar pruebas;  
* mantener fase `en_prueba`.  
  
No permite declarar:  
  
```text  
validada  
```  
  
Solo después de superar ambos casos puede proponerse validación humana.  
  
`candidata a validada` no es un nuevo estado formal.  
  
Estados oficiales:  
  
```text  
pendiente  
diseñada  
en_prueba  
validada  
```  
  
---  
  
# 25. Regla de generalización  
  
El playbook y su template no deben codificar reglas específicas de:  
  
* Lidl;  
* supermercados;  
* `CAND-2026-020`;  
* `CAND-2026-019`.  
  
Debe comprobarse que son genéricos:  
  
* ejes editoriales;  
* universo candidato;  
* jerarquización;  
* retrocesos;  
* primer escaneo;  
* tratamiento de sobrecualificación;  
* tipos de contenido;  
* relación con factualidad.  
  
Principio:  
  
> El caso valida el contrato. El caso no define el contrato.  
  
---  
  
# 26. Entregables tras aprobación del diseño  
  
Una vez aprobado este documento, Work deberá producir **primero un plan de implementación**.  
  
El plan deberá conducir como mínimo a:  
  
```text  
PLAYBOOK_GUION_ADAPTACION_CV.md  
TEMPLATE_GUION_ADAPTACION_CV_v2.md  
guion-adaptacion-cv.md de CAND-2026-020  
evaluacion del GATE-GUION-CV-CONTENIDO  
```  
  
También deberá contemplar:  
  
* sincronización previa del estado de `CAND-2026-020`;  
* actualización de índice de artefactos;  
* actualización de estado de fase;  
* actualización posterior de la SPEC;  
* registro definitivo de decisión `ARQ`;  
* registro definitivo de incertidumbre `INC`;  
* registro del gate;  
* referencia expresa a `DEF-ARQ-001`;  
* prueba posterior con `CAND-2026-019`.  
  
---  
  
# 27. Responsabilidad de Work  
  
Esta sección es normativa para cualquier agente que reciba este diseño.  
  
## 27.1 Rol  
  
Work actúa como:  
  
> planificador e implementador de un diseño previamente aprobado.  
  
No actúa como diseñador autónomo de esta fase.  
  
SPEC v0.4.0 (sección 3.2) establece que, salvo instrucción explícita contraria, el agente solo planifica y no implementa. Esta sección invoca expresamente esa excepción para la fase `PLAYBOOK_GUION_ADAPTACION_CV`: Work queda autorizado a implementar, siempre dentro de la secuencia obligatoria de 27.2 y con revisión humana del plan antes de ejecutarlo.  
  
---  
  
## 27.2 Secuencia obligatoria  
  
```text  
diseño aprobado  
 ↓  
verificación de estado real  
 ↓  
plan de implementación  
 ↓  
revisión/aprobación del plan  
 ↓  
implementación  
 ↓  
prueba CAND-2026-020  
 ↓  
evaluación  
 ↓  
posterior contraste CAND-2026-019  
```  
  
---  
  
## 27.3 Antes de planificar  
  
Work debe:  
  
1. leer la SPEC vigente;  
2. leer este diseño completo;  
3. consultar el estado operativo vigente;  
4. identificar la sesión PCS;  
5. inspeccionar el repositorio real;  
6. comprobar existencia de artefactos;  
7. comprobar el estado de `CAND-2026-020`;  
8. verificar gates;  
9. verificar que `DEF-ARQ-001` sigue abierto o consultar su estado actualizado;  
10. identificar discrepancias entre diseño y repositorio.  
  
---  
  
## 27.4 Qué puede hacer al planificar  
  
Puede:  
  
* localizar rutas reales;  
* identificar archivos que deben crearse;  
* identificar archivos que deben actualizarse;  
* descomponer la implementación;  
* proponer orden técnico;  
* proponer pruebas;  
* proponer validaciones;  
* señalar dependencias;  
* señalar incertidumbres;  
* señalar contradicciones.  
  
---  
  
## 27.5 Qué no puede hacer al planificar  
  
No puede:  
  
* rediseñar este contrato;  
* cambiar responsabilidades;  
* modificar el gate;  
* fusionar CV y carta;  
* cerrar `DEF-ARQ-001`;  
* inventar el contrato de propagación factual;  
* diseñar la rama de carta;  
* diseñar prematuramente el JSON;  
* diseñar el generador final;  
* ampliar alcance;  
* sustituir estados;  
* introducir nuevas taxonomías;  
* tratar una inferencia como decisión aprobada.  
  
---  
  
## 27.6 Reglas específicas sobre `DEF-ARQ-001`  
  
Mientras siga abierto:  
  
Work puede implementar:  
  
* detección local;  
* bloqueo local;  
* invalidación local;  
* referencia al defecto.  
  
Work no puede implementar por iniciativa propia:  
  
* cascadas automáticas de regeneración;  
* propagación transversal de cambios;  
* actualización automática de artefactos aguas abajo;  
* reglas generales para candidaturas presentadas/no presentadas que no estén ya aprobadas;  
* cierre del defecto.  
  
Si la implementación necesita alguno de esos comportamientos:  
  
```text  
STOP  
→ devolver a arquitectura  
```  
  
---  
  
## 27.7 Reglas específicas sobre la carta  
  
Work debe tratar el registro `INC-NNN` como:  
  
```text  
bloquea_plan: false  
```  
  
Puede continuar con el CV.  
  
No puede aprovechar la implementación del CV para decidir:  
  
* playbook de carta;  
* template;  
* gate;  
* generación;  
* infraestructura compartida;  
* convergencia técnica.  
  
---  
  
## 27.8 Criterios de parada de Work  
  
Work debe detener la tarea afectada cuando:  
  
* el repositorio contradiga una autoridad normativa;  
* falte una decisión imprescindible;  
* una tarea dependa de cerrar `DEF-ARQ-001`;  
* sea necesario modificar la arquitectura;  
* aparezca una nueva incertidumbre bloqueante;  
* se necesite diseñar una fase futura no autorizada;  
* exista ambigüedad factual que el guion no pueda resolver.  
  
Debe continuar con las tareas independientes que sigan siendo válidas.  
  
---  
  
## 27.9 Salida mínima del plan  
  
Cada tarea del plan debe seguir el esquema canónico ya definido en SPEC v0.4.0 (sección 39, "estructura mínima de una tarea"), sin redefinirlo:  
  
```text  
ID  
titulo  
objetivo  
justificacion  
precondiciones  
archivos_a_leer  
archivos_afectados  
accion  
resultado_esperado  
criterios_de_aceptacion  
verificacion  
dependencias  
gate_asociado  
aprobacion_humana  
```  
  
Esta fase añade un único campo adicional, propio de su naturaleza editorial:  
  
```text  
riesgo_o_incidencia  
```  
  
para registrar si la tarea puede activar `requiere_correccion`, `requiere_revision_origen`, `requiere_actualizacion_factual` o `bloqueado` según la sección 18.  
  
Debe distinguir:  
  
* archivos a crear;  
* archivos a modificar;  
* archivos solo de lectura;  
* artefactos de prueba;  
* actualizaciones de gobernanza.  
  
---  
  
## 27.10 Prohibición de implementación silenciosa  
  
Si Work encuentra una mejora no contemplada:  
  
1. la registra;  
2. determina si es local o arquitectónica;  
3. no la introduce silenciosamente;  
4. devuelve a diseño cualquier decisión arquitectónica.  
  
Principio:  
  
> Work materializa el contrato; no completa sus huecos mediante diseño implícito.  
  
---  
  
# 28. Fuera de alcance  
  
No forma parte de este bloque:  
  
* redacción final del CV;  
* maquetación;  
* DOCX;  
* PDF;  
* LaTeX;  
* carta;  
* playbook de carta;  
* template de carta;  
* gate de carta;  
* artefacto estratégico de carta;  
* generación de carta;  
* `datos-generacion.json`;  
* adaptación del generador;  
* nuevo veredicto final;  
* envío;  
* contacto externo;  
* resolución arquitectónica de `DEF-ARQ-001`.  
  
---  
  
# 29. Criterio de cierre del diseño  
  
El diseño puede aprobarse cuando exista decisión humana explícita sobre:  
  
* [ ] responsabilidad CV-only;  
* [ ] separación CV/carta;  
* [ ] rama de carta como incertidumbre formal no bloqueante;  
* [ ] contrato de fase de diez campos;  
* [ ] autoridad estratégica;  
* [ ] autoridad factual;  
* [ ] papel del análisis;  
* [ ] orden normativo de 15 pasos;  
* [ ] universo candidato;  
* [ ] tipos de contenido;  
* [ ] presencia / obligatoriedad / peso;  
* [ ] criterio objetivo;  
* [ ] protección cronológica;  
* [ ] primer escaneo;  
* [ ] autoridad derivada del brief;  
* [ ] tratamiento de incidencias;  
* [ ] relación explícita con `DEF-ARQ-001`;  
* [ ] ausencia de cierre local de `DEF-ARQ-001`;  
* [ ] invalidación local sin inventar propagación;  
* [ ] gate `GATE-GUION-CV-CONTENIDO`;  
* [ ] evaluación IA separada de aprobación humana;  
* [ ] `CAND-2026-020` como prueba principal;  
* [ ] `CAND-2026-019` como contraste;  
* [ ] progresión `en_prueba → candidata a validada`;  
* [ ] responsabilidad explícita de Work;  
* [ ] límites de implementación.  
  
Una vez aprobado:  
  
> el siguiente paso será elaborar en Work un plan de implementación contra este contrato.  
  
---  
  
# 30. Decisiones consolidadas  
  
Las decisiones `D-NN` son locales a este documento de diseño y no requieren por sí solas ninguna acción sobre la SPEC. Una decisión `D-NN` se promueve a `ARQ-NN` únicamente cuando afecta a la arquitectura general de `job-up` más allá de esta fase concreta — como ya ocurre con D-03, que debe registrarse como `ARQ-XX` en la próxima actualización de la SPEC (sección 3 de este documento). El resto de decisiones `D-NN` permanece como memoria local de este diseño.  
  
## D-01 — Adaptador exclusivo de CV  
  
`PLAYBOOK_GUION_ADAPTACION_CV` gobierna únicamente el CV.  
  
## D-02 — Estrategia común única  
  
`candidatura.md` conserva la estrategia común.  
  
## D-03 — Separación CV/carta decidida  
  
La separación es una decisión arquitectónica.  
  
## D-04 — Rama de carta diferida  
  
Su arquitectura específica queda registrada como incertidumbre formal no bloqueante.  
  
## D-05 — Factualidad externa  
  
El guion selecciona hechos; no los crea.  
  
## D-06 — Contrato de fase explícito  
  
La fase satisface los diez campos normativos de la SPEC.  
  
## D-07 — Ejecución secuencial  
  
El playbook sigue un orden normativo de quince pasos.  
  
## D-08 — Universo candidato acotado  
  
No se barre indiscriminadamente todo el core.  
  
## D-09 — Mapa multidimensional  
  
Se separan:  
  
```text  
presencia  
obligatoriedad  
peso_editorial  
```  
  
## D-10 — Relevancia trazable  
  
El contenido prioritario se relaciona con un criterio objetivo.  
  
## D-11 — Primer escaneo gobernado  
  
La adaptación considera explícitamente la lectura inicial del recruiter.  
  
## D-12 — Cronología protegida  
  
La relevancia no justifica una representación engañosa de la trayectoria.  
  
## D-13 — Brief derivado  
  
El brief resume; no gobierna.  
  
## D-14 — Corrección proporcional  
  
Los errores editoriales pueden corregirse localmente.  
  
## D-15 — `DEF-ARQ-001` permanece abierto  
  
El tratamiento local de hechos nuevos no constituye el contrato arquitectónico de propagación.  
  
## D-16 — Cambio material puede invalidar el guion  
  
La invalidación local no implica resolver automáticamente la propagación.  
  
## D-17 — Gate legible  
  
```text  
GATE-GUION-CV-CONTENIDO  
```  
  
## D-18 — IA evalúa, humano aprueba  
  
La aprobación oficial no es automática.  
  
## D-19 — Gate habilita diseño posterior  
  
Mientras la siguiente fase no exista, no autoriza su ejecución.  
  
## D-20 — Validación progresiva  
  
```text  
CAND-2026-020  
→ en_prueba  
  
CAND-2026-020 + CAND-2026-019  
→ candidata a validada  
```  
  
## D-21 — Work implementa, no rediseña  
  
Los huecos arquitectónicos vuelven a diseño.  
  
---  
  
# 31. Resumen operativo  
  
```text  
candidatura.md  
 ↓  
estrategia aprobada  
 ↓  
PLAYBOOK_GUION_ADAPTACION_CV  
 ↓  
universo candidato  
 ↓  
presencia  
obligatoriedad  
peso  
criterio objetivo  
orden  
detalle  
léxico  
límites  
 ↓  
guion-adaptacion-cv.md  
 ↓  
control recruiter  
control factual  
control estratégico  
 ↓  
¿nueva evidencia factual?  
 │  
 ├─ no  
 │ ↓  
 │ evaluación IA  
 │ ↓  
 │ decisión humana  
 │ ↓  
 │ GATE-GUION-CV-CONTENIDO  
 │  
 └─ sí  
 ↓  
 detener incorporación  
 ↓  
 requiere_actualizacion_factual  
 ↓  
 DEF-ARQ-001  
 ↓  
 resolución aguas arriba  
```  
  
---  
  
# 32. Registro formal de incertidumbres  
  
## `INC-NNN` — Rama específica de carta pendiente de diseño  
  
```text  
ID: INC-NNN  
  
elemento:  
Arquitectura posterior de adaptación y generación  
de la carta de presentación.  
  
motivo:  
La separación de responsabilidades CV/carta está decidida,  
pero no es necesario diseñar la rama de carta para implementar  
y probar PLAYBOOK_GUION_ADAPTACION_CV.  
  
impacto:  
Quedan deliberadamente sin decidir:  
- playbook de adaptación de carta;  
- template;  
- gate;  
- artefacto estratégico;  
- fase de generación de contenido;  
- infraestructura compartida o separada con CV;  
- relación técnica entre ambas ramas.  
  
bloquea_plan: false  
  
resolucion_necesaria:  
Antes de iniciar el diseño de la rama específica de carta  
o de una infraestructura común CV/carta.  
```  
  
`INC-NNN` es provisional dentro de este diseño.  
  
La actualización de la SPEC deberá asignar el identificador numérico definitivo dentro del registro oficial de incertidumbres.  
  
La existencia de este `INC` no autoriza a Work a resolverlo durante la implementación del guion de CV.  
  
---  
  
# 33. Relación con defectos arquitectónicos abiertos  
  
## `DEF-ARQ-001` — Propagación de cambios factuales  
  
Estado heredado:  
  
```text  
clasificacion: ARQUITECTURA  
estado: abierto  
```  
  
Este diseño:  
  
* lo reconoce;  
* lo referencia;  
* evita contradecirlo;  
* define la reacción local del guion.  
  
Este diseño **no**:  
  
* lo resuelve;  
* lo cierra;  
* define toda la propagación;  
* autoriza implementación transversal.  
  
Criterio de compatibilidad:  
  
> `PLAYBOOK_GUION_ADAPTACION_CV` debe ser implementable sin que Work tenga que inventar la solución de `DEF-ARQ-001`.  
  
Si esto deja de ser posible:  
  
```text  
bloqueo arquitectónico  
→ regresar a diseño  
```  
  
---  
  
# 34. Principios finales  
  
## Principio editorial  
  
> El guion decide qué historia profesional debe hacer visible el CV y qué evidencia debe sostenerla, pero no redacta todavía el documento final.  
  
## Principio estratégico  
  
> La estrategia pertenece a `candidatura.md`; el guion no puede reinventarla para obtener un CV aparentemente mejor.  
  
## Principio factual  
  
> Lo que mejora el encaje mediante falsificación no es adaptación.  
  
## Principio competitivo  
  
> La seguridad factual no debe producir un CV débil: dentro de los hechos acreditados debe seleccionarse y jerarquizarse la evidencia con máxima capacidad de generar entrevista.  
  
## Principio de selección  
  
> El CV debe funcionar tanto bajo lectura completa como bajo el primer escaneo de un recruiter.  
  
## Principio arquitectónico  
  
> Un playbook local no debe apropiarse de la resolución de un defecto arquitectónico abierto.  
  
## Principio agentic  
  
> Una decisión que el agente tenga que adivinar es una decisión que el contrato todavía no ha especificado suficientemente.  
  
## Principio de implementación  
  
> Work materializa decisiones aprobadas; las incertidumbres y defectos arquitectónicos regresan a la capa que tiene autoridad para resolverlos.  

---

# Changelog

## 0.3.1 — 2026-08-06

Revisión editorial tras análisis en tres roles (arquitecto senior de documentación y workflows agentic, recruiter senior y coach de carrera, AI workflow engineer), sin reabrir ninguna decisión de fondo de la versión 0.3.0.

* Se corrige la referencia cruzada de la sección 4 (`CRITERIOS_DE_ACEPTACION`): apuntaba a la sección 18 y debía apuntar a la sección 19.
* Se normaliza la jerarquía de encabezados de la sección 12 (12.3 a 12.10 pasan de nivel 1 a nivel 2; 12.3.1-12.3.5 y 12.10.1 pasan a nivel 3), para que la sección se anide correctamente bajo "12. Contrato de `guion-adaptacion-cv.md`".
* Se separa el frontmatter en `defectos_relacionados` (solo `DEF-ARQ-001`) y `audiencias` (`humano`, `agente_ia_planificador`, `agente_ia_ejecutor`), que estaban mezclados bajo `defectos_arquitectonicos_relacionados`.
* Se añade en 27.1 la cita explícita de la excepción de SPEC v0.4.0 (sección 3.2) que autoriza a Work a implementar además de planificar en esta fase.
* Se sustituye el esquema propio de 9 campos de 27.9 por el esquema canónico de 14 campos de SPEC v0.4.0 (sección 39), añadiendo únicamente `riesgo_o_incidencia` como campo propio de esta fase.
* Se añade en la sección 15 una nota explícita, sin resolverla, sobre la asimetría entre el gate de salida (específico de CV) y el gate de entrada `GATE-CANDIDATURA-GUION` (todavía genérico).
* Se añade al inicio de la sección 30 la regla de cuándo una decisión `D-NN` local se promueve a `ARQ-NN` de la SPEC.
* Se añade en 12.3.4 la preferencia editorial por logros con métrica acreditada frente a logros solo cualitativos, sin autorizar inventar cifras.
* Se documenta en el frontmatter que `estado_documento` pertenece a un eje de estado ("documento de diseño de fase") todavía no declarado formalmente en el glosario de la SPEC.

Ningún cambio de esta versión modifica el contrato de fase, el orden normativo de ejecución, la separación CV/carta, la relación con `DEF-ARQ-001` ni los criterios de prueba con `CAND-2026-020` y `CAND-2026-019` ya fijados en 0.3.0.
