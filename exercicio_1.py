import numpy as np
import pandas as pd

# 1. Vetor NumPy com as idades
idades = np.array([18, 21, 19, 22, 20])
print("Vetor de idades:", idades)

# 2. Matriz 2x3 qualquer
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Shape da matriz:", matriz.shape)
print("Elemento [1, 2]:", matriz[1, 2])

# 3. Series com índice nomeado
series_idades = pd.Series(
    idades, 
    index=["Ana", "Bruno", "Carla", "Diego", "Eva"], 
    name="idades"
)
print("\nSeries de idades:\n", series_idades)

# 4. Usando loc para mostrar a idade da Carla
print("\nIdade da Carla (loc):", series_idades.loc["Carla"])

# 5. Filtrando quem tem 21 anos ou mais
print("\nPessoas com 21 anos ou mais:\n", series_idades[series_idades >= 21])