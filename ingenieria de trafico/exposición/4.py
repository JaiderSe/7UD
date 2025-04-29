import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
frecuencia = 50  # Hz (frecuencia de la red eléctrica)
amplitud = 220    # Voltios (amplitud de voltaje)
resistencia = 100  # Ohms (carga resistiva)
periodo = 1 / frecuencia  # Periodo de la señal

# Tiempo continuo: 5000 puntos entre 0 y 2 periodos
tiempo = np.linspace(0, 2 * periodo, 5000)

# Señal de voltaje (onda senoidal)
voltaje = amplitud * np.sin(2 * np.pi * frecuencia * tiempo)

# Potencia instantánea: P(t) = V(t)^2 / R
potencia_instantanea = (voltaje ** 2) / resistencia

# Potencia media (integral en un periodo)
# Usamos la fórmula teórica para senoides: Pm = (Amplitud^2) / (2 * R)
potencia_media_teorica = (amplitud ** 2) / (2 * resistencia)

# Simulación numérica de la potencia media (aproximación por suma)
potencia_media_numerica = np.mean(potencia_instantanea)

# Gráficas
plt.figure(figsize=(12, 6))

# 1. Señal de voltaje y potencia instantánea
plt.subplot(2, 1, 1)
plt.plot(tiempo, voltaje, color='blue', label='Voltaje (V)')
plt.plot(tiempo, potencia_instantanea, color='red', label='Potencia instantánea (W)')
plt.axhline(y=potencia_media_teorica, color='green', linestyle='--', 
            label=f'Potencia media = {potencia_media_teorica:.2f} W')
plt.title('Señal Continua: Voltaje y Potencia Instantánea', fontweight='bold')
plt.ylabel('Magnitud')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

# 2. Detalle de la potencia en un periodo
plt.subplot(2, 1, 2)
plt.plot(tiempo, potencia_instantanea, color='red', label='Potencia instantánea')
plt.fill_between(tiempo, potencia_instantanea, alpha=0.2, color='red', 
                 label='Área bajo la curva (Energía)')
plt.axhline(y=potencia_media_teorica, color='green', linestyle='--', 
            label=f'Potencia media = {potencia_media_teorica:.2f} W')
plt.title('Cálculo de Potencia Media en un Periodo', fontweight='bold')
plt.xlabel('Tiempo (s)')
plt.ylabel('Potencia (W)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()

# Resultados numéricos
print(f"Potencia media teórica: {potencia_media_teorica:.2f} W")
print(f"Potencia media numérica (simulación): {potencia_media_numerica:.2f} W")