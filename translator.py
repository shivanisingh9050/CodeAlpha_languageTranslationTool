import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translation Tool")

text = st.text_area("Enter text to translate")

source = st.selectbox(
    "Source Language",
    ["auto", "en", "hi", "fr", "es"]
)

target = st.selectbox(
    "Target Language",
    ["hi", "en", "fr", "es"]
)

if st.button("Translate"):
    translated = GoogleTranslator(
        source=source,
        target=target
    ).translate(text)

    st.success(translated)