import streamlit as st
import numpy as np
import time

st.header("Layouts and Containers")

st.sidebar.markdown("Layouts and Containers")

st.subheader("st.columns")

st.write("""

Insert containers laid out as side-by-side columns.

Inserts a number of multi-element containers laid out side-by-side and returns a list of container objects.

To add elements to the returned containers, you can use the "with" notation (preferred) or just call methods directly on the returned object. See examples below.

Columns can only be placed inside other columns up to one level of nesting.


""")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)

st.subheader("st.container")

st.write("""

Insert a multi-element container.

Inserts an invisible container into your app that can be used to hold multiple elements. This allows you to, for example, insert multiple elements into your app out of order.

To add elements to the returned container, you can use the "with" notation (preferred) or just call methods directly on the returned object. See examples below.


""")

with st.container():
   st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))


row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container()
    tile.title(":balloon:")

long_text = "Lorem ipsum. " * 1000

with st.container():
    st.markdown(long_text)

st.subheader("st.empty")

st.write("""

Insert a single-element container.

Inserts a container into your app that can be used to hold a single element. This allows you to, for example, remove elements at any point, or replace several elements at once (using a child multi-element container).

To insert/replace/clear an element on the returned container, you can use "with" notation or just call methods directly on the returned object. See examples below.


""")

st.code('''
with st.empty():
    for seconds in range(60):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ 1 minute over!")
''', language='python')

st.subheader("st.expander")

st.write("""

Insert a multi-element container that can be expanded/collapsed.

Inserts a container into your app that can be used to hold multiple elements and can be expanded or collapsed by the user. When collapsed, all that is visible is the provided label.

To add elements to the returned container, you can use the "with" notation (preferred) or just call methods directly on the returned object. See examples below.


""")

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write("""
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")


st.subheader("st.sidebar")

st.write("""

Not only can you add interactivity to your app with widgets, you can organize them into a sidebar. Elements can be passed to `st.sidebar` using object notation and `with` notation.

""")

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")

st.subheader("st.tabs")

st.write("""

Insert containers separated into tabs.

Inserts a number of multi-element containers as tabs. Tabs are a navigational element that allows users to easily move between groups of related content.

To add elements to the returned containers, you can use the "with" notation (preferred) or just call methods directly on the returned object. See examples below.
""")

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)