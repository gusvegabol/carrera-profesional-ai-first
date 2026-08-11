---
id: PLAYBOOK_COMPONER_CARTA_PRESENTACION
tipo: playbook
version: "1.1.0"
estado: en_prueba
alcance: exclusivo_composicion_carta_presentacion
entrada_principal: contenido-carta-presentacion.md
salidas_documentales:
  - carta-presentacion.docx
  - carta-presentacion.pdf
salida_texto: Carta completa consolidada
registro: evaluacion-composicion-carta-presentacion.md
gate_entrada: GATE-CONTENIDO-CARTA-COMPOSICION
gate_salida: GATE-CARTA-REVISION-HUMANA
---

# PLAYBOOK — Componer carta de presentación

## 1. Propósito

Este playbook transforma un `contenido-carta-presentacion.md` semánticamente cerrado y aprobado en las representaciones necesarias para presentar una carta de candidatura por distintos canales.

Debe soportar dos modos operativos:

```text
MODO TEXTO

contenido-carta-presentacion.md
→ Carta completa consolidada
→ copiar/pegar
```

```text
MODO DOCUMENTO

cabecera canónica de candidatura
+
Carta completa consolidada
→ carta-presentacion.docx
→ carta-presentacion.pdf
```

El modo texto no genera un artefacto adicional.

El modo documento genera documentos formales directamente utilizables sin edición manual posterior.

Principio central:

> El contenido decide qué dice la carta. La composición decide únicamente cómo se presenta.

## 2.1 Política de fotografía

La carta no incluye fotografía por defecto. La existencia de una fotografía
autorizada para el CV no autoriza a mostrarla en la carta. Solo una decisión o
configuración humana expresa y específica para esta carta podría habilitarla
en una futura extensión contractual.

En el contrato vigente, la ausencia de fotografía no es un defecto, no bloquea
la composición, no bloquea la revisión y no invalida la carta. Este compositor
no carga, busca, copia ni renderiza fotografías.

---

## 2. Responsabilidad de fase

`PLAYBOOK_COMPONER_CARTA_PRESENTACION` puede decidir únicamente:

- estructura documental;
- aplicación de la cabecera canónica;
- tipografía;
- tamaños;
- márgenes;
- alineaciones;
- espaciados;
- saltos;
- paginación;
- compatibilidad DOCX;
- conversión PDF;
- verificaciones de equivalencia;
- controles de render;
- controles de privacidad documental.

No puede decidir:

- nueva información;
- nuevos argumentos;
- nuevas evidencias;
- nueva motivación;
- nuevo posicionamiento;
- cambio de tono;
- reescritura;
- resumen;
- ampliación;
- eliminación semántica;
- actualización de hechos;
- presentación externa de la candidatura.

Composición no equivale a redacción.

---

## 3. Flujo

```text
contenido-carta-presentacion.md
        ↓
GATE-CONTENIDO-CARTA-COMPOSICION
        ↓
PLAYBOOK_COMPONER_CARTA_PRESENTACION
        ↓
        ├── modo_texto
        │      └── Carta completa consolidada
        │          → copiar/pegar
        │
        └── modo_documento
               └── cabecera canónica candidatura
                   +
                   Carta completa consolidada
                   ↓
                   carta-presentacion.docx
                   carta-presentacion.pdf
                   ↓
                   evaluacion-composicion-carta-presentacion.md
                   ↓
                   GATE-CARTA-REVISION-HUMANA
```

Con `GATE-CONTENIDO-CARTA-COMPOSICION = aprobado`, si no existe dato nuevo,
decisión humana, revisión humana ni acción irreversible, la orquestación inicia
automáticamente esta composición. La selección de esta transición se representa
en `scripts/job-up/orquestar_transiciones.py`; no se solicita una confirmación
adicional para iniciar la composición. La composición no abre por sí misma
ningún gate posterior; deja la salida preparada para
`GATE-CARTA-REVISION-HUMANA`.

---

## 4. Artefactos

### 4.1 Fuente semántica

```text
contenido-carta-presentacion.md
```

La única sección autorizada como cuerpo visible es:

```text
Carta completa consolidada
```

### 4.2 Documento editable

