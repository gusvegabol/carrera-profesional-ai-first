
# PLAYBOOK_CANDIDATURA

## 1. Propósito

Este playbook define cómo crear y mantener `candidatura.md`.

`candidatura.md` es la **ficha operativa viva de una candidatura**.

Su función es:

* identificar la candidatura;
* registrar de dónde procede;
* conservar la decisión estratégica adoptada;
* fijar el posicionamiento que deben respetar las fases posteriores;
* conservar las evidencias prioritarias;
* conservar límites y afirmaciones excluidas;
* distinguir advertencias, datos pendientes y bloqueos;
* registrar el estado de la candidatura;
* mantener el índice y estado de sus artefactos;
* servir como punto de control entre las distintas fases del flujo.

No es función de `candidatura.md`:

* volver a analizar la oferta;
* volver a investigar la empresa;
* decidir de nuevo el encaje;
* sustituir `analisis-oferta.md`;
* sustituir el futuro análisis de empresa objetivo;
* redactar el CV;
* redactar la carta;
* generar el guion de adaptación;
* ejecutar el veredicto final.

La fase posterior a composición se ejecuta así:

```text
cv.pdf / cv.docx / cv.tex
→ revisión humana del PDF
→ revision-humana-cv.md
→ PLAYBOOK_VEREDICTO_FINAL_CV
→ veredicto-final-cv.md
→ GATE-VEREDICTO-CV
```

El estado operativo solo puede avanzar después de la revisión humana y del
veredicto. El gate tiene decisión humana separada; Job-up no envía candidaturas
automáticamente.

---

## 2. Posición dentro de la arquitectura

`candidatura.md` se crea después de que exista un análisis de origen suficientemente completo.

Existen al menos dos posibles orígenes:

### 2.1 Candidatura por oferta

```text
oferta
→ PLAYBOOK_ANALISIS_OFERTA
→ analisis-oferta.md
→ PLAYBOOK_CANDIDATURA
→ candidatura.md
```

### 2.2 Candidatura a empresa objetivo

```text
empresa objetivo
→ futuro PLAYBOOK_ANALISIS_EMPRESA_OBJETIVO
→ artefacto de análisis
→ PLAYBOOK_CANDIDATURA
→ candidatura.md
```

A partir de `candidatura.md`, ambos caminos deben poder compartir las mismas fases posteriores.

---

## 3. Principio de neutralidad del origen

`candidatura.md` debe ser agnóstico al mecanismo que generó la oportunidad.

Debe registrar:

* `tipo_origen`;
* artefacto de origen;
* empresa;
* puesto o ámbito objetivo;
* decisión estratégica.

Valores iniciales previstos para `tipo_origen`:

* `oferta`;
* `empresa_objetivo`.

La arquitectura debe permitir añadir en el futuro otros tipos sin rediseñar `candidatura.md`.

---

## 4. Fuentes de autoridad

### 4.1 Artefacto de análisis de origen

Es la fuente de autoridad sobre:

* problema u oportunidad detectada;
* encaje;
* requisitos;
* riesgos;
* argumento competitivo;
* posicionamiento;
* evidencias prioritarias;
* afirmaciones excluidas;
* decisión estratégica.

`candidatura.md` consume esos resultados.

No debe reinterpretarlos salvo revisión explícita del análisis.

### 4.2 Datos core

`datos-core-busqueda.md` sigue siendo la fuente factual única de la trayectoria profesional.

El contenido heredado del análisis mantiene su trazabilidad hacia los datos core.

### 4.3 Artefactos posteriores

Guion, CV, carta y veredicto pueden actualizar el **estado operativo** de la candidatura, pero no alterar silenciosamente la estrategia de origen.

Si una fase posterior demuestra que la estrategia necesita cambiar:

1. registrar la incidencia;
2. revisar el artefacto que originó la decisión;
3. propagar después el cambio a `candidatura.md`.

`revision-humana-cv.md` acredita que la persona responsable revisó el PDF
concreto y registra su huella SHA-256. `veredicto-final-cv.md` diagnostica
integridad, fidelidad y competitividad aplicando los dos roles definidos por
`PLAYBOOK_VEREDICTO_FINAL_CV`. Ninguno de los dos artefactos modifica el CV ni
sustituye la decisión humana de `GATE-VEREDICTO-CV` ni abre el gate de candidatura completa.

---

## 5. Diferencia entre decisión y estado

Son dimensiones distintas y no deben confundirse.

### 5.1 Decisión estratégica

Procede del análisis.

Valores previstos:

* `preparar_candidatura`;
* `preparar_con_advertencias`;
* `pedir_datos_adicionales_antes_de_redactar`;
* `no_recomendada`.

Responde:

> ¿Conviene construir esta candidatura y bajo qué condiciones?

### 5.2 Estado operativo

Describe dónde se encuentra la candidatura en su ciclo de vida.

Valores previstos:

* `en_preparacion`;
* `detenida`;
* `pendiente_de_aprobacion`;
* `aprobada`;
* `enviada`;
* `rechazada`;
* `duplicada`;
* `fallida`.

Responde:

> ¿En qué punto operativo está actualmente?

Una candidatura puede, por ejemplo, tener:

```yaml
decision_estrategica: preparar_con_advertencias
estado: en_preparacion
```

No existe contradicción.

---

## 6. Creación inicial

Crear `candidatura.md` cuando el artefacto de análisis de origen produzca una decisión distinta de:

`no_recomendada`

Cuando la decisión sea:

### `preparar_candidatura`

Crear la ficha y continuar.

### `preparar_con_advertencias`

Crear la ficha, registrar advertencias y continuar.

En toda creación o reanudación de una candidatura debe preguntarse antes de redactar el CV:

> ¿Qué datos privados autorizas a incorporar en este CV: nombre, apellido 1, apellido 2, email, teléfono, LinkedIn,
> ubicación y fotografía?

Registrar cada respuesta como `incluir`, `omitir` o `pendiente` en `autorizacion_datos_cv`. La persona responsable de
la candidatura tiene la autoridad final. Un campo `pendiente` bloquea la generación del contenido y del CV, pero no
impide completar el análisis de la oferta.

### `pedir_datos_adicionales_antes_de_redactar`

Crear la ficha con:

```yaml
estado: detenida
```

y registrar los datos que bloquean la continuación.

### `no_recomendada`

No iniciar producción documental normal.

El sistema puede registrar la oportunidad en el seguimiento correspondiente, pero no debe crear una candidatura operativa completa salvo que exista una razón explícita de trazabilidad.

---

## 7. Identificación y trazabilidad

La ficha debe registrar como mínimo:

* identificador;
* tipo de origen;
* empresa;
* puesto o ámbito objetivo;
* fecha de creación;
* sesión relacionada, cuando exista;
* artefacto de análisis de origen;
* decisión estratégica;
* estado operativo;
* presentada: `true` o `false`.

`presentada` nunca se infiere del estado.

---

## 8. Síntesis estratégica heredada

`candidatura.md` no debe copiar entero el análisis.

Debe conservar únicamente la información necesaria para gobernar las fases posteriores.

### 8.1 Ángulo de candidatura

Síntesis compacta del argumento competitivo.

### 8.2 Posicionamiento

Registrar:

* principal;
* secundario, si aporta;
* enfoques a evitar.

### 8.3 Evidencias prioritarias

Registrar los identificadores factuales que deben alimentar las siguientes fases.

No existe un número fijo.

Usar únicamente las evidencias necesarias para sostener la estrategia.

### 8.4 Afirmaciones excluidas

Conservar las afirmaciones que las fases posteriores no deben introducir.

No limitarse a requisitos tecnológicos.

Puede incluir:

* responsabilidades;
* titulaciones;
* métricas;
* sectores;
* herramientas;
* experiencia;
* niveles de dominio;
* atribuciones;
* cualquier formulación incompatible con la evidencia.

---

## 9. Advertencias, datos pendientes y bloqueos

Deben ser tres categorías separadas.

### 9.1 Advertencia

Condición que debe vigilarse pero no impide continuar.

Ejemplos:

* riesgo de sobrecualificación;
* tecnología no acreditada;
* banda salarial parcialmente compatible;
* sector no coincidente.

### 9.2 Dato pendiente

Información que sería útil confirmar, pero cuya ausencia no impide necesariamente producir una candidatura factual.

Debe registrarse con su estado:

* pendiente;
* confirmado;
* descartado;
* no disponible.

### 9.3 Bloqueo

Condición que impide avanzar con seguridad a la siguiente fase.

Un bloqueo debe contener:

* descripción;
* fase afectada;
* resolución necesaria.

Si existe al menos un bloqueo activo, el estado debe ser:

`detenida`

Un bloqueo no se resuelve mediante inferencia.

---

## 10. Artefactos

`candidatura.md` debe funcionar como índice vivo de los artefactos operativos.

No debe asumir que todos existen desde el inicio.

Cada artefacto debe registrar al menos:

* nombre;
* ruta/enlace;
* estado.

Estados recomendados:

* `no_iniciado`;
* `en_preparacion`;
* `completado`;
* `requiere_revision`;
* `bloqueado`;
* `no_aplica`.

Artefactos previstos inicialmente:

* análisis de origen;
* guion de adaptación del CV;
* CV DOCX;
* CV PDF;
* CV TEX;
* carta DOCX;
* carta PDF;
* veredicto final del CV;
* paquete de presentación;
* informe de empresa / entrevista cuando corresponda.

La incorporación futura de nuevos artefactos no debe requerir modificar el modelo conceptual.

---

## 11. Actualizaciones por fase

### 11.1 Después del análisis

Crear la ficha con:

* origen;
* decisión;
* estrategia;
* evidencias;
* límites;
* advertencias;
* bloqueos.

### 11.2 Después del guion

Actualizar:

