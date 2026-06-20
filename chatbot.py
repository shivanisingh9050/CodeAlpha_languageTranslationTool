import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faq = pd.read_csv("faq.csv")

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(faq["Question"])

st.title("FAQ Chatbot")

query = st.text_input("Ask a Question")

if query:
    q_vec = vectorizer.transform([query])
    sim = cosine_similarity(q_vec, vectors)
    idx = sim.argmax()
    st.success(faq["Answer"][idx])