import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parámetros de la señal DISCRETA
fs = 1000  # Frecuencia de muestreo (Hz)
N = 1000   # Número de muestras
n = np.arange(N)  # Índices discretos (k)
f1 = 50    # Frecuencia componente 1 (Hz)
f2 = 120   # Frecuencia componente 2 (Hz)

# Señal discreta: 2 sinusoides + ruido
x_discreta = 0.7 * np.sin(2 * np.pi * f1 * n / fs) + 0.5 * np.sin(2 * np.pi * f2 * n / fs) + 0.1 * np.random.randn(N)

# 1. Gráfica de la señal discreta
plt.figure(figsize=(12, 8))
plt.subplot(2, 1, 1)
plt.stem(n[:100], x_discreta[:100], 'b', markerfmt='bo', basefmt=" ", linefmt='b-', label='Señal discreta')  # Solo mostramos las primeras 100 muestras
plt.title('Señal Discreta de Entrada: Dos sinusoides + Ruido')
plt.xlabel('Muestras (k)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

# 2. Cálculo de la PSD para señales discretas (usando welch)
frequencies, psd = signal.welch(x_discreta, fs, nperseg=256, scaling='density')

# 3. Gráfica de la PSD
plt.subplot(2, 1, 2)
plt.semilogy(frequencies, psd, 'r-', linewidth=2)
plt.title('Densidad Espectral de Potencia (PSD) - Señal Discreta')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('PSD [V²/Hz] (log)')
plt.grid(True, which="both", ls="--")

# Marcamos las frecuencias teóricas
plt.axvline(x=f1, color='g', linestyle='--', label=f'{f1} Hz')
plt.axvline(x=f2, color='m', linestyle='--', label=f'{f2} Hz')
plt.legend()

plt.tight_layout()
plt.show()