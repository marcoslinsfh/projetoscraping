import pandas as pd
import sqlite3
from datetime import datetime
import io


arq ='data/data.jsonl'
df = pd.read_json (arq, lines=True)

# Adicionando colunas no Dataframe

df['source'] = 'https://lista.mercadolivre.com.br/tenis-corrida-masculino' 
df['dt_coleta'] = datetime.now()

# Setar o pandas par amostrar todas as colunas
pd.options.display.max_columns

# Tratandos os valores nulos das colunas numericas e de texto
df['avaliacao'] = df['avaliacao'].fillna(0).astype(float)
df['preco_antes'] = df['preco_antes'].fillna(0).astype(float)
df['preco'] = df['preco'].fillna(0).astype(float)
df['preco_antes_cents'] = df['preco_antes_cents'].fillna(0).astype(float)
df['preco_cents'] = df['preco_cents'].fillna(0).astype(float)

# Remover parenteses do campo avaliacao

df['qtd_avaliacao'] = df['qtd_avaliacao'].str.replace('[\(\)]', '', regex=True)
df['qtd_avaliacao'] = df['qtd_avaliacao'].fillna(0).astype(int)

# Tratar os precos e centavos dos precos novos e anteriores
df['preco_total'] = df['preco'] + df['preco_cents']/ 100
df['preco_total_antes'] = df['preco_antes'] + df['preco_antes_cents']/100

# Preencher as linhas NULL das colunas Anunciante, Promocao e Frete e realizar outras transformacoes

df['anunciante'] = df['anunciante'].str.replace('por ', '').fillna('Nao Informado')
df['promocao'] = df['promocao'].fillna('Sem Promocao')
df['frete'] = df['frete'].fillna('Frete Pago')

df = df.drop (columns=['preco', 'preco_antes', 'preco_cents', 'preco_antes_cents'])

# Conectar com o banco de dados SQLite

conn = sqlite3.connect('data/bd_mercadolivre.db')

# Salvando o Dataframe no banco de dados SQLite
df.to_sql ('mercadolivreitens', conn, if_exists='replace', index=False)

# Fechando a conexao com o SQLite

conn.close()



              