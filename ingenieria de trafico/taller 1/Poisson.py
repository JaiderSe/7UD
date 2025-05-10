import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo
lambda_rate = 5     # tasa promedio de llegada (paquetes por segundo)
T = 10              # duración de la simulación (segundos)
np.random.seed(0)   # para resultados reproducibles

# Generar tiempos entre llegadas (exponencial)
inter_arrival_times = np.random.exponential(1/lambda_rate, int(2 * lambda_rate * T))
arrival_times = np.cumsum(inter_arrival_times)

# Filtrar llegadas dentro del intervalo [0, T]
arrival_times = arrival_times[arrival_times <= T]
num_packets = len(arrival_times)

# Graficar las llegadas
plt.figure(figsize=(10, 4))
plt.eventplot(arrival_times, orientation='horizontal', colors='blue')
plt.title(f"Simulación de llegadas de paquetes (Modelo de Poisson, λ = {lambda_rate})")
plt.xlabel("Tiempo (s)")
plt.yticks([])
plt.grid(True)
plt.show()

print(f"Total de paquetes llegados en {T} segundos: {num_packets}")
