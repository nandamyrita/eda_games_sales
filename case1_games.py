import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import sys

# Configurações iniciais
sns.set(style="whitegrid", palette="pastel")
plt.rcParams["figure.figsize"] = (10, 6)

# Criar diretório de saída 
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

# Carregar dados
csv_path = Path("data/vgsales.csv")

# Função para carregar, limpar dados e renomear colunas
def load_and_clean_data(csv_path):

    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Erro: O arquivo {csv_path} não foi encontrado.", file=sys.stderr)
        return None

    df.rename(columns={
    "Nome" : "Name",
    "Plataforma" : "Platform",
    "Ano" : "Year",
    "Gênero" : "Genre",
    "Publisher" : "Publisher",
    "Vendas Globais (milhões)" : "Global_Sales"
    }, inplace=True)

    inicial_row = len(df)
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
    df.dropna(subset=["Year"], inplace=True)
    df["Year"] = df["Year"].astype(int)
    df.dropna(inplace=True)
    final_row = len(df)

    print(f"Linhas iniciais: {inicial_row}, Linhas após limpeza: {final_row}")
    

    return df

# Adicionar coluna de década
def add_decade_column(df):
    def decade_label(year):
        if 1990 <= year <= 1999:
            return "1990s"
        elif 2000 <= year <= 2009:
            return "2000s"
        elif 2010 <= year <= 2016:
            return "2010s"
        else:
            return "Outros"
    
    df["Decade"] = df["Year"].apply(decade_label)
    return df


# Saber genero e plataforma mais populares
def top_genre_platform(df):
   
    genre_sales = df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)
    top_genre = genre_sales.index[0]
    top_genre_sales = genre_sales.iloc[0] 


    platform_counts = df["Platform"].value_counts()
    top_platform = platform_counts.index[0]
    top_platform_count = platform_counts.iloc[0]  

    print("\n" + "="*50)
    print("        RELATÓRIO DE ANÁLISE DESCRITIVA")
    print("="*50)
    print(f"| GÊNERO MAIS VENDIDO: {' ': <25} | {top_genre}")
    print(f"| Vendas Totais (Milhões): {' ': <22} | {top_genre_sales:,.2f}")
    print("-" * 50)
    print(f"| PLATAFORMA COM MAIS JOGOS: {' ': <18} | {top_platform}")
    print(f"| Total de Jogos Lançados: {' ': <21} | {top_platform_count:,}")
    print("="*50 + "\n")

    return genre_sales, platform_counts


#mostrar gráfico de barras 
def plot_top_genres(genre_sales):
   
    top5_genres = genre_sales.head(5)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top5_genres.index, y=top5_genres.values, palette="viridis")
    plt.title("Top 5 Gêneros por Vendas Globais", fontsize=16 , fontweight='bold')
    plt.xlabel("Gênero", fontsize=14)
    plt.ylabel("Vendas Globais (milhões)", fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "top5_genres_global_sales.png")
    plt.close()


# gerar gráfico de linha
def plot_games_per_year(df):
    games_per_year = df["Year"].value_counts().sort_index()

    plt.figure(figsize=(12, 6))
    sns.lineplot(x=games_per_year.index, y=games_per_year.values, marker="o", color="darkred")
    plt.title("Número de Jogos Lançados por Ano", fontsize=16 , fontweight='bold')
    plt.xlabel("Ano", fontsize=14)
    plt.ylabel("Número de Jogos", fontsize=14)
    plt.grid(True, alpha=0.6)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "games_per_year.png")
    plt.show()

# Função principal
def main():
    df = load_and_clean_data(csv_path)
    df = add_decade_column(df)
    genre_sales, platform_counts = top_genre_platform(df)
    if genre_sales is not None and platform_counts is not None:
        plot_top_genres(genre_sales)
        plot_games_per_year(df)

    print("Análise concluída. Gráficos salvos na pasta 'outputs'.")

if __name__ == "__main__":
    main()

    
