
import sys
import numpy as np    
import pandas as pd               
import plotly.express as px 
import streamlit as st 
import time
 
# setting path

# from main_page import file, submit_button

with st.sidebar:
    st.title('Page 2 ❄️')
    st.caption("This page showcases how you can explore data")
    
st.markdown("# Visualize Your Data")
"""
Now we want to try understand our data better.
Select the variables and type of plots
""" 
    
try:
    file = st.session_state["uploaded_file"]
    
    outer1, outer2 = st.columns([1,1])
    
    with outer1:
        # https://docs.streamlit.io/develop/api-reference/data/st.dataframe
        st.dataframe(file)
    
    with outer2:
        with st.form(key='confirm_plot_selection'):
            
            file_columns = list(file.columns)
            print("file:", file)
            print("file cols:", list(file.columns))
            
            col1, col2, col3 = st.columns([1,1,1])
            with col1:
                x_filter = st.selectbox ("Select X value", [None] + file_columns)
            with col2:
                y_filter = st.selectbox ("Select Y value", [None] + file_columns)
            with col3:
                group_filter = st.selectbox ("Select Group value", [None] + file_columns)

            #https://plotly.com/python/plotly-express/
            chart_visual = st.selectbox("Select Visual Charts", [None] + ["Line Chart", "Box Plot"])
            submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        if chart_visual == "Line Chart":
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

        if fig:
            st.plotly_chart(fig)
        
        else:
            st.write("Choose an appropriate Plot!")
        
except:
    st.write("Please input data in the Main Page first!")
