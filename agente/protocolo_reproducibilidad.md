# PROTOCOLO DE REPRODUCIBILIDAD V6

## Captura Obligatoria del Estado del Repositorio

Antes de evaluar CUALQUIER cosa, ejecutar estos comandos y registrar resultados:

```bash
# 1. Capturar SHA del commit actual
$ git rev-parse HEAD
# Ejemplo: 5fdd304c26097aa16dc6d065e8b1c3d6359e7010

# 2. Capturar checksums SHA256
$ sha256sum README.md rubrica.md agente/system_prompt.md agente/configuracion.md

# 3. Timestamp exacto
$ date -u +"%Y-%m-%dT%H:%M:%SZ"
# Ejemplo: 2026-09-04T15:32:45Z
```

## Registrar en JSON

**SIEMPRE incluir esta sección en el JSON de salida:**

```json
{
  "reproducibilidad": {
    "commit_sha": "5fdd304c26097aa16dc6d065e8b1c3d6359e7010",
    "timestamp_evaluacion": "2026-09-04T15:32:45Z",
    "archivo_checksums": {
      "README.md": "a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3",
      "rubrica.md": "f7e8d9c0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6",
      "agente/system_prompt.md": "c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4"
    },
    "puede_re_ejecutarse": true,
    "garantia_resultados_identicos": true
  }
}
```

## Verificación de Re-ejecución

```bash
# Git checkout al mismo commit
$ git checkout 5fdd304c26097aa16dc6d065e8b1c3d6359e7010

# Verificar checksums
$ sha256sum README.md | grep a3b4c5d6...
# Si coincide → ✅ Mismo código
# Si no → ❌ Repositorio fue modificado
```

## Beneficio

Re-ejecutar sobre el MISMO commit = EXACTAMENTE el mismo resultado.
Garantía de reproducibilidad 100%.
