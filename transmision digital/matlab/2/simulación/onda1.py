import numpy as np
import matplotlib.pyplot as plt

# Definir la función escalón unitario
def u(t):
    return np.where(t >= 0, 1, 0)

# Rango de tiempo
t = np.arange(-2, 10.01, 0.01)

# Definir la función por partes
y = (2 + np.sin(2 * np.pi * t)) * (u(t) - u(t - 1)) \
  + (-4 * t + 6) * (u(t - 1) - u(t - 2)) \
  + (-2 + np.sin(2 * np.pi * t)) * (u(t - 2) - u(t - 3))

# Graficar
plt.plot(t, y, 'r', linewidth=2)
plt.axis([-1, 8, -5, 5])
plt.grid(True)
plt.xlabel('Tiempo (t)')
plt.ylabel('y(t)')
plt.title('Gráfica de la función definida por partes')
plt.show()
