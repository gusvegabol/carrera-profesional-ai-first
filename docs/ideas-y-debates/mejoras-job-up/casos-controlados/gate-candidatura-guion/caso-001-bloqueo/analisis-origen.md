---
id: caso-controlado-gate-001-analisis
tipo: caso_controlado_analisis
fecha: 2026-08-05
decision_estrategica: pedir_datos_adicionales_antes_de_redactar
---

# Caso controlado 001 — Bloqueo por dato esencial

## Escenario

Oferta simulada de responsable de almacén que exige un permiso profesional vigente para manejar una maquinaria concreta. Los datos core no contienen ese permiso ni evidencia equivalente.

## Decisión estratégica

`pedir_datos_adicionales_antes_de_redactar`

## Justificación

El permiso es una condición esencial de la oferta y no puede afirmarse, compensarse ni inferirse desde experiencia transferible. Debe solicitarse confirmación antes de continuar.

## Resultado esperado

- Crear la ficha de candidatura en estado `detenida`.
- Mantener `presentada: false`.
- Registrar el bloqueo, la fase afectada y la resolución necesaria.
- No crear guion, documentos finales ni veredicto.
