---
id: PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
version: 1.0.1
estado: pendiente
aprobacion_humana: pendiente
alcance: exclusivo_cv
entrada: guion-adaptacion-cv.md
salida: datos-generacion.json
gate_entrada: GATE-GUION-CV-CONTENIDO
gate_salida: GATE-CONTENIDO-CV-COMPOSICION
template: TEMPLATE_DATOS_GENERACION_CV.json
schema_esperado: datos-generacion-cv
version_schema_esperada: 1.2
version_template_esperada: 1.2
spec_referencia: SPEC-Arquitectura-modular-generación-candidatura-v0-4-0.md
playbook_anterior: PLAYBOOK_GUION_ADAPTACION_CV
defectos_relacionados:
  - DEF-ARQ-001
---

# Playbook — Generación de contenido del CV

## 1. Propósito y alcance

`PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA` transforma un `guion-adaptacion-cv.md` aprobado en **contenido textual final y estructurado para un CV concreto**.

Produce:

```text
datos-generacion.json
```

En la arquitectura actual, este playbook y `datos-generacion.json` tienen alcance exclusivamente CV.

El nombre histórico `PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA` se conserva porque es el identificador arquitectónico vigente.

No implica generación común de CV y carta.

La fase:

* redacta contenido final;
* materializa decisiones editoriales;
* preserva factualidad;
* preserva estrategia;
* preserva trazabilidad;
* entrega contenido cerrado para composición determinista.

No:

* vuelve a analizar la oferta;
* vuelve a diseñar la candidatura;
* reselecciona evidencia;
* modifica el guion;
* diseña carta;
* compone DOCX, PDF o LaTeX;
* decide diseño visual;
* ejecuta el generador;
* realiza veredicto final;
* envía la candidatura.

Pregunta:

> Dado un guion de CV aprobado, ¿cuál es la redacción final más clara, competitiva, factual y compacta que materializa exactamente sus decisiones sin volver a decidir qué historia contar?

---

## 2. Posición dentro de la arquitectura

```text
candidatura.md
        ↓
PLAYBOOK_GUION_ADAPTACION_CV
        ↓
guion-adaptacion-cv.md
        ↓
GATE-GUION-CV-CONTENIDO
        ↓
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
        ↓
datos-generacion.json
        ↓
GATE-CONTENIDO-CV-COMPOSICION
        ↓
futura composición del CV
```

Responsabilidades:

```text
candidatura.md
→ estrategia

guion-adaptacion-cv.md
→ decisiones editoriales

PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
→ redacción final

datos-generacion.json
→ contenido final estructurado + trazabilidad

composición futura
→ materialización técnica
```

Principio:

> El guion decide; esta fase redacta; la composición materializa.

---

## 3. Contrato normativo de fase

### OBJETIVO

Producir la redacción final estructurada del CV a partir de un guion aprobado, conservando:

* idioma;
* posicionamiento;
* selección;
* evidencia;
* jerarquía;
* seniority;
* tono;
* restricciones;
* cobertura estratégica;
* arquitectura editorial.

La composición debe poder utilizar la salida sin reconstruir estrategia ni reescribir contenido.

### PRECONDICIONES

* `GATE-GUION-CV-CONTENIDO: aprobado`;
* `guion-adaptacion-cv.md` vigente;
* `idioma_cv` explícito en el guion;
* evaluación del gate resoluble;
* `presentada: false`;
* fuentes necesarias resolubles;
* ausencia de bloqueo;
* template JSON aprobado antes de ejecución material.

Una candidatura presentada solo puede utilizarse como prueba retrospectiva controlada.

### ENTRADAS

Principal:

```text
guion-adaptacion-cv.md
```

Validación:

```text
evaluacion-gate-guion-cv-contenido.md
```

Fuentes factuales:

* solo las ya autorizadas por el guion;
* `datos-core-busqueda.md` cuando proceda;
* otras expresamente trazadas.

Las fuentes se consultan para resolver o verificar contenido autorizado.

