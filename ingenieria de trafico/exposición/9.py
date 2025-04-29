import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import signal

# Configuración general
fs = 1000  # Frecuencia de muestreo (Hz)
tiempo_total = 1.0  # Duración de la señal (s)
t = np.linspace(0, tiempo_total, int(fs * tiempo_total), endpoint=False)

# --- Señal CONTINUA (sinusoidal + ruido) ---
f_continua = 50  # Frecuencia de la señal continua (Hz)
senal_continua = 0.7 * np.sin(2 * np.pi * f_continua * t) + 0.1 * np.random.randn(len(t))

# --- Señal DISCRETA (binaria PWM) ---
f_discreta = 10  # Frecuencia de la señal discreta (Hz)
duty_cycle = 0.3  # Ciclo de trabajo (30% en "alto")
senal_discreta = (signal.square(2 * np.pi * f_discreta * t, duty=duty_cycle) + 1) * 0.5  # Convertir a 0 y 1

# --- Cálculo de la Potencia Instantánea ---
# Continua: P(t) = x(t)^2 / R (asumimos R=1 Ohm)
potencia_continua = senal_continua ** 2

# Discreta: P(t) = x(t)^2 / R (x(t) = 0 o 1)
potencia_discreta = senal_discreta ** 2

# --- Transformada de Fourier para obtener frecuencia ---
# Ventana deslizante para análisis tiempo-frecuencia (STFT)
frecuencias_continua, tiempos_continua, Zxx_continua = signal.stft(senal_continua, fs, nperseg=100)
frecuencias_discreta, tiempos_discreta, Zxx_discreta = signal.stft(senal_discreta, fs, nperseg=100)

# Potencia en frecuencia (|STFT|^2)
psd_continua = np.abs(Zxx_continua) ** 2
psd_discreta = np.abs(Zxx_discreta) ** 2

# --- Gráficos 3D ---
fig = plt.figure(figsize=(16, 8))

# 1. Señal CONTINUA
ax1 = fig.add_subplot(121, projection='3d')
T_cont, F_cont = np.meshgrid(tiempos_continua, frecuencias_continua)
ax1.plot_surface(T_cont, F_cont, 10 * np.log10(psd_continua + 1e-10), cmap='viridis')  # Escala logarítmica (dB)
ax1.set_title('Señal CONTINUA: Potencia vs Frecuencia vs Tiempo', fontweight='bold')
ax1.set_xlabel('Tiempo (s)')
ax1.set_ylabel('Frecuencia (Hz)')
ax1.set_zlabel('Potencia (dB)')
ax1.view_init(30, 45)  # Ángulo de visualización

# 2. Señal DISCRETA
ax2 = fig.add_subplot(122, projection='3d') 
T_disc, F_disc = np.meshgrid(tiempos_discreta, frecuencias_discreta)
ax2.plot_surface(T_disc, F_disc, 10 * np.log10(psd_discreta + 1e-10), cmap='plasma')  # Escala logarítmica (dB)
ax2.set_title('Señal DISCRETA: Potencia vs Frecuencia vs Tiempo', fontweight='bold')
ax2.set_xlabel('Tiempo (s)')
ax2.set_ylabel('Frecuencia (Hz)')
ax2.set_zlabel('Potencia (dB)')
ax2.view_init(30, 45)

plt.tight_layout()
plt.show()