# Perfil Profesional Accionable y equivalencia ESCO

## Base conceptual para el próximo playbook de cobertura profesional

## Estado del documento

Documento de diseño conceptual.

Este documento redefine el objetivo de la cobertura profesional dentro de `Carrera Profesional AI-First`.

La cobertura profesional no debe entenderse solo como una forma de hacer más entrevistas ni como una colección de zonas, mapas o artefactos. Debe entenderse como el proceso de construcción de un perfil profesional accionable, evidenciado e interoperable con estándares del mercado laboral, especialmente ESCO.

---

## 1. Punto de partida

La entrevista profunda ya ha validado una hipótesis importante:

> Una conversación bien guiada puede extraer una competencia profesional real, defendible y con evidencia.

Esa validación pertenece al nivel de extracción profunda.

Pero la cobertura profesional apunta a un objetivo superior:

> Construir una representación útil de la trayectoria profesional de una persona para que Carrera AI pueda ayudarla a entender su valor, narrarlo, orientarlo, compararlo con el mercado laboral y traducirlo a estándares como ESCO.

Por tanto, la entrevista deja de ser el centro del sistema.

La entrevista es el método de extracción.

El centro del sistema pasa a ser el perfil profesional accionable.

---

## 2. Objetivo del Perfil Profesional Accionable

El Perfil Profesional Accionable es la representación estructurada, evidenciada y utilizable del valor profesional de una persona.

Su objetivo es convertir experiencia vivida en información profesional que pueda generar decisiones, orientación, narrativa y equivalencias laborales.

Fórmula base:

```text
Experiencia vivida
→ información profesional estructurada
→ valor profesional interpretable
→ equivalencia con mercado laboral
→ decisiones y acciones de carrera
```

El perfil debe permitir responder preguntas como:

* qué ha hecho profesionalmente la persona;
* qué sabe hacer;
* dónde lo ha demostrado;
* con qué herramientas trabaja o ha trabajado;
* cómo usa o puede usar IA;
* qué competencias tiene evidencia suficiente;
* qué ocupaciones equivalentes pueden derivarse;
* qué cualificaciones formales o informales son relevantes;
* qué opciones profesionales futuras tienen sentido;
* qué brechas existen para determinados objetivos;
* cómo puede narrarse profesionalmente su trayectoria.

---

## 3. Relación con ESCO

ESCO debe considerarse una referencia estratégica del producto.

Carrera AI no debe limitarse a producir etiquetas internas como “resiliencia”, “gestión administrativa” o “adaptación sectorial”.

Debe poder traducir la información extraída en entrevista a conceptos equivalentes o candidatos dentro de ESCO:

* capacidades / competencias;
* cualificaciones;
* ocupaciones.

El objetivo no es asignar códigos ESCO de forma automática y definitiva.

El objetivo es generar una capa de correspondencia trazable:

```text
Relato de entrevista
→ experiencia significativa
→ evidencia profesional
→ competencia interpretada
→ candidato ESCO
→ estado de validación
```

---

## 4. Principio de trazabilidad

Ninguna equivalencia ESCO debe aparecer como verdad sin trazabilidad.

Cada asignación debe conservar:

* qué fragmento o experiencia de entrevista la originó;
* qué competencia interna se infirió;
* qué concepto ESCO se propone;
* con qué nivel de confianza;
* qué dudas existen;
* si está validado, pendiente, rechazado o necesita revisión humana.

Ejemplo:

```yaml
competencia_interna: gestión administrativa documental
evidencia_origen: experiencia como técnico administrativo en asesoría y empresa de rent car
esco_tipo: skill_or_competence
esco_concepto_candidato:
esco_uri:
confianza: media
estado: candidato
dudas:
  - confirmar herramientas concretas utilizadas
  - diferenciar gestión administrativa general de gestión contable/laboral/fiscal
```

---

## 5. Capas mínimas del Perfil Profesional Accionable

El perfil debe recoger al menos estas capas:

### 5.1 Trayectoria

Cronología profesional estructurada.

Debe recoger:

* etapas o bloques profesionales;
* puestos desempeñados;
* sectores;
* transiciones;
* periodos aproximados;
* simultaneidades relevantes, como estudiar mientras se trabaja;
* cambios de rol;
* rupturas, retornos o reconversiones.

No debe ser una simple lista de empleos.

Debe permitir entender la evolución profesional de la persona.

---

### 5.2 Experiencias significativas

Episodios concretos con valor profesional.

Una experiencia significativa debe recoger:

* contexto;
* dificultad;
* acción propia;
* resultado;
* aprendizaje;
* evidencia;
* posible valor profesional derivado.

Estas experiencias son la materia prima principal para extraer competencias defendibles.

---

### 5.3 Competencias demostradas

Competencias inferidas a partir de evidencias reales.

Cada competencia debe distinguir:

* etiqueta interna;
* descripción humana;
* evidencias;
* nivel de confianza;
* alcance;
* límites;
* posible equivalencia ESCO;
* estado de validación.

Una competencia no debe aceptarse solo porque “suena bien”.

Debe poder defenderse.

---

### 5.4 Herramientas, tecnologías y sistemas

Relación de herramientas usadas por la persona, pero no como listado plano.

Debe recoger:

* herramienta;
* categoría;
* contexto de uso;
* tarea realizada;
* nivel estimado;
* frecuencia;
* vigencia;
* evidencia;
* transferibilidad.

Categorías posibles:

* ofimática;
* software sectorial;
* ERP / CRM / gestión interna;
* comunicación;
* organización;
* programación;
* automatización;
* integraciones;
* maquinaria;
* vehículos;
* equipos físicos;
* normativa;
* procedimientos.

---

### 5.5 IA aplicada al trabajo

La IA merece una capa propia.

No debe quedar escondida dentro de herramientas.

Debe recoger:

* herramientas de IA utilizadas;
* tareas en las que se usan;
* frecuencia;
* autonomía;
* calidad del uso;
* capacidad de validación;
* impacto en productividad;
* impacto en aprendizaje;
* impacto en toma de decisiones;
* riesgos conocidos;
* límites éticos o de confidencialidad.

No interesa solo saber si la persona usa IA.

Interesa saber cómo la integra en su forma de trabajar.

---

### 5.6 Evidencias

Base probatoria del perfil.

Debe recoger:

* qué afirmación profesional sostiene;
* de qué experiencia procede;
* si es directa o inferida;
* nivel de fuerza;
* validación por la persona;
* dudas pendientes.

La evidencia evita que el perfil se convierta en una colección de etiquetas aspiracionales.

---

### 5.7 Patrones profesionales

Formas recurrentes de actuar, aprender, adaptarse o resolver.

Ejemplos:

* aprende trabajando;
* se adapta por necesidad y consolida después;
* tiende a asumir responsabilidad práctica;
* transforma herramientas en sistemas;
* se mueve bien entre sectores;
* necesita estructura para reducir incertidumbre;
* combina formación y experiencia.

Estos patrones ayudan a orientar futuro, no solo a describir pasado.

---

### 5.8 Preferencias y restricciones

Información necesaria para que la orientación sea realista.

Debe recoger:

* trabajos que quiere evitar;
* condiciones mínimas;
* tolerancia al riesgo;
* disponibilidad;
* movilidad;
* salario mínimo;
* preferencia por estabilidad o autonomía;
* tipo de entorno deseado;
* nivel de trato con personas;
* disposición a formarse;
* restricciones familiares, geográficas o de salud si la persona decide aportarlas.

Sin esta capa, Carrera AI puede detectar competencias, pero no orientar bien.

---

### 5.9 Opciones profesionales futuras

Hipótesis de evolución profesional.

Cada opción debe recoger:

* ocupación o familia ocupacional posible;
* encaje con trayectoria;
* competencias que la sostienen;
* herramientas relevantes;
* brechas;
* riesgos;
* próximos pasos;
* posible correspondencia ESCO.

No deben presentarse como recomendaciones definitivas, sino como opciones razonadas.

---

### 5.10 Narrativas profesionales

Salidas reutilizables para comunicación profesional.

Debe permitir generar:

