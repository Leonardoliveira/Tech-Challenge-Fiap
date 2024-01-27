import streamlit as st
import pandas as pd
import datetime
from PIL import Image
# import matplotlib.pyplot as plt


#Leitura e tratamento
df = pd.read_csv("df_forecast.csv", sep=",")
df['Data'] = pd.to_datetime(df['Data'])
df.set_index('Data', inplace=True)

#Criando Menu StreamLit
st.sidebar.title("Menu")
paginaSelecionada = st.sidebar.selectbox("Selecione a página", ["Visão Geral", "Previsões", "Nosso Time"])

#Leitura de imagem
imagem_local = Image.open("Logo.png")
# Exibir a imagem
st.image(imagem_local, use_column_width="Auto")

if paginaSelecionada == "Visão Geral":
    st.header("Visão Geral da previsão ao longo do ano:")

    st.line_chart(df, use_container_width=True)
    #Gráfico geral ao longo do tempo
    #plt.figure(figsize=(10, 5))
    #plt.plot(df.index, df['PrevisaoPreco'], label='Valores')
    #plt.title('Gráfico Estático da previsão de Valores ao Longo do Tempo')
    #plt.xlabel('Data')
    #plt.ylabel('PrevisaoPreco')
    #plt.legend()
    #st.pyplot(plt)

# Configuração do Menu Previsões
elif paginaSelecionada == "Previsões":
    #Criação de guias para diferenciar as pesquisas
    tab1, tab2= st.tabs(["Previsão por mês", "Previsão por data"])
    with tab1:
        col1, col2 = st.columns(2)
        # Separando as duas amostras para ficar lado a lado
        with col1:
            mes_selecionado = st.selectbox("Selecione um mês", range(2, 13))
            df_filtrado = df[df.index.month == mes_selecionado]
            st.dataframe(df_filtrado)
        with col2:
            st.bar_chart(df_filtrado, use_container_width=True)
    with tab2:
        #Seleciona a data e mostra o valor referente a mesma
        st.header("Para verificar a previsão de uma data específica:")
        data_selecionada = st.date_input("Selecione uma data de 01/02/2024 até 31/12/2024", value=None)
        data_pandas = pd.Timestamp(data_selecionada)
        #Trata exceção na pesquisa de datas que não estão no DataFrame
        if data_pandas in df.index:
            valor_correspondente = df.loc[data_pandas, 'PrevisaoPreco']
            st.write(valor_correspondente)
        else:
            st.write(f"A data {data_pandas} não está presente nas previsões.")

elif paginaSelecionada == "Nosso Time":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Fabricio Palacios")
        st.caption("linkedin.com/in/fabricio-palacios")

    with col2:
        st.header("Felipe dos Santos Lima")
        st.caption("linkedin.com/in/felipedossantoslima")

    with col3:
        st.header("Leonardo Oliveira")
        st.caption("linkedin.com/in/lb-de-oliveira")