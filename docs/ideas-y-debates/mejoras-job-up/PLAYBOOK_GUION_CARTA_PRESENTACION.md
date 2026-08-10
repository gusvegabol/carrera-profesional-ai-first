---
id: PLAYBOOK_GUION_CARTA_PRESENTACION
tipo: playbook
version: "1.0.0"
estado: probado
alcance: exclusivo_carta_presentacion
entrada_principal: candidatura.md
salida: guion-carta-presentacion.md
gate_entrada: GATE-CANDIDATURA-GUION
gate_salida: GATE-GUION-CARTA-CONTENIDO
rama: job-up
---

# Playbook — Guion de carta de presentación

## 1. Propósito y alcance

`PLAYBOOK_GUION_CARTA_PRESENTACION` transforma la estrategia común ya aprobada de una candidatura en un **mapa argumental y comunicativo auditable para una carta de presentación concreta**.

Produce:

```text
guion-carta-presentacion.md
```

El guion establece:

- a quién se dirige realmente la carta;
- qué debe conseguir comunicativamente;
- qué argumento central debe construir;
- qué evidencias merece narrar;
- qué motivaciones personales pueden afirmarse;
- qué información cultural puede utilizarse;
- qué necesidades de la oferta deben conectarse con evidencia;
- qué carencias conviene tratar, omitir o contextualizar;
- qué tono, estructura y extensión debe tener;
- qué vocabulario de la oferta debe aparecer naturalmente;
- qué afirmaciones están prohibidas.

No:

- redacta la carta final;
- modifica `candidatura.md`;
- modifica `analisis-oferta.md`;
- modifica hechos profesionales;
- reabre la estrategia;
- sustituye el CV;
- vuelve a decidir la competitividad general de la candidatura;
- inventa motivaciones;
- atribuye valores corporativos al candidato;
- compone DOCX/PDF;
- presenta la candidatura;
- inicia sesión en plataformas externas;
- adjunta documentos ni realiza envíos.

Es un adaptador exclusivo de la carta.

---

# 2. Pregunta central

El playbook debe responder:

> **¿Qué argumento personal, factual y dirigido al destinatario debe construir la carta para conseguir que un recruiter —humano o IA— entienda rápidamente por qué merece considerar esta candidatura, complementando el CV y conectando la evidencia disponible con la oportunidad y, cuando exista información verificable, con el contexto real de la empresa?**

La finalidad no es resumir el CV.

La carta debe:

```text
interpretar
+
conectar
+
contextualizar
+
presentar
```

sin:

```text
inventar
+
repetir
+
exagerar
+
maquillar carencias
```

---

# 3. Principio rector

> **La carta habla directamente al recruiter.**

El lector potencial puede ser:

1. recruiter humano;
2. hiring manager;
3. IA de selección;
4. ATS o sistema de indexación previo.

La carta debe funcionar primero como comunicación profesional y humana.

La compatibilidad ATS/IA se obtiene mediante lenguaje profesional relevante y factual, no mediante acumulación artificial de keywords.

---

# 4. Autoridades y límites

| Fuente | Autoridad |
| --- | --- |
| `candidatura.md` | Estrategia común, posicionamiento, tesis, evidencias prioritarias, carencias, exclusiones y límites. |
| `analisis-oferta.md` | Necesidades, requisitos, señales de selección, lenguaje de la oferta y contexto. |
| fuente completa de la oferta | Texto literal de la oportunidad, incluida cultura, propuesta de empleador y lenguaje corporativo cuando existan. |
| `datos-core-busqueda.md` | Hechos profesionales, cronología y evidencia factual. |
| declaraciones verificadas del usuario para la carta | Motivación personal, conocimiento previo, razones profesionales, relación real con empresa o puesto. |
| URL oficial de empresa, cuando exista | Cultura, valores, propuesta de empleador, lenguaje y contexto corporativo declarado. |

Ninguna fuente puede asumir autoridad de otra.

Especialmente:

```text
cultura de empresa
≠
atributo del candidato

requisito de la oferta
≠
experiencia del candidato

hecho profesional
≠
motivación personal

plataforma publicadora
≠
empresa ofertante
```

---

# 5. Entidades que deben distinguirse

