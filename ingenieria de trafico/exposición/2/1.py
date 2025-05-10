import numpy as np
import matplotlib.pyplot as plt

# Parámetros
T = 1.0  # Tiempo total
N = 1000  # Número de pasos de tiempo
dt = T / N  # Incremento de tiempo
num_trayectorias = 5  # Número de trayectorias a simular

# Simulación de Movimiento Browniano
t = np.linspace(0, T, N)  # Tiempos
trayectorias = np.zeros((num_trayectorias, N))  # Matriz para almacenar las trayectorias

for i in range(num_trayectorias):
    dB = np.sqrt(dt) * np.random.randn(N)  # Incrementos normales
    trayectorias[i, :] = np.cumsum(dB)  # Sumar los incrementos para obtener la trayectoria

# Graficar las trayectorias
plt.figure(figsize=(8, 5))
for i in range(num_trayectorias):
    plt.plot(t, trayectorias[i, :], label=f'Trayectoria {i+1}')

plt.xlabel("Tiempo t")
plt.ylabel("X_t (Valor del proceso)")
plt.title("Ejemplo de Trayectorias de un Movimiento Browniano")
plt.legend()
plt.grid()
plt.show()
 