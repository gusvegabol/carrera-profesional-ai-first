---
id: estado-actual
titulo: carrera-profesional-ai-first
estado: vigente
fecha_actualizacion: 2026-07-12
ultima_sesion_relacionada: sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai
host: carrera-ai
---

# estado-actual

## Situación actual

El trabajo vigente del host permanece en la revisión metodológica de la entrevista de cobertura profesional. `docs/DOCUMENTO_SPEC_CARRERA_AI.md` sigue siendo la referencia funcional visible; no se ha modificado para esta línea de trabajo. El núcleo metodológico y el Perfil Profesional Accionable continúan siendo el marco para diseñar la cobertura de trayectorias profesionales sin sustituir el playbook de profundidad existente.

Se han elaborado cuatro propuestas para que una IA cubra toda la vida profesional de una persona, dos conservadoras y dos innovadoras. El informe `docs/Ideas debate - como afrontar entrevista cobertura profesional/05_Evaluacion_experta_y_recomendacion_de_enfoque.md` las compara con una rúbrica equilibrada y recomienda, de forma debatible, usar la Idea 2, doble pasada de panorama e inmersión selectiva, como arquitectura base de un primer piloto.

La recomendación requiere complementar esa arquitectura con la conversación no lineal, las anclas y los retornos opcionales de la Idea 1, y con un registro ligero de hipótesis, evidencia, límites y corrección por la persona de la Idea 4. El atlas relacional de la Idea 3 queda como posible evolución posterior, no como requisito del MVP. ESCO mantiene el papel de correspondencia candidata posterior, trazable y revisable; no prueba competencias individuales ni certifica a la persona.

También existe una presentación HTML autónoma para explicar la propuesta a personas no expertas: `docs/Ideas debate - como afrontar entrevista cobertura profesional/06_Presentacion_propuesta_recomendada.html`. Resume el problema, la doble pasada, sus garantías y el piloto propuesto.

Este resultado no adopta todavía un playbook ni constituye una decisión canónica de PCS. No se han creado acciones ni decisiones formales derivadas: la recomendación debe ser debatida y, si procede, aceptada o ajustada explícitamente antes de convertirla en trabajo operativo.

## Foco operativo

Evaluar y decidir si la arquitectura recomendada de doble pasada, junto con sus salvaguardas requeridas, debe orientar el primer piloto de cobertura profesional.

## Próximos pasos

- Revisar la evaluación experta y la presentación con las personas que deban debatir el enfoque.
- Decidir explícitamente si se adopta, modifica o descarta la recomendación para el primer piloto.
- Si se adopta, definir el contrato del piloto: muestra de entrevistas, salida inicial revisable, control de privacidad, criterios de corrección y señales de utilidad.
- Mantener separadas la cobertura, la profundidad y la correspondencia ESCO mientras no exista una decisión posterior que cambie ese alcance.
- No tratar la evaluación como validación con personas ni actualizar el SPEC o el playbook de profundidad por inferencia.

## Acciones abiertas relevantes

- No hay acciones formales registradas.
- Es candidata a acción futura la definición del primer piloto, condicionada a una decisión explícita sobre la recomendación metodológica.

## Decisiones vigentes relevantes

- `hosts/hosts.yaml` registra `carrera-ai` como host PCS.
- La carpeta `.pcs/` conserva la memoria operativa local; el estado actual vive en este documento y no en una sesión histórica.
- `docs/DOCUMENTO_SPEC_CARRERA_AI.md` es la referencia funcional visible del host; la revisión actual no lo modifica.
- `PLAYBOOK_ENTREVISTA_PROFESIONAL_v1_3_2_IA` sigue gobernando la profundidad.
- Cobertura y profundidad son capas complementarias; la cobertura no sustituye el playbook de profundidad.
- La recomendación de doble pasada es un resultado debatible de evaluación, no una decisión formal ni un playbook adoptado.
- ESCO solo puede entrar más adelante como correspondencia candidata, explicable y revisable.

## Bloqueos o riesgos

- La recomendación todavía no ha sido aceptada como orientación operativa; convertirla en norma antes del debate sería prematuro.
- Una implementación rígida de las dos pasadas podría volver lineal o evaluativa una conversación que debe admitir saltos, retornos, omisiones y correcciones.
- Un perfil persuasivo con evidencia insuficiente puede inflar capacidades u ocultar incertidumbre; la persona debe poder revisar, matizar, rechazar o retirar información.
- ESCO no debe confundirse con prueba de competencia, cualificación o certificación individual.
- La información de trayectoria profesional es personal y debe limitarse a lo necesario para el propósito de carrera.
- `.tmp/` queda excluida del uso operativo salvo autorización expresa.

## Referencias históricas y de continuidad

- `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`: sesión abierta que registra el núcleo metodológico, las fases del perfil y la exploración posterior de enfoques.
- `sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md`: línea paralela para investigar correspondencias ESCO candidatas sin bloquear la Fase 1.
- `docs/Ideas debate - como afrontar entrevista cobertura profesional/01_Conservadora_linea_de_vida_flexible_y_reconstruible.md`.
- `docs/Ideas debate - como afrontar entrevista cobertura profesional/02_Conservadora_doble_pasada_panorama_e_inmersion_selectiva.md`.
- `docs/Ideas debate - como afrontar entrevista cobertura profesional/03_Innovadora_atlas_conversacional_de_episodios_transiciones_y_capacidades.md`.
- `docs/Ideas debate - como afrontar entrevista cobertura profesional/04_Innovadora_dossier_de_hipotesis_contrastables_y_evidencia_progresiva.md`.
- `docs/Ideas debate - como afrontar entrevista cobertura profesional/05_Evaluacion_experta_y_recomendacion_de_enfoque.md`.
- `docs/Ideas debate - como afrontar entrevista cobertura profesional/06_Presentacion_propuesta_recomendada.html`.
