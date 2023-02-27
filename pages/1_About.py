import streamlit as st
import os
from PIL import Image

st.title('Lets know about me and Data!', anchor=None)
st.markdown("<h4 style='padding-top:0;'>I am currently doing my Master in Data Science with the modules od Data Visualization, Machine Learning, Deep Learning, Mathematics for Data Science, Data Analytics and Applications for Data Science.</h4>", unsafe_allow_html=True)

st.markdown("<h4 style='padding-top:0;'>I am happy to be part of Data Science Intern at Innomatics Research Lab. </h4>", unsafe_allow_html=True)

st.markdown("<h4 style='color: green;padding-top:0;'>What's Data Science?</h4>", unsafe_allow_html=True)
st.markdown("<h5 style='padding-top:0;'>Data science is the domain of study that deals with vast volumes of data using modern tools and techniques to find unseen patterns, derive meaningful information, and make business decisions. Data science uses complex machine learning algorithms to build predictive models.</h5>", unsafe_allow_html=True)
st.markdown("<h4 style='color: green;padding-top:0;'>What's Machine Learning?</h4>", unsafe_allow_html=True)
st.markdown("<h5 style='padding-top:0;'>Machine learning is a subfield of artificial intelligence, which is broadly defined as the capability of a machine to imitate intelligent human behavior. Artificial intelligence systems are used to perform complex tasks in a way that is similar to how humans solve problems.</h5>", unsafe_allow_html=True)
st.markdown("<h4 style='color: green;padding-top:0;'>What's Data Analytics?</h4>", unsafe_allow_html=True)
st.markdown("<h5 style='padding-top:0;'>Data analytics is the pursuit of extracting meaning from raw data using specialized computer systems. These systems transform, organize, and model the data to draw conclusions and identify patterns.</h5>", unsafe_allow_html=True)


image=Image.open('datascience.png')
style = '<style>img{border: 2px solid None; padding: 10px; border-radius: 20%; margin-left: 200px; margin-top: 0px;}</style>'
st.markdown(style, unsafe_allow_html=True)
st.image(image, caption=None, width=300, use_column_width=None, clamp=False, channels="RGB", output_format="auto")


st.balloons()