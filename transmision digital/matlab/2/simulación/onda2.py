import numpy as np
import matplotlib.pyplot as plt

# Definir la función escalón unitario
def u(t):
    return np.where(t >= 0, 1, 0)

# Rango de tiempo
t = np.arange(-2, 10.01, 0.01)

# Definir la función por partes
y = (2/3*t)*(u(t)-u(t-3))+(3)*(u(t-3)-u(t-6))+(-(3/4)*t+11/2)*(u(t-6)-u(t-10))

# Graficar
plt.plot(t, y, 'r', linewidth=2)
plt.axis([-1, 11, -5, 8])
plt.grid(True)
plt.xlabel('Tiempo (t)')
plt.ylabel('y(t)')
plt.title('Gráfica de la función definida por partes')
plt.show()
