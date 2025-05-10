import numpy as np
import matplotlib.pyplot as plt

# Parámetros
fs = 1000  # Frecuencia de muestreo (Hz)
t = np.linspace(0, 1, fs)  # 1 segundo de señal
f = 5  # Frecuencia de la señal (Hz)

# Señal de entrada (continua)
x_t = 0.3 * np.sin(2 * np.pi * f * t) + 0.1 * np.random.randn(fs)  # Sinusoide + ruido

# Gráfica
plt.figure(figsize=(10, 4))
plt.plot(t, x_t, label='Señal de entrada $x(t)$')
plt.title('Señal de entrada continua con ruido')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()
plt.show()