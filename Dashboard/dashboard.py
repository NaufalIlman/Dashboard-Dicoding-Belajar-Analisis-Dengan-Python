import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard Bike Sharing Dataset")

from PIL import Image
image = Image.open('Dashboard/clemsonbikeshare.jpg')

st.image(image, caption='~')

data_day = pd.read_csv("Data/day.csv")


st.markdown('Halaman ini menampilkan sejumlah visualisasi dan bagan dari data bike sharing')
#sidebar
st.sidebar.title('Tampilan Menu Dashboard')

#checkbox to show data 
if st.checkbox("Show Data"):
    st.write(data_day.head())

#checkbox to show data 
if st.checkbox("Show Descriptive Analysis"):
    st.write(data_day.describe())


#selectbox + visualisation

# Multiple widgets of the same type may not share the same key.
select=st.sidebar.selectbox('pilih jenis grafik',['Histogram','Pie Chart'],key=0)
st.markdown("###  Jumlah Penyewa Berdasarkan Cuaca")

if select == "Histogram":
        fig = px.bar(data_day, x='weathersit', y='cnt', color = 'cnt', height= 500)
        st.plotly_chart(fig)
else:
        fig = px.pie(data_day, values='cnt', names='weathersit')
        st.plotly_chart(fig)

st.text("weathersit:") 
st.text("1: Clear, Few clouds, Partly cloudy, Partly cloudy")
st.text("2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist")
st.text("3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds")
st.text("4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog)")

select2=st.sidebar.selectbox('pilih jenis grafik',['Histogram','Pie Chart'],key=1)
st.markdown("###  Jumlah Penyewa Berdasarkan musim")

if select2 == "Histogram":
        fig = px.bar(data_day, x='season', y='cnt', color = 'cnt', height= 500)
        st.plotly_chart(fig)
else:
        fig = px.pie(data_day, values='cnt', names='season')
        st.plotly_chart(fig)

st.text("season:") 
st.text("1: springer")
st.text("2: summer")
st.text("3: Fall")
st.text("4: Winter")

select3=st.sidebar.selectbox('pilih jenis grafik',['Histogram','Pie Chart'],key=2)
st.markdown("###  Jumlah Penyewa Berdasarkan hari")

if select3 == "Histogram":
        fig = px.bar(data_day, x='weekday', y='cnt', color = 'cnt', height= 500)
        st.plotly_chart(fig)
else:
        fig = px.pie(data_day, values='cnt', names='weekday')
        st.plotly_chart(fig)

st.text("Day:") 
st.text("0: Sunday")
st.text("1: Monday")
st.text("2: Tuesday")
st.text("3: Wednesday")
st.text("4: Thursday")
st.text("1: Friday")
st.text("2: Saturday")

st.sidebar.header('About Us')
st.sidebar.markdown('Created by Muhammad Naufal Ilman')
