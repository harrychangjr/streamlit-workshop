import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import time
from io import StringIO

st.header("Input widgets")

st.sidebar.markdown("Input widgets")

st.subheader("st.button")

st.write("Display a button widget.")

st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

st.subheader("st.download_button")

st.write("""

Display a download button widget.

This is useful when you would like to provide a way for your users to download a file directly from your app.

Note that the data to be downloaded is stored in-memory while the user is connected, so it's a good idea to keep file sizes under a couple hundred megabytes to conserve memory.

""")

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

my_large_df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

csv = convert_df(my_large_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)

text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

binary_contents = b'example content'
# Defaults to 'application/octet-stream'
st.download_button('Download binary file', binary_contents)

with open("pnn.png", "rb") as file:
    btn = st.download_button(
            label="Download image",
            data=file,
            file_name="pnn.png",
            mime="image/png"
          )
    
st.subheader("st.link_button")

st.write("""

Display a link button element.

When clicked, a new tab will be opened to the specified URL. This will create a new session for the user if directed within the app.
""")

st.link_button("Go to gallery", "https://streamlit.io/gallery")

st.subheader("st.page_link")

st.write("""

Display a link to another page in a multipage app or to an external page.

If another page in a multipage app is specified, clicking `st.page_link` stops the current page execution and runs the specified page as if the user clicked on it in the sidebar navigation.

If an external page is specified, clicking `st.page_link` opens a new tab to the specified page. The current script run will continue if not complete.
""")

st.page_link("01_Main.py", label="Home", icon="🏠")
st.page_link("pages/03_Text_Elements.py", label="Page 3", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")

st.subheader("st.checkbox")

st.write("Display a checkbox widget.")

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')

st.subheader("st.toggle")

st.write("Display a toggle widget.")

on = st.toggle('Activate feature')

if on:
    st.write('Feature activated!')

st.subheader("st.radio")

st.write("Display a radio button widget.")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    index=None,
)

st.write("You selected:", genre)

# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled")
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )

st.subheader("st.selectbox")

st.write("Display a select widget.")

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

option = st.selectbox(
   "How would you like to be contacted?",
   ("Email", "Home phone", "Mobile phone"),
   index=None,
   placeholder="Select contact method...",
)

st.write('You selected:', option)


st.subheader("st.multiselect")

st.write("""

Display a multiselect widget.

The multiselect widget starts as empty.

""")

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

st.subheader("st.slider")

st.write("""

Display a slider widget.

This supports int, float, date, time, and datetime types.

This also allows you to render a range slider by passing a two-element tuple or list as the value.

The difference between *st.slider* and *st.select_slider* is that slider only accepts numerical or date/time data and takes a range as input, while *select_slider* accepts any datatype and takes an iterable set of options.

""")

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

st.subheader("st.select_slider")

st.write("""

Display a slider widget to select items from a list.

This also allows you to render a range slider by passing a two-element tuple or list as the `value`.

The difference between `st.select_slider` and `st.slider` is that `select_slider` accepts any datatype and takes an iterable set of options, while `st.slider` only accepts numerical or date/time data and takes a range as input.
         
""")

color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)

st.subheader("st.text_input")

st.write("""

Display a single-line text input widget.
         
""")

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

st.subheader("st.number_input")

st.write("""

Display a numeric input widget.
         
""")

number = st.number_input('Insert a number')
st.write('The current number is ', number)

number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
st.write('The current number is ', number)

st.subheader("st.text_area")

st.write("""

Display a multi-line text input widget.
         
""")

txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
    )

st.write(f'You wrote {len(txt)} characters.')

st.subheader("st.date_input")

st.write("""

Display a date input widget.
         
""")

import datetime
d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
)
d

d = st.date_input("When's your birthday", value=None)
st.write('Your birthday is:', d)

st.subheader("st.time_input")

st.write("""

Display a time input widget.
         
""")

t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)

t = st.time_input('Set an alarm for', value=None)
st.write('Alarm is set for', t)

st.subheader("st.file_uploader")

st.write("""

Display a file uploader widget.

By default, uploaded files are limited to 200MB. You can configure this using the *server.maxUploadSize* config option. For more info on how to set config options, see https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options
         
""")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

st.subheader("st.camera_input")

st.write("""

Display a widget that returns pictures from the user's webcam.
         
""")

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

st.subheader("st.color_picker")

st.write("""

Display a color picker widget.
         
""")

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)


