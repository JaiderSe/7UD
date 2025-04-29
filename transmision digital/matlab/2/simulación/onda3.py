import numpy as np
import matplotlib.pyplot as plt

# Definir la función escalón unitario
def u(t):
    return np.where(t >= 0, 1, 0)

# Rango de tiempo
t = np.arange(-2, 10.01, 0.01)

# Definir la función por partes
y = 0.5*(-np.cos(0.5*np.pi*t)+1)*(u(t)-u(t-4))+0.5*(np.cos(0.5*np.pi*t)-1)*(u(t-4)-u(t-8))

# Graficar
plt.plot(t, y, 'r', linewidth=2)
plt.axis([-1, 8, -3, 3])
plt.grid(True)
plt.xlabel('Tiempo (t)')
plt.ylabel('y(t)')
plt.title('Gráfica de la función definida por partes')
plt.show()
