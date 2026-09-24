import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")

t2012 = pd.read_csv(
    "Tabela5-sem_emprego_2012.csv", sep=";", decimal=",", encoding="utf-8-sig"
)
t2026 = pd.read_csv(
    "Tabela5-sem_emprego_2026.csv", sep=";", decimal=",", encoding="utf-8-sig"
)

t2012 = t2012.rename(
    columns={"Desocupados - mulheres (2012 T1)": "mulheres_2012"}
)
t2026 = t2026.rename(
    columns={"Desocupados - mulheres (2026 T1)": "mulheres_2026"}
)

comp = t2012.merge(t2026, on=["Sigla", "Código", "Estado"], how="inner")

ordem = comp.sort_values("mulheres_2026", ascending=False)["Estado"]

longo = comp.melt(
    id_vars=["Sigla", "Código", "Estado"],
    value_vars=["mulheres_2012", "mulheres_2026"],
    var_name="Ano",
    value_name="Participacao_mulheres",
)

longo["Ano"] = longo["Ano"].map(
    {"mulheres_2012": "2012 T1", "mulheres_2026": "2026 T1"}
)

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