```text
carta-presentacion.docx
```

En `modo_documento` debe contener:

```text
cabecera canónica
+
cuerpo semántico aprobado
```

### 4.3 Documento presentable

```text
carta-presentacion.pdf
```

Debe representar la misma composición documental que el DOCX.

### 4.4 Registro interno

```text
evaluacion-composicion-carta-presentacion.md
```

Registra:

- entradas;
- configuración;
- cabecera;
- trazabilidad;
- verificaciones;
- incidencias;
- resultado técnico.

No forma parte de la documentación destinada al recruiter.

---

## 5. Fuente semántica única

No deben existir dos versiones independientes de la carta.

Queda prohibido mantener:

```text
carta_para_copiar
carta_para_documento
```

como textos independientes susceptibles de divergir.

La única autoridad textual es:

```text
contenido-carta-presentacion.md
→ Carta completa consolidada
```

---

## 6. `modo_texto`

Se utiliza cuando una plataforma ofrece un campo de texto para introducir la carta.

Salida operacional:

```text
Carta completa consolidada
```

Reglas:

1. se copia directamente desde la fuente semántica;
2. no se añade cabecera documental;
3. no se genera `.txt`;
4. no se genera otro `.md`;
5. no se crea una versión abreviada;
6. no se reescribe;
7. no se añaden datos de contacto por composición.

Principio:

> `modo_texto` es una forma de uso de la fuente semántica, no un nuevo artefacto.

---

## 7. `modo_documento`

Se utiliza cuando la plataforma permite o exige adjuntar la carta como documento.

Debe generar:

```text
cabecera canónica de candidatura
+
Carta completa consolidada
```

en:

```text
carta-presentacion.docx
carta-presentacion.pdf
```

Ambos documentos deben quedar preparados para uso directo.

No debe ser necesario:

```text
abrir DOCX
→ añadir cabecera manualmente
→ corregir estilo
→ sincronizarlo visualmente con CV
→ volver a generar PDF
```

---

## 8. Cabecera canónica de candidatura

La cabecera es obligatoria en `modo_documento`.

Debe utilizar el mismo sistema canónico de identidad profesional utilizado por el CV.

No debe crearse una definición separada para la carta si puede reutilizarse la existente.

Arquitectura preferente:

```text
fuente canónica de identidad
        ↓
cabecera_candidatura
        ├── CV
        └── carta
```

Debe evitarse:

```text
cabecera_cv
cabecera_carta_copiada
```

con mantenimiento independiente.

---

## 9. Identidad y coherencia con el CV

La cabecera de carta debe ser igual o coherente con la cabecera canónica del CV en los elementos que formen parte de ese sistema:

- nombre;
- identificación profesional, cuando proceda;
- datos de contacto autorizados;
- jerarquía visual;
- familia tipográfica;
- tamaños relativos;
- alineación;
- espaciados;
- separadores;
- tratamiento del contacto;
- elementos visuales;
- reglas de presentación.

La carta no tiene que copiar el layout completo del CV.

El objetivo es compartir identidad documental, no convertir la carta en un CV.

---

## 10. Cabecera como presentación, no contenido

La cabecera pertenece a:

```text
presentación_documental
```

y no a:

```text
texto_semantico_carta
```

Por tanto:

```text
DOCX/PDF formal
=
elementos_presentacion_documental
+
texto_semantico_carta
```

La presencia de una cabecera autorizada no constituye por sí misma una adición semántica ilícita al cuerpo.

Las verificaciones deben poder distinguir ambos planos.

---

## 11. Fuente canónica de la cabecera

El compositor no debe obtener la cabecera copiando texto extraído del `cv.docx` o `cv.pdf`.

Debe investigar y reutilizar la fuente estructurada, helper, modelo intermedio, configuración, componente o contrato que utilice realmente el generador de CV.

Prioridad:

1. reutilización directa de un componente ya compartible;
2. extracción mínima de un helper común;
3. reutilización de configuración común;
4. adaptación mínima del mecanismo existente.

No debe realizarse una refactorización amplia del compositor de CV si una solución menor y limpia resuelve el contrato.

---

## 12. Datos privados de cabecera

La cabecera no autoriza a recuperar datos personales por iniciativa propia.

