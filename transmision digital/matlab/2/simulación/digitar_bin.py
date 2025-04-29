import numpy as np
import matplotlib.pyplot as plt

# Señal en el tiempo
fs = 1000  # Hz (frecuencia de muestreo)
t = np.linspace(0, 1, fs)
x = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t)

# Aplicar FFT
X = np.fft.fft(x)
frequencies = np.fft.fftfreq(len(X), d=1/fs)

# Mostrar magnitudes
plt.plot(frequencies[:fs//2], np.abs(X[:fs//2]))
plt.title("Espectro de frecuencias")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()
plt.show()
