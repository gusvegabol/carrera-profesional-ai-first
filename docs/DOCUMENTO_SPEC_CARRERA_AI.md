# Product Spec — Carrera AI

## Perfil Profesional Accionable con equivalencia ESCO

## 1. Resumen

Carrera AI es una aplicación que ayuda a una persona a convertir su experiencia profesional real en un perfil profesional accionable, evidenciado e interoperable con estándares del mercado laboral, especialmente ESCO.

La app no se limita a generar un CV ni a listar competencias. Su objetivo es entender la trayectoria de una persona mediante entrevista asistida por IA, extraer información profesional relevante, organizarla en un modelo útil y traducirla a salidas prácticas:

* diagnóstico profesional;
* competencias demostradas;
* herramientas y tecnologías usadas;
* uso de IA aplicada al trabajo;
* evidencias;
* narrativas profesionales;
* opciones laborales futuras;
* brechas de desarrollo;
* correspondencias con ESCO en capacidades/competencias, ocupaciones y cualificaciones.

La entrevista es el mecanismo de captura.
El producto real es el Perfil Profesional Accionable.

---

## 2. Problema

Muchas personas tienen experiencia profesional valiosa, pero no saben convertirla en valor profesional visible.

Saben contar puestos, empresas o tareas, pero no siempre saben traducir eso a:

* competencias demostrables;
* evidencias defendibles;
* herramientas realmente dominadas;
* patrones de trabajo;
* posibilidades profesionales futuras;
* narrativas útiles para CV, LinkedIn o entrevistas;
* equivalencias reconocibles por sistemas de empleo.

Esto genera varios problemas:

1. La persona infravalora parte de su trayectoria.
2. Experiencias relevantes quedan ocultas porque no encajan en etiquetas laborales simples.
3. Los CV se convierten en listas pobres de puestos y tareas.
4. Las plataformas de empleo no entienden bien perfiles no lineales.
5. Las competencias inferidas no quedan vinculadas a evidencias.
6. La experiencia real no se traduce fácilmente a estándares como ESCO.
7. La orientación profesional se queda en consejos genéricos.

Carrera AI busca resolver esta desconexión entre experiencia vivida, valor profesional real y lenguaje del mercado laboral.

---

## 3. Objetivo del producto

Construir un sistema que, mediante entrevista asistida por IA, genere un Perfil Profesional Accionable capaz de transformar la trayectoria profesional de una persona en información útil para tomar decisiones de carrera, construir narrativas, detectar oportunidades y mapear competencias, ocupaciones y cualificaciones a ESCO.

Definición operativa:

> Carrera AI convierte experiencia profesional vivida en un perfil estructurado, evidenciado, narrable y traducible a estándares laborales.

---

## 4. Usuarios objetivo

### 4.1 Usuario principal

Personas que necesitan entender, ordenar o mejorar su carrera profesional.

Casos típicos:

* personas con trayectorias no lineales;
* personas con experiencia valiosa pero poco formalizada;
* trabajadores que han cambiado de sector;
* personas que quieren mejorar su CV;
* personas que quieren recolocarse;
* personas que no saben explicar bien su valor profesional;
* personas con competencias adquiridas informalmente;
* personas que quieren orientar su futuro laboral;
* personas que necesitan traducir su experiencia al lenguaje de ofertas y plataformas de empleo.

### 4.2 Usuarios secundarios futuros

* orientadores laborales;
* empresas de colocación;
* centros de formación;
* servicios públicos de empleo;
* consultores de carrera;
* equipos de RRHH;
* plataformas de matching laboral.

---

## 5. Propuesta de valor

Carrera AI permite a una persona pasar de:

```text
“He trabajado en varios sitios y no sé bien cómo vender mi experiencia.”
```

a:

```text
“Tengo una trayectoria estructurada, competencias demostradas, evidencias, herramientas, opciones profesionales realistas y equivalencias con estándares laborales como ESCO.”
```

La app aporta valor en cuatro niveles:

### 5.1 Valor personal

Ayuda a la persona a entender su propia trayectoria y reconocer valor profesional que antes no veía.

### 5.2 Valor narrativo

Convierte experiencia dispersa en relatos útiles para CV, LinkedIn, entrevistas y candidaturas.

### 5.3 Valor orientador

Detecta opciones futuras, brechas y próximos pasos realistas.

### 5.4 Valor interoperable

Traduce la información profesional a conceptos compatibles con ESCO: capacidades/competencias, ocupaciones y cualificaciones.

---

