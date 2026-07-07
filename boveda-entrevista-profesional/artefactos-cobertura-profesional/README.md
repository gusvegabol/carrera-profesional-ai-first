# README — artefactos-cobertura-profesional

## Estado de este documento

Describe qué contiene cada subcarpeta de `artefactos-cobertura-profesional/`, cómo se relacionan entre sí, y qué reglas rigen su ciclo de vida.

Esta carpeta contiene el **estado vivo** generado al usar [[PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_0]]. No contiene método — eso vive en [[CONCEPTO_COBERTURA_PROFESIONAL]], [[PATRON_STAR_SIMPLE]] y `07_playbook/`. Contiene lo que una persona real produce al ser entrevistada bajo ese playbook, a lo largo de varias sesiones.

Vive dentro de la bóveda, sin numeración, deliberadamente — a diferencia de `01_` a `08_`, no es método ni evidencia curada para lectura reflexiva; es registro operativo que crece con cada sesión real. Se mantiene dentro de la bóveda (y no como carpeta separada a nivel de host) por dos razones prácticas: evita que la ejecución del playbook tenga que escribir fuera del árbol al que ya tiene acceso, y mantiene el contenido bajo el mismo paraguas de Obsidian y su vault-operator.

**Regla transversal para todo lo que sigue:** una vez cerrado, un fichero no se edita retroactivamente. Correcciones o nueva información se registran como fichero nuevo (con sufijo `_b`, `_c`...) o como actualización explícita con fecha, nunca sobrescribiendo silenciosamente lo ya escrito. Sin esto no es posible auditar después por qué el sistema decidió algo.

---

## `mapas/`

**Contenido:** un fichero por persona o contexto entrevistado — `MAPA_<identificador>.md`. Es el único documento de toda la carpeta que se edita de forma continua, sesión tras sesión; todo lo demás se crea una vez y no se vuelve a tocar.

**Qué guarda por cada zona:** nombre, estado ([[CONCEPTO_COBERTURA_PROFESIONAL]]: explorada / candidata / parcial / pendiente), y una referencia por ruta a los ficheros de detalle correspondientes — nunca el detalle en sí. El mapa debe poder leerse entero en segundos; si empieza a crecer con contenido largo dentro, es señal de que algo se está guardando en el sitio equivocado.

**A tener en cuenta:**
- El identificador de zona, una vez asignado, no se reutiliza ni se renumera aunque la zona se descarte o se fusione con otra.
- Una zona puede tener más de una referencia a `competencias/` o `inmersiones/` si se retomó varias veces — el mapa lista todas, no solo la más reciente.
- Es el único fichero de esta carpeta sin fecha de cierre — está vivo mientras la persona siga siendo entrevistada.

---

## `checkpoints/`

**Contenido:** `CHECKPOINT_<identificador>_ZONA_<nnn>.md` — uno por cada inmersión de [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]] interrumpida antes de cerrar. Contenido: patrón activo, paso exacto donde se interrumpió, evidencia clasificada (hecho / interpretación / hipótesis / pendiente), guardarraíles activados, estado de fatiga o tiempo declarado.

**Cuándo se crea:** solo si una zona queda en estado *parcial* — nunca por defecto. Mientras no haya interrupción, esta carpeta puede estar vacía.

**Cuándo deja de usarse:** cuando la zona pasa a *explorada*, el checkpoint no se traslada ni se borra — se marca `Estado: cerrado` con fecha de integración, y su contenido relevante queda resumido en la inmersión resultante. Se conserva solo como trazabilidad.

**A tener en cuenta:** un checkpoint activo (`Estado: activo`) es la única fuente fiable para la excepción de reanudación exacta (`PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_0` §10.2 — "no quiero repetirlo todo"). Si el fichero no existe o está incompleto, el playbook debe decirlo con honestidad en vez de fingir precisión.

---

## `inmersiones/`

**Contenido:** `INMERSION_<identificador>_ZONA_<nnn>.md` (o `_b`, `_c`... si la zona se retoma más de una vez) — el resultado íntegro de una activación completa de [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]] sobre esa zona. Formato: la ficha mínima completa de v1.3.2 §14, sin recortar — situación, acción propia, resultado, contexto, las tres validaciones, calidad de evidencia, qué no debe afirmarse todavía.

**Cuándo se crea:** cada vez que cobertura invoca profundidad y la inmersión llega a cierre — con o sin competencia plenamente validada. Una inmersión que cerró con evidencia débil también se registra aquí, con honestidad sobre su debilidad.

**A tener en cuenta:**
- Es el documento fuente: si algo en `competencias/` necesita más contexto del que tiene, se remite aquí.
- Puede incluir, si se decide conservarla, referencia a la sesión de origen en `sesiones/` para reconstruir el hilo completo si hace falta auditar.
- No confundir con `08_entrevistas_piloto/`: aquello son casos de profundidad aislada, pensados como evidencia curada y citable en la bóveda (ya alimentan antipatrones, como [[PILOTO_005_ENTREVISTA_REPONEDOR_SUPERMERCADO]]). Esto es registro operativo de una pieza de un proceso de cobertura más largo — mismo formato de ficha, función distinta.

---

## `competencias/`

**Contenido:** `COMPETENCIA_<identificador>_ZONA_<nnn>.md` — versión corta derivada de una inmersión ya cerrada: nombre corto, formulación observable, versión humana, calidad de evidencia, y referencia explícita a su inmersión de origen (`Inmersión: inmersiones/INMERSION_..._ZONA_003.md`).

