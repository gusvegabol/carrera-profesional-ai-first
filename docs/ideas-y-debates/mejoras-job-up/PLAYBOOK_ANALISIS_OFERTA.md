# PLAYBOOK_GENERAR_ANALISIS_OFERTA.md

## 1. Propósito

Este playbook define cómo debe generarse `analisis-oferta.md` dentro de una candidatura.

Su función es producir un análisis factual y estratégico de una oferta de empleo que permita decidir:

* qué dice realmente la oferta;
* qué necesidad parece existir detrás de la contratación;
* qué requisitos condicionan el encaje;
* qué evidencias de la trayectoria profesional son relevantes;
* qué tipo de correspondencia existe entre oferta y trayectoria;
* qué carencias y riesgos existen;
* desde qué argumento puede competir honestamente la candidatura;
* si conviene continuar;
* qué límites deberán respetar posteriormente el CV, la carta y otros documentos.

No es función de este playbook redactar:

* el CV final;
* la carta de presentación;
* titulares definitivos de CV;
* bloques finales de experiencia;
* respuestas finales a formularios de candidatura.

`analisis-oferta.md` es una **capa de decisión, trazabilidad y gobierno factual**, no un documento comercial final.

---

## 2. Arquitectura: playbook, template y artefacto

El sistema distingue tres niveles.

### 2.1 Playbook

Este documento es la **fuente normativa**.

Define:

* cómo debe razonarse;
* qué controles factuales deben aplicarse;
* qué decisiones deben producirse;
* qué criterios de calidad deben cumplirse.

### 2.2 Template

`TEMPLATE_ANALISIS_OFERTA_v2.md` es el **contrato operativo de materialización**.

Define:

* estructura;
* campos;
* tablas;
* placeholders;
* controles locales de cierre.

El template no sustituye al playbook.

Si existe contradicción entre ambos, prevalece el playbook hasta que la discrepancia sea resuelta explícitamente.

### 2.3 Artefacto

`analisis-oferta.md` contiene exclusivamente el resultado concreto de ejecutar:

> oferta + contexto empresarial + datos core + playbook + template.

Las instrucciones del template no deben aparecer como contenido del artefacto final.

---

## 3. Separación entre proceso y salida

### 3.1 Proceso de análisis

La IA debe recorrer las fases de razonamiento de la sección 7.

Sirven para asegurar:

* profundidad;
* mirada crítica;
* trazabilidad;
* consistencia.

### 3.2 Contrato documental

Las fases de razonamiento **no deben reproducirse mecánicamente como once secciones**.

El artefacto final seguirá la estructura definida por `TEMPLATE_ANALISIS_OFERTA_v2.md` y resumida en la sección 8.

Principio:

> La profundidad pertenece al proceso; la claridad, densidad informativa y trazabilidad pertenecen al artefacto.

---

## 4. Rol de la IA

La IA debe combinar estos roles:

1. reclutador experto en selección;
2. reclutador escéptico que busca motivos de descarte;
3. reclutador estratégico que busca cómo hacer defendible una candidatura;
4. consultor de empleabilidad;
5. analista de ofertas;
6. auditor factual;
7. preparador de brief para skills posteriores.

Debe evitar dos sesgos.

### 4.1 Sesgo de encaje

No intentar demostrar que el candidato cumple una oferta cuando las evidencias no lo sostienen.

### 4.2 Sesgo de descarte

No tratar automáticamente una carencia literal como impeditiva cuando exista evidencia profesional transferible que razonablemente pueda compensarla.

---

## 5. Entradas

### 5.1 Oferta

Utilizar cuando estén disponibles:

* texto completo;
* ficha estructurada;
* transcripción;
* URL original;
* plataforma;
* fecha de consulta.

Debe registrarse el estado de la fuente:

* `texto_completo`;
* `transcripcion_condensada`;
* `fuente_parcial`;
* `no_disponible`.

Si la fuente presenta limitaciones, deben quedar explícitas.

---

### 5.2 Empresa

Deben distinguirse expresamente:

#### Empresa publicadora

Entidad que publica, intermedia o gestiona el proceso de selección.

#### Empresa contratante

Entidad para la que se desempeñará realmente el puesto.

Estados posibles:

* identificada;
* no identificada;
* coincidente con empresa publicadora.

Nunca deben transferirse características de una empresa a otra sin evidencia.

Cuando exista URL corporativa o investigación previa, incorporar únicamente información factual relevante para interpretar el puesto.

---

### 5.3 Datos core del candidato

Debe utilizarse la fuente factual completa disponible sobre:

