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
