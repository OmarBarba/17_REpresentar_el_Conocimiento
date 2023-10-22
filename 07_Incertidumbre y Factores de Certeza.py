import numpy as np

probabilidad_lluvia = 0.3  # Probabilidad de lluvia
probabilidad_nublado = 0.6  # Probabilidad de cielo nublado

if np.random.rand() < probabilidad_lluvia:
    print("Hay una alta probabilidad de lluvia.")
elif np.random.rand() < probabilidad_nublado:
    print("El cielo está nublado, pero no necesariamente lloverá.")
else:
    print("El cielo está despejado y es poco probable que llueva.")
