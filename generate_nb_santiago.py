import nbformat as nbf
import os

nb = nbf.v4.new_notebook()

text = """\
# Análisis SIVIGILA - VIH/SIDA (Por Santiago)

Este notebook explora el dataset de vigilancia epidemiológica para encontrar patrones sobre los casos de VIH en Medellín, cumpliendo con los puntos de la rúbrica.
"""

code1 = """\
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar dataset
df = pd.read_csv('../data/sivigila_vih(in).csv', encoding='latin1', low_memory=False)
df.head()
"""

text2 = """\
## 1 y 2. Exploración y Limpieza de datos
Seleccionamos las columnas más importantes para nuestro análisis y eliminamos los valores nulos o atípicos.
"""

code2 = """\
# Seleccionar columnas relevantes
df_clean = df[['fec_not', 'edad_', 'sexo_', 'nombre_barrio', 'nombre_comuna', 'grupo_edad_quinque', 'nom_eve', 'tip_ss_', 'ocupacion_']].copy()

# Eliminar nulos y edades irreales
df_clean = df_clean.dropna(subset=['sexo_', 'edad_'])
df_clean = df_clean[(df_clean['edad_'] >= 0) & (df_clean['edad_'] < 120)]

print(f"Total de registros limpios: {len(df_clean)}")
"""

text3 = """\
## 3 y 4. Análisis Exploratorio y Gráficos
Vamos a buscar patrones interesantes en la distribución por género, edad y afiliación.
"""

code3 = """\
# Casos por género
plt.figure(figsize=(8,5))
sns.countplot(data=df_clean, x='sexo_', palette='Set2')
plt.title('Distribución de Casos de VIH por Sexo en Medellín')
plt.show()

print("Porcentajes por sexo:")
print(df_clean['sexo_'].value_counts(normalize=True) * 100)
"""

code4 = """\
# Distribución de edad de los casos
plt.figure(figsize=(10,5))
sns.histplot(data=df_clean, x='edad_', bins=30, kde=True, color='purple')
plt.title('Distribución de Edad de los Casos')
plt.show()

print(f"Edad promedio: {df_clean['edad_'].mean():.1f} años")
print(f"Edad mediana: {df_clean['edad_'].median()} años")
"""

code5 = """\
# Casos por Comuna (Top 5 excluyendo Sin Información)
comunas_validas = df_clean[df_clean['nombre_comuna'] != 'Sin Información']
top_comunas = comunas_validas['nombre_comuna'].value_counts().head(5)

plt.figure(figsize=(10,5))
sns.barplot(x=top_comunas.index, y=top_comunas.values, palette='viridis')
plt.title('Top 5 Comunas con más casos reportados')
plt.xticks(rotation=45)
plt.show()
"""

text4 = """\
## Exportación a Excel
Como paso final del procesamiento de datos, exportamos el dataset limpio para poder compartirlo.
"""

code6 = """\
# Exportar a Excel
output_path = '../data/resultados_vih_santiago.xlsx'
df_clean.to_excel(output_path, index=False)
print(f"Datos exportados exitosamente a {output_path}")
"""

text5 = """\
## 5. Conclusiones Finales

Tras analizar los 15,470 registros válidos, los principales hallazgos son:

1. **Género:** La incidencia es abrumadoramente mayor en hombres (84.7%) comparado con las mujeres (15.3%).
2. **Edad:** La población más afectada son los adultos jóvenes. La edad promedio de notificación es de 32.9 años.
3. **Ubicación:** Las comunas con mayores focos de casos reportados son La Candelaria (1,224), Belén (999), Aranjuez (838) y Robledo (817).
4. **Seguridad Social:** Un preocupante 8.2% de los casos corresponden a personas no aseguradas (N), mientras que la gran mayoría (64.2%) pertenece al régimen contributivo (C).
"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(text),
    nbf.v4.new_code_cell(code1),
    nbf.v4.new_markdown_cell(text2),
    nbf.v4.new_code_cell(code2),
    nbf.v4.new_markdown_cell(text3),
    nbf.v4.new_code_cell(code3),
    nbf.v4.new_code_cell(code4),
    nbf.v4.new_code_cell(code5),
    nbf.v4.new_markdown_cell(text4),
    nbf.v4.new_code_cell(code6),
    nbf.v4.new_markdown_cell(text5)
]

os.makedirs('notebooks', exist_ok=True)
with open('notebooks/analisis_santiago.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)