No para descubrir nuevos argumentos.

### RESPONSABILIDADES

* respetar `idioma_cv`;
* redactar titular;
* redactar perfil;
* redactar experiencia;
* redactar funciones;
* redactar responsabilidades;
* redactar logros;
* redactar resultados;
* integrar métricas;
* redactar formación y secciones autorizadas;
* preservar cargos, empresas y fechas;
* aplicar seniority;
* aplicar tono;
* aplicar convención gramatical;
* utilizar léxico respaldado;
* respetar restricciones;
* materializar presencia, obligatoriedad, peso, ubicación, orden y detalle;
* preservar cobertura estratégica;
* controlar duplicación;
* producir contenido competitivo para recruiter;
* producir ATS respaldado;
* mantener trazabilidad;
* serializar conforme al template.

### FUERA_DE_RESPONSABILIDAD

No puede:

* cambiar idioma;
* modificar estrategia;
* modificar posicionamiento;
* añadir evidencia no autorizada;
* recuperar contenido `omitir`;
* cambiar obligatoriedad;
* cambiar peso;
* cambiar función estratégica;
* cambiar arquitectura editorial;
* cambiar seniority histórico;
* inventar hechos;
* investigar externamente;
* diseñar carta;
* diseñar composición;
* decidir formato visual;
* generar formatos finales;
* resolver `DEF-ARQ-001`.

### SALIDA

```text
datos-generacion.json
```

Solo contiene datos y contenido del CV.

### POSTCONDICIONES

* idioma respetado;
* redacción completa;
* ausencia de placeholders;
* contenido incluido materializado;
* omitido ausente;
* obligaciones respetadas;
* jerarquía preservada;
* restricciones cumplidas;
* hechos exactos;
* contenido sustantivo trazable;
* cobertura estratégica auditable;
* restricciones auditables;
* JSON válido;
* composición capaz de consumirlo sin reescribir.

### DEFECTOS_CRITICOS

* cambio de idioma;
* invención factual;
* contenido no respaldado;
* recuperación de omitido;
* pérdida de obligatorio;
* pérdida injustificada de prioridad;
* cambio silencioso de peso;
* cambio silencioso de seniority;
* alteración de cargo o fecha;
* métrica inventada;
* transferencia presentada como experiencia literal;
* formación presentada como experiencia;
* automatización presentada como IA sin respaldo;
* keyword convertida en experiencia;
* término prohibido;
* contradicción con guion;
* JSON inválido;
* placeholders;
* carta;
* decisiones visuales;
* necesidad de que composición reescriba.

### GATE_SIGUIENTE

```text
GATE-CONTENIDO-CV-COMPOSICION
```

### CRITERIOS_DE_ACEPTACION

Los definidos en la sección 17.

---

## 4. Jerarquía de autoridad

### 4.1 `guion-adaptacion-cv.md`

Gobierna:

* idioma;
* presencia;
* obligatoriedad;
* peso;
* criterio objetivo;
* función estratégica;
* sección;
* orden;
* detalle;
* seniority;
* tono;
* léxico;
* restricciones;
* cobertura;
* arquitectura;
* brief.

No se reevalúan estas decisiones.

### 4.2 Fuentes factuales

Gobiernan:

* identidad;
* cargos;
* empresas;
* fechas;
* responsabilidades;
* tecnologías;
* hechos;
* resultados;
* métricas;
* formación.

### 4.3 `candidatura.md` y `analisis-oferta.md`

Solo para:

* trazabilidad;
* resolver referencia explícita;
* comprobar autoridad anterior.

No para reconstruir o mejorar silenciosamente el guion.

### 4.4 Conflicto

Si:

```text
guion
vs
fuente factual
```

se contradicen:

```text
requiere_revision_origen
```

Si aparece evidencia factual nueva:

```text
requiere_actualizacion_factual
→ DEF-ARQ-001
```

---

## 5. Operaciones permitidas

Puede:

```text
redactar
parafrasear
condensar
fusionar
dividir
normalizar
ordenar según guion
```

