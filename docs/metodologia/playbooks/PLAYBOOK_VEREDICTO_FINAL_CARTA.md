---
id: PLAYBOOK_VEREDICTO_FINAL_CARTA
tipo: playbook
version: "1.0.0"
estado: en_prueba
alcance: exclusivo_veredicto_final_carta
entrada_principal: carta-presentacion.pdf
entradas_auxiliares:
  - carta-presentacion.docx
  - contenido-carta-presentacion.md
  - guion-carta-presentacion.md
  - candidatura.md
  - analisis-oferta.md
  - cv.pdf
  - evaluacion-composicion-carta-presentacion.md
artefacto_salida: veredicto-final-carta.md
gate_entrada: GATE-CARTA-REVISION-HUMANA
gate_salida: GATE-VEREDICTO-CARTA
---

# PLAYBOOK — Veredicto final de carta de presentación

## 1. Propósito

Este playbook evalúa si una carta de presentación final, ya compuesta y aprobada mediante revisión humana, es suficientemente correcta, útil, coherente y competitiva para incorporarse como componente documental de una candidatura.

Su función no es generar ni mejorar la carta.

Su función es responder:

> Si un recruiter recibe esta carta junto con el CV, ¿la carta mejora, mantiene o perjudica la candidatura y conviene incluirla junto al CV?

Produce:

`veredicto-final-carta.md`

El playbook diagnostica.

No corrige.

---

## 2. Posición en el flujo

```text
candidatura.md
        ↓
guion-carta-presentacion.md
        ↓
contenido-carta-presentacion.md
        ↓
carta-presentacion.docx / pdf
        ↓
evaluacion-composicion-carta-presentacion.md
        ↓
GATE-CARTA-REVISION-HUMANA = aprobado
        ↓
PLAYBOOK_VEREDICTO_FINAL_CARTA
        ↓
veredicto-final-carta.md
        ↓
GATE-VEREDICTO-CARTA
        ↓
decisión humana
```

Este playbook solo puede ejecutarse cuando:

```text
GATE-CARTA-REVISION-HUMANA = aprobado
```

No sustituye esa revisión humana.

Una vez que `GATE-CARTA-REVISION-HUMANA = aprobado` está registrado y no existe
otro dato, decisión o autorización pendiente, la orquestación continúa
automáticamente con este veredicto. La selección efectiva se representa en
`scripts/job-up/orquestar_transiciones.py`: no es válido anunciar el veredicto
como «siguiente paso» y detenerse para pedir confirmación. La decisión humana
del propio `GATE-VEREDICTO-CARTA` sigue siendo obligatoria y es la única pausa
humana de esta transición.

---

## 3. Responsabilidad

El playbook debe evaluar conjuntamente:

```text
valor recruiter
calidad editorial/documental
+
coherencia contractual
+
valor incremental frente al CV
+
conveniencia de inclusión de la carta junto al CV
```

No debe:

- redactar;
- reescribir;
- corregir;
- componer;
- regenerar;
- investigar nuevas evidencias;
- ampliar estrategia;
- añadir hechos;
- modificar el CV;
- modificar la carta;
- decidir la presentación externa.

---

## 4. Pregunta central

La pregunta principal del veredicto es:

> ¿Esta carta aporta suficiente valor adicional, sin introducir riesgos o incoherencias, como para formar parte competitivamente de la candidatura?

Debe distinguirse entre:

```text
calidad de la carta
≠
conveniencia de incluirla
```

Una carta puede ser correcta y no aportar suficiente valor adicional.

---

## 5. Modelo de evaluación

La evaluación se realiza mediante tres roles independientes:

1. Recruiter.
2. Responsable editorial/documental.
3. Auditor de coherencia.

Después se aplica una síntesis determinista.

La síntesis no constituye un cuarto rol experto.

---

# 6. Rol 1 — Recruiter

## 6.1. Responsabilidad

Evalúa el efecto real de la carta en un proceso de selección.

Debe leerla como si acabara de recibirla junto al CV.

Su pregunta central es:

> ¿Después de leer esta carta tengo más razones, las mismas o menos razones para avanzar con el candidato?

## 6.2. Dimensiones

Debe evaluar:

```yaml
recruiter:
  comprension_rapida_encaje:
    alta | media | baja

  valor_incremental_frente_cv:
    alto | medio | bajo

  credibilidad_motivacion:
    alta | media | baja

  especificidad_candidatura:
    alta | media | baja

  efecto_sobre_percepcion_candidato:
    mejora | neutro | perjudica

  hallazgos: []
```

