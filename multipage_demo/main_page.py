import streamlit as st 
import pandas as pd

st.set_page_config(          
    page_title = "Real-Time Data Dashboard",             
    page_icon = "Active",          
    layout = "wide",       
)

# To run web app with multiple pages, run 'streamlit main_page.py' on your terminal

'''
As apps grow large, it becomes useful to organize them into multiple pages. 
This makes the app easier to manage as a developer and easier to navigate as a user. 
Streamlit provides a frictionless way to create multipage apps.

We designed this feature so that building a multipage app is as easy as building a single-page app! 
Just add more pages to an existing app as follows:

In the folder containing your main script, create a new pages folder. Let’s say your main script is named main_page.py.
Add new .py files in the pages folder to add more pages to your app.
Run streamlit run main_page.py as usual.
That’s it! The main_page.py script will now correspond to the main page of your app.
And you’ll see the other scripts from the pages folder in the sidebar page selector. The pages are listed according to filename (without file extensions and disregarding underscores).
'''



with st.sidebar:
    st.title('Main page 🎈')
    st.caption("main")

with st.form(key='my_form_to_submit'):
    file = st.file_uploader("Upload file here:", accept_multiple_files = False)
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
