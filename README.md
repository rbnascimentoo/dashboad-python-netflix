# 🎬 Dashboard de Análise de Conteúdo da Netflix

Este projeto é um dashboard interativo construído com Streamlit para analisar um conjunto de dados sobre o conteúdo disponível na Netflix.

## 📊 Funcionalidades

- Visualização da distribuição de conteúdo entre Filmes e Séries de TV.
- Gráfico com os principais países produtores de conteúdo.
- Gráfico com a distribuição dos principais gêneros.
- Filtros interativos por tipo de conteúdo (Filme/Série) e por país.
- Tabela de dados que responde dinamicamente aos filtros aplicados.

## 🚀 Como Executar

Para executar este projeto localmente, siga os passos abaixo:

### Pré-requisitos

- Python 3.7+
- pip

### Instalação

1.  Clone o repositório (ou use a sua pasta local).

2.  Crie e ative um ambiente virtual (recomendado):
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  Instale as dependências a partir do arquivo `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
    *(Se você ainda não tem um, crie-o com `pip freeze > requirements.txt`)*

4.  Certifique-se de que o arquivo `netflix_dataset.csv` está na mesma pasta que `app.py`.
    Você pode baixo-lo aqui: https://www.kaggle.com/datasets/rohitgrewal/netflix-data?resource=download&select=Netflix+Dataset.csv

### Executando a Aplicação

Com as dependências instaladas, inicie a aplicação com o comando:
```bash
streamlit run app.py
```
O dashboard será aberto automaticamente no seu navegador.