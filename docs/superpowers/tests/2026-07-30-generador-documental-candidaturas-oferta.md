# Pruebas del generador documental de candidaturas por oferta

## Entorno y fixtures

Las pruebas no modificarán candidaturas reales. Usarán una candidatura
sintética bajo `.tmp/job-up-generador-fixtures/` con:

- una copia de las dos plantillas DOCX;
- `TEMPLATE_CV_FORMATO.tex`;
- una fotografía PNG válida de prueba;
- un `datos-generacion.json` generado desde su plantilla;
- un seguimiento y una ficha con `presentada: false`;
- salidas y registros aislados.

La ejecución se hará con Python 3.12+, las dependencias de
`scripts/job-up/requirements.txt`, LibreOffice y Poppler o PDFium disponibles. Cada
prueba conservará su `execution_id` y limpiará solo su propio fixture.

## Matriz de casos

| Caso | Preparación | Resultado esperado |
| --- | --- | --- |
| generación inicial | candidatura `en_preparacion`, sin salidas | publica exactamente cinco artefactos |
| regeneración | `presentada: false`, cinco salidas existentes | sobrescribe solo las cinco salidas canónicas |
| presentada | `presentada: true` | detiene antes de escribir |
| estado ausente | falta `estado` o `presentada` | detiene y registra el error |
| estado discordante | seguimiento y ficha difieren | detiene sin publicar |
| duplicada | estado `duplicada` | detiene sin publicar |
| cero experiencias | seis parejas vacías | elimina los seis bloques sin líneas vacías |
| tres experiencias | parejas 1–3 informadas, 4–6 vacías | publica solo tres bloques |
| seis experiencias | seis parejas informadas | conserva los seis bloques |
| pareja inconsistente | cabecera vacía y descripción informada | detiene por JSON inválido semánticamente |
| marcador dividido | fixture DOCX con marcadores en varios runs | sustituye y conserva negrita/estilo |
| marcador desconocido | marcador no declarado en JSON | detiene por plantilla incompatible |
| template corrupto | carácter `�`, pie interno o slot de foto ausente | detiene por plantilla incompatible |
| fotografía ausente | ruta inexistente | detiene antes de crear salidas |
| fotografía inválida | fichero no es PNG/JPEG válido | detiene antes de publicar |
| PDF antiguo | PDF previo con el mismo nombre | lo elimina solo del temporal, exige PDF nuevo |
| LibreOffice bloqueado | proceso supera 60 segundos | termina el árbol, registra y no reintenta |
| fallo de publicación | error simulado en el tercer destino | restaura y verifica los anteriores |
| interrupción recuperable | manifiesto en fase `publicando` | la siguiente ejecución recupera o se detiene dejando evidencia |
| concurrencia | dos procesos para la misma candidatura | uno adquiere el bloqueo y el otro se detiene |
| LaTeX sin compilador | no debe ser necesario | genera `cv.tex` y lo valida estructuralmente |
| LaTeX inválido | llaves o entornos desequilibrados | detiene la publicación y registra `LATEX_INVALIDO` |
| registro no escribible | carpeta de registros bloqueada | informa del fallo en consola |

## Evidencias obligatorias

Cada ejecución de prueba debe conservar temporalmente, fuera de las
candidaturas reales:

- código de salida;
- consola capturada;
- registro JSON si se esperaba un fallo;
- listado de hashes de temporales y publicaciones;
- `pdfinfo` y render PNG de cada PDF;
- resultado del validador de DOCX y del validador LaTeX;
- estado final del manifiesto de publicación.

La prueba se considera aprobada solo si el resultado observado coincide con la
fila completa de la matriz y no deja procesos LibreOffice activos.

## Evidencia ejecutada en la primera implementación

El 2026-07-30 se ejecutó:

```text
python -m unittest discover -s tests -v
```

Resultado: 23 pruebas superadas. La integración ejecutada generó los cinco
artefactos, validó la fotografía en DOCX y PDF, renderizó ambas páginas con
PDFium, publicó mediante manifiesto,
confirmó `latex: validado_estructuralmente` sin necesitar un compilador LaTeX y dejó limpia la subcarpeta de
ejecución. También se probaron el bloqueo concurrente, la restauración tras un
fallo de reemplazo y la recuperación de un manifiesto en `publicando`.

Las filas de timeout, renderizado visual Poppler y registro no escribible siguen
siendo controles pendientes de ejecución específica; no se consideran
aprobadas por la integración anterior.

El 2026-07-31 se migraron las fichas históricas y el seguimiento para añadir
`presentada`. La auditoría estructural validó 3 candidaturas regenerables y
14 bloqueadas por presentación, y confirmó que los wikilinks de la tabla no
se rompen al leer sus separadores internos.

### Trazabilidad de la matriz

Las filas de la matriz quedan cubiertas por estas pruebas automatizadas:

| Grupo de filas | Evidencia |
| --- | --- |
| generación, regeneración, cinco artefactos y PDF | `test_cli_integration_generates_and_publishes_five_artifacts`, `test_publication_replaces_all_outputs_and_can_restore_after_interruption` |
| estados ausente, discordante, presentada y duplicada | `test_state_matrix_accepts_only_regenerable_combinations`, `test_state_missing_and_discordant_sources_are_blocked` |
| cero, tres y seis experiencias; parejas incompletas | `test_experience_matrix_accepts_zero_three_or_six_complete_pairs` |
| marcadores divididos, desconocidos y duplicados | `test_split_marker_is_replaced_and_unknown_duplicate_markers_are_rejected` |
| plantilla, slot fotográfico y fotografía inválida/ausente | `test_template_and_photo_contract_reject_corruption`, `test_missing_photo_and_unwritable_error_log_stop_or_fallback` |
| PDF antiguo, timeout y limpieza de staging | `test_conversion_removes_stale_pdf_before_accepting_new_output`, `test_libreoffice_timeout_kills_tree_and_cleans_staging` |
| publicación fallida, recuperación y concurrencia | `test_publication_restores_previous_outputs_when_a_replace_fails`, `test_recovery_restores_a_publicando_manifest_before_new_generation`, `test_candidate_lock_rejects_a_live_second_execution` |
| LaTeX sin compilador y estructura inválida | `test_latex_validation_is_structural_and_does_not_require_compiler`, `test_latex_structural_validation_rejects_unbalanced_document` |
| registro no escribible | `test_missing_photo_and_unwritable_error_log_stop_or_fallback` |
