import matplotlib.pyplot as plt
import numpy as np

# Configuración general
plt.figure(figsize=(12, 6))

# --- Gráfico DISCRETO (Dado) ---
plt.subplot(1, 2, 1)  # 1 fila, 2 columnas, primer gráfico

resultados = [1, 2, 3, 4, 5, 6]
probabilidad = [1/6] * 6  # Probabilidad uniforme

plt.bar(resultados, probabilidad, color='skyblue', edgecolor='black', width=0.8)
plt.title("Datos Discretos\nLanzamiento de un dado", fontweight='bold')
plt.xlabel("Resultados posibles")
plt.ylabel("Probabilidad")
plt.ylim(0, 0.3)

# --- Gráfico CONTINUO (Temperatura) ---
plt.subplot(1, 2, 2)  # 1 fila, 2 columnas, segundo gráfico

horas = np.linspace(0, 24, 1000)  # 1000 puntos entre 0 y 24
temperatura = 15 + 10 * np.sin(2 * np.pi * horas / 24)  # Simulación de temperatura

plt.plot(horas, temperatura, color='tomato', linewidth=2)
plt.title("Datos Continuos\nTemperatura en un día", fontweight='bold')
plt.xlabel("Hora del día")
plt.ylabel("Temperatura (°C)")
plt.grid(True, linestyle='--', alpha=0.5)

# Ajustes finales
plt.tight_layout()  # Evita solapamiento
plt.show()