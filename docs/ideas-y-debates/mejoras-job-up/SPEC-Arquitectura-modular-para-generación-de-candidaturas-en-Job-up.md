---
id: spec-arquitectura-generacion-candidaturas-job-up
titulo: SPEC — Arquitectura modular para generación de candidaturas en Job-up
estado: borrador_operativo
fecha: 2026-08-02
host: carrera-ai
rama: job-up
contexto_pcs: sesion-20260801-2040-job-up
---
# SPEC — Arquitectura modular para generación de candidaturas en Job-up

## 1. Propósito

Este documento fija el enfoque actual para rediseñar la generación de candidaturas dentro de `job-up`.

Su objetivo principal es evitar pérdida de contexto, decisiones y criterios ya debatidos en sesiones anteriores de ChatGPT, especialmente en relación con:

* la separación entre análisis, estrategia, redacción y composición documental;
* la generación de candidaturas por oferta;
* la futura generación de presentaciones espontáneas o candidaturas sin oferta desde la web de una empresa;
* el papel futuro de `datos-generacion.json` como frontera entre contenido redactado y composición técnica;
* la función de una skill directora de orquesta que coordine fases especializadas;
* la regla de corrección entre contenido y maquetación;
* el orden correcto de maduración de los playbooks y artefactos.

Este SPEC debe leerse al iniciar futuras sesiones de trabajo sobre la mejora del flujo de candidatura de `job-up`.

---

## 2. Contexto

`job-up` es una rama operativa dentro de `carrera-ai` dedicada a la búsqueda de empleo y a la preparación de candidaturas revisables.

El flujo anterior tendía a mezclar en una misma ejecución:

* análisis de oferta;
* decisión estratégica;
* adaptación del CV;
* redacción de CV;
* redacción de carta;
* generación documental;
* validación posterior.

La nueva arquitectura separa esas responsabilidades en fases gobernadas por playbooks, templates y artefactos intermedios.

La decisión central es que `job-up` no debe depender de una única skill monolítica que “hace una candidatura completa”, sino de una skill directora que coordina procesos especializados.

---

## 3. Principio arquitectónico central

La generación de una candidatura se divide en dos mundos claramente separados:

```text
Mundo IA / razonamiento / estrategia / redacción
→ produce decisiones, guiones y contenido estructurado

Mundo técnico / composición determinista
→ proyecta ese contenido a documentos finales
```

La frontera futura entre ambos mundos será:

```text
datos-generacion.json
```

Regla principal de la arquitectura final:

> Para corregir contenido, se modifica `datos-generacion.json` o la fase que lo produce.
> Para corregir maquetación, se modifica el template visual o `generar_candidatura.py`.

Esta regla debe usarse como criterio de diagnóstico ante cualquier fallo, pero no implica que `datos-generacion.json` sea el siguiente documento a diseñar. Antes deben estar suficientemente cerradas y probadas las fases que lo alimentan.

---

## 4. Dos puertas de entrada

La arquitectura debe admitir dos formas de iniciar una candidatura.

---

### 4.1 Candidatura por oferta

Parte de una oferta concreta publicada en una fuente externa: InfoJobs, LinkedIn, Indeed, web corporativa, PDF, texto copiado u otra fuente equivalente.

Flujo inicial:

```text
oferta
→ PLAYBOOK_ANALISIS_OFERTA
→ analisis-oferta.md
```

`analisis-oferta.md` es una capa de decisión, trazabilidad y gobierno factual.

Debe determinar:

* qué dice realmente la oferta;
* qué empresa publica la oferta;
* qué empresa contrata realmente, si es identificable;
* qué problema empresarial parece existir detrás del puesto;
* qué requisitos son críticos, compensables o deseables;
* qué palabras clave pueden utilizarse de forma segura;
* qué evidencias de la trayectoria profesional son relevantes;
* qué carencias existen;
* qué riesgos de descarte hay;
* qué argumento competitivo es defendible;
* si procede continuar con la candidatura.

No debe redactar:

* CV final;
* carta de presentación;
* bloques definitivos de experiencia;
* titulares finales;
* respuestas comerciales listas para enviar.

---

### 4.2 Presentación sin oferta en web de empresa

Parte de una empresa objetivo, no de una oferta concreta.

Flujo previsto:

