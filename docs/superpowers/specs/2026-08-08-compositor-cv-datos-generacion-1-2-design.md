# Diseño del compositor de CV para `datos-generacion.json` 1.2

**Fecha:** 2026-08-08  
**Estado:** aprobado para implantación, salvo la excepción sin fotografía  
**Caso piloto:** CAND-2026-020  
**Caso de generalización:** CAND-2026-019

## 1. Objetivo

Adaptar el generador documental de Job-up al contrato CV-only 1.2 sin reducir ese contrato a los marcadores, límites de cantidad ni estructura fija del generador histórico.

El flujo activo será:

```text
datos-generacion.json 1.2
→ validación contractual
→ modelo intermedio pasivo
→ renderizado DOCX y LaTeX
→ conversión DOCX→PDF
→ validación y publicación transaccional
→ cv.docx + cv.pdf + cv.tex
```

## 2. Fuente semántica y determinismo

El compositor consume como única fuente semántica `contenido_cv` del JSON aprobado. Utiliza únicamente:

- `encabezado.nombre_completo`;
- `encabezado.unidades`;
- `encabezado.contacto`;
- `secciones`;
- `bloques`;
- `cabecera`;
- `unidades`;
- los correspondientes campos `tipo`, `rol`, `titulo_visible`, `texto` y `orden`.

Las colecciones se ordenan numéricamente por `orden`. El texto visible se reproduce literalmente: el compositor no resume, corrige, fusiona, divide ni reescribe.

`candidatura`, `generacion`, `control` y la trazabilidad permiten validar el artefacto, pero no aportan texto visible ni decisiones editoriales.

El compositor no consulta `candidatura.md`, `guion-adaptacion-cv.md`, `analisis-oferta.md`, `datos-core-busqueda.md` ni el seguimiento para decidir contenido.

## 3. Modelo intermedio pasivo

Se introduce un árbol de renderizado inmutable y común a los dos formatos editables:

- `RenderCV` contiene encabezado y secciones;
- `RenderEncabezado` contiene nombre, unidades y contactos;
- `RenderSeccion` contiene tipo, título visible y bloques;
- `RenderBloque` contiene tipo, cabecera y unidades;
- cada elemento textual conserva su texto literal, orden y rol o tipo de presentación.

El modelo se construye en una función pura a partir de `contenido_cv`. DOCX y LaTeX reciben el mismo árbol ya ordenado y no vuelven a interpretar el JSON.

## 4. Renderizado

### 4.1 DOCX

El renderizador conserva de la plantilla canónica los márgenes, estilos, paleta y composición del encabezado que resulten reutilizables. Sustituye el cuerpo de marcadores fijos por párrafos dinámicos creados desde el modelo intermedio.

Las cabeceras de bloque se presentan en el orden declarado y las unidades respetan `parrafo`, `bullet` o `linea`. No existen límites artificiales de experiencias, competencias, formación o secciones.

### 4.2 LaTeX

El renderizador genera una estructura dinámica, escapa únicamente los caracteres técnicos necesarios para preservar literalmente el texto visible y mantiene el orden del modelo intermedio. No utiliza slots numerados.

### 4.3 PDF

`cv.pdf` procede exclusivamente de convertir el `cv.docx` generado mediante `soffice.com`, perfil temporal aislado y una sola ejecución. Se conserva el límite vigente de dos páginas y el mecanismo de revisión humana cuando se exceda.

## 5. Fotografía

### 5.1 Decisión aprobada

Todo CV incluye por defecto la fotografía canónica autorizada:

`boveda-entrevista-profesional/busqueda-empleo/foto-perfil.png`

La fotografía es un recurso técnico de composición, no contenido semántico de `datos-generacion.json`. El compositor no la busca ni la elige heurísticamente. Si falta, es inválida o no puede incorporarse, la generación falla antes de publicar.

### 5.2 Vacío contractual detectado

La guía de formato y las plantillas históricas permiten excluir la fotografía mediante instrucción expresa «en la invocación». Sin embargo, el inicio de candidatura no dispone de un campo o artefacto persistente equivalente a `incluir_fotografia: true|false`. Por ello no existe una ruta determinista y auditable para transportar la excepción hasta el compositor.

La excepción sin fotografía queda fuera de la implantación hasta obtener aprobación contractual.

### 5.3 Modificación mínima propuesta, pendiente de aprobación

- **Documento que cambiaría:** `TEMPLATE_CANDIDATURA_v2.md` y el contrato de `PLAYBOOK_CANDIDATURA.md`; la SPEC 0.4.0 registraría la regla transversal.
- **Campo:** `incluir_fotografia: true|false` en el frontmatter de `candidatura.md`.
- **Valor predeterminado:** `true`.
- **Autoridad:** la persona responsable de la candidatura.
- **Momento:** inicio de la candidatura, antes de generar contenido o documentos.
- **Transporte:** el orquestador técnico leería exclusivamente ese valor operativo y entregaría al compositor un perfil técnico cerrado. El compositor seguiría sin consultar la ficha ni usarla como fuente semántica.

Esta propuesta no se implanta mientras no sea aprobada.

## 6. Infraestructura reutilizada

Se conservan y generalizan:

- resolución segura de rutas y rechazo de escapes;
- configuración local de proyecto y `soffice.com`;
- validación de fotografía;
- bloqueo por candidatura;
- temporales por ejecución;
- conversión DOCX→PDF;
- validaciones estructurales de DOCX, PDF y LaTeX;
- límite de páginas y revisión humana;
- manifiesto, publicación transaccional y restauración;
- registro de errores y limpieza.

La publicación se parametriza para tres salidas: `cv_docx`, `cv_pdf` y `cv_tex`.

## 7. Elementos retirados del flujo activo

- contrato JSON 1.0;
- `carta` y `latex` como copias semánticas del contenido;
- plantillas y salidas de carta;
- marcadores fijos;
- seis posiciones de experiencia;
- cuatro posiciones de competencias;
- tres posiciones de formación;
- lectura de documentos externos para completar o decidir contenido.

Los recursos históricos pueden conservarse como archivo o referencia, pero no gobiernan el flujo 1.2.

## 8. Validación

La implantación debe acreditar:

1. construcción literal y ordenada del modelo intermedio;
2. cantidades variables y secciones heterogéneas;
3. equivalencia semántica entre DOCX y LaTeX;
4. fotografía predeterminada incorporada;
5. ausencia de carta;
6. publicación y restauración de tres artefactos;
7. rechazo de contratos, rutas y recursos inválidos;
8. independencia respecto a documentos no autorizados;
9. generación real de CAND-2026-020 y CAND-2026-019;
10. inspección estructural de DOCX y LaTeX y revisión visual de los PDF producidos.

## 9. Criterio de finalización

La adaptación queda lista para revisión cuando los dos casos reales producen exclusivamente `cv.docx`, `cv.pdf` y `cv.tex`, sus textos y orden coinciden con `contenido_cv`, incluyen la fotografía canónica, superan las validaciones técnicas y no dependen de fuentes semánticas externas.