Son operaciones semánticamente conservadoras.

No cambian:

* actor;
* acción;
* contexto;
* fecha;
* alcance;
* resultado;
* causalidad;
* tecnología;
* responsabilidad;
* precisión de métricas;
* restricciones.

### 5.1 Fusionar

Varias decisiones pueden formar una unidad cuando:

* pertenecen a la misma sección;
* son compatibles;
* mejora claridad;
* conservan trazabilidad.

Las restricciones se acumulan.

> En una fusión prevalece la restricción más exigente.

### 5.2 Dividir

Una decisión puede producir varias unidades cuando:

* el detalle lo justifica;
* contiene evidencias distintas;
* mejora comprensión.

No se utiliza para inflar peso.

### 5.3 Condensar

Puede reducir longitud.

No puede perder:

* hecho principal;
* función estratégica;
* evidencia diferencial;
* restricción.

Si cumplir el presupuesto obliga a eliminar una decisión del guion:

```text
requiere_revision_origen
```

---

## 6. Modelo de trazabilidad

Contenido visible:

```text
C-001
C-002
C-003
...
```

### 6.1 Contenido derivado de `M-NNN`

```text
C-NNN
→ M-NNN
→ evidencia
```

Se permiten relaciones muchos-a-muchos con trazabilidad explícita.

### 6.2 Continuidad autorizada por sección

Puede existir:

```text
C-NNN
→ SEC-NN
→ fuente factual
```

solo para:

* empresa;
* cargo;
* periodo;
* información mínima de continuidad.

No autoriza incorporar sin `M-NNN`:

* logros;
* resultados;
* responsabilidades competitivas;
* tecnologías;
* competencias;
* métricas;
* afirmaciones de encaje.

### 6.3 Datos personales y administrativos

Antes de generar el JSON debe existir en `candidatura.md` una decisión resuelta en
`autorizacion_datos_cv`. La decisión la toma la persona responsable de la candidatura
y debe registrar, de forma independiente, `nombre`, `apellido_1`, `apellido_2`,
`email`, `telefono`, `linkedin`, `ubicacion` y `fotografia` como `incluir` u `omitir`.

El JSON debe copiar únicamente los campos autorizados desde
`datos-privados-candidatura.md`, conservar la separación entre nombre, apellido 1 y
apellido 2 y dejar trazabilidad de cada componente. Los campos `omitir` no pueden
aparecer en `contenido_cv`; una decisión `pendiente` bloquea la generación del CV.
La autorización se materializa en `control.datos_privados` y el compositor solo
consume ese JSON, sin consultar la candidatura ni la fuente privada durante la
composición.

No necesitan `M-NNN` cuando no constituyen afirmación competitiva.

### 6.4 Exhaustividad

Toda afirmación profesional sustantiva debe recorrer:

```text
C
→ M
→ evidencia
```

o, para continuidad:

```text
C
→ SEC
→ fuente factual
```

---

## 7. Correspondencia con el mapa

### Presencia

```text
incluir
→ debe materializarse

omitir
→ no puede aparecer
```

### Obligatoriedad

```text
obligatoria
→ representación inequívoca
```

### Peso

`alto` → protagonismo claro.

`medio` → visible pero subordinado.

`bajo` → compacto.

`minimo` → indispensable.

Peso gobierna prominencia.

No longitud exacta.

### Detalle

```text
amplio
normal
breve
mencion
```

### Ubicación y orden

Respetar:

```text
seccion_destino
orden_en_seccion
```

Solo son admisibles microajustes sintácticos.

---

## 8. Convención gramatical de redacción

La fase debe producir una voz coherente y determinista.

### 8.1 Regla general

No utilizar pronombres personales explícitos como apertura habitual:

```text
Yo
I
```

El CV debe sonar profesional, directo y orientado a evidencia.

### 8.2 Perfil o resumen

Preferir construcción profesional nominal o descriptiva.

Ejemplo conceptual:

```text
Profesional de operaciones de supermercados con experiencia en...
```

Evitar:

```text
Soy un profesional...
```

salvo que una regla lingüística específica lo exija.

### 8.3 Experiencia en español

Para responsabilidades o logros personales:

* experiencia terminada → verbo de acción en primera persona singular, preferentemente pretérito;
* experiencia vigente → verbo de acción en presente;
* omitir el pronombre `yo`.

Ejemplos:

```text
Diseñé...
Implanté...
Reorganicé...
Gestiono...
Coordino...
```

No convertir por sistema todo el contenido en sustantivos como:

```text
Gestión de...
Realización de...
Responsabilidad sobre...
```

cuando un verbo de acción produzca una evidencia más clara.

### 8.4 Experiencia en inglés

Cuando `idioma_cv` sea inglés, seguir la convención propia del CV en inglés:

```text
Designed...
Implemented...
Managed...
```

sin pronombre `I`.

### 8.5 Otros idiomas

Aplicar la convención profesional equivalente del idioma decidido.

No traducir literalmente la sintaxis española cuando resulte antinatural.

### 8.6 Coherencia temporal

Dentro de una misma experiencia debe mantenerse el tiempo verbal coherente con su estado temporal.

No alternar arbitrariamente:

```text
Diseñé
Gestionaba
Implemento
```

salvo que el significado temporal lo justifique.

### 8.7 Excepción

Una construcción nominal puede utilizarse cuando:

* sea una etiqueta;
* sea un titular;
* sea una competencia;
* sea una cabecera;
* resulte lingüísticamente más natural;
* el guion requiera una mención mínima.

La convención gramatical nunca autoriza alterar un hecho.

---

## 9. Procedimiento normativo

### Paso 1 — Validar precondiciones

Confirmar:

* gate;
* decisión humana;
* guion;
* idioma;
* fuentes;
* candidatura;
* bloqueo;
* template.

### Paso 2 — Cargar contrato editorial

Extraer:

* idioma;
* posicionamiento;
* gancho;
* seniority;
* tono;
* mapa;
* arquitectura;
* léxico;
* límites;
* cobertura;
* duplicación;
* brief.

### Paso 3 — Construir inventario de salida

Por `SEC-NN`:

* `M-NNN` incluidos;
* obligatorios;
* continuidad;
* orden;
* profundidad;
* restricciones.

No tomar nuevas decisiones.

### Paso 4 — Instanciar template

Usar exactamente el template vigente.

No inventar propiedades.

### Paso 5 — Resolver datos estables

Obtener solo datos necesarios.

No inferir huecos.

### Paso 6 — Redactar apertura

Cuando proceda:

* titular;
* perfil;
* resumen.

Aplicar:

* idioma;
* posicionamiento;
* gancho;
* seniority;
* tono;
* convención gramatical.

### Paso 7 — Redactar experiencia principal

Por experiencia:

1. preservar empresa;
2. preservar cargo;
3. preservar periodo;
4. procesar contenido autorizado;
5. aplicar orden;
6. aplicar profundidad;
7. aplicar restricciones;
8. aplicar convención gramatical;
9. registrar trazabilidad.

### Paso 8 — Redactar continuidad

Solo información suficiente.

No rescatar contenido competitivo no seleccionado.

### Paso 9 — Redactar secciones adicionales

Solo las previstas.

### Paso 10 — Revisar seniority, tono e idioma

Comprobar:

* cargo;
* responsabilidad;
* tono;
* idioma;
* uniformidad.

### Paso 11 — Aplicar léxico y ATS

Solo términos:

* autorizados;
* respaldados;
* naturales.

### Paso 12 — Optimizar redacción

Preferir:

* hechos;
* verbos específicos;
* acción;
* alcance;
* efecto;
* métricas defendibles.

Eliminar:

* clichés;
* autoelogio;
* lenguaje de carta.

### Paso 13 — Controlar duplicación

La misma evidencia solo se repite cuando cumple función distinta.

### Paso 14 — Ajustar densidad

