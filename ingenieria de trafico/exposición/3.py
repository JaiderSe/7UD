import matplotlib.pyplot as plt

# Definir la señal discreta (ejemplo: transmisión binaria [0, 1, 0, 1, 1])
tiempo = [0, 1, 2, 3,4,5,6,7,8,9]  # Tiempo en segundos (puntos de transición)
senal = [0, 1, 0, 1, 0, 1, 1, 0, 1, 0]    # Valores discretos (0V o 5V)

# Crear la gráfica estilo escalón (típico en señales digitales)
plt.figure(figsize=(10, 5))
plt.step(tiempo, senal, where='post', color='red', linewidth=1, label='Señal digital (5V)')
plt.scatter(tiempo, senal, color='black', s=50, zorder=10)  # Puntos de muestra

# Personalización
plt.title("Energía de Señal Discreta\nTransmisión Binaria", fontweight='bold')
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.yticks([0, 1], ['0V', '5V'])  # Valores discretos
plt.grid(True, linestyle='--', alpha=1)
plt.legend()
plt.tight_layout()
plt.show()