El playbook debe identificar explícitamente:

```text
plataforma_publicadora
intermediario_reclutador
empresa_objetivo
destinatario_real
```

Pueden coincidir o no.

Ejemplo:

```text
Indeed
→ plataforma

Lidl
→ empresa objetivo
```

Otro caso:

```text
Randstad
→ intermediario

empresa final
→ anónima
```

Nunca se utilizará la cultura de la plataforma o intermediario como cultura de la empresa final salvo que dicho intermediario sea realmente el empleador destinatario.

---

# 6. Tipología de empresa destinataria

Clasificar obligatoriamente:

```text
empresa_identificada
intermediario_con_empresa_identificada
intermediario_con_empresa_anonima
```

## 6.1 Empresa identificada

Puede utilizarse:

- cultura presente en la oferta;
- URL oficial aportada;
- contexto corporativo verificable.

## 6.2 Intermediario con empresa identificada

Debe diferenciar:

- quien gestiona el proceso;
- quien contrata;
- a quién debe dirigirse la carta.

## 6.3 Empresa anónima

Es un estado normal y válido.

En este caso:

- no intentar descubrir especulativamente la identidad;
- no solicitar cultura de una empresa desconocida;
- no atribuir al empleador la cultura del intermediario;
- personalizar por puesto, sector, funciones y necesidades;
- mantener un destinatario genérico profesional cuando sea necesario.

La ausencia de cultura por anonimato:

```text
no es defecto
no es bloqueo
no reduce por sí sola la calidad del guion
```

---

# 7. Fuentes de cultura y propuesta de empleador

## 7.1 Prioridad

Orden de relevancia:

```text
1. información cultural contenida en la propia oferta
2. fuente oficial específica de empleo/carreras
3. fuente corporativa oficial general
```

La oferta tiene prioridad contextual porque está vinculada al proceso concreto.

---

## 7.2 Cultura presente en la oferta

El playbook debe analizar siempre si la oferta contiene:

- valores;
- propósito;
- forma de trabajo;
- estilo de liderazgo;
- autonomía;
- orientación a cliente;
- colaboración;
- desarrollo;
- diversidad;
- responsabilidad;
- innovación;
- propuesta de empleador;
- otras señales culturales relevantes.

No todo adjetivo de una oferta es automáticamente cultura.

Debe separar:

```yaml
contexto_oferta_carta:
  necesidades_funcionales: []
  requisitos: []
  atributos_personales_buscados: []
  señales_culturales: []
  propuesta_empleador: []
```

---

# 8. URL oficial de cultura o empresa

Existen dos vías de entrada.

## Vía A — Aportada al iniciar la candidatura

Si la skill de inicio ya recibió una URL oficial de la empresa:

```text
→ no volver a solicitarla
→ resolverla y utilizarla si sigue siendo válida
```

## Vía B — Solicitada antes del guion de carta

Si:

```text
empresa identificada
+
no existe URL previamente registrada
```

la IA preguntará al usuario si puede proporcionar una URL oficial donde la empresa hable de:

- cultura;
- valores;
- empleo;
- personas;
- propósito;
- forma de trabajar.

La URL es opcional.

Si el usuario no dispone de ella:

```text
→ continuar
```

No constituye bloqueo.

Si la empresa es anónima:

```text
→ no solicitar URL
```

---

# 9. Registro de fuentes culturales

El guion debe conservar procedencia.

Ejemplo:

```yaml
contexto_empresa:
  empresa_objetivo: Lidl
  tipo: empresa_identificada

  fuentes:
    - tipo: oferta
      disponible: true

    - tipo: web_oficial
      disponible: true
      url: ...

  señales_culturales:
    - señal: responsabilidad
      fuente: oferta
      referencia: ...

    - señal: trabajo_en_equipo
      fuente: web_oficial
      referencia: ...
```

Si dos fuentes muestran énfasis distintos:

```text
→ conservar procedencia
→ no fusionarlas como una única afirmación
```

---

# 10. Regla de utilización cultural

La información cultural puede:

- contextualizar;
- adaptar lenguaje;
- mejorar personalización;
- identificar conexiones relevantes;
- orientar el tono;
- construir un puente comunicativo.

