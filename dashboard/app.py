
import streamlit as st
import pandas as pd
import sqlite3


# Conectar ao banco de dados SQLite
conn = sqlite3.connect ('data/bd_mercadolivre.db')

# Carregar os dados da tabela mercadolivreitens em um Dataframe pandas
df = pd.read_sql('select * from mercadolivreitens', conn)

# Fechar a conexao com o banco de dados
conn.close()

# Titulo da Aplicacao
st.set_page_config(layout="wide")
st.title ('Pesquisa de Mercado de Tenis Esportivo Masculino no ML')

# Exibir a tabela do Dataframe
st.subheader ('Tabela de Itens do Mercado Livre - (Tenis Masculino)')
st.write(df)

# Criando colunas
col1, col2, col3 = st.columns(3)


# Melhorar o layout com colunas para KPIs
st.subheader ('KPIs Principais da Pagina do Sistema')

# KPI1 : Numero total de itens
total_itens = df.shape[0]
col1.metric (label='Numero Total de Itens', value=total_itens)

# KPI2:  Total de Marcas 
total_marcas = df['brand'].nunique()
col2.metric(label='Numero de Marcas Únicas', value=total_marcas)

# KPI3: Preço Medio novo (em reais)
preco_medio = df['preco_total'].mean()
col3.metric (label='Preço Médio Novo (R$)', value=f"{preco_medio:.2f}")

# Quais marcas sao mais encontradas ate a pagina 20
st.subheader ('Marcas mais encontradas até a 20a página')
col1, col2 = st.columns ([4,2])

top_10pag = df['brand'].value_counts().sort_values(ascending=False).head(10)

col1.bar_chart(top_10pag)
col2.write(top_10pag)

# Preco Medio por Marca

st.subheader ('Preço Médio por Marca')
col1, col2 = st.columns ([4,2])

media_preco = df.groupby('brand')['preco_total'].mean().sort_values(ascending=False).head(10)
col1.bar_chart(media_preco)
col2.write(media_preco)

# Qual a satisfacao total po rMarca
st.subheader ('Satisfacao por Marca')
col1, col2 = st.columns ([4,2])
df_avaliados = df[df['avaliacao'] > 0]
satisfacao = df_avaliados.groupby('brand')['avaliacao'].mean().sort_values(ascending=False).head(10)
col1.bar_chart(satisfacao)
col2.write(satisfacao)