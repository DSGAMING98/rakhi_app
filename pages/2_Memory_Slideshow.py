import streamlit as st
import os
from PIL import Image
import time
import base64

st.set_page_config(page_title="Memory Slideshow 🎞️", layout="centered")

st.title("Childhood Memory Slideshow")

st.markdown("Upload your favorite sibling or childhood pics to relive the chaos, cuteness, and cringe")

uploaded_imgs = st.file_uploader("Upload images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)


def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
        <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)

bg_music_path = os.path.join("assets", "bg_music", "soft_track.mp3")



speed = st.slider("Slideshow speed (seconds per image)", 1, 10, 3)

if st.button("Start Slideshow"):
    if not uploaded_imgs:
        st.warning("Please upload at least 1 image.")
    else:

        if os.path.exists(bg_music_path):
            autoplay_audio(bg_music_path)

        placeholder = st.empty()
        while True:
            for img in uploaded_imgs:
                image = Image.open(img)
                placeholder.image(image, use_column_width=True, caption=img.name)
                time.sleep(speed)

