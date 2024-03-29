import streamlit as st

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

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")