import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leer el archivo CSV
file_path = './csv/ejercicio2.csv'

# Saltar las primeras filas innecesarias y cargar los datos correctamente
data = pd.read_csv(file_path, skiprows=1)  

# Asegurarse de que las columnas necesarias existan
if 'Sequence' in data.columns and 'Volt' in data.columns:
    x = data['Sequence']
    y = data['Volt']
else:
    print("Las columnas 'Sequence' y 'Volt' no se encontraron en el archivo CSV.")
    print("Por favor, verifica el archivo CSV.")
    exit()
    
    # Generar datos de ejemplo si no existen las columnas
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

# Graficar la onda seno
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Onda Seno', color='blue')
plt.title('Gráfica de Onda Seno')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()