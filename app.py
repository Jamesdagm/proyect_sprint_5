import streamlit as st
import pandas as pd
import plotly_express as px

# Leer el archivo CSV en un DataFrame
df = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('Cuadro de Mandos de la Aplicación Web')

# Mostrar una tabla con los primeros 5 registros del DataFrame
st.subheader('Primeros 5 Registros del DataFrame:')
st.write(df.head())

# Botón para construir un histograma al hacer clic
if st.button('Mostrar Histograma de Precios'):
    # Construir el histograma utilizando plotly-express
    fig = px.histogram(df, x='price', title='Histograma de Precios')

    # Mostrar el histograma utilizando st.plotly_chart()
    st.plotly_chart(fig)

# Botón para construir un gráfico de dispersión al hacer clic
if st.button('Mostrar Gráfico de Dispersión'):
    # Construir el gráfico de dispersión utilizando plotly-express
    fig_scatter = px.scatter(df, x='odometer', y='price', title='Gráfico de Dispersión')

    # Mostrar el gráfico de dispersión utilizando st.plotly_chart()
    st.plotly_chart(fig_scatter)
    