No puede:

- crear evidencia profesional;
- demostrar una competencia del candidato;
- demostrar afinidad personal no declarada;
- demostrar motivación;
- justificar afirmaciones emocionales ficticias.

Regla:

> **La cultura puede determinar cómo construir el mensaje, nunca qué cualidades posee el candidato.**

---

# 11. Captura humana de motivación

Antes de producir un guion apto, el flujo debe disponer de información suficiente para distinguir:

```text
motivación declarada
razón profesional factual
ausencia de motivación específica
afirmación no acreditada
```

La IA debe obtener directamente del usuario únicamente la información necesaria.

No debe forzar entusiasmo.

---

# 12. Preguntas de motivación

La captura puede adaptarse al caso, pero debe cubrir cuando resulte pertinente:

## 12.1 Interés por el puesto

Pregunta conceptual:

> ¿Existe alguna razón real por la que este puesto te interese especialmente?

Son respuestas válidas:

- encaje con experiencia previa;
- condiciones;
- responsabilidades;
- sector;
- desarrollo;
- ubicación;
- estabilidad;
- aprendizaje;
- vuelta a una actividad conocida;
- ninguna motivación específica adicional.

`ninguna` es una respuesta válida.

---

## 12.2 Conocimiento o relación previa con la empresa

Preguntar cuando la empresa esté identificada:

> ¿Tienes conocimiento o relación previa real con esta empresa?

Ejemplos:

- cliente;
- antiguo proveedor;
- antiguo empleado;
- proceso previo;
- contacto profesional;
- conocimiento habitual de productos/servicios;
- seguimiento real de su actividad;
- ninguna.

No transformar:

```text
"conozco la empresa como cliente"
```

en:

```text
"admiro profundamente su cultura"
```

---

## 12.3 Preferencia profesional

Preguntar cuando sea útil:

> ¿Qué aspecto real de esta oportunidad encaja especialmente con lo que buscas?

Puede permitir razones como:

- responsabilidad operativa;
- gestión de equipos;
- automatización;
- trabajo técnico;
- atención a cliente;
- estabilidad;
- aprendizaje;
- sector;
- otras razones declaradas.

---

# 13. Autoridad de las motivaciones

Tres niveles.

## Nivel 1 — Declaración explícita del usuario

Puede formularse como motivación personal.

Ejemplo:

```text
"Me interesa volver al ámbito de operaciones de supermercados."
```

## Nivel 2 — Razón profesional respaldada por hechos

Puede utilizarse como conexión profesional.

Ejemplo:

```text
"La posición conecta con mi experiencia en pedidos, stock y organización operativa."
```

No puede convertirse en emoción.

## Nivel 3 — No acreditado

No puede aparecer.

Ejemplos prohibidos sin declaración real:

```text
"Me apasiona el sector."
"Siempre he admirado su empresa."
"Sigo desde hace años su evolución."
"Comparto profundamente sus valores."
"Es una empresa en la que siempre he querido trabajar."
```

---

# 14. Ausencia de motivación específica

No bloquea.

El guion puede construir una carta profesional basada en:

```text
oportunidad
+
encaje
+
evidencia
+
valor aportable
```

sin fingir una motivación emocional.

---

# 15. Precondiciones

Antes de iniciar el guion deben cumplirse:

1. candidatura vigente;
2. `presentada: false`;
3. `candidatura.md` resoluble;
4. `analisis-oferta.md` resoluble;
5. oferta fuente resoluble;
6. fuentes factuales necesarias resolubles;
7. ausencia de bloqueo activo que impida continuar;
8. destinatario clasificado;
9. información cultural de la oferta analizada;
10. URL externa procesada si ya fue aportada;
11. si empresa identificada y no había URL, se ofreció al usuario la posibilidad de aportarla;
12. motivaciones personales que se pretendan utilizar están explícitamente verificadas con el usuario.

No disponer de:

- URL externa;
- cultura adicional;
- empresa identificada;

no bloquea por sí solo el guion.

---

# 16. Roles obligatorios

## Rol A — Recruiter senior especializado en comunicación de candidatura

Pregunta central:

