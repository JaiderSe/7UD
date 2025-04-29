import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parámetros de la señal
fs = 1000  # Frecuencia de muestreo (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # 1 segundo de señal
f1 = 50  # Frecuencia de la señal principal (Hz)
f2 = 120  # Frecuencia adicional (Hz)

# Señal de entrada: 2 senoides + ruido
x = 0.7 * np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t) + 0.1 * np.random.randn(len(t))

# 1. Gráfica de la señal temporal
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.plot(t, x, color='blue', alpha=0.6)
plt.title('Señal de Entrada: Dos sinusoides + Ruido')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)

# 2. Cálculo de la Densidad Espectral de Potencia (PSD)
# Usando la función welch de scipy (método basado en FFT)
frequencies, psd = signal.welch(x, fs, nperseg=1024, scaling='density')

# 3. Gráfica de la PSD
plt.subplot(2, 1, 2)
plt.semilogy(frequencies, psd, color='red', linewidth=2)  # Escala logarítmica en Y
plt.title('Densidad Espectral de Potencia (PSD)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PSD [V²/Hz] (log)')
plt.grid(True, which="both", ls="--")

# Marcamos las frecuencias teóricas
plt.axvline(x=f1, color='green', linestyle='--', label=f'Frecuencia {f1} Hz')
plt.axvline(x=f2, color='purple', linestyle='--', label=f'Frecuencia {f2} Hz')
plt.legend()

plt.tight_layout()
plt.show()