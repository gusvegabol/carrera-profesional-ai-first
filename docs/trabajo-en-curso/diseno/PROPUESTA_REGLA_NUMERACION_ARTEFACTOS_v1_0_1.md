# Propuesta de regla de numeración de artefactos v1.0.1
## artefactos-cobertura-profesional

## Estado de este documento

Este documento es una propuesta de trabajo.

Recoge una versión más madura de la posible convención de:

- los identificadores de los artefactos;
- los contadores;
- los nombres de fichero;
- la relación entre los distintos documentos;
- el significado operativo de “creado”.

Todavía no debe leerse como regla vigente ni como versión final adoptada. Su función actual es servir de base para debate, revisión y eventual adopción posterior.

Si esta propuesta llegara a aprobarse, entonces sí debería traducirse a:

- templates;
- `artefactos-cobertura-profesional/templates/README.md`;
- `artefactos-cobertura-profesional/README.md`;
- y, si procede, a la estructura materializada de carpetas y artefactos.

---

## 1. Alcance

Esta convención aplica a la capa viva de `artefactos-cobertura-profesional/`.

Gobierna:

- `entrevistados/`
- `mapas/`
- `zonas/`
- `sesiones/`
- `checkpoints/`
- `inmersiones/`
- `competencias/`
- `templates/`

No gobierna:

- la bóveda conceptual (`01_conceptos/`, `04_patrones_de_preguntas/`, `07_playbook/`, etc.);
- PCS canónico;
- artefactos legacy anteriores salvo que se apruebe una migración explícita.

---

## 2. Precedencia

Si hay contradicción entre documentos, manda este orden:

1. este documento;
2. los templates de `artefactos-cobertura-profesional/templates/`;
3. `artefactos-cobertura-profesional/templates/README.md`;
4. `artefactos-cobertura-profesional/README.md`;
5. README de subcarpetas como `entrevistados/README.md`.

---

## 3. Principios generales

1. Ningún identificador ya usado debe reutilizarse nunca.
2. Todo contador almacena cantidad de hijos ya creados realmente.
3. Un artefacto solo se considera creado cuando el fichero ya existe grabado con nombre final y ubicación definitiva.
4. Mientras no exista fichero real, el contador no cambia.
5. Si un identificador fue emitido y el fichero quedó creado, ese identificador queda reservado para siempre, aunque luego el artefacto se cierre, descarte, fusione o deje de usarse.
6. La fuente última de verdad es el árbol real de ficheros creados; los contadores son ayuda operativa, no autoridad superior.

---

## 4. Qué significa “creado”

Creado significa:

- documento grabado en disco;
- con nombre final;
- en su ruta definitiva.

No significa:

- borrador en memoria;
- template rellenado pero no guardado;
- nombre calculado sin fichero real;
- intención de crear algo más adelante.

La actualización de un contador solo puede ocurrir después de que el fichero hijo ya exista realmente.

---

## 5. Estructura mínima obligatoria

La convención exige la existencia de estas carpetas operativas:

- `entrevistados/`
- `mapas/`
- `zonas/`
- `sesiones/`
- `checkpoints/`
- `inmersiones/`
- `competencias/`
- `templates/`

Dos consecuencias directas:

1. La carpeta `zonas/` pasa a ser obligatoria.
2. Debe existir `templates/TEMPLATE_ZONA.md`.

Sin documento de zona no existe un lugar estable donde vivan:

- el estado propio de la zona;
- sus referencias consolidadas;
- `contador_inmersiones`;
- `contador_competencias`.

---

## 6. Jerarquía de artefactos

La jerarquía es esta:

- un `entrevistado` puede tener varios `mapas` a lo largo del tiempo;
- por defecto debe existir un solo `mapa` activo por entrevistado;
- un `mapa` puede tener varias `zonas`;
- una `sesión` pertenece a un único `mapa`;
- una `zona` pertenece a un único `mapa`;
- una `inmersión` pertenece a una única `zona`;
- una `competencia` pertenece a una única `zona` y deriva de una única `inmersión`;
- un `checkpoint` y una `inmersión` comparten el mismo identificador de intento;
- `checkpoint` no tiene contador propio separado.