```text
empresa objetivo
→ futuro PLAYBOOK_ANALISIS_EMPRESA_OBJETIVO
→ artefacto equivalente al analisis-oferta.md
```

Este flujo debe servir para candidaturas espontáneas o presentaciones directas a empresas donde no existe oferta abierta.

La diferencia principal es que no hay requisitos explícitos de una oferta. Por tanto, el análisis debe inferir oportunidades desde:

* actividad de la empresa;
* áreas funcionales;
* señales de crecimiento, digitalización, operaciones o necesidad organizativa;
* posibles problemas empresariales donde la trayectoria del candidato pueda aportar valor;
* ajuste razonable entre empresa y perfil;
* límites de lo que no puede afirmarse.

El futuro artefacto debe ser equivalente a `analisis-oferta.md` en función, pero adaptado a ausencia de oferta.

Nombre provisional:

```text
analisis-empresa-objetivo.md
```

o equivalente a decidir.

---

## 5. Ficha común de candidatura

Después del análisis inicial, ambas puertas de entrada convergen en:

```text
PLAYBOOK_CANDIDATURA
→ candidatura.md
```

`candidatura.md` es la ficha viva de ciclo de vida de una candidatura.

Su función no es volver a analizar ni redactar, sino gobernar la candidatura.

Debe registrar:

* identificador de candidatura;
* tipo de origen;
* empresa;
* puesto o ámbito objetivo;
* artefacto de análisis de origen;
* decisión estratégica heredada;
* estado operativo;
* presentada: `true` o `false`;
* posicionamiento;
* evidencias prioritarias;
* afirmaciones excluidas;
* advertencias;
* datos pendientes;
* bloqueos;
* artefactos existentes y pendientes;
* próxima fase prevista.

Debe distinguir siempre:

```text
decisión estratégica
≠
estado operativo
```

Ejemplo válido:

```yaml
decision_estrategica: preparar_con_advertencias
estado: en_preparacion
```

La decisión estratégica responde:

> ¿Conviene construir esta candidatura y bajo qué condiciones?

El estado operativo responde:

> ¿En qué punto real está la candidatura?

---

## 6. Modelo común para ambos orígenes

`candidatura.md` debe ser agnóstico al origen.

Valores iniciales previstos:

```yaml
tipo_origen: oferta
```

```yaml
tipo_origen: empresa_objetivo
```

Esto permite que el flujo posterior sea común:

```text
análisis de oportunidad
→ candidatura.md
→ guion-adaptacion-cv.md
→ datos-generacion.json
→ documentos finales
→ veredicto
```

La candidatura por oferta y la presentación espontánea se diferencian en la fase de análisis, pero comparten las fases posteriores.

---

## 7. Estado actual de maduración

La arquitectura final está orientada, pero no todas las fases están cerradas ni probadas.

Estado actual:

| Fase                          | Artefacto                                                           | Estado                                                           |
| ----------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Análisis por oferta           | `PLAYBOOK_ANALISIS_OFERTA` → `analisis-oferta.md`                   | Bastante avanzado y probado parcialmente                         |
| Análisis por empresa objetivo | futuro `PLAYBOOK_ANALISIS_EMPRESA_OBJETIVO` → artefacto equivalente | Pendiente                                                        |
| Ficha de candidatura          | `PLAYBOOK_CANDIDATURA` → `candidatura.md`                           | Diseñado, pendiente de prueba/cierre suficiente                  |
| Adaptación estratégica        | `PLAYBOOK_GUION_ADAPTACION_CV` → `guion-adaptacion-cv.md`           | Pendiente                                                        |
| Generación de contenido       | `PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA` → `datos-generacion.json`  | Futuro; no debe abordarse aún como siguiente paso                |
| Composición documental        | `generar_candidatura.py` + templates visuales                       | Futuro/pendiente de adaptar al JSON                              |
| Veredicto                     | playbook específico → `veredicto-final-cv.md`                       | Existe como concepto previo; pendiente de adaptar al nuevo flujo |
| Preparación de entrevista     | playbook específico → informe correspondiente                       | Posterior y condicional                                          |

La prioridad inmediata está entre la fase 2 y la fase 3:

```text
PLAYBOOK_CANDIDATURA
→ candidatura.md
→ PLAYBOOK_GUION_ADAPTACION_CV
→ guion-adaptacion-cv.md
```

---

## 8. Adaptación estratégica