Todo dato visible debe:

1. pertenecer a la identidad documental autorizada de la candidatura;
2. respetar el contrato vigente de privacidad;
3. proceder de una fuente estructurada autorizada;
4. coincidir con los datos que el sistema permite usar en el CV.

Queda prohibido añadir por la cabecera:

- segundo apellido no autorizado;
- LinkedIn no autorizado;
- ubicación no autorizada;
- teléfono alternativo;
- correo alternativo;
- cualquier dato personal no aprobado.

Regla bloqueante:

```text
dato personal nuevo no autorizado
→ composición no apta
```

---

## 13. Precondiciones

Antes de `modo_documento` deben cumplirse:

- existe `contenido-carta-presentacion.md`;
- `estado_contenido: apto`;
- `GATE-CONTENIDO-CARTA-COMPOSICION` aprobado humanamente;
- candidatura vigente;
- `presentada: false`;
- existe `Carta completa consolidada`;
- la fuente canónica de cabecera puede resolverse;
- los datos de cabecera están autorizados;
- no existen incidencias semánticas abiertas.

Si falla una precondición material:

```text
→ no componer
→ registrar bloqueo
```

---

## 14. Fuente semántica cerrada

La única fuente autorizada para el cuerpo de la carta es:

```text
contenido-carta-presentacion.md
→ Carta completa consolidada
```

Está prohibido recuperar texto adicional desde:

- `datos-core-busqueda.md`;
- `analisis-oferta.md`;
- `candidatura.md`;
- `guion-carta-presentacion.md`;
- CV;
- oferta;
- web de empresa;
- fuentes externas;
- memoria del modelo.

Los documentos necesarios para resolver la cabecera solo pueden utilizarse para presentación e identidad documental autorizada.

---

## 15. Inmutabilidad semántica

Durante composición queda prohibido:

- escribir;
- reescribir;
- resumir;
- ampliar;
- parafrasear;
- mejorar estilo;
- mejorar naturalidad;
- corregir redacción;
- cambiar tono;
- cambiar palabras;
- cambiar cifras;
- cambiar evidencias;
- cambiar tiempos verbales;
- reordenar argumentos;
- eliminar frases;
- añadir frases.

Si se detecta un defecto semántico:

```text
→ no corregir en composición
→ requiere_revision_contenido
```

---

## 16. Modelo de comparación

La verificación debe mantener separados:

```text
texto_semantico_carta
```

y:

```text
elementos_presentacion_documental
```

La comparación semántica debe comprobar:

```text
Carta completa consolidada
=
cuerpo de DOCX
=
cuerpo de PDF
```

La comparación documental debe comprobar adicionalmente:

```text
cabecera DOCX
=
cabecera PDF
=
cabecera canónica autorizada
```

No es correcto comparar el texto completo del DOCX contra el cuerpo semántico y declarar la cabecera como una adición ilícita.

---

## 17. Normalizaciones permitidas

Solo se permiten normalizaciones técnicas que no cambien significado, por ejemplo:

- representación de saltos de línea;
- espaciado técnico;
- caracteres tipográficos equivalentes;
- propiedades de párrafo;
- control de viudas y huérfanas;
- hipervínculos;
- caracteres de no separación.

Una normalización no puede:

- eliminar palabras;
- añadir palabras;
- modificar cifras;
- modificar orden semántico;
- fundir frases;
- cambiar puntuación con impacto semántico.

---

## 18. Composición determinista

Con las mismas:

- fuentes;
- versión de compositor;
- configuración;
- cabecera;
- autorizaciones;

la composición debe producir resultados funcionalmente equivalentes.

No se debe introducir generación lingüística ni decisión editorial durante la composición.

### Contrato de párrafos y elementos documentales

Las líneas físicas consecutivas no vacías de `contenido-carta-presentacion.md`
forman un único párrafo semántico y se unen con espacios. Solo una línea vacía
separa párrafos. El compositor no convierte el hard wrapping Markdown en
`<w:br/>` ni en saltos manuales de Word. El cuerpo narrativo se justifica una
vez reconstruidos los párrafos; saludo y firma conservan su alineación
funcional.

