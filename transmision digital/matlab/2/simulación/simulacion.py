import numpy as np
from matplotlib.widgets import Button
import matplotlib.pyplot as plt

def escalon_unitario(t):
    """Función escalón unitario."""
    return np.where(t >= 0, 1, 0)
def u(t):
    return np.where(t >= 0, 1, 0)

# Rango de tiempo
t = np.arange(-2, 10.01, 0.01)


# Evaluar la función escalón unitario
y = (2 + np.sin(2 * np.pi * t)) * (u(t) - u(t - 1)) \
  + (-4 * t + 6) * (u(t - 1) - u(t - 2)) \
  + (-2 + np.sin(2 * np.pi * t)) * (u(t - 2) - u(t - 3))



# Funciones disponibles
def funcion1(t):
    return (2 + np.sin(2 * np.pi * t)) * (u(t) - u(t - 1)) \
  + (-4 * t + 6) * (u(t - 1) - u(t - 2)) \
  + (-2 + np.sin(2 * np.pi * t)) * (u(t - 2) - u(t - 3))

def funcion2(t):
    return (2/3*t)*(u(t)-u(t-3))+(3)*(u(t-3)-u(t-6))+(-(3/4)*t+11/2)*(u(t-6)-u(t-10))

def funcion3(t):
    return 0.5*(-np.cos(0.5*np.pi*t)+1)*(u(t)-u(t-4))+0.5*(np.cos(0.5*np.pi*t)-1)*(u(t-4)-u(t-8))

# Función para actualizar la gráfica
def actualizar_grafica(event):
    global y
    if event.inaxes == ax_boton1:
        y = funcion1(t)
    elif event.inaxes == ax_boton2:
        y = funcion2(t)
    elif event.inaxes == ax_boton3:
        y = funcion3(t)
    linea.set_ydata(y)
    plt.draw()

# Graficar la función inicial
y = funcion1(t)

# Crear un diseño con subplots en la misma ventana
fig, (ax_funcion, ax_espectral) = plt.subplots(2, 1, facecolor='black', figsize=(8, 6))
fig.subplots_adjust(hspace=0.5)

# Configuración del eje para la función
ax_funcion.set_facecolor('black')
ax_funcion.spines['top'].set_color('green')
ax_funcion.spines['bottom'].set_color('green')
ax_funcion.spines['left'].set_color('green')
ax_funcion.spines['right'].set_color('green')
ax_funcion.tick_params(axis='x', colors='green')
ax_funcion.tick_params(axis='y', colors='green')
ax_funcion.yaxis.label.set_color('green')
ax_funcion.xaxis.label.set_color('green')
ax_funcion.title.set_color('green')

# Graficar la función inicial
linea, = ax_funcion.plot(t, y, color='cyan', label="Función de onda")
ax_funcion.set_title("Funciones con Botones")
ax_funcion.set_xlabel("Tiempo (t)")
ax_funcion.set_ylabel("Amplitud")
ax_funcion.grid(color='green', linestyle='--', linewidth=0.5)
ax_funcion.legend(facecolor='black', edgecolor='green', labelcolor='green')

# Configuración del eje para el análisis espectral
ax_espectral.set_facecolor('black')
ax_espectral.spines['top'].set_color('green')
ax_espectral.spines['bottom'].set_color('green')
ax_espectral.spines['left'].set_color('green')
ax_espectral.spines['right'].set_color('green')
ax_espectral.tick_params(axis='x', colors='green')
ax_espectral.tick_params(axis='y', colors='green')
ax_espectral.yaxis.label.set_color('green')
ax_espectral.xaxis.label.set_color('green')
ax_espectral.title.set_color('green')

# Calcular y graficar el análisis espectral
frecuencia = np.fft.fftfreq(len(t), d=(t[1] - t[0]))
espectro = np.abs(np.fft.fft(y))

linea_espectral, = ax_espectral.plot(frecuencia, espectro, color='cyan', label="Espectro de Potencia")
ax_espectral.set_title("Análisis Espectral de Potencia")
ax_espectral.set_xlabel("Frecuencia (Hz)")
ax_espectral.set_ylabel("Amplitud")
ax_espectral.grid(color='green', linestyle='--', linewidth=0.5)
ax_espectral.legend(facecolor='black', edgecolor='green', labelcolor='green')

# Actualizar el análisis espectral al cambiar la función
def actualizar_espectral():
    global espectro
    espectro = np.abs(np.fft.fft(y))
    linea_espectral.set_ydata(espectro)
    plt.draw()

# Modificar la función de actualización para incluir el espectro
def actualizar_grafica(event):
    global y
    if event.inaxes == ax_boton1:
        y = funcion1(t)
    elif event.inaxes == ax_boton2:
        y = funcion2(t)
    elif event.inaxes == ax_boton3:
        y = funcion3(t)
    linea.set_ydata(y)
    actualizar_espectral()
    plt.draw()

# Crear botones
ax_boton2 = plt.axes([0.7, 0.05, 0.1, 0.075])
ax_boton3 = plt.axes([0.81, 0.05, 0.1, 0.075])
ax_boton1 = plt.axes([0.59, 0.05, 0.1, 0.075])

boton1 = Button(ax_boton1, 'Onda 1', color='green', hovercolor='lime')
boton2 = Button(ax_boton2, 'Onda 2', color='green', hovercolor='lime')
boton3 = Button(ax_boton3, 'Onda 3', color='green', hovercolor='lime')

# Conectar los botones a la función de actualización
boton1.on_clicked(actualizar_grafica)
boton2.on_clicked(actualizar_grafica)
boton3.on_clicked(actualizar_grafica)



plt.show()