Preservar:

1. obligatorios;
2. peso alto;
3. evidencia diferencial;
4. peso medio;
5. peso bajo;
6. mínimo.

### Paso 15 — Validar cobertura del mapa

```text
cada M-NNN incluir
→ C-NNN

cada C-NNN competitivo
→ M-NNN
```

### Paso 16 — Validar cobertura estratégica

Cada prioridad estratégica del guion debe conservar una materialización auditable.

No basta con marcar todos los `M-NNN`.

Debe comprobarse que la relación estratégica entre ellos sigue visible.

### Paso 17 — Validar restricciones

Cada restricción material debe indicar:

* origen;
* contenido afectado;
* cumplimiento.

### Paso 18 — Validar primer escaneo textual

Debe hacer visible:

1. perfil;
2. encaje;
3. dos o tres señales;
4. evidencia diferencial.

### Paso 19 — Serializar JSON

Debe ser:

* JSON válido;
* conforme al template;
* sin comentarios;
* sin placeholders;
* sin carta;
* sin instrucciones visuales.

### Paso 20 — Control final y gate

Revisar todo el contrato y evaluar:

```text
GATE-CONTENIDO-CV-COMPOSICION
```

---

## 10. Reglas de redacción profesional

### 10.1 Redactar, no transcribir

No aparecen:

* motivos internos;
* advertencias;
* etiquetas;
* instrucciones editoriales.

### 10.2 Hecho antes que adjetivo

Preferir evidencia observable.

### 10.3 Responsabilidad no equivale a logro

Función:

> qué hacía.

Logro:

> qué cambió o consiguió.

### 10.4 Acción, contexto y efecto

Cuando exista evidencia:

```text
acción
+ contexto
+ efecto
```

No inventar componentes ausentes.

### 10.5 Una idea principal por unidad

Evitar unidades excesivamente acumulativas.

### 10.6 Métricas

Solo:

* existentes;
* trazables;
* contextualizadas.

### 10.7 Competencias

Preferir evidencia frente a autoevaluación.

---

## 11. Reglas por tipo de contenido

### Titular

Sintetiza posicionamiento.

No sustituye cargo histórico.

### Perfil

Orienta lectura.

No introduce hechos.

### Experiencia

Preserva:

* empresa;
* cargo;
* periodo.

### Continuidad

Contextualiza.

No compite con experiencia prioritaria.

### Formación

No crea:

* títulos;
* equivalencias;
* acreditaciones.

### Herramientas y tecnologías

Solo autorizadas.

### Transferibilidad

No equivale a experiencia literal.

### Automatización e IA

No son equivalentes.

---

## 12. Seniority y sobrecualificación

Puede:

* reducir protagonismo directivo;
* priorizar ejecución;
* priorizar proximidad funcional.

No puede:

* cambiar cargo;
* ocultar historia necesaria;
* presentar responsabilidad inferior ficticia.

> Se adapta la atención del recruiter, no la historia profesional.

---

## 13. Léxico y ATS

Clasificaciones:

```text
utilizable
uso_condicionado
prohibido
```

ATS:

> vocabulario relevante respaldado.

No:

> copiar vocabulario de oferta sin evidencia.

---

## 14. Idioma

La fase consume:

```text
idioma_cv
```

del guion.

No lo decide.

No lo cambia.

Si falta:

```text
requiere_revision_origen
```

Si el contenido recibido contiene fragmentos en otro idioma sin autorización:

```text
requiere_correccion
```

o `requiere_revision_origen` cuando procedan del guion.

---

## 15. Incidencias y retroceso

### Error local de redacción

```text
requiere_correccion
```

### Corrección que cambiaría decisión editorial

```text
requiere_revision_origen
```

### Guion insuficiente

```text
requiere_revision_origen
```

### Idioma ausente o ambiguo

```text
requiere_revision_origen
```

### Evidencia factual nueva

```text
requiere_actualizacion_factual
DEF-ARQ-001
```

### Contradicción factual

