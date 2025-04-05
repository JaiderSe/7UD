import numpy as np

# Definir la matriz de transición
P = np.array([[0.7, 0.2, 0.1],
              [0.3, 0.4, 0.3],
              [0.2, 0.3, 0.5]])

# Resolver el sistema πP = π con la restricción de que las probabilidades suman 1
n = P.shape[0]
A = np.vstack([P.T - np.eye(n), np.ones(n)])
b = np.append(np.zeros(n), 1)

# Resolver el sistema de ecuaciones
pi = np.linalg.lstsq(A, b, rcond=None)[0]
print(pi)
