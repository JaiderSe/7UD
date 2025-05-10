import numpy as np
from scipy.signal import welch

import matplotlib.pyplot as plt

# Parámetros de la señal
fs = 10000  # Frecuencia de muestreo
t = np.linspace(0, 1, fs, endpoint=False)  # Vector de tiempo
fc = 1000  # Frecuencia de la portadora
fm = 50  # Frecuencia de la señal moduladora
Am = 1  # Amplitud de la señal moduladora
Ac = 1  # Amplitud de la portadora
SNR = 10  # Relación señal a ruido en dB

# Señal moduladora
m_t = Am * np.sin(2 * np.pi * fm * t)

# Señal modulada en AM
s_t = Ac * (1 + m_t) * np.cos(2 * np.pi * fc * t)

# Añadir ruido blanco
potencia_senal = np.mean(s_t**2)
potencia_ruido = potencia_senal / (10**(SNR / 10))
ruido = np.sqrt(potencia_ruido) * np.random.normal(size=len(t))
s_t_ruido = s_t + ruido

# Densidad espectral de potencia de la señal sin ruido
f, Pxx = welch(s_t, fs, nperseg=1024)

# Graficar
plt.figure(figsize=(12, 8))

# Señal original y modulada con ruido
plt.subplot(3, 1, 1)
plt.plot(t, m_t, label="Señal Original (Moduladora)")
plt.plot(t, s_t_ruido, label="Señal Modulada con Ruido", alpha=0.7)
plt.title("Señal Original y Señal Modulada con Ruido")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()

# Densidad espectral de potencia
plt.subplot(3, 1, 2)
plt.semilogy(f, Pxx)
plt.title("Densidad Espectral de Potencia de la Señal Sin Ruido")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Densidad Espectral de Potencia")
plt.grid()

# Señal modulada sin ruido
plt.subplot(3, 1, 3)
plt.plot(t, s_t, label="Señal Modulada Sin Ruido")
plt.title("Señal Modulada Sin Ruido")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()