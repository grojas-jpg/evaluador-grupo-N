#!/usr/bin/env python3
"""
Validador de JSONs de calibración V6
Verifica: reproducibilidad, deteccion_fraude, weak_evidence, evidence_chain
"""

import json
import glob

REQUIRED_FIELDS = [
    'reproducibilidad',
    'sistema_completo_funcionando',
    'proceso_documentado',
    'formato_reproducibilidad',
    'analisis_economico',
    'gobierno_riesgo',
    'deteccion_fraude',
    'puntaje_total'
]

def validar_json(filepath):
    """Valida estructura JSON según V6"""
    try:
        with open(filepath) as f:
            data = json.load(f)
        
        # Verificar campos obligatorios
        for field in REQUIRED_FIELDS:
            assert field in data, f"Campo faltante: {field}"
        
        # Verificar reproducibilidad
        assert 'commit_sha' in data['reproducibilidad'], "Falta commit_sha"
        assert 'archivo_checksums' in data['reproducibilidad'], "Falta archivo_checksums"
        assert 'timestamp_evaluacion' in data['reproducibilidad'], "Falta timestamp"
        
        # Verificar fraude
        assert 'alertas_manipulacion' in data['deteccion_fraude'], "Falta alertas_manipulacion"
        
        print(f"✅ {filepath} válido")
        return True
    except Exception as e:
        print(f"❌ {filepath} INVÁLIDO: {e}")
        return False

if __name__ == '__main__':
    archivos = glob.glob('calibracion/resultados_v6/**/*.json', recursive=True)
    
    if not archivos:
        print("⚠️  No se encontraron JSONs en calibracion/resultados_v6/")
        exit(0)
    
    validos = sum(validar_json(f) for f in archivos)
    print(f"\n{validos}/{len(archivos)} JSONs válidos")
    
    exit(0 if validos == len(archivos) else 1)
