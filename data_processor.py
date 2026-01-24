import pandas as pd
import re

def extract_polymyxin_data(row):
    """Extrai a sensibilidade à Polimixina B da coluna 'Observações do isolado'."""
    obs = str(row['Observações do isolado'])
    # Busca por Polimixina B seguida de Sensível ou Resistente
    if 'Polimixina B' in obs:
        if 'Sensível' in obs:
            return 'Sensível'
        elif 'Resistente' in obs:
            return 'Resistente'
    return None

def process_data(file_path):
    """Carrega, processa e limpa os dados da planilha."""
    print("Carregando dados...")
    df = pd.read_excel(file_path)

    # 1. Padronização de colunas
    df = df.rename(columns={'Resultado': 'Microrganismo', 'Unidade de coleta': 'Setor', 'Classificação': 'Sensibilidade'})
    
    # 2. Remoção de resultados negativos
    df_pos = df[~df['Microrganismo'].str.contains('NEGATIVA|Negativa', na=False, case=False)].copy()
    
    # 3. Limpeza do nome do microrganismo (removendo ~ e pontos finais duplicados)
    df_pos['Microrganismo'] = df_pos['Microrganismo'].str.replace('~', '', regex=False).str.strip()
    df_pos['Microrganismo'] = df_pos['Microrganismo'].str.replace(r'\.+$', '', regex=True).str.strip()
    
    # 4. Extração da Polimixina B
    print("Extraindo Polimixina B das observações...")
    # Criamos um dataframe apenas com quem tem Polimixina nas observações
    df_poli = df_pos[df_pos['Observações do isolado'].str.contains('Polimixina B', na=False, case=False)].copy()
    df_poli['Sensibilidade_Extraida'] = df_poli.apply(extract_polymyxin_data, axis=1)
    
    # Filtramos apenas onde conseguimos extrair o status
    df_poli = df_poli.dropna(subset=['Sensibilidade_Extraida'])
    
    # Criamos as novas linhas de Polimixina B
    poli_rows = df_poli.copy()
    poli_rows['Antimicrobiano'] = 'Polimixina B'
    poli_rows['Sensibilidade'] = poli_rows['Sensibilidade_Extraida']
    
    # 5. Combinar dados
    # Removemos qualquer Polimixina B que já exista na coluna Antimicrobiano para não duplicar
    df_pos = df_pos[df_pos['Antimicrobiano'] != 'Polimixina B']
    df_final = pd.concat([df_pos, poli_rows], ignore_index=True)
    
    # 6. Seleção de colunas finais
    cols = ['Código da O.S.', 'Data da O.S.', 'Setor', 'Material', 'Microrganismo', 'Antimicrobiano', 'Sensibilidade']
    df_final = df_final[cols].dropna(subset=['Antimicrobiano'])
    df_final['Antimicrobiano'] = df_final['Antimicrobiano'].str.strip()

    print(f"Processamento concluído. Total de registros: {len(df_final)}")
    return df_final

if __name__ == '__main__':
    processed = process_data('/home/ubuntu/upload/HCL2025.xlsx')
    processed.to_csv('processed_data.csv', index=False)
    print("Arquivo processed_data.csv gerado com sucesso.")
    
    # Validação final
    print("\nResumo Polimixina B:")
    print(processed[processed['Antimicrobiano'] == 'Polimixina B']['Sensibilidade'].value_counts())
