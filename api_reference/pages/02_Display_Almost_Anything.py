import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time
import matplotlib.pyplot as plt

st.header("Display almost anything")

st.sidebar.markdown("Display almost anything")

st.subheader("st.write")

st.write("""

Write arguments to the app.

This is the Swiss Army knife of Streamlit commands: it does different things depending on what you throw at it. Unlike other Streamlit commands, write() has some unique properties:

1. You can pass in multiple arguments, all of which will be written.
2. Its behavior depends on the input types as follows.
3. It returns None, so its "slot" in the App cannot be reused.

""")

st.write('Hello, *World!* :sunglasses:')

st.write(1234)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))

data_frame = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

st.write('1 + 1 = ', 2)
st.write('Below is a DataFrame:', data_frame, 'Above is a dataframe.')

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)

st.subheader("st.write_stream")

st.write("""

Stream a generator, iterable, or stream-like sequence to the app.

`st.write_stream` iterates through the given sequences and writes all chunks to the app. String chunks will be written using a typewriter effect. Other data types will be written using `st.write`.

""")

_LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""


def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)


if st.button("Stream data"):
    st.write_stream(stream_data)

st.subheader("Magic")

st.write("""

Magic commands are a feature in Streamlit that allows you to write almost anything (markdown, data, charts) without having to type an explicit command at all. Just put the thing you want to show on its own line of code, and it will appear in your app. Here's an example:

""")

# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart


