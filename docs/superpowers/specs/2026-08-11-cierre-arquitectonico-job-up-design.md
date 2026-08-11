# Diseño — Cierre arquitectónico y reorganización documental de Job-up

**Fecha:** 2026-08-11
**Host:** `carrera-ai`
**Sesión PCS:** `sesion-20260805-1757-job-up`
**Rama:** `codex/job-up-validar-presentacion`

## Decisión de alcance

La arquitectura vigente de Job-up se cierra en la generación y validación de
los artefactos documentales de una candidatura. El recorrido canónico será:

```text
oferta → análisis → candidatura → guion CV → contenido CV → composición CV
→ veredicto CV → guion carta → contenido carta → composición carta
→ veredicto carta → candidatura documental completa → fin de la fase actual
```

La candidatura documental completa se define como:

```text
CV final aprobado + carta final aprobada cuando sea requerida
```

Esta condición no equivale a `presentada: true` y no requiere
`GATE-CANDIDATURA-PRESENTACION`.

## Capas fuera de alcance

La presentación externa automatizada queda fuera del flujo principal. No se
implementan navegación, cuentas, inicio de sesión, formularios, decisiones de
privacidad, consentimientos, captcha ni envíos. La presentación futura seguirá
bajo responsabilidad humana hasta que exista un contrato independiente.

La UI o wizard inicial de configuración también queda fuera de alcance. Se
documenta como línea futura para descubrir opciones, aplicar defaults y
persistir una configuración estructurada, sin añadir ahora campos ni
implementar interfaz.

## Reorganización documental

- Playbooks operativos aceptados: `docs/metodologia/playbooks/`.
- Templates operativos de Job-up: `boveda-entrevista-profesional/busqueda-empleo/proceso/plantillas/`.
- Diseños, comparativas y contratos todavía experimentales: `docs/ideas-y-debates/mejoras-job-up/`.
- Presentación y evaluación de canal: clasificados como futura línea y
  separados del flujo documental vigente.
- Versiones sustituidas o artefactos experimentales de candidaturas:
  `historico/`, conservando la ruta de procedencia cuando sea necesario.

Los scripts consumirán exclusivamente las ubicaciones canónicas. Las
instancias de candidatura conservarán sus artefactos propios, pero dejarán de
tratar el paquete o la validación de presentación como precondición de cierre
documental.

## Criterios de validación

1. CAND-2026-020 termina con CV y carta aprobados, candidatura documental
   completa y `presentada: false`.
2. Una candidatura con carta requerida no aprobada permanece incompleta.
3. Una candidatura sin carta requerida puede completar el flujo si su contrato
   lo permite.
4. La ausencia de `GATE-CANDIDATURA-PRESENTACION` no bloquea el cierre
   documental.
5. Ningún playbook o template operativo depende de `docs/ideas-y-debates`.
6. Las referencias internas y los scripts apuntan a rutas existentes.
7. La suite específica y la suite completa pasan, junto con la comprobación de
   sintaxis y `git diff --check`.

## Restricciones de ejecución

Se conserva la rama existente y su trabajo no comprometido. Esta reorganización
no autoriza commit, merge, PR, presentación externa, inicio de sesión ni
construcción de UI.