**Por qué existe si ya está `inmersiones/`:** es lo que el mapa y cualquier lectura rápida del perfil de la persona necesitan consultar primero, sin abrir el documento largo cada vez. Es un índice enriquecido: no repite evidencia, la resume con lo justo para reconocer la competencia de un vistazo.

**A tener en cuenta:**
- Solo se crea si la inmersión resultó en competencia con evidencia al menos media — una inmersión débil que no llegó a competencia razonable queda solo en `inmersiones/`, sin entrada aquí.
- Fichero nuevo por cada competencia distinta, aunque proceda de la misma zona reabierta — nunca se anexa a un fichero de competencia ya cerrado.

---

## `sesiones/`

**Contenido:** `SESION_COBERTURA_<identificador>_<fecha>.md` — registro de una sesión completa de cobertura: apertura, calibración de tiempo, panorámica, qué candidatas se detectaron, si se activó profundidad, cierre con puerta nueva.

**Carácter opcional** — a diferencia de las otras cuatro carpetas, no es estrictamente necesaria para que el sistema funcione; el mapa y las inmersiones ya contienen lo esencial para operar. Su valor es de auditoría: permite reconstruir el hilo completo de una sesión, no solo su resultado.

**A tener en cuenta:** si se activa su uso, aplicar la misma regla que v1.3.2 §16 regla 17 exige para pilotos de profundidad — conservar transcripción verbatim, no solo resumen, porque un resumen no permite auditar comportamiento turno a turno.

---

## Cómo se relacionan entre sí

```text
mapas/MAPA_<id>.md
  → referencia por ruta a →
    checkpoints/CHECKPOINT_<id>_ZONA_<n>.md     (solo si hay zona parcial)
    inmersiones/INMERSION_<id>_ZONA_<n>.md      (una por cada activación cerrada de profundidad)
    competencias/COMPETENCIA_<id>_ZONA_<n>.md   (solo si la inmersión produjo competencia)
    sesiones/SESION_COBERTURA_<id>_<fecha>.md   (opcional, solo si se decide conservar)
```

El mapa es el único punto de entrada — nadie debería tener que abrir cuatro carpetas distintas para entender el estado de una persona; el mapa apunta a donde hace falta.

---

## Identificadores y numeración

Esquema anidado, todo numérico — sin letras de intento, para no mezclar dos alfabetos distintos.

```text
id_entrevistado:  ENT-<nnn>              contador global, 3 dígitos, ceros a la izquierda
id_mapa:          ENT-<nnn>-M<nn>        anidado bajo entrevistado, 2 dígitos
id_zona:          ENT-<nnn>-M<nn>-Z<nnn> anidado bajo mapa, 3 dígitos
intento:          ENT-<nnn>-M<nn>-Z<nnn>-<nn>  anidado bajo zona, 2 dígitos
```

**`id_entrevistado`** es el único contador verdaderamente global — todos los demás son anidados y se derivan mirando el fichero padre correspondiente (última zona registrada en el mapa, último intento sobre esa zona), sin necesidad de contador propio.

**Dónde se guarda el contador:** `artefactos-cobertura-profesional/_contadores.md`, con una única línea:

```text
ultimo_id_entrevistado: ENT-003
```

**Regla de no reutilización:** un `id_zona`, una vez asignado, no se reutiliza ni se renumera aunque la zona se descarte o se fusione con otra.

**Intento, no letra:** cuando una zona se retoma más de una vez (varios intentos de inmersión, con o sin checkpoint interrumpido de por medio), el número de intento se comparte entre `checkpoint`, `inmersión` y `competencia` de ese mismo intento — nacen juntos, se identifican igual:

```text
checkpoints/CHECKPOINT_ENT-001-M01-Z003-01.md    (si ese intento se interrumpió)
inmersiones/INMERSION_ENT-001-M01-Z003-01.md
competencias/COMPETENCIA_ENT-001-M01-Z003-01.md  (solo si hubo competencia)

inmersiones/INMERSION_ENT-001-M01-Z003-02.md     (segundo intento, meses después)
```

**Pendiente de aplicar, todavía no hecho:** `TEMPLATE_CHECKPOINT.md` y su referencia en este README describen el nombre de fichero solo con número de zona (`CHECKPOINT_<id_mapa>_ZONA_<n>.md`), sin número de intento. Con la convención de arriba, un segundo intento interrumpido sobre la misma zona colisionaría de nombre con el checkpoint ya cerrado del primero — falta corregir la plantilla para incluir el número de intento en el nombre.

---

## Relación con otros documentos de la bóveda

- [[PLAYBOOK_COBERTURA_PROFESIONAL_v1_0_0]] — el playbook cuya ejecución genera todo el contenido de esta carpeta.
- [[PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA]] — formato de ficha reutilizado en `inmersiones/` y `checkpoints/`.
- [[CONCEPTO_COBERTURA_PROFESIONAL]] — vocabulario de zonas usado en `mapas/`.
- `08_entrevistas_piloto/` — carpeta distinta, para evidencia curada de profundidad aislada; no confundir con `inmersiones/`.

## Fuente base

Redactado por Claude a partir de la estructura de carpetas decidida por Gustavo, 2026-07-06.