## 6. Principio central de diseño

La app no debe empezar preguntando “qué puesto buscas”.

Debe empezar entendiendo:

* qué has hecho;
* en qué contextos;
* con qué responsabilidades;
* qué problemas resolviste;
* qué herramientas usaste;
* qué aprendiste;
* qué evidencias existen;
* qué quieres y qué no quieres;
* cómo se puede traducir eso a lenguaje profesional y estándar.

La app no debe producir etiquetas sin evidencia.

Toda competencia, ocupación candidata o equivalencia ESCO debe conservar trazabilidad hacia la experiencia que la originó.

---

## 7. Modelo de información principal

El núcleo del producto es el Perfil Profesional Accionable.

### 7.1 Perfil Profesional Accionable

Entidad principal que representa el valor profesional estructurado de una persona.

Debe incluir:

1. Trayectoria.
2. Experiencias significativas.
3. Competencias demostradas.
4. Herramientas, tecnologías y sistemas.
5. IA aplicada al trabajo.
6. Evidencias.
7. Patrones profesionales.
8. Preferencias y restricciones.
9. Opciones futuras.
10. Narrativas profesionales.
11. Brechas y necesidades de desarrollo.
12. Preguntas pendientes.
13. Correspondencia ESCO.

---

## 8. Capas del perfil

### 8.1 Trayectoria

Representación cronológica y contextual de la vida profesional.

Debe capturar:

* etapas o bloques profesionales;
* puestos;
* sectores;
* empresas o contextos;
* periodos aproximados;
* simultaneidades, como estudiar mientras se trabaja;
* cambios de rol;
* transiciones;
* rupturas;
* retornos;
* reconversiones.

Ejemplo:

```text
Etapa 1 — Construcción / obra / inmobiliaria
- Mozo operario.
- Conductor de camiones para obra.
- Vendedor inmobiliario coincidiendo con finalización de FP.

Etapa 2 — Administración en asesoría
- Técnico administrativo.
- Gestión documental, fiscal, laboral o contable.

Etapa 3 — Trabajo autónomo
- Actividad propia.
- Gestión comercial, operativa y económica.

Etapa 4 — Administración en Rent Car
- Técnico administrativo en entorno operativo.
```

La trayectoria no es un CV.
Es la estructura temporal que permite entender evolución y contexto.

---

### 8.2 Experiencias significativas

Episodios concretos con valor profesional.

Cada experiencia debe recoger:

* contexto;
* situación o problema;
* acción propia;
* dificultad;
* resultado;
* aprendizaje;
* evidencia;
* competencias candidatas derivadas;
* herramientas usadas;
* posible relación con ESCO.

Ejemplo:

```text
Experiencia:
Terminó FP mientras trabajaba y realizó transición desde construcción hacia administración.

Valor profesional posible:
Capacidad de compatibilizar formación y trabajo, reconversión profesional, aprendizaje aplicado, disciplina sostenida.

Evidencia:
Cambio real de sector y acceso posterior a puesto administrativo.
```

---

### 8.3 Competencias demostradas

Competencias inferidas a partir de evidencias.

Cada competencia debe incluir:

* nombre interno;
* descripción en lenguaje humano;
* evidencias asociadas;
* experiencias origen;
* nivel de confianza;
* alcance;
* límites;
* validación por la persona;
* posible equivalencia ESCO.

Ejemplo:

```yaml
competencia: adaptación sectorial
descripcion: capacidad para trasladar aprendizajes y hábitos de trabajo entre sectores distintos
evidencias:
  - paso de construcción a administración
  - paso de asesoría a Rent Car
confianza: media
estado: candidata
```

---

### 8.4 Herramientas, tecnologías y sistemas

La app debe recoger herramientas de forma rica, no como listado plano.

Cada herramienta debe incluir:

* nombre;
* categoría;
* contexto de uso;
* tarea realizada;
* nivel estimado;
* frecuencia;
* vigencia;
* evidencia;
* transferibilidad;
* relación con competencias.

Categorías:

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

Ejemplo:

```yaml
herramienta: Excel
categoria: ofimática
contexto: administración / control interno
uso: seguimiento, cálculo, listados, control documental
nivel: operativo
vigencia: actual
transferibilidad: alta
```

---

### 8.5 IA aplicada al trabajo

La IA debe ser una dimensión propia.

No basta con saber si la persona usa herramientas de IA. Hay que entender cómo las usa.

Debe recoger:

* herramientas de IA utilizadas;
* tareas apoyadas por IA;
* frecuencia;
* nivel de autonomía;
* calidad del uso;
* capacidad de validación;
* integración en procesos;
* impacto en productividad;
* impacto en aprendizaje;
* impacto en toma de decisiones;
* riesgos conocidos;
* límites éticos o de confidencialidad.

Ejemplo:

```yaml
ia_aplicada:
  herramienta: ChatGPT
  uso: análisis de documentación, generación de prompts, revisión de estructuras, apoyo a decisiones
  nivel: avanzado
  evidencia: uso coordinado con CODEX, Notion, Drive y PCS
  criterio_validacion: revisión humana y trazabilidad
```

---

### 8.6 Evidencias

La evidencia sostiene el perfil.

Cada evidencia debe incluir:

* afirmación que sostiene;
* experiencia origen;
* tipo de evidencia;
* fuerza;
* validación;
* dudas;
* fuente.

Tipos posibles:

* relato directo;
* resultado observable;
* documento;
* herramienta creada;
* cambio laboral real;
* validación externa;
* comparación;
* responsabilidad asumida.

Ejemplo:

```yaml
evidencia: cambio de mozo operario a conductor de camiones
sostiene:
  - responsabilidad operativa
  - confianza adquirida en entorno de obra
fuerza: media
validacion_usuario: pendiente
```

---

### 8.7 Patrones profesionales

Patrones recurrentes en la forma de trabajar.

Ejemplos:

* aprende trabajando;
* se adapta por necesidad;
* consolida después de experimentar;
* combina formación y empleo;
* transforma herramientas en sistemas;
* se mueve entre sectores;
* asume responsabilidad práctica;
* necesita estructura para reducir incertidumbre.

Estos patrones ayudan a orientar mejor que una simple lista de competencias.

---

### 8.8 Preferencias y restricciones

La orientación necesita condiciones reales.

Debe recoger:

* qué quiere hacer;
* qué no quiere hacer;
* salario mínimo;
* movilidad;
* disponibilidad;
* tolerancia al riesgo;
* preferencia por estabilidad o autonomía;
* tipo de entorno deseado;
* trato con personas;
* disposición a formación;
* restricciones personales o familiares si la persona decide compartirlas.

---

### 8.9 Opciones futuras

Hipótesis profesionales razonadas.

Cada opción debe incluir:

* ocupación o familia ocupacional;
* por qué encaja;
* evidencias a favor;
* competencias necesarias;
* herramientas relevantes;
* brechas;
* riesgos;
* siguientes pasos;
* equivalencias ESCO posibles.

Ejemplo:

```yaml
opcion: administrativo de operaciones
encaje: experiencia administrativa + adaptación sectorial + entorno operativo Rent Car
brechas: confirmar herramientas sectoriales y nivel de Excel
esco_ocupacion_candidata:
estado: candidata
```

---

### 8.10 Narrativas profesionales

Salidas comunicables.

La app debe poder generar:

* resumen profesional;
* titular profesional;
* extracto de CV;
* perfil de LinkedIn;
* respuesta a “háblame de ti”;
* explicación de cambios de sector;
* relato de reconversión;
* relato de etapa autónoma;
* argumentario para entrevista;
* carta de candidatura orientada a oferta.

Las narrativas deben derivar de evidencias, no de adornos.

---

### 8.11 Brechas y necesidades de desarrollo

La app debe comparar perfil actual con opciones futuras.

Debe detectar:

* competencias débiles;
* herramientas faltantes;
* cualificaciones necesarias;
* evidencias insuficientes;
* experiencia no demostrada;
* narrativa confusa;
* requisitos de ocupaciones objetivo;
* próximos pasos.

---

### 8.12 Preguntas pendientes

El perfil debe conservar incertidumbre.

Ejemplos:

* falta confirmar herramientas usadas en asesoría;
* falta diferenciar tareas administrativas de tareas contables;
* falta validar si la etapa autónoma debe narrarse como emprendimiento, aprendizaje o riesgo;
* falta mapear ocupaciones ESCO con confianza suficiente;
* falta saber preferencias actuales de la persona.

---

### 8.13 Correspondencia ESCO

Capa de interoperabilidad.

Debe incluir correspondencias candidatas con:

* capacidades / competencias;
* ocupaciones;
* cualificaciones.

Cada correspondencia debe tener:

* concepto interno origen;
* tipo ESCO;
* etiqueta ESCO candidata;
* URI o código ESCO;
* evidencia origen;
* confianza;
* estado;
* dudas;
* validación.

Estados:

```text
candidato
validado
rechazado
pendiente_revision
pendiente_evidencia
```

Niveles de confianza:

```text
alta
media
baja
```

Ejemplo:

```yaml
esco_mapping:
  tipo: skill_or_competence
  competencia_interna: gestión administrativa documental
  esco_label_candidata:
  esco_uri:
  evidencia_origen:
    - técnico administrativo en asesoría
    - técnico administrativo en Rent Car
  confianza: media
  estado: candidato
  dudas:
    - confirmar tareas concretas
    - confirmar herramientas usadas
```

---

## 9. Flujo principal de usuario

### 9.1 Onboarding

Objetivo: crear el caso y explicar el propósito.

La app debe comunicar:

* no es un test;
* no es solo un generador de CV;
* la entrevista busca extraer valor profesional real;
* la persona podrá revisar y validar;
* las equivalencias ESCO serán candidatas hasta validación.

Datos mínimos:

* alias o nombre visible;
* situación actual;
* objetivo inicial;
* disponibilidad para entrevista;
* consentimiento de uso de datos.

---

### 9.2 Entrevista de trayectoria

Objetivo: construir una cronología inicial.

La IA pregunta por:

* primeros trabajos;
* formación;
* cambios de sector;
* puestos relevantes;
* simultaneidades;
* etapas autónomas;
* interrupciones;
* situación actual.

Salida:

* línea de trayectoria inicial;
* bloques profesionales;
* preguntas pendientes.

---

### 9.3 Entrevista de experiencias significativas

Objetivo: detectar episodios con valor profesional.

La IA explora:

* momentos difíciles;
* logros;
* cambios de rol;
* aprendizajes;
* herramientas usadas;
* responsabilidades;
* resultados.

Salida:

* experiencias significativas;
* competencias candidatas;
* evidencias.

---

### 9.4 Extracción de competencias y herramientas

Objetivo: convertir experiencias en capacidades demostradas.

Salida:

* competencias internas;
* herramientas y sistemas;
* IA aplicada;
* evidencias;
* nivel de confianza.

---

### 9.5 Mapeo ESCO candidato

Objetivo: traducir el perfil al lenguaje estándar.

Proceso:

1. Extraer términos candidatos.
2. Buscar conceptos ESCO relacionados.
3. Proponer correspondencias.
4. Mostrar justificación.
5. Marcar confianza.
6. Pedir validación o revisión.

Salida:

* competencias ESCO candidatas;
* ocupaciones ESCO candidatas;
* cualificaciones relacionadas;
* brechas.

---

### 9.6 Revisión del perfil

Objetivo: que la persona valide, corrija o matice.

La app debe permitir:

* aceptar;
* rechazar;
* corregir;
* añadir evidencia;
* marcar como pendiente;
* pedir una nueva entrevista de profundidad.

---

### 9.7 Generación de salidas

Objetivo: convertir perfil en utilidad práctica.

Salidas posibles:

* diagnóstico profesional;
* CV base;
* perfil LinkedIn;
* resumen profesional;
* candidatura orientada a oferta;
* preparación de entrevista;
* mapa de brechas;
* opciones profesionales;
* plan de desarrollo;
* equivalencias ESCO exportables.

---

## 10. Funcionalidades MVP

### 10.1 Incluido en MVP

El MVP debe centrarse en demostrar que Carrera AI puede construir un perfil útil a partir de entrevista.

Funcionalidades mínimas:

1. Crear perfil profesional.
2. Realizar entrevista guiada de trayectoria.
3. Registrar experiencias significativas.
4. Extraer competencias candidatas con evidencia.
5. Registrar herramientas y sistemas.
6. Registrar uso de IA aplicada.
7. Proponer primeras opciones profesionales.
8. Generar narrativa profesional inicial.
9. Detectar brechas y preguntas pendientes.
10. Proponer correspondencias ESCO candidatas con estado y confianza.
11. Permitir validación humana básica.

---

### 10.2 Fuera del MVP

No incluir inicialmente:

* matching automático con ofertas reales;
* integración directa con InfoJobs, Randstad u otras plataformas;
* scoring laboral cerrado;
* recomendaciones automáticas definitivas;
* base de datos compleja multiusuario;
* frontend sofisticado;
* edición colaborativa;
* analítica avanzada;
* certificación formal de competencias;
* validación oficial de cualificaciones.

---

## 11. Requisitos funcionales

### RF-01 — Crear perfil

El sistema debe permitir crear un Perfil Profesional Accionable para una persona.