> ¿Qué tendría que leer un recruiter para comprender rápidamente por qué esta candidatura merece consideración sin recibir una repetición del CV?

Debe evaluar anticipadamente:

- utilidad;
- diferenciación;
- claridad;
- relevancia;
- credibilidad;
- humanización;
- personalización;
- concisión;
- efecto recruiter.

Debe combatir:

- carta genérica;
- resumen del CV;
- grandilocuencia;
- clichés;
- entusiasmo artificial;
- sobreexplicación;
- lenguaje burocrático;
- texto que parezca generado por IA.

---

## Rol B — Coach de carrera orientado a posicionamiento y comunicación

Debe convertir la estrategia ya aprobada en una narrativa convincente sin reabrirla.

Debe decidir:

- qué merece narrarse;
- qué conexión necesita explicación;
- qué motivación es útil;
- qué carencia conviene contextualizar;
- qué debe dejarse al CV;
- cómo presentar seniority;
- cómo cerrar invitando a continuar el proceso.

No decide nuevos hechos ni nuevas estrategias.

---

## Rol C — Auditor senior de factualidad y flujo

Comprueba:

```text
analisis-oferta
→ candidatura
→ fuentes factuales
→ declaraciones usuario
→ contexto empresa
→ guion carta
```

Debe impedir:

- requisito → experiencia;
- cultura → atributo personal;
- inferencia → motivación;
- formación → experiencia;
- intermediario → empleador;
- empresa anónima → empresa identificada;
- frase corporativa → afinidad personal;
- carencia → falsa fortaleza.

---

# 17. Procedimiento normativo

El orden es obligatorio.

## Paso 1 — Validar precondiciones

Confirmar:

- candidatura;
- estado;
- fuentes;
- bloqueo;
- presentación;
- empresa/destinatario.

---

## Paso 2 — Cargar estrategia heredada

Extraer sin modificar:

- posicionamiento;
- tesis;
- evidencias prioritarias;
- carencias;
- riesgos;
- exclusiones;
- mensaje profesional;
- seniority;
- límites.

---

## Paso 3 — Analizar la oferta para la carta

Extraer específicamente:

```text
necesidades funcionales
problemas que debe resolver el puesto
atributos buscados
lenguaje relevante
señales culturales
propuesta de empleador
```

No volver a realizar el análisis estratégico completo.

---

## Paso 4 — Resolver destinatario

Clasificar:

```text
empresa_identificada
intermediario_con_empresa_identificada
intermediario_con_empresa_anonima
```

Determinar:

```text
destinatario_real
forma_de_direccion
nivel_de_personalizacion_posible
```

---

## Paso 5 — Resolver contexto cultural externo

Si existe URL registrada:

```text
→ analizar
```

Si no existe y la empresa está identificada:

```text
→ solicitar opcionalmente al usuario
```

Si no se aporta:

```text
→ continuar
```

Si empresa anónima:

```text
→ no solicitar
```

---

## Paso 6 — Obtener motivación humana necesaria

Determinar si existen declaraciones verificadas sobre:

- interés por puesto;
- interés por empresa;
- relación previa;
- preferencia profesional;
- motivos concretos.

Preguntar únicamente lo necesario.

No inducir respuestas positivas.

---

## Paso 7 — Construir matriz de afirmaciones permitidas

Cada afirmación candidata debe clasificarse como:

```text
hecho_profesional
motivacion_declarada
razon_profesional
contexto_empresa
contexto_oferta
no_acreditada
```

`no_acreditada`:

```text
→ prohibida
```

---

## Paso 8 — Definir objetivo comunicativo

El guion debe establecer una frase operativa del tipo:

```text
La carta debe conseguir que el recruiter entienda que [...]
```

Debe ser concreta para la candidatura.

---

## Paso 9 — Diseñar el gancho inicial

La apertura debe:

- identificar oportunidad;
- establecer rápidamente relevancia;
- aportar una razón para seguir leyendo.

Evitar aperturas vacías como:

```text
"Me pongo en contacto con ustedes..."
"Por medio de la presente..."
"Adjunto mi candidatura..."
```

salvo necesidad contextual.

---

## Paso 10 — Definir argumento central

Debe conectar:

