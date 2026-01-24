import pandas as pd
import re

def extract_polymyxin_data(row):
    """Extrai a sensibilidade à Polimixina B da coluna 'Observações do isolado'."""
    obs = str(row['Observações do isolado'])
    if 'Polimixina B' in obs:
        if 'Sensível' in obs:
            return 'Sensível'
        elif 'Resistente' in obs:
            return 'Resistente'
    return None

def process_data(file_path):
    """Carrega, processa, limpa duplicatas e integra Polimixina B."""
    print("Carregando dados...")
    df = pd.read_excel(file_path)

    # 1. Padronização de colunas
    df = df.rename(columns={'Resultado': 'Microrganismo', 'Unidade de coleta': 'Setor', 'Classificação': 'Sensibilidade'})
    
    # 2. Remoção de resultados negativos
    df = df[~df['Microrganismo'].str.contains('NEGATIVA|Negativa', na=False, case=False)].copy()
    
    # 3. Limpeza do nome do microrganismo
    df['Microrganismo'] = df['Microrganismo'].str.replace('~', '', regex=False).str.strip()
    df['Microrganismo'] = df['Microrganismo'].str.replace(r'\.+$', '', regex=True).str.strip()
    
    # 4. Extração da Polimixina B das observações (antes de remover duplicatas gerais)
    print("Extraindo Polimixina B das observações...")
    df_isolados_unicos = df.drop_duplicates(subset=['Código da O.S.', 'Microrganismo']).copy()
    df_isolados_unicos['Sensibilidade_Poli'] = df_isolados_unicos.apply(extract_polymyxin_data, axis=1)
    
    df_poli_rows = df_isolados_unicos.dropna(subset=['Sensibilidade_Poli']).copy()
    df_poli_rows['Antimicrobiano'] = 'Polimixina B'
    df_poli_rows['Sensibilidade'] = df_poli_rows['Sensibilidade_Poli']
    
    # 5. Combinar e Limpar Duplicatas
    # Removemos qualquer Polimixina B que já exista na coluna Antimicrobiano original
    df = df[df['Antimicrobiano'] != 'Polimixina B']
    df_final = pd.concat([df, df_poli_rows], ignore_index=True)
    
    # Seleção de colunas essenciais
    cols = ['Código da O.S.', 'Data da O.S.', 'Setor', 'Material', 'Microrganismo', 'Antimicrobiano', 'Sensibilidade']
    df_final = df_final[cols].dropna(subset=['Antimicrobiano', 'Sensibilidade'])
    
    # LIMPEZA DE DUPLICATAS CRÍTICA:
    # Se houver mais de um resultado para o mesmo ATB no mesmo isolado, mantemos apenas um.
    print("Removendo duplicatas absolutas...")
    df_final = df_final.drop_duplicates(subset=['Código da O.S.', 'Microrganismo', 'Antimicrobiano'])
    
    # Limpeza final de strings
    df_final['Antimicrobiano'] = df_final['Antimicrobiano'].str.strip()
    df_final['Sensibilidade'] = df_final['Sensibilidade'].str.strip()

    print(f"Processamento concluído. Total de registros únicos: {len(df_final)}")
    return df_final

if __name__ == '__main__':
    processed = process_data('/home/ubuntu/upload/HCL2025.xlsx')
    processed.to_csv('processed_data.csv', index=False)
    print("Arquivo processed_data.csv gerado com sucesso.")
    
    # Validação
    print("\nResumo Polimixina B (Registros Únicos):")
    print(processed[processed['Antimicrobiano'] == 'Polimixina B']['Sensibilidade'].value_counts())
    
    print("\nVerificação de duplicatas residuais (deve ser 0):")
    print(processed.duplicated(subset=['Código da O.S.', 'Microrganismo', 'Antimicrobiano']).sum())
