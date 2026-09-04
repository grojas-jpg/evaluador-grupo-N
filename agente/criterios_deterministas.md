# CRITERIOS DETERMINISTAS V6

## Principio: SIN SUBJETIVIDAD

Cada criterio usa verificación mecánica paso-a-paso. No hay interpretación ("suficiente", "adecuado"). 

### SC-01: Contrato de Entrada (6 Piezas)

**Pasos:**
1. ¿Existe agente/configuracion.md? → SÍ/NO
2. ¿Contiene sección "Contrato de Entrada"? → SÍ/NO
3. ¿Identifica exactamente 6 piezas (campos)? → SÍ/NO
4. ¿Cada pieza tiene ≥20 palabras de descripción? → SÍ/NO

**Resultado:**
- Cumple todos → **6 puntos**
- Falta paso 3 o 4 → **4 puntos**
- Falta paso 2 → **2 puntos**
- Falta paso 1 → **0 puntos**

---

### SC-02: Herramienta Real

**Pasos:**
1. ¿Existe agente/herramienta.md? → SÍ/NO
2. ¿Contiene sección "Herramienta Utilizada"? → SÍ/NO
3. ¿Identifica nombre + versión + endpoint/librería? → SÍ/NO (3/3)
4. ¿Archivo ≥150 palabras? → SÍ/NO
5. ¿Hay evidencia de uso real (ejemplos, logs)? → SÍ/NO

**Resultado:**
- Cumple todos → **8 puntos**
- Cumple 1-4 → **5 puntos**
- Cumple 1-3 → **3 puntos**
- Cumple 1-2 → **0 puntos**

---

### SC-03: Salida JSON Estructurada

**Pasos:**
1. ¿Existe agente/contrato_salida.md? → SÍ/NO
2. ¿Define estructura JSON con esquema? → SÍ/NO
3. ¿Especifica ≥5 campos obligatorios? → SÍ/NO
4. ¿Hay validación/reglas para cada campo? → SÍ/NO

**Resultado:**
- Cumple todos → **7 puntos**
- Cumple 3/4 → **5 puntos**
- Cumple 2/4 → **3 puntos**
- Cumple 1/4 → **1 punto**
- Cumple 0/4 → **0 puntos**

---

### PD-01: Iteraciones Cronológicas (≥3 Cambios Reales)

**Pasos:**
1. ¿Existe carpeta corridas/? → SÍ/NO
2. ¿Hay ≥3 archivos corridas/*/01_salida.json? → SÍ/NO
3. ¿Cada corrida tiene timestamp DISTINTO (>1 min aparte)? → SÍ/NO
4. ¿Hay cambios REALES >20% entre corridas? → SÍ/NO

**Resultado:**
- Cumple todos, cambios reales → **9 puntos**
- Cumple 1-3, cambios parciales (10-20%) → **6 puntos**
- Cumple 1-2 → **3 puntos**
- Falta paso 2 → **0 puntos**

---

### FR-02: ≥3 Corridas Reproducibles

**Pasos:**
1. ¿≥3 corridas con estructura válida? → SÍ/NO
2. ¿Cada corrida tiene input + output + log? → SÍ/NO
3. ¿Output es reproducible (determinista)? → SÍ/NO

**Resultado:**
- Cumple todos, determinista → **13 puntos**
- Cumple 1-2, 99% similar → **11 puntos**
- Cumple 1-2, 90% similar → **8 puntos**
- Falta paso 1 → **0 puntos**

---

### AE-01: Costo por Corrida (Verificable)

**Pasos (Modo STRICT):**
1. ¿Existe analisis_economico.md? → SÍ/NO
2. ¿Declara costo con fuente verificable? → SÍ/NO
3. ¿El cálculo matemático es correcto? → SÍ/NO
4. ¿La fuente es oficial (URL, documento)? → SÍ/NO

**Resultado:**
- Cumple todos → **5 puntos**
- Cumple 1-3 → **3 puntos**
- Cumple 1-2 → **1 punto**
- Error matemático → **0 puntos - 3 penalización**

---

## Garantía: Dos evaluadores = SIEMPRE mismo resultado

Porque no hay interpretación, cada criterio es binario o cuantitativo.
