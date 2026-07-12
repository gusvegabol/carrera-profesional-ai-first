# Presentación de la propuesta de entrevista Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crear una presentación HTML autónoma, de siete pantallas y diez minutos de duración, que explique a personas no expertas la propuesta recomendada de entrevista de cobertura profesional.

**Architecture:** Un único documento HTML contendrá contenido, estilos y comportamiento. Las siete secciones semánticas se alternarán mediante una clase `is-active`; un bloque JavaScript pequeño gestionará botones, puntos de progreso, teclado y la actualización accesible del contador.

**Tech Stack:** HTML5, CSS3 y JavaScript del navegador; PowerShell para comprobaciones estáticas locales.

## Global Constraints

- Crear solo `docs/Ideas debate - como afrontar entrevista cobertura profesional/06_Presentacion_propuesta_recomendada.html`.
- No usar dependencias, recursos remotos, imágenes externas, fuentes web ni bibliotecas.
- Conservar los cuatro documentos de ideas, el informe de evaluación y PCS sin cambios.
- Usar español con tildes, eñes y signos de apertura; presentar una recomendación debatible, no una certificación.
- Implementar siete pantallas: problema, decisión, doble pasada, primera pasada, segunda pasada, garantías y piloto.
- Funcionar con botones, puntos de progreso, flechas de teclado, `Home`, `prefers-reduced-motion` y pantallas móviles.

---

### Task 1: Crear el mazo HTML y su comportamiento de navegación

**Files:**
- Create: `docs/Ideas debate - como afrontar entrevista cobertura profesional/06_Presentacion_propuesta_recomendada.html`
- Test: comprobación PowerShell local sobre el archivo HTML creado

**Interfaces:**
- Consumes: `05_Evaluacion_experta_y_recomendacion_de_enfoque.md` como fuente de la recomendación y los complementos.
- Produces: un archivo HTML autónomo que puede abrirse desde el sistema de archivos sin servidor ni conexión.

- [ ] **Step 1: Ejecutar la comprobación inicial y confirmar que falla porque el HTML aún no existe**

```powershell
$html = 'docs\Ideas debate - como afrontar entrevista cobertura profesional\06_Presentacion_propuesta_recomendada.html'
if (Test-Path -LiteralPath $html) {
  throw 'La comprobación inicial esperaba que el HTML no existiera.'
}
throw 'Fallo esperado: falta la presentación HTML.'
```

Expected: el comando termina con `Fallo esperado: falta la presentación HTML.`

- [ ] **Step 2: Crear el documento HTML con estructura semántica y contenido de siete pantallas**

Usar esta estructura y estos identificadores; el texto debe mantener el vocabulario cotidiano definido por el diseño:

```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Una entrevista que escucha toda la trayectoria</title>
  <style>
    :root { --ink: #153936; --paper: #f7f0e4; --coral: #e7684a; --sun: #f2c84b; }
    .slide { display: none; }
    .slide.is-active { display: grid; }
    @media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation: none !important; transition: none !important; } }
  </style>
</head>
<body>
  <main id="deck" aria-labelledby="deck-title">
    <section class="slide is-active" data-slide="0" aria-hidden="false">...</section>
    <section class="slide" data-slide="1" aria-hidden="true">...</section>
    <section class="slide" data-slide="2" aria-hidden="true">...</section>
    <section class="slide" data-slide="3" aria-hidden="true">...</section>
    <section class="slide" data-slide="4" aria-hidden="true">...</section>
    <section class="slide" data-slide="5" aria-hidden="true">...</section>
    <section class="slide" data-slide="6" aria-hidden="true">...</section>
  </main>
  <nav aria-label="Navegación de la presentación">
    <button type="button" id="previous-slide" aria-label="Pantalla anterior">Anterior</button>
    <div id="progress-dots" role="tablist" aria-label="Pantallas de la presentación"></div>
    <button type="button" id="next-slide" aria-label="Pantalla siguiente">Siguiente</button>
  </nav>
  <p id="slide-status" aria-live="polite"></p>
  <script>
    const slides = [...document.querySelectorAll('.slide')];
    const dots = document.getElementById('progress-dots');
    const status = document.getElementById('slide-status');
    let current = 0;
    function goTo(index) {
      current = Math.min(Math.max(index, 0), slides.length - 1);
      slides.forEach((slide, position) => {
        const active = position === current;
        slide.classList.toggle('is-active', active);
        slide.setAttribute('aria-hidden', String(!active));
      });
      [...dots.children].forEach((dot, position) => {
        const active = position === current;
        dot.setAttribute('aria-selected', String(active));
        dot.tabIndex = active ? 0 : -1;
      });
      status.textContent = `Pantalla ${current + 1} de ${slides.length}`;
    }
    slides.forEach((slide, index) => {
      const dot = document.createElement('button');
      dot.type = 'button';
      dot.role = 'tab';
      dot.ariaLabel = `Ir a la pantalla ${index + 1}`;
      dot.addEventListener('click', () => goTo(index));
      dots.append(dot);
    });
    document.getElementById('previous-slide').addEventListener('click', () => goTo(current - 1));
    document.getElementById('next-slide').addEventListener('click', () => goTo(current + 1));
    window.addEventListener('keydown', event => {
      if (event.key === 'ArrowRight') goTo(current + 1);
      if (event.key === 'ArrowLeft') goTo(current - 1);
      if (event.key === 'Home') goTo(0);
    });
    goTo(0);
  </script>
</body>
</html>
```