* trayectoria;
* cargos;
* responsabilidades;
* logros;
* herramientas;
* formación;
* métricas;
* conocimientos;
* resultados;
* atribuciones;
* límites;
* precauciones de redacción.

Cuando existan identificadores como `HER-01`, `GSC-01`, etc., deben conservarse.

Los datos core son la **fuente de autoridad sobre la trayectoria profesional**.

---

### 5.4 Metadatos

Registrar:

* identificador de candidatura;
* fecha de análisis;
* empresa publicadora;
* empresa contratante;
* puesto;
* sesión PCS o referencia interna, si existe.

---

### 5.5 Datos privados

Los datos privados de contacto o candidatura no forman parte de las entradas normales de este playbook.

Solo podrán utilizarse si:

1. una necesidad concreta del análisis lo exige;
2. existe autorización expresa;
3. su uso no puede resolverse mediante datos no privados.

---

## 6. Principios obligatorios

### 6.1 No invención

No inventar:

* titulaciones;
* certificaciones;
* herramientas;
* métricas;
* responsabilidades;
* empresas;
* cargos;
* idiomas;
* años de experiencia;
* nivel de dominio;
* tecnologías;
* resultados;
* experiencia profesional;
* autorizaciones;
* datos privados.

Estados factuales admitidos:

* `acreditado`;
* `parcialmente acreditado`;
* `no acreditado`;
* `no disponible`.

Las interpretaciones deberán etiquetarse como:

* `inferencia razonable`;
* `estimación estratégica`.

---

### 6.2 Separación de capas

Distinguir siempre:

**Oferta**
: información declarada por la fuente de empleo.

**Empresa**
: información factual obtenida externamente.

**Trayectoria**
: hechos presentes en los datos core.

**Inferencia**
: interpretación razonada.

**Estrategia**
: decisión sobre cómo competir.

**Límite**
: afirmación prohibida o que requiere matiz.

Una inferencia nunca debe presentarse como hecho.

---

### 6.3 Formación no equivale a experiencia

Formación, actualización o uso no profesional no deben convertirse en experiencia laboral.

Utilizar, según corresponda:

* formación;
* actualización;
* conocimiento en desarrollo;
* exposición formativa;
* experiencia no profesional.

---

### 6.4 Automatización no equivale a IA

No convertir automáticamente en Inteligencia Artificial:

* algoritmos;
* automatizaciones;
* hojas de cálculo;
* scripts;
* programación;
* integraciones;
* bases de datos;
* dashboards;
* análisis de datos;
* herramientas internas.

Solo podrá atribuirse experiencia profesional en IA cuando los datos core la acrediten expresamente.

---

### 6.5 Encaje funcional no equivale a coincidencia tecnológica

Una misma necesidad de la oferta puede estar cubierta funcionalmente mediante tecnologías diferentes.

Ejemplo:

> La oferta solicita automatización de procesos mediante una tecnología concreta.

Puede existir:

* experiencia real automatizando procesos;
* pero ninguna experiencia con esa herramienta concreta.

Ambas dimensiones deben mantenerse separadas.

Estados de `tipo de encaje`:

* `funcional`;
* `tecnologico_literal`;
* `ambos`;
* `sin_encaje`.

El tipo de encaje no determina por sí solo su fuerza.

---

### 6.6 Fuerza del encaje

La matriz utilizará:

* `alta`;
* `media`;
* `baja`;
* `no_acreditada`.

La fuerza debe evaluarse considerando:

* similitud del problema;
* responsabilidad real;
* contexto profesional;
* resultados;
* actualidad cuando sea relevante;
* grado de transferencia;
* coincidencia tecnológica cuando resulte crítica.

---

### 6.7 Trazabilidad

Toda evidencia relevante debe enlazarse, cuando sea posible, con su identificador factual.

Evitar:

> Tiene experiencia automatizando.

Preferir:

> `HER-01` acredita automatización documental y administrativa con resultados medidos.

La descripción dentro de la matriz debe ser breve.

La evidencia completa permanece en los datos core.

---

### 6.8 Mirada crítica

El análisis debe buscar simultáneamente:

* razones para considerar la candidatura;
* razones para descartarla.

No suavizar carencias importantes.

No dramatizar carencias menores.

---

### 6.9 Economía documental

Una misma carencia o evidencia no debe desarrollarse repetidamente.

Principio:

> Registrar una vez con detalle; reutilizar después mediante síntesis.

La matriz de encaje y la tabla de carencias son las fuentes principales para las secciones estratégicas posteriores.

---

