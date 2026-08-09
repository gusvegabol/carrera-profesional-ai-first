---
id: TEMPLATE_REVISION_HUMANA_CV
tipo: template
version: "1.0.1"
estado: vigente
artefacto_instancia: revision-humana-cv.md
---

# Revisión humana del CV generado

> Registra la revisión humana posterior a composición.
>
> No sustituye el veredicto final del CV.

## 1. Identificación

| Campo | Valor |
| --- | --- |
| Candidatura | `CAND-AAAA-NNN` |
| Empresa | |
| Puesto | |
| Fecha de revisión | |
| Persona responsable | |

## 2. CV revisado

| Campo | Valor |
| --- | --- |
| Archivo principal | `cv.pdf` |
| Huella / hash / identificador de versión | |
| Fecha de generación | |
| Número de páginas | |

La huella es el SHA-256 exacto del `cv.pdf` revisado. No se acepta una revisión
sin huella ni una huella perteneciente a otra versión.

## 3. Comprobaciones humanas mínimas

- [ ] El PDF puede abrirse y leerse correctamente.
- [ ] No se observan cortes, desbordamientos o errores graves de composición.
- [ ] La fotografía, cuando procede, aparece correctamente.
- [ ] Los datos de contacto visibles parecen correctos.
- [ ] El documento revisado corresponde a la candidatura indicada.
- [ ] No se detecta un defecto evidente que obligue a regenerarlo antes del veredicto.

## 4. Decisión

```yaml
revision_humana_cv:
  decision: aprobado_para_veredicto | requiere_correccion
  cv_revisado: cv.pdf
  huella_cv:
  fecha:
  decidido_por:
```

## 5. Observaciones

...

## 6. Regla de vigencia

> Esta revisión solo es válida para el CV cuya huella figura en este documento.

Cualquier regeneración material de `cv.pdf` invalida automáticamente esta revisión como revisión vigente.
