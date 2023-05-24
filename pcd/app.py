# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json

import requests  # pip install requests
from streamlit_lottie import st_lottie  # pip install streamlit-lotti
import streamlit as st
from st_pages import Page, add_page_title, show_pages
import webbrowser

# Set page config
st.set_page_config(
    page_title="Seed classifier",
    page_icon=":watermelon:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

container = st.container()
container.width = 800
with st.container():
    col1, col2 = st.columns([1.25, 1.1])
    with col1:
        container1= st.container()
        container1.title("Welcome to Seed Classifier!")
        container1.write("Classify watermelon  seeds  with our model.This app was Monitored by Limagrain group")
        container2= st.container()
        col11, col22,col33 = st.columns([1,1,1])
        with col11:
            st.write(" ");
        with col22:
            if st.button("Start", key="my_button"):
                webbrowser.open_new_tab('http://localhost:8501/%20Watermelon%20classifier')
        with col33 :
            st.write(" ")
       
    with col2:
        lottie_hello = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_8wpitnly.json") 
        st_lottie(lottie_hello, height=600,width=600,key=None,)     
# with st.container():
#     col1, col2,col3,col4,col5 = st.columns([1,1,1,1,1])
#     with col1:
#         st.image('logo.png', width=100)
#     with col2 :
#         st.image('vilmo.png', width=100)

# Add pages using st_pages
show_pages(
    [
        Page("app.py", " Home", "🏠"),
        # Can use :<icon-name>: or the actual icon
        Page("watermelon.py", " Watermelon classifier", ":watermelon:"),
        Page("aboutus.py", " About Us", ":?:"),
    ]
)