```text
requiere_revision_origen
```

### Bloqueo

```text
bloqueado
```

---

## 16. Precedencia

```text
bloqueado
>
requiere_actualizacion_factual
>
requiere_revision_origen
>
requiere_correccion
>
apto
```

Todas las incidencias se registran.

---

## 17. Criterios de aceptación

* [ ] precondiciones;
* [ ] idioma correcto;
* [ ] JSON válido;
* [ ] template vigente;
* [ ] solo CV;
* [ ] sin placeholders;
* [ ] fidelidad al guion;
* [ ] todos los `incluir`;
* [ ] ningún `omitir`;
* [ ] obligatorios presentes;
* [ ] peso alto visible;
* [ ] ubicación y orden;
* [ ] continuidad autorizada;
* [ ] seniority;
* [ ] tono;
* [ ] convención gramatical;
* [ ] cargos y fechas;
* [ ] hechos;
* [ ] métricas;
* [ ] restricciones auditadas;
* [ ] cobertura estratégica auditada;
* [ ] léxico;
* [ ] ATS;
* [ ] duplicación;
* [ ] claridad;
* [ ] primer escaneo;
* [ ] trazabilidad;
* [ ] ninguna estrategia nueva;
* [ ] ninguna investigación externa;
* [ ] ninguna composición;
* [ ] ninguna carta;
* [ ] composición futura no necesita reescribir.

---

## 18. Evaluación del gate

Artefacto:

```text
evaluacion-gate-contenido-cv-composicion.md
```

Campos:

```text
id
tipo
candidatura
gate
datos_generacion_evaluados
guion_origen
fecha_evaluacion
resultado_evaluacion
recomendacion_ia
decision_humana
estado_gate
fecha_decision_humana
sesion
```

IA:

```text
apto → aprobar
otro → no_aprobar
```

Decisión humana:

```text
pendiente
aprobado
bloqueado
```

El estado oficial vive en el artefacto de evaluación.

No en el JSON.

Mientras composición no exista:

```text
GATE-CONTENIDO-CV-COMPOSICION: aprobado
```

solo autoriza diseñarla.

---

## 19. Contrato semántico de `datos-generacion.json`

Schema físico:

```text
TEMPLATE_DATOS_GENERACION_CV.json
```

Identificadores y versiones esperados:

```text
schema_id: datos-generacion-cv
schema_version: 1.2
template_id: TEMPLATE_DATOS_GENERACION_CV.json
template_version: 1.2
```

La referencia normativa es el archivo literal
`TEMPLATE_DATOS_GENERACION_CV.json`. El identificador interno del
template se conserva en el frontmatter del contrato canónico.
del contrato, con versión `1.2`.

Debe separar:

### Identificación

* candidatura;
* versiones;
* fecha;
* origen;
* gates.

### Datos factuales

Los necesarios para materializar.

### Contenido visible

* secciones;
* bloques;
* unidades;
* orden;
* texto.

### Trazabilidad

* `C-NNN`;
* `M-NNN` o `SEC-NN`;
* evidencia.

### Control

Debe representar como mínimo:

```text
cobertura_mapa
cobertura_estrategica
cobertura_continuidad
restricciones
lexico
primer_escaneo
validaciones
incidencias
```

No contiene campos de carta.

`datos-generacion.json` no puede contener datos, rutas, secciones ni decisiones
de carta de presentación.

`datos-generacion.json` no puede contener decisiones de composición ni
maquetación.

### Campos contractuales verificables

Cada unidad visible debe registrar `id_contenido`, `refs_guion`,
`ref_seccion_guion` y `origen_factual`, según su modo de trazabilidad.

El bloque `control` debe mantener, como mínimo, los campos `cobertura_mapa`,
`cobertura_estrategica`, `cobertura_continuidad`, `restricciones`, `lexico`,
`primer_escaneo`, `validaciones` e `incidencias`.