Después de `candidatura.md`, la siguiente fase es:

```text
PLAYBOOK_GUION_ADAPTACION_CV
→ guion-adaptacion-cv.md
```

Esta fase no debe redactar todavía los textos finales de CV ni carta.

Su función es transformar la decisión estratégica en un plan de adaptación.

Debe definir:

* qué relato profesional conviene construir;
* qué experiencias deben priorizarse;
* qué evidencias deben alimentar el CV;
* qué evidencias deben alimentar la carta;
* qué tono debe usarse;
* qué riesgos deben gestionarse;
* qué carencias deben mantenerse visibles;
* qué afirmaciones están prohibidas;
* qué debe quedar en segundo plano;
* qué datos faltan, si los hay;
* qué límites deben respetar los documentos finales.

`guion-adaptacion-cv.md` funciona como puente entre análisis/ficha y redacción final.

Debe consumir:

```text
analisis de oportunidad
+ candidatura.md
+ datos-core-busqueda.md
```

y producir una instrucción estratégica suficientemente concreta para que, en una fase posterior, `PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA` pueda redactar sin volver a decidir desde cero.

---

## 9. Generación única del contenido de candidatura

La redacción final ocurrirá una sola vez en:

```text
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
→ datos-generacion.json
```

Esta será una fase crítica de la arquitectura, pero no es el siguiente paso inmediato.

Consumirá:

```text
analisis de oportunidad
+ candidatura.md
+ guion-adaptacion-cv.md
+ datos-core-busqueda.md
+ datos privados autorizados
```

Producirá:

```text
datos-generacion.json
```

Este JSON contendrá los textos definitivos que luego se proyectarán a documentos.

Deberá incluir, como mínimo provisional:

* datos identificativos permitidos;
* puesto o ámbito objetivo;
* empresa;
* perfil profesional adaptado;
* titular o bloque equivalente;
* bloques de experiencia seleccionados;
* logros priorizados;
* competencias o capacidades destacadas;
* formación relevante;
* herramientas y tecnologías;
* texto de carta de presentación;
* posibles bloques LaTeX equivalentes si procede;
* advertencias de contenido;
* afirmaciones excluidas;
* metadatos de trazabilidad;
* referencias a artefactos fuente.

La decisión importante es que CV, carta y LaTeX no se redactarán como documentos independientes.

Todos serán proyecciones del mismo contenido estructurado.

Pero esta fase debe diseñarse solo cuando estén suficientemente probadas:

1. `candidatura.md`;
2. `guion-adaptacion-cv.md`;
3. la relación entre análisis, ficha y guion.

---

## 10. Composición documental determinista

La generación física de documentos queda separada de la redacción.

Fase futura:

```text
generar_candidatura.py
```

Consumirá:

```text
datos-generacion.json
+ templates visuales
```

Producirá:

```text
cv.docx
cv.pdf
cv.tex
carta-presentacion.docx
carta-presentacion.pdf
```

Reglas:

* no analiza;
* no interpreta;
* no decide estrategia;
* no redacta;
* no corrige contenido;
* no mejora frases;
* no elimina carencias;
* no inventa información;
* no parchea decisiones del playbook.

Su función será únicamente componer documentos desde contenido ya producido por la fase de generación.

---

## 11. Veredicto del CV

Después de generar los documentos entrará:

```text
playbook específico
→ veredicto-final-cv.md
```

El veredicto evaluará el CV ya generado.

Debe revisar:

* integridad factual;
* privacidad;
* coherencia con la oferta o empresa objetivo;
* coherencia con `candidatura.md`;
* coherencia con `guion-adaptacion-cv.md`;
* calidad del primer escaneo;
* fuerza del posicionamiento;
* cobertura ATS cuando proceda;
* calidad narrativa;
* límites y afirmaciones prohibidas;
* correspondencia entre CV y carta, si procede.

Regla obligatoria de la arquitectura final:

> Si el veredicto detecta un fallo de contenido, no se parchea directamente el DOCX.
> La corrección vuelve a `PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA` y se regenera `datos-generacion.json`.

Si detecta fallo de maquetación:

> La corrección se realiza en el template visual o en `generar_candidatura.py`.

---

## 12. Preparación de entrevista

La preparación de entrevista es una fase posterior y condicional.

Solo procede cuando:

* la candidatura está preparada;
* la candidatura ha sido enviada;
* existe una entrevista;
* o se decide preparar argumentario preventivo.

Flujo:

```text
playbook específico
→ informe de preparación de entrevista
```

No forma parte del núcleo obligatorio de generación documental.

---

## 13. Flujo completo final previsto

### 13.1 Por oferta

```text
oferta
→ PLAYBOOK_ANALISIS_OFERTA
→ analisis-oferta.md
→ PLAYBOOK_CANDIDATURA
→ candidatura.md
→ PLAYBOOK_GUION_ADAPTACION_CV
→ guion-adaptacion-cv.md
→ PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
→ datos-generacion.json
→ generar_candidatura.py
→ cv.docx / cv.pdf / cv.tex / carta-presentacion.docx / carta-presentacion.pdf
→ veredicto-final-cv.md
→ preparación de entrevista, si procede
```

---

### 13.2 Por empresa objetivo / presentación espontánea

```text
empresa objetivo
→ futuro PLAYBOOK_ANALISIS_EMPRESA_OBJETIVO
→ analisis-empresa-objetivo.md
→ PLAYBOOK_CANDIDATURA
→ candidatura.md
→ PLAYBOOK_GUION_ADAPTACION_CV
→ guion-adaptacion-cv.md
→ PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
→ datos-generacion.json
→ generar_candidatura.py
→ cv.docx / cv.pdf / cv.tex / carta-presentacion.docx / carta-presentacion.pdf
→ veredicto-final-cv.md
→ preparación de entrevista, si procede
```

---

## 14. Flujo inmediato de trabajo

El flujo completo final no debe confundirse con el siguiente paso real de trabajo.

El orden correcto de maduración es:

```text
1. Validar suficientemente PLAYBOOK_CANDIDATURA y TEMPLATE_CANDIDATURA_v2
2. Probar candidatura.md con al menos un caso real completo
3. Diseñar PLAYBOOK_GUION_ADAPTACION_CV
4. Diseñar TEMPLATE_GUION_ADAPTACION_CV, si procede
5. Probar guion-adaptacion-cv.md con una candidatura real
6. Solo después diseñar PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
7. Definir datos-generacion.json y su schema/template
8. Adaptar generar_candidatura.py a ese contrato
9. Adaptar el veredicto al nuevo flujo
```

Motivo:

`PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA` consume necesariamente:

```text
analisis de oportunidad
+ candidatura.md
+ guion-adaptacion-cv.md
+ datos-core-busqueda.md
+ datos privados autorizados
```

Por tanto, no puede diseñarse con suficiente precisión si `candidatura.md` no está probado y si `guion-adaptacion-cv.md` aún no existe.

---

## 15. Skill directora de orquesta

La skill principal de `job-up` debe actuar como directora de orquesta.

No debe absorber toda la lógica en un único prompt.

Responsabilidades futuras de la skill directora:

1. identificar el tipo de entrada;
2. determinar si es candidatura por oferta o empresa objetivo;
3. invocar el playbook de análisis correspondiente;
4. crear o actualizar `candidatura.md`;
5. invocar el guion de adaptación;
6. invocar la generación de contenido;
7. validar la existencia y estructura de `datos-generacion.json`;
8. ejecutar o preparar la composición documental;
9. invocar el veredicto;
10. detenerse para aprobación humana;
11. registrar estado e incidencias;
12. no enviar, contactar ni usar datos privados sin autorización.

La skill directora coordina, pero no debe mezclar responsabilidades.

En el estado actual, todavía no debe implementarse plenamente esta skill directora final, porque faltan fases intermedias por cerrar.

---

## 16. Principios de continuidad para futuras sesiones

Para evitar pérdida de contexto en futuras sesiones de ChatGPT, toda sesión sobre esta línea debe empezar reconstruyendo este estado mínimo:

