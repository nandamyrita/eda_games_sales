import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Tuple
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import numpy as np
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
            return "Anos 90"
        elif 2000 <= year <= 2009:
            return "Anos 2000"
        elif 2010 <= year <= 2016:
            return "Anos 2010"
        else:
            return "Outros"
    
    df["Decade"] = df["Year"].apply(decade_label)

    return df

# Saber genero e plataforma mais populares
def get_top_stats(df: pd.DataFrame) -> Tuple[pd.Series, pd.Series]:
    genre_sales = df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)
    platform_counts = df["Platform"].value_counts()
    return genre_sales, platform_counts

#mostrar gráfico de barras dos 5 gêneros mais vendidos globalmente
def plot_top_genres(genre_sales):
    top5_genres = genre_sales.head(5)
    top5_df = top5_genres.reset_index()
    top5_df.columns = ["Genre", "Global_Sales"]

    plt.figure(figsize=(12, 6))
    ax = sns.barplot(
        data=top5_df,
        x="Genre",
        y="Global_Sales",
        palette=["#2E7D32", "#43A047", "#66BB6A", "#AED581", "#FFEB3B"]
    )

    for i, v in enumerate(top5_df["Global_Sales"]):
        ax.text(i, v + 0.5, f"{v:.2f}", ha='center', fontweight='bold')

    plt.title("Top 5 Gêneros Mais Vendidos Globalmente", fontsize=16, fontweight='bold')
    plt.xlabel("Gênero", fontsize=14)
    plt.ylabel("Vendas Globais (milhões)", fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "top5_genres_global_sales.png")
    plt.close()

# Mostrar gráfico de linha de jogos por ano
def plot_games_per_year(df):
    games_per_year = df["Year"].value_counts().sort_index()
    plt.figure(figsize=(14, 7))
    
    ax = sns.lineplot(
        x=games_per_year.index,
        y=games_per_year.values,
        marker="o",
        linewidth=2.5,
        color="#2E7D32"
    )
    
    for x, y in zip(games_per_year.index, games_per_year.values):
        ax.text(x, y + 1, str(y), ha='center', fontsize=10, fontweight='bold')
    
    plt.title("Número de Jogos Lançados por Ano", fontsize=18, fontweight='bold')
    plt.xlabel("Ano", fontsize=14)
    plt.ylabel("Número de Jogos", fontsize=14)
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "games_per_year.png")
    plt.close()

# Machine Learning: K-Means e Regressão Linear
def apply_machine_learning(df):
    X = df[["Global_Sales"]].values
    kmeans = KMeans(n_clusters=3, random_state=42)
    df["Sales_Cluster"] = kmeans.fit_predict(X)

    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x="Global_Sales", hue="Sales_Cluster", bins=30, palette="Set2", multiple="stack")
    plt.title("Clusters de Vendas Globais (Baixas, Médias, Altas)")
    plt.xlabel("Vendas Globais (milhões)")
    plt.ylabel("Número de Jogos")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "sales_clusters.png")
    plt.close()

    games_per_year = df.groupby("Year").size().reset_index(name="Num_Games")
    X = games_per_year["Year"].values.reshape(-1, 1)
    y = games_per_year["Num_Games"].values

    model = LinearRegression()
    model.fit(X, y)

    future_years = np.array([2017, 2018, 2019, 2020]).reshape(-1, 1)
    predictions = model.predict(future_years)

    for year, pred in zip(future_years.flatten(), predictions):
        print(f"Previsão de jogos lançados em {year}: {int(pred)}")


# Função principal
def main():
    df = load_and_clean_data(csv_path)
    if df is None:
        print("Execução encerrada devido a erro no carregamento de dados.")
        return
    
    df = add_decade_column(df)

    print("\n" + "="*70)
    print(" TABELA DE AMOSTRA ")
    print("="*70)
    print(df.head().to_string(index=False))
    print("="*70 + "\n")

    genre_sales, platform_counts = get_top_stats(df)
    
    plot_top_genres(genre_sales)
    plot_games_per_year(df)

    apply_machine_learning(df)

    top_genre = genre_sales.index[0]
    top_genre_sales = genre_sales.iloc[0]
    top_platform = platform_counts.index[0]
    top_platform_count = platform_counts.iloc[0]
    top5_genres_list = genre_sales.head(5).index.tolist()
    year_counts = df["Year"].value_counts()
    top_year = year_counts.idxmax()
    top_year_count = year_counts.max()

    
    print("\n" + "="*70)
    print("                 RELATÓRIO DE ANÁLISE DESCRITIVA")
    print("="*70)
    print(f"Gênero de jogo mais vendido: {top_genre}")
    print(f"Vendas globais totais desse gênero: {top_genre_sales:,.2f} milhões de unidades")
    print(f"Outros gêneros do Top 5: {', '.join(top5_genres_list[1:])}")
    print(f"Plataforma com maior número de lançamentos: {top_platform}")
    print(f"Total de jogos lançados nessa plataforma: {top_platform_count}")
    print(f"Ano com mais lançamentos de jogos: {top_year} ({top_year_count} jogos)")
    print("="*70 + "\n")

    
    print("="*70)
    print("                     CONCLUSÃO")
    print("="*70)
    print(f"Nesta análise, observou-se que o gênero {top_genre} foi o mais vendido globalmente, com um total de {top_genre_sales:,.2f} milhões de unidades.")
    print(f"Os outros gêneros do Top 5 incluem: {', '.join(top5_genres_list[1:])}, mostrando forte diversidade de estilos de jogo.")
    print(f"A plataforma {top_platform} apresentou o maior número de lançamentos ({top_platform_count} jogos).")
    print(f"O ano com mais lançamentos de jogos foi {top_year}, com {top_year_count} jogos, indicando um pico de atividade na indústria.")
    print("Também aplicamos Machine Learning: agrupamos os jogos por vendas (clusters) e fizemos previsão de lançamentos futuros.")
    print("="*70 + "\n")

    print("Análise concluída com sucesso. Gráficos salvos na pasta 'outputs'.")

if __name__ == "__main__":
    main()