import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# --- Configurações da Página ---
st.set_page_config(layout="wide", page_title="Dashboard de Sensibilidade Antimicrobiana - CCIH")

# --- Funções de Carregamento e Processamento de Dados ---

@st.cache_data
def load_data(file_path):
    """Carrega os dados processados."""
    df = pd.read_csv(file_path)
    df['Data da O.S.'] = pd.to_datetime(df['Data da O.S.'])
    return df

@st.cache_data
def get_microrganism_groups(df):
    """Identifica e agrupa microrganismos (simplificado para o escopo)."""
    # Para este conjunto de dados, vamos assumir que todos são bactérias, exceto se houver fungos explícitos.
    # Como não vimos fungos na análise inicial, vamos focar na prevalência.
    # Se o usuário tiver fungos, a lógica precisará ser mais robusta (ex: lista de fungos conhecidos).
    
    # Excluindo resultados negativos que podem ter passado pelo filtro inicial (embora o data_processor tente remover)
    micros = df[~df['Microrganismo'].str.contains('NEGATIVA|Negativa', na=False, case=False)]['Microrganismo'].unique()
    return sorted(micros)

# --- Funções de Visualização ---

def create_prevalence_chart(df_filtered):
    """Cria o gráfico de barras dos microrganismos mais prevalentes."""
    # Contagem de microrganismos únicos por Código da O.S. (isolados)
    df_isolados = df_filtered.drop_duplicates(subset=['Código da O.S.', 'Microrganismo'])
    
    prevalence = df_isolados['Microrganismo'].value_counts().reset_index()
    prevalence.columns = ['Microrganismo', 'Contagem']
    
    # Aplicar filtro Top 15 (preferência do CCIH)
    top_15 = prevalence.head(15)
    
    # Formatação em itálico
    top_15['Microrganismo_Italico'] = '<i>' + top_15['Microrganismo'] + '</i>'

    fig = px.bar(
        top_15,
        x='Microrganismo_Italico',
        y='Contagem',
        title='Microrganismos Mais Prevalentes (Top 15)',
        labels={'Microrganismo_Italico': 'Microrganismo', 'Contagem': 'Número de Isolados'},
        color='Contagem',
        color_continuous_scale=px.colors.sequential.Viridis
    )
    fig.update_layout(xaxis={'categoryorder':'total descending'}, title_x=0.5)
    return fig

def create_material_distribution_chart(df_filtered):
    """Cria o gráfico de distribuição por material."""
    # Contagem de amostras únicas por Código da O.S. e Material
    df_amostras = df_filtered.drop_duplicates(subset=['Código da O.S.', 'Material'])
    
    distribution = df_amostras['Material'].value_counts().reset_index()
    distribution.columns = ['Material', 'Contagem']
    
    fig = px.bar(
        distribution,
        x='Material',
        y='Contagem',
        title='Distribuição por Material',
        labels={'Material': 'Material', 'Contagem': 'Contagem de Amostras'},
        color='Contagem',
        color_continuous_scale=px.colors.sequential.Plasma
    )
    fig.update_layout(xaxis={'categoryorder':'total descending'}, title_x=0.5)
    return fig

def calculate_antibiogram(df, microrganism):
    """Calcula o percentual de sensibilidade para um microrganismo."""
    df_micro = df[df['Microrganismo'] == microrganism].copy()
    
    # Agrupar por Antimicrobiano e Sensibilidade
    antibiogram = df_micro.groupby(['Antimicrobiano', 'Sensibilidade']).size().unstack(fill_value=0)
    
    # Calcular o total de testes por Antimicrobiano
    antibiogram['Total'] = antibiogram.sum(axis=1)
    
    # Calcular o percentual de sensibilidade (S / Total)
    sensivel = antibiogram.get('Sensível', 0)
    
    if isinstance(sensivel, pd.Series):
        antibiogram['% Sensível'] = (sensivel / antibiogram['Total']) * 100
    else:
        antibiogram['% Sensível'] = 0
        
    return antibiogram.reset_index()

