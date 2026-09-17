import pandas as pd
import numpy as np

# ============ DATOS LIMPIOS - PREESCOLAR CDMX Y EDOMEX ============

datos = {
    'Ciclo': ['2000/2001', '2005/2006', '2010/2011', '2015/2016', '2020/2021', 
              '2021/2022', '2022/2023', '2023/2024', '2024/2025'],
    'Año': [2000.5, 2005.5, 2010.5, 2015.5, 2020.5, 2021.5, 2022.5, 2023.5, 2024.5],
    'CDMX': [59.4, 69.0, 73.5, 80.1, 71.6, 69.4, 75.4, 74.9, 71.5],
    'EdoMex': [34.3, 58.2, 61.3, 64.3, 59.6, 56.7, 61.1, 58.1, 53.9]
}

df = pd.DataFrame(datos)

# Guardar
df.to_csv('preescolar_cdmx_edomex.csv', index=False)
df.to_excel('preescolar_cdmx_edomex.xlsx', index=False)

# ============ REGRESIÓN LINEAL SIMPLE ============

def regresion_lineal(x, y):
    """Calcula pendiente (a) e intercepto (b) para y = a*x + b"""
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    sum_x2 = sum(x[i]**2 for i in range(n))
    
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    b = (sum_y - a * sum_x) / n
    
    return a, b

# Calcular parámetros
años = df['Año'].values
a_cdmx, b_cdmx = regresion_lineal(años, df['CDMX'].values)
a_edomex, b_edomex = regresion_lineal(años, df['EdoMex'].values)

# ============ FUNCIÓN PARA PREDICCIONES ============

def predecir(año, entidad='CDMX'):
    """
    Predice asistencia a preescolar
    
    Args:
        año (float): Año a predecir (ej: 2026.5 para ciclo 2026/2027)
        entidad (str): 'CDMX' o 'EdoMex'
    
    Returns:
        float: Tasa predicha (%)
    """
    if entidad == 'CDMX':
        pred = a_cdmx * año + b_cdmx
    else:
        pred = a_edomex * año + b_edomex
    
    return round(max(0, min(100, pred)), 2)

# ============ EJEMPLO DE USO ============

print("PREDICCIONES - ASISTENCIA PREESCOLAR\n")
print("=" * 45)

años_test = [2025.5, 2026.5, 2027.5, 2028.5, 2029.5, 2030.5]

for año in años_test:
    ciclo = f"{int(año)}/{int(año)+1}"
    print(f"{ciclo}: CDMX {predecir(año, 'CDMX')}% | EdoMex {predecir(año, 'EdoMex')}%")

# ============ GUARDAR PREDICCIONES ============

predicciones = pd.DataFrame({
    'Ciclo': [f"{int(año)}/{int(año)+1}" for año in años_test],
    'CDMX': [predecir(año, 'CDMX') for año in años_test],
    'EdoMex': [predecir(año, 'EdoMex') for año in años_test]
})

predicciones.to_csv('predicciones.csv', index=False)

print("\n✓ Archivos generados:")
print("  - preescolar_cdmx_edomex.csv")
print("  - preescolar_cdmx_edomex.xlsx")
print("  - predicciones.csv")