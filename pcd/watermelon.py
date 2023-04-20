# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 16:38:36 2023

@author: asus
"""


import streamlit as st
import pandas as pd
import plotly.express as px
import tensorflow as tf
from PIL import Image
import numpy as np



# Load the pre-trained model
model = tf.keras.models.load_model('C:\\Users\\lenovo\\model_AC(FinalVersion).h5')
ClassifyTest = False
# Define the results list
results = []
TetraSum= 1
TriSum=  1

# Set page config
st.set_page_config(
    page_title="Seed classifier",
    page_icon=":watermelon:",
    layout="wide",
    initial_sidebar_state="collapsed",
)
hide_st_style = """
            <style>
            footer {visibility: hidden;}
           
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Define container style
container_style = """
    background-color: #f2f2f2;
    border: 1px solid #e6e6e6;
    border-radius: 10px;
    padding: 10px;
    height: 300px;
    width: 500px;
"""

# Create first container with two columns
with st.container():
    col1, col2 = st.columns([1, 1])
    
    # Add upload file widget to first column
    with col1:
        st.write("# Classification")
        col11, col21 = st.columns([1, 1])
        with col11:
            uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True)
            if uploaded_files is not None:
                # Create a list to store the uploaded file data
                file_data = []
                # Loop over the uploaded files and process each one
                for uploaded_file in uploaded_files:
                    # Read the image data
                    img = Image.open(uploaded_file)
                    # Convert the image to a NumPy array
                    img_array = np.array(img)
                    resize= tf.image.resize(img_array,(256,256))
                    print(img_array.shape)
                    # Add the file data to the list
                    file_data.append({
                        'file_name': uploaded_file.name,'image_data': resize })

    
        # Add button to perform classification
        if st.button("Classify"):
            ClassifyTest=True
            if file_data:
                # Loop over the file data and make predictions for each image
                for data in file_data:
                    # Make a prediction using the pre-trained model
                    prediction = model.predict(np.expand_dims(data['image_data']/255,0))
                    # Get the predicted class label
                    class_label = '3n' if prediction[0][0] < 0.86 else '4n'
                    if (class_label == '4n'):
                        TetraSum=TetraSum+1
                    else:
                        TriSum=TriSum+1
                    # Add the result to the list
                    results.append({'file_name': data['file_name'],'class_label': class_label }) 
                    # Create a dataframe from the results 
                    df_results = pd.DataFrame(results) 
                    # Set the index to be the file name 
                    df_results.set_index('file_name', inplace=True) 
                    # Save the dataframe to an Excel file with the unique file name 
                    df_results.to_excel(f'results.xlsx')

    
    # Add pie chart to second column
    with col2:
        st.write("# Statistics")
        print( ClassifyTest)
        if  (ClassifyTest):
            TriSum=TriSum-1 
            TetraSum=TetraSum-1
        # Group data together
        colors = ['#FFA07A', '#F08080']
        df = pd.DataFrame({
       'category': ['3n', '4n'],
       'value': [TriSum , TetraSum ]}) 
        fig = px.pie(df, values='value', names='category',color_discrete_sequence=colors)
        st.plotly_chart(fig, use_container_width=True)

       # if (classify_test == False):
       #     df = pd.DataFrame({'category': ['3n', '4n'],'value': [0, 0]})
       # else:
        #    for result in results:
                # Increment the count of the predicted class label
       #         df.loc[df['category'] == result['class_label'], 'value'] += 1
       #         fig = px.pie(df, values='value', names='category')
        #        st.plotly_chart(fig, use_container_width=True)

    # Apply custom style to first container
    st.markdown(f'<style>.streamlit-container:first-child {{ {container_style} }}</style>', unsafe_allow_html=True)



# Create second container 
with st.container():
    with  st.expander("find the excel sheet here") :
        with open("results.xlsx", "rb") as file:
            st.download_button(label="Download data as xls",data=file,file_name='result.xls', mime='text/xls')
    
  
        

