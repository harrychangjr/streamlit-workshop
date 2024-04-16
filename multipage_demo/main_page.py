import streamlit as st 
import pandas as pd

st.set_page_config(          
    page_title = "Data Centre",             
    page_icon = "Active",          
    layout = "wide",      
)

st.markdown("# Input Your Data")

'''
Multipage Streamlit apps are useful when we want to organise our data and functionalities.
To get started, you just need to have the main_page and another folder containing the scripts for the other pages

This section showcases:
    1. Using multiple pages
    2. Streamlit Components
    3. Sample Data Uses

Based on: [Data Collection] -> [Data Analysis] -> [Data Modelling]

Let's Begin!
'''

with st.sidebar:
    st.title('Main page 🎈')
    st.caption("First Page")

with st.form(key='confirm_upload'): # form identifier
    file = st.file_uploader("Upload file here:", accept_multiple_files = False) #literally uploads the bytes data
    submit_button = st.form_submit_button(label='Submit')
    
if file:
    st.session_state["uploaded_file"] = pd.read_csv(file)
    

# Process the uploaded files
if file:
    if file.type == "text/csv" or file.type == "text/xlsx":
        file_details = {"FileName": file.name, "FileType": file.type, "FileSize": file.size}
        st.write("You have uploaded: ", file_details)
        
    else:
        st.write("Please upload valid file and check file type!")
