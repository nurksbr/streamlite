import streamlit as st
from textblob import TextBlob

st.title("Metin Duygu Analizi Uygulaması 😊😢")

text = st.text_area("Metni girin:")

if st.button("Analiz Et"):
    if text:
        blob = TextBlob(text)
        sentiment = blob.sentiment
        st.write(f"Polarity (Duygu): {sentiment.polarity}")
        st.write(f"Subjectivity (Öznelik): {sentiment.subjectivity}")
