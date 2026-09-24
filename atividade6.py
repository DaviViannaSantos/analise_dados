import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Configuração do estilo gráfico
sns.set_theme(style="whitegrid")

# 1. Carregar as duas Tabelas 5
t2012 = pd.read_csv(
    "Tabela5-sem_emprego_2012.csv", sep=";", decimal=",", encoding="utf-8-sig"
)
t2026 = pd.read_csv(
    "Tabela5-sem_emprego_2026.csv", sep=";", decimal=",", encoding="utf-8-sig"
)

# Limpeza e renomeação das colunas de interesse
t2012 = t2012.rename(
    columns={"Desocupados - mulheres (2012 T1)": "mulheres_2012"}
)
t2026 = t2026.rename(
    columns={"Desocupados - mulheres (2026 T1)": "mulheres_2026"}
)

# 2. Juntar tabelas (Merge)
comp = t2012.merge(t2026, on=["Sigla", "Código", "Estado"], how="inner")

# 3. Ordenação dos Estados pelo valor de 2026
ordem = comp.sort_values("mulheres_2026", ascending=False)["Estado"]

# 4. Derreter o DataFrame (Melt)
longo = comp.melt(
    id_vars=["Sigla", "Código", "Estado"],
    value_vars=["mulheres_2012", "mulheres_2026"],
    var_name="Ano",
    value_name="Participacao_mulheres",
)

# Mapear os rótulos de ano
longo["Ano"] = longo["Ano"].map(
    {"mulheres_2012": "2012 T1", "mulheres_2026": "2026 T1"}
)

# 5. Criação do Gráfico
fig, ax = plt.subplots(figsize=(10, 10))

sns.barplot(
    data=longo,
    y="Estado",
    x="Participacao_mulheres",
    hue="Ano",
    order=ordem,
    ax=ax,
    palette="Set2",
)

# Linha de referência em 50%
ax.axvline(50, color="crimson", linestyle="--", linewidth=1.5)

ax.set_xlabel("Participação das mulheres entre as pessoas desocupadas (%)")
ax.set_ylabel("")
ax.set_title(
    "Desocupação: participação feminina em 2012 T1 e 2026 T1",
    fontweight="bold",
)
ax.legend(title="Período")

fig.tight_layout()
plt.show()