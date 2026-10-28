import pandas as pd
import json

# Troque 'dados.json' pelo nome exato do arquivo que você baixou
arquivo_json = 'Transações Pix por Município.json' 
arquivo_csv = 'dados_pix.csv'

print("Lendo o arquivo JSON...")
with open(arquivo_json, 'r', encoding='utf-8') as f:
    dados = json.load(f)

# O Banco Central guarda as linhas da tabela dentro da chave 'value'
tabela = pd.DataFrame(dados['value'])

print("Convertendo para CSV...")
# Usamos sep=';' para que o Excel em português abra as colunas perfeitamente
tabela.to_csv(arquivo_csv, index=False, encoding='utf-8-sig', sep=';')

print("Sucesso! Arquivo convertido.")
