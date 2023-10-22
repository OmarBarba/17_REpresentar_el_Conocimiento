import numpy as np

# Probabilidad de obtener un 6 en un dado de 6 caras
probabilidad_dado = 1 / 6

# Realizar un experimento de lanzamiento de dado
resultado_lanzamiento = np.random.choice([1, 2, 3, 4, 5, 6], p=[probabilidad_dado] * 6)

print(f"Resultado del lanzamiento de dado: {resultado_lanzamiento}")