La fecha y el asunto son estructura documental, no contenido libre: se derivan
exclusivamente de la fecha de composición y del puesto/empresa confirmados en
la candidatura. La jerarquía visual vigente es Calibri, nombre 18 pt negrita,
titular 11 pt, contacto 10,5 pt y cuerpo 11 pt. Si alguno de esos datos no puede
derivarse sin inventar, la composición se bloquea.

---

## 19. DOCX

El DOCX debe:

- abrir correctamente;
- incluir la cabecera;
- conservar el cuerpo íntegro;
- ser editable;
- no contener comentarios;
- no contener control de cambios;
- no contener campos extraños;
- no contener texto oculto no autorizado;
- mantener jerarquía legible;
- conservar datos autorizados;
- evitar superposición;
- evitar líneas cortadas;
- evitar páginas vacías inesperadas.

---

## 20. PDF

El PDF debe:

- derivarse del documento compuesto;
- incluir la misma cabecera;
- mantener el mismo cuerpo;
- renderizar correctamente;
- mantener caracteres;
- evitar cortes;
- evitar superposición;
- evitar páginas vacías inesperadas;
- mantener datos de contacto completos;
- ser visualmente coherente con el DOCX.

---

## 21. Paginación

Objetivo preferente:

```text
1 página
```

No es una obligación absoluta si para conseguirla fuera necesario deteriorar:

- legibilidad;
- tamaño de fuente;
- espaciado mínimo razonable;
- integridad del contenido.

Está prohibido resumir o eliminar contenido para forzar una página.

Si el contenido no cabe de manera profesional:

```text
→ requiere_correccion_composicion
```

---

## 22. Coherencia visual con el CV

La composición debe comprobar explícitamente:

- cabecera;
- tipografía;
- identidad;
- tratamiento del nombre;
- tratamiento del contacto;
- jerarquía;
- sistema visual.

Debe evitar:

- decoración nueva no compartida;
- elementos gráficos sin función;
- diseño que compita con el contenido;
- una estética independiente que haga parecer CV y carta documentos de candidaturas distintas.

---

## 23. Render y revisión visual

El registro separa siempre generación de inspección:

```yaml
render_generado: true | false
render_inspeccionado: true | false
revision_visual: no_realizada | ejecutada
evidencia_inspeccion: ruta_o_registro_de_la_inspeccion
```

Crear un PNG o comprobar que existe una página no equivale a inspeccionarlo.
`revision_visual: ejecutada` solo es válido con evidencia de revisión real.

La revisión visual solo puede declararse realizada si se ha inspeccionado efectivamente el render.

Debe comprobar al menos:

- cabecera visible;
- alineación;
- espaciado;
- cortes;
- solapamientos;
- saltos;
- página vacía;
- tipografía;
- estabilidad general;
- coherencia con CV.

Si no se ha realizado revisión visual:

```text
revision_visual: no_realizada
```

No debe inferirse a partir de tests estructurales.

---

## 24. Estados de composición

Valores:

```text
apta
requiere_correccion_composicion
requiere_revision_contenido
bloqueada
```

Precedencia:

```text
bloqueada
>
requiere_revision_contenido
>
requiere_correccion_composicion
>
apta
```

---

## 25. `apta`

Solo puede declararse `apta` cuando:

### Entrada

- contenido apto;
- gate de entrada aprobado;
- candidatura vigente;
- privacidad resoluble.

### Modo texto

- `Carta completa consolidada` permanece intacta;
- no se ha creado una segunda fuente;
- no se ha introducido cabecera.

### Modo documento

- DOCX generado;
- PDF generado;
- cabecera canónica presente;
- cabecera coherente con CV;
- cabecera DOCX = cabecera PDF;
- cuerpo fuente = cuerpo DOCX;
- cuerpo fuente = cuerpo PDF;
- cuerpo DOCX = cuerpo PDF;
- sin omisiones;
- sin adiciones semánticas;
- sin cambios de cifras;
- sin cambios de orden;
- sin datos privados no autorizados;
- render apto;
- documentos utilizables sin edición manual.

---

## 26. Gate de salida

La composición técnicamente `apta` puede habilitar:

```text
GATE-CARTA-REVISION-HUMANA
```

