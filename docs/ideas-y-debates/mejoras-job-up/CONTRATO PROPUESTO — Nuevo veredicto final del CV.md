# CONTRATO PROPUESTO — Nuevo veredicto final del CV

**Estado:** propuesta para aprobación humana  
**Futura implementación:** `PLAYBOOK_VEREDICTO_FINAL_CV`  
**Salida prevista:** `veredicto-final-cv.md`  
**Alcance:** exclusivo del CV final generado  
**Casos de control iniciales:** `CAND-2026-020` y `CAND-2026-019`

---

# 1. Pregunta que debe responder

El nuevo veredicto responde exclusivamente a:

> **¿El CV final generado para esta candidatura es factual, fiel al flujo, profesionalmente competitivo y suficientemente sólido para autorizar su avance hacia presentación?**

No responde a:

- si el candidato debería aceptar el puesto;
- si la empresa es conveniente;
- si se garantiza entrevista;
- si debe enviarse automáticamente;
- si la carta es adecuada;
- si deben inventarse argumentos para compensar carencias;
- si una candidatura con mal encaje puede convertirse en buena mediante redacción.

El veredicto evalúa simultáneamente:

```text
integridad
+
fidelidad al flujo
+
calidad recruiter
+
calidad del artefacto final
+
competitividad real
```

---

# 2. Posición en el flujo

```text
datos-generacion.json
        ↓
GATE-CONTENIDO-CV-COMPOSICION
        ↓
composición determinista
        ↓
cv.docx / cv.pdf / cv.tex
        ↓
REVISIÓN Y APROBACIÓN HUMANA DEL CV GENERADO
        ↓
PLAYBOOK_VEREDICTO_FINAL_CV
        ↓
veredicto-final-cv.md
        ↓
GATE-VEREDICTO-CV-PRESENTACION
        ↓
futura presentación / envío
```

La revisión humana posterior a composición continúa siendo una precondición independiente.

El veredicto no la sustituye.

---

# 3. Roles obligatorios

El veredicto debe ejecutarse con dos perspectivas explícitas.

## Rol A — Recruiter senior + coach de carrera

Evalúa el CV como lo haría una persona responsable de selección para esa oportunidad.

Pregunta:

> ¿Qué percibe un recruiter al enfrentarse al documento terminado y qué probabilidad tiene el CV de provocar una lectura favorable o una entrevista dentro de los límites factuales existentes?

Debe evaluar:

- primer escaneo;
- claridad del posicionamiento;
- relevancia;
- evidencia;
- encaje;
- diferenciación;
- seniority;
- sobrecualificación;
- ATS;
- credibilidad;
- narrativa;
- legibilidad;
- competitividad real.

No puede:

- premiar exageraciones;
- convertir transferibilidad en experiencia literal;
- convertir formación en experiencia;
- añadir tecnologías porque aparezcan en la oferta;
- ocultar una carencia material para mejorar la puntuación.

---

## Rol B — Auditor senior de flujo agentic

Evalúa si el CV final es una materialización correcta de las decisiones y contratos anteriores.

Pregunta:

> ¿El resultado final preserva sin desviaciones las decisiones, autorizaciones y límites que llegaron a esta fase?

Debe comprobar:

```text
candidatura
→ guion
→ datos-generacion
→ composición
→ CV final
```

y asignar cualquier defecto a su **capa propietaria**.

No debe arreglar localmente un defecto de otra capa.

---

# 4. Precondiciones

El veredicto no puede iniciarse si falta cualquiera de estas condiciones:

1. Existe `cv.pdf` final.
2. Existe `cv.docx`.
3. Existe `datos-generacion.json` correspondiente.
4. La composición terminó correctamente.
5. `GATE-CONTENIDO-CV-COMPOSICION` estaba aprobado.
6. Existe autorización de datos privados para el CV.
7. El CV generado ha recibido la revisión humana posterior a composición exigida por la arquitectura.
8. La candidatura sigue:
   ```text
   presentada: false
   ```
9. Las fuentes de autoridad necesarias son resolubles.

El PDF es el **artefacto principal de evaluación recruiter y visual**.

El DOCX puede utilizarse para comprobaciones técnicas cuando proceda.

---

# 5. Entradas autorizadas

El veredicto puede consultar:

## Artefacto evaluado

```text
cv.pdf
```

y, si es necesario:

```text
cv.docx
cv.tex
```

## Contenido inmediatamente anterior

```text
datos-generacion.json
```

## Decisión editorial

```text
guion-adaptacion-cv.md
```

## Estrategia

```text
candidatura.md
analisis-oferta.md
```

## Factualidad

Las fuentes factuales autorizadas por el flujo, principalmente:

```text
datos-core-busqueda.md
```

## Privacidad

La autorización vigente registrada para esa candidatura.

## Gates y manifiestos