### RF-02 — Capturar trayectoria

El sistema debe permitir registrar una cronología profesional estructurada.

### RF-03 — Detectar experiencias significativas

El sistema debe identificar episodios profesionales relevantes durante la entrevista.

### RF-04 — Extraer competencias candidatas

El sistema debe inferir competencias a partir de experiencias, nunca sin evidencia.

### RF-05 — Registrar herramientas

El sistema debe capturar herramientas, tecnologías, sistemas, maquinaria, procedimientos y normativa usados.

### RF-06 — Registrar IA aplicada

El sistema debe capturar usos de IA como dimensión propia.

### RF-07 — Gestionar evidencias

Cada afirmación relevante debe poder vincularse a una o varias evidencias.

### RF-08 — Proponer opciones futuras

El sistema debe generar hipótesis profesionales razonadas.

### RF-09 — Generar narrativas

El sistema debe producir textos profesionales reutilizables.

### RF-10 — Detectar brechas

El sistema debe detectar diferencias entre perfil actual y opciones objetivo.

### RF-11 — Mapear a ESCO

El sistema debe proponer correspondencias candidatas con ESCO.

### RF-12 — Validar o rechazar inferencias

La persona debe poder validar, corregir o rechazar competencias, evidencias y equivalencias.

### RF-13 — Conservar incertidumbre

El sistema debe registrar preguntas pendientes y niveles de confianza.

---

## 12. Requisitos no funcionales

### RNF-01 — Trazabilidad

Toda inferencia debe poder rastrearse hasta una experiencia o evidencia.

### RNF-02 — Explicabilidad

La app debe explicar por qué propone una competencia, narrativa, opción o equivalencia ESCO.

### RNF-03 — Prudencia

El sistema no debe presentar inferencias como verdades cerradas.

### RNF-04 — Privacidad

Los datos profesionales personales deben tratarse con especial cuidado.

### RNF-05 — Interoperabilidad

El modelo debe prepararse para usar estándares como ESCO mediante API o datasets descargados.

### RNF-06 — Revisión humana

Las equivalencias laborales relevantes deben admitir validación humana.

### RNF-07 — Evolución

El perfil debe poder crecer, corregirse y actualizarse con nuevas entrevistas o experiencias.

---

## 13. Modelo de datos conceptual

```text
PerfilProfesional
  id_perfil
  persona_alias
  situacion_actual
  objetivo_inicial
  trayectoria[]
  experiencias[]
  competencias[]
  herramientas[]
  ia_aplicada[]
  evidencias[]
  patrones[]
  preferencias_restricciones
  opciones_futuras[]
  narrativas[]
  brechas[]
  preguntas_pendientes[]
  esco_mappings[]
```

### Experiencia

```text
Experiencia
  id_experiencia
  etapa
  contexto
  periodo
  descripcion
  dificultad
  accion
  resultado
  aprendizaje
  evidencias[]
  competencias_candidatas[]
  herramientas[]
```

### Competencia

```text
Competencia
  id_competencia
  etiqueta_interna
  descripcion
  evidencias[]
  experiencias_origen[]
  confianza
  estado_validacion
  esco_mappings[]
```

### Herramienta

```text
Herramienta
  id_herramienta
  nombre
  categoria
  contexto_uso
  tarea
  nivel_estimado
  frecuencia
  vigencia
  evidencia
  transferibilidad
```

### IA aplicada

```text
IAAplicada
  id_ia
  herramienta
  uso
  contexto
  frecuencia
  nivel
  impacto
  validacion
  riesgos
```

### ESCO Mapping

```text
ESCO_Mapping
  id_mapping
  tipo
  concepto_interno
  esco_label
  esco_uri
  evidencia_origen
  confianza
  estado
  dudas
```

---

## 14. Experiencia de usuario esperada

La experiencia debe sentirse como una conversación inteligente, no como un formulario.

La IA debe:

* preguntar con contexto;
* detectar valor oculto;
* pedir ejemplos concretos;
* no forzar jerga profesional;
* traducir lenguaje cotidiano a lenguaje laboral;
* mostrar inferencias para validación;
* explicar correspondencias ESCO;
* generar salidas prácticas.

La persona debe sentir:

```text
“Ahora entiendo mejor lo que sé hacer.”
“Ahora puedo explicar mejor mi trayectoria.”
“Ahora veo opciones que antes no veía.”
“Ahora mi experiencia tiene traducción al lenguaje del mercado laboral.”
```

---

## 15. Métricas de éxito