## 6.3. Criterios

Debe comprobar:

- si se entiende rápidamente el encaje;
- si la carta añade algo útil respecto al CV;
- si la motivación resulta creíble;
- si está adaptada a la candidatura concreta;
- si evita limitarse a repetir el CV;
- si fortalece o debilita la percepción del candidato.

## 6.4. Reglas

```text
efecto_sobre_percepcion_candidato = perjudica
→ hallazgo bloqueante
```

```text
valor_incremental_frente_cv = bajo
sin otros defectos
→ reserva relevante
```

---

# 7. Rol 2 — Responsable editorial/documental

## 7.1. Responsabilidad

Evalúa si la carta funciona correctamente como pieza escrita y documental.

No juzga la calidad profesional del candidato.

Su pregunta central es:

> ¿La carta cumple su función con el mínimo texto necesario y sin ruido editorial?

## 7.2. Dimensiones

```yaml
editorial:
  claridad:
    alta | media | baja

  foco:
    alto | medio | bajo

  progresion_argumental:
    solida | suficiente | debil

  redundancia:
    baja | media | alta

  tono:
    adecuado | mejorable | inadecuado

  extension:
    adecuada | aceptable | problematica

  apertura:
    fuerte | suficiente | debil

  cierre:
    fuerte | suficiente | debil

  hallazgos: []
```

## 7.3. Debe evaluar

- claridad;
- foco;
- progresión argumental;
- redundancia;
- apertura;
- cierre;
- tono;
- extensión;
- equilibrio entre párrafos;
- legibilidad general;
- relación documental con el CV.

## 7.4. Regla anti-preferencia

No constituye defecto:

> “Yo lo escribiría de otra forma.”

Sí puede constituir defecto:

> “Este fragmento repite sustancialmente información ya expresada y reduce claridad o eficacia.”

El rol editorial no debe transformar preferencias estilísticas en incidencias.

---

# 8. Rol 3 — Auditor de coherencia

## 8.1. Responsabilidad

Comprueba que la carta final sigue respetando la arquitectura, estrategia, autorizaciones y flujo aprobados.

Su pregunta central es:

> ¿Esta carta final sigue siendo exactamente la carta que la arquitectura autorizó producir?

## 8.2. Dimensiones

```yaml
auditor:
  gates_previos_validos:
    si | no

  coherencia_con_candidatura:
    si | no

  coherencia_con_cv:
    si | no

  respeto_autorizaciones:
    si | no

  ausencia_afirmaciones_nuevas_no_autorizadas:
    si | no

  identidad_empresa_puesto_correcta:
    si | no

  integridad_flujo:
    si | no

  contradicciones: []
```

## 8.3. Reglas

Los incumplimientos contractuales materiales son bloqueantes.

Ejemplos:

```text
afirmación profesional no autorizada
→ bloqueante
```

```text
empresa o puesto incorrectos
→ bloqueante
```

```text
gate previo obligatorio no aprobado
→ bloqueante
```

```text
contradicción profesional relevante con CV o candidatura
→ bloqueante
```

---

# 9. Independencia de los tres roles

Los roles deben evaluar de forma independiente.

No deben ejecutarse como deliberación colectiva.

Modelo:

```text
carta + fuentes permitidas
        ↓
Recruiter
        ↓
evaluación independiente
```

```text
carta + fuentes permitidas
        ↓
Editorial
        ↓
evaluación independiente
```

```text
carta + fuentes permitidas
        ↓
Auditor
        ↓
evaluación independiente
```

Después:

```text
tres evaluaciones
      ↓
síntesis determinista
      ↓
veredicto-final-carta.md
```

Ningún rol debe adaptar su opinión para coincidir con otro.

---

# 10. Conclusión individual de cada rol

Cada rol termina exclusivamente con:

```text
sin_objeciones
observaciones
reservas
hallazgo_bloqueante
```

Ningún rol decide por sí mismo el resultado global.

---

# 11. Síntesis

La síntesis debe:

1. reunir los hallazgos;
2. eliminar duplicados;
3. clasificarlos;
4. aplicar las reglas de precedencia;
5. producir el resultado final.

No puede introducir críticas nuevas.

```text
síntesis
≠
nueva evaluación
```

---

# 12. Precedencia entre hallazgos

La prioridad es:

```text
integridad / coherencia contractual
        >
daño recruiter
        >
reservas de valor competitivo
        >
calidad editorial
        >
observaciones
```

