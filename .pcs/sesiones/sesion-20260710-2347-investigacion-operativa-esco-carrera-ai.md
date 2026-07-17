---
id: sesion-20260710-2347-investigacion-operativa-esco-carrera-ai
titulo: Investigación operativa ESCO para Carrera AI
inicio: 2026-07-10
cierre:
estado: abierta
tipo: sesion
host: carrera-ai
sesion_padre: sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai
linea_paralela: esco
fuera_del_alcance_de: "2.0"
version_global_candidata: "2.5"
---

# Sesión PCS - Investigación operativa ESCO para Carrera AI

> La versión global 2.5 es una candidatura provisional, no una versión abierta. Esta investigación no bloquea ni modifica el criterio de finalización de Carrera AI 2.0.

## 1. Identificación

| Campo | Valor |
| --- | --- |
| Tipo de documento | Sesión de trabajo PCS |
| Proyecto anfitrión | Carrera Profesional AI-First |
| Host anfitrión | `carrera-ai` |
| Nombre de sesión | Investigación operativa ESCO para Carrera AI |
| Fichero | `sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md` |
| Fecha de apertura | 2026-07-10 |
| Estado | Abierta |
| Naturaleza | Investigación técnica y metodológica aplicada |
| Ámbito | Definir cómo obtener correspondencias candidatas ESCO desde competencias, habilidades, ocupaciones o formulaciones profesionales |
| Sesión padre | `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md` |
| Ejecuta cambios físicos | Sí, solo dentro del alcance que se autorice expresamente |

## 2. Motivo de apertura

Esta sesión separa la investigación operativa sobre ESCO de la definición general del núcleo metodológico y del futuro playbook de cobertura profesional.

El núcleo metodológico menciona ESCO como marco de correspondencia, pero todavía no establece cómo debe usarse en la aplicación, qué datos necesita, qué salida debe producir, qué límites debe respetar ni cómo se verificará que una equivalencia sea razonable.

La hipótesis de trabajo es que esta línea puede avanzar en paralelo: recibir una competencia, habilidad, profesión, ocupación o descripción profesional sintética y devolver una correspondencia ESCO candidata, explicada, trazable y revisable.

## 3. Relación con la sesión padre

Esta sesión queda vinculada a `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`.

La sesión padre conserva la arquitectura general:

- fases del Perfil Profesional Accionable;
- SPEC del playbook de cobertura profesional;
- pruebas sintéticas por fase;
- relación entre entrevista, evidencia, perfil y validación.

Esta sesión hija se limita a estudiar y diseñar el subproblema ESCO:

- cómo consultar o usar ESCO;
- cómo distinguir habilidades/competencias, conocimientos, ocupaciones y cualificaciones;
- cómo producir candidatos con código o URI ESCO;
- cómo explicar el ajuste;
- cómo conservar dudas, alternativas y estado de validación.

## 4. Decisiones de partida

- ESCO no debe tratarse como verdad automática, certificación ni validación oficial.
- La salida esperada debe ser una correspondencia candidata, no "el código correcto" sin matices.
- Toda correspondencia debe indicar versión ESCO, tipo de concepto, etiqueta, identificador, explicación y razón de ajuste.
- Cuando la entrada sea ambigua o insuficiente, el sistema debe devolver dudas o pedir más contexto en vez de forzar un código.
- La correspondencia ESCO debe poder enlazarse después con el Perfil Profesional Accionable mediante trazabilidad: formulación profesional -> evidencia/contexto -> candidato ESCO -> estado de revisión.
- Esta investigación puede generar una skill futura, pero la skill no se crea ni se especifica todavía como implementación cerrada.

## 5. Líneas de investigación

1. Identificar las fuentes oficiales y mecanismos disponibles de ESCO: API, descargas, formatos, versiones y políticas de uso.
2. Definir qué tipos de entrada admitirá el flujo inicial: competencia, habilidad, conocimiento, profesión, ocupación o texto profesional libre.
3. Decidir qué tipos de conceptos ESCO deben entrar en el primer alcance: habilidades/competencias y ocupaciones como candidatos principales; cualificaciones solo si se justifica después.
4. Diseñar el contrato de salida mínimo: candidatos ordenados, identificador ESCO, etiqueta, tipo, explicación, evidencias usadas, dudas, alternativas y estado.
5. Definir guardarraíles contra sobreafirmación, traducciones pobres, falsos amigos, entradas demasiado genéricas y ocupaciones confundidas con competencias.
6. Preparar casos sintéticos de prueba para comprobar búsqueda, ranking, rechazo prudente y explicabilidad.
7. Evaluar si conviene una skill local que encapsule el procedimiento para uso repetido por CODEX o por futuros agentes.

## 6. Preguntas guía

1. ¿Qué versión de ESCO debe fijarse para que los resultados sean reproducibles?
2. ¿Qué identificador debe conservarse como referencia estable: código, URI, UUID u otro campo?
3. ¿Cómo debe comportarse el sistema ante una competencia expresada en lenguaje común y no en terminología ESCO?
4. ¿Cómo se separa una ocupación candidata de una habilidad candidata cuando la entrada mezcla ambas?
5. ¿Qué umbral mínimo de contexto exige una correspondencia aceptable?
6. ¿Cómo se documenta que un candidato ESCO es plausible pero no validado por la persona?
7. ¿Qué pruebas sintéticas deben pasar antes de usar ESCO dentro del playbook de cobertura?

## 7. Relación con las tres fases del perfil

Esta línea no pertenece a la Fase 1 del Perfil Profesional Accionable, porque la Fase 1 queda centrada en una primera versión útil del perfil sin correspondencia ESCO.

Su resultado alimentará principalmente la Fase 2:

- Fase 1: primera versión útil del perfil sin ESCO.
- Fase 2: primera versión útil del perfil con correspondencias ESCO candidatas.
- Fase 3: perfil completo por ciclos, con ESCO integrado como capa revisable dentro del perfil vivo.

## 8. Riesgos

- Convertir ESCO en un etiquetador automático que oculte incertidumbre.
- Confundir una profesión u ocupación con una competencia profesional demostrada.
- Mapear formulaciones ricas de experiencia a etiquetas demasiado genéricas.
- Usar una versión ESCO no fijada y perder reproducibilidad.
- Mezclar conocimientos, habilidades, ocupaciones y cualificaciones como si fueran equivalentes.
- Crear una skill demasiado pronto, antes de entender API, datos, salida y pruebas.

## 9. Resultado esperado

Esta sesión deberá dejar una base suficiente para decidir si se crea una skill ESCO y, si procede, con qué contrato.

El resultado mínimo esperado antes de implementar una skill es:

1. fuente ESCO y versión recomendada;
2. alcance inicial de tipos de concepto;
3. contrato de entrada y salida;
4. reglas de prudencia y explicabilidad;
5. lista inicial de pruebas sintéticas;
6. criterio para integrar el resultado en la SPEC del playbook de cobertura profesional.

## 10. Siguiente gesto recomendado

Realizar una investigación breve sobre el uso oficial de ESCO en aplicaciones: API, descargas, versionado, identificadores, búsqueda y formatos de respuesta.

Después, redactar un pequeño diseño de contrato para una futura skill que devuelva candidatos ESCO explicados, no códigos definitivos.

## 11. Trazabilidad

- Host resuelto: `carrera-ai` -> `C:/Users/gusve/Documents/Apps/carrera-profesional-ai-first`
- Sesión padre: `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`
- Sesión relacionada de cobertura: `sesion-20260705-concepto-cobertura-profesional-carrera-ai.md`
- Estado de la sesión: abierta
- PCS canónico: no modificado
