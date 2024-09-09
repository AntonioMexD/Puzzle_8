import pandas as pd

# Cargar los resultados
df = pd.read_csv('experiments_results.csv')

# Verificar los nombres de las columnas
print(df.columns)

# Análisis
summary = df.groupby(['Search Algorithm', 'Heuristic']).agg({
    'Found Solution': 'mean',  # Promedio de encontrar solución
    'Time': 'mean',            # Tiempo promedio
    'Max Frontier Size': 'mean'  # Tamaño máximo de la frontera promedio
}).reset_index()

print(summary)