Cuando sean necesarios para comprobar trazabilidad o composición.

---

# 6. Jerarquía de evaluación

El veredicto consta de **cuatro capas consecutivas**.

No pueden compensarse entre sí.

---

# CAPA 1 — Integridad

Resultado:

```text
apta
no_apta
```

Es `no_apta` si existe al menos una de estas situaciones:

- hecho profesional no respaldado;
- métrica inventada o alterada;
- cargo, fecha o empresa incorrectos;
- formación presentada con nivel superior al acreditado;
- tecnología o dominio no acreditado;
- experiencia transferible presentada como experiencia literal;
- formación presentada como experiencia;
- automatización presentada como IA sin respaldo;
- responsabilidad colectiva presentada como individual;
- dato privado utilizado sin autorización;
- dato privado autorizado para omitir que aparece;
- restricción factual incumplida;
- requisito de oferta presentado como cumplido cuando no lo está.

Una integridad `no_apta` bloquea automáticamente el avance.

---

# CAPA 2 — Fidelidad al flujo

Resultado:

```text
apta
no_apta
```

Debe comprobarse que:

### Estrategia

El CV no contradice `candidatura.md`.

### Guion

- aparecen las decisiones `incluir`;
- no reaparecen las decisiones `omitir`;
- se conservan prioridades;
- se respeta seniority;
- se respeta el idioma;
- se respetan restricciones;
- la arquitectura narrativa sustantiva sigue siendo reconocible.

### Datos de generación

El contenido visible del CV coincide semánticamente con `datos-generacion.json`.

La composición no:

- reescribió;
- resumió;
- añadió;
- fusionó;
- tradujo;
- eliminó contenido por iniciativa propia.

### Composición

Solo tomó decisiones pertenecientes a:

- estilo;
- espaciado;
- distribución;
- paginación;
- formato;
- fotografía;
- recursos técnicos autorizados.

Si la desviación pertenece a una fase anterior:

```text
→ registrar defecto
→ identificar capa propietaria
```

No corregir el PDF manualmente.

Una fidelidad `no_apta` bloquea el avance.

---

# CAPA 3 — Calidad recruiter del CV final

Solo se puntúa si:

```text
integridad: apta
fidelidad_flujo: apta
```

Se utilizan **seis criterios**, todos de 1 a 5.

## C1 — Primer escaneo y posicionamiento

Pregunta:

> ¿En aproximadamente 6–10 segundos queda claro quién es esta persona, para qué tipo de aportación compite y por qué merece continuar leyendo?

Evalúa:

- titular;
- perfil;
- primera evidencia;
- jerarquía;
- señal competitiva inicial.

---

## C2 — Encaje competitivo real

Pregunta:

> ¿El CV muestra de forma convincente las evidencias más relevantes para las necesidades reales de la oferta?

Evalúa:

- requisitos;
- funciones;
- problemas del puesto;
- transferibilidad;
- carencias;
- riesgo de descarte.

No evalúa solo que las keywords estén presentes.

Debe distinguir:

```text
CV bien construido
≠
candidatura competitiva
```

---

## C3 — Cobertura ATS respaldada

Pregunta:

> ¿Está presente de forma natural el vocabulario útil de la oferta que puede defenderse factual y profesionalmente?

Penaliza:

- keyword stuffing;
- términos sin respaldo;
- omisión innecesaria de términos respaldados relevantes.

---

## C4 — Fuerza de la evidencia

Pregunta:

> ¿Las experiencias prioritarias demuestran acciones, contexto, alcance y resultados con suficiente fuerza y especificidad?

Evalúa:

- hechos concretos;
- resultados;
- métricas;
- responsabilidades;
- diferenciación.

No exige una métrica cuando no exista.

---

## C5 — Adecuación narrativa y seniority

Pregunta:

> ¿El documento presenta la trayectoria desde el nivel y el ángulo apropiados para esta oportunidad sin falsear cargos ni degradar artificialmente la historia?

Evalúa:

- coherencia;
- progresión;
- tono;
- seniority;
- sobrecualificación;
- foco;
- densidad de trayectoria secundaria.

---

## C6 — Calidad documental y visual

Pregunta:

> ¿El PDF terminado favorece la lectura de recruiter y materializa correctamente la jerarquía editorial?

Evalúa:

- legibilidad;
- densidad;
- espacios;
- jerarquía;
- fotografía;
- consistencia;
- longitud;
- equilibrio;
- uso de página;
- anomalías visuales;
- cortes;
- desbordamientos.

No decide preferencias estéticas arbitrarias.

Debe relacionar cualquier defecto con una consecuencia de selección.

Ejemplo:

```text
demasiado contenido secundario
→ diluye primer escaneo
```

y no:

```text
no me gusta este color
```

---

# 7. Escala común 1–5

