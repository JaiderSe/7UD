import numpy as np
import matplotlib.pyplot as plt

# Configuración de la señal continua
tiempo = np.linspace(0, 0.1, 1000)  # 1000 puntos entre 0 y 0.1 segundos
frecuencia = 50  # Hz (frecuencia típica de corriente alterna)
amplitud = 220   # Voltios (como en un enchufe estándar)
senal = amplitud * np.sin(2 * np.pi * frecuencia * tiempo)  # Señal senoidal

# Creación de la gráfica
plt.figure(figsize=(10, 5))
plt.plot(tiempo, senal, color='blue', linewidth=2, label='Voltaje AC (220V, 50Hz)')
plt.title("Señal de Energía Continua\nCorriente Alterna (CA)", fontweight='bold')
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Voltaje (V)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)  # Línea de referencia en 0V
plt.legend()
plt.tight_layout()
plt.show()