### 6.10 No redactar documentos posteriores

`analisis-oferta.md` puede contener:

* estrategia;
* posicionamiento;
* selección factual;
* límites;
* brief;
* palabras clave;
* tono recomendado.

No debe contener:

* perfil final de CV;
* experiencia final ya redactada;
* carta;
* titulares definitivos;
* textos comerciales listos para enviar.

---

## 7. Proceso de análisis

La IA debe recorrer internamente once fases.

### Fase 1 — Extracción factual

Capturar sin interpretar:

* empresa publicadora;
* empresa contratante;
* puesto;
* fuente;
* URL;
* modalidad;
* ubicación;
* jornada;
* contrato;
* salario;
* seniority;
* personas a cargo;
* funciones;
* requisitos;
* herramientas;
* competencias;
* condiciones;
* palabras clave.

---

### Fase 2 — Contexto empresarial

Determinar únicamente a partir de información verificable:

* actividad;
* contexto relevante;
* señales de transformación;
* características que ayuden a interpretar el puesto.

Evitar investigación corporativa que no tenga efecto sobre el análisis.

Si publicador y contratante son distintos, mantenerlos separados.

---

### Fase 3 — Lectura estratégica

Determinar como `inferencia razonable`:

* por qué parece existir el puesto;
* qué problema empresarial intenta resolver;
* qué impacto se espera;
* qué perfil parece necesitar realmente;
* qué señales revelan prioridades.

---

### Fase 4 — Jerarquía de requisitos

Clasificar:

* `critico`;
* `importante_pero_compensable`;
* `deseable`;
* `dificil_de_compensar`.

La clasificación debe justificarse mediante señales de la oferta.

---

### Fase 5 — Uso seguro del lenguaje

Clasificar términos como:

* `literal_de_la_oferta`;
* `utilizable_con_respaldo_factual`;
* `utilizable_solo_con_matiz`;
* `no_utilizable_como_experiencia`.

No asumir que una palabra clave puede trasladarse al CV únicamente porque aparezca en la oferta.

---

### Fase 6 — Matriz de encaje factual

Para cada necesidad relevante, analizar:

> necesidad → evidencia → tipo de encaje → fuerza → límite.

No analizar la trayectoria cronológicamente.

Priorizar las necesidades que puedan afectar:

* descarte;
* posicionamiento;
* argumento competitivo;
* redacción posterior.

No es obligatorio incluir requisitos triviales sin efecto estratégico.

---

### Fase 7 — Carencias

Registrar de forma consolidada las carencias relevantes.

Para cada una indicar:

* estado;
* efecto probable;
* tratamiento.

Tratamientos posibles:

* `no_afirmar`;
* `matizar`;
* `pedir_dato`;
* `compensar_funcionalmente`;
* otro tratamiento explícitamente justificado.

No volver a desarrollar esas carencias completas en secciones posteriores.

---

### Fase 8 — Lectura de descarte

Simular:

* posible filtro previo;
* lectura humana;
* dudas de credibilidad;
* sobrecualificación;
* infracualificación;
* dispersión;
* déficit formal;
* déficit tecnológico;
* déficit sectorial u otros relevantes.

Los niveles de riesgo son `estimaciones estratégicas`.

No afirmar conocer mecanismos de ATS o filtros internos salvo evidencia.

Para cada riesgo debe evaluarse si existe mitigación factual.

---

### Fase 9 — Argumento competitivo y posicionamiento

Responder:

> ¿Por qué debería entrevistarse a esta persona pese a sus carencias?

El argumento debe:

* surgir de la matriz;
* responder al problema del puesto;
* apoyarse en evidencias;
* reconocer límites;
* ser suficientemente diferencial.

Después definir:

* posicionamiento principal;
* posicionamiento secundario, si aporta;
* enfoques a evitar.

El posicionamiento no debe surgir de una taxonomía predeterminada.

---

### Fase 10 — Selección y decisión

Determinar:

* qué debe dominar la candidatura;
* qué debe quedar en segundo plano;
* qué evidencias priorizar;
* qué afirmaciones excluir;
* qué tono utilizar.

No existe número fijo de logros.

Seleccionar los mínimos necesarios para sostener el argumento.

Elegir una decisión:

* `preparar_candidatura`;
* `preparar_con_advertencias`;
* `pedir_datos_adicionales_antes_de_redactar`;
* `no_recomendada`.

---

### Fase 11 — Brief operativo

Convertir el análisis en instrucciones compactas para las skills posteriores.

El brief debe permitir continuar sin releer todo el razonamiento.

