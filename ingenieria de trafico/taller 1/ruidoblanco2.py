import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

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

# Calcular la densidad espectral de potencia (PSD)
frequencies_clean, psd_clean = welch(clean_signal, fs, nperseg=256)
frequencies_noisy, psd_noisy = welch(noisy_signal, fs, nperseg=256)

# Graficar las señales y la PSD
plt.figure(figsize=(12, 10))

# Señal limpia
plt.subplot(4, 1, 1)
plt.plot(t, clean_signal, label="Señal limpia")
plt.title("Señal limpia")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.legend()

# Interferencia
plt.subplot(4, 1, 2)
plt.plot(t, interference, label="Interferencia", color="orange")
plt.title("Interferencia (Ruido impulsivo + Ruido de banda ancha)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.legend()
    
# Señal resultante
plt.subplot(4, 1, 3)
plt.plot(t, noisy_signal, label="Señal con interferencia", color="red")
plt.title("Señal resultante")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.legend()

# Densidad espectral de potencia (PSD)
plt.subplot(4, 1, 4)
plt.semilogy(frequencies_clean, psd_clean, label="PSD Señal limpia")
plt.semilogy(frequencies_noisy, psd_noisy, label="PSD Señal con ruido", color="red")
plt.title("Densidad espectral de potencia (PSD)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Densidad espectral de potencia")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()