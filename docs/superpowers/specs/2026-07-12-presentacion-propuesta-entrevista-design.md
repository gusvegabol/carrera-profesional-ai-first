# Diseño: presentación de la propuesta recomendada

## Objetivo

Crear una presentación HTML autónoma de siete pantallas para explicar, en unos diez minutos y a una audiencia no experta, por qué la entrevista recomendada combina un panorama libre de la trayectoria con una inmersión selectiva en uno o dos episodios.

La fuente de contenido es [la evaluación experta](<../../Ideas debate - como afrontar entrevista cobertura profesional/05_Evaluacion_experta_y_recomendacion_de_enfoque.md>). La presentación explica una recomendación debatible; no certifica competencias ni convierte ESCO en prueba individual.

## Entrega y navegación

- Crear un único archivo autónomo en `docs/Ideas debate - como afrontar entrevista cobertura profesional/06_Presentacion_propuesta_recomendada.html`.
- Incluir HTML, CSS y JavaScript en el propio archivo; no cargar fuentes, bibliotecas, imágenes ni datos remotos.
- Mostrar una pantalla por vez, con botones anterior/siguiente, puntos de progreso, teclas de flecha y la tecla Inicio para volver a la primera pantalla.
- Adaptarse a pantalla de escritorio y móvil; respetar `prefers-reduced-motion`.

## Estructura narrativa

1. **Portada:** la pregunta humana: «¿Cómo escuchamos toda una trayectoria sin convertirla en un formulario?»
2. **El problema:** una carrera puede tener saltos, pausas, cambios y aprendizajes que un CV no muestra.
3. **La decisión:** la doble pasada es la recomendación porque separa cobertura y evidencia.
4. **Primera pasada:** conversación libre y panorama de toda la trayectoria.
5. **Segunda pasada:** la persona elige uno o dos episodios para profundizar con preguntas concretas.
6. **Tres garantías:** libertad de recorrido, evidencia corregible y control de privacidad; ESCO aparece como referencia candidata posterior.
7. **Resultado y piloto:** perfil inicial útil, preguntas pendientes y qué se validará con entrevistas reales.

## Dirección visual

- Usar una paleta clara y cálida: fondo marfil, verde petróleo para estructura, coral para decisiones y amarillo para énfasis.
- Usar tipografía con carácter disponible localmente, apoyada por serif para mensajes humanos y sans serif para navegación.
- Representar las ideas mediante gráficos CSS: recorrido discontinuo, dos pasadas, tarjetas de evidencia y un perfil de salida. Evitar diagramas técnicos y tablas densas.
- Mantener cada pantalla en una idea principal, texto breve y una ilustración dominante.

## Calidad y comprobación

- Todos los textos estarán en español con ortografía revisada.
- El HTML enlazará al informe de evaluación como fuente de la recomendación.
- Verificar la carga sin conexión, navegación mediante controles y teclado, ausencia de errores de consola, adaptación móvil y reducción de movimiento.
