import streamlit as st
import random

st.set_page_config(page_title="Gift Suggester", layout="centered")
st.title("Rakhi Gift Suggester")

st.markdown("Describe your sibling and we’ll tell you what chaos-curated gift fits best.")


sibling_type = st.selectbox("What type of sibling are you dealing with?", [
    "The Drama Queen",
    "The Silent But Deadly",
    "The Nerd Who Judges You",
    "The Chaotic Sister",
    "The Baby Who Gets Everything",
    "The Gym Freak",
    "The I-Don’t-Know-What-They-Are"
])

budget = st.slider("Your budget (in ₹)", 100, 5000, 1000, step=100)

description = st.text_area("Anything specific about them? (Optional)", placeholder="e.g., loves anime, addicted to coffee, steals my hoodies...")


gift_ideas = {
    "The Drama Queen": [
        "Custom mirror with 'Main Character' engraved",
        "A crown. Literally. Let them feel royal.",
        "Skincare hamper because 'glow-up' is life"
    ],
    "The Silent But Deadly": [
        "Journal to secretly plot world domination",
        "Wireless noise-cancelling headphones",
        "A book titled 'How to Speak (Occasionally)'"
    ],
    "The Nerd Who Judges You": [
        "Bluetooth reading lamp",
        "A sarcastic mug that says 'I’m always right'",
        "Limited edition collectible (anime, marvel, etc.)"
    ],
    "The Chaotic Sister": [
        "Fidget toys that look cursed",
        "Meme pillow with their worst photo printed",
        "Personalized chaos survival kit (snacks, bandaids, chill pills)"
    ],
    "The Baby Who Gets Everything": [
        "Customized hoodie that says 'I’m the Favorite'",
        "Mini fridge for their midnight snacks",
        "Keychain that says 'Sponsored by Big Sis'"
    ],
    "The Gym Freak": [
        "Shaker bottle with sarcastic quote",
        "Smartwatch or fitness band (budget dependent)",
        "Protein snack box (desi flavored)"
    ],
    "The I-Don’t-Know-What-They-Are": [
        "Gift card (let them decide)",
        "Personalized name mug (you can't go wrong)",
        "LED light strips for mood-switching siblings"
    ]
}

if st.button("Suggest Gifts"):
    st.markdown("---")
    st.subheader("🎁 Top Gift Ideas:")

    suggestions = random.sample(gift_ideas[sibling_type], k=3)
    for gift in suggestions:
        st.markdown(f"- {gift}")

    if description:
        st.markdown(f"Based on what you said: *{description}*")
