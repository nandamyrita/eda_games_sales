# 🎮 Case 1 — Análise de Dados de Games

## 🧠 Contexto

O objetivo deste projeto é realizar uma **análise exploratória de dados (EDA)** sobre o mercado global de games, identificando **padrões de vendas**, **gêneros mais populares**, **plataformas mais utilizadas** e **principais publishers**.

Este case tem como propósito demonstrar habilidades em **Python**, **análise de dados**, **visualização gráfica** e **organização de código**, sendo parte de uma avaliação técnica.

---

## 📁 Estrutura do Projeto

```
case1_games/
│
├── data/
│   └── vgsales.csv         # Base de dados original
│
├── case1_games.py           # Script principal com toda a análise
│
├── requirements.txt         # Bibliotecas necessárias
│
└── README.md                # Documentação do projeto
```

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.x**
- **Pandas**: Para manipulação e análise de dados.
- **Matplotlib**: Para geração de gráficos.
- **Seaborn**: Para visualizações mais estéticas e gráficas.
- **Pathlib**: Para manipulação de caminhos de arquivos.
- **sys**: Para tratamento de erros de arquivo.

---

## 💾 Base de Dados

**Arquivo:** `vgsales.csv`  
**Fonte:** Dataset público adaptado contendo informações sobre vendas globais de videogames.

| Nome               | Plataforma | Ano  | Gênero   | Publisher  | Vendas Globais (milhões) |
| ------------------ | ---------- | ---- | -------- | ---------- | ------------------------ |
| Super Mario Galaxy | Wii        | 2007 | Platform | Nintendo   | 11.35                    |
| Call of Duty: MW2  | X360       | 2009 | Shooter  | Activision | 13.52                    |
| Wii Sports Resort  | Wii        | 2009 | Sports   | Nintendo   | 33.09                    |
| Grand Theft Auto V | PS4        | 2014 | Action   | Take-Two   | 21.40                    |

---

## 📊 Análises Realizadas

- Identifica o gênero de jogo que mais vendeu globalmente.
- Identifica a plataforma com maior número de jogos lançados.
- Cria uma nova coluna `Decade` classificando os jogos em "1990s", "2000s", "2010s" ou "Outros".

---

## 📈 Exemplos de Gráficos

### 🧩 Top 5 Gêneros Mais Vendidos

Gráfico de barras mostrando as vendas globais totais dos 5 gêneros mais vendidos.

### 🎮 Total de Jogos por Ano

Gráfico de linhas mostrando o total de jogos lançados por ano.

---

## 🧹 Limpeza e Tratamento de Dados

Durante o processo de análise, foram realizadas as seguintes etapas:

1. **Remoção de valores nulos** e inconsistências.
2. **Padronização de colunas** e nomes.
3. **Converte a coluna `Year` para numérico** e remove linhas com valores faltantes.
4. **Criação de coluna derivada "Década"** para análises temporais.

---

## 🚀 Como Executar o Projeto

### 🔧 Passo 1: Clonar o repositório

```bash
git clone https://github.com/seuusuario/case1_games.git
cd case1_games
```

### 🔧 Passo 2: Criar e ativar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate
```

### 🔧 Passo 3: Instalar dependências

```bash
pip install -r requirements.txt
```

### 🔧 Passo 4: Executar o script principal

```bash
python case1_games.py
```

## 🧩 Resultados Principais

| Métrica                              | Resultado |
| ------------------------------------ | --------- |
| 🕹️ Gênero mais vendido               | Shooter   |
| 💻 Plataforma com mais lançamentos   | PC        |
| 📆 Década com maior volume de vendas | 2010s     |

---

## 🌱 Possíveis Extensões Futuras

- 📊 Criação de dashboard interativo (Streamlit ou React + Flask)
- 🔮 Previsão de vendas futuras com **Machine Learning**
- 🧭 Comparação entre **regiões geográficas**
- 💬 Análises de **tendências de mercado** com NLP
- 🧠 Integração com APIs externas de dados de games (ex: RAWG API)

---

## 🔍 Comandos Extras (Profissionais)

### Rodar análise com log detalhado:

```bash
python -u case1_games.py > logs.txt
```

### Criar ambiente com Conda (alternativa):

```bash
conda create -n case1_games python=3.11
conda activate case1_games
pip install -r requirements.txt
```

---

## 👩‍💻 Autora

**Maria Fernanda**  
Estudante de **Desenvolvimento de Software** na Fatec, com foco em **Front-End**, **Análise de Dados** e **Inteligência Artificial**.

Atua com Python, Java, React e Tailwind CSS, e tem grande interesse em unir tecnologia e design para criar soluções criativas e eficientes.

---

## ⚠️ Avisos Importantes

> 🔒 **Segurança:** Nenhuma credencial sensível foi incluída neste repositório.  
> 📊 **Licença de Dados:** Dataset utilizado apenas para fins **acadêmicos e educacionais**.  
> 💡 **Propósito:** Projeto de análise de dados desenvolvido para fins de **avaliação técnica**.  
> 🧠 **Observação:** Resultados baseiam-se apenas na amostra fornecida e podem variar conforme a base de dados.

---
