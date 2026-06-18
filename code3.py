import streamlit as st 
st.header("Audio from URL")
audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
st.audio(audio_url)
st.write("---")
st.header("Video from URL")
video_url = "https://www.youtube.com/watch?v=G8klFsIcBb0"
st.video(video_url)
st.write("---")
st.header("Image from URL")
img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/250px-Python-logo-notext.svg.png"
st.image(img_url, caption="Image from URL")
st.write("---")