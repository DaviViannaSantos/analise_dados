import pandas as pd

# Caminho do arquivo na mesma pasta
path = "Tabela 1.1.1.xls"

indicador_1 = pd.read_excel(path, engine="xlrd", skiprows=7)

indicador_1.columns = [
    "uf_regiao",
    "total",
    "total_branca",
    "total_preta_parda",
    "homem_branca",
    "homem_preta_parda",
    "mulher_branca",
    "mulher_preta_parda"
]

indicador_1 = indicador_1.dropna(subset=["total"]).reset_index(drop=True)

# Como é um Jupyter Notebook (.ipynb), o display() funciona perfeitamente aqui:
print(indicador_1.head())