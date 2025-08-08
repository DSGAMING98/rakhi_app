import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
from io import BytesIO
import re

st.title("Rakhi Card Generator")

st.markdown(
    "<div style='background-color:#ffe6e6;padding:10px;border-radius:5px;'>"
    "<b style='color:red;'>Do not use emojis!</b> The current font does not support them and your card will break. "
    "Stick to words only (for now).</div>", unsafe_allow_html=True
)


sibling_name = st.text_input("To:", value="My Dumb Brother")
your_name = st.text_input("From:", value="Your Less Annoying Sister")
custom_message = st.text_area("Write your fake-hate message:", height=200,
    value="You're the most annoying creature alive, but I guess I’d still fight the world for you. Happy Raksha Bandhan, you lovable idiot.")


def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags
        "]+",
        flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

sibling_name = remove_emojis(sibling_name)
your_name = remove_emojis(your_name)
custom_message = remove_emojis(custom_message)


font_color = st.color_picker("Pick font color", "#A02020")


font_dir = os.path.join("assets", "fonts")
font_main = os.path.join(font_dir, "LittleBoy-X3m3a.ttf")
font_alt = os.path.join(font_dir, "LittleBoy-gx1x5.ttf")
bg_path = os.path.join("assets", "card_bg.png")

if st.button("Generate Card"):
    try:
        img = Image.open(bg_path).convert("RGBA")
        draw = ImageDraw.Draw(img)
        width, height = img.size


        try:
            font_title = ImageFont.truetype(font_main, 54)
            font_msg = ImageFont.truetype(font_main, 42)
            font_sign = ImageFont.truetype(font_main, 38)
        except:
            font_title = ImageFont.truetype(font_alt, 54)
            font_msg = ImageFont.truetype(font_alt, 42)
            font_sign = ImageFont.truetype(font_alt, 38)


        wrapped_msg = textwrap.fill(custom_message, width=30)
        msg_lines = wrapped_msg.split("\n")
        bbox = font_msg.getbbox("A")
        line_height = (bbox[3] - bbox[1]) + 10  # height + padding

        msg_block_height = line_height * len(msg_lines)
        msg_y = int(height * 0.45 - msg_block_height // 2)


        title_w = draw.textlength(sibling_name, font=font_title)
        draw.text(((width - title_w) / 2, height * 0.30), sibling_name, font=font_title, fill=font_color)


        for i, line in enumerate(msg_lines):
            line_w = draw.textlength(line, font=font_msg)
            draw.text(((width - line_w) / 2, msg_y + i * line_height), line, font=font_msg, fill=font_color)


        sign_text = f"- {your_name}"
        sign_w = draw.textlength(sign_text, font=font_sign)
        draw.text(((width - sign_w) / 2, msg_y + msg_block_height + 20), sign_text, font=font_sign, fill=font_color)


        st.image(img, caption="Your Rakhi Card", use_container_width=True)
        buf = BytesIO()
        img.save(buf, format="PNG")
        st.download_button("Download Card", data=buf.getvalue(), file_name="rakhi_card.png", mime="image/png")

    except Exception as e:
        st.error(f"Something went wrong: {e}")