* estado del artefacto;
* enlace;
* cualquier incidencia que obligue a revisar el análisis.

No duplicar el contenido completo del guion.

### 11.3 Después de generar los artefactos documentales

Registrar:

* existencia;
* rutas;
* estados;
* incidencias.

No copiar el contenido de CV, carta, email o formulario a `candidatura.md`.

### 11.4 Después del veredicto del CV

Registrar el enlace, el resultado y la decisión del gate `GATE-VEREDICTO-CV`.
La aprobación de este gate valida únicamente el CV. No convierte la candidatura
en `aprobada` ni autoriza la presentación.

Mientras no exista un paquete completo, mantener:

```yaml
estado: en_preparacion
presentada: false
```

### 11.5 Preparación del paquete de presentación

Crear `paquete-presentacion.md` y registrar el canal u origen conocido. El
paquete mínimo siempre debe contener el CV y la carta de presentación. La carta
se produce mediante su propio playbook, guion, revisión y decisión, separados
del flujo exclusivo del CV.

Los formularios, preguntas, credenciales y cargas específicas de Indeed,
LinkedIn, Lidl, Mercadona u otros portales quedan bajo responsabilidad de la
persona responsable. Job-up no inicia sesión ni presenta candidaturas en
portales externos como parte del flujo general.

### 11.6 Después del gate de candidatura completa

Solo cuando el CV y la carta estén presentes y revisados puede la persona
responsable decidir `GATE-CANDIDATURA-PRESENTACION`. Los artefactos adicionales
del canal se registran si se conocen, pero no son una condición general para
generar el paquete mínimo.

Si se aprueba:

```yaml
estado: aprobada
presentada: false
```

Esta aprobación no registra un envío. La presentación siempre la realiza la
persona responsable y después debe aportar la evidencia de la acción real.

### 11.7 Después del envío

Solo tras confirmación real del envío:

```yaml
estado: enviada
presentada: true
```

---

## 12. Relación con el veredicto

La decisión del veredicto no sustituye la decisión estratégica de la candidatura.

Son preguntas diferentes:

**Decisión estratégica**

> ¿Debemos competir?

**Veredicto**

> ¿Los documentos construidos están suficientemente bien para revisión/aprobación?

Registrar ambas.

---

## 13. Economía documental

`candidatura.md` debe ser compacto.

No debe repetir:

* extracción factual de la oferta;
* jerarquía completa de requisitos;
* matriz de encaje;
* análisis de riesgos completo;
* razonamiento completo del posicionamiento;
* contenido del guion;
* contenido del CV;
* contenido de la carta;
* contenido completo del veredicto.

Debe enlazar a esos artefactos.

Principio:

> `candidatura.md` gobierna; no replica.

---

## 14. Contrato del artefacto

La estructura concreta se materializa mediante `TEMPLATE_CANDIDATURA_v2.md`.

Debe contener:

```text
frontmatter

1. Identificación y origen
2. Decisión y estrategia heredada
3. Evidencias y límites
4. Advertencias, datos pendientes y bloqueos
5. Estado operativo
6. Artefactos de candidatura
7. Control de coherencia
```

---

## 15. Criterios de calidad

Antes de cerrar o actualizar una ficha comprobar:

### Trazabilidad

1. ¿Se conoce el artefacto de origen?
2. ¿La decisión procede del análisis?
3. ¿Las evidencias mantienen identificadores?
4. ¿Las afirmaciones excluidas proceden de límites documentados?

### Separación de responsabilidades

5. ¿La ficha evita volver a analizar la oportunidad?
6. ¿No reproduce el guion?
7. ¿No reproduce CV o carta?
8. ¿No sustituye el veredicto?

### Estado

9. ¿Decisión estratégica y estado operativo están separados?
10. ¿`presentada` refleja un hecho real?
11. ¿Los bloqueos activos implican `detenida`?
12. ¿`pendiente_de_aprobacion` solo se usa cuando los documentos necesarios están preparados?

### Modularidad

13. ¿La ficha funciona igual para `oferta` y `empresa_objetivo`?
14. ¿Los artefactos pueden aparecer progresivamente?
15. ¿La ausencia de un artefacto futuro no rompe la ficha?

### Economía

16. ¿Solo se conserva información necesaria para gobernar fases posteriores?
17. ¿Se evita duplicar contenido ya disponible en otros artefactos?

---

## 16. Regla de cierre

`candidatura.md` es válida cuando permite responder inmediatamente:

1. ¿De dónde nace esta candidatura?
2. ¿Por qué hemos decidido competir?
3. ¿Con qué posicionamiento?
4. ¿Qué evidencias podemos utilizar?
5. ¿Qué no debemos afirmar?
6. ¿Qué advertencias o bloqueos existen?
7. ¿Qué artefactos existen y en qué estado?
8. ¿Cuál es el estado operativo actual?

Si esas respuestas requieren reconstruir el análisis original, la ficha está incompleta.

Si la ficha empieza a reproducir el análisis completo, está sobredimensionada.
