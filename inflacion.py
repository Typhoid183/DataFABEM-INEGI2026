import pandas as pd
import numpy as np
from datetime import datetime

# Crear dataset de Inflación General 2027
inflacion_general = {
    'Mes': ['Dic-24', 'Ene-25', 'Feb-25', 'Mar-25', 'Abr-25', 'May-25', 'Jun-25', 
            'Jul-25', 'Ago-25', 'Sep-25', 'Oct-25', 'Nov-25', 'Dic-25', 'Ene-26', 
            'Feb-26', 'Mar-26', 'Abr-26', 'May-26', 'Jun-26', 'Jul-26', 'Ago-26', 'Sep-26'],
    'Media': [3.68, 3.71, 3.69, 3.68, 3.68, 3.68, 3.7, 3.71, 3.71, 3.75, 3.78, 3.74, 
              3.74, 3.77, 3.78, 3.82, 3.82, 3.84, 3.86, 3.85, 3.85, np.nan],
    'Mediana': [3.7, 3.72, 3.7, 3.7, 3.72, 3.71, 3.72, 3.73, 3.75, 3.75, 3.71, 3.7, 
                3.7, 3.73, 3.75, 3.8, 3.8, 3.84, 3.84, 3.84, 3.84, np.nan],
    'Q1': [3.51, 3.55, 3.5, 3.5, 3.52, 3.51, 3.6, 3.5, 3.5, 3.57, 3.61, 3.59, 
           3.61, 3.64, 3.65, 3.67, 3.7, 3.73, 3.75, 3.73, 3.75, np.nan],
    'Q3': [3.8, 3.9, 3.88, 3.85, 3.81, 3.83, 3.8, 3.84, 3.83, 3.96, 3.92, 3.85, 
           3.82, 3.98, 3.95, 3.99, 4.0, 3.97, 4.0, 3.99, 3.93, np.nan],
    'Minimo': [3.19, 3.19, 3.19, 3.19, 3.0, 3.19, 3.1, 3.16, 3.16, 3.16, 3.16, 3.16, 
               3.16, 3.09, 3.3, 3.37, 3.37, 3.45, 3.44, 3.32, 3.5, np.nan],
    'Maximo': [4.02, 4.04, 4.04, 4.34, 4.26, 4.04, 4.23, 4.67, 4.65, 4.63, 4.63, 4.35, 
               4.35, 4.33, 4.37, 4.34, 4.34, 4.4, 4.5, 4.5, 4.54, np.nan],
    'Desv_Estandar': [0.24, 0.23, 0.23, 0.28, 0.27, 0.24, 0.26, 0.3, 0.3, 0.33, 0.3, 0.25, 
                      0.26, 0.25, 0.25, 0.24, 0.23, 0.22, 0.21, 0.22, 0.21, np.nan],
    'N_Respuestas': [30, 31, 31, 31, 34, 34, 33, 36, 38, 38, 34, 36, 35, 39, 40, 39, 43, 43, 41, 42, 41, np.nan],
    'Tipo': ['Inflación General'] * 22
}

df_general = pd.DataFrame(inflacion_general)

# Crear dataset de Inflación Subyacente 2027
inflacion_subyacente = {
    'Mes': ['Dic-24', 'Ene-25', 'Feb-25', 'Mar-25', 'Abr-25', 'May-25', 'Jun-25', 
            'Jul-25', 'Ago-25', 'Sep-25', 'Oct-25', 'Nov-25', 'Dic-25', 'Ene-26', 
            'Feb-26', 'Mar-26', 'Abr-26', 'May-26', 'Jun-26', 'Jul-26', 'Ago-26', 'Sep-26'],
    'Media': [3.56, 3.61, 3.61, 3.61, 3.59, 3.64, 3.67, 3.65, 3.65, 3.7, 3.69, 3.67, 
              3.76, 3.71, 3.73, 3.8, 3.81, 3.85, 3.8, 3.84, 3.82, np.nan],
    'Mediana': [3.54, 3.6, 3.6, 3.6, 3.6, 3.6, 3.65, 3.61, 3.6, 3.65, 3.7, 3.65, 
                3.75, 3.75, 3.74, 3.75, 3.8, 3.86, 3.8, 3.86, 3.8, np.nan],
    'Q1': [3.43, 3.4, 3.4, 3.4, 3.4, 3.48, 3.51, 3.51, 3.51, 3.54, 3.51, 3.53, 
           3.6, 3.6, 3.61, 3.62, 3.65, 3.7, 3.7, 3.7, 3.72, np.nan],
    'Q3': [3.72, 3.8, 3.8, 3.8, 3.76, 3.8, 3.8, 3.78, 3.77, 3.8, 3.83, 3.83, 
           3.95, 3.89, 3.89, 3.9, 3.95, 3.95, 3.92, 3.98, 3.92, np.nan],
    'Minimo': [2.9, 3.0, 3.0, 3.0, 3.0, 3.0, 3.01, 3.01, 3.01, 3.01, 3.01, 3.01, 
               3.12, 2.84, 3.0, 3.2, 3.2, 3.27, 3.04, 3.37, 3.27, np.nan],
    'Maximo': [4.0, 4.0, 4.04, 4.08, 4.4, 4.9, 4.87, 4.82, 4.84, 4.8, 4.38, 4.18, 
               4.38, 4.34, 4.4, 4.87, 4.4, 4.52, 4.33, 4.41, 4.46, np.nan],
    'Desv_Estandar': [0.26, 0.26, 0.26, 0.27, 0.3, 0.34, 0.36, 0.32, 0.3, 0.35, 0.28, 0.26, 
                      0.29, 0.32, 0.31, 0.33, 0.26, 0.24, 0.24, 0.21, 0.2, np.nan],
    'N_Respuestas': [28, 29, 29, 29, 31, 32, 31, 33, 35, 36, 33, 35, 34, 37, 38, 37, 41, 41, 39, 38, 38, np.nan],
    'Tipo': ['Inflación Subyacente'] * 22
}

