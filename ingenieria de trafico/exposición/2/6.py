import numpy as np
import matplotlib.pyplot as plt

# Señal periódica: coseno
t = np.linspace(0, 2*np.pi, 100)
signal = np.cos(5*t)

# Autocorrelación con numpy
autocorr = np.correlate(signal, signal, mode='full')
lags = np.arange(-len(signal)+1, len(signal))

plt.plot(lags, autocorr)
plt.title("Autocorrelación de la señal")
plt.xlabel("Retardo")
plt.ylabel("Valor de la autocorrelación")
plt.grid()
plt.show()