1. Estamos en `carrera-ai`.
2. La rama operativa es `job-up`.
3. La sesión PCS abierta relacionada es `sesion-20260801-2040-job-up`, salvo que el estado vivo indique otra.
4. El objetivo del bloque es mejorar la arquitectura de generación de candidaturas.
5. La arquitectura vigente es modular.
6. Hay dos puertas de entrada: oferta y empresa objetivo.
7. Tras el análisis, ambas vías convergen en `candidatura.md`.
8. `candidatura.md` está diseñada, pero debe probarse/cerrarse suficientemente.
9. `PLAYBOOK_GUION_ADAPTACION_CV` todavía está pendiente.
10. `datos-generacion.json` es una pieza futura, no el siguiente paso inmediato.
11. La composición documental será determinista.
12. CV, carta y LaTeX serán proyecciones del mismo contenido cuando exista el JSON.
13. Los errores de contenido se corregirán en la fase de generación de contenido o en el JSON.
14. Los errores de maquetación se corregirán en templates o script.
15. No se debe volver a diseñar desde cero lo ya decidido sin una razón explícita.

---

## 17. Decisiones consolidadas

### DEC-01 — Separación entre análisis y redacción

`analisis-oferta.md` y el futuro análisis de empresa objetivo no redactan documentos finales.

---

### DEC-02 — `candidatura.md` como ficha viva

`candidatura.md` gobierna la candidatura, pero no sustituye análisis, guion, CV, carta ni veredicto.

---

### DEC-03 — Dos puertas de entrada

El flujo admite:

* candidatura por oferta;
* candidatura o presentación espontánea por empresa objetivo.

---

### DEC-04 — Convergencia tras análisis

Después del análisis inicial, ambas vías usan la misma ficha y el mismo flujo posterior.

---

### DEC-05 — Adaptación estratégica antes de redacción final

Antes de redactar contenido final debe existir:

```text
PLAYBOOK_GUION_ADAPTACION_CV
→ guion-adaptacion-cv.md
```

El guion traduce análisis y ficha en instrucciones estratégicas de adaptación.

---

### DEC-06 — Redacción única futura

CV, carta y LaTeX no deben redactarse por separado.

La redacción ocurrirá en:

```text
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
→ datos-generacion.json
```

Pero esta fase queda para después de validar `candidatura.md` y diseñar/probar `guion-adaptacion-cv.md`.

---

### DEC-07 — Composición determinista futura

`generar_candidatura.py` solo compondrá documentos.

No analizará, no redactará y no corregirá contenido.

---

### DEC-08 — Corrección por capa

Contenido:

```text
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA / datos-generacion.json
```

Maquetación:

```text
templates visuales / generar_candidatura.py
```

Esta regla será plenamente operativa cuando exista el contrato de `datos-generacion.json`.

---

### DEC-09 — Veredicto sin parcheo directo

El veredicto no debe corregir directamente el DOCX.

Si detecta fallos de contenido, devolverá la corrección a la fase de generación de contenido.

---

## 18. Artefactos actuales conocidos

Ya existen o han sido trabajados:

```text
PLAYBOOK_ANALISIS_OFERTA.md
TEMPLATE_ANALISIS_OFERTA_v2.md
analisis-oferta-cand-2026-019.md
PLAYBOOK_CANDIDATURA.md
TEMPLATE_CANDIDATURA_v2.md
candidatura_CAND-2026-019_v2.md
```

Pendientes o futuros:

```text
PLAYBOOK_ANALISIS_EMPRESA_OBJETIVO.md
TEMPLATE_ANALISIS_EMPRESA_OBJETIVO.md
PLAYBOOK_GUION_ADAPTACION_CV.md ajustado a esta arquitectura
TEMPLATE_GUION_ADAPTACION_CV.md, si procede
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA.md
schema de datos-generacion.json
template o ejemplo de datos-generacion.json
adaptación de generar_candidatura.py
playbook/veredicto ajustado a corrección por JSON
playbook preparación entrevista
```

---

## 19. Próximo trabajo recomendado

El siguiente trabajo no debe ser todavía diseñar `PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA.md`.

Aunque `datos-generacion.json` será una pieza central de la arquitectura final, todavía no debe abordarse como siguiente fase porque antes deben consolidarse las piezas que lo alimentan.

La prioridad inmediata es:

```text
1. Revisar PLAYBOOK_CANDIDATURA
2. Revisar TEMPLATE_CANDIDATURA_v2
3. Probar candidatura.md con al menos un caso real completo
4. Confirmar si candidatura.md queda cerrada o necesita ajuste
5. Diseñar PLAYBOOK_GUION_ADAPTACION_CV
6. Diseñar TEMPLATE_GUION_ADAPTACION_CV, si procede
7. Probar guion-adaptacion-cv.md con una candidatura real
```

Solo cuando esas dos piezas estén consolidadas tendrá sentido definir el contrato de generación final:

