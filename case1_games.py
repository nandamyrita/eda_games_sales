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
    "Genero" : "Genre",
    "Publisher" : "Publisher",
    "Vendas Globais (milhões)" : "Global_Sales"
}, inplace=True)

df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

df.dropna(subset=["Year"], inplace=True) 
df["Year"] = df["Year"].astype(int)

missing_values = df.isnull().sum()
print("Valores ausentes por coluna:\n", missing_values)

df.dropna(inplace=True)


print(df.head()) 
