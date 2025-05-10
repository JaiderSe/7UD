import numpy as np
import matplotlib.pyplot as plt

# Parámetros
fs = 1000            # Frecuencia de muestreo (Hz)
T = 1                # Duración de la señal (segundos)
f_c = 10             # Frecuencia de la portadora (Hz)
N = fs * T           # Número de muestras
t = np.linspace(0, T, N)

# Señal transmitida (portadora senoidal)
tx_signal = np.sin(2 * np.pi * f_c * t)

# Canal de desvanecimiento Rayleigh
# Rayleigh se genera como la magnitud de dos variables gaussianas (I y Q)
I = np.random.normal(0, 1, N)
Q = np.random.normal(0, 1, N)
rayleigh_fading = np.sqrt(I**2 + Q**2)

# Señal recibida (afectada por el canal)
rx_signal = rayleigh_fading * tx_signal

# Gráficas
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, tx_signal)
plt.title("Señal Transmitida (Portadora)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")

plt.subplot(3, 1, 2)
plt.plot(t, rayleigh_fading)
plt.title("Desvanecimiento Rayleigh (Canal)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Ganancia")

plt.subplot(3, 1, 3)
plt.plot(t, rx_signal)
plt.title("Señal Recibida (Afectada por Rayleigh)")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")

plt.tight_layout()
plt.show()