Una carta editorialmente excelente no puede compensar:

- falsedad;
- contradicción;
- dato no autorizado;
- gate inválido;
- incumplimiento contractual.

---

# 13. No existe votación por mayoría

Está prohibido resolver mediante:

```text
dos roles positivos
+
un rol negativo
→ mayoría positiva
```

Un solo hallazgo bloqueante válido obliga a bloquear.

La lógica se basa en clasificación de hallazgos, no en votos.

---

# 14. Clasificación de hallazgos

Todo hallazgo debe pertenecer a una de estas categorías:

```text
bloqueante
reserva_relevante
reserva_menor
observacion
```

---

# 15. Hallazgos bloqueantes

La carta será `NO_APTA` si existe al menos un bloqueante.

Son bloqueantes, entre otros:

- afirmación incompatible con los hechos aprobados;
- contradicción relevante con el CV;
- información no autorizada;
- exageración o promesa no respaldada;
- cambio de posicionamiento respecto a la candidatura;
- empresa incorrecta;
- puesto incorrecto;
- destinatario materialmente incorrecto;
- tono claramente perjudicial;
- genericidad extrema que haga inútil la carta;
- defecto documental que impida su uso;
- gate previo obligatorio no aprobado;
- contradicción operativa no resuelta.

Regla:

```text
1 bloqueante
→ NO_APTA
```

No existe compensación por otros aspectos positivos.

---

# 16. Reservas relevantes

Una reserva relevante no significa que la carta sea falsa o inutilizable.

Significa que existe una limitación competitiva significativa.

Ejemplos:

- valor incremental bajo frente al CV;
- motivación poco diferenciadora;
- exceso notable de generalidades;
- adaptación limitada a empresa o puesto;
- repetición importante del CV;
- apertura o cierre claramente débiles;
- tono demasiado neutro;
- calidad editorial suficiente pero poco competitiva.

Regla:

```text
sin bloqueantes
+
≥ 1 reserva relevante
→ APTA_CON_RESERVAS
```

---

# 17. Reservas menores

Son limitaciones reales pero no suficientes para cambiar por sí solas el resultado.

Ejemplos:

- alguna reiteración;
- formulación ligeramente larga;
- cierre mejorable pero correcto;
- pequeña pérdida de foco;
- ajuste editorial menor.

Una reserva menor puede coexistir con:

```text
APTA
```

---

# 18. Observaciones

Las observaciones no constituyen defectos.

Ejemplos:

- existiría otra formulación igualmente válida;
- podría usarse una apertura alternativa;
- podría hacerse una reducción estilística sin necesidad real.

Regla:

```text
observacion
≠ defecto
```

Las observaciones no deben iniciar ciclos de reescritura.

---

# 19. Resultado final

Solo existen tres resultados:

```text
APTA
APTA_CON_RESERVAS
NO_APTA
```

Reglas:

```text
si existe bloqueante
→ NO_APTA
```

```text
si no hay bloqueantes
y existe reserva relevante
→ APTA_CON_RESERVAS
```

```text
si no hay bloqueantes
ni reservas relevantes
→ APTA
```

---

# 20. Valor incremental frente al CV

El valor incremental constituye una dimensión propia.

Debe evaluarse como:

```text
alto
medio
bajo
```

No significa necesariamente introducir hechos adicionales.

Puede aportar valor mediante:

- contextualización;
- motivación;
- conexión entre experiencia y puesto;
- explicación de interés;
- narrativa;
- enfoque;
- tono;
- refuerzo de encaje.

Regla:

```text
valor incremental = bajo
→ reserva relevante
```

No implica automáticamente `NO_APTA`.

---

# 21. Calidad de la carta frente a conveniencia de inclusión

Debe distinguirse:

```text
calidad de carta
≠
conveniencia de incluirla junto al CV
```

Por tanto, el veredicto debe generar además:

```text
incluir
incluir_con_reservas
no_incluir
```

como recomendación independiente.

`recomendacion_inclusion_carta` responde únicamente a si conviene conservar la
carta junto al CV como documentación de la candidatura. No representa un
paquete, un canal, un gate de presentación ni autorización de envío.

---

# 22. Recomendación de inclusión

Combinaciones normales:

```text
APTA
→ incluir
```

```text
APTA_CON_RESERVAS
→ incluir_con_reservas
```

Pero puede existir:

```text
APTA_CON_RESERVAS
→ no_incluir
```

cuando la carta sea correcta pero su aportación sea demasiado limitada o exista una razón concreta vinculada al canal o candidatura.

