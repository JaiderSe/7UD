import numpy as np
import matplotlib.pyplot as plt

# Configuración
fs = 1000  # Frecuencia de muestreo (Hz)
t = np.linspace(0, 4, int(fs * 4), endpoint=False)  # 4 segundos

# --- 1. Crear señal con fase enrollada (modulación de frecuencia) ---
f_portadora = 2  # Frecuencia de la portadora (Hz)
f_moduladora = 0.37  # Frecuencia de modulación (Hz) -> 0.37 ciclos/segundo (de tu imagen)
indice_mod = 5  # Índice de modulación (controla la desviación de fase)

# Señal modulada en fase (PM) o frecuencia (FM)
phase_enrollada = 2 * np.pi * f_portadora * t + indice_mod * np.sin(2 * np.pi * f_moduladora * t)
senal_enrollada = np.cos(phase_enrollada)  # Señal final

# --- 2. Gráfica de la señal en el tiempo ---
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, senal_enrollada, 'b-', linewidth=1, label='Señal enrollada (PM)')
plt.title('Señal con Fase Modulada (0.37 ciclos/segundo)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

# --- 3. Fase instantánea (en radianes y ciclos) ---
phase_instantanea = phase_enrollada % (2 * np.pi)  # Fase entre 0 y 2π
ciclos_por_segundo = phase_instantanea / (2 * np.pi)  # Convertir a ciclos

plt.subplot(3, 1, 2)
plt.plot(t, phase_instantanea, 'g-', label='Fase instantánea (rad)')
plt.title('Fase Instantánea (Módulo 2π)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Fase (rad)')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, ciclos_por_segundo, 'r-', label='Ciclos por segundo')
plt.title('Ciclos por Segundo (Fase / 2π)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ciclos')
plt.ylim(0, 1)  # Normalizado a [0, 1] ciclo
plt.grid(True)

plt.tight_layout()
plt.show()

# --- 4. Espectro de Frecuencia (FFT) ---
freqs = np.fft.fftfreq(len(t), 1/fs)[:len(t)//2]
fft_val = np.abs(np.fft.fft(senal_enrollada)[:len(t)//2])

plt.figure(figsize=(10, 4))
plt.stem(freqs, fft_val, 'm-', markerfmt='mo', basefmt=" ")
plt.title('Espectro de Frecuencia de la Señal Enrollada')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.xlim(0, 10)  # Rango de 0 a 10 Hz
plt.grid(True)
plt.show()