### Métricas de valor del usuario

* La persona reconoce el perfil como representativo.
* La persona descubre competencias que no sabía expresar.
* La persona puede usar una narrativa generada.
* La persona identifica opciones futuras plausibles.
* La persona entiende mejor sus brechas.

### Métricas de calidad del perfil

* Porcentaje de competencias con evidencia.
* Porcentaje de herramientas con contexto de uso.
* Porcentaje de inferencias validadas.
* Número de preguntas pendientes relevantes.
* Nivel de trazabilidad de narrativas.

### Métricas ESCO

* Número de competencias internas con candidato ESCO.
* Número de ocupaciones candidatas.
* Porcentaje de mappings aceptados/rechazados.
* Confianza media de mappings.
* Casos donde falta información para mapear.

---

## 16. Riesgos

### Riesgo 1 — Generar humo profesional

La IA puede producir competencias bonitas sin evidencia.

Mitigación: toda competencia debe estar vinculada a experiencia y evidencia.

### Riesgo 2 — Mapear mal a ESCO

Una equivalencia ESCO incorrecta puede distorsionar el perfil.

Mitigación: estados de confianza, revisión humana y explicación del mapping.

### Riesgo 3 — Sobrediseñar artefactos

Diseñar documentos, mapas o carpetas antes de validar el valor de producto.

Mitigación: priorizar modelo de información y salidas útiles.

### Riesgo 4 — Convertir la entrevista en formulario

Demasiada estructura puede hacer que la experiencia sea rígida.

Mitigación: conversación guiada con extracción progresiva.

### Riesgo 5 — Invadir privacidad

La carrera profesional puede incluir información sensible.

Mitigación: minimización de datos, consentimiento y control del usuario.

### Riesgo 6 — Recomendaciones demasiado fuertes

La app podría parecer que decide por la persona.

Mitigación: presentar opciones razonadas, no decisiones cerradas.

---

## 17. Hipótesis principales a validar

1. Una entrevista guiada puede construir una trayectoria profesional suficientemente estructurada.
2. La persona reconoce como válido el perfil generado.
3. Las competencias extraídas pueden vincularse a evidencias.
4. Las herramientas usadas pueden capturarse con contexto suficiente.
5. El uso de IA aplicada puede convertirse en ventaja profesional detectable.
6. La app puede proponer correspondencias ESCO útiles, aunque sean candidatas.
7. Las narrativas generadas son reutilizables por la persona.
8. El perfil ayuda a identificar opciones futuras realistas.

---

## 18. MVP recomendado

El MVP debería centrarse en un único flujo:

```text
Entrevista de trayectoria
→ Perfil Profesional Accionable inicial
→ Competencias + evidencias
→ Herramientas + IA aplicada
→ Narrativa profesional inicial
→ ESCO mappings candidatos
→ Preguntas pendientes
```

No hace falta construir todavía una app completa.

Basta con demostrar que, para una persona real, el sistema puede generar un perfil que sea:

* reconocible;
* útil;
* evidenciado;
* narrable;
* parcialmente mapeable a ESCO;
* mejor que un CV tradicional como base de orientación.

---

## 19. Salida mínima de MVP

La salida mínima del MVP debe ser un documento o vista con:

1. Resumen profesional.
2. Línea de trayectoria.
3. Experiencias significativas.
4. Competencias demostradas.
5. Herramientas, tecnologías y sistemas.
6. IA aplicada.
7. Evidencias.
8. Opciones futuras.
9. Narrativa reutilizable.
10. Brechas.
11. Preguntas pendientes.
12. Correspondencias ESCO candidatas.

---

## 20. Definición de éxito

El MVP tiene éxito si una persona puede decir:

> “Este perfil representa mejor mi valor profesional que mi CV actual, me ayuda a explicar mi trayectoria y me ofrece una primera traducción útil hacia competencias, ocupaciones o cualificaciones reconocibles en el mercado laboral.”

---

## 21. Decisiones pendientes

1. Qué parte del perfil será documento y qué parte será dato estructurado.
2. Si ESCO se integrará mediante API, dataset descargado o búsqueda asistida.
3. Cómo validar mappings ESCO.
4. Cómo guardar evidencias sin almacenar información sensible innecesaria.
5. Cómo versionar cambios en el perfil.
6. Qué salida se prioriza primero: CV, orientación, matching, narrativa o ESCO.
7. Cómo medir la calidad de una entrevista de cobertura.
8. Si la app debe funcionar primero como asistente conversacional, panel visual o generador de documentos.
