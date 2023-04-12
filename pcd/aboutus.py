# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:38:52 2023

@author: asus
"""
import json

import requests  # pip install requests
from streamlit_lottie import st_lottie  # pip install streamlit-lotti
import streamlit as st
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
    col1, col2,col3 = st.columns([1, 2,1])
    with col2:
        container1= st.container()
        container1.title("About us") 
        lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_f2jo61ci.json")  
        st_lottie(lottie_hello, height=600,width=600,key=None,)
 
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)