def create_antibiogram_heatmap(df_filtered):
    """Cria o mapa de calor de sensibilidade aos antibióticos."""
    
    # 1. Identificar os microrganismos mais prevalentes (Top 15)
    df_isolados = df_filtered.drop_duplicates(subset=['Código da O.S.', 'Microrganismo'])
    prevalence = df_isolados['Microrganismo'].value_counts().reset_index()
    top_15_micros = prevalence.head(15)['Microrganismo'].tolist()
    
    # 2. Calcular o antibiograma para cada um dos Top 15
    heatmap_data = []
    for micro in top_15_micros:
        result = calculate_antibiogram(df_filtered, micro)
        result['Microrganismo'] = micro
        heatmap_data.append(result)
        
    if not heatmap_data:
        return go.Figure().update_layout(title="Sem dados para o Mapa de Calor de Sensibilidade")

    df_heatmap = pd.concat(heatmap_data, ignore_index=True)
    
    # Pivotar a tabela para o formato do mapa de calor
    pivot_table = df_heatmap.pivot_table(
        index='Microrganismo', 
        columns='Antimicrobiano', 
        values='% Sensível', 
        fill_value=np.nan
    )
    
    # Ordenar microrganismos pela prevalência
    pivot_table = pivot_table.reindex(top_15_micros)
    
    # Formatação em itálico
    pivot_table.index = ['<i>' + m + '</i>' for m in pivot_table.index]
    
    # 3. Definição da escala de cores e legendas (Baseado no dashboard de referência)
    colorscale = [
        [0.0, 'rgb(255, 0, 0)'],    # <20% (Vermelho)
        [0.2, 'rgb(255, 165, 0)'],  # 20-39% (Laranja)
        [0.4, 'rgb(255, 255, 0)'],  # 40-59% (Amarelo)
        [0.6, 'rgb(173, 255, 47)'], # 60-79% (Verde Amarelado)
        [0.8, 'rgb(0, 128, 0)'],    # >=80% (Verde Escuro)
        [1.0, 'rgb(0, 128, 0)']
    ]
    
    # 4. Criar o mapa de calor
    fig = go.Figure(data=go.Heatmap(
        z=pivot_table.values,
        x=pivot_table.columns,
        y=pivot_table.index,
        colorscale=colorscale,
        zmin=0,
        zmax=100,
        text=pivot_table.apply(lambda x: [f'{v:.0f}%' if not pd.isna(v) else 'N/A' for v in x], axis=1).values,
        texttemplate="%{text}",
        hoverongaps=False
    ))
    
    fig.update_layout(
        title='Mapa de Calor - Sensibilidade aos Antibióticos',
        xaxis_title='Antimicrobiano',
        yaxis_title='Microrganismo',
        title_x=0.5,
        height=600
    )
    
    return fig

def calculate_resistance_mechanisms(df, microrganism):
    """Calcula o percentual de presença de mecanismos de resistência."""
    df_micro = df[df['Microrganismo'] == microrganism].copy()
    
    # Contar isolados únicos para o microrganismo
    df_isolados = df_micro.drop_duplicates(subset=['Código da O.S.', 'Microrganismo'])
    total_isolados = len(df_isolados)
    
    if total_isolados == 0:
        return pd.Series(index=['KPC', 'NDM', 'OXA', 'VIM', 'IMP', 'ESBL', 'MRSA', 'VRE'], dtype=float).fillna(np.nan)

    results = {}
    mecanismos = ['KPC', 'NDM', 'OXA', 'VIM', 'IMP', 'ESBL', 'MRSA', 'VRE']
    
    for mec in mecanismos:
        # Contar o número de isolados únicos com o mecanismo Positivo
        count_positive = df_isolados[df_isolados[mec] == 'Positivo']['Código da O.S.'].nunique()
        results[mec] = (count_positive / total_isolados) * 100
        
    return pd.Series(results)

