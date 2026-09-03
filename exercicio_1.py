import numpy as np
import pandas as pd

idades = np.array([18, 21, 19, 22, 20])
print("Vetor de idades:", idades)

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Shape da matriz:", matriz.shape)
print("Elemento [1, 2]:", matriz[1, 2])

series_idades = pd.Series(
    idades, 
    index=["Ana", "Bruno", "Carla", "Diego", "Eva"], 
    name="idades"
)
print("\nSeries de idades:\n", series_idades)

print("\nIdade da Carla (loc):", series_idades.loc["Carla"])

print("\nPessoas com 21 anos ou mais:\n", series_idades[series_idades >= 21])
