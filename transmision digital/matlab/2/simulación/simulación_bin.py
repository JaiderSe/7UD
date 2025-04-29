import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox




# Rango de tiempo
t = np.arange(0, 10.01, 0.01)

# Función escalón unitario
def u(t):
    return np.where(t >= 0, 1, 0)

# Funciones disponibles
def funcion1(t):
    return (2 + np.sin(2 * np.pi * t)) * (u(t) - u(t - 1)) + (-4 * t + 6) * (u(t - 1) - u(t - 2)) + (-2 + np.sin(2 * np.pi * t)) * (u(t - 2) - u(t - 3))

def funcion2(t):
    return (2/3 * t) * (u(t) - u(t - 3)) \
         + (3) * (u(t - 3) - u(t - 6)) \
         + (-(3/4) * t + 11/2) * (u(t - 6) - u(t - 10))

def funcion3(t):
    return 0.5 * (-np.cos(0.5 * np.pi * t) + 1) * (u(t) - u(t - 4)) \
         + 0.5 * (np.cos(0.5 * np.pi * t) - 1) * (u(t - 4) - u(t - 8))

# Configuración inicial
y = funcion1(t)
binaria = [1, 0, 1, 1, 0, 0, 1, 0]

# Función para graficar la función periódica
def actualizar_periodica(y, text):
    try:
        binaria = [int(bit) for bit in text]
        t_periodica = []
        y_periodica = []
        for i, bit in enumerate(binaria):
            if bit == 1:
                t_periodica.extend(t + i * t[-1])
                y_periodica.extend(y)
            else:
                t_periodica.extend(t + i * t[-1])
                y_periodica.extend(np.zeros_like(y))
        
        ax_periodica.clear()
        ax_periodica.plot(t_periodica, y_periodica, color='cyan', label="Función Periódica")
        ax_periodica.set_title("Funciones Periódicas")
        ax_periodica.set_xlabel("Tiempo (t)")
        ax_periodica.set_ylabel("Amplitud")
        ax_periodica.grid(color='green', linestyle='--', linewidth=1)
        ax_periodica.legend(facecolor='black', edgecolor='green', labelcolor='green')
        
        plt.draw()
        
    except ValueError:
        print("Error: Ingrese una cadena de valores binarios (0 y 1).")

# Función para actualizar la señal binaria desde el TextBox
def actualizar_binaria(text):
    try:
        binaria = [int(bit) for bit in text]
        graficar_binaria(binaria)
    except ValueError:
        print("Error: Ingrese una cadena de valores binarios (0 y 1).")

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
    actualizar_espectral()
 
    plt.draw()

# Función para actualizar el análisis espectral
def actualizar_espectral():
    global espectro
    espectro = np.abs(np.fft.fft(y))
    linea_espectral.set_ydata(espectro)
    plt.draw()

# Función para graficar una señal binaria
def graficar_binaria(binaria):
    t_bin = np.arange(0, len(binaria), 1)
    ax_binaria.clear()
    ax_binaria.step(t_bin, binaria, where='post', color='cyan', label="Señal Binaria")
    ax_binaria.set_title("Señal Binaria")
    ax_binaria.set_xlabel("Tiempo (t)")
    ax_binaria.set_ylabel("Amplitud")
    ax_binaria.grid(color='green', linestyle='--', linewidth=1)
    ax_binaria.legend(facecolor='black', edgecolor='green', labelcolor='green')
    plt.draw()

# Función para graficar la función periódica    
def graficar_periodica(binaria):
    
    t_bin = np.arange(0, len(binaria), 1)
    ax_periodica.clear()
    ax_periodica.step(t_bin, binaria, where='post', color='cyan', label="Señal Binaria")
    ax_periodica.set_title("Señal Binaria")
    ax_periodica.set_xlabel("Tiempo (t)")
    ax_periodica.set_ylabel("Amplitud")
    ax_periodica.grid(color='green', linestyle='--', linewidth=1)
    ax_periodica.legend(facecolor='black', edgecolor='green', labelcolor='green')
    plt.draw()

# Función para graficar el análisis espectral
def graficar_espectral(ax, t, y):
    frecuencia = np.fft.fftfreq(len(t), d=(t[1] - t[0]))
    espectro = np.abs(np.fft.fft(y))
    linea_espectral, = ax.plot(frecuencia, espectro, color='cyan', label="Espectro de Potencia")
    ax.set_title("Análisis Espectral de Potencia")
    ax.set_xlabel("Frecuencia (Hz)")
    ax.set_ylabel("Amplitud")
    ax.grid(color='green', linestyle='--', linewidth=0.5)
    ax.legend(facecolor='black', edgecolor='green', labelcolor='green')
    return linea_espectral


    






# Crear la figura y los subplots
fig, ((ax_funcion, ax_espectral), (ax_binaria, ax_periodica)) = plt.subplots(2, 2, facecolor='black', figsize=(10, 8))
fig.subplots_adjust(hspace=0.5)

# Configuración del eje para la señal binaria
ax_binaria.set_facecolor('black')
for spine in ax_binaria.spines.values():
    spine.set_color('green')
ax_binaria.tick_params(axis='x', colors='green')
ax_binaria.tick_params(axis='y', colors='green')
ax_binaria.yaxis.label.set_color('green')
ax_binaria.xaxis.label.set_color('green')
ax_binaria.title.set_color('green')
# Graficar la señal binaria inicial
graficar_binaria(binaria)


# Configuración del eje para la función periódica
ax_periodica.set_facecolor('black')
for spine in ax_periodica.spines.values():
    spine.set_color('green')
ax_periodica.tick_params(axis='x', colors='green')
ax_periodica.tick_params(axis='y', colors='green')
ax_periodica.yaxis.label.set_color('green')
ax_periodica.xaxis.label.set_color('green')
ax_periodica.title.set_color('green')
ax_periodica.set_title("Funciones Periódicas")
ax_periodica.set_xlabel("Tiempo (t)")
ax_periodica.set_ylabel("Amplitud")
#graficar la función periódica
graficar_periodica(binaria)


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
for spine in ax_espectral.spines.values():
    spine.set_color('green')
ax_espectral.tick_params(axis='x', colors='green')
ax_espectral.tick_params(axis='y', colors='green')
ax_espectral.yaxis.label.set_color('green')
ax_espectral.xaxis.label.set_color('green')
ax_espectral.title.set_color('green')
# Llamar a la función para graficar el análisis espectral
linea_espectral = graficar_espectral(ax_espectral, t, y)




# Crear un TextBox para ingresar la señal binaria
ax_textbox = plt.axes([0.1, 0.93, 0.4, 0.05])
textbox = TextBox(ax_textbox, 'Señal Binaria:', initial="10110010", color='green', hovercolor='lime')
textbox.on_submit(lambda text: (actualizar_binaria(text), actualizar_periodica(y, text)))


# Crear botones
ax_boton1 = plt.axes([0.59, 0.93, 0.1, 0.05])
ax_boton2 = plt.axes([0.7, 0.93, 0.1, 0.05])
ax_boton3 = plt.axes([0.81, 0.93, 0.1, 0.05])

boton1 = Button(ax_boton1, 'Onda 1', color='green', hovercolor='lime')
boton2 = Button(ax_boton2, 'Onda 2', color='green', hovercolor='lime')
boton3 = Button(ax_boton3, 'Onda 3', color='green', hovercolor='lime')

# Conectar los botones a la función de actualización
boton1.on_clicked(actualizar_grafica)
boton2.on_clicked(actualizar_grafica)
boton3.on_clicked(actualizar_grafica)

plt.show()
