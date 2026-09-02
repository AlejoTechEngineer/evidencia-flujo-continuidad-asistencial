# Bitácora de decisiones de política

Registro breve de cada cambio de regla operativa, su motivo y el efecto medido. Es la evidencia que
vincula una decisión con su resultado y permite auditar el sistema de trabajo sin burocracia.

| Fecha | Decisión | Motivo | Efecto esperado | Efecto medido |
|---|---|---|---|---|
| 2026-07-06 | Publicación inicial de políticas y límites de WIP | El tablero no reflejaba el trabajo real | Visibilidad del cuello de botella | Cuello identificado en Validación documental |
| 2026-07-20 | Reducción del WIP de Validación documental de 4 a 2 | Cola dominante concentrada en esa columna | Descenso del P85 global | P85 pasó de 24 a 19 días |
| 2026-08-03 | Creación de la columna Espera externa (HL7/FHIR) | La dependencia externa contaminaba el tiempo de ciclo propio | Separar espera controlable de no controlable | Cola larga aislada y atribuida |
| 2026-08-17 | Cupo semanal de 2 expedites con post mortem | Las urgencias absorbían capacidad sin registro | Proteger el flujo del trabajo planeado | 12 expedites en 8 semanas, dentro de cupo |
| 2026-08-31 | Compromisos externos expresados por P85 | Los promedios generaban promesas incumplibles | Compromisos sostenibles | En verificación en la ventana actual |

## Criterio de registro

Se registra toda decisión que modifique una política del tablero, un límite de WIP o la Definición de
Hecho. No se registran decisiones de contenido de los ítems: para eso está el propio tablero.

Cada entrada debe poder responder tres preguntas: qué se cambió, por qué, y qué se observó después.
Si la tercera columna queda vacía de forma sistemática, el equipo está cambiando políticas sin
verificar su efecto, que es el antipatrón que esta bitácora existe para prevenir.