```text
necesidad de la oportunidad
+
evidencia del candidato
+
valor aportable
```

El argumento central no es una lista de competencias.

---

## Paso 11 — Seleccionar evidencias narrables

Escoger pocas evidencias de alta utilidad argumentativa.

Cada evidencia debe justificar:

```text
por_que_aparece
que_demuestra
con_que_necesidad_conecta
que_limite_tiene
```

La carta no debe intentar contener todas las evidencias del CV.

---

## Paso 12 — Diseñar relación con empresa/cultura

Para cada señal cultural utilizable:

```text
señal corporativa
        ↓
¿existe conexión factual o declaración personal?
        │
      sí ─→ puede utilizarse
      no ─→ no atribuir afinidad
```

El guion puede recomendar mencionar la señal sin afirmar identidad personal con ella.

---

## Paso 13 — Decidir tratamiento de carencias

Cada carencia debe clasificarse:

```text
no_mencionar
contextualizar
reconocer_brevemente
bloqueante_para_carta
```

La carta no debe convertir una carencia en el centro de la comunicación salvo necesidad estratégica excepcional.

No debe pedir disculpas por carencias.

No debe ocultarlas mediante afirmaciones ambiguas.

---

## Paso 14 — Definir cobertura semántica ATS/IA

Identificar vocabulario útil procedente de la oferta:

- puesto;
- funciones;
- competencias;
- procesos;
- sector;
- herramientas;
- resultados;
- conceptos profesionales.

Clasificar:

```text
utilizable
uso_condicionado
prohibido_como_atributo
```

Regla:

> Las keywords aparecen porque forman parte natural del argumento, no porque exista una cuota ATS que cubrir.

No usar keyword stuffing.

---

## Paso 15 — Diseñar estructura narrativa

La estructura debe ser breve.

Patrón orientativo:

```text
1. apertura relevante
2. argumento principal
3. evidencia / conexión
4. empresa / motivación, cuando proceda
5. cierre
```

No es obligatorio utilizar cinco párrafos.

El guion decide la estructura adecuada al caso.

---

## Paso 16 — Definir tono

Registrar explícitamente:

```text
tono
grado_formalidad
grado_cercania
nivel_tecnico
nivel_directividad
```

El lenguaje debe ser:

- profesional;
- natural;
- directo;
- humano;
- específico.

Evitar:

- solemnidad innecesaria;
- lenguaje excesivamente corporativo;
- frases hechas;
- superlativos sin respaldo;
- estilo artificialmente entusiasta.

---

## Paso 17 — Definir longitud

La carta debe ser suficientemente breve para favorecer lectura real.

El guion debe fijar:

```text
longitud_objetivo
numero_aproximado_parrafos
densidad
```

La extensión nunca se aumenta para rellenar espacio.

---

## Paso 18 — Establecer relación con el CV

El guion debe declarar explícitamente:

```text
que_interpreta_del_cv
que_no_debe_repetir
que_contexto_anade
```

Regla:

> **Si un párrafo puede sustituirse por tres bullets del CV sin perder información, probablemente no aporta suficiente valor como carta.**

---

## Paso 19 — Control de recruiter humano

Comprobar que:

- el propósito aparece rápido;
- existe argumento;
- no hay introducción vacía;
- la evidencia es específica;
- la personalización es real;
- la motivación es creíble;
- el texto proyectado es breve;
- existe una razón para continuar al CV o entrevista.

---

## Paso 20 — Control recruiter IA / ATS

Comprobar:

- puesto reconocible;
- necesidades relevantes presentes;
- vocabulario profesional compatible;
- conexiones semánticas claras;
- keywords respaldadas;
- ausencia de stuffing;
- naturalidad intacta.

---

## Paso 21 — Control de factualidad

Verificar:

- hechos;
- métricas;
- herramientas;
- cargos;
- motivaciones;
- relación con empresa;
- cultura;
- seniority;
- carencias.

---

## Paso 22 — Generar `guion-carta-presentacion.md`

El artefacto debe contener decisiones, no prosa final.

---

## Paso 23 — Evaluar gate de salida

Crear o actualizar el artefacto oficial correspondiente a:

```text
GATE-GUION-CARTA-CONTENIDO
```

