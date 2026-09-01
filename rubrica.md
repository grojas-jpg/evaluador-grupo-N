# Rúbrica Ejecutable — Agente Corrector de Trabajos Finales
Programación de y con Agentes de IA · MBA UCEMA · 2026 2T
Basada en la rúbrica oficial del Trabajo Final

---

## 1. SISTEMA COMPLETO Y FUNCIONANDO (30 puntos)

**¿Qué se evalúa?**
Que el trabajo tenga objetivo claro, contrato escrito (system + user prompt), al menos una herramienta o conector real, salida estructurada, y puntos de supervisión humana definidos (L0–L4).

### Excelente (27-30)
- Objetivo del agente explícito y concreto (no genérico tipo "ayudar con tareas")
- `prompts/system_prompt.md` y `prompts/user_prompt.md` presentes, ambos con las piezas completas de un contrato (rol, tarea, restricciones, formato de salida)
- Usa al menos una herramienta o conector REAL (API, archivo, planilla, calendario) — no simulado
- Salida en formato estructurado (JSON, tabla, etc.) consistente
- Define supervisión humana con el vocabulario L0–L4: qué hace el agente solo, qué revisa una persona, quién firma
- BUSCA: carpeta `prompts/` con ambos archivos, mención explícita de una herramienta con nombre y uso real, sección de supervisión con niveles L0-L4 nombrados

### Bueno (21-26)
- Objetivo y contrato presentes pero algo genéricos en partes
- Herramienta real usada pero poco integrada al flujo
- Salida estructurada pero con inconsistencias menores
- Supervisión mencionada pero sin usar bien el vocabulario L0-L4

### Aceptable (13-20)
- Contrato incompleto (falta system o user prompt, o están muy básicos)
- Herramienta mencionada pero no queda claro si se usó de verdad
- Salida sin estructura clara
- Supervisión mencionada vagamente ("un humano revisa") sin niveles

### Deficiente (0-12)
- Sin contrato real, o es un prompt suelto sin estructura
- Sin herramienta real (todo simulado o inventado)
- Sin formato de salida definido
- Sin mención de supervisión

---

## 2. PROCESO DOCUMENTADO (25 puntos)

**¿Qué se evalúa?**
Que `DECISIONES.md` cuente la historia real: iteraciones del contrato, errores, qué se achicó y por qué.

### Excelente (22-25)
- `DECISIONES.md` > 400 palabras
- Muestra al menos 2 iteraciones concretas del contrato (versión 1 → qué falló → versión 2)
- Documenta errores textuales reales (no solo "mejoramos el prompt")
- Explica qué se recortó de alcance y por qué
- BUSCA: `DECISIONES.md` con secciones tipo "Primera versión", "Qué falló", "Ajuste", fechas o commits referenciados

### Bueno (16-21)
- `DECISIONES.md` presente (200-400 palabras), muestra al menos una iteración clara
- Menciona errores pero sin mucho detalle

### Aceptable (8-15)
- `DECISIONES.md` corto (< 200 palabras), sin iteraciones claras, más descriptivo que reflexivo

### Deficiente (0-7)
- `DECISIONES.md` ausente o vacío, sin evidencia de iteración

---

## 3. FORMATO Y REPRODUCIBILIDAD (15 puntos)

**¿Qué se evalúa?**
Que la estructura obligatoria esté respetada y que las corridas sean reconstruibles por un tercero.

### Excelente (13-15)
- Estructura completa: `README.md`, `prompts/`, `corridas/`, `DECISIONES.md`
- `corridas/` tiene al menos 3 ejecuciones reales, cada una con entrada, salida y fecha, guardadas tal como salieron (sin editar a mano)
- Un tercero podría reconstruir qué pasó en cada corrida solo leyendo los archivos
- BUSCA: 3+ subcarpetas o archivos en `corridas/`, cada uno con input/output/fecha identificables

### Bueno (9-12)
- Estructura casi completa (falta algún archivo menor)
- 2-3 corridas documentadas pero con detalles faltantes (falta fecha o falta la entrada completa)

### Aceptable (5-8)
- Estructura incompleta
- 1-2 corridas, poco detalladas

### Deficiente (0-4)
- Estructura obligatoria no respetada, o carpeta `corridas/` vacía/ausente

---

## 4. ANÁLISIS ECONÓMICO (15 puntos)

**¿Qué se evalúa?**
Costo por corrida (tokens in/out), proyección de costo (semanal/anual) y elección de modelo justificada.

### Excelente (13-15)
- Calcula tokens de entrada y salida de al menos una corrida real, con el costo en USD
- Proyecta el costo si el sistema corriera en producción (por semana Y por año)
- Justifica la elección de modelo con el criterio del curso ("el más chico que hace bien la tarea"), mencionando qué modelo probó o descartó y por qué
- BUSCA: números concretos de tokens y costo, una proyección con al menos 2 escalas temporales, una justificación explícita de modelo (no solo "usamos GPT-4 porque es bueno")

### Bueno (9-12)
- Costo por corrida calculado, proyección presente pero solo a una escala temporal
- Elección de modelo mencionada pero justificación superficial

### Aceptable (5-8)
- Menciona costos de forma aproximada, sin cálculo real de tokens
- Sin proyección o justificación de modelo

### Deficiente (0-4)
- Sin análisis económico, o solo una frase genérica

---

## 5. GOBIERNO Y RIESGO (15 puntos)

**¿Qué se evalúa?**
Qué sistemas toca el agente y con qué permisos, qué puede salir mal, qué se revisa antes de confiar en una salida, y quién firma el resultado.

### Excelente (13-15)
- Lista explícita de qué sistemas/datos toca el agente y con qué nivel de permiso (lectura/escritura)
- Identifica al menos 2 riesgos concretos y específicos del caso (no genéricos tipo "puede alucinar")
- Define qué se revisa antes de confiar en la salida y quién firma el resultado final
- BUSCA: sección de gobierno con permisos nombrados, riesgos específicos al dominio del caso, un "firmante" identificado

### Bueno (9-12)
- Permisos y riesgos mencionados pero algo genéricos
- Firmante o revisión mencionados sin mucho detalle

### Aceptable (5-8)
- Menciona riesgos de forma vaga, sin permisos claros ni firmante definido

### Deficiente (0-4)
- Sin sección de gobierno y riesgo, o una frase suelta sin sustancia

---

## PUNTAJE TOTAL

| Dimensión | Puntos |
|---|---|
| Sistema completo y funcionando | 0-30 |
| Proceso documentado | 0-25 |
| Formato y reproducibilidad | 0-15 |
| Análisis económico | 0-15 |
| Gobierno y riesgo | 0-15 |
| **TOTAL** | **0-100** |

**Interpretación:**
- 85-100: Excelente
- 70-84: Bueno
- 55-69: Aceptable
- < 55: Deficiente

---

## NOTAS PARA EL AGENTE CORRECTOR
- No dar puntos por lo que el README *dice* que existe si no hay evidencia en el repo (archivos, carpetas, contenido real).
- Si el README afirma algo que el resto del repo contradice o no respalda, marcarlo explícitamente como inconsistencia y bajar el puntaje de la dimensión correspondiente.
- Citar siempre evidencia concreta (nombre de archivo, cantidad de palabras/líneas, contenido puntual) — nunca un puntaje sin cita.
- Puntajes distribuidos son más creíbles que "todo excelente": si hay fortalezas y debilidades, que se reflejen en la nota.
