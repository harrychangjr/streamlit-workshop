
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
    st.caption("Page 2 ❄️")



with st.form(key='my_form_to_submit'):
    file = st.session_state["uploaded_file"] #literally uploads the bytes data
    file_columns = list(file.columns)
    print("file:", file)
    print("file cols:", list(file.columns))
    x_filter = st.selectbox ("Select X value", file_columns)
    y_filter = st.selectbox ("Select Y value", file_columns)
    group_filter = st.selectbox ("Select Group value", file_columns)

    #https://plotly.com/python/plotly-express/
    chart_visual = st.selectbox("Selecting Visual Charts", ("Line Chart", "Box Plot"))
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write("nice")
    if chart_visual == "Line Chart":
        fig = px.line(file, 
                    x=x_filter, 
                    y=y_filter, 
                    color=group_filter, 
                    title= f"Plot of {y_filter} against {x_filter}")

    elif chart_visual == "Box Plot":
        fig = px.box(file, 
                    y=y_filter, 
                    x=group_filter,
                    title= f"Plot of {y_filter} by {group_filter}")


    st.plotly_chart(fig)
