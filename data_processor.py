import pandas as pd
import re

def extract_polymyxin_data(row):
    """Extrai a sensibilidade à Polimixina B da coluna 'Observações do isolado'."""
    obs = str(row['Observações do isolado'])
    # Regex flexível para capturar Sensível, Resistente ou Intermediário
    match = re.search(r'Polimixina B \(MIC\): [^ -]+ - (Sensível|Resistente|Intermediário)', obs, re.IGNORECASE)
    if match:
        return match.group(1).capitalize()
    return None

def process_data(file_path):
    """Carrega, processa e limpa os dados da planilha."""
    print("Carregando dados...")
    df = pd.read_excel(file_path)

    # 1. Limpeza e padronização de colunas
    df = df.rename(columns={'Resultado': 'Microrganismo', 'Unidade de coleta': 'Setor', 'Classificação': 'Sensibilidade'})
    
    # 2. Remoção de resultados negativos
    df_pos = df[~df['Microrganismo'].str.contains('NEGATIVA|Negativa', na=False, case=False)].copy()
    
    # 3. Limpeza do nome do microrganismo (removendo ~ e pontos finais)
    df_pos['Microrganismo'] = df_pos['Microrganismo'].str.replace('~', '', regex=False).str.strip()
    df_pos['Microrganismo'] = df_pos['Microrganismo'].str.replace(r'\.+$', '', regex=True).str.strip() # Remove um ou mais pontos no final
    
    # 4. Extração da sensibilidade à Polimixina B
    print("Extraindo dados de Polimixina B da coluna de observações...")
    # Identificar isolados que possuem a informação de Polimixina nas observações
    mask_poli = df_pos['Observações do isolado'].str.contains('Polimixina B', na=False, case=False)
    df_with_poli = df_pos[mask_poli].copy()
    
    # Extrair o status (Sensível/Resistente)
    df_with_poli['Sensibilidade_Polimixina'] = df_with_poli.apply(extract_polymyxin_data, axis=1)
    
    # Filtrar apenas onde a extração funcionou
    df_poli_extracted = df_with_poli.dropna(subset=['Sensibilidade_Polimixina']).copy()
    
    # Criar novas linhas específicas para o antibiótico Polimixina B
    # Importante: Fazemos isso para que a Polimixina apareça como um "Antimicrobiano" no dashboard
    polimixina_rows = df_poli_extracted.copy()
    polimixina_rows['Antimicrobiano'] = 'Polimixina B'
    polimixina_rows['Sensibilidade'] = polimixina_rows['Sensibilidade_Polimixina']
    
    # 5. Combinar os dados originais com as novas linhas de Polimixina B
    # Removemos qualquer Polimixina B que já possa existir na coluna Antimicrobiano para evitar duplicidade
    df_pos = df_pos[df_pos['Antimicrobiano'] != 'Polimixina B']
    df_final = pd.concat([df_pos, polimixina_rows], ignore_index=True)
    
    # 6. Limpeza final de colunas
    cols_to_keep = ['Código da O.S.', 'Data da O.S.', 'Setor', 'Material', 'Microrganismo', 'Antimicrobiano', 'Sensibilidade']
    df_final = df_final[cols_to_keep]
    
    # 7. Limpeza de Antimicrobiano
    df_final = df_final.dropna(subset=['Antimicrobiano'])
    df_final['Antimicrobiano'] = df_final['Antimicrobiano'].str.strip()

    print(f"Dados processados. Total de linhas: {len(df_final)}")
    return df_final

if __name__ == '__main__':
    processed_df = process_data('/home/ubuntu/upload/HCL2025.xlsx')
    processed_df.to_csv('processed_data.csv', index=False)
    print("Dados salvos em processed_data.csv")
    
    # Verificação de integridade
    print("\nContagem de Polimixina B extraída:")
    print(processed_df[processed_df['Antimicrobiano'] == 'Polimixina B']['Sensibilidade'].value_counts())
    
    print("\nTop 5 Microrganismos (Verificar limpeza de nomes):")
    print(processed_df['Microrganismo'].value_counts().head(5))
