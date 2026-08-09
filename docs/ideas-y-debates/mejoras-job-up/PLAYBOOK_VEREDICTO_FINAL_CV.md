---
id: PLAYBOOK_VEREDICTO_FINAL_CV
tipo: playbook
version: "1.1.0"
estado: vigente
artefacto_salida: veredicto-final-cv.md
revision_humana_previa: revision-humana-cv.md
gate_salida: GATE-VEREDICTO-CV
---

# PLAYBOOK_VEREDICTO_FINAL_CV — v1.0.1

## Propósito y límites

Este playbook diagnostica si el CV final de una candidatura es íntegro, fiel al
flujo y suficientemente competitivo para recomendar su avance hacia presentación.
No redacta ni parchea el CV, no cambia estrategia, guion o `datos-generacion.json`,
no crea hechos, no genera carta, no presenta la candidatura y no aprueba el gate.

La recomendación de `aprobar` solo significa que el CV concreto puede pasar a la
decisión humana de `GATE-VEREDICTO-CV`. No significa que la candidatura completa
esté preparada, que exista carta o email, ni que pueda presentarse.

## Cambio contractual

Se incorpora como precondición formal:

```text
revision-humana-cv.md
```

Este artefacto registra la aceptación humana del CV generado y queda ligado inequívocamente a la versión/huella del PDF revisado.

---

## 2. Posición corregida en el flujo

```text
datos-generacion.json
        ↓
GATE-CONTENIDO-CV-COMPOSICION
        ↓
composición determinista
        ↓
cv.docx / cv.pdf / cv.tex
        ↓
REVISIÓN HUMANA DEL CV GENERADO
        ↓
revision-humana-cv.md
        ↓
PLAYBOOK_VEREDICTO_FINAL_CV
        ↓
veredicto-final-cv.md
        ↓
GATE-VEREDICTO-CV
```

La revisión humana y el veredicto continúan siendo responsabilidades diferentes.
Este playbook termina en la validación del CV. La preparación del paquete y el
gate de candidatura completa pertenecen a una fase posterior e independiente.

## Roles obligatorios

### Rol A — Recruiter senior + coach de carrera

Evalúa primer escaneo, posicionamiento, relevancia, encaje, diferenciación,
evidencia, seniority, sobrecualificación, ATS, narrativa, credibilidad, calidad
visual y competitividad real. Debe distinguir `CV correcto` de `candidatura
competitiva`.

### Rol B — Auditor senior de flujo agentic

Contrasta `analisis-oferta.md → candidatura.md → guion-adaptacion-cv.md →
datos-generacion.json → composición → CV`, comprobando pérdidas, añadidos,
desviaciones, privacidad, decisiones tomadas por la capa incorrecta y defectos
que pertenecen a fases anteriores.

---

## 6. Precondiciones obligatorias — versión corregida

No ejecutar el veredicto si falta cualquiera de estas condiciones:

- existe `cv.pdf`;
- existe `cv.docx`;
- existe `datos-generacion.json`;
- existe `guion-adaptacion-cv.md`;
- existe `candidatura.md`;
- existe `analisis-oferta.md`;
- existen las fuentes factuales necesarias;
- existe autorización vigente de datos privados;
- `GATE-CONTENIDO-CV-COMPOSICION` está aprobado;
- la composición terminó correctamente;
- existe `revision-humana-cv.md`;
- `revision-humana-cv.md` contiene una decisión humana válida;
- la revisión humana identifica inequívocamente el CV revisado;
- la huella/versión del CV revisado coincide con el `cv.pdf` sometido al veredicto;
- la candidatura mantiene `presentada: false`.

También bloquea si falta cualquiera de las fuentes, gates o autorizaciones
necesarias para reconstruir la trazabilidad completa.

### 6.1 Validación de identidad del CV

Antes de iniciar CAPA 1 debe comprobarse:

```yaml
revision_humana:
  artefacto: revision-humana-cv.md
  cv_revisado:
  huella_cv:
  decision:
  fecha:
  decidido_por:
```

Debe cumplirse:

```text
huella(revision-humana-cv.md)
==
huella(cv.pdf sometido a veredicto)
```

Si no coincide:

```yaml
estado_veredicto: bloqueado
motivo: revision_humana_corresponde_a_otra_version
```

No se ejecutan las capas de veredicto.

## Capas y resultados

