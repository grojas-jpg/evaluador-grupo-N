# Rúbrica ejecutable v0
Rúbrica Ejecutable — Agente Evaluador de Trabajos Finales
Programación de Agentes de IA · MBA UCEMA 2T 2026
Basada en los criterios oficiales del Parcial
---
1. RÚBRICA EJECUTABLE (25 puntos)
¿Qué se evalúa?
La calidad de la rúbrica que define cómo el agente calificará: precisión, escalas claras, evidencia exigida.
El objetivo es que sea tan precisa que una máquina pueda aplicarla igual dos veces, y tan legible que un humano puede discutirla.
Excelente (22-25 puntos)
Descripción: Rúbrica excepcional. Precisa, escalas claras, evidencia específica por nivel.
Criterios:
Define 4-6 dimensiones con pesos explícitos (ej: "30%", "20%")
Para CADA dimensión:
Escalas definidas por nivel (Excelente, Bueno, Aceptable, Deficiente)
Rango de puntajes claro para cada nivel (ej: 18-20, 14-17, 10-13, 0-9)
Criterios específicos y verificables (NO: "buen código", SÍ: "funciones documentadas", "pruebas unitarias presentes")
Ejemplos concretos de qué VE o BUSCA el agente (ej: "Archivo README > 500 palabras", "Carpeta tests/ con 10+ archivos")
Qué EVIDENCIA debe buscar el agente en el repositorio
Lenguaje preciso, sin ambigüedades
Diferenciación clara entre niveles (no son todos "casi iguales")
Incluye casos tramposos: cómo detectar mentiras (inconsistencias, afirmaciones sin evidencia)
Evidencia a buscar:
Archivo rubrica.md > 800 palabras
Tiene estructura: dimensión → niveles → criterios → ejemplos → evidencia
Para cada nivel, hay qué "buscar" en el repo (archivos, carpetas, contenido)
Menciona cómo detectar TRAMPAS (mentiras)
Ejemplo de excelente:
```markdown
## Documentación (25%)

### Excelente (23-25):
- README.md > 500 palabras
- Explica: propósito, arquitectura, instrucciones paso a paso, limitaciones
- BUSCA: "Instrucciones de cómo ejecutar", "Ejemplos de entrada/salida"
- TRAMPA: "Dice que implementó X pero carpeta X no existe"

### Bueno (18-22):
...
```
Bueno (17-21 puntos)
Descripción: Rúbrica clara y usable, pero le faltan detalles o escalas no están perfectas.
Criterios:
Define 3-4 dimensiones con pesos
Tiene niveles y rangos pero:
Falta especificar qué "buscar" en algunos niveles
Criterios son claros pero algo genéricos
Faltan ejemplos en algunos lugares
Detecta trampas pero no muy explícitamente
Legible y funcionable
Evidencia a buscar:
rubrica.md existe, 500-800 palabras
Estructura presente: niveles, criterios, algo de evidencia
Falta profundidad en los "qué buscar"
Aceptable (11-16 puntos)
Descripción: Rúbrica básica, cubre dimensiones pero falta precisión.
Criterios:
Define 2-3 dimensiones, pesos no muy claros
Tiene niveles pero sin criterios claros de diferenciación
Sin ejemplos específicos
"Qué buscar" es vago (ej: "buena documentación" en vez de "README > 300 palabras")
Ambigüedades sin resolver
Evidencia a buscar:
rubrica.md existe pero corta (300-500 palabras)
Describe dimensiones pero no cómo evaluarlas
Sin ejemplos o "qué buscar"
Deficiente (0-10 puntos)
Descripción: Rúbrica incompleta o poco útil. Imposible que un agente la aplique consistentemente.
Criterios:
Falta estructura clara
Dimensiones vagas
Sin escalas o rangos
Sin criterios específicos
Un agente no sabe qué hacer
Evidencia a buscar:
rubrica.md ausente o < 300 palabras
No tiene niveles, criterios, o ejemplos
---
2. AGENTE CORRECTOR FUNCIONANDO (25 puntos)
¿Qué se evalúa?
El agente corrector (el system prompt) corre en la práctica. Lee un repositorio real, aplica la rúbrica y devuelve un formato completo y consistente.
Excelente (22-25 puntos)
Descripción: El agente corre perfectamente, evalúa repositorios reales, devuelve formato completo consistentemente.
Criterios:
El agente (system prompt) se aplica sin errores a repositorios reales
Devuelve TODAS las dimensiones con: puntaje + justificación + evidencia citada
Formato salida es JSON válido y consistente (misma estructura cada vez)
Explica cada puntaje citando evidencia específica del repo (ej: "README.md de 450 palabras")
Propone mejora concreta y accionable
Pruebas documentadas en 3 casos diferentes
Evidencia a buscar:
Carpeta casos/ con 3 ejemplos evaluados
Para cada caso: output del agente en JSON válido
Cada output tiene: puntajes, justificaciones CON EVIDENCIA, sugerencia mejora
Formato es idéntico en los 3 casos (estructura JSON igual)
Sin errores de formato o parseo
Ejemplo de excelente:
```json
{
  "evaluacion": {
    "rubrica": { "puntaje": 22, "justificacion": "Vi README.md de 650 palabras con escalas...", "evidencia": ["README > 600 palabras", "4 niveles claros"] },
    "agente_corrector": { "puntaje": 23, ... },
    "puntaje_total": 95,
    "sugerencia": "Para mejorar, agregar ejemplos de ejecución en README"
  }
}
```
Bueno (17-21 puntos)
Descripción: El agente funciona bien, evalúa correctamente, formato es casi perfecto.
Criterios:
El agente evalúa sin errores críticos
Devuelve todas las dimensiones con puntajes y justificaciones
Formato es mostly consistente (pequeñas variaciones)
Cite evidencia pero algo superficial
Sugerencia presente pero genérica
Evaluó al menos 2 casos
Evidencia a buscar:
2+ casos evaluados
Outputs en formato similar
Justificaciones presentes pero menos detalladas
Pequeñas inconsistencias de formato
Aceptable (11-16 puntos)
Descripción: El agente funciona parcialmente. Falta algo en la salida o hay inconsistencias.
Criterios:
El agente produce salida pero incompleta
Faltan dimensiones O faltan justificaciones
Formato no es consistente entre evaluaciones
Evidencia es mínima o genérica
Sugerencia falta o no es útil
Evidencia a buscar:
1-2 casos evaluados
Salida incompleta (faltan campos)
Formato varía entre casos
Deficiente (0-10 puntos)
Descripción: El agente no funciona o la salida es inutilizable.
Criterios:
No se puede aplicar a un repositorio real
Salida confusa o incoherente
No es JSON válido o no tiene estructura
Sin justificaciones
Sin evidencia
Evidencia a buscar:
Ningún caso evaluado correctamente
Output es texto suelto, no JSON
Imposible entender qué evaluó
---
3. CASOS DE PRUEBA (20 puntos)
¿Qué se evalúa?
Existen 3 casos de prueba bien construidos. El agente los evalúa y los DISTINGUE correctamente.
Excelente (18-20 puntos)
Descripción: Tres casos realistas y diferenciados. El agente les da notas DIFERENTES y apropiadas. Detecta el tramposo.
Criterios:
Caso Excelente:
Proyecto realista y bien hecho (código > 200 líneas O equivalente)
Documentación completa y profesional
Código limpio, comentado
README claro con instrucciones paso a paso
Tests/pruebas presentes
El agente le da: 85+ puntos
Caso Flojo:
Proyecto incompleto o de baja calidad
Documentación mínima (README < 100 palabras)
Código sin comentarios, desorganizado
Faltan features importantes
Tests mínimos o ausentes
El agente le da: 40-60 puntos
Caso Tramposo:
README afirma features que NO están en el código
Infla números (menciona "20 tests" pero tiene 2)
Código es simple pero README lo describe como avanzado
Afirma documentación que no existe
DETECCIÓN: El agente lo detecta y lo marca como "inconsistencias"
El agente le da: 50-70 puntos (BAJA nota porque ve las mentiras)
Diferenciación:
Notas entre casos son CLARAMENTE diferentes (no: 82, 80, 78)
El agente JUSTIFICA por qué cada uno recibe su nota
Detecta mentiras en tramposo: "README dice 'X' pero no encontré evidencia"
Evidencia a buscar:
Carpeta casos/ existe con: excelente/, flojo/, tramposo/
Cada caso tiene README.md, código, estructura
Los casos son evidentemente diferentes (no copias con pequeños cambios)
Agente evalúa los 3: outputs en JSON para cada uno
Notas claramente distribuidas: ej 92, 55, 68
Ejemplo de diferenciación:
```
CASO EXCELENTE: 92 puntos → "README de 520 palabras, 150 líneas código comentado, tests presentes"
CASO FLOJO: 55 puntos → "README de 80 palabras, 40 líneas código sin comentarios, sin tests"
CASO TRAMPOSO: 65 puntos → "README afirma 'IA avanzada' pero código usa solo APIs simples. INCONSISTENCIA DETECTADA"
```
Bueno (14-17 puntos)
Descripción: Los 3 casos existen y son diferenciados. El agente casi siempre los distingue.
Criterios:
Los 3 casos están presentes
Casos son distintos pero podrían ser más realistas
Agente los evalúa pero:
Notas son algo parecidas (ej: 85, 80, 78)
Detecta tramposo pero no explica bien la mentira
Justificaciones son correctas pero genéricas
Evidencia a buscar:
3 carpetas con contenido diferente
Agente produce 3 evaluaciones
Notas diferentes pero no tan claras
Aceptable (10-13 puntos)
Descripción: Casos presentes pero poco diferenciados. El agente los confunde parcialmente.
Criterios:
Los 3 casos existen pero son muy similares
Agente da notas parecidas (ej: 75, 73, 71)
No se ve claramente qué hace cada uno diferente
Tramposo no es claramente detectado
Evidencia a buscar:
Carpetas existen pero contenido parecido
Agente da notas similares
Deficiente (0-9 puntos)
Descripción: Casos ausentes, vacíos, o agente no los distingue en absoluto.
Criterios:
Faltan carpetas O están vacías
Los 3 casos no se pueden diferenciar
Agente no los evalúa o produce el mismo puntaje
Evidencia a buscar:
Carpetas faltando O vacías
Agente no evalúa los casos
---
4. CALIBRACIÓN DOCUMENTADA (15 puntos)
¿Qué se evalúa?
¿El grupo probó el agente? ¿Documentó desacuerdos? ¿Iteró y ajustó? ¿Reflexionó sobre el proceso?
Excelente (13-15 puntos)
Descripción: Calibración exhaustiva, bien documentada, con iteraciones y reflexión.
Criterios:
Archivo calibracion.md detallado (300+ palabras)
Muestra EXPLÍCITAMENTE:
Notas que dio el agente en los 3 casos
Notas que hubiera puesto el grupo manualmente
Dónde coincidieron, dónde no
Ejemplo: "Caso flojo: Agente 52, Nosotros 55 → Desacuerdo en Rúbrica"
Documenta iteraciones:
"Primer borrador: agente fue muy duro en Funcionalidad"
"Ajustamos la rúbrica: agregamos ejemplos de 'código flojo'"
"Segunda prueba: ahora coincide"
Reflexión clara: "Lo que aprendimos fue..."
Menciona al menos 2 desacuerdos encontrados y resueltos
Evidencia a buscar:
calibracion.md existe con 300+ palabras
Tiene secciones: "Prueba inicial", "Desacuerdos", "Ajustes realizados", "Resultado final"
Números específicos: "Agente: 82, Grupo: 80"
Menciona cambios concretos: "modificamos sección X de la rúbrica"
Ejemplo de excelente:
```markdown
# Calibración

## Prueba inicial
- Caso excelente: Agente 88, Nosotros 90 (pequeño desacuerdo)
- Caso flojo: Agente 45, Nosotros 60 (GRAN desacuerdo)
- Caso tramposo: Agente 70, Nosotros 65

## Desacuerdos encontrados
En "Casos de Prueba", el agente fue demasiado indulgente con el flojo.
Probablemente porque nuestra rúbrica no daba criterios claros.

## Ajustes realizados
Reescribimos la sección "Caso Flojo" de la rúbrica:
- Antes: "Proyecto incompleto"
- Después: "Proyecto incompleto: README < 100 palabras, código < 100 líneas sin comentarios"

## Prueba final
- Caso excelente: Agente 89, Nosotros 90 ✓
- Caso flojo: Agente 59, Nosotros 60 ✓
- Caso tramposo: Agente 68, Nosotros 65 ✓
```
Bueno (10-12 puntos)
Descripción: Calibración presente, algunos desacuerdos documentados, ajustes realizados.
Criterios:
calibracion.md presente (150-300 palabras)
Muestra notas iniciales y finales
Documenta 1-2 desacuerdos
Explica qué ajustes hizo
Falta: reflexión profunda O segunda iteración clara
Evidencia a buscar:
Archivo con secciones básicas
Números específicos presentes
Cambios documentados pero sin mucho detalle
Aceptable (7-9 puntos)
Descripción: Calibración presente pero superficial. Pocos detalles.
Criterios:
calibracion.md corto (80-150 palabras)
Muestra notas pero sin detalles
Menciona ajustes pero sin especificar cuáles
Sin reflexión clara
Una sola iteración
Evidencia a buscar:
Archivo existe pero breve
Solo números sin explicación
Deficiente (0-6 puntos)
Descripción: Sin calibración documentada o sin evidencia de iteración.
Criterios:
calibracion.md ausente O vacío
No se documentó si el agente coincidió con el grupo
Sin desacuerdos ni ajustes mencionados
Sin reflexión
---
5. PROCESO GRUPAL (15 puntos)
¿Qué se evalúa?
La historia de commits muestra trabajo real: quién aportó qué, cómo evolucionó la rúbrica, decisiones registradas.
Excelente (13-15 puntos)
Descripción: Commits variados, colaborativos, con mensajes descriptivos. La historia cuenta la evolución real.
Criterios:
Mínimo 10 commits en el repositorio
3+ personas diferentes son autoras de commits
Commits distribuidos (no todo el último día)
Mensajes descriptivos, no genéricos:
✓ "feat: agregar escalas por nivel en rúbrica"
✗ "update", "fix", "changes"
La historia de commits muestra evolución:
"docs: rúbrica inicial" → "refactor: mejorar criterios de Funcionalidad" → "calibration: ajustar escalas tras prueba"
Menciona en commits decisiones clave
Evidencia a buscar:
En GitHub: git log muestra 10+ commits
Múltiples autores: "Juana, Marcos, Carla, Santiago"
Fechas distribuidas (no todos en el último día)
Mensajes claros que explican qué y por qué
Ejemplo de buena historia:
```
commit 45a2b1 (Santiago) - "docs: rúbrica inicial con 4 dimensiones"
commit 38c9d2 (Juana) - "feat: agregar niveles de puntaje a rúbrica"
commit 2f1e4a (Marcos) - "refactor: mejorar criterios en Funcionalidad"
commit 91k8l3 (Carla) - "agente: crear system prompt inicial"
commit 5x3c7e (Santiago) - "test: evaluar caso excelente"
commit 6y4d8f (Juana) - "calibration: desacuerdo en Casos, ajustamos"
commit 7z5e9g (Marcos) - "refactor: rúbrica v2 basada en calibración"
...
```
Bueno (10-12 puntos)
Descripción: Commits presentes, pero menos variados o algo tarde en el tiempo.
Criterios:
6-9 commits
2-3 autores
Mensajes mostly descriptivos
Algunos commits cerca del final pero no todos
La historia es clara pero menos detallada
Evidencia a buscar:
Commits distribuidos más en el tiempo
2+ autores presentes
Aceptable (7-9 puntos)
Descripción: Commits presentes pero concentrados. Pocos autores.
Criterios:
3-5 commits
Principalmente una persona (quizá una segunda)
Mensajes genéricos
Commits mostly en los últimos días
Evidencia a buscar:
Pocos commits
Mostly de una persona
Deficiente (0-6 puntos)
Descripción: Un único commit o no hay historia.
Criterios:
Un solo commit (todo al final)
Todos de la misma persona
Sin evidencia de proceso colaborativo
---
PUNTAJE TOTAL
Suma de las 5 dimensiones: 0 a 100 puntos
Cálculo:
Rúbrica ejecutable: 0-25
Agente corrector: 0-25
Casos de prueba: 0-20
Calibración: 0-15
Proceso grupal: 0-15
TOTAL: 0-100
Interpretación:
85-100: Excelente — Listo para prueba de fuego, muy probable de ganar
75-84: Bueno — Funciona bien, algunos ajustes podrían mejorar el desempeño
65-74: Aceptable — Funcional pero incompleto, riesgo moderado en prueba de fuego
50-64: Deficiente — Necesita trabajo importante antes de la prueba
< 50: Crítico — No está listo, alto riesgo de fallar en vivo
---
NOTAS PARA EL AGENTE EVALUADOR
La rúbrica define todo. Si no es precisa, el agente no funciona bien. Sé estricto aquí.
Funcionalidad es crítica. Si el agente no corre o produce basura, eso baja mucho.
Detecta tramposos. En Casos de Prueba, verifica que el tramposo sea realmente distinto y que el agente lo vea.
Valora la iteración. Un equipo que falló en primera calibración pero lo documentó y ajustó suma MÁS que perfección sin reflexión.
Cita SIEMPRE. "README.md de 450 palabras", "5 commits de 3 autores", "Desacuerdo en rúbrica, ajustaron X".
Sé justo pero riguroso. El objetivo es un agente evaluador que funcione en la prueba de fuego.
