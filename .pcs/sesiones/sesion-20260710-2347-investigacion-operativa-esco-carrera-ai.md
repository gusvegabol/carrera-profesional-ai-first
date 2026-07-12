---
id: sesion-20260710-2347-investigacion-operativa-esco-carrera-ai
titulo: Investigacion operativa ESCO para Carrera AI
inicio: 2026-07-10
cierre:
estado: abierta
tipo: sesion
host: carrera-ai
sesion_padre: sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai
---

# Sesion PCS - Investigacion operativa ESCO para Carrera AI

## 1. Identificacion

| Campo | Valor |
| --- | --- |
| Tipo de documento | Sesion de trabajo PCS |
| Proyecto anfitrion | Carrera Profesional AI-First |
| Host anfitrion | `carrera-ai` |
| Nombre de sesion | Investigacion operativa ESCO para Carrera AI |
| Fichero | `sesion-20260710-2347-investigacion-operativa-esco-carrera-ai.md` |
| Fecha de apertura | 2026-07-10 |
| Estado | Abierta |
| Naturaleza | Investigacion tecnica y metodologica aplicada |
| Ambito | Definir como obtener correspondencias candidatas ESCO desde competencias, habilidades, ocupaciones o formulaciones profesionales |
| Sesion padre | `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md` |
| Ejecuta cambios fisicos | Si, solo dentro del alcance que se autorice expresamente |

## 2. Motivo de apertura

Esta sesion separa la investigacion operativa sobre ESCO de la definicion general del nucleo metodologico y del futuro playbook de cobertura profesional.

El nucleo metodologico menciona ESCO como marco de correspondencia, pero todavia no establece como debe usarse en la aplicacion, que datos necesita, que salida debe producir, que limites debe respetar ni como se verificara que una equivalencia sea razonable.

La hipotesis de trabajo es que esta linea puede avanzar en paralelo: recibir una competencia, habilidad, profesion, ocupacion o descripcion profesional sintetica y devolver una correspondencia ESCO candidata, explicada, trazable y revisable.

## 3. Relacion con la sesion padre

Esta sesion queda vinculada a `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`.

La sesion padre conserva la arquitectura general:

- fases del Perfil Profesional Accionable;
- SPEC del playbook de cobertura profesional;
- pruebas sinteticas por fase;
- relacion entre entrevista, evidencia, perfil y validacion.

Esta sesion hija se limita a estudiar y disenar el subproblema ESCO:

- como consultar o usar ESCO;
- como distinguir habilidades/competencias, conocimientos, ocupaciones y cualificaciones;
- como producir candidatos con codigo o URI ESCO;
- como explicar el ajuste;
- como conservar dudas, alternativas y estado de validacion.

## 4. Decisiones de partida

- ESCO no debe tratarse como verdad automatica, certificacion ni validacion oficial.
- La salida esperada debe ser una correspondencia candidata, no "el codigo correcto" sin matices.
- Toda correspondencia debe indicar version ESCO, tipo de concepto, etiqueta, identificador, explicacion y razon de ajuste.
- Cuando la entrada sea ambigua o insuficiente, el sistema debe devolver dudas o pedir mas contexto en vez de forzar un codigo.
- La correspondencia ESCO debe poder enlazarse despues con el Perfil Profesional Accionable mediante trazabilidad: formulacion profesional -> evidencia/contexto -> candidato ESCO -> estado de revision.
- Esta investigacion puede generar una skill futura, pero la skill no se crea ni se especifica todavia como implementacion cerrada.

## 5. Lineas de investigacion

1. Identificar las fuentes oficiales y mecanismos disponibles de ESCO: API, descargas, formatos, versiones y politicas de uso.
2. Definir que tipos de entrada admitira el flujo inicial: competencia, habilidad, conocimiento, profesion, ocupacion o texto profesional libre.
3. Decidir que tipos de conceptos ESCO deben entrar en el primer alcance: habilidades/competencias y ocupaciones como candidatos principales; cualificaciones solo si se justifica despues.
4. Disenar el contrato de salida minimo: candidatos ordenados, identificador ESCO, etiqueta, tipo, explicacion, evidencias usadas, dudas, alternativas y estado.
5. Definir guardarrailes contra sobreafirmacion, traducciones pobres, falsos amigos, entradas demasiado genericas y ocupaciones confundidas con competencias.
6. Preparar casos sinteticos de prueba para comprobar busqueda, ranking, rechazo prudente y explicabilidad.
7. Evaluar si conviene una skill local que encapsule el procedimiento para uso repetido por CODEX o por futuros agentes.

## 6. Preguntas guia

1. Que version de ESCO debe fijarse para que los resultados sean reproducibles?
2. Que identificador debe conservarse como referencia estable: codigo, URI, UUID u otro campo?
3. Como debe comportarse el sistema ante una competencia expresada en lenguaje comun y no en terminologia ESCO?
4. Como se separa una ocupacion candidata de una habilidad candidata cuando la entrada mezcla ambas?
5. Que umbral minimo de contexto exige una correspondencia aceptable?
6. Como se documenta que un candidato ESCO es plausible pero no validado por la persona?
7. Que pruebas sinteticas deben pasar antes de usar ESCO dentro del playbook de cobertura?

## 7. Relacion con las tres fases del perfil

Esta linea no pertenece a la Fase 1 del Perfil Profesional Accionable, porque la Fase 1 queda centrada en una primera version util del perfil sin correspondencia ESCO.

Su resultado alimentara principalmente la Fase 2:

- Fase 1: primera version util del perfil sin ESCO.
- Fase 2: primera version util del perfil con correspondencias ESCO candidatas.
- Fase 3: perfil completo por ciclos, con ESCO integrado como capa revisable dentro del perfil vivo.

## 8. Riesgos

- Convertir ESCO en un etiquetador automatico que oculte incertidumbre.
- Confundir una profesion u ocupacion con una competencia profesional demostrada.
- Mapear formulaciones ricas de experiencia a etiquetas demasiado genericas.
- Usar una version ESCO no fijada y perder reproducibilidad.
- Mezclar conocimientos, habilidades, ocupaciones y cualificaciones como si fueran equivalentes.
- Crear una skill demasiado pronto, antes de entender API, datos, salida y pruebas.

## 9. Resultado esperado

Esta sesion debera dejar una base suficiente para decidir si se crea una skill ESCO y, si procede, con que contrato.

El resultado minimo esperado antes de implementar una skill es:

1. fuente ESCO y version recomendada;
2. alcance inicial de tipos de concepto;
3. contrato de entrada y salida;
4. reglas de prudencia y explicabilidad;
5. lista inicial de pruebas sinteticas;
6. criterio para integrar el resultado en la SPEC del playbook de cobertura profesional.

## 10. Siguiente gesto recomendado

Realizar una investigacion breve sobre el uso oficial de ESCO en aplicaciones: API, descargas, versionado, identificadores, busqueda y formatos de respuesta.

Despues, redactar un pequeno diseno de contrato para una futura skill que devuelva candidatos ESCO explicados, no codigos definitivos.

## 11. Trazabilidad

- Host resuelto: `carrera-ai` -> `C:/Users/gusve/Documents/Apps/carrera-profesional-ai-first`
- Sesion padre: `sesion-20260710-2308-nucleo-metodologico-perfil-profesional-accionable-carrera-ai.md`
- Sesion relacionada de cobertura: `sesion-20260705-concepto-cobertura-profesional-carrera-ai.md`
- Estado de la sesion: abierta
- PCS canonico: no modificado
