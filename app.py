# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
from PIL import Image
import requests  
from streamlit_lottie import st_lottie  
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


    
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
   

container = st.container()
container.width = 800
with st.container():
    col1, col2 = st.columns([1.3, 1.5])
    with col1:
        container1= st.container()
        container1.title("Welcome to Seed Classifier!")
        container1.write("Classify watermelon  seeds  with our model.Project Monitored by Limagrain group")
        container2= st.container()
        col11, col22,col33 = st.columns([1,1,0.5])
        with col11:
            st.write(" ");
        with col22:
            if st.button("Start", key="my_button"):
                webbrowser.open_new_tab('http://localhost:8501/%20Watermelon%20classifier')
        with col33 :
            st.write(" ")
       
    with col2:
        lottie_hello = load_lottiefile ("watermelon.json") 
        st_lottie(lottie_hello, height=600,width=600,key=None,)     

show_pages(
    [Page("app.py", " Home", "🏠"), Page("watermelon.py", " Watermelon classifier", ":watermelon:"), Page("aboutus.py", " About Us", ":?:"),])


