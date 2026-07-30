# Seguimiento de candidaturas

## Propósito

Este documento define el vocabulario y los campos estructurados que utiliza el
generador documental para decidir si puede crear o sobrescribir documentos.
La tabla `seguimiento-candidaturas.md` es la fuente global del estado; la ficha
`candidatura.md` aporta la confirmación estructurada de presentación.

## Campos obligatorios para el generador

En el frontmatter de `candidatura.md` deben existir:

```yaml
id: CAND-YYYY-NNN
estado: en_preparacion
presentada: false
```

La ficha debe declarar además el identificador de la candidatura. Las fichas
históricas que usan `id_candidatura` se aceptan durante la migración; las
nuevas fichas deben usar `id`. El valor debe coincidir exactamente con la fila
del seguimiento.

`presentada` solo admite `true` o `false`. No se interpreta el texto libre de
`observaciones` para decidir si se puede sobrescribir.

## Estados permitidos

- `en_preparacion`: expediente en preparación; no presentado.
- `pendiente_de_aprobacion`: documentos preparados para revisión humana; no presentado.
- `aprobada`: documentos aprobados por la persona; no implica presentación y
  requiere `presentada: false` o `true` explícito.
- `enviada`: candidatura presentada; bloquea la sobrescritura.
- `rechazada`: candidatura presentada y rechazada; bloquea la sobrescritura.
- `detenida`: flujo detenido; solo permite regenerar con `presentada: false`.
- `duplicada`: expediente duplicado; bloquea la generación.
- `fallida`: última generación fallida; permite una nueva ejecución si
  `presentada: false`.

La forma `preparada` queda obsoleta y no es válida para nuevas candidaturas.
Los expedientes históricos existentes fueron migrados para incluir
`presentada` antes de ejecutar el generador.

## Regla de sobrescritura

El generador solo podrá sobrescribir cuando `presentada` sea exactamente
`false` y el estado no sea `duplicada`. Si `presentada` falta, no es booleana o
entra en conflicto con el estado global, el generador se detendrá.

Cuando el seguimiento global y la ficha de candidatura no coincidan, no hay
precedencia automática: se detiene el flujo para corregir la discrepancia.

## Reglas de la tabla global

- La cabecera debe contener las columnas `id_candidatura`, `estado` y
  `presentada`; esta última se sitúa junto a `estado` y solo admite `true` o
  `false`.
- Cada `id_candidatura` debe aparecer una sola vez.
- La fila debe contener un estado permitido.
- Una tabla ausente, dañada o con duplicados es un bloqueo.
- Las candidaturas espontáneas pueden usar este vocabulario, pero quedan fuera
  del generador documental de esta primera versión.
