import numpy as np
import matplotlib.pyplot as plt

# Parámetros
num_intentos = 50  # Número de paquetes enviados
p_exito = 0.9  # Probabilidad de que el paquete llegue correctamente

# Simulación del Proceso de Bernoulli
paquetes = np.random.choice([0, 1], size=num_intentos, p=[1 - p_exito, p_exito])

# Gráfica del proceso
plt.figure(figsize=(10, 4))
plt.step(range(1, num_intentos + 1), paquetes, where="mid", marker="o", linestyle="--", color="b")

# Configuración de la gráfica
plt.xlabel("Intento de transmisión (t)")
plt.ylabel("Estado del paquete (X_t)")
plt.title("Simulación de un Proceso de Bernoulli (Transmisión de paquetes)")
plt.yticks([0, 1], ["Perdido (0)", "Recibido (1)"])
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Mostrar la gráfica
plt.show()
