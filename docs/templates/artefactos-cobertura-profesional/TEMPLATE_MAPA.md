---
tipo: mapa
id_mapa:
id_entrevistado:
fecha_creacion:
fecha_actualizacion:
estado: activo | en_pausa | cerrado
fecha_cierre:
---

# Mapa de cobertura — <identificador>

## Entrevistado

Referencia: <id_entrevistado>

## Zonas

<!-- Repetir un bloque como este por cada zona. El identificador de zona, una vez asignado, no se reutiliza ni se renumera. -->

### Zona <n> — <nombre de la zona>

Identificador de zona: <id_zona, por ejemplo ENT-001-M01-Z003>

Estado: explorada | candidata | parcial | pendiente

Checkpoint: checkpoints/CHECKPOINT_<id_mapa>-<id_zona>-<intento>.md (solo si estado: parcial; si la inmersión terminó, indicar «no aplica»)
Inmersión(es): inmersiones/INMERSION_<id_mapa>-<id_zona>-<intento>.md (una por cada activación cerrada; el intento usa `a`, `b`, etc.)
Competencia(s): competencias/COMPETENCIA_<id_mapa>-<id_zona>-<intento>.md (solo si hubo competencia)

Señal de origen: <texto breve que motivó registrar esta zona>
Sesión de origen: sesiones/SESION_COBERTURA_<id_mapa>_<fecha>.md

Transcripción de origen: transcripciones/TRANSCRIPCION_<id_entrevistado>-<id_mapa>_<fecha>.md

## Advertencia de límite

<Qué no debe concluirse todavía a partir de lo explorado hasta ahora — actualizar en cada cierre de sesión.>

## Siguiente exploración recomendada

<Zona propuesta y motivo breve, si lo hay.>
