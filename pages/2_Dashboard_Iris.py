import streamlit as st
import os
from matplotlib import image
import pandas as pd
import plotly.express as px

file = os.path.dirname(os.path.abspath(__file__))
main = os.path.join(file, os.pardir)
interest = os.path.join(main, "resources")
img = os.path.join(interest, "images", "iris.jpg")
data = os.path.join(interest, "data", "iris.csv")

st.title("Dashboard - Iris Data")

img = image.imread(img)
st.image(img)

df = pd.read_csv(data)
st.dataframe(df)

species = st.selectbox("Species:", df['Species'].unique())


fig_1 = px.histogram(df[df['Species'] == species], x="SepalLengthCm")
st.plotly_chart(fig_1, use_container_width=True)