No debe repetir el análisis completo.

---

## 8. Contrato de `analisis-oferta.md`

La materialización concreta se rige por `TEMPLATE_ANALISIS_OFERTA_v2.md`.

Su estructura canónica es:

```md
---
id: analisis-oferta-[ID_CANDIDATURA]
tipo: analisis_oferta
fecha_analisis: [AAAA-MM-DD]
candidatura: [ID_CANDIDATURA]
empresa_publicadora: [NOMBRE_O_NO_DISPONIBLE]
empresa_contratante: [NOMBRE_O_NO_IDENTIFICADA]
puesto: [PUESTO]
sesion_pcs: [REFERENCIA_O_NO_ASIGNADA]
---

# Análisis de oferta — [ID_CANDIDATURA]

## 1. Identificación de la oferta

## 2. Fuente y contenido factual
### 2.1 Fuente de la oferta
### 2.2 Contexto empresarial disponible
### 2.3 Funciones explícitas
### 2.4 Requisitos explícitos
### 2.5 Tecnologías, competencias y condiciones

## 3. Lectura estratégica
### 3.1 Problema de negocio probable
### 3.2 Perfil realmente buscado
### 3.3 Impacto esperado

## 4. Requisitos y lenguaje de candidatura
### 4.1 Jerarquía de requisitos
### 4.2 Uso seguro de palabras clave

## 5. Matriz de encaje factual

| Necesidad o requisito | Evidencia factual del candidato | Tipo de encaje | Fuerza | Límite o precaución |
|---|---|---|---|---|

### 5.1 Carencias relevantes

| Carencia | Estado | Efecto probable | Tratamiento requerido |
|---|---|---|---|

## 6. Lectura de descarte
### 6.1 Principales riesgos
### 6.2 Lectura probable del perfil
### 6.3 Condiciones para mantener credibilidad

## 7. Estrategia de candidatura
### 7.1 Argumento competitivo defendible
### 7.2 Posicionamiento
### 7.3 Selección factual
### 7.4 Afirmaciones excluidas

## 8. Decisión y brief para skills posteriores
### 8.1 Decisión estratégica
### 8.2 Advertencias y dudas
### 8.3 Brief operativo
```

---

## 9. Reglas del artefacto

### 9.1 Identificación

Debe distinguir siempre:

* empresa publicadora;
* empresa contratante.

Si no se conoce la empresa contratante:

`no_identificada`

No inferirla.

---

### 9.2 Fuente

Registrar:

* disponibilidad del contenido;
* referencia trazable;
* limitaciones.

No es obligatorio copiar una oferta extensa si existe referencia fiable y accesible.

Si se utiliza transcripción condensada, indicarlo.

---

### 9.3 Contexto empresarial

Incorporar únicamente hechos que ayuden a interpretar:

* puesto;
* actividad;
* transformación;
* dimensiones relevantes;
* necesidad empresarial.

Si no existe información útil:

`no_disponible`

---

### 9.4 Jerarquía

Cada requisito debe incluir:

* clasificación;
* motivo basado en señales de la oferta.

No clasificar por intuición aislada.

---

### 9.5 Palabras clave

La tabla debe impedir contaminación entre oferta y trayectoria.

Una tecnología presente en la oferta no pasa automáticamente a ser una competencia del candidato.

---

### 9.6 Matriz de encaje

Es el núcleo factual del documento.

Debe diferenciar explícitamente:

**Tipo**

* funcional;
* tecnológico literal;
* ambos;
* sin encaje.

**Fuerza**

* alta;
* media;
* baja;
* no acreditada.

Ejemplo conceptual:

| Necesidad                  | Evidencia                          | Tipo       | Fuerza        |
| -------------------------- | ---------------------------------- | ---------- | ------------- |
| Automatización de procesos | Evidencia real con otra tecnología | funcional  | alta          |
| Power Automate             | Sin experiencia documentada        | sin encaje | no acreditada |

Esta separación es obligatoria.

---

### 9.7 Carencias relevantes

La tabla de carencias es el inventario canónico.

Cada carencia debe indicar:

* estado;
* efecto probable;
* tratamiento requerido.

Las secciones posteriores deben referirse a ellas mediante síntesis.

---

### 9.8 Riesgos

La lectura de descarte debe representar riesgos como hipótesis o estimaciones.

Evitar:

> El ATS descartará la candidatura.

Preferir:

> Existe riesgo de filtro previo debido a...

Cuando sea posible, registrar:

* riesgo;
* nivel estimado;
* motivo;
* mitigación factual.

