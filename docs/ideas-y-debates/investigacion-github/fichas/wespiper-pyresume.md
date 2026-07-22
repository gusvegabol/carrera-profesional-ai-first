# Ficha técnica: `wespiper/pyresume`

## Identificación

**Repositorio:** `wespiper/pyresume`  
**URL:** <https://github.com/wespiper/pyresume>  
**Fecha de revisión:** 2026-07-20  
**Última actividad observada:** no comprobada con fecha exacta; el repositorio muestra 2 commits.  
**Licencia:** MIT.  
**Área funcional:** importación y parsing de CV.  
**Objeto estudiado:** componente Python de parsing, modelo de datos y puntuación de confianza.  
**Nivel de evidencia:** inspección técnica documental; experimento no ejecutado.  
**Estado de la ficha:** revisada

## Pregunta de investigación

¿Puede un parser local de CV aportar contexto inicial a Carrera AI-First sin
convertir el CV en la fuente principal de la trayectoria?

## Problema que resuelve

El repositorio presenta una librería Python para extraer información
estructurada de CV en PDF, DOCX y TXT. Declara extracción de contacto,
experiencia, educación, habilidades y otras secciones, además de puntuaciones
de confianza por sección.

El README muestra una arquitectura modular con parser principal, modelos,
extractores por formato y utilidades de fechas y teléfonos.

## Relación con Carrera AI-First

Puede servir como capa opcional de importación previa para:

- detectar nombres de empresas, puestos, periodos y herramientas ya escritos;
- preparar preguntas de contraste y omisiones;
- evitar pedir a la persona que repita información documental básica.

No debe sustituir la entrevista, porque un CV no contiene necesariamente
experiencia tácita, simultaneidades, decisiones ni evidencias suficientes.

## Stack y arquitectura

**Lenguajes:** Python.  
**Frameworks y librerías principales:** `pdfplumber`, `python-docx` y utilidades
de parsing declaradas en el README.  
**Servicios externos:** opcionalmente OpenAI o Anthropic para formatos
complejos, según el README.  
**Infraestructura:** ejecución local y dependencias Python.  
**Arquitectura:** `ResumeParser`, modelos de dominio, extractores PDF/DOCX/TXT
y utilidades de fechas, patrones y teléfonos.

El README también usa el nombre `LeverParser` y los comandos de instalación
`leverparser`, mientras el repositorio se denomina `pyresume`; esta
inconsistencia debe verificarse antes de cualquier prueba.

## Componentes potencialmente reutilizables

| Tipo | Componente o patrón | Ubicación | Qué aporta | ¿Separable? |
| --- | --- | --- | --- | --- |
| Código | Parser por formato | `pyresume/` | Aísla la lectura inicial de PDF, DOCX y TXT. | parcial |
| Modelo | Entidades `Resume`, `Experience`, `Education` | `models/resume.py` | Puede inspirar una entrada documental, no el perfil completo. | parcial |
| Patrón | Puntuación de confianza por sección | ejemplos de confianza | Hace visibles resultados inciertos del parsing. | sí |
| Flujo | Importar → estructurar → exportar JSON | README | Puede servir como preprocesamiento controlado. | sí |

## Modelo de datos, prompts y flujos

El modelo parte de un CV estructurado en contacto, experiencia, educación,
habilidades, proyectos y certificaciones. La puntuación de confianza se asocia
a las secciones extraídas.

No se ha comprobado una capa conversacional o de validación humana equivalente
a la de Carrera AI-First. Su valor potencial está en producir hipótesis de
datos para que la persona las confirme, complete o rechace.

## Diferencias y límites frente a Carrera AI-First

- Parte de un documento, mientras Carrera AI-First parte de la trayectoria
  vivida y de la conversación.
- Extraer una habilidad no demuestra que exista una competencia validada.
- La precisión declarada en el README no sustituye una prueba con CV variados.
- La inconsistencia entre `pyresume`, `LeverParser` y `leverparser` introduce
  incertidumbre sobre el estado real del paquete.

