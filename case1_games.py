import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Tuple
import sys



# Configurações iniciais
sns.set(style="whitegrid", palette="Greens")
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
def get_top_stats(df: pd.DataFrame) -> Tuple[pd.Series, pd.Series]:
    genre_sales = df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)
    platform_counts = df["Platform"].value_counts()
    return genre_sales, platform_counts


#mostrar gráfico de barras 
def plot_top_genres(genre_sales):
   
    top5_genres = genre_sales.head(5)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top5_genres.index, y=top5_genres.values, palette=["#2E7D32", "#43A047", "#66BB6A", "#AED581", "#FFEB3B"])
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
    sns.lineplot(x=games_per_year.index, y=games_per_year.values, marker="o", color="#2E7D32")
    plt.title("Número de Jogos Lançados por Ano", fontsize=16 , fontweight='bold')
    plt.xlabel("Ano", fontsize=14)
    plt.ylabel("Número de Jogos", fontsize=14)
    plt.grid(True, alpha=0.6)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "games_per_year.png")
    plt.close()

# Função principal
def main():
    df = load_and_clean_data(csv_path)
    if df is None:
        print("Execução encerrada devido a erro no carregamento de dados.")
        return

    df = add_decade_column(df)

    print("\n" + "="*70)
    print(" TABELA DE AMOSTRA COM COLUNA 'DECADE' ADICIONADA ")
    print("="*70)
    print(df.head().to_string(index=False))
    print("="*70 + "\n")

    genre_sales, platform_counts = get_top_stats(df)
    
    plot_top_genres(genre_sales)
    plot_games_per_year(df)
    
    top_genre = genre_sales.index[0]
    top_genre_sales = genre_sales.iloc[0]
    top_platform = platform_counts.index[0]
    top_platform_count = platform_counts.iloc[0]

    print("\n" + "="*70)
    print("                 RELATÓRIO DE ANÁLISE DESCRITIVA")
    print("="*70)
    print(f"Gênero de jogo mais vendido: {top_genre}")
    print(f"Vendas globais totais desse gênero: {top_genre_sales:,.2f} milhões de unidades")
    print(f"Plataforma com maior número de lançamentos: {top_platform}")
    print(f"Total de jogos lançados nessa plataforma: {top_platform_count}")
    print("="*70 + "\n")

    print("="*70)
    print("                     CONCLUSÃO")
    print("="*70)
    print(f"Nesta análise, observou-se que o gênero {top_genre} foi o mais vendido globalmente, com um total de {top_genre_sales:,.2f} milhões de unidades, enquanto a plataforma {top_platform} apresentou o maior número de lançamentos ({top_platform_count} jogos). Esses resultados indicam uma forte preferência do mercado por títulos de ação e tiro, além de demonstrar a relevância do PC como principal meio de distribuição de jogos ao longo das últimas décadas.")
    print("="*70 + "\n")

    print("Análise concluída com sucesso. Gráficos salvos na pasta 'outputs'.")

if __name__ == "__main__":
    main()