```text
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
→ datos-generacion.json
```

---

## 20. Guion mínimo para próximas sesiones

Cuando se retome esta línea, usar este orden:

### Paso 1 — Confirmar estado

* ¿Seguimos en `carrera-ai/job-up`?
* ¿La sesión PCS abierta sigue siendo `sesion-20260801-2040-job-up`?
* ¿El objetivo sigue siendo mejorar la generación modular de candidaturas?

### Paso 2 — Determinar fase de trabajo

Elegir solo una:

* análisis por oferta;
* análisis por empresa objetivo;
* `candidatura.md`;
* guion de adaptación;
* generación de contenido;
* JSON/schema;
* composición documental;
* veredicto;
* preparación entrevista;
* skill directora.

### Paso 3 — No mezclar capas

Antes de cambiar algo, clasificarlo:

```text
¿Es análisis?
¿Es estrategia?
¿Es redacción?
¿Es estructura JSON?
¿Es composición técnica?
¿Es validación?
¿Es estado PCS?
```

### Paso 4 — Respetar el orden de maduración

No avanzar a una fase si sus entradas todavía no existen o no están suficientemente probadas.

En particular:

```text
No diseñar PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
sin haber probado antes candidatura.md
y sin tener PLAYBOOK_GUION_ADAPTACION_CV.
```

### Paso 5 — Registrar decisión

Toda decisión relevante debe quedar en una sección explícita de “decisiones consolidadas” o en una sesión PCS.

### Paso 6 — Registrar siguiente gesto

Cada sesión debe terminar indicando:

* qué quedó decidido;
* qué artefactos quedan afectados;
* qué falta;
* cuál es el siguiente paso recomendado.

---

## 21. Riesgos a evitar

### Riesgo 1 — Volver al monolito

No reconstruir una skill que haga todo en un único prompt.

---

### Riesgo 2 — Redactar varias veces

No generar CV, carta y LaTeX como redacciones independientes.

---

### Riesgo 3 — Saltar fases

No pasar a `PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA` antes de cerrar suficientemente `candidatura.md` y diseñar/probar `guion-adaptacion-cv.md`.

---

### Riesgo 4 — Parchear DOCX

No corregir contenido directamente en documentos finales.

---

### Riesgo 5 — Confundir empresa publicadora y contratante

Especialmente en ofertas intermediadas.

---

### Riesgo 6 — Convertir formación en experiencia

La formación o actualización no debe presentarse como experiencia profesional si no está acreditada.

---

### Riesgo 7 — Convertir automatización en IA

Automatización, algoritmos, programación o integración no equivalen automáticamente a experiencia profesional en IA.

---

### Riesgo 8 — Perder decisiones entre sesiones

Toda sesión futura debe recuperar este SPEC antes de rediseñar el flujo.

---

## 22. Resumen ejecutivo

La nueva generación de candidaturas en `job-up` se basa en una arquitectura modular:

```text
análisis de oportunidad
→ candidatura.md
→ guion-adaptacion-cv.md
→ datos-generacion.json
→ generar_candidatura.py
→ documentos finales
→ veredicto
→ entrevista si procede
```

La candidatura puede nacer de una oferta o de una empresa objetivo sin oferta.

La arquitectura final ya está orientada, pero el trabajo no debe avanzar directamente hacia `datos-generacion.json`.

El punto actual de trabajo está entre la fase 2 y la fase 3:

```text
PLAYBOOK_CANDIDATURA
→ candidatura.md
→ PLAYBOOK_GUION_ADAPTACION_CV
→ guion-adaptacion-cv.md
```

Antes de diseñar la generación final de contenido, deben quedar suficientemente probados:

1. que `candidatura.md` gobierna bien el ciclo de vida sin repetir el análisis;
2. que separa decisión estratégica, estado operativo, advertencias, bloqueos y artefactos;
3. que `guion-adaptacion-cv.md` traduce correctamente la estrategia en instrucciones de adaptación;
4. que el futuro `datos-generacion.json` recibirá entradas estables y no decisiones todavía inmaduras.

La regla maestra se mantiene:

> Contenido se corrige en el JSON o en la fase que lo produce.
> Maquetación se corrige en templates o script.

Pero esa regla pertenece a la arquitectura final. El siguiente trabajo inmediato es cerrar y probar las fases previas.
