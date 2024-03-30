import streamlit as st
import numpy as np

st.header("Media elements")

st.sidebar.markdown("Media elements")

st.subheader("st.image")

st.write("Display an image or list of images.")

st.image('pnn.png', caption='Kaushik, Matthew and Harry at Product Networking Night 2024. Held at SMU Connexion Level 5 Event Square on 22 March 2024 (Friday)')

st.subheader("st.audio")

st.write("Display an audio player.")

audio_file = open('sample.wav', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/wav')

sample_rate = 44100  # 44100 samples per second
seconds = 2  # Note duration of 2 seconds
frequency_la = 440  # Our played note will be 440 Hz
# Generate array with seconds*sample_rate steps, ranging between 0 and seconds
t = np.linspace(0, seconds, seconds * sample_rate, False)
# Generate a 440 Hz sine wave
note_la = np.sin(frequency_la * t * 2 * np.pi)

st.audio(note_la, sample_rate=sample_rate)

st.subheader("st.video")

st.write("Display a video player.")

video_url = 'https://www.youtube.com/watch?v=HDpG17IyvT8'

st.video(video_url)