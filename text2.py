import streamlit as st
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

st.title("Metin Özetleme Uygulaması 📝")

text = st.text_area("Metni girin:", height=300)

if st.button("Özetle"):
    parser = PlaintextParser.from_string(text, Tokenizer("turkish"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 3)  # 3 cümlelik özet

    st.header("Özet")
    for sentence in summary:
        st.write(sentence)
