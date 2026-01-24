import pandas as pd
import re

def extract_polymyxin_data(row):
    """Extrai a sensibilidade à Polimixina B da coluna 'Observações do isolado'."""
    obs = str(row['Observações do isolado'])
    match = re.search(r'Polimixina B \(MIC\): [^ -]+ - (Sensível|Resistente|Intermediário)\.', obs, re.IGNORECASE)
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
    
    # 3. Limpeza do nome do microrganismo (removendo ~)
    df_pos['Microrganismo'] = df_pos['Microrganismo'].str.replace('~', '', regex=False).str.strip()
    
    # 4. Extração da sensibilidade à Polimixina B
    print("Extraindo dados de Polimixina B...")
    df_polimixina = df_pos[df_pos['Observações do isolado'].str.contains('Polimixina B', na=False, case=False)].copy()
    df_polimixina['Sensibilidade_Polimixina'] = df_polimixina.apply(extract_polymyxin_data, axis=1)
    
    # 5. Filtrar apenas as linhas onde a extração da Polimixina foi bem-sucedida
    df_polimixina = df_polimixina.dropna(subset=['Sensibilidade_Polimixina'])
    
    # 6. Criar novas linhas para Polimixina B
    polimixina_rows = df_polimixina.copy()
    polimixina_rows['Antimicrobiano'] = 'Polimixina B'
    polimixina_rows['Sensibilidade'] = polimixina_rows['Sensibilidade_Polimixina']
    
    # 7. Combinar os dados originais com as novas linhas de Polimixina B
    df_final = pd.concat([df_pos, polimixina_rows], ignore_index=True)
    
    # 8. Limpeza final de colunas
    cols_to_keep = ['Código da O.S.', 'Data da O.S.', 'Setor', 'Material', 'Microrganismo', 'Antimicrobiano', 'Sensibilidade', 'Observações do isolado']
    df_final = df_final[cols_to_keep]
    
    # 9. Extração de Mecanismos de Resistência (para o segundo mapa de calor)
    mecanismos = ['KPC', 'NDM', 'OXA', 'VIM', 'IMP', 'ESBL', 'MRSA', 'VRE']
    for mec in mecanismos:
        # Usar uma regex mais robusta para capturar o resultado do teste (Positivo/Negativo)
        # Exemplo: Teste NG Carba ? KPC: Negativo
        df_final[mec] = df_final['Observações do isolado'].apply(
            lambda x: 'Positivo' if re.search(rf'{mec}: Positivo', str(x), re.IGNORECASE) else 
                      ('Negativo' if re.search(rf'{mec}: Negativo', str(x), re.IGNORECASE) else None)
        )

    # 10. Limpeza de Antimicrobiano
    df_final = df_final.dropna(subset=['Antimicrobiano'])
    df_final['Antimicrobiano'] = df_final['Antimicrobiano'].str.strip()

    print(f"Dados processados. Total de linhas: {len(df_final)}")
    return df_final

if __name__ == '__main__':
    processed_df = process_data('/home/ubuntu/upload/HCL2025.xlsx')
    processed_df.to_csv('processed_data.csv', index=False)
    print("Dados salvos em processed_data.csv")
    
    # Verificação rápida
    print("\nVerificação rápida - Polimixina B:")
    print(processed_df[processed_df['Antimicrobiano'] == 'Polimixina B']['Sensibilidade'].value_counts())
    print("\nVerificação rápida - Mecanismos de Resistência (KPC):")
    print(processed_df['KPC'].value_counts(dropna=False))
