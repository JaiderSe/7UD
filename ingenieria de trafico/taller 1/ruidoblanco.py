import numpy as np

import matplotlib.pyplot as plt

# Parámetros de la señal
fs = 1000  # Frecuencia de muestreo (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # Vector de tiempo de 1 segundo
f = 5  # Frecuencia de la señal (Hz)

# Crear señal limpia (onda senoidal)
clean_signal = np.sin(2 * np.pi * f * t)

# Generar interferencia
# 1. Ruido impulsivo aleatorio
impulsive_noise = np.zeros_like(t)
num_impulses = 20  # Número de impulsos
impulse_indices = np.random.choice(len(t), num_impulses, replace=False)
impulsive_noise[impulse_indices] = np.random.uniform(-5, 5, num_impulses)

# 2. Ruido de banda ancha
broadband_noise = np.random.normal(0, 0.5, len(t))

# Sumar interferencia a la señal
interference = impulsive_noise + broadband_noise
noisy_signal = clean_signal + interference

# Graficar las señales
plt.figure(figsize=(12, 8))

# Señal limpia
plt.subplot(3, 1, 1)
plt.plot(t, clean_signal, label="Señal limpia")
plt.title("Señal limpia")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.legend()

# Interferencia
plt.subplot(3, 1, 2)
plt.plot(t, interference, label="Interferencia", color="orange")
plt.title("Interferencia (Ruido impulsivo + Ruido de banda ancha)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.legend()

# Señal resultante
plt.subplot(3, 1, 3)
plt.plot(t, noisy_signal, label="Señal con interferencia", color="red")
plt.title("Señal resultante")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()