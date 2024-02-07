import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV en un DataFrame
df = pd.read_csv('vehicles_us.csv')

# Configurar la aplicación Streamlit
st.title('Explorador de Datos de Vehículos')

# Mostrar el DataFrame en Streamlit
st.header('Conjunto de Datos de Vehículos')
st.write(df)


# Botón para construir un histograma (condition vs model_year)
if st.button('Histograma (Condición vs Modelo-Año)'):
    # Construir y mostrar el histograma usando Plotly Express
    fig_condition = px.histogram(df, x='model_year', color='condition', title='Histograma (Condition vs Model Year)')
    st.plotly_chart(fig_condition)

# Botón para construir un gráfico de dispersión
if st.button('Gráfico de Dispersión (Odómetro Vs Precio Vehículos)'):
    # Construir y mostrar el gráfico de dispersión usando Plotly Express
    fig_scatter = px.scatter(df, x='Odómetro', y='price', color='fuel', title='Odómetro Vs Precio Vehículos')
    st.plotly_chart(fig_scatter)