# Diseño — PLAYBOOK_GUION_ADAPTACION_CV

**Fecha:** 2026-08-06  
**Estado:** diseño aprobado pendiente de revisión documental  
**Caso de referencia:** `CAND-2026-020` — Lidl, Responsable de turno Tienda Tamaraceite

## 1. Propósito

`PLAYBOOK_GUION_ADAPTACION_CV` convierte la estrategia común ya aprobada de una candidatura en decisiones editoriales específicas para el CV.

Su salida, `guion-adaptacion-cv.md`, debe permitir que una fase posterior genere el contenido del CV sin volver a interpretar la oferta ni decidir de nuevo qué historia profesional contar.

No redacta, diseña visualmente ni genera el CV.

## 2. Arquitectura y límites

```text
datos-core-busqueda.md
        ↓
analisis-oferta.md
        ↓
candidatura.md
        ↓
guion-adaptacion-cv.md
        ↓
futura generación de contenido del CV
        ↓
CV
```

`candidatura.md` conserva la estrategia común de la candidatura. El guion es un adaptador especializado del CV y no duplica ni vuelve a justificar dicha estrategia.

La carta de presentación queda fuera de alcance. Se diseñará posteriormente mediante su propio playbook y guion, ambos consumidores de la misma estrategia común.

El playbook puede:

- seleccionar, jerarquizar y organizar contenido factual para el CV;
- decidir qué contenido se prioriza, reduce, omite u obliga a conservar;
- indicar orden, peso relativo y detalle editorial;
- trasladar límites, carencias, advertencias y afirmaciones excluidas a instrucciones de redacción;
- producir un brief cerrado para la futura generación de contenido del CV.

El playbook no puede:

- alterar hechos, métricas, evidencias, requisitos de la oferta ni la estrategia de `candidatura.md`;
- modificar el estado de presentación;
- redactar el CV definitivo;
- decidir diseño visual, tipografía o maquetación;
- generar o guiar una carta de presentación;
- enviar o presentar la candidatura.

## 3. Entrada válida

La entrada válida es una `candidatura.md` con `GATE-CANDIDATURA-GUION: aprobado` para ese caso.

Debe conservar enlaces resolubles al análisis de origen y a las evidencias factuales utilizadas. Si la candidatura está detenida o contiene un bloqueo activo, no puede iniciarse el guion.

## 4. Contrato de `guion-adaptacion-cv.md`

El template del guion tendrá estas secciones obligatorias:

1. **Identificación y entrada**: candidatura, empresa, puesto, fecha, sesión, enlace a `candidatura.md` y confirmación del gate de entrada aprobado.
2. **Instrucción editorial de CV**: posicionamiento heredado, mensaje principal y objetivo del documento, sin justificar nuevamente la estrategia.
3. **Mapa de edición**: contenidos con tratamiento, motivo, evidencia factual y, cuando haga falta, peso relativo, orden o detalle.
4. **Experiencia y logros seleccionados**: experiencias de apertura, funciones y logros utilizables con identificadores factuales, sin frases finales de CV.
5. **Arquitectura de contenido**: orden de secciones, experiencia de apertura, distribución relativa de espacio y contenidos que no deben dominar.
6. **Léxico respaldado**: palabras clave utilizables por respaldo factual y términos prohibidos o de uso limitado.
7. **Carencias, advertencias y límites de redacción**: tratamiento editorial, riesgos y afirmaciones que no deben aparecer.
8. **Brief cerrado para generación**: instrucciones compactas que solo consumen decisiones del guion y no reabren la estrategia.
9. **Control de coherencia**: comprobaciones de trazabilidad, límites, tratamientos editoriales y bloqueos.

### 4.1 Mapa de edición

Todo contenido considerado debe usar exactamente uno de estos tratamientos:

| Tratamiento | Significado |
| --- | --- |
| `priorizar` | Debe aparecer con peso visible porque sostiene directamente el encaje. |
| `reducir` | Puede aparecer, pero con menos espacio, detalle o prominencia. |
| `omitir` | No aporta valor al CV concreto o introduce ruido; solo procede si no genera un vacío temporal o una presentación engañosa. |
| `obligatorio_conservar` | Debe permanecer por coherencia cronológica o factual aunque no sea estratégico. |

Cada fila debe indicar el motivo de adaptación y la evidencia que la respalda. Reducir u omitir no pueden emplearse para ocultar una carencia ni inducir a error.

## 5. Retroceso por evidencia nueva o contradictoria

Si durante la elaboración del guion se detecta una evidencia nueva, insuficiente o contradictoria, el guion se detiene. No se añade una excepción ni se modifica de forma parcial el guion existente.

El recorrido obligatorio es:

```text
datos-core-busqueda.md
→ analisis de origen
→ candidatura.md
→ nueva validación
→ regeneración completa de guion-adaptacion-cv.md
```

La regeneración completa evita que sobrevivan decisiones editoriales tomadas con una versión factual o estratégica obsoleta.

## 6. Gate de salida

El playbook concluye con `GATE-GUION-CONTENIDO`. Valida el guion, no el CV.

Para aprobarlo deben cumplirse todos estos criterios:

- la entrada procede de una candidatura con `GATE-CANDIDATURA-GUION` aprobado;
- cada contenido priorizado, reducido, omitido o conservado tiene motivo y trazabilidad factual;
- los contenidos prioritarios sostienen el posicionamiento heredado;
- ninguna omisión oculta carencias ni induce a error;
- afirmaciones excluidas, advertencias y límites se trasladan al guion;
- el guion no introduce hechos, métricas, competencias ni requisitos nuevos;
- la arquitectura editorial y el brief final permiten generar el CV sin reinterpretar oferta o estrategia;
- no existe bloqueo activo.

Resultados permitidos:

| Resultado | Consecuencia |
| --- | --- |
| `aprobado` | Autoriza diseñar la siguiente fase: generación de contenido del CV. |
| `requiere_correccion` | Corrige el guion sin cambiar hechos ni estrategia. |
| `requiere_revision_origen` | Detiene el guion y vuelve a análisis y candidatura por incoherencia estratégica. |
| `requiere_actualizacion_factual` | Aplica el retroceso completo y regenera el guion. |
| `bloqueado` | No genera ningún contenido hasta resolver el bloqueo. |

La evaluación de este gate registrará criterios, incidencias y resultado. `candidatura.md` solo actualizará el índice y estado del artefacto, sin copiar su contenido.

## 7. Prueba prevista

La primera prueba usará `CAND-2026-020` para comprobar que el guion:

- prioriza operaciones de supermercado, pedidos, stock, caja y equipos;
- reduce contenidos directivos que puedan provocar percepción de sobrecualificación;
- conserva lo necesario para no deformar la trayectoria;
- no presenta la FP no finalizada como titulación;
- limita la experiencia de caja a cuadres y sistema de mejora en Excel;
- respeta los límites de compras, proveedores y negociación;
- ante una evidencia nueva, exige la regeneración completa en lugar de un parche.

## 8. Entregables de implantación posteriores

- `TEMPLATE_GUION_ADAPTACION_CV_v2.md`;
- `PLAYBOOK_GUION_ADAPTACION_CV.md`;
- actualización de la SPEC con el contrato de fase, gate, alcance exclusivo de CV y retroceso factual;
- guion de prueba y evaluación del gate para `CAND-2026-020`.

Quedan fuera de alcance la redacción o maquetación del CV, la carta, los datos de generación, el generador existente y la presentación de la candidatura.
