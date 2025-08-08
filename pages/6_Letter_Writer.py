import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os


FONT_PATH_REGULAR = "assets/fonts/NotoSans.ttf"
FONT_PATH_BOLD = "assets/fonts/NotoSans-Bold.ttf"
BG_PATH = "assets/letter_bg.jpg"


FONT_SIZE = 115


st.title("Letter Writer")

sibling_name = st.text_input("To:", value="My annoying brother")
your_name = st.text_input("From:", value="Your iconic sister")

letter_body = st.text_area("Write your letter:", height=300, value=(
    "You're the most chaotic human I’ve ever met.\n"
    "And yet somehow I love you more than everything.\n"
    "Happy Raksha Bandan, idiot."
))

font_color = st.color_picker("Pick text color", value="#000000")
bold_text = st.checkbox("Make it bold")


if st.button("Generate Letter"):
    try:

        bg = Image.open(BG_PATH).convert("RGBA")
        width, height = bg.size


        font_path = FONT_PATH_BOLD if bold_text else FONT_PATH_REGULAR
        font = ImageFont.truetype(font_path, FONT_SIZE)

        draw = ImageDraw.Draw(bg)


        full_text = f"Dear {sibling_name},\n\n{letter_body}\n\nFrom: {your_name}"


        paragraphs = full_text.split("\n")
        wrapped_lines = []

        for para in paragraphs:
            if para.strip():
                lines = textwrap.wrap(para, width=40)
                wrapped_lines.extend(lines)
            else:
                wrapped_lines.append("")


        bbox = font.getbbox("Ay")
        line_height = int((bbox[3] - bbox[1]) * 1.6)

        total_text_height = line_height * len(wrapped_lines)
        y_start = int((height - total_text_height) / 2.2)


        for i, line in enumerate(wrapped_lines):
            line_width = font.getlength(line)
            x = int((width - line_width) / 2)
            y = y_start + i * line_height
            draw.text((x, y), line, fill=font_color, font=font)

        st.image(bg)

    except OSError as e:
        st.error(f"Font not found or error loading it: {e}")
