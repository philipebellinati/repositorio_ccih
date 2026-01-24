import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# --- Configurações da Página ---
st.set_page_config(
    layout="wide", 
    page_title="Dashboard de Sensibilidade Antimicrobiana - CCIH",
    initial_sidebar_state="expanded"
)

# --- Estilo CSS Customizado ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    div[data-testid="stExpander"] {
        border: none;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- Funções de Carregamento e Processamento de Dados ---

@st.cache_data
def load_data(file_path):
    """Carrega os dados processados."""
    df = pd.read_csv(file_path)
    df['Data da O.S.'] = pd.to_datetime(df['Data da O.S.'])
    df['Ano'] = df['Data da O.S.'].dt.year
    df['Mês'] = df['Data da O.S.'].dt.month
    return df

# --- Funções de Visualização ---

def create_prevalence_chart(df_filtered):
    """Cria o gráfico de barras dos microrganismos mais prevalentes."""
    # Contagem de microrganismos únicos por Código da O.S. (isolados)
    df_isolados = df_filtered.drop_duplicates(subset=['Código da O.S.', 'Microrganismo'])
    
    prevalence = df_isolados['Microrganismo'].value_counts().reset_index()
    prevalence.columns = ['Microrganismo', 'Contagem']
    
    top_15 = prevalence.head(15)
    top_15['Microrganismo_Italico'] = '<i>' + top_15['Microrganismo'] + '</i>'

    fig = px.bar(
        top_15,
        x='Microrganismo_Italico',
        y='Contagem',
        title='Top 15 Microrganismos',
        labels={'Microrganismo_Italico': 'Microrganismo', 'Contagem': 'Isolados'},
        color='Contagem',
        color_continuous_scale='Blues'
    )
    fig.update_layout(
        xaxis={'categoryorder':'total descending'}, 
        title_x=0.5,
        xaxis_tickangle=-45,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=50, b=100)
    )
    return fig

def create_material_distribution_chart(df_filtered):
    """Cria o gráfico de distribuição por material."""
    df_amostras = df_filtered.drop_duplicates(subset=['Código da O.S.', 'Material'])
    distribution = df_amostras['Material'].value_counts().reset_index()
    distribution.columns = ['Material', 'Contagem']
    
    fig = px.bar(
        distribution.head(10),
        x='Material',
        y='Contagem',
        title='Top 10 Materiais',
        labels={'Material': 'Material', 'Contagem': 'Amostras'},
        color='Contagem',
        color_continuous_scale='Reds'
    )
    fig.update_layout(
        xaxis={'categoryorder':'total descending'}, 
        title_x=0.5,
        xaxis_tickangle=-45,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=50, b=100)
    )
    return fig

