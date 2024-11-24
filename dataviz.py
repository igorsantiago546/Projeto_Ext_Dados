import streamlit as st
import seaborn as sns
import pandas as pd
# from sqlalchemy import create_engine 
import sqlite3 as sql

#def database():
 #cursor = conn.cursor()
  #  consulta = cursor.execute('SELECT * FROM dados')
   # return consulta

##engine = create_engine('sqlite:///banco.db', echo=True)

#def carregar_dados():
    #engine = create_engine('sqlite:///banco.db')
    #query = 'SELECT * FROM dados'
    #df = pd.read_sql(query, con=engine)
    #return df 

#df_lido = database()
    
st.write('**APP Informática**')
st.sidebar.header('Escolha o Hardware')

df = pd.read_csv('./basestratadas/Dados_tratados.csv', sep=',', encoding='utf-8')

categoria = df['Categoria'].drop_duplicates()
categoria_escolhido = st.sidebar.selectbox('Selecione uma catgoria', categoria)

df2 = df.loc[df['Categoria']==categoria_escolhido]
st.write(f'Categoria escolhida: {categoria_escolhido}')
st.write(f'Preços por componente')

#fig = px.box(df2, x='Preço')
#st.plotly_chart(fig)

#fig2 = px.pie(df2, 'Preço')
#st.plotly_chart(fig2)

#fig3 = px.bar(
 #   df2,
  #  x="Produto",
   # y="Preço",
   # title="Gráfico de Barras",
   # labels={"Produto": "Produtos", "Preço": "Preços"},
   # text="Preço",
   # color="Produto"
#)


#st.plotly_chart(fig3)


col1, col2, col3 = st.columns(3)
col1.metric("Média da categoria",value=df2.Preço.mean().round(2))
col2.metric("Mediana da categoria",value=df2.Preço.median().round(2))
col3.metric("Desvio Padrão da categoria",value=df2.Preço.std().round(2))