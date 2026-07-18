---
titulo: Propuesta de uso transversal de Obsidian en Carrera AI
version: 1.0.0
estado: propuesta_para_decision
fecha: 2026-07-17
sesion_origen: sesion-20260717-1930-debate-obsidian-proyecto-completo
---

# Propuesta de uso transversal de Obsidian en Carrera AI

## Decisión que responde esta propuesta

**¿Debe Obsidian pasar de gestionar únicamente
`boveda-entrevista-profesional/` a facilitar la consulta y el enlace del
conjunto documental del proyecto?**

Sí. Se recomienda abrir la **raíz de `carrera-ai` como una única bóveda de
Obsidian**, con una política explícita de exclusiones y una migración controlada
de su configuración y de los datos compartidos de Vault Operator. El objetivo
no es convertir todo el repositorio en el mismo tipo de documento, sino mejorar
la lectura y el enlace entre documentos que ya son complementarios.

La recomendación no es todavía una decisión PCS ni autoriza movimientos,
borrados o cambios de configuración. Si se aprueba, debe materializarse con un
plan de migración verificable.

## Base factual

- El alcance documental consultable contiene **98 archivos Markdown** fuera de
  las carpetas de herramienta excluidas; 70 viven en
  `boveda-entrevista-profesional/`, 26 en `docs/` y 2 en la raíz.
- `.pcs/` contiene documentación operativa y debe poder leerse desde la bóveda,
  pero no pierde por ello sus reglas de autoridad, privacidad ni continuidad.
- Hay cinco nombres de nota repetidos, entre ellos `README` (16 apariciones) y
  `AGENTS` (2). Por tanto, la navegación transversal necesita convenciones de
  enlace con ruta cuando el título no sea único.
- La configuración actual de Obsidian está dentro de
  `boveda-entrevista-profesional/.obsidian/` y ya incluye los plugins
  `vault-operator` y `hide-folders`.
- Vault Operator está configurado con `agentFolderPath: .vault-operator` y su
  implementación local busca primero `obsilo-shared/` en el directorio padre
  de la bóveda; usa `vault-operator-shared/` como alternativa. Al cambiar la
  raíz de la bóveda, cambia también ese directorio padre.
- `.gitignore` regula qué archivos no sigue Git; no es una regla de visibilidad
  de Obsidian. La política de exclusión de la bóveda debe existir por separado.

## Criterios de evaluación

Se comparan las alternativas con cinco criterios, ponderados para el objetivo
real de esta sesión:

| Criterio | Peso | Qué se busca |
| --- | ---: | --- |
| Consulta y enlace transversal | 30 % | Encontrar y conectar fuentes de todo el proyecto sin duplicarlas. |
| Separación de autoridad | 20 % | Distinguir producto, metodología, PCS e historial sin mezclar sus roles. |
| Riesgo de migración | 20 % | Evitar pérdida de datos, rotura de plugins o enlaces. |
| Compatibilidad operativa | 20 % | Mantener Git, Vault Operator, Codex y la estructura documental. |
| Esfuerzo sostenible | 10 % | Coste inicial y mantenimiento posterior. |

## Alternativa 1 — Mantener la bóveda localizada actual

Obsidian sigue abriendo solo `boveda-entrevista-profesional/`. El resto del
repositorio se consulta con el explorador de archivos, el editor o enlaces
externos puntuales.

**Pros**

- No requiere migración ni cambio de configuración.
- Mantiene aislados los datos de Vault Operator ya existentes.
- Reduce el riesgo de que la vista de Obsidian muestre ficheros operativos o
  históricos fuera de contexto.

**Contras**

- No responde al problema principal: los documentos de `docs/` y `.pcs/` no
  participan de la misma navegación ni del mismo grafo.
- Obliga a alternar herramientas y rutas para reconstruir el contexto global.
- Favorece enlaces frágiles o referencias en texto plano entre capas del
  proyecto.

**Valoración:** segura, pero insuficiente para el objetivo de consulta y
linkaje transversal.