`NO_APTA` implica:

```text
no_incluir
```

hasta corrección y nuevo veredicto.

---

# 23. Fuentes permitidas — principio general

El veredicto trabaja sobre una candidatura cerrada.

Puede:

- verificar;
- comparar;
- diagnosticar.

No puede:

- ampliar;
- descubrir nuevos hechos para mejorar;
- reescribir;
- reabrir estrategia.

Regla:

```text
verificar ≠ ampliar
comparar ≠ reescribir
detectar defecto ≠ corregirlo
```

---

# 24. Fuente principal común

La representación principal es:

```text
carta-presentacion.pdf
```

El veredicto debe evaluar el artefacto que verá el recruiter.

Puede consultarse:

```text
carta-presentacion.docx
```

cuando sea necesario verificar estructura o equivalencia.

---

# 25. Fuentes permitidas — Recruiter

Puede consultar:

```text
carta-presentacion.pdf
cv.pdf
candidatura.md
analisis-oferta.md
```

Solo para evaluar:

- objetivo;
- requisitos;
- encaje;
- información ya visible en CV;
- valor que añade la carta.

No debe buscar nuevos argumentos profesionales.

---

# 26. Fuentes permitidas — Editorial

Puede consultar:

```text
carta-presentacion.pdf
contenido-carta-presentacion.md
cv.pdf
guion-carta-presentacion.md
```

El guion solo sirve para comprobar intención editorial.

No autoriza reescritura.

Por defecto no consulta:

```text
datos-core-busqueda.md
web
nuevas fuentes externas
```

---

# 27. Fuentes permitidas — Auditor

Puede consultar:

```text
candidatura.md
guion-carta-presentacion.md
contenido-carta-presentacion.md
evaluacion-composicion-carta-presentacion.md
carta-presentacion.docx
carta-presentacion.pdf
cv.pdf
gates y evaluaciones previas pertinentes
```

Solo cuando exista una duda factual concreta puede consultar:

```text
datos-core-busqueda.md
```

Pero únicamente para verificar una afirmación ya presente.

Nunca para descubrir material nuevo.

---

# 28. Fuentes prohibidas por defecto

No deben utilizarse para enriquecer el veredicto:

- web abierta;
- memoria general del modelo;
- LinkedIn;
- búsquedas nuevas sobre empresa;
- nuevas fuentes sobre la oferta;
- otros CV históricos;
- cartas históricas;
- información no incorporada al flujo vigente.

---

# 29. Jerarquía de fuentes

Cada fuente manda solo en su ámbito.

```text
hechos profesionales
→ datos-core-busqueda.md

estrategia
→ candidatura.md

autorización editorial
→ guion-carta-presentacion.md

contenido semántico cerrado
→ contenido-carta-presentacion.md

representación final
→ carta-presentacion.docx / pdf

estado de composición y gates
→ evaluaciones correspondientes
```

Ninguna capa puede sustituir a otra.

---

# 30. Ausencia de información no autorizada

Está prohibido penalizar la carta porque no incluya información que nunca fue autorizada editorialmente.

Ejemplo:

```text
datos-core contiene logro X
+
guion no autoriza X
+
carta no contiene X
```

Resultado:

```text
no constituye defecto
```

El veredicto evalúa la estrategia aprobada, no todo el conocimiento disponible sobre el candidato.

---

# 31. Información nueva detectada

Si aparece una información realmente relevante que no estaba integrada:

```text
NO incorporarla
```

Debe registrarse como:

```text
incidencia_fuera_de_fase
```

y devolver el caso a la fase responsable.

Ejemplos:

```text
nuevo hecho profesional
→ datos-core → análisis → candidatura → guion → contenido
```

```text
nuevo contexto empresarial
→ análisis correspondiente → propagación
```

```text
nueva decisión editorial
→ guion
```

```text
problema de redacción
→ contenido
```

```text
problema visual
→ composición
```

Si la carta cambia como consecuencia:

```text
el veredicto debe rehacerse
```

---

# 32. Regla anti-perfeccionismo

El veredicto no busca la mejor carta imaginable.

Busca determinar si la carta existente es suficientemente sólida, coherente y competitiva.

No debe:

- inventar mejoras;
- reescribir por preferencia;
- iniciar iteraciones sin necesidad;
- penalizar alternativas estilísticas válidas.

---

# 33. Regla de retorno a fase responsable

El veredicto diagnostica.

No corrige.

Si detecta un defecto:

