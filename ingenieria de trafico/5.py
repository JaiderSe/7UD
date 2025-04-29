import numpy as np
import matplotlib.pyplot as plt

# Parámetros
fs = 1000  # Frecuencia de muestreo (Hz)
t = np.linspace(0, 1, fs, endpoint=False)  # 1 segundo de señal
f = 5  # Frecuencia de la señal (Hz)

# Señal periódica + ruido
x = np.sin(2 * np.pi * f * t) + 0.5 * np.random.randn(fs)

# Autocorrelación (usando numpy)
autocorr = np.correlate(x, x, mode='full')
lags = np.arange(-len(x) + 1, len(x)) / fs  # Desplazamientos en segundos

# Gráficas
plt.figure(figsize=(12, 6))

# Señal original
plt.subplot(2, 1, 1)
plt.plot(t, x, 'b', label='Señal con ruido')
plt.title('Señal Original: Sinusoide de 5 Hz + Ruido')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid()
plt.legend()

# Autocorrelación
plt.subplot(2, 1, 2)
plt.plot(lags, autocorr, 'r', label='Autocorrelación')
plt.title('Autocorrelación de la Señal')
plt.xlabel('Desplazamiento (τ)')
plt.ylabel('Correlación')
plt.grid()
plt.axvline(x=0, color='k', linestyle='--', label='τ = 0')
plt.axvline(x=1/f, color='g', linestyle='--', label=f'τ = {1/f:.2f} s (Periodo)')
plt.legend()

plt.tight_layout()
plt.show()