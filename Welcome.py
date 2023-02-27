import streamlit as st
import os
from PIL import Image

st.title('Welcome to the World of', anchor=None)
st.markdown("<h1 style='color: #ed53ce; padding-top:0;'>Lashika Arunachalam</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='padding-top:0;'>Data Science Intern @Innomatics Research Labs</h3>", unsafe_allow_html=True)


image=Image.open('pic.png')
style = '<style>img{border: 2px solid None; padding: 10px; border-radius: 50%; margin-left: 550px; margin-top: 0px;}</style>'
st.markdown(style, unsafe_allow_html=True)
st.image(image, caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


st.markdown("<h1 style='font-size:20px;padding-top:0;'>LinkedIn:</h1>", unsafe_allow_html=True)
url = 'https://www.linkedin.com/in/lashika-arunachalam/'
link = f'<a href="{url}" target="_blank">Lashika Arunachalam</a>'
st.markdown(link, unsafe_allow_html=True)

st.snow()
