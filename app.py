import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuração da Página ---
st.set_page_config(
    page_title="Dashboard de Análise da Netflix",
    page_icon="🎬",
    layout="wide"
)

# --- Carregamento dos Dados ---
# O decorator @st.cache_data garante que os dados não sejam recarregados a cada interação.
@st.cache_data
def load_data():
    try:
        # Alterado para carregar o novo dataset
        df = pd.read_csv('netflix_dataset.csv')
        # Tratamento básico de dados: preencher países vazios
        df['Country'] = df['Country'].fillna('Desconhecido')
        return df
    except FileNotFoundError:
        st.error("Arquivo 'netflix_dataset.csv' não encontrado. Certifique-se de que ele está na mesma pasta que o app.py")
        return None

df = load_data()

if df is not None:
    # --- Título do Dashboard ---
    st.title("🎬 Dashboard de Análise de Conteúdo da Netflix")
    st.markdown("Use os filtros na barra lateral para explorar os dados.")

    # --- Barra Lateral (Sidebar) com Filtros ---
    st.sidebar.header("Filtros")
    
    # Filtro por Tipo de Conteúdo (Movie/TV Show)
    tipos_disponiveis = df['Type'].unique()
    tipo_selecionado = st.sidebar.selectbox(
        "Selecione o Tipo de Conteúdo:",
        options=tipos_disponiveis
    )

    # Filtro por País
    # Para o dataset real, pode ser necessário um tratamento mais avançado para múltiplos países
    paises_disponiveis = sorted(df['Country'].unique())
    pais_selecionado = st.sidebar.multiselect(
        "Selecione o País:",
        options=paises_disponiveis,
        default=['Brazil'] # Padrão com alguns países
    )

    # --- Lógica de Filtragem ---
    # Começa filtrando por tipo, que sempre tem um valor selecionado
    df_filtrado = df[df['Type'] == tipo_selecionado]
    # Se um ou mais países forem selecionados, aplica o filtro de país.
    # Se a lista estiver vazia, o filtro não é aplicado e todos os países são mostrados.
    if pais_selecionado:
        df_filtrado = df_filtrado[df_filtrado['Country'].isin(pais_selecionado)]

    # Gráficos em colunas
    col1, col2, col3 = st.columns(3)

    with col1:
        # Gráfico Treemap: Distribuição de Filmes vs. Séries
        st.subheader("Distribuição por Tipo")
        type_counts = df['Type'].value_counts().reset_index()
        type_counts.columns = ['Tipo', 'Contagem']
        fig_treemap_type = px.treemap(
            type_counts,
            path=[px.Constant("Todos"), 'Tipo'],
            values='Contagem',
            title='Distribuição por Tipo de Conteúdo',
            color='Tipo'
        )
        fig_treemap_type.update_layout(margin = dict(t=50, l=25, r=25, b=25))
        st.plotly_chart(fig_treemap_type, use_container_width=True)

    with col2:
        # Gráfico de Barras: Top 5 Países Produtores
        st.subheader("Top Países Produtores")
        top_countries = df['Country'].value_counts().nlargest(5).reset_index()
        top_countries.columns = ['Country', 'count']
        fig_bar = px.bar(top_countries, x='Country', y='count', title='Top 5 Países com Mais Conteúdo')
        st.plotly_chart(fig_bar, use_container_width=True)

    with col3:
        # Gráfico de Pizza: Top 15 Gêneros
        st.subheader("Distribuição por Gêneros")
        # Processamento para contar os gêneros a partir da coluna 'listed_in'
        df_genres = df.dropna(subset=['Type'])
        genres = df_genres['Type'].str.split(', ').explode()
        top_genres = genres.value_counts().nlargest(15).reset_index()
        top_genres.columns = ['Gênero', 'Contagem']
        fig_pie_genres = px.pie(
            top_genres,
            names='Gênero',
            values='Contagem',
            title='Top 15 Gêneros na Netflix'
        )
        st.plotly_chart(fig_pie_genres, use_container_width=True)

    # --- Conteúdo Principal ---
    st.header(f"Exibindo: {tipo_selecionado}s")

    # Exibindo os dados filtrados em uma tabela
    st.subheader("Dados Filtrados")
    st.dataframe(df_filtrado)
