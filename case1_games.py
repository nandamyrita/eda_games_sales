import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import argparse

sns.set(style="whitegrid", palette="pastel")
plt.rcParams["figure.figsize"] = (10, 6)
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

CSV_PATH = Path("data/vgsales.csv")
df = pd.read_csv(CSV_PATH)

df.rename(columns={
    "Nome" : "Name",
    "Plataforma" : "Plataform",
    "Ano" : "Year",
    "Gênero" : "Genre",
    "Publisher" : "Publisher",
    "Vendas Globais (milhões)" : "Global_Sales"
}, inplace=True)

df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

df.dropna(subset=["Year"], inplace=True) 
df["Year"] = df["Year"].astype(int)

missing_values = df.isnull().sum()
print("Valores ausentes por coluna:\n", missing_values)

df.dropna(inplace=True)

genre_sales = df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)
top_genres = genre_sales.index[0]

plataform_counts = df["Plataform"].value_counts()
top_plataform = plataform_counts.index[0]


def decade_label(year):
 if 1990 <= year <= 1999:
    return "1990s"
 elif 2000 <= year <= 2009:
    return "2000s"
 elif 2010 <= year <= 2016:
    return "2010s"
 else:
    return "Outros"
 

df["Decada"] = df["Year"].apply(decade_label)


top5_genres = genre_sales.head(5)

plt.figure(figsize=(12, 6))
sns.barplot(x=top5_genres.index, y=top5_genres.values, palette="viridis")
plt.title("Top 5 Gêneros por Vendas Globais", fontsize=16 , fontweight='bold')
plt.xlabel("Gênero", fontsize=14)
plt.ylabel("Vendas Globais (milhões)", fontsize=14)
plt.savefig(OUTPUT_DIR / "top5_genres_global_sales.png")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


games_per_year = df["Year"].value_counts().sort_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x=games_per_year.index, y=games_per_year.values, marker="o")
plt.title("Número de Jogos Lançados por Ano", fontsize=16 , fontweight='bold')
plt.xlabel("Ano", fontsize=14)
plt.ylabel("Número de Jogos", fontsize=14)
plt.savefig(OUTPUT_DIR / "games_per_year.png")
plt.grid(True)
plt.tight_layout()
plt.show()


print(df.head()) 