pero no lo aprueba.

La aprobación corresponde exclusivamente a la persona responsable.

El gate autoriza únicamente la revisión humana de los documentos generados.

No autoriza:

- veredicto final;
- envío o presentación externa;
- modificación de estado a `presentada: true`.

---

## 27. Auditoría obligatoria

Cada ejecución en `modo_documento` debe actualizar o generar:

```text
evaluacion-composicion-carta-presentacion.md
```

Debe registrar al menos:

- versión del playbook;
- versión del template;
- modo;
- fuente semántica;
- hash o identificador;
- generador;
- cabecera;
- origen de cabecera;
- versión o identificador;
- reutilización de cabecera CV;
- autorización de datos;
- DOCX;
- PDF;
- equivalencia del cuerpo;
- equivalencia de cabecera;
- revisión visual;
- incidencias;
- resultado.

---

## 28. Tests contractuales mínimos

Deben mantenerse los tests existentes y añadirse como mínimo:

### T15 — Cabecera canónica obligatoria

Cuando se genera DOCX/PDF:

```text
→ existe cabecera
→ procede del mecanismo canónico
→ coincide con el sistema utilizado por el CV
→ no requiere edición manual
```

### T16 — Canal texto independiente

La cabecera documental:

```text
→ no modifica Carta completa consolidada
→ no modifica contenido-carta-presentacion.md
→ no aparece en modo_texto
```

### T17 — Cabecera ausente

Si `modo_documento` no puede aplicar cabecera:

```text
→ no apta
```

### T18 — Cabecera divergente

Si la cabecera de carta diverge materialmente del sistema canónico del CV:

```text
→ no apta
```

### T19 — Privacidad de cabecera

Si aparece un dato personal no autorizado:

```text
→ no apta
```

### T20 — Cuerpo intacto con cabecera

Una cabecera válida no debe afectar a la comparación semántica del cuerpo.

### T21 — DOCX/PDF comparten cabecera

Debe verificarse:

```text
cabecera DOCX
=
cabecera PDF
```

### T22 — Fuente semántica inmutable

La ejecución no modifica:

```text
contenido-carta-presentacion.md
```

---

## 29. Regla de defectos generalizables

Si una candidatura real descubre un defecto generalizable:

```text
defecto real
→ regla del playbook
→ reflejo en template
→ test automático cuando sea viable
→ regeneración desde fuentes canónicas
```

No resolver únicamente el caso concreto.

---

## 30. Prohibiciones

Este playbook no puede:

- modificar `contenido-carta-presentacion.md`;
- modificar `guion-carta-presentacion.md`;
- modificar `candidatura.md` salvo que otro contrato lo autorice expresamente;
- recuperar hechos para ampliar el cuerpo;
- redactar una segunda carta;
- crear `carta-presentacion.txt`;
- generar una cabecera independiente mantenida aparte si existe una fuente canónica reutilizable;
- presentar externamente la candidatura;
- aprobar gates humanos;
- diseñar el veredicto final.

---

## 31. Criterio de éxito

La fase es correcta cuando:

```text
MODO TEXTO
Carta completa consolidada
→ disponible intacta para copiar/pegar
```

y:

```text
MODO DOCUMENTO
cabecera canónica compartida con CV
+
Carta completa consolidada intacta
→ DOCX
→ PDF
```

con:

- trazabilidad;
- privacidad;
- equivalencia verificable;
- render correcto;
- coherencia visual;
- ausencia de edición manual necesaria.

---

## 32. Historial

### v1.0.0

Primera versión operativa de composición DOCX/PDF con fuente semántica cerrada, equivalencia, privacidad, render y auditoría.

### v1.1.0

Se incorpora formalmente:

- distinción `modo_texto` / `modo_documento`;
- uso directo de `Carta completa consolidada` para copiar/pegar;
- prohibición de `.txt`;
- cabecera canónica obligatoria en documentos;
- reutilización del sistema de cabecera del CV;
- separación cuerpo semántico / elementos documentales;
- equivalencia específica de cuerpo y cabecera;
- controles de privacidad de cabecera;
- nuevos tests contractuales;
- exigencia de documento formal listo para uso sin edición manual.
