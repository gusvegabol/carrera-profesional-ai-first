# Bóveda de entrevista profesional

Esta bóveda existe dentro del host `carrera-ai` para construir, ordenar y hacer crecer conocimiento sobre entrevista profesional profunda.

No es PCS canónico ni una aplicación independiente. Es una bóveda local del proyecto anfitrión para preparar un futuro playbook de entrevista profesional y para estudiar la entrevista como capacidad nuclear del sistema.

## Convención de nombres de ficheros

La bóveda usa una convención semántica para distinguir el tipo de conocimiento que contiene cada documento.

La regla general es `carpeta/RAIZ_SEMANTICA_NOMBRE_DESCRIPTIVO_EN_MAYUSCULAS_SIN_TILDES.md`.

`00_proposito/` es una excepción porque contiene documentos fundacionales, no entradas catalogables. Esa carpeta conserva nombres naturales en minúscula y kebab-case.

Cuando exista riesgo de ambigüedad, las referencias a documentos físicos deben usar la ruta completa desde la raíz de la bóveda.

| Carpeta | Raíz recomendada |
| --- | --- |
| `00_proposito/` | sin prefijo semántico obligatorio |
| `01_conceptos/` | `CONCEPTO_` |
| `02_metodos/` | `METODO_` |
| `03_roles/` | `ROL_` |
| `04_patrones_de_preguntas/` | `PATRON_` |
| `05_fricciones_y_antipatrones/` | `ANTIPATRON_` o `FRICCION_` |
| `06_ejemplos/` | `EJEMPLO_` |
| `07_playbook/` | `PLAYBOOK_` o `SECCION_PLAYBOOK_` |
| `08_fuentes/` | `FUENTE_` |
| `templates/` | `TEMPLATE_` |

Ejemplos de uso de la convención:

- `01_conceptos/CONCEPTO_EXPERIENCIA_TACITA_VALIDABLE.md`
- `02_metodos/METODO_ENTREVISTA_EVENTOS_CONDUCTUALES.md`
- `03_roles/ROL_COACH_LABORAL.md`
- `04_patrones_de_preguntas/PATRON_STAR_AMPLIADO.md`
- `05_fricciones_y_antipatrones/ANTIPATRON_FORMULARIO_DISFRAZADO_DE_ENTREVISTA.md`
- `05_fricciones_y_antipatrones/FRICCION_PERSONA_MINIMIZA_SU_EXPERIENCIA.md`
- `06_ejemplos/EJEMPLO_TRANSICION_PROFESIONAL_RECONSTRUIDA.md`
- `07_playbook/PLAYBOOK_ENTREVISTA_PROFESIONAL_PROFUNDA.md`
- `08_fuentes/FUENTE_ANALISIS_ESTRUCTURAL_RECONSTRUCCION_TRAYECTORIAS.md`
- `templates/TEMPLATE_NOTA_ENTREVISTA.md`

Ejemplos de excepción fundacional:

- `00_proposito/idea-central.md`
- `00_proposito/preguntas-guia.md`
- `00_proposito/principios-iniciales.md`

## Para qué sirve

- Definir el problema de entrevista con claridad.
- Reunir conceptos, métodos, roles, patrones, fricciones y ejemplos.
- Evitar que la entrevista se convierta en un formulario o en una conversación superficial.
- Preparar material reutilizable para un playbook futuro.

## Qué contiene hoy

- `00_proposito/`: base fundacional de la bóveda.
- `01_conceptos/`: términos y distinciones clave.
- `02_metodos/`: enfoques y técnicas de entrevista.
- `03_roles/`: miradas desde distintos perfiles.
- `04_patrones_de_preguntas/`: secuencias y tipos de preguntas.
- `05_fricciones_y_antipatrones/`: errores a evitar.
- `06_ejemplos/`: casos y muestras prácticas.
- `07_playbook/`: síntesis operativa futura.
- `08_fuentes/`: referencias y material de apoyo.
- `templates/`: material heredado u opcional para reutilizar con criterio.

## Regla de uso

- Partir siempre de `00_proposito/idea-central.md`.
- No crear todavía el playbook final.
- No convertir esta bóveda en burocracia documental.
- No usarla para modificar PCS ni otras zonas del host.

## Siguiente paso recomendado

Desarrollar primero los conceptos base y los patrones de preguntas más nucleares antes de escribir el playbook.