---

## 7. Función de cada tipo de artefacto

### 7.1 Entrevistado

Representa a la persona o caso entrevistado.

Es el ancla mínima del sistema y el padre de los mapas.

### 7.2 Mapa

Representa el estado general de cobertura de un entrevistado.

Debe funcionar como índice de zonas, no como contenedor duplicado de todo el detalle operativo.

### 7.3 Zona

Representa una parte diferenciable de la trayectoria profesional que merece seguimiento propio.

La zona pasa a ser el nodo operativo central entre mapa y profundidad. En ella deben converger:

- su estado;
- su señal de origen;
- la sesión de origen;
- sus checkpoints;
- sus inmersiones;
- sus competencias;
- sus contadores propios.

### 7.4 Sesión

Registra una sesión completa de cobertura.

Es trazabilidad narrativa, no el lugar donde se guarda el estado estructural estable.

### 7.5 Checkpoint

Registra una inmersión interrumpida.

Comparte intento con la inmersión asociada y no necesita contador independiente.

### 7.6 Inmersión

Registra una activación completa de profundidad sobre una zona.

### 7.7 Competencia

Registra una competencia ya extraída con evidencia suficiente.

Por ahora, una inmersión puede producir como máximo una competencia formalizada. Si esa regla cambia en el futuro, deberá revisarse esta convención.

---

## 8. Esquema de identificadores

La jerarquía de IDs es esta:

```text
id_entrevistado = ENT-0001
id_mapa         = ENT-0001-M01
id_zona         = ENT-0001-M01-Z001
id_sesion       = ENT-0001-M01-S001
id_inmersion    = ENT-0001-M01-Z001-I01
id_competencia  = ENT-0001-M01-Z001-C01
```

### Reglas

- `ENT` es global.
- `M` cuelga de `ENT`.
- `Z` y `S` cuelgan de `M`.
- `I` cuelga de `Z`.
- `C` cuelga de `Z`.
- La relación entre competencia e inmersión se conserva en `id_inmersion` dentro del frontmatter de la competencia.

### Razón de esta forma

- `id_zona` identifica el trozo de trayectoria que se sigue.
- `id_inmersion` identifica cuántas veces se ha intentado profundizar en esa zona.
- `id_competencia` identifica cuántas competencias formalizadas han salido de esa zona.

Esto evita mezclar:

- la identidad de la zona;
- la identidad del intento;
- la identidad del resultado.

---

## 9. Nombres de fichero

Los nombres de fichero deben derivarse siempre del identificador del artefacto.

### Convención

```text
entrevistados/ENTREVISTADO_ENT-0001.md
mapas/MAPA_ENT-0001-M01.md
zonas/ZONA_ENT-0001-M01-Z001.md
sesiones/SESION_COBERTURA_ENT-0001-M01-S001.md
checkpoints/CHECKPOINT_ENT-0001-M01-Z001-I01.md
inmersiones/INMERSION_ENT-0001-M01-Z001-I01.md
competencias/COMPETENCIA_ENT-0001-M01-Z001-C01.md
```

### Reglas

- El nombre de fichero no debe depender de títulos libres.
- El nombre de fichero no debe depender de fechas incrustadas en el nombre.
- Las fechas pertenecen al frontmatter, no al identificador.
- El prefijo semántico (`ENTREVISTADO_`, `MAPA_`, `ZONA_`, etc.) es obligatorio.

---

## 10. Ubicación de los contadores

### 10.1 Contador global

Debe existir un único contador global externo para entrevistados, por ejemplo:

- `artefactos-cobertura-profesional/_contadores.md`

Ese contador solo sirve para generar nuevos `id_entrevistado`.

No debe usarse para mapas, zonas, sesiones, inmersiones ni competencias.