df_subyacente = pd.DataFrame(inflacion_subyacente)

# Combinar ambos datasets
df_completo = pd.concat([df_general, df_subyacente], ignore_index=True)

# Agregar metadatos
df_completo['Fuente'] = 'Banxico - Encuestas Especialistas Economía'
df_completo['Fecha_Consulta'] = '2026-09-16 16:24'
df_completo['Horizonte_Proyeccion'] = 'Dic 2027 (dic-dic)'

print("=" * 80)
print("DATASET INFLACIÓN BANXICO - EXPECTATIVAS 2027")
print("=" * 80)
print(df_completo.head(10))
print("\n")

# ============ GUARDAR EN DIFERENTES FORMATOS ============

# 1. CSV
df_completo.to_csv('inflacion_banxico_2027.csv', index=False, encoding='utf-8')
print("✓ Guardado: inflacion_banxico_2027.csv")

# 2. Excel
df_completo.to_excel('inflacion_banxico_2027.xlsx', index=False)
print("✓ Guardado: inflacion_banxico_2027.xlsx")

# 3. JSON
df_completo.to_json('inflacion_banxico_2027.json', orient='records', indent=2)
print("✓ Guardado: inflacion_banxico_2027.json")

# ============ ANÁLISIS ESTADÍSTICO ============

print("\n" + "=" * 80)
print("ANÁLISIS ESTADÍSTICO")
print("=" * 80)

# Resumen por tipo de inflación
print("\nInflación General - Estadísticas:")
print(df_general[['Media', 'Mediana', 'Desv_Estandar', 'N_Respuestas']].describe())

print("\nInflación Subyacente - Estadísticas:")
print(df_subyacente[['Media', 'Mediana', 'Desv_Estandar', 'N_Respuestas']].describe())

# ============ VISUALIZACIÓN (OPCIONAL) ============

import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 1, figsize=(14, 8))

# Gráfica 1: Inflación General
axes[0].plot(df_general['Mes'], df_general['Media'], marker='o', label='Media', linewidth=2)
axes[0].fill_between(range(len(df_general)), df_general['Q1'], df_general['Q3'], 
                      alpha=0.3, label='Rango Intercuartílico')
axes[0].set_title('Expectativas de Inflación General 2027 (dic-dic)', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Inflación (%)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)
axes[0].tick_params(axis='x', rotation=45)

# Gráfica 2: Inflación Subyacente
axes[1].plot(df_subyacente['Mes'], df_subyacente['Media'], marker='s', 
             label='Media', linewidth=2, color='orange')
axes[1].fill_between(range(len(df_subyacente)), df_subyacente['Q1'], df_subyacente['Q3'], 
                      alpha=0.3, label='Rango Intercuartílico', color='orange')
axes[1].set_title('Expectativas de Inflación Subyacente 2027 (dic-dic)', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Mes de Levantamiento')
axes[1].set_ylabel('Inflación (%)')
axes[1].legend()
axes[1].grid(True, alpha=0.3)
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('inflacion_banxico_2027.png', dpi=300, bbox_inches='tight')
print("\n✓ Gráfica guardada: inflacion_banxico_2027.png")
plt.show()

# ============ ESTADÍSTICAS FINALES ============

print("\n" + "=" * 80)
print("RESUMEN DE DATOS")
print("=" * 80)
print(f"Total de registros: {len(df_completo)}")
print(f"Período: Diciembre 2024 - Septiembre 2026")
print(f"Tipos de inflación: {df_completo['Tipo'].unique().tolist()}")
print(f"Rango Media General: {df_general['Media'].min():.2f}% - {df_general['Media'].max():.2f}%")
print(f"Rango Media Subyacente: {df_subyacente['Media'].min():.2f}% - {df_subyacente['Media'].max():.2f}%")