def create_resistance_heatmap(df_filtered):
    """Cria o mapa de calor de mecanismos de resistência."""
    
    # 1. Identificar os microrganismos mais prevalentes (Top 15)
    df_isolados = df_filtered.drop_duplicates(subset=['Código da O.S.', 'Microrganismo'])
    prevalence = df_isolados['Microrganismo'].value_counts().reset_index()
    top_15_micros = prevalence.head(15)['Microrganismo'].tolist()
    
    # 2. Calcular os mecanismos de resistência para cada um dos Top 15
    heatmap_data = {}
    for micro in top_15_micros:
        heatmap_data[micro] = calculate_resistance_mechanisms(df_filtered, micro)
        
    df_heatmap = pd.DataFrame(heatmap_data).T
    
    if df_heatmap.empty:
        return go.Figure().update_layout(title="Sem dados para o Mapa de Calor de Mecanismos de Resistência")

    # Ordenar microrganismos pela prevalência
    df_heatmap = df_heatmap.reindex(top_15_micros)
    
    # Formatação em itálico
    df_heatmap.index = ['<i>' + m + '</i>' for m in df_heatmap.index]
    
    # 3. Definição da escala de cores e legendas (Baseado no dashboard de referência)
    # Cores invertidas para resistência: Vermelho = Alta Presença
    colorscale = [
        [0.0, 'rgb(0, 128, 0)'],    # <20% (Verde Escuro)
        [0.2, 'rgb(173, 255, 47)'], # 20-39% (Verde Amarelado)
        [0.4, 'rgb(255, 255, 0)'],  # 40-59% (Amarelo)
        [0.6, 'rgb(255, 165, 0)'],  # 60-79% (Laranja)
        [0.8, 'rgb(255, 0, 0)'],    # >=80% (Vermelho)
        [1.0, 'rgb(255, 0, 0)']
    ]
    
    # 4. Criar o mapa de calor
    fig = go.Figure(data=go.Heatmap(
        z=df_heatmap.values,
        x=df_heatmap.columns,
        y=df_heatmap.index,
        colorscale=colorscale,
        zmin=0,
        zmax=100,
        text=df_heatmap.apply(lambda x: [f'{v:.0f}%' if not pd.isna(v) else 'N/A' for v in x], axis=1).values,
        texttemplate="%{text}",
        hoverongaps=False
    ))
    
    fig.update_layout(
        title='Mapa de Calor - Mecanismos de Resistência',
        xaxis_title='Mecanismo de Resistência',
        yaxis_title='Microrganismo',
        title_x=0.5,
        height=600
    )
    
    return fig

# --- Aplicação Streamlit Principal ---

