---
id: PLAYBOOK_COMPONER_CV
tipo: playbook
version: "1.0.0"
estado: vigente
alcance: exclusivo_composicion_cv
entrada_principal: datos-generacion.json
salidas:
  - cv.docx
  - cv.pdf
  - cv.tex
gate_entrada: GATE-CONTENIDO-CV-COMPOSICION
gate_salida: GATE-VEREDICTO-CV
template_principal: TEMPLATE_CV_FORMATO.docx
---

# Playbook de composición del CV

## Propósito

Este playbook transforma el contrato `datos-generacion.json` aprobado en los
tres artefactos del CV: `cv.docx`, `cv.pdf` y `cv.tex`. Es una operación de
composición determinista; no decide estrategia, no redacta contenido y no
consulta el canal de presentación.

## Entradas y límites

- Consume únicamente el JSON de contenido que haya superado
  `GATE-CONTENIDO-CV-COMPOSICION`.
- Usa las plantillas visuales canónicas de
  `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/`.
- Construye la cabecera mediante el helper canónico y respeta la autorización
  de datos privados registrada en el JSON.
- Incluye la fotografía autorizada por defecto; no la busca ni la elige por
  heurística.
- Ordena exclusivamente con los campos `orden` y conserva literalmente los
  textos de `contenido_cv`.
- No lee `candidatura.md`, `guion-adaptacion-cv.md`, `analisis-oferta.md`,
  `datos-core-busqueda.md` ni el seguimiento para decidir contenido.

## Procedimiento

1. Validar la ruta de entrada y la estructura del JSON.
2. Construir el modelo intermedio pasivo desde `contenido_cv`.
3. Renderizar DOCX, PDF mediante el procedimiento de conversión documentado y
   LaTeX desde el mismo modelo.
4. Comprobar que no quedan marcadores, que la fotografía existe y que DOCX,
   PDF y LaTeX contienen el mismo texto visible autorizado.
5. Registrar la revisión humana del PDF y su huella antes de completar
   `PLAYBOOK_VEREDICTO_FINAL_CV`.

## Salida y prohibiciones

La salida válida son únicamente `cv.docx`, `cv.pdf` y `cv.tex`, junto con los
registros de revisión/veredicto previstos por sus contratos. La composición no
abre gates de presentación, no inicia sesión, no rellena formularios y no
marca `presentada: true`.