```text
1 — Deficiente
Provoca una lectura claramente desfavorable o no cumple el criterio.

2 — Débil
Existe base útil, pero el defecto reduce materialmente la competitividad.

3 — Correcta
Alcanza un nivel suficiente, aunque conserva una debilidad relevante.

4 — Sólida
Clara, pertinente, creíble y competitiva; solo admite mejoras menores.

5 — Excelente
Especialmente fuerte, diferenciada y precisa para esta oportunidad sin superar los límites factuales.
```

Cada criterio debe registrar:

```text
nota
evidencia_observada
fortaleza
debilidad
impacto_recruiter
mejora_posible
capa_propietaria
limite_factual
```

La media puede calcularse únicamente como indicador.

**Nunca gobierna el resultado.**

---

# CAPA 4 — Decisión de veredicto

Resultados propuestos:

```text
bloqueado_por_integridad
requiere_correccion_de_flujo
no_competitivo
revisar_antes_de_presentar
apto_para_presentacion
```

## `bloqueado_por_integridad`

Cuando:

```text
integridad: no_apta
```

No puede presentarse.

Debe corregirse la capa propietaria y regenerarse todo lo downstream que corresponda.

---

## `requiere_correccion_de_flujo`

Cuando:

```text
integridad: apta
fidelidad_flujo: no_apta
```

El contenido puede ser verdadero, pero el resultado no materializa correctamente el contrato.

No puede presentarse.

---

## `no_competitivo`

Cuando:

```text
integridad: apta
fidelidad: apta
```

pero el recruiter concluye que el CV representa correctamente una candidatura cuyo encaje real es insuficiente para recomendar presentación.

Debe justificarse con evidencia concreta de la oferta.

No significa:

```text
CV defectuoso
```

Puede significar:

```text
CV correcto
+
candidatura débil
```

Este resultado es necesario para casos como CAND-2026-019.

---

## `revisar_antes_de_presentar`

Cuando el CV es viable, pero existe al menos una debilidad corregible suficientemente relevante como para justificar una nueva iteración antes de presentación.

Normalmente:

- alguna nota 2;
- o nota 3 con mejora clara de alto impacto;
- o combinación de varios 3 que debilita la candidatura.

No se utiliza si corregir exigiría inventar hechos.

---

## `apto_para_presentacion`

Solo cuando:

```text
integridad: apta
fidelidad: apta
```

y el recruiter considera que:

- la propuesta de valor es clara;
- las evidencias prioritarias son visibles;
- no existe defecto competitivo material corregible;
- el documento final es profesional;
- las carencias reales están tratadas correctamente;
- el CV representa la mejor candidatura factual razonable con la información disponible.

No exige perfección.

---

# 8. Precedencia

```text
bloqueado_por_integridad
>
requiere_correccion_de_flujo
>
no_competitivo
>
revisar_antes_de_presentar
>
apto_para_presentacion
```

La media nunca modifica esta precedencia.

---

# 9. Corrección por capa

Todo defecto debe clasificarse:

```text
factual
estrategia
guion
contenido
privacidad
composicion
competitividad_no_corregible
```

Ruta:

```text
factual
→ fuente factual / DEF-ARQ-001

estrategia
→ candidatura / análisis

guion
→ PLAYBOOK_GUION_ADAPTACION_CV

contenido
→ PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA

privacidad
→ autorización de candidatura

composición
→ compositor / template

competitividad_no_corregible
→ no maquillar
→ decisión humana sobre mantener la candidatura
```

Regla fundamental:

> El veredicto diagnostica y enruta. No parchea el CV.

---

# 10. Salida

Artefacto:

```text
veredicto-final-cv.md
```

Debe identificar inequívocamente:

- candidatura;
- empresa;
- puesto;
- versión/huella del CV evaluado;
- fecha;
- artefactos consultados;
- resultado de integridad;
- resultado de fidelidad;
- seis puntuaciones recruiter;
- diagnóstico competitivo;
- defectos detectados;
- capa propietaria;
- correcciones necesarias;
- resultado global;
- recomendación para gate;
- decisión humana posterior.

Debe poder saberse exactamente **qué CV fue evaluado**.

Una regeneración del CV invalida el veredicto anterior como veredicto vigente.

---

# 11. Gate de salida propuesto

```text
GATE-VEREDICTO-CV-PRESENTACION
```

El playbook puede recomendar:

```text
aprobar
no_aprobar
```

Regla:

```text
apto_para_presentacion
→ recomendar aprobar

cualquier otro resultado
→ recomendar no_aprobar
```

La IA no aprueba el gate.

La persona responsable decide:

```text
pendiente
aprobado
bloqueado
```

Un gate aprobado significa exclusivamente:

> El CV evaluado puede avanzar hacia la futura fase de presentación.

No significa:

- candidatura enviada;
- empresa aprobada;
- carta aprobada;
- aceptación de condiciones;
- autorización para automatizar el envío.

---

# 12. Relación con la revisión humana posterior a composición

La revisión humana ya exigida por la SPEC y este veredicto **no son la misma cosa**.

## Revisión humana posterior a composición

Pregunta:

> ¿El documento generado parece correcto y suficientemente estable para someterlo al veredicto?

Es una barrera de aceptación del artefacto generado.

## Nuevo veredicto

Pregunta:

> ¿Este CV final, confrontado con la oferta y con todo el contrato factual/estratégico, merece avanzar hacia presentación?

Por tanto:

```text
revisión humana
→ precondición

veredicto
→ evaluación formal

gate
→ decisión humana de avance
```

---

# 13. Fuera de responsabilidad

El veredicto no:

- redacta una nueva versión del CV;
- modifica `datos-generacion.json`;
- modifica el guion;
- modifica estrategia;
- investiga hechos nuevos;
- modifica autorizaciones privadas;
- remaqueta el documento;
- genera carta;
- presenta candidatura;
- cambia automáticamente estados;
- aprueba su propio gate.

---

# 14. Investigación externa

La investigación contextual **no forma parte del veredicto base**.

Si en el futuro se permite:

```text
veredicto inicial
→ terminado primero
→ investigación opcional autorizada
→ potencial nueva iteración
→ nuevo veredicto
```

Nunca puede utilizarse para:

- inventar fit cultural;
- atribuir prácticas no demostradas;
- añadir experiencia al candidato.

Este punto conserva el principio útil del diseño histórico, pero queda fuera del contrato mínimo inicial.

---

# 15. Casos de aceptación iniciales

## CAND-2026-020 — Lidl

El contrato debe poder producir razonablemente:

```text
integridad: apta
fidelidad_flujo: apta
competitividad: suficiente
resultado esperado:
apto_para_presentacion
```

si el CV vigente mantiene la calidad observada.

---

## CAND-2026-019 — ASIC

El contrato debe poder producir razonablemente:

```text
integridad: apta
fidelidad_flujo: apta
CV técnicamente correcto
PERO
encaje competitivo insuficiente/parcial
resultado esperado:
no_competitivo
```

sin intentar mejorar artificialmente el resultado mediante:

- IA no acreditada;
- Power Platform no acreditada;
- Dynamics;
- Salesforce;
- grado universitario inexistente.

La existencia de estos dos resultados diferentes constituye una prueba esencial del contrato.

---

# 16. Criterios de aceptación del futuro playbook

El futuro `PLAYBOOK_VEREDICTO_FINAL_CV` será aceptable si:

- [ ] evalúa el PDF real;
- [ ] usa obligatoriamente los dos roles;
- [ ] comprueba integridad antes de calidad;
- [ ] comprueba fidelidad del pipeline;
- [ ] puntúa los seis criterios recruiter;
- [ ] distingue CV correcto de candidatura competitiva;
- [ ] puede emitir `no_competitivo`;
- [ ] no maquilla carencias;
- [ ] asigna cada defecto a su capa;
- [ ] invalida el veredicto cuando cambia el CV;
- [ ] no modifica artefactos anteriores;
- [ ] no autoriza envíos;
- [ ] conserva decisión humana del gate;
- [ ] diferencia revisión humana, veredicto y presentación;
- [ ] funciona de forma general con 019 y 020.

---

# 17. Contrato normativo resumido de fase

## OBJETIVO

Determinar si el CV final generado es íntegro, fiel al flujo y suficientemente competitivo para avanzar hacia presentación.

## PRECONDICIONES

CV final generado, composición correcta, revisión humana posterior a composición realizada, privacidad resuelta y candidatura no presentada.

## ENTRADAS

CV final, `datos-generacion.json`, guion, candidatura, análisis, fuentes factuales autorizadas, autorización privada y controles/gates necesarios.

## RESPONSABILIDADES

Integridad, fidelidad, evaluación recruiter, evaluación visual/documental, diagnóstico competitivo, clasificación de defectos y recomendación de gate.

## FUERA_DE_RESPONSABILIDAD

Redacción, estrategia, factualidad nueva, composición, carta, investigación base, envío y aprobación del gate.

## SALIDA

```text
veredicto-final-cv.md
```

## POSTCONDICIONES

Existe un diagnóstico reproducible del CV concreto, defectos enrutados por capa y recomendación explícita de avance/no avance.

## DEFECTOS_CRITICOS

Invención, privacidad incorrecta, desviación del pipeline, composición que altera contenido, evaluación sin PDF, aprobación de un CV competitivo solo por puntuación media o aprobación automática.

## GATE_SIGUIENTE

```text
GATE-VEREDICTO-CV-PRESENTACION
```

## CRITERIOS_DE_ACEPTACION

Los definidos en la sección 16.