# Planning — Agente Evaluador (Parcial)

1. Definir el rol antes de escribir nada: el agente corrige TRABAJOS FINALES, no parciales — usa la rúbrica oficial del trabajo final (Sistema completo 30, Proceso documentado 25, Formato 15, Análisis económico 15, Gobierno y riesgo 15).
2. Escribir primero la rúbrica ejecutable, basada en esa rúbrica oficial.
3. Escribir el system prompt del agente corrector, derivado de la rúbrica (mismas 5 dimensiones y pesos en el JSON de salida).
4. Construir los 3 casos de prueba (excelente / flojo / tramposo), simulando trabajos finales reales.
5. Correr el agente contra los 3 casos y documentar la calibración con números concretos.
6. Ajustar rúbrica/prompt según los desacuerdos y volver a probar.
7. Gestionar todo con una rama por artefacto y commits frecuentes y descriptivos (criterio "Proceso grupal").
