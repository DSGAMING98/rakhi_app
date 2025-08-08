import streamlit as st
from PIL import Image

import os

st.set_page_config(page_title="Virtual Rakhi Tie", layout="centered")
st.title("🎀 Virtual Rakhi Tie")

st.markdown("Upload your brother’s hand pic, and we’ll virtually tie the rakhi (because physical presence is overrated 💅)")


wrist_img = st.file_uploader("Upload a pic of the wrist/hand", type=["jpg", "jpeg", "png"])


rakhi_folder = os.path.join("assets", "rakhis")
available_rakhis = [f for f in os.listdir(rakhi_folder) if f.endswith(".png")]

selected_rakhi = st.selectbox("Choose a Rakhi design 🎨", available_rakhis)

def overlay_rakhi(wrist_img_path, rakhi_img_path, scale=0.4, rotation=15):
    base = Image.open(wrist_img_path).convert("RGBA")
    rakhi = Image.open(rakhi_img_path).convert("RGBA")


    rakhi_size = (int(base.width * scale), int(rakhi.height * base.width * scale / rakhi.width))
    rakhi = rakhi.resize(rakhi_size, Image.Resampling.LANCZOS)


    rakhi = rakhi.rotate(rotation, expand=True)


    position = ((base.width - rakhi.width) // 2, (base.height - rakhi.height) // 2)


    base.paste(rakhi, position, rakhi)

    target_width = 1200
    scale_factor = target_width / base.width
    new_size = (int(base.width * scale_factor), int(base.height * scale_factor))
    base = base.resize(new_size, Image.Resampling.LANCZOS)

    return base



if st.button("Tie Rakhi"):
    if wrist_img and selected_rakhi:
        try:

            wrist_img_path = os.path.join("temp_wrist.png")
            with open(wrist_img_path, "wb") as f:
                f.write(wrist_img.read())

            rakhi_path = os.path.join(rakhi_folder, selected_rakhi)
            final_img = overlay_rakhi(wrist_img_path, rakhi_path)

            st.image(final_img, caption="Rakhi Tied Virtually!", use_column_width=True)


            final_img.save("final_rakhi_tied.png")
            with open("final_rakhi_tied.png", "rb") as f:
                st.download_button("Download", data=f, file_name="rakhi_tied.png", mime="image/png")

        except Exception as e:
            st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please upload a wrist pic and select a rakhi.")