El estado del gate no vive dentro del guion.

---

# 18. Mapa argumental de la carta

Cada unidad utiliza:

```text
A-NNN
```

Campos mínimos:

```text
ref_local
funcion_argumental
idea
tipo_afirmacion
fuente
evidencia
necesidad_objetivo
presencia
obligatoriedad
orden
nivel_detalle
relacion_cv
personalizacion
limites
prohibiciones
```

---

# 19. Tipos de unidad argumental

Valores preferentes:

```text
apertura
argumento
evidencia
resultado
conexion_oferta
conexion_empresa
motivacion
contextualizacion
tratamiento_carencia
cierre
otro
```

`otro` requiere justificación.

---

# 20. Funciones estratégicas

Una unidad puede cumplir:

```text
captar_atencion
explicar_encaje
demostrar_valor
humanizar
diferenciar
conectar_empresa
contextualizar
mitigar_riesgo
reforzar_keyword
invitar_conversacion
```

---

# 21. Personalización

Niveles:

```text
puesto
oferta
empresa
cultura
motivacion_usuario
```

La carta no necesita alcanzar todos.

Casos:

```text
empresa anónima
→ puesto + oferta

empresa conocida sin cultura adicional
→ puesto + oferta + empresa

empresa conocida con cultura
→ puesto + oferta + empresa + cultura

motivación verificada
→ puede añadirse motivacion_usuario
```

La falta de niveles superiores no penaliza si no están disponibles.

---

# 22. Regla contra la carta genérica

El guion debe comprobar:

> ¿Podría utilizarse prácticamente la misma carta para otra empresa cambiando solo el nombre?

Si:

```text
sí
```

el guion requiere corrección.

La personalización no exige elogiar a la empresa.

Puede consistir en:

- problema concreto;
- función concreta;
- contexto concreto;
- evidencia concreta.

---

# 23. Regla contra el segundo CV

La carta no debe:

- enumerar cronología;
- reproducir todas las responsabilidades;
- repetir secciones de habilidades;
- enumerar herramientas sin función argumental;
- copiar bullets.

La carta debe explicar:

```text
por qué esas evidencias importan aquí
```

---

# 24. ATS, IA recruiter y humano

El guion reconoce tres tipos de lectura:

## ATS clásico

Necesita:

- términos reconocibles;
- estructura textual clara;
- ausencia de artificios innecesarios.

## IA recruiter

Necesita:

- conexión semántica clara;
- evidencia;
- contexto;
- ausencia de contradicciones.

## Recruiter humano

Necesita:

- relevancia;
- brevedad;
- credibilidad;
- interés;
- claridad.

Prioridad:

```text
1. factualidad
2. utilidad recruiter
3. argumentación
4. naturalidad y legibilidad
5. compatibilidad ATS/IA
```

---

# 25. Léxico

Clasificar:

```text
utilizable
uso_condicionado
prohibido
```

No se permite:

- keyword stuffing;
- copiar frases corporativas de forma artificial;
- introducir tecnologías solo porque aparecen en la oferta;
- presentar atributos deseados como atributos poseídos;
- utilizar valores de empresa como autoatribución.

---

# 26. Tratamiento de carencias

La carta no sirve para ocultar carencias estructurales.

Puede:

- orientar la atención hacia evidencia real;
- explicar transferibilidad;
- contextualizar una transición;
- reconocer brevemente una limitación cuando sea estratégicamente necesario.

No puede:

- convertir transferibilidad en experiencia literal;
- convertir formación en experiencia;
- prometer dominio inexistente;
- sustituir evidencia faltante con entusiasmo.

---

# 27. Motivación y cultura — reglas negativas

Queda prohibido generar sin respaldo:

```text
"Me apasiona..."
"Siempre he querido..."
"Admiro..."
"Comparto sus valores..."
"Sigo a su empresa desde hace años..."
"Me identifico plenamente con su cultura..."
```

Una formulación puede ser legítima únicamente si existe:

```text
declaracion_usuario
```

o si se formula como hecho profesional no emocional.

---

# 28. Idioma

El guion debe fijar:

```text
idioma_carta
```

Reglas por prioridad:

