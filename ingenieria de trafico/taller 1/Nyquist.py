import numpy as np
import matplotlib.pyplot as plt

# Parámetros físicos
k = 1.38e-23         # Constante de Boltzmann
T = 290              # Temperatura en Kelvin (~17 °C)
B = 1e6              # Ancho de banda (Hz)

# Parámetros de simulación
fs = 10e6            # Frecuencia de muestreo (Hz)
duration = 1e-3      # Duración de la señal (1 ms)
N = int(fs * duration)
t = np.linspace(0, duration, N)

# Señal transmitida (ej. una portadora)
f_c = 1e6
signal = np.sin(2 * np.pi * f_c * t)

# Potencia del ruido térmico
N_power = k * T * B   # en vatios
noise_std = np.sqrt(N_power)  # Desviación estándar del ruido

# Generar ruido térmico (gaussiano)
thermal_noise = np.random.normal(0, noise_std, N)

# Señal recibida
received = signal + thermal_noise

# Calcular la densidad espectral de potencia (PSD)
frequencies, psd_signal = plt.psd(signal, NFFT=1024, Fs=fs)
_, psd_noise = plt.psd(thermal_noise, NFFT=1024, Fs=fs)

# Gráficas
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(t[:1000], signal[:1000])
plt.title("Señal Original (Portadora)")
plt.ylabel("Amplitud")

plt.subplot(4, 1, 2)
plt.plot(t[:1000], thermal_noise[:1000])
plt.title("Ruido Térmico (Ruido blanco gaussiano)")
plt.ylabel("Amplitud")

plt.subplot(4, 1, 3)
plt.plot(t[:1000], received[:1000])
plt.title("Señal Recibida (con Ruido Térmico)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.subplot(4, 1, 4)
plt.semilogy(frequencies, psd_signal, label="Señal")
plt.semilogy(frequencies, psd_noise, label="Ruido")
plt.title("Densidad Espectral de Potencia (PSD)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("PSD (V²/Hz)")
plt.legend()

plt.tight_layout()
plt.show()

