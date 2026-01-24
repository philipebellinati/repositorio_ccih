import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import re
import os

# --- Configurações da Página ---
st.set_page_config(
    layout="wide", 
    page_title="Dashboard de Sensibilidade Antimicrobiana - CCIH",
    initial_sidebar_state="expanded"
)

# --- Variáveis de Configuração ---
# SENHA PADRÃO: ccih2025. Recomenda-se usar st.secrets para produção.
ADMIN_PASSWORD = st.secrets.get("ADMIN_PASSWORD", "ccih2025") 
PROCESSED_DATA_FILE = 'processed_data.csv'

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
    </style>
    """, unsafe_allow_html=True)

# --- Funções de Processamento de Dados (Integradas) ---

def extract_polymyxin_data(row):
    """Extrai a sensibilidade à Polimixina B da coluna 'Observações do isolado'."""
    obs = str(row['Observações do isolado'])
    if 'Polimixina B' in obs:
        if 'Sensível' in obs:
            return 'Sensível'
        elif 'Resistente' in obs:
            return 'Resistente'
    return None

def process_data(df):
    """Processa, limpa duplicatas e integra Polimixina B."""
    
    # 1. Padronização de colunas
    df = df.rename(columns={'Resultado': 'Microrganismo', 'Unidade de coleta': 'Setor', 'Classificação': 'Sensibilidade'})
    
    # 2. Remoção de resultados negativos
    df = df[~df['Microrganismo'].str.contains('NEGATIVA|Negativa', na=False, case=False)].copy()
    
    # 3. Limpeza do nome do microrganismo (remove pontos finais e espaços)
    df['Microrganismo'] = df['Microrganismo'].str.replace('~', '', regex=False).str.strip()
    df['Microrganismo'] = df['Microrganismo'].str.replace(r'\.+$', '', regex=True).str.strip()
    
    # 4. Extração da Polimixina B das observações
    df_isolados_unicos = df.drop_duplicates(subset=['Código da O.S.', 'Microrganismo']).copy()
    df_isolados_unicos['Sensibilidade_Poli'] = df_isolados_unicos.apply(extract_polymyxin_data, axis=1)
    
    df_poli_rows = df_isolados_unicos.dropna(subset=['Sensibilidade_Poli']).copy()
    df_poli_rows['Antimicrobiano'] = 'Polimixina B'
    df_poli_rows['Sensibilidade'] = df_poli_rows['Sensibilidade_Poli']
    
    # 5. Combinar e Limpar Duplicatas
    df = df[df['Antimicrobiano'] != 'Polimixina B']
    df_final = pd.concat([df, df_poli_rows], ignore_index=True)
    
    # Seleção de colunas essenciais
    cols = ['Código da O.S.', 'Data da O.S.', 'Setor', 'Material', 'Microrganismo', 'Antimicrobiano', 'Sensibilidade']
    df_final = df_final[cols].dropna(subset=['Antimicrobiano', 'Sensibilidade'])
    
    # LIMPEZA DE DUPLICATAS CRÍTICA: Remove linhas onde OS, Microrganismo e ATB são idênticos
    df_final = df_final.drop_duplicates(subset=['Código da O.S.', 'Microrganismo', 'Antimicrobiano'])
    
    # Limpeza final de strings
    df_final['Antimicrobiano'] = df_final['Antimicrobiano'].str.strip()
    df_final['Sensibilidade'] = df_final['Sensibilidade'].str.strip()

    return df_final

# --- Funções de Carregamento e Cache ---

@st.cache_data
def load_data(file_path):
    """Carrega os dados processados."""
    if not os.path.exists(file_path):
        st.error(f"Arquivo de dados processados '{file_path}' não encontrado. Por favor, use a aba 'Administrador' para fazer o upload da planilha original.")
        return pd.DataFrame()
        
    df = pd.read_csv(file_path)
    df['Data da O.S.'] = pd.to_datetime(df['Data da O.S.'])
    df['Ano'] = df['Data da O.S.'].dt.year
    df['Mês'] = df['Data da O.S.'].dt.month
    return df

# --- Funções de Visualização ---

def create_prevalence_chart(df_filtered):
    """Cria o gráfico de barras dos microrganismos mais prevalentes."""
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
        stats = df_micro.groupby(['Antimicrobiano', 'Sensibilidade']).size().unstack(fill_value=0)
        
        if 'Sensível' not in stats.columns:
            stats['Sensível'] = 0
            
        total = stats.sum(axis=1)
        # Filtra antibióticos com menos de 10 testes para evitar distorção
        valid_tests = total[total >= 10]
        
        perc = (stats['Sensível'] / total) * 100
        perc = perc[valid_tests.index] # Aplica o filtro
        
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
        [0.0, '#d73027'], [0.2, '#f46d43'], [0.4, '#fee08b'], 
        [0.6, '#d9ef8b'], [0.8, '#1a9850'], [1.0, '#1a9850']
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

# --- Páginas do Dashboard ---

def main_dashboard(df):
    """Página principal do dashboard."""
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

    # Filtro de Antibiótico (Apenas para Tabela de Dados)
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

def admin_page():
    """Página de administração para upload de dados."""
    st.title("🔒 Área Administrativa - Upload de Dados")
    st.warning("Atenção: O upload de um novo arquivo substituirá os dados atuais do dashboard.")

    uploaded_file = st.file_uploader("Selecione o arquivo Excel original (HCL2025.xlsx)", type=['xlsx'])

    if uploaded_file is not None:
        try:
            # 1. Carregar o arquivo
            df_original = pd.read_excel(uploaded_file)
            st.success("Arquivo carregado com sucesso!")
            
            # 2. Processar os dados
            with st.spinner("Processando e limpando os dados..."):
                df_processed = process_data(df_original)
            
            # 3. Salvar o novo arquivo processado
            df_processed.to_csv(PROCESSED_DATA_FILE, index=False)
            
            st.success(f"Processamento concluído! {len(df_processed)} registros únicos salvos.")
            st.balloons()
            
            # 4. Limpar o cache e recarregar o dashboard
            st.cache_data.clear()
            st.info("O dashboard será recarregado automaticamente com os novos dados.")
            st.experimental_rerun()

        except Exception as e:
            st.error(f"Ocorreu um erro durante o processamento. Verifique se o arquivo está no formato esperado (colunas: 'Código da O.S.', 'Resultado', 'Antimicrobiano', 'Classificação', 'Observações do isolado', etc.).")
            st.exception(e)

# --- Lógica de Autenticação e Navegação ---

def main():
    # Inicializa o estado de navegação
    if 'page' not in st.session_state:
        st.session_state.page = 'dashboard'
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    # Navegação na Sidebar
    st.sidebar.markdown("---")
    if st.session_state.page == 'dashboard':
        if st.sidebar.button("Ir para Admin"):
            st.session_state.page = 'login'
            st.experimental_rerun()
    elif st.session_state.page == 'admin':
        if st.sidebar.button("Voltar para Dashboard"):
            st.session_state.page = 'dashboard'
            st.experimental_rerun()
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.page = 'login'
            st.experimental_rerun()

    # Lógica de Roteamento
    if st.session_state.page == 'dashboard':
        df = load_data(PROCESSED_DATA_FILE)
        if not df.empty:
            main_dashboard(df)
    
    elif st.session_state.page == 'login':
        st.title("Login Administrativo")
        password = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            if password == ADMIN_PASSWORD:
                st.session_state.logged_in = True
                st.session_state.page = 'admin'
                st.experimental_rerun()
            else:
                st.error("Senha incorreta.")
    
    elif st.session_state.page == 'admin':
        if st.session_state.logged_in:
            admin_page()
        else:
            st.session_state.page = 'login'
            st.experimental_rerun()

if __name__ == "__main__":
    main()