def create_antibiogram_heatmap(df_filtered):
    """Cria o mapa de calor de sensibilidade aos antibióticos."""
    
    # 1. Identificar os microrganismos mais prevalentes (Top 15)
    df_isolados = df_filtered.drop_duplicates(subset=['Código da O.S.', 'Microrganismo'])
    top_15_micros = df_isolados['Microrganismo'].value_counts().head(15).index.tolist()
    
    if not top_15_micros:
        return go.Figure().update_layout(title="Sem dados para exibição")

    # 2. Calcular sensibilidade
    heatmap_data = []
    for micro in top_15_micros:
        df_micro = df_filtered[df_filtered['Microrganismo'] == micro]
        # Agrupar por Antimicrobiano e Sensibilidade
        stats = df_micro.groupby(['Antimicrobiano', 'Sensibilidade']).size().unstack(fill_value=0)
        
        # Garantir que a coluna 'Sensível' exista, mesmo que com zeros
        if 'Sensível' not in stats.columns:
            stats['Sensível'] = 0
            
        total = stats.sum(axis=1)
        perc = (stats['Sensível'] / total) * 100
        res = perc.reset_index()
        res.columns = ['Antimicrobiano', '% Sensível']
        res['Microrganismo'] = micro
        heatmap_data.append(res)
            
    if not heatmap_data:
        return go.Figure().update_layout(title="Sem dados de sensibilidade")

    df_heatmap = pd.concat(heatmap_data)
    pivot_table = df_heatmap.pivot_table(index='Microrganismo', columns='Antimicrobiano', values='% Sensível')
    pivot_table = pivot_table.reindex(top_15_micros)
    pivot_table.index = ['<i>' + m + '</i>' for m in pivot_table.index]
    
    # 3. Escala de cores CCIH
    colorscale = [
        [0.0, '#d73027'],   # <20% (Vermelho)
        [0.2, '#f46d43'],   # 20-39% (Laranja)
        [0.4, '#fee08b'],   # 40-59% (Amarelo)
        [0.6, '#d9ef8b'],   # 60-79% (Verde Claro)
        [0.8, '#1a9850'],   # >=80% (Verde Escuro)
        [1.0, '#1a9850']
    ]
    
    fig = go.Figure(data=go.Heatmap(
        z=pivot_table.values,
        x=pivot_table.columns,
        y=pivot_table.index,
        colorscale=colorscale,
        zmin=0, zmax=100,
        text=pivot_table.apply(lambda x: [f'{v:.0f}%' if not pd.isna(v) else 'N/A' for v in x], axis=1).values,
        texttemplate="%{text}",
        hoverongaps=False
    ))
    
    fig.update_layout(
        title='Perfil de Sensibilidade Antimicrobiana (%)',
        title_x=0.5,
        height=700,
        xaxis_tickangle=-45,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    return fig

# --- Aplicação Principal ---

def main():
    df = load_data('processed_data.csv')
    
    st.title("📊 Dashboard de Sensibilidade Antimicrobiana")
    st.markdown("Controle de Infecção Hospitalar - **CCIH Hospital Cancer**")

    # --- Sidebar ---
    st.sidebar.header("Filtros")
    
    # Ano e Mês
    all_years = sorted(df['Ano'].unique(), reverse=True)
    sel_year = st.sidebar.selectbox("Ano", ['Todos'] + all_years)
    
    df_f = df.copy()
    if sel_year != 'Todos':
        df_f = df_f[df_f['Ano'] == sel_year]

    month_map = {1:'Jan', 2:'Fev', 3:'Mar', 4:'Abr', 5:'Mai', 6:'Jun', 7:'Jul', 8:'Ago', 9:'Set', 10:'Out', 11:'Nov', 12:'Dez'}
    avail_months = sorted(df_f['Mês'].unique())
    sel_month_name = st.sidebar.selectbox("Mês", ['Todos'] + [month_map[m] for m in avail_months])
    
    if sel_month_name != 'Todos':
        sel_month = [k for k, v in month_map.items() if v == sel_month_name][0]
        df_f = df_f[df_f['Mês'] == sel_month]

    # Outros Filtros
    sel_material = st.sidebar.selectbox("Material", ['Todos'] + sorted(df_f['Material'].unique().tolist()))
    if sel_material != 'Todos': df_f = df_f[df_f['Material'] == sel_material]
    
    sel_sector = st.sidebar.selectbox("Setor", ['Todos'] + sorted(df_f['Setor'].unique().tolist()))
    if sel_sector != 'Todos': df_f = df_f[df_f['Setor'] == sel_sector]

    sel_micro = st.sidebar.selectbox("Microrganismo", ['Todos'] + sorted(df_f['Microrganismo'].unique().tolist()))
    if sel_micro != 'Todos': df_f = df_f[df_f['Microrganismo'] == sel_micro]

    # Filtro de Antibiótico (Polimixina B estará aqui)
    # Usamos o multiselect para permitir a seleção de ATBs específicos para filtrar o dataset,
    # mas o mapa de calor sempre mostrará todos os ATBs dos top 15 microrganismos.
    all_atbs = sorted(df_f['Antimicrobiano'].unique().tolist())
    sel_atb = st.sidebar.multiselect("Filtrar por Antibiótico (Apenas para Tabela de Dados)", all_atbs)
    
    df_f_atb = df_f.copy()
    if sel_atb: df_f_atb = df_f_atb[df_f_atb['Antimicrobiano'].isin(sel_atb)]

    # --- Layout ---
    total_isolados = df_f.drop_duplicates(subset=['Código da O.S.', 'Microrganismo'])['Código da O.S.'].nunique()
    st.metric("Total de Isolados Únicos", total_isolados)

    st.markdown("---")
    
    c1, c2 = st.columns(2)
    with c1: st.plotly_chart(create_prevalence_chart(df_f), use_container_width=True)
    with c2: st.plotly_chart(create_material_distribution_chart(df_f), use_container_width=True)

    st.markdown("---")
    st.header("Mapa de Calor - Perfil de Sensibilidade")
    st.plotly_chart(create_antibiogram_heatmap(df_f), use_container_width=True)

    # Legenda
    st.markdown("""
    <div style="display: flex; justify-content: center; gap: 20px; font-size: 0.9em;">
        <span><b style="color:#1a9850;">■</b> ≥80% Sensível</span>
        <span><b style="color:#d9ef8b;">■</b> 60-79%</span>
        <span><b style="color:#fee08b;">■</b> 40-59%</span>
        <span><b style="color:#f46d43;">■</b> 20-39%</span>
        <span><b style="color:#d73027;">■</b> <20%</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabela de dados detalhada (opcional)
    with st.expander("Ver Dados Detalhados (Filtrados)"):
        st.dataframe(df_f_atb)

if __name__ == "__main__":
    main()
