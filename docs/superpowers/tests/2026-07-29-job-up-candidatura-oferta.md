# Prueba de comportamiento: `job-up-candidatura-oferta`

Esta prueba define el comportamiento mínimo que debe cumplir la skill de
candidatura por oferta. La skill no crea sesiones PCS directamente y no
realiza envíos ni contactos externos.

| Entrada | Estado de sesión | Resultado esperado |
| --- | --- | --- |
| URL accesible | una sesión Job-up abierta | extraer contenido, registrar URL y continuar el flujo |
| URL inaccesible + Markdown | una sesión Job-up abierta | usar Markdown, registrar contenido aportado y continuar |
| Texto pegado | una sesión Job-up abierta | extraer datos disponibles y pedir solo faltantes esenciales |
| Cualquiera | ninguna sesión Job-up abierta | informar y preguntar si desea ejecutar `job-up-inicia-sesion`; sin respuesta afirmativa, detenerse |
| Cualquiera | ninguna sesión + respuesta afirmativa | invocar `job-up-inicia-sesion`, comprobar una única sesión creada y continuar |
| Cualquiera | varias sesiones Job-up abiertas | pedir que la persona usuaria seleccione una sesión; no elegir por inferencia |
| Cualquiera | una sesión Job-up abierta + autorización privada aplicable | usar solo los datos autorizados para ese expediente |
| Cualquiera | una sesión Job-up abierta + autorización ausente o ambigua | no copiar ni propagar datos privados; bloquear solo los documentos que los requieran |

## Criterios de revisión

- La procedencia queda registrada como URL de origen cuando existe; en los
  demás casos se registra el material aportado y la fecha de recepción.
- La skill solicita únicamente datos esenciales ausentes y detiene el flujo si
  siguen faltando o existe una contradicción factual.
- Una autorización escrita de la ficha privada solo puede reutilizarse para la
  misma candidatura; no habilita otros expedientes ni acciones externas.
- La salida de fase 1 queda en `pendiente_de_aprobacion`.