`validaciones` debe incluir `idioma_respetado`, `solo_cv`,
`sin_placeholders`, `fidelidad_guion`, `cobertura_incluir_completa`,
`cobertura_estrategica_completa`, `sin_contenido_omitido`,
`obligatorios_presentes`, `peso_alto_respetado`,
`ubicacion_y_orden_respetados`, `continuidad_limitada_a_lo_autorizado`,
`seniority_respetado`, `tono_respetado`,
`convencion_gramatical_respetada`, `restricciones_respetadas`,
`lexico_respetado`, `sin_keyword_stuffing`, `duplicacion_controlada`,
`trazabilidad_completa`, `primer_escaneo_textual_apto` y
`sin_decisiones_de_composicion`.

`primer_escaneo` debe registrar `perfil_identificable`, `encaje_visible`,
`senales_fuertes_visibles` y `refs_contenido_dominantes`.

---

## 20. Contenido listo para composición

> El texto visible entregado es el texto que debe aparecer en el CV salvo transformaciones técnicas permitidas posteriormente.

Composición podrá:

* ubicar;
* estilizar;
* paginar;
* transformar formato.

No:

* mejorar frases;
* introducir logros;
* cambiar verbos;
* resumir por iniciativa propia;
* añadir keywords;
* cambiar seniority;
* corregir hechos;
* traducir.

Si composición detecta error de contenido:

```text
→ volver a esta fase
```

---

## 21. Prueba principal — CAND-2026-020

Debe probar:

* operaciones;
* pedidos;
* previsión;
* stock;
* rotación;
* caducidades;
* equipos;
* tareas;
* caja;
* cargo histórico;
* formación;
* sobrecualificación;
* idioma.

Debe impedir:

* FP no finalizada como título;
* tesorería;
* banca;
* compras centralizadas;
* experiencia literal Lidl;
* ruido tecnológico;
* cambio de idioma.

Superado:

```text
→ en_prueba
```

---

## 22. Prueba de generalidad — CAND-2026-019

Debe probar:

* tecnología;
* automatización;
* IA;
* transferibilidad;
* stack;
* seniority;
* léxico;
* idioma;
* evidencia no retail.

Progresión:

```text
020 superado
→ en_prueba

020 + 019
→ candidata a validada
```

`candidata a validada` no es estado formal.

---

## 23. Generalización

No codificar:

* Lidl;
* ASIC;
* supermercados;
* IA;
* casos concretos.

> Los casos prueban el contrato; no lo definen.

---

## 24. Salida correcta

```text
guion-adaptacion-cv.md
        ↓
GATE-GUION-CV-CONTENIDO
        ↓
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
        ↓
datos-generacion.json
        ↓
evaluacion-gate-contenido-cv-composicion.md
```

No produce:

```text
cv.docx
cv.pdf
cv.tex
carta
veredicto
envío
```

---

## 25. Principios finales

### Redacción

> Convierte decisiones en texto final; no vuelve a decidir qué contar.

### Idioma

> El idioma se hereda del guion y no se infiere en esta fase.

### Voz

> La redacción utiliza una convención gramatical coherente con el idioma y el estado temporal de la experiencia.

### Factualidad

> Ninguna mejora estilística justifica modificar un hecho.

### Competitividad

> La evidencia priorizada debe resultar visible y defendible.

### Trazabilidad

> Toda afirmación profesional sustantiva llega a una autorización editorial y una fuente factual.

### Cobertura

> Cubrir todos los `M-NNN` no basta si se pierde la prioridad estratégica que justificaba su combinación.

### Restricciones

> Una restricción importante debe poder auditarse contra el contenido concreto al que afecta.

### Continuidad

> Mantener cronología no autoriza a recuperar contenido competitivo no seleccionado.

### Seniority

> Se adapta el foco, no la historia.

### ATS

> Keywords respaldadas y relevantes, no copia de oferta.

### Corrección por capa

> Texto → esta fase.
> Decisión editorial → guion.
> Formato → composición.

### Agentic

> Si el agente necesita volver a elegir qué historia contar, debe detenerse.