## Alternativa 2 — Abrir la raíz como bóveda sin política adicional

Se abre `C:\Users\gusve\Documents\Apps\carrera-profesional-ai-first` como
bóveda y se deja que Obsidian muestre el árbol disponible tal como está.

**Pros**

- Todos los Markdown quedan inmediatamente disponibles en una sola navegación.
- Los enlaces con ruta pueden unir `docs/`, `.pcs/` y la bóveda actual sin
  duplicar archivos.
- El cambio conceptual es simple: una sola raíz documental.

**Contras**

- La interfaz se contaminaría con directorios técnicos, históricos o locales
  que no aportan lectura cotidiana.
- `.gitignore` no evita por sí solo esa contaminación visual.
- La configuración existente y las rutas de almacenamiento de Vault Operator
  pueden dejar de apuntar al lugar esperado.
- Los nombres repetidos producirían ambigüedad si se usan wikilinks sin ruta.

**Valoración:** alcanza la cobertura, pero deja demasiados riesgos sin
gobernar.

## Alternativa 3 — Bóveda transversal gobernada en la raíz **(recomendada)**

Se abre la raíz del repositorio como bóveda, pero se acompaña de una política
de navegación y migración. Se muestran las fuentes documentales relevantes;
se ocultan del explorador los directorios de configuración, cachés, datos
compartidos, artefactos temporales y cualquier otra ruta que no sea material
de lectura. La jerarquía documental continúa gobernando qué puede afirmarse o
modificarse.

**Pros**

- Resuelve el objetivo completo: una única vista para los 98 Markdown
  alcanzables, sin crear una segunda copia del conocimiento.
- Permite enlaces directos y backlinks entre metodología, definición de
  producto, decisiones, estado y sesiones.
- Mantiene visibles las fronteras: las carpetas siguen expresando su función y
  la propuesta añade una guía de autoridad, no una falsa homogeneidad.
- Reutiliza el plugin `hide-folders` que ya está instalado.
- Permite una migración reversible mediante copia de seguridad y validación
  antes de retirar configuraciones antiguas.

**Contras**

- Exige diseñar y mantener una lista de exclusiones propia de Obsidian.
- Requiere resolver las rutas de `obsilo-shared/` y
  `vault-operator-shared/` antes de usar el nuevo contexto de Vault Operator.
- Obliga a disciplinar los wikilinks con ruta para nombres no únicos.
- Añade una breve fase de verificación funcional, especialmente para el
  plugin, enlaces `obsidian://` y búsquedas.

**Valoración:** es la mejor relación entre cobertura documental, seguridad y
sostenibilidad.

## Alternativa 4 — Crear una bóveda espejo o un índice duplicado

Se mantiene la bóveda actual y se crea otra carpeta que copie, enlace mediante
atajos o resuma los Markdown de las demás áreas.

**Pros**

- Puede ofrecer una interfaz curada sin tocar la raíz del repositorio.
- Permite experimentar sin cambiar la configuración activa.

**Contras**

- Introduce duplicación, sincronización y posibles divergencias entre fuente e
  índice.
- Los enlaces pueden apuntar a copias o atajos en lugar del documento
  autoritativo.
- Aumenta el mantenimiento y debilita la trazabilidad PCS.
- No resuelve de forma limpia el almacenamiento compartido de Vault Operator.

**Valoración:** útil como prototipo aislado, pero no recomendable como
arquitectura estable.

## Comparativa resumida

Puntuación de 1 a 5; el resultado es una ayuda para debatir, no una decisión
automática.

| Alternativa | Consulta y enlace | Autoridad | Riesgo | Compatibilidad | Esfuerzo | Resultado ponderado |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1. Mantener ámbito local | 1 | 5 | 5 | 5 | 5 | 3,8 |
| 2. Raíz sin política | 5 | 2 | 2 | 3 | 4 | 3,3 |
| 3. Raíz gobernada | 5 | 5 | 4 | 4 | 3 | **4,4** |
| 4. Bóveda espejo | 4 | 2 | 3 | 2 | 1 | 2,8 |