---

### 9.9 Argumento competitivo

Debe formular una tesis compacta.

No debe ser:

* resumen cronológico;
* lista genérica de fortalezas;
* perfil de CV;
* carta;
* enumeración de logros.

Debe responder al problema detectado en la oferta.

---

### 9.10 Selección factual

Debe indicar:

* qué debe dominar;
* qué debe quedar en segundo plano;
* qué evidencias son prioritarias.

No existe número fijo.

---

### 9.11 Afirmaciones excluidas

Toda afirmación prohibida debe incluir:

* motivo;
* alternativa permitida, si existe.

Ejemplo:

| Afirmación                   | Motivo        | Alternativa                        |
| ---------------------------- | ------------- | ---------------------------------- |
| Experiencia profesional en X | No acreditada | Formación en X, si está acreditada |

---

### 9.12 Decisión

Valores admitidos exclusivamente:

* `preparar_candidatura`;
* `preparar_con_advertencias`;
* `pedir_datos_adicionales_antes_de_redactar`;
* `no_recomendada`.

La decisión debe estar justificada por:

* matriz;
* carencias;
* riesgos;
* argumento competitivo.

---

### 9.13 Brief

Debe incluir como mínimo:

* ángulo;
* evidencias prioritarias;
* palabras utilizables con respaldo;
* palabras utilizables solo con matiz;
* afirmaciones prohibidas;
* riesgos que debe gestionar la redacción;
* tono;
* contenido a evitar o relegar;
* decisión.

Debe poder ser consumido directamente por una skill posterior.

---

## 10. Control de calidad del playbook

Antes de considerar terminado `analisis-oferta.md`, verificar:

### Fidelidad

1. ¿La oferta está representada fielmente?
2. ¿La fuente y sus limitaciones están registradas?
3. ¿Empresa publicadora y contratante están diferenciadas?
4. ¿No se han transferido características entre empresas sin evidencia?

### Integridad factual

5. ¿Cada afirmación sobre trayectoria está respaldada?
6. ¿Los identificadores de evidencia son correctos?
7. ¿Formación y experiencia están diferenciadas?
8. ¿Automatización e IA están diferenciadas?
9. ¿Las tecnologías de la oferta no han contaminado las competencias del candidato?

### Encaje

10. ¿La matriz distingue encaje funcional y tecnológico literal?
11. ¿La fuerza del encaje está evaluada independientemente de su tipo?
12. ¿Las carencias relevantes aparecen explícitamente?
13. ¿Las evidencias débiles no se presentan como fuertes?

### Calidad estratégica

14. ¿Se identifica el problema empresarial probable?
15. ¿Los requisitos están jerarquizados?
16. ¿Existe una lectura suficientemente crítica de descarte?
17. ¿Los riesgos están formulados como estimaciones cuando corresponde?
18. ¿Existe un argumento competitivo concreto y defendible?
19. ¿El posicionamiento deriva de las evidencias?

### Economía documental

20. ¿Cada carencia se desarrolla una sola vez?
21. ¿Cada evidencia evita repetición extensa?
22. ¿Hecho, inferencia, estrategia y límite son distinguibles?
23. ¿El documento evita reproducir innecesariamente el razonamiento interno?

### Preparación posterior

24. ¿Está claro qué debe dominar el CV?
25. ¿Está claro qué debe quedar en segundo plano?
26. ¿Está claro qué no puede afirmarse?
27. ¿El brief es directamente utilizable?
28. ¿La decisión está justificada?

---

## 11. Control local del template

Además del control anterior, la ejecución debe superar el checklist incluido en `TEMPLATE_ANALISIS_OFERTA_v2.md`.

Ese checklist funciona como defensa operativa inmediata.

No sustituye al control de calidad del playbook.

Si ambos controles detectan criterios incompatibles, debe revisarse la alineación entre playbook y template antes de producir nuevos artefactos.

---

## 12. Regla de cierre

El análisis está terminado cuando permite responder con evidencia a cinco preguntas:

1. **¿Qué dice realmente la oferta?**
2. **¿Qué problema parece intentar resolver la contratación?**
3. **¿Qué puede demostrar realmente el candidato frente a ese problema?**
4. **¿Qué no puede demostrar y qué límites deben mantenerse?**
5. **¿Existe una estrategia suficientemente defendible para continuar?**

Si alguna respuesta relevante permanece ambigua por falta de datos:

* registrar la duda;
* decidir si bloquea o no la continuación;
* no resolverla mediante invención.

Solo entonces puede cerrarse `analisis-oferta.md`.