### 10.2 En el entrevistado

Cada entrevistado debe incluir:

- `contador_mapas`

### 10.3 En el mapa

Cada mapa debe incluir:

- `contador_zonas`
- `contador_sesiones`

### 10.4 En la zona

Cada zona debe incluir:

- `contador_inmersiones`
- `contador_competencias`

---

## 11. Significado de los contadores

Todos los contadores empiezan en `0`.

El valor guardado significa siempre “cuántos hijos reales ya existen”.

Ejemplos:

- `contador_mapas: 1` = ese entrevistado tiene un mapa creado;
- `contador_zonas: 4` = ese mapa tiene cuatro zonas creadas;
- `contador_sesiones: 3` = ese mapa tiene tres sesiones creadas;
- `contador_inmersiones: 2` = esa zona tiene dos inmersiones creadas;
- `contador_competencias: 1` = esa zona tiene una competencia creada.

El contador nunca almacena el siguiente valor libre. Almacena la cantidad ya creada.

---

## 12. Regla de generación de un nuevo identificador

La secuencia correcta es siempre esta:

1. leer el contador actual del padre;
2. calcular `nuevo = contador_actual + 1`;
3. construir el nuevo identificador con ese valor;
4. crear el fichero real;
5. solo si el fichero quedó creado, actualizar el contador del padre a `nuevo`.

### Ejemplos

- `contador_mapas: 0` -> se crea `M01` -> `contador_mapas: 1`
- `contador_zonas: 3` -> se crea `Z004` -> `contador_zonas: 4`
- `contador_sesiones: 1` -> se crea `S002` -> `contador_sesiones: 2`
- `contador_inmersiones: 1` -> se crea `I02` -> `contador_inmersiones: 2`
- `contador_competencias: 0` -> se crea `C01` -> `contador_competencias: 1`

---

## 13. Frontmatter mínimo obligatorio por artefacto

### 13.1 Entrevistado

```yaml
tipo: entrevistado
id_entrevistado: ENT-0001
alias:
fecha_creacion:
contador_mapas: 0
```

### 13.2 Mapa

```yaml
tipo: mapa
id_mapa: ENT-0001-M01
id_entrevistado: ENT-0001
fecha_creacion:
fecha_actualizacion:
estado: activo
fecha_cierre:
contador_zonas: 0
contador_sesiones: 0
```

### 13.3 Zona

```yaml
tipo: zona
id_zona: ENT-0001-M01-Z001
id_mapa: ENT-0001-M01
id_entrevistado: ENT-0001
fecha_creacion:
fecha_actualizacion:
estado: candidata
fecha_cierre:
contador_inmersiones: 0
contador_competencias: 0
```

### 13.4 Sesión

```yaml
tipo: sesion
id_sesion: ENT-0001-M01-S001
id_mapa: ENT-0001-M01
id_entrevistado: ENT-0001
fecha_creacion:
estado: abierta
fecha_cierre:
motivo_cierre:
```

### 13.5 Checkpoint

```yaml
tipo: checkpoint
id_inmersion: ENT-0001-M01-Z001-I01
id_zona: ENT-0001-M01-Z001
id_mapa: ENT-0001-M01
id_entrevistado: ENT-0001
fecha_creacion:
estado: activo
fecha_cierre:
```

### 13.6 Inmersión

```yaml
tipo: inmersion
id_inmersion: ENT-0001-M01-Z001-I01
id_zona: ENT-0001-M01-Z001
id_mapa: ENT-0001-M01
id_entrevistado: ENT-0001
id_competencia:
fecha_creacion:
resultado:
```

### 13.7 Competencia

```yaml
tipo: competencia
id_competencia: ENT-0001-M01-Z001-C01
id_inmersion: ENT-0001-M01-Z001-I01
id_zona: ENT-0001-M01-Z001
id_mapa: ENT-0001-M01
id_entrevistado: ENT-0001
fecha_creacion:
calidad_evidencia:
```

---