La alternativa 1 puntúa bien en seguridad porque no cambia nada, pero falla en
el criterio más importante: no mejora la consulta conjunta. La alternativa 3
es la única que cumple el propósito sin pagar el coste continuo de una copia.

## Propuesta recomendada

### 1. Definir la raíz del repositorio como bóveda transversal

Abrir `C:\Users\gusve\Documents\Apps\carrera-profesional-ai-first` como
bóveda de Obsidian. La raíz pasa a ser el contenedor de navegación, no una
declaración de que todo su contenido tiene la misma autoridad.

Las fuentes que deben formar parte de la consulta normal son:

- `README.md` y `AGENTS.md`: orientación del host.
- `docs/`: definición funcional, versionado, metodología y propuestas.
- `boveda-entrevista-profesional/`: conocimiento y playbook de entrevista.
- `.pcs/`: estado, decisiones, acciones y sesiones, con la precedencia ya
  definida por sus instrucciones locales.

### 2. Separar exclusión de Git y exclusión de Obsidian

Conservar `.gitignore` para Git. Añadir, durante la implantación, una política
de exclusiones de Obsidian que oculte del explorador las rutas no destinadas a
consulta documental: configuraciones `.obsidian/`, `.obsidian-agent/` y
`.vault-operator/`, datos compartidos, `vault-operator-shared/`,
`obsilo-shared/`, `.worktrees/`, cachés y otros artefactos locales.

La política debe revisarse con cuidado: ocultar una carpeta no cambia la
autoridad ni permite tratarla como inexistente. También debe permitir una
consulta técnica explícita cuando sea necesaria.

### 3. Adoptar una convención de enlaces transversal

Para evitar ambigüedad, los enlaces nuevos deben seguir estas reglas:

- Usar wikilink simple solo cuando el nombre de nota sea único.
- Para nombres repetidos, usar wikilink con ruta, por ejemplo
  `[[docs/AGENTS|Instrucciones de documentación]]`.
- Mantener enlaces Markdown relativos existentes cuando ya sean correctos; no
  convertirlos masivamente sin una revisión por archivo.
- En documentos PCS, conservar la distinción entre enlace de navegación y
  afirmación de autoridad: enlazar una sesión no convierte su contenido en
  estado vivo ni en decisión vigente.
- Crear un índice de navegación transversal solo después de la implantación,
  con enlaces a las entradas principales de cada capa; no duplicar resúmenes
  autoritativos.

### 4. Resolver los directorios actuales con migración, no con borrado

| Directorio actual | Tratamiento recomendado | Razón |
| --- | --- | --- |
| `boveda-entrevista-profesional/.obsidian/` | Crear la configuración de la nueva bóveda en la raíz y migrar selectivamente ajustes, plugins y temas; conservar copia hasta validar. | Contiene configuración, plugins y espacio de trabajo vinculados a la antigua raíz. |
| `boveda-entrevista-profesional/.vault-operator/` | Migrar o regenerar bajo la raíz nueva, tras copia de seguridad y prueba del plugin. | `agentFolderPath` usa `.vault-operator`; la nueva bóveda necesita un directorio coherente con su raíz. |
| `boveda-entrevista-profesional/.obsidian-agent/` | Inventariar su contenido; no trasladar ni borrar por defecto. Retirar solo si una prueba confirma que no tiene consumidores. | Es un directorio local oculto cuyo papel no queda demostrado por la configuración revisada. |
| `obsilo-shared/` | Trasladar de forma controlada a `C:\Users\gusve\Documents\Apps\obsilo-shared/` al cambiar la raíz de bóveda. | Es la primera ruta compartida que Vault Operator busca en el directorio padre de la bóveda. |
| `vault-operator-shared/` | Trasladar de forma controlada a `C:\Users\gusve\Documents\Apps\vault-operator-shared/`; mantenerlo separado de `obsilo-shared/`. | Es la alternativa compartida que Vault Operator conoce y contiene historial/estado distinto; no debe fusionarse ni eliminarse por inferencia. |