Rellenar las secciones con el siguiente contenido, apoyado por ilustraciones CSS de recorrido, dos pasadas, tarjetas de evidencia y perfil de salida:

1. «¿Cómo escuchamos toda una trayectoria sin convertirla en un formulario?»
2. Trayectorias con cambios, pausas, actividades paralelas y aprendizajes invisibles en un CV.
3. La recomendación: «doble pasada» para cubrir primero y profundizar después.
4. Primera pasada: panorama libre, anclas y preguntas pendientes; la persona puede empezar por donde quiera.
5. Segunda pasada: elegir uno o dos episodios; preguntar por situación, acción y resultado sin convertirlo en un examen.
6. Garantías: conversación no lineal, afirmaciones con evidencia y límite, privacidad bajo control, ESCO como correspondencia candidata posterior.
7. Piloto: perfil inicial útil, revisión de la persona y aprendizaje con entrevistas reales.

- [ ] **Step 3: Ejecutar la comprobación estática y confirmar que la estructura y los requisitos son válidos**

```powershell
$html = 'docs\Ideas debate - como afrontar entrevista cobertura profesional\06_Presentacion_propuesta_recomendada.html'
$content = Get-Content -Raw -LiteralPath $html
$required = @(
  '<html lang="es">',
  'class="slide is-active"',
  'data-slide="6"',
  'id="previous-slide"',
  'id="next-slide"',
  'id="progress-dots"',
  'prefers-reduced-motion',
  'ArrowRight',
  'ArrowLeft',
  'Una entrevista que escucha toda la trayectoria',
  'Doble pasada',
  'ESCO como correspondencia candidata posterior'
)
foreach ($item in $required) {
  if (-not $content.Contains($item)) { throw "Falta el requisito: $item" }
}
if (([regex]::Matches($content, 'class="slide')).Count -ne 7) {
  throw 'La presentación debe contener exactamente siete pantallas.'
}
if ($content -match 'https?://') { throw 'La presentación debe ser autónoma y no cargar recursos remotos.' }
'Comprobación estática correcta.'
```

Expected: `Comprobación estática correcta.`

- [ ] **Step 4: Revisar manualmente el HTML en escritorio y móvil**

Abrir el archivo local y comprobar lo siguiente:

1. Los botones anterior y siguiente cambian de pantalla sin recargar.
2. Las flechas cambian de pantalla y `Home` vuelve a la primera.
3. Los puntos de progreso seleccionan cada pantalla y anuncian el estado.
4. En una ventana estrecha no aparece desplazamiento horizontal y el texto sigue siendo legible.
5. La última pantalla enlaza a `05_Evaluacion_experta_y_recomendacion_de_enfoque.md` como fuente de la recomendación.

- [ ] **Step 5: Comprobar el cambio y crear el commit de la presentación**

```powershell
git diff --check
git add -- 'docs/Ideas debate - como afrontar entrevista cobertura profesional/06_Presentacion_propuesta_recomendada.html'
git commit -m 'docs: add interview proposal presentation'
```

Expected: sin errores de espacios; el commit contiene solo el HTML de la presentación.

## Self-Review

- El plan cubre las siete pantallas, navegación, accesibilidad, diseño autónomo, móvil y fuente de la recomendación.
- No usa dependencias ni inventa validaciones académicas; el contenido mantiene que se trata de una propuesta a contrastar.
- Los únicos identificadores JavaScript definidos son `slides`, `dots`, `status`, `current` y `goTo`, y se usan de forma coherente en el HTML y las comprobaciones.
