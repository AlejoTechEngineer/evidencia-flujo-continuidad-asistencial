# ADR-001 — Adopción de Kanban con salvaguarda de DoD proporcional

- **Estado:** Aceptada
- **Fecha:** 2026-09-01
- **Ámbito:** Sistema de trabajo del equipo de Continuidad Asistencial Digital
- **Alternativas evaluadas:** Scrum, Kanban

## Contexto

El nodo piloto opera con pacientes reales. En las últimas ocho semanas, el 43 % de los ítems
ingresados al tablero no estaba planeado y el tiempo de ciclo presenta una variabilidad alta
(P50 = 4 días, P85 = 19 días, cociente 4,7). El equipo es pequeño y está distribuido en tres husos
horarios, con dependencias fuera de su control sobre el motor de interoperabilidad HL7/FHIR y el
proveedor de identidad institucional.

El criterio dominante, por tanto, no es la incertidumbre de requisitos sino **la variabilidad de
llegada de la demanda**. El criterio secundario es la trazabilidad regulatoria.

## Decisión

Se adopta **Kanban** como sistema de gobierno del flujo, con:

1. Límites de trabajo en curso numéricos por columna, con revisión quincenal basada en datos.
2. Política de *expedite* con cupo semanal máximo y post mortem breve por cada uso.
3. Compromisos externos expresados por **P85** y nunca por promedio.
4. **DoD proporcional** conservada como salvaguarda no negociable en los ítems que tocan datos
   sensibles de paciente: verificaciones por riesgo con bloqueo ante incumplimiento.

## Alternativa descartada

**Scrum.** Ofrece mayor trazabilidad ante auditoría mediante el objetivo de sprint y una DoD
verificable, y habría sido la elección correcta si el problema fuese la incertidumbre de alcance.
Se descarta porque el timebox cerrado convierte cada incidente de interoperabilidad en una ruptura
del compromiso del sprint: con un 43 % de trabajo no planeado, la renegociación del objetivo dejaría
de ser una excepción para volverse la norma, vaciando de sentido la cadencia.

## Consecuencias aceptadas

- **Menos plan a largo plazo.** Se gana control de flujo a costa de visibilidad de horizonte largo;
  la planeación trimestral pasa a expresarse como rangos por percentil.
- **Menor throughput del trabajo normal.** La capacidad reservada para urgencias clínicas reduce la
  salida de evolutivos. Es un costo asumido conscientemente por criticidad del dominio.
- **Mayor disciplina exigida.** Sin cadencia que fuerce la conversación, el tablero debe reflejar la
  realidad a diario o el método se degrada a un diagrama decorativo.

## Riesgos y antipatrones vigilados

| Antipatrón | Señal temprana | Contramedida |
|---|---|---|
| «Todo es urgente» | Expedites por encima del cupo semanal | Auditoría semanal de causas de urgencia |
| Tablero desactualizado | Ítems sin movimiento con trabajo real en curso | Ritual diario de actualización y revisión de bloqueos |
| Promedios engañosos | Compromisos basados en la media del lead time | Comprometer por P85 y gestionar por envejecimiento |
| «Ligero» leído como «sin reglas» | Ítems sensibles cerrados sin verificación | DoD proporcional con bloqueo ante incumplimiento |

## Verificación

Ventana de dos a tres semanas. Se considera que la decisión funciona si el P85 desciende de 19 a
≤ 14 días **manteniendo** el cumplimiento de WIP en 80 % o más y sin incremento de defectos P1/P2
posliberación. Si el P85 mejora pero el cumplimiento cae, se concluye que la mejora no es sostenible
y se revisa la política antes de extenderla.

## Punto de revisión

Gate G3, aprobación de despliegue en el nodo piloto.