1. instrucción expresa;
2. idioma requerido por la oportunidad;
3. idioma principal inequívoco de la oferta;
4. coherencia con el paquete cuando exista autoridad documentada.

Si existe ambigüedad:

```text
requiere_revision_origen
```

No seleccionar silenciosamente.

---

# 29. Incidencias

| Situación | Resultado |
| --- | --- |
| Error argumental local | `requiere_correccion` |
| Motivación necesaria pero no verificada | `requiere_interaccion_usuario` |
| URL opcional no aportada | no incidencia |
| Empresa anónima | no incidencia |
| Cultura no disponible | no incidencia |
| Contradicción estrategia/origen | `requiere_revision_origen` |
| Evidencia factual nueva | `requiere_actualizacion_factual` |
| Fuente necesaria inaccesible | `bloqueado` |
| Afirmación personal no verificable | omitir o `requiere_interaccion_usuario` |
| Contradicción arquitectónica | `bloqueado` |

---

# 30. Nueva evidencia factual

Si durante la preparación aparece un nuevo hecho profesional relevante:

```text
→ no incorporarlo localmente
```

Debe volver al mecanismo factual correspondiente:

```text
datos-core-busqueda
        ↓
analisis-oferta
        ↓
candidatura
        ↓
nuevo guion carta
```

No parchear el guion.

---

# 31. Cambios en declaraciones personales

Una nueva declaración de motivación del usuario no es automáticamente una nueva evidencia profesional.

Debe:

- registrarse como declaración del usuario;
- conservar fecha/procedencia;
- utilizarse únicamente como afirmación personal.

No requiere modificar `datos-core-busqueda.md` salvo que contenga además un hecho profesional nuevo.

---

# 32. Control previo al gate

Antes de evaluar `GATE-GUION-CARTA-CONTENIDO`:

- [ ] candidatura vigente;
- [ ] `presentada: false`;
- [ ] estrategia intacta;
- [ ] oferta analizada para carta;
- [ ] destinatario clasificado;
- [ ] empresa anónima tratada correctamente, si procede;
- [ ] cultura de la oferta identificada;
- [ ] URL previa utilizada si existía;
- [ ] URL opcional solicitada cuando procedía;
- [ ] ausencia de URL no tratada como bloqueo;
- [ ] motivaciones utilizadas verificadas;
- [ ] no existen sentimientos inventados;
- [ ] argumento central definido;
- [ ] evidencias seleccionadas;
- [ ] relación con CV explícita;
- [ ] carencias tratadas;
- [ ] cobertura semántica definida;
- [ ] ATS/IA contemplados sin stuffing;
- [ ] tono definido;
- [ ] idioma definido;
- [ ] longitud definida;
- [ ] prohibiciones explícitas;
- [ ] no existe prosa final de carta;
- [ ] trazabilidad suficiente.

---

# 33. Gate de salida

`GATE-GUION-CARTA-CONTENIDO` responde:

> **¿El guion contiene decisiones suficientes, factual y estratégicamente coherentes para autorizar la redacción de la carta sin que la siguiente capa tenga que inventar estrategia, motivaciones, cultura o evidencia?**

Resultados propuestos:

```text
apto
requiere_correccion
requiere_interaccion_usuario
requiere_revision_origen
requiere_actualizacion_factual
bloqueado
```

Precedencia:

```text
bloqueado
>
requiere_actualizacion_factual
>
requiere_revision_origen
>
requiere_interaccion_usuario
>
requiere_correccion
>
apto
```

La IA puede recomendar.

La decisión humana oficial se registra en el artefacto de gate correspondiente.

---

# 34. Contenido mínimo de `guion-carta-presentacion.md`

Debe contener como mínimo:

## Identificación

- candidatura;
- empresa;
- puesto;
- destinatario;
- tipo de empresa;
- idioma.

## Fuentes

- candidatura;
- análisis;
- oferta;
- fuentes factuales;
- declaraciones usuario;
- URL cultural si existe.

## Contexto de empresa

- identidad;
- anonimato;
- intermediario;
- señales culturales;
- propuesta de empleador;
- procedencia.

## Motivación verificada

- declaraciones disponibles;
- razones profesionales;
- afirmaciones no permitidas.

