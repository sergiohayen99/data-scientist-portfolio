import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header("Página de ventas de vehículos")

graph_button = st.button("Gráfica de barras sobre el modelo de los vehículos")

if graph_button:
    st.write("Creación de una gráfica de barras para el conjunto de datos de anuncios de venta de coches sobre el modelo de los vehículos")
    bar1 = px.bar(car_data, x = "model", y = "count", title = "Modelo", labels = {"model":"Modelo"})
    st.plotly_chart(bar1, use_container_width=True)

graph_button = st.button("Gráfica de barras sobre el año del modelo de los vehículos")

if graph_button:
    st.write("Creación de una gráfica de barras para el conjunto de datos de anuncios de venta de coches sobre el año del modelo de los vehículos")
    bar2 = px.bar(car_data, x = "model_year", y = "count", title = "Año del modelo", labels = {"model_year":"Año"})
    st.plotly_chart(bar2, use_container_width=True)

graph_button = st.button("Gráfica de barras sobre la condición en la que se encuentra cada vehículo")

if graph_button:
    st.write("Creación de una gráfica de barras para el conjunto de datos de anuncios de venta de coches sobre la condición en la que se encuentra cada vehículo")
    bar3 = px.bar(car_data, x = "condition", y = "count", title = "Condición del vehículo", labels = {"condition":"Condición"})
    st.plotly_chart(bar3, use_container_width=True)

graph_button = st.button("Gráfica de barras sobre número de cilindros de los vehículos")

if graph_button:
    st.write("Creación de una gráfica de barras para el conjunto de datos de anuncios de venta de coches sobre el número de cilindros de los vehículos")
    bar4 = px.bar(car_data, x = "cylinders", y = "count", title = "Número de cilindros", labels = {"cylinders":"No. Cilindros"})
    st.plotly_chart(bar4, use_container_width=True)

graph_button = st.button("Gráfica de barras sobre el tipo de combustible que utiliza cada vehículo")

if graph_button:
    st.write("Creación de una gráfica de barras para el conjunto de datos de anuncios de venta de coches sobre el tipo de combustible que utiliza cada vehículo")
    bar5 = px.bar(car_data, x = "fuel", y = "count", title = "Tipo de combustible", labels = {"fuel":"Combustible"})
    st.plotly_chart(bar5, use_container_width=True)

graph_button = st.button("Gráfica de barras sobre el tipo de transmisión de cada vehículo")

if graph_button:
    st.write("Creación de una gráfica de barras para el conjunto de datos de anuncios de venta de coches sobre el tipo de transmisión de cada vehículo")
    bar6 = px.bar(car_data, x = "transmission", y = "count", title = "Tipo de transmisión", labels = {"transmission":"Transmisión"})
    st.plotly_chart(bar6, use_container_width=True)

graph_button = st.button("Gráfica de barras sobre el tipo de vehículo")

if graph_button:
    st.write("Creación de una gráfica de barras para el conjunto de datos de anuncios de venta de coches sobre el tipo de vehículo")
    bar7 = px.bar(car_data, x = "type", y = "count", title = "Tipo de vehículo", labels = {"type":"Tipo de vehículo"})
    st.plotly_chart(bar7, use_container_width=True)

graph_button = st.button("Gráfica de barras sobre el color de los vehículos")

if graph_button:
    st.write("Creación de una gráfica de barras para el conjunto de datos de anuncios de venta de coches sobre color de los vehículos")
    bar8 = px.bar(car_data, x = "paint_color", y = "count", title = "Color del vehículo", labels = {"paint_color":"Color"})
    st.plotly_chart(bar8, use_container_width=True)

graph_button = st.button("Histograma de los precios de los vehículos")

if graph_button:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches sobre los precios de los vehículos")
    hist1 = px.hist(car_data, x = "price", title = "Precio del vehículo", labels = {"price":"Precio"})
    st.plotly_chart(hist1, use_container_width=True)

graph_button = st.button("Histograma de la cantidad de millas recorridas de los vehículos")

if graph_button:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches sobre la cantidad de millas recorridas de los vehículos")
    hist2 = px.hist(car_data, x = "odometer", title = "Nivel del odómetro", labels = {"odometer","Odómetro"})
    st.plotly_chart(hist2, use_container_width=True)

graph_button = st.button("Histograma del tiempo que lleva el vehículo en la lista")

if graph_button:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches sobre el tiempo que lleva el vehículo en la lista")
    hist3 = px.hist(car_data, "days_listed", title = "Número de dias en la lista", labels = {"days_kisted":"No. días"})
    st.plotly_chart(hist3, use_container_width=True)

graph_button = st.button("Gráfico de dispersión entre el precio y el año del modelo de los vehículos")

if graph_button:
    st.write("Creación de una gráfica de dispersión para el conjunto de datos de anuncios de venta de coches entre el precio y el año del modelo del vehículo")
    scatter1 = px.scatter(car_data, x = "year", y = "price", title = "Comparativa entre el año del modelo y el precio de los vehículos")
    st.plotly_chart(scatter1, use_container_width=True)

graph_button = st.button("Gráfico de dispersión entre el precio y el nivel del odómetro de los vehículos")

if graph_button:
    st.write("Creación de una gráfica de dispersión para el conjunto de datos de anuncios de venta de coches entre el precio y el nivel del odómetro de los vehículos")
    scatter2 = px.scatter(car_data, x = "odometer", y = "price", title = "Comparativa entre nivel del odómetro y el odómetro de los vehículos")
    st.plotly_chart(scatter2, use_container_width=True)

graph_button = st.button("Gráfico de dispersión entre el precio y el número de días que el vehículo ha estado en la lista")

if graph_button:
    st.write("Creación de una gráfica de dispersión para el conjunto de datos de anuncios de venta de coches entre el precio y el número de días que el vehículo ha estado en la lista")
    scatter3 = px.scatter(car_data, x = "days_listed", y = "price", title = "Comparativa entre el numero de días en la lista y el número de días en la lista")
    st.plotly_chart(scatter3, use_container_width=True)