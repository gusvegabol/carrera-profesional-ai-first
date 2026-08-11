# Índice operativo de Job-up

Este índice define dónde viven los contratos operativos y dónde termina la
fase actual de generación documental.

## Flujo canónico

```text
OFERTA
  ↓
PLAYBOOK_ANALISIS_OFERTA → analisis-oferta.md
  ↓
PLAYBOOK_CANDIDATURA → candidatura.md
  ↓
PLAYBOOK_GUION_ADAPTACION_CV → guion-adaptacion-cv.md
  ↓ GATE-GUION-CV-CONTENIDO
PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA → datos-generacion.json
  ↓ GATE-CONTENIDO-CV-COMPOSICION
PLAYBOOK_COMPONER_CV → cv.docx / cv.pdf / cv.tex
  ↓ revisión humana + GATE-VEREDICTO-CV
PLAYBOOK_GUION_CARTA_PRESENTACION → guion-carta-presentacion.md
  ↓ GATE-GUION-CARTA-CONTENIDO
PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION → contenido-carta-presentacion.md
  ↓ GATE-CONTENIDO-CARTA-COMPOSICION
PLAYBOOK_COMPONER_CARTA_PRESENTACION → carta-presentacion.docx / carta-presentacion.pdf
  ↓ revisión humana + GATE-VEREDICTO-CARTA
CANDIDATURA DOCUMENTALMENTE COMPLETA
  ↓
FIN DEL ALCANCE ACTUAL
```

La rama de carta se ejecuta solo cuando la candidatura la requiere. La
presentación externa no es una fase de este flujo y `presentada` no cambia por
la existencia de documentos aprobados. Tras `CANDIDATURA DOCUMENTALMENTE
COMPLETA` no existe ningún módulo activo posterior.

## Playbooks vigentes

Todos los playbooks operativos de Job-up están en este directorio:

- `PLAYBOOK_CANDIDATURA_POR_OFERTA.md`
- `PLAYBOOK_ANALISIS_OFERTA.md`
- `PLAYBOOK_CANDIDATURA.md`
- `PLAYBOOK_GUION_ADAPTACION_CV.md`
- `PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA.md`
- `PLAYBOOK_COMPONER_CV.md`
- `PLAYBOOK_VEREDICTO_FINAL_CV.md`
- `PLAYBOOK_GUION_CARTA_PRESENTACION.md`
- `PLAYBOOK_GENERAR_CONTENIDO_CARTA_PRESENTACION.md`
- `PLAYBOOK_COMPONER_CARTA_PRESENTACION.md`
- `PLAYBOOK_VEREDICTO_FINAL_CARTA.md`

## Templates vigentes

Los templates de Job-up están en
`boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/`.
Incluyen análisis, candidatura, guiones, contenido CV, revisión, composición,
formatos visuales y veredictos de CV y carta.

## Scripts y artefactos

- Scripts: `scripts/job-up/`; `orquestar_transiciones.py` representa la
  selección determinista de composición, veredicto, espera humana y cierre.
- Expedientes: `boveda-entrevista-profesional/busqueda-empleo/candidaturas/`.
- Histórico: `historico/`, preservando la ruta de procedencia.
- Investigación y diseños: `docs/ideas-y-debates/mejoras-job-up/`.

## Fuera de alcance y líneas futuras

- La presentación automatizada asistida por IA queda documentada en
  `docs/ideas-y-debates/mejoras-job-up/futuro/presentacion/`; no se ejecuta.
- El entorno inicial de preguntas/configuración se conserva como línea futura
  en la SPEC; no se implementan UI, wizard, servidor, plugin ni campos nuevos.
- No se almacenan credenciales ni se inicia sesión en portales.
