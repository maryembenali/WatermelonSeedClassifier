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


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

container = st.container()
container.width = 800
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        container1 = st.container()
        container1.title("About us")
        lottie_hello = load_lottiefile("bye.json")
        st_lottie(lottie_hello, height=500, width=500, key=None,)
        container1.write("This project was done by a group of 2nd year engineering students at ENSI as a part of an end-of-year academic project. The team is composed of [Akrem Ben Mbarek](https://www.linkedin.com/in/akrem-ben-mbarek-4358bb252), [Maryem Ben Ali](https://www.linkedin.com/in/maryem-ben-ali-947491222/), and [Nour Wanis](https://www.facebook.com/).")

hide_st_style = """ <style>footer {visibility: hidden;}</style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)
