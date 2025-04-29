import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd
import matplotlib.pyplot as plt

# 1. Parámetros de la señal
fs = 44100  # frecuencia de muestreo (Hz)
duracion = 1.0  # duración total en segundos
tiempo_escalon = 0.2  # en qué momento ocurre el escalón

# 2. Crear la señal tipo escalón
t = np.linspace(0, duracion, int(fs*duracion), endpoint=False)
senal = np.zeros_like(t)
senal[t >= tiempo_escalon] = 0.8  # amplitud del escalón (máx ±1 para WAV)

# 3. Guardar como archivo WAV
senal_int16 = np.int16(senal * 32767)  # convertir a formato 16 bits
wav.write("escalon.wav", fs, senal_int16)

# 4. (Opcional) Reproducir el sonido
print("Reproduciendo el escalón...")
sd.play(senal, fs)
sd.wait()

# 5. Ver la forma de onda
plt.plot(t, senal)
plt.title("Señal tipo escalón")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid()
plt.show()
