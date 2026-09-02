# Políticas del tablero

Políticas explícitas de entrada y salida por columna. Su visibilidad es, en sí misma, la evidencia
mínima de que Kanban se está aplicando y no solamente declarando.

## Límites de trabajo en curso

| Columna | Límite de WIP | Justificación |
|---|---|---|
| Análisis | 3 | Evita abrir trabajo que no se podrá sostener |
| Desarrollo | 4 | Un ítem por persona más una holgura |
| Validación documental | 2 | Cuello de botella identificado; límite deliberadamente bajo |
| Espera externa (HL7/FHIR) | sin límite, con envejecimiento visible | Fuera del control del equipo; se mide, no se limita |
| Listo para liberar | 3 | Previene acumulación previa a la ventana de despliegue |

## Reglas de entrada y salida

- **Nada existe si no está en una tarjeta.** El trabajo fuera del tablero no se contabiliza y por
  tanto no se gestiona.
- Toda tarjeta lleva **fecha de entrada**; sin ella no se puede calcular tiempo de ciclo.
- Un ítem sale de *Validación documental* solo con la verificación por riesgo aplicada según la
  Definición de Hecho proporcional.
- **Terminar antes de empezar:** al alcanzar el límite de una columna, la prioridad es desbloquear,
  no iniciar trabajo nuevo.

## Política de expedite

- Cupo máximo: **2 expedites por semana**.
- Un expedite solo procede ante afectación directa de la atención al paciente.
- Cada expedite genera un post mortem breve con causa raíz, registrado en la bitácora.
- Superar el cupo dispara revisión de la política, no una excepción silenciosa.

## Gestión del envejecimiento

Un ítem que supera los 19 días (P85 actual) se marca y se fuerza su desbloqueo con prioridad sobre
el inicio de trabajo nuevo. El envejecimiento se revisa a diario, no al cierre de la ventana.

## Cadencia de revisión

| Ritual | Frecuencia | Salida esperada |
|---|---|---|
| Revisión de bloqueos | Diaria | Ítems desbloqueados o escalados |
| Lectura de métricas de flujo | Quincenal | Ajuste de límites con datos |
| Auditoría de expedites | Semanal | Causas raíz registradas |