## Evaluación

| Criterio | Puntuación | Justificación |
| --- | ---: | --- |
| Encaje funcional | 4/5 | Resuelve una necesidad lateral clara de importación. |
| Reutilización real | 3/5 | La estructura parece modular, pero aún no se ha probado el paquete. |
| Calidad arquitectónica | 4/5 | El README describe separación por extractores, modelos y utilidades. |
| Madurez | 2/5 | Solo se observan 2 commits y no hay evidencia suficiente de mantenimiento prolongado. |
| Dependencias | 3/5 | Las dependencias son manejables, pero cambian según el formato y el modo LLM. |
| Licencia | 5/5 | MIT clara. |
| Coste de integración | 3/5 | La prueba puede ser barata; la integración fiable exige evaluar formatos. |
| Riesgo de desvío | 4/5 | Es una capa acotada si se mantiene fuera del núcleo conversacional. |
| Valor de aprendizaje | 4/5 | Ayuda a definir cómo tratar fuentes previas y confianza de extracción. |

## Riesgos

- **Dependencias:** compatibilidad real de PDF/DOCX y del modo LLM.
- **Calidad:** actividad limitada y nomenclatura interna inconsistente.
- **Privacidad:** los CV contienen datos personales; la importación debe ser
  local y opcional.
- **Desvío:** el parser podría convertirse en el centro del producto si se
  confunde extracción con descubrimiento de trayectoria.

## Experimento mínimo propuesto

**Hipótesis:** un parser local puede preparar preguntas útiles sin cerrar el
perfil ni añadir afirmaciones no validadas.

**Alcance:** comparar la salida estructurada de un CV sintético en PDF, DOCX y
TXT con el modelo documental de Carrera AI-First.

**Exclusiones:** no usar datos reales, no activar integraciones LLM y no
incorporar código al host.

**Datos de prueba:** CV sintético con dos etapas, una simultaneidad, una
herramienta y una experiencia tácita omitida deliberadamente.

**Resultado observable:** porcentaje de campos correctamente extraídos,
confianzas, preguntas que el parser permite generar y elementos que la
entrevista debe descubrir desde cero.

**Coste estimado:** bajo/medio; requiere preparar fixtures y revisar la
inconsistencia del paquete.

## Resultado del experimento

**Resultado:** pendiente.  
**Evidencia:** pendiente de crear `EXP-002-importacion-de-cv/`.  
**Problemas encontrados:** nomenclatura del paquete y actividad limitada.  
**Aprendizaje:** la utilidad potencial está en preparar contexto y preguntas,
no en producir el perfil.

## Decisión preliminar

**Decisión:** prototipar.

**Justificación:** es el candidato más directamente relacionado con la
importación de CV, pero necesita una prueba acotada antes de evaluar su valor
real.

**Qué podría incorporarse:** el patrón de extracción modular y la confianza
por campo o sección.

**Qué no debe incorporarse:** el CV como fuente de verdad ni una extracción
automática presentada como competencia.

**Siguiente paso:** delimitar `EXP-002-importacion-de-cv`.

## Trazabilidad

- Documento general: [`INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md`](../INVESTIGACION_GITHUB_CARRERA_AI_FIRST.md).
- Flujo: [`FLUJO_INVESTIGACION_GITHUB.md`](../FLUJO_INVESTIGACION_GITHUB.md).
- Sesión PCS: `sesion-20260720-1242-investigacion-github-carrera-ai-first`.
- Experimento: `experimentos/EXP-002-importacion-de-cv/`.

## Fuentes consultadas

- [Repositorio y README](https://github.com/wespiper/pyresume).
- [LICENSE](https://github.com/wespiper/pyresume/blob/main/LICENSE).

## Revisión final

- [x] Licencia comprobada.
- [x] Hechos, inferencias y recomendaciones separados.
- [x] Objeto y nivel de evidencia registrados.
- [x] Riesgo de desvío evaluado.
- [x] No se presenta la ficha como autorización de integración.
