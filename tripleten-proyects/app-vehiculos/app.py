import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header("Página de ventas de vehículos")

graph_button = st.button("Construir gráfica de barras")

if graph_button:
    st.write("Creación de una gráfica de barras para el conjunto de datos de anuncios de venta de coches sobre el modelo de los vehículos")
    bar1 = px.bar(car_data, x = "model", y = "count", title = "Modelo", xlabel = "Modelo")
    st.plotly_chart(bar1, use_container_width=True)

graph_button = st.button("Construir histograma")

if graph_button:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches sobre la cantidad de millas recorridas de los vehículos")
    hist2 = px.hist(car_data, x = "odometer", title = "Nivel del odómetro", xlabel = "Odómetro")
    st.plotly_chart(hist2, use_container_width=True)

graph_button = st.button("Construir gráfica de dispersión")

if graph_button:
    st.write("Creación de una gráfica de dispersión para el conjunto de datos de anuncios de venta de coches entre el precio y el año del modelo del vehículo")
    scatter1 = px.scatter(car_data, x = "year", y = "price", title = "Comparativa entre el año del modelo y el precio de los vehículos", xlabel = "Modelo", ylabel = "Precio")
    st.plotly_chart(scatter1, use_container_width=True)