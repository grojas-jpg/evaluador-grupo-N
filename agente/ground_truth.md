# GROUND TRUTH V6 - Fuentes de Verdad Explícitas

## Jerarquía de Autoridad (Cuando hay Conflictos)

```
NIVEL 1 (CANON - VERDAD SUPREMA):
  corridas/**/01_salida.json     ← Output real
  corridas/**/analysis.json

NIVEL 2 (ESPECIFICACIÓN):
  agente/system_prompt.md        ← Definición oficial
  agente/configuracion.md
  calibracion.md

NIVEL 3 (DOCUMENTACIÓN):
  DECISIONES.md                  ← Explicación
  README.md

NIVEL 4 (COMENTARIOS):
  Comentarios en código
```

---

## Ejemplo 1: Conflicto de Costo

**Conflicto:**
```
README.md (Nivel 3):         "USD 0.005"
analisis_economico.md (L3):  "USD 0.003"
corridas/01_salida.json (L1):"USD 0.0008" ← VERDAD
```

**Resolución:**
- Usa Nivel 1 = USD 0.0008
- Registra conflicto
- Penaliza inconsistencia (-1 pt)

---

## Ejemplo 2: Conflicto de Herramienta

**Conflicto:**
```
system_prompt.md (L2):       "OpenAI GPT-4"
DECISIONES.md (L3):          "Google Vertex"
No hay evidencia en corridas/
```

**Resolución:**
- Usa system_prompt.md (Nivel 2)
- Busca evidencia en Nivel 1
- Si no existe → -2 puntos

---

## Ejemplo 3: Conflicto de Iteraciones

**Conflicto:**
```
README.md:        "50 iteraciones"
git log:          "150 commits"
corridas/:        "3 archivos"
```

**Resolución:**
- Usa git log (Nivel 2)
- Explica discrepancia
- Si injustificado → -2 puntos

---

## Regla: Automático y Justo

Sin ambigüedad. Sin interpretación. Jerarquía clara.