## Objetivo comunicativo

Una frase operativa.

## Argumento central

La tesis de la carta.

## Mapa argumental

Unidades `A-NNN`.

## Evidencias narrables

Con límites.

## Relación con CV

- qué complementa;
- qué no repite.

## Personalización

- oferta;
- empresa;
- cultura;
- motivación.

## Tratamiento de carencias

Decisión por carencia.

## Cobertura ATS/IA

- vocabulario utilizable;
- condicionado;
- prohibido.

## Arquitectura narrativa

- apertura;
- desarrollo;
- cierre;
- orden.

## Tono e idioma

Explícitos.

## Longitud

Objetivo.

## Prohibiciones

Lista específica.

## Control recruiter

Resultado de primer escaneo argumental.

## Incidencias

Todas las detectadas.

---

# 35. Postcondiciones

Un guion `apto` debe permitir a la futura capa de contenido redactar la carta sin decidir:

- estrategia;
- motivación;
- cultura;
- evidencias;
- destinatario;
- argumentos;
- tratamiento de carencias;
- palabras clave fundamentales;
- tono;
- longitud;
- idioma.

La siguiente capa podrá redactar.

No podrá rediseñar.

---

# 36. Casos de aceptación obligatorios

Antes de considerar generalizable el playbook deben probarse al menos:

## Caso A — Empresa identificada + cultura en oferta + URL oficial

Debe combinar fuentes manteniendo procedencia.

## Caso B — Empresa identificada + cultura solo en oferta

Debe generar guion apto sin URL.

## Caso C — Empresa identificada + URL aportada desde inicio

No debe volver a pedirla.

## Caso D — Empresa identificada + sin URL

Debe ofrecer al usuario aportarla y continuar si no dispone de ella.

## Caso E — Empresa anónima mediante intermediario

Debe:

- no intentar descubrirla;
- no pedir URL;
- no utilizar cultura del intermediario;
- personalizar por oportunidad.

## Caso F — Usuario con motivación específica real

Debe permitir incorporarla.

## Caso G — Usuario sin motivación específica

Debe producir guion apto sin inventarla.

## Caso H — Keyword ATS sin evidencia

Debe prohibir su atribución al candidato.

## Caso I — Cultura sin conexión factual

Debe poder utilizar el contexto, pero no afirmar afinidad personal.

---

# 37. Criterios de aceptación del playbook

El playbook se considera apto para implantación cuando:

- [ ] mantiene `candidatura.md` como estrategia común;
- [ ] no redacta la carta;
- [ ] no reabre la competitividad;
- [ ] distingue plataforma, intermediario y empleador;
- [ ] soporta empresa anónima;
- [ ] usa cultura de la oferta;
- [ ] soporta URL aportada al inicio;
- [ ] solicita URL posteriormente solo cuando procede;
- [ ] URL externa es opcional;
- [ ] obtiene motivación verificable del usuario;
- [ ] acepta ausencia de motivación específica;
- [ ] no inventa emociones;
- [ ] cultura no se convierte en atributo del candidato;
- [ ] carta complementa al CV;
- [ ] evita segundo CV narrativo;
- [ ] incorpora ATS/IA sin keyword stuffing;
- [ ] distingue recruiter humano, IA y ATS;
- [ ] clasifica carencias;
- [ ] mantiene trazabilidad;
- [ ] bloquea nueva evidencia no propagada;
- [ ] produce un guion suficiente para una capa de redacción separada.

---

# 38. Principios finales

> **La carta no demuestra más experiencia de la que existe. Explica mejor por qué la experiencia existente importa para esta oportunidad.**

> **Personalizar no significa halagar a la empresa. Significa hablar de esta oportunidad concreta con razones verdaderas.**

> **Una motivación modesta pero verdadera es mejor que una motivación intensa inventada.**

> **La ausencia de información cultural no autoriza a fabricarla.**

> **Una empresa anónima no impide una buena carta; cambia el objeto de la personalización.**

> **ATS e IA deben reconocer el encaje porque el argumento es semánticamente claro y factual, no porque la carta esté saturada de keywords.**

> **El guion decide qué debe decir la carta. La fase siguiente decide cómo redactarlo.**