1. **Integridad:** `apta` o `no_apta`, sin compensación por notas.
2. **Fidelidad al flujo:** `apta` o `no_apta`, incluyendo privacidad y el traspaso
   semántico exacto desde el JSON al CV.
3. **Calidad recruiter:** seis criterios C1–C6, cada uno de 1 a 5, solo si las
   capas anteriores son aptas.
4. **Diagnóstico competitivo:** cada debilidad se clasifica como
   `corregible_con_evidencia_existente` o `no_corregible_sin_nueva_evidencia`.

Los criterios son:

- C1 — Primer escaneo y posicionamiento.
- C2 — Encaje competitivo real.
- C3 — Cobertura ATS respaldada.
- C4 — Fuerza de la evidencia.
- C5 — Adecuación narrativa y seniority.
- C6 — Calidad documental y visual del PDF real.

Cada criterio registra nota, evidencia, fortaleza, debilidad, impacto recruiter,
mejora posible, capa propietaria y límite factual. La media es informativa y no
gobierna la precedencia.

Resultados globales permitidos, en esta precedencia:

```text
bloqueado_por_integridad
>
requiere_correccion_de_flujo
>
no_competitivo
>
revisar_antes_de_presentar
>
apto_para_presentacion
```

`no_competitivo` significa que el CV es correcto e íntegro, pero el encaje
material sigue siendo insuficiente. No se añaden keywords o hechos para evitarlo.

## Enrutamiento de defectos

```text
factual → fuente factual y propagación aguas arriba
estrategia → analisis-oferta.md / candidatura.md
guion → PLAYBOOK_GUION_ADAPTACION_CV
contenido → PLAYBOOK_GENERAR_CONTENIDO_CANDIDATURA
privacidad → autorización de candidatura
composicion → compositor / template
competitividad_no_corregible → decisión humana, sin maquillar
```

---

## 7. Artefacto principal evaluado — adición

El CV sometido al veredicto debe ser exactamente la versión identificada en:

```text
revision-humana-cv.md
```

No se permite utilizar como precondición una revisión realizada sobre una versión anterior.

---

## 8. Entradas autorizadas — adición

### 8.8 Revisión humana previa

```text
revision-humana-cv.md
```

Su única función dentro del veredicto es acreditar:

- CV revisado;
- huella o versión;
- decisión humana;
- fecha;
- identidad de la persona responsable cuando corresponda.

El veredicto no reinterpreta ni modifica esa decisión.

---

## 32. Regeneración e invalidación — versión corregida

Una regeneración material del CV produce simultáneamente:

```text
cv nuevo
→ revision-humana-cv.md anterior deja de ser vigente
→ veredicto-final-cv.md anterior deja de ser vigente
```

Secuencia obligatoria:

```text
nuevo cv.pdf
        ↓
nueva revisión humana
        ↓
nuevo revision-humana-cv.md
        ↓
nuevo veredicto
```

No puede reutilizarse una revisión humana anterior mediante simple cambio de referencia.

---

## 43. Criterios de aceptación — adiciones

El playbook se considera apto para implantación cuando, además:

- [ ] exige `revision-humana-cv.md`;
- [ ] exige identificar la huella del CV revisado;
- [ ] bloquea si la huella revisada y la huella evaluada no coinciden;
- [ ] invalida revisión y veredicto después de una regeneración material;
- [ ] no permite marcar manualmente una revisión genérica como sustituto de ese control.

---

## 44. Postcondiciones — precisión añadida

El veredicto debe registrar:

```yaml
revision_humana_origen:
  artefacto: revision-humana-cv.md
  huella_cv:
  decision:
```

La huella debe coincidir con la del CV identificado por el propio veredicto.

## Recomendación y gate humano

El playbook escribe `recomendacion_gate: aprobar` únicamente cuando el resultado
es `apto_para_presentacion`; en cualquier otro caso escribe `no_aprobar`. La
sección `decision_humana` solo puede quedar en `pendiente`, `aprobado` o
`bloqueado` y nunca la completa autónomamente la IA.

Una regeneración material del PDF invalida la revisión y el veredicto anteriores.
La secuencia obligatoria es: nuevo PDF → nueva revisión humana → nuevo veredicto.

La decisión humana de este gate valida únicamente el CV. No habilita
`GATE-CANDIDATURA-PRESENTACION`, no cambia `presentada`, no aprueba carta o
email y no autoriza ningún envío.

La investigación contextual externa queda fuera del veredicto base y requiere
autorización específica y URL propuestas antes de cualquier consulta.
