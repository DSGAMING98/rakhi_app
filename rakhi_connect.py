# rakhi_connect.py
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Rakhi Connect 💞", layout="wide")

st.markdown("<h1 style='text-align: center; color: #d63384;'>🎀 Rakhi Connect 🎀</h1>", unsafe_allow_html=True)
st.markdown("### Celebrating the sibling bond with vibes, love, and a lil’ destruction of hate.")

try:
    img = Image.open("assets/rakhi_banner.jpeg")
    st.image(img, use_container_width=True)
except:
    st.info("No banner found. Add one at assets/rakhi_banner.jpeg")


