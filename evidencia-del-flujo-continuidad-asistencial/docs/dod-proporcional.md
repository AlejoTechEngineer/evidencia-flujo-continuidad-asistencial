# Definición de Hecho proporcional

La ligereza de Kanban no elimina las salvaguardas: las gradúa según el riesgo. Un ítem que toca datos
clínicos no puede cerrarse con el mismo criterio que un ajuste de interfaz.

## Nivel 1 — Riesgo bajo

Cambios cosméticos, textos, ajustes de presentación sin acceso a datos de paciente.

- [ ] Revisión por pares aprobada
- [ ] Pipeline en verde
- [ ] Criterios de aceptación verificados

## Nivel 2 — Riesgo medio

Cambios de lógica de negocio sin exposición de datos sensibles.

- Todo lo del nivel 1, más:
- [ ] Pruebas automatizadas cubriendo el camino crítico
- [ ] Verificación de compatibilidad hacia atrás de la interfaz
- [ ] Nota de versión redactada

## Nivel 3 — Riesgo alto (bloqueante)

Cualquier ítem que lea, escriba o transporte datos sensibles de paciente, o que modifique la
integración HL7/FHIR.

- Todo lo del nivel 2, más:
- [ ] Revisión de seguridad sobre el manejo del dato sensible
- [ ] Registro de auditoría verificado en ambiente de pruebas
- [ ] Prueba de trazabilidad de extremo a extremo entre nodos
- [ ] Plan de reversión documentado y probado

**Regla de bloqueo:** un ítem de nivel 3 con alguna verificación incumplida no avanza a *Listo para
liberar*. No existe la categoría «casi listo»: el incumplimiento bloquea, no advierte.

## Por qué se conserva bajo Kanban

Kanban gobierna el flujo, no la calidad interna. Sin esta salvaguarda, la reducción del tiempo de
ciclo podría lograrse degradando la verificación, lo que en un dominio clínico es un intercambio
inaceptable. La DoD proporcional es el límite explícito que la decisión metodológica no negocia.
