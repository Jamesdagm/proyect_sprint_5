import pandas as pd
import streamlit as st
import plotly_express as px

# Cargar el conjunto de datos
df = pd.read_csv("vehicles_us.csv")

# Mostrar encabezado usando st.header
st.header("Datos del conjunto de vehículos")

# Mostrar tabla con todos los datos
st.write("Tabla de datos:")
st.write(df)

# Crear un botón para construir un histograma (tipos de vehículo por marca)
if st.button("Construir Histograma"):
    # Usar plotly_express para crear un histograma
    fig_histogram = px.histogram(df, x="make", color="vehicleType", title="Histograma: Tipos de vehículo por marca")
    # Mostrar el gráfico usando st.plotly_chart
    st.plotly_chart(fig_histogram)

# Crear un botón para construir un gráfico de dispersión usando plotly_express
if st.button("Construir Gráfico de Dispersión"):
    # Usar plotly_express para crear un gráfico de dispersión
    fig_scatter = px.scatter(df, x="mileage", y="price", color="make", title="Gráfico de Dispersión: Millaje vs Precio por Marca")
    # Mostrar el gráfico usando st.plotly_chart
    st.plotly_chart(fig_scatter)

    # Mostrar el histograma utilizando st.plotly_chart()
    st.plotly_chart(fig)

# Botón para construir un gráfico de dispersión al hacer clic
if st.button('Mostrar Gráfico de Dispersión'):
    # Construir el gráfico de dispersión utilizando plotly-express
    fig_scatter = px.scatter(df, x='odometer', y='price', title='Gráfico de Dispersión')

    # Mostrar el gráfico de dispersión utilizando st.plotly_chart()
    st.plotly_chart(fig_scatter)
    