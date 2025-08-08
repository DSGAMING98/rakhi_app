import streamlit as st

st.set_page_config(page_title="Sibling Roast Quiz", layout="centered")

st.title("Sibling Quiz – Sister’s Interrogation Edition")

st.markdown("Sit down, bro. It’s time for your **annual sibling performance review**")

score = 0


q1 = st.radio("1. What's my favorite thing to yell at you for?", [
    "Breathing too loud",
    "Leaving the bathroom light on",
    "Stealing the charger I just hid",
    "All of the above (obviously)"
])
if q1 == "All of the above (obviously)":
    score += 1
    st.success("Damn right.")

q2 = st.radio("2. When I say 'I don’t want anything from the shop', what do I actually mean?", [
    "I don’t want anything",
    "Get me Lays or you’ll suffer",
    "I’m testing you",
    "It’s a trap"
])
if q2 == "Get me Lays or you’ll suffer":
    score += 1
    st.success("So you DO listen sometimes.")

q3 = st.radio("3. How many times have you annoyed me today (be honest)?", [
    "None",
    "Like 3",
    "Probably 10+",
    "I exist, so infinite"
])
if q3 == "I exist, so infinite":
    score += 1
    st.success("At least you’re self-aware.")

q4 = st.radio("4. What happens if you eat my chocolate?", [
    "You’ll say sorry and buy another",
    "You’ll disappear mysteriously",
    "You’ll never eat again",
    "I’ll cry, you’ll die"
])
if q4 == "I’ll cry, you’ll die":
    score += 1
    st.success("Emotional damage AND physical.")

q5 = st.radio("5. What do you actually mean when you call me annoying?", [
    "I hate you",
    "You're annoying",
    "I love you but I must insult you to survive",
    "Go away forever"
])
if q5 == "I love you but I must insult you to survive":
    score += 1
    st.success("A sibling classic.")


if st.button("Show My Sibling Score"):
    st.markdown("---")
    st.subheader("Sibling Compatibility Results:")
    if score == 5:
        st.success("💯 Perfect sibling! Either you’re lying, or you’re actually decent. Suspicious.")
    elif score >= 3:
        st.info("🙂 Acceptable sibling. Mildly tolerable. Keep snacks flowing.")
    else:
        st.error("👎 Go apologize to your sister right now. And buy her chocolate.")