## 14. Regla específica de checkpoint e inmersión

`checkpoint` e `inmersion` comparten el mismo `id_inmersion`.

Ejemplo:

- `CHECKPOINT_ENT-0001-M01-Z001-I01.md`
- `INMERSION_ENT-0001-M01-Z001-I01.md`

Ambos documentos pertenecen al mismo intento `I01` sobre la misma zona `Z001`.

### Consecuencias

- `checkpoint` no necesita contador propio;
- `checkpoint` no representa una rama distinta;
- `checkpoint` representa el estado interrumpido de una inmersión identificada por `I`.

---

## 15. Regla específica del mapa

Con la introducción del documento de zona, el mapa deja de ser el lugar donde se duplican rutas detalladas de checkpoints, inmersiones y competencias.

### El mapa debe contener

- referencia al entrevistado;
- lista de zonas;
- estado general;
- advertencia de límite;
- siguiente exploración recomendada.

### El mapa no debe contener como fuente principal

- detalle operativo completo de cada zona;
- histórico fino de inmersiones;
- listas duplicadas de competencias;
- lógica de contadores de profundidad.

Ese detalle debe vivir en cada documento `ZONA_...`.

El mapa funciona como índice. La zona funciona como nodo operativo.

---

## 16. Regla específica de la zona

Cada documento de zona debe ser la pieza central de agregación operativa para esa zona.

Debe poder responder, sin consultar el mapa:

- qué zona es;
- en qué estado está;
- en qué sesión nació;
- qué señal la originó;
- cuántas inmersiones ha tenido;
- cuántas competencias ha producido;
- qué checkpoints, inmersiones y competencias le pertenecen.

---

## 17. Regla de consistencia y reparación

Si alguna vez hay divergencia entre un contador y los ficheros realmente existentes:

- mandan los ficheros realmente existentes;
- el contador debe repararse tomando el mayor ordinal ya materializado entre sus hijos directos.

Ejemplos:

- si existe `MAPA_ENT-0001-M02.md` pero `contador_mapas: 1`, el contador correcto es `2`;
- si existe `INMERSION_...-I03.md` pero `contador_inmersiones: 2`, el contador correcto es `3`.

---

## 18. Régimen de adopción

Esta convención aplica a todos los artefactos nuevos creados tras su adopción.

Los artefactos anteriores se consideran legado hasta que exista una decisión explícita de migración.

No deben renombrarse ni reescribirse por inercia.

---

## 19. Impacto obligatorio de esta convención

Si esta convención se adopta, deben realizarse estos cambios:

1. crear la carpeta `zonas/` si todavía no existe;
2. crear `templates/TEMPLATE_ZONA.md`;
3. adaptar `TEMPLATE_ENTREVISTADO.md` para incluir `contador_mapas`;
4. adaptar `TEMPLATE_MAPA.md` para incluir `contador_zonas` y `contador_sesiones`, y para dejar de duplicar detalle que debe vivir en la zona;
5. adaptar `TEMPLATE_SESION.md` para introducir `id_sesion`;
6. adaptar `TEMPLATE_CHECKPOINT.md` para incluir `id_inmersion`;
7. adaptar `TEMPLATE_INMERSION.md` para incluir `id_inmersion`;
8. adaptar `TEMPLATE_COMPETENCIA.md` para que el nombre del fichero y el frontmatter sigan esta convención;
9. actualizar `artefactos-cobertura-profesional/templates/README.md` para que remita a esta convención como fuente normativa;
10. actualizar `artefactos-cobertura-profesional/README.md` para que no contradiga esta estructura.

---

## 20. Regla final

La identidad del sistema no debe depender de inferencias, memoria implícita ni reconstrucciones blandas.

Debe depender de:

- ficheros reales;
- identificadores estables;
- contadores locales y explícitos;
- relaciones trazables entre artefactos.

Esa es la base mínima para que la cobertura profesional pueda reanudarse sin ambigüedad, sin colisiones y sin perder historia.