La regla es simple: **copiar, adaptar, validar y solo entonces retirar el
origen**. No fusionar `obsilo-shared/` y `vault-operator-shared/` sin una
comparación de contenido y una decisión explícita.

### 5. Ejecutar una implantación en cuatro fases

1. **Inventario y respaldo.** Registrar rutas, tamaños y dependencias; copiar
   los directorios de configuración y compartidos fuera del alcance de trabajo
   antes de intervenir.
2. **Bóveda piloto.** Abrir la raíz como bóveda y crear la configuración raíz;
   migrar de forma selectiva plugins y preferencias sin eliminar el contexto
   antiguo.
3. **Validación.** Comprobar apertura de notas, búsqueda, backlinks, enlaces
   `obsidian://`, funcionamiento de Vault Operator, rutas compartidas y
   ausencia de exposición innecesaria de directorios técnicos.
4. **Consolidación.** Aplicar las exclusiones, actualizar los enlaces que sean
   realmente ambiguos, documentar la arquitectura y decidir el destino final
   de las rutas antiguas.

## Criterios de aceptación antes de consolidar

- La bóveda raíz muestra y abre los Markdown de `docs/`,
  `boveda-entrevista-profesional/` y `.pcs/`.
- Las rutas de datos locales no aparecen como material de lectura ordinario.
- Los cinco grupos de nombres repetidos pueden enlazarse sin ambigüedad.
- El estado actual, una decisión vigente y una sesión se distinguen con claridad
  en la navegación y en los documentos de enlace.
- Vault Operator abre, conserva su historial y reconoce los directorios
  compartidos en el nivel `Apps`.
- Ningún directorio se elimina antes de que la nueva configuración haya sido
  validada y de que exista copia recuperable.
- Git continúa ignorando los datos locales previstos y el repositorio no
  incorpora archivos de bases de datos, historiales o cachés por accidente.

## Riesgos y salvaguardas

| Riesgo | Salvaguarda |
| --- | --- |
| Confundir navegación con autoridad | Mantener en cada capa sus instrucciones y fuentes de verdad; usar índices solo como puertas de entrada. |
| Enlace a una nota equivocada por nombre repetido | Exigir rutas en wikilinks ambiguos y comprobar backlinks tras cada cambio. |
| Pérdida de contexto de Vault Operator | Copia previa, traslado controlado, prueba de apertura y mantenimiento temporal del origen. |
| Exposición de datos técnicos o personales | Exclusiones de Obsidian, no indexar ni mostrar por defecto directorios compartidos, cachés, bases de datos o historiales. |
| Migración difícil de revertir | Fases separadas y punto de retorno hasta la validación completa. |

## Decisión solicitada

Se propone aprobar la alternativa 3 y abrir una acción de implantación limitada
a la fase 1 y la preparación de la fase 2. Esa acción deberá definir el
respaldo concreto, el método de traslado y las pruebas de Vault Operator antes
de cualquier movimiento o eliminación.

## Fuentes y trazabilidad

- Sesión de origen:
  [debate sobre Obsidian](../../.pcs/sesiones/sesion-20260717-1930-debate-obsidian-proyecto-completo.md).
- Configuración local observada:
  `boveda-entrevista-profesional/.obsidian/` y
  `boveda-entrevista-profesional/.vault-operator/`.
- Código local observado de Vault Operator:
  `boveda-entrevista-profesional/.obsidian/plugins/vault-operator/main.js`.
- [Documentación oficial de Git sobre `.gitignore`](https://git-scm.com/docs/gitignore).
- [Documentación oficial de URI y apertura de bóvedas de Obsidian](https://help.obsidian.md/Extending%2BObsidian/Obsidian%2BURI).

Esta propuesta es una recomendación técnica y documental. No sustituye una
decisión PCS formal ni modifica por sí misma el estado operativo del proyecto.
