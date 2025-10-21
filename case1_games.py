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


print(df.head()) 