```text
factual
→ fase factual correspondiente

estrategia/editorial
→ guion

redacción/contenido
→ contenido

composición
→ composición

visual
→ composición / revisión humana
```

Después de una corrección material:

```text
propagación
→ nueva revisión correspondiente
→ nuevo veredicto
```

---

# 34. Estructura mínima de `veredicto-final-carta.md`

Debe incluir:

```text
1. Identificación
2. Resultado ejecutivo
3. Evaluación recruiter
4. Evaluación editorial/documental
5. Auditoría de coherencia
6. Hallazgos clasificados
7. Valor incremental frente al CV
8. Recomendación de inclusión
9. Incidencias fuera de fase
10. Gate de salida
```

---

# 35. Frontmatter mínimo del artefacto

```yaml
---
id: veredicto-final-carta-CAND-XXXX
tipo: veredicto_final_carta
version: "1.0.0"
estado: completado
candidatura: CAND-XXXX
fecha_veredicto: AAAA-MM-DD
playbook: PLAYBOOK_VEREDICTO_FINAL_CARTA
gate_entrada: GATE-CARTA-REVISION-HUMANA
estado_gate_entrada: aprobado
gate_salida: GATE-VEREDICTO-CARTA
resultado_final: APTA | APTA_CON_RESERVAS | NO_APTA
recomendacion_inclusion_carta: incluir | incluir_con_reservas | no_incluir
---
```

---

# 36. Resultado ejecutivo

Debe contener:

```yaml
resultado:
  veredicto:
  valor_incremental_frente_cv:
  efecto_sobre_candidatura:
  recomendacion_inclusion_carta:
```

Debe acompañarse de una justificación breve.

No debe convertirse en una nueva carta.

---

# 37. Hallazgos

Debe existir:

```yaml
hallazgos:
  bloqueantes: []
  reservas_relevantes: []
  reservas_menores: []
  observaciones: []
```

---

# 38. Valor incremental

Debe incluir:

```yaml
valor_incremental:
  nivel: alto | medio | bajo
  explica:
  repite_cv:
  aporta_contexto_nuevo_autorizado:
  refuerza_motivacion:
  mejora_percepcion_recruiter:
```

`aporta_contexto_nuevo_autorizado` significa valor comunicativo autorizado, no incorporación de nuevos hechos externos.

---

# 39. Incidencias fuera de fase

Debe existir:

```yaml
incidencias_fuera_de_fase: []
```

Si existe una incidencia material no resuelta:

```text
estado del veredicto = bloqueado
```

hasta corregir y propagar.

---

# 40. Gate de salida

Se propone:

```text
GATE-VEREDICTO-CARTA
```

Este gate requiere decisión humana.

El playbook nunca lo aprueba automáticamente.

Estados previstos:

```text
pendiente
aprobado
bloqueado
```

---

# 41. Reglas del gate

```text
resultado = APTA
→ habilita decisión humana
→ gate sigue pendiente
```

```text
resultado = APTA_CON_RESERVAS
→ requiere decisión humana explícita
→ gate sigue pendiente
```

```text
resultado = NO_APTA
→ no puede aprobarse sin corrección,
propagación y nuevo veredicto
```

---

# 42. Frontera con la presentación externa

La aprobación de `GATE-VEREDICTO-CARTA` cierra únicamente la evaluación de la
carta. El flujo vigente no inicia presentación externa, formularios ni
credenciales. La candidatura registra su cierre documental cuando el CV y la
carta requeridos estén aprobados, manteniendo `presentada: false` y sin módulo
activo posterior.

No son por sí solas autorización para presentar.

---

# 43. Criterios de éxito del playbook

El playbook se considera ejecutado correctamente cuando:

1. evalúa la carta final aprobada;
2. no modifica contenido ni presentación;
3. mantiene independencia de los tres roles;
4. clasifica hallazgos por severidad;
5. distingue calidad e inclusión;
6. evalúa valor incremental frente al CV;
7. no recupera hechos nuevos como mejoras;
8. respeta gates previos;
9. produce un resultado determinista;
10. deja el gate de salida pendiente de decisión humana.

---

# 44. Pruebas mínimas

## T01 — Carta correcta, útil y coherente

Esperado:

```text
APTA
```

---

## T02 — Carta correcta con poco valor incremental

Esperado:

```text
APTA_CON_RESERVAS
```

---

## T03 — Afirmación no autorizada

Esperado:

```text
NO_APTA
```

---

## T04 — Empresa o puesto incorrectos

Esperado:

```text
NO_APTA
```

---

## T05 — Contradicción relevante con CV

Esperado:

```text
NO_APTA
```

---

## T06 — Redundancias menores

Esperado:

```text
APTA
+
reserva menor u observación
```

---

## T07 — Calidad editorial mejorable pero utilizable

Esperado:

```text
APTA
o
APTA_CON_RESERVAS
```

según severidad objetiva.

---

## T08 — Gate humano previo no aprobado

Esperado:

```text
veredicto bloqueado
```

---

## T09 — Información nueva descubierta

Esperado:

```text
incidencia_fuera_de_fase
```

Sin incorporar la información.

---

## T10 — Recruiter positivo + auditor bloqueante

Esperado:

```text
NO_APTA
```

---

## T11 — Mayoría positiva con un bloqueante real

Esperado:

```text
NO_APTA
```

No existe votación por mayoría.

---

## T12 — Valor incremental bajo

Esperado:

```text
reserva relevante
→ APTA_CON_RESERVAS
```

si no existen bloqueantes.

---

## T13 — Valor incremental medio o alto

Si no existen otros problemas:

```text
APTA
→ recomendacion: incluir
```

---

## T14 — Hecho útil en datos-core no autorizado en carta

Esperado:

- no proponerlo;
- no penalizar su ausencia;
- no modificar carta;
- no generar nuevo contenido.

---

## T15 — Independencia de roles

Esperado:

- recruiter independiente;
- editorial independiente;
- auditor independiente;
- síntesis únicamente consolidativa.

---

## T16 — Resultado APTA

Esperado:

```text
GATE-VEREDICTO-CARTA = pendiente
```

Nunca aprobado automáticamente.

---

## T17 — Resultado NO_APTA

Esperado:

- bloqueo;
- retorno a fase responsable;
- corrección;
- propagación;
- nuevo veredicto.

---

# 45. Regla de generalización de defectos

Cuando aparezca un defecto real:

```text
defecto real
        ↓
identificar fase responsable
        ↓
determinar si es específico o generalizable
        ↓
si es general:
actualizar contrato/playbook correspondiente
        ↓
reflejar en template
        ↓
añadir prueba automatizable cuando sea posible
        ↓
regenerar desde fuentes canónicas
        ↓
revalidar
```

Está prohibido convertir el playbook en una colección de parches específicos de candidaturas concretas.

---

# 46. Estado inicial del playbook

Versión:

```text
1.0.0
```

Estado:

```text
en_prueba
```

No debe declararse `vigente` únicamente porque CAND-2026-020 lo supere.

---

# 47. Estrategia inicial de validación

Debe probarse, como mínimo, con:

1. un caso positivo;
2. un caso con reservas o bloqueo;
3. preferiblemente un segundo caso positivo.

CAND-2026-020 puede utilizarse como primer caso positivo.

Debe evitarse sobreajuste al caso Lidl.

---

# 48. Prohibiciones

Este playbook no puede:

- modificar `candidatura.md`;
- modificar `guion-carta-presentacion.md`;
- modificar `contenido-carta-presentacion.md`;
- modificar la carta DOCX/PDF;
- modificar el CV;
- incorporar datos nuevos;
- investigar libremente fuentes externas;
- rediseñar la candidatura;
- decidir el envío;
- aprobar automáticamente gates humanos;
- iniciar presentación externa o cambiar `presentada`;
- reescribir la carta porque exista una alternativa estilística.

---

# 49. Criterio final

`PLAYBOOK_VEREDICTO_FINAL_CARTA` no busca optimizar indefinidamente la carta.

Determina si la pieza final ya aprobada es:

- coherente;
- suficientemente sólida;
- competitivamente útil;
- conveniente como componente de la candidatura.

Su resultado debe permitir una decisión humana clara sin reabrir fases cerradas innecesariamente.

---

# 50. Historial

## 1.0.0

Primera versión.

Introduce:

- evaluación mediante tres roles independientes;
- clasificación bloqueante / reserva relevante / reserva menor / observación;
- resultados `APTA`, `APTA_CON_RESERVAS`, `NO_APTA`;
- evaluación explícita del valor incremental respecto al CV;
- separación entre calidad de la carta y conveniencia de inclusión;
- fronteras estrictas de fuentes;
- prohibición de mejoras oportunistas;
- incidencias fuera de fase;
- `GATE-VEREDICTO-CARTA` con decisión humana;
- pruebas mínimas T01–T17;
- regla de generalización de defectos.
