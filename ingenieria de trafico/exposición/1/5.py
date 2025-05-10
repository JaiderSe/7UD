import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal discreta
frecuencia = 10  # Hz (frecuencia de la señal digital)
amplitud = 5      # Voltios (nivel alto)
muestras_por_periodo = 20  # Resolución de la señal
duty_cycle = 0.3  # Ciclo de trabajo (30% en estado alto)

# Tiempo discreto (2 periodos)
n_periodos = 2
tiempo = np.linspace(0, n_periodos / frecuencia, n_periodos * muestras_por_periodo, endpoint=False)

# Generar señal PWM discreta
senal = np.where((tiempo * frecuencia) % 1 < duty_cycle, amplitud, 0)

# Calcular potencia instantánea (asumimos R = 1 Ohm para simplificar)
R = 1
potencia_instantanea = (senal ** 2) / R

# Potencia media (promedio en los periodos mostrados)
potencia_media = np.mean(potencia_instantanea)

# Gráfica
plt.figure(figsize=(12, 6))

# Señal discreta y potencia
plt.subplot(2, 1, 1)
plt.step(tiempo, senal, where='post', color='blue', label='Señal digital (V)')
plt.title('Señal Discreta (PWM) y Potencia Instantánea', fontweight='bold')
plt.ylabel('Voltaje (V)')
plt.yticks([0, amplitud], ['0V', f'{amplitud}V'])
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

# Potencia instantánea y media
plt.subplot(2, 1, 2)
plt.step(tiempo, potencia_instantanea, where='post', color='red', label='Potencia instantánea (W)')
plt.axhline(y=potencia_media, color='green', linestyle='--', 
            label=f'Potencia media = {potencia_media:.2f} W')
plt.title('Potencia de Señal Discreta', fontweight='bold')
plt.xlabel('Tiempo (s)')
plt.ylabel('Potencia (W)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()

# Resultados
print(f"Potencia media teórica (duty_cycle={duty_cycle}): {duty_cycle * amplitud**2 / R:.2f} W")
print(f"Potencia media calculada: {potencia_media:.2f} W")