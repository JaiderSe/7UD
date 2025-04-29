import numpy as np
import matplotlib.pyplot as plt

# Configuración
fs = 500  # Frecuencia de muestreo (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # 1 segundo de señal
f1, f2 = 30, 70  # Frecuencias (Hz)

# Señal compuesta
x = 0.5 * np.sin(2 * np.pi * f1 * t) + 0.3 * np.cos(2 * np.pi * f2 * t)

# DFT
X = np.fft.fft(x)
N = len(X)
frequencies = np.fft.fftfreq(N, 1/fs)

# Parte Real e Imaginaria
Re = np.real(X)
Im = np.imag(X)

# Gráficas
plt.figure(figsize=(15, 5))

# Parte Real
plt.subplot(1, 3, 1)
plt.stem(frequencies[:N//2], Re[:N//2], 'b', markerfmt='bo', label='Re')
plt.title('Parte Real (Coeficientes coseno)')
plt.xlabel('Frecuencia (Hz)')
plt.grid()

# Parte Imaginaria
plt.subplot(1, 3, 2)
plt.stem(frequencies[:N//2], Im[:N//2], 'r', markerfmt='ro', label='Im')
plt.title('Parte Imaginaria (Coeficientes seno)')
plt.xlabel('Frecuencia (Hz)')
plt.grid()

# Magnitud
plt.subplot(1, 3, 3)
magnitud = np.abs(X)[:N//2]
plt.stem(frequencies[:N//2], magnitud, 'g', markerfmt='go', label='|X(f)|')
plt.title('Magnitud (Espectro de Potencia)')
plt.xlabel('Frecuencia (Hz)')
plt.grid()

plt.tight_layout()
plt.show()