* resumen profesional;
* perfil de CV;
* perfil de LinkedIn;
* respuesta a “háblame de ti”;
* explicación de cambios de sector;
* relato de reconversión;
* argumentario para entrevista;
* justificación de brechas o etapas difíciles;
* presentación orientada a una oferta concreta.

La narrativa debe apoyarse en evidencia, no en adornos.

---

### 5.11 Brechas y necesidades de desarrollo

Diferencia entre perfil actual y objetivo profesional.

Debe recoger:

* competencias por reforzar;
* herramientas por aprender;
* cualificaciones necesarias;
* experiencia faltante;
* evidencias débiles;
* aspectos narrativos poco claros;
* requisitos de ocupaciones objetivo;
* acciones recomendadas.

---

### 5.12 Preguntas pendientes

Todo perfil debe conservar incertidumbre.

Debe recoger:

* información no explorada;
* inferencias débiles;
* equivalencias ESCO dudosas;
* experiencias que requieren más detalle;
* contradicciones;
* decisiones pendientes de la persona.

---

### 5.13 Correspondencia ESCO

Capa de interoperabilidad con mercado laboral.

Debe recoger correspondencias candidatas con:

* capacidades / competencias;
* ocupaciones;
* cualificaciones.

Cada correspondencia debe tener estado:

```text
candidato
validado
rechazado
pendiente_revision
pendiente_evidencia
```

Y nivel de confianza:

```text
alta
media
baja
```

La correspondencia ESCO no sustituye al juicio humano ni a la narrativa profesional.

La complementa.

---

## 6. Nuevo papel de la cobertura profesional

La cobertura profesional ya no debe definirse como “explorar más zonas”.

Debe definirse como:

> El proceso de extracción y estructuración suficiente de información profesional para construir un Perfil Profesional Accionable capaz de alimentar orientación, narrativa, comparación con el mercado laboral y equivalencia ESCO.

Esto cambia el foco:

```text
Antes:
entrevista → zonas → inmersiones → competencias

Ahora:
entrevista → perfil profesional accionable → evidencias → equivalencias → decisiones de carrera
```

---

## 7. Consecuencia para el próximo playbook

El próximo playbook de cobertura profesional no debe empezar preguntando:

* cuántas zonas hay;
* cómo se numeran;
* cuántos mapas existen;
* qué artefactos se crean.

Debe empezar preguntando:

* qué información necesita Carrera AI;
* qué debe extraer la entrevista;
* qué parte del perfil queda cubierta;
* qué parte queda pendiente;
* qué puede mapearse a ESCO;
* qué necesita validación;
* qué salida accionable puede generarse.

La arquitectura documental debe venir después del modelo de información.

---

## 8. Salida mínima esperada de una entrevista de cobertura

Una entrevista de cobertura debería poder producir, como mínimo:

```text
1. Cronología profesional inicial.
2. Experiencias significativas detectadas.
3. Competencias candidatas con evidencia.
4. Herramientas y sistemas usados.
5. Uso de IA aplicada al trabajo.
6. Preferencias y restricciones relevantes.
7. Primeras opciones profesionales posibles.
8. Narrativas iniciales reutilizables.
9. Brechas o preguntas pendientes.
10. Correspondencias ESCO candidatas.
```

No todas las capas tienen que quedar completas en una sesión.

Pero sí debe quedar claro qué está cubierto, qué está incompleto y qué requiere profundización.

---

## 9. Principio de diseño

La entrevista no debe producir documentos por producir documentos.

Debe producir información profesional que pueda convertirse en valor.

El criterio de éxito no es tener un mapa bonito.

El criterio de éxito es que Carrera AI pueda generar mejores decisiones, mejores narrativas, mejores equivalencias laborales y mejores próximos pasos para la persona.

---

## 10. Definición final propuesta

El Perfil Profesional Accionable es el modelo vivo de información que Carrera AI construye sobre una persona para transformar su trayectoria, experiencias, competencias, herramientas, uso de IA, evidencias, preferencias y objetivos en salidas prácticas de carrera: diagnóstico, narrativa, orientación, brechas, próximos pasos y correspondencias con estándares laborales como ESCO.

La cobertura profesional es el proceso que alimenta ese perfil.
