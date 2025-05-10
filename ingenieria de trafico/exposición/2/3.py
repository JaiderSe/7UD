import numpy as np
import matplotlib.pyplot as plt

# Señal discreta: sinusoide + ruido
fs = 1000  # Frecuencia de muestreo (Hz)
t = np.arange(0, 1, 1/fs)
f_signal = 50  # Frecuencia de la señal (Hz)
x = np.sin(2 * np.pi * f_signal * t) + 0.5 * np.random.randn(len(t))

# DFT (usando la exponencial compleja)
N = len(x)
frequencies = np.fft.fftfreq(N, 1/fs)
X = np.fft.fft(x)  # Esto implica sum_{k=0}^{N-1} x[k] e^{-j 2π f k / N}

# PSD (|DFT|^2 normalizada)
PSD = np.abs(X)**2 / (N * fs)

# Gráfica
plt.figure(figsize=(10, 5))
plt.plot(frequencies[:N//2], PSD[:N//2], 'r-')  # Solo frecuencias positivas
plt.title('Densidad Espectral de Potencia (PSD)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Potencia [V²/Hz]')
plt.grid()
plt.show()