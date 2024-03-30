import streamlit as st
import numpy as np
import pandas as pd
import time

st.header("Chat Elements")

st.sidebar.markdown("Chat Elements")

st.subheader("st.chat_input")

st.write("Display a chat input widget.")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

st.code("""
#Alternative
with st.sidebar:
    messages = st.container(height=300)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")
"""
)

st.subheader("st.chat_message")

st.write("""

Insert a chat message container.

To add elements to the returned container, you can use `with` notation (preferred) or just call methods directly on the returned object. See the examples below.

""")

with st.chat_message("user"):
    st.write("Hello 👋")
    st.line_chart(np.random.randn(30, 3))

message = st.chat_message("assistant")
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))

st.subheader("st.status")

st.write("""

Insert a status container to display output from long-running tasks.

Inserts a container into your app that is typically used to show the status and details of a process or task. The container can hold multiple elements and can be expanded or collapsed by the user similar to st.expander. When collapsed, all that is visible is the status icon and label.

The label, state, and expanded state can all be updated by calling .update() on the returned object. To add elements to the returned container, you can use "with" notation (preferred) or just call methods directly on the returned object.

By default, st.status() initializes in the "running" state. When called using "with" notation, it automatically updates to the "complete" state at the end of the "with" block. See examples below for more details.

""")

with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)

st.button('Rerun')

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
