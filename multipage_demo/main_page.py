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
    1. Using multiple pages (file structure and persisting variables)
    2. Waiting for excecution
    3. Sample Data Uses
    4. Streamlit components

              main_page            page_2             page_3
Based on: [Data Collection] -> [Data Analysis] -> [Data Modelling]

Let's Begin!
'''

with st.sidebar:
    st.title('Main page 🎈')
    st.caption("First Page")

def confirm_upload():
    st.write("Data Uploaded!")
    
# Form groups elements is built with a Submit button. 
# Values will be sent as a batch when Submit button is pressed.
# If Widgets are not in a form, Streamlit script will rerun everytime the value is changed (Useful for "pausing" excecution)
with st.form(key='confirm_upload'):
    file = st.file_uploader("Upload file here:", accept_multiple_files = False) #literally uploads the bytes data
    submit_button = st.form_submit_button(label='Submit', on_click = confirm_upload)

if submit_button: # check that button has been pressed
    if file: # check data is available

        # Process the uploaded files
        if file.type == "text/csv" or file.type == "text/xlsx":
            file_details = {"FileName": file.name, "FileType": file.type, "FileSize": file.size}
            st.write("You have uploaded: ", file_details)

            #persist data within the session
            try:
                st.session_state["uploaded_file"] = pd.read_csv(file)
            except:
                st.session_state["uploaded_file"] = pd.read_xlsx(file)
            
        else:
            st.write("Please upload valid file and check file type!")
    
