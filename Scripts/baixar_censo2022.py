import basedosdados as bd
import pandas as pd

billing_id = "projeto-fgv-emap"

query = """
  SELECT
    dados.id_municipio AS id_municipio,
    diretorio_id_municipio.nome AS id_municipio_nome,
    SUM(dados.populacao) AS populacao_total
  FROM `basedosdados.br_ibge_censo_2022.alfabetizacao_grupo_idade_sexo_raca` AS dados
  LEFT JOIN (
      SELECT DISTINCT id_municipio, nome  
      FROM `basedosdados.br_bd_diretorios_brasil.municipio`
  ) AS diretorio_id_municipio
    ON dados.id_municipio = diretorio_id_municipio.id_municipio
  GROUP BY 
    dados.id_municipio, 
    diretorio_id_municipio.nome
"""

print("A descarregar os dados do Censo 2022 da Base dos Dados...")
tabela_censo = bd.read_sql(query = query, billing_project_id = billing_id)

print("A converter para CSV...")
tabela_censo.to_csv("Populacao_Censo_2022.csv", index=False, encoding='utf-8-sig', sep=';')

print(f"Sucesso! Ficheiro salvo com {len(tabela_censo)} linhas prontas para o cruzamento.")