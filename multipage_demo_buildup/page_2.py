
import sys
import numpy as np    
import pandas as pd               
import plotly.express as px 
import streamlit as st 
import time

#TODO:
from main_page import file ###

with st.sidebar:
    st.title('Page 2 ❄️')
    st.caption("This page showcases how you can explore data")
    
st.markdown("# Visualize Your Data")

"""
Now we want to try understand our data better.
Select the variables and type of plots
""" 
    
try:
    # get persisted data
    #TODO:
    ### get data from session state

    # create "sections" in the display
    #TODO:
    ### define outer sections
    
    ### outer 1
    st.dataframe(file)
    
    ### outer 2
    with st.form(key='confirm_plot_selection'):
        
        file_columns = list(file.columns)
        # print("file:", file)
        # print("file cols:", list(file.columns))
        
        ### define inner sections
        ### inner 1
        x_filter = st.selectbox(label = "Select X value", options = [None] + file_columns)
        ### inner 2
        y_filter = st.selectbox(label = "Select Y value", options = [None] + file_columns)
        ### inner 3
        group_filter = st.selectbox(label = "Select Group value", options = [None] + file_columns)

        #https://plotly.com/python/plotly-express/
        chart_visual = st.selectbox("Select Visual Charts", [None] + ["Scatter Plot", "Box Plot"])
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        #create chart
        if chart_visual == "Scatter Plot":
            fig = px.scatter(file, 
                        x=x_filter, 
                        y=y_filter, 
                        color=group_filter, 
                        opacity = 0.5,
                        title= f"Plot of {y_filter} against {x_filter}")

        elif chart_visual == "Box Plot":
            fig = px.box(file, 
                        y=y_filter, 
                        x=x_filter,
                        title= f"Plot of {y_filter} by {group_filter}")

        #plot chart using plotly
        if fig:
            st.plotly_chart(fig)
        
        else: 
            st.write("Choose an appropriate Plot!")
        
except:
    st.write("Please input data in the Main Page first!")