def main():
    # Carregar dados
    df = load_data('processed_data.csv')
    
    st.title("Dashboard de Sensibilidade Antimicrobiana")
    st.markdown("Análise de prevalência e sensibilidade - CCIH Hospital Cancer")

    # --- Sidebar para Filtros ---
    st.sidebar.header("Filtros")
    
    # Filtro de Mês (Período)
    min_date = df['Data da O.S.'].min().to_numpy()
    max_date = df['Data da O.S.'].max().to_numpy()
    
    # Converter para datetime.date para o slider
    min_date_dt = pd.to_datetime(min_date).date()
    max_date_dt = pd.to_datetime(max_date).date()
    
    date_range = st.sidebar.date_input(
        "Período de Análise",
        value=(min_date_dt, max_date_dt),
        min_value=min_date_dt,
        max_value=max_date_dt
    )
    
    if len(date_range) == 2:
        start_date = pd.to_datetime(date_range[0])
        end_date = pd.to_datetime(date_range[1])
        df_filtered = df[(df['Data da O.S.'] >= start_date) & (df['Data da O.S.'] <= end_date)]
    else:
        df_filtered = df.copy()

    # Filtro de Material
    materials = ['Todos os materiais'] + sorted(df_filtered['Material'].unique().tolist())
    selected_material = st.sidebar.selectbox("Material", materials)
    if selected_material != 'Todos os materiais':
        df_filtered = df_filtered[df_filtered['Material'] == selected_material]

    # Filtro de Setor
    sectors = ['Todos os setores'] + sorted(df_filtered['Setor'].unique().tolist())
    selected_sector = st.sidebar.selectbox("Setor", sectors)
    if selected_sector != 'Todos os setores':
        df_filtered = df_filtered[df_filtered['Setor'] == selected_sector]

    # Filtro de Microrganismo
    micros = ['Todos os microrganismos'] + get_microrganism_groups(df_filtered)
    selected_micro = st.sidebar.selectbox("Microrganismo", micros)
    if selected_micro != 'Todos os microrganismos':
        df_filtered = df_filtered[df_filtered['Microrganismo'] == selected_micro]

    # Botão Limpar Filtros (apenas informativo, o recarregamento do app faz o reset)
    if st.sidebar.button("Limpar Filtros"):
        st.experimental_rerun()

    # --- Métricas e Gráficos ---
    
    # Contagem de Isolados Únicos
    total_isolados = df_filtered.drop_duplicates(subset=['Código da O.S.', 'Microrganismo'])['Código da O.S.'].nunique()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Total de Isolados", value=total_isolados)
        
    with col2:
        # Exibir filtros ativos
        active_filters = []
        if selected_material != 'Todos os materiais': active_filters.append(f"Material: {selected_material}")
        if selected_sector != 'Todos os setores': active_filters.append(f"Setor: {selected_sector}")
        if selected_micro != 'Todos os microrganismos': active_filters.append(f"Microrganismo: {selected_micro}")
        
        if active_filters:
            st.info("Filtros Ativos: " + ", ".join(active_filters))
        else:
            st.info("Nenhum filtro ativo")

    st.markdown("---")

    # Gráficos de Prevalência e Distribuição
    col3, col4 = st.columns(2)
    
    with col3:
        st.plotly_chart(create_prevalence_chart(df_filtered), use_container_width=True)
        
    with col4:
        st.plotly_chart(create_material_distribution_chart(df_filtered), use_container_width=True)

    st.markdown("---")

    # Mapa de Calor de Sensibilidade
    st.header("Mapa de Calor - Sensibilidade aos Antibióticos")
    st.plotly_chart(create_antibiogram_heatmap(df_filtered), use_container_width=True)
    
    # Legenda para o Mapa de Calor de Sensibilidade
    st.markdown("""
    **Legenda de Sensibilidade:**
    | Cor | % Sensível |
    | :---: | :---: |
    | <span style="color:rgb(0, 128, 0)">███</span> | ≥80% Sensível |
    | <span style="color:rgb(173, 255, 47)">███</span> | 60-79% |
    | <span style="color:rgb(255, 255, 0)">███</span> | 40-59% |
    | <span style="color:rgb(255, 165, 0)">███</span> | 20-39% |
    | <span style="color:rgb(255, 0, 0)">███</span> | <20% |
    | N/A | Sem dados |
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Mapa de Calor de Mecanismos de Resistência
    st.header("Mapa de Calor - Mecanismos de Resistência")
    st.plotly_chart(create_resistance_heatmap(df_filtered), use_container_width=True)
    
    # Legenda para o Mapa de Calor de Mecanismos de Resistência
    st.markdown("""
    **Legenda de Mecanismos de Resistência:**
    | Cor | % Presença |
    | :---: | :---: |
    | <span style="color:rgb(255, 0, 0)">███</span> | ≥80% Presente |
    | <span style="color:rgb(255, 165, 0)">███</span> | 60-79% |
    | <span style="color:rgb(255, 255, 0)">███</span> | 40-59% |
    | <span style="color:rgb(173, 255, 47)">███</span> | 20-39% |
    | <span style="color:rgb(0, 128, 0)">███</span> | <20% Presente |
    | N/A | Sem dados |
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    # O script data_processor.py deve ser executado antes para gerar processed_data.csv
    if not pd.io.common.file_exists('processed_data.csv'):
        st.error("O arquivo 'processed_data.csv' não foi encontrado. Certifique-se de que o script de processamento de dados foi executado com sucesso.")
    else:
        main()
