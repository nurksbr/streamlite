import streamlit as st
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# Gerekli nltk verilerini indirme ve ayarlama
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

st.title("Metin Özetleme Uygulaması 📝")

text = st.text_area("Metni girin:", height=300)

def summarize(text, num_sentences):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    words = [word for word in words if word.isalnum()]
    words = [word for word in words if word.lower() not in stop_words]

    freq_dist = FreqDist(words)
    sentences = sent_tokenize(text)

    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_dist:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = freq_dist[word]
                else:
                    sentence_scores[sentence] += freq_dist[word]

    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    summary = ' '.join(sorted_sentences[:num_sentences])
    return summary

if st.button("Özetle"):
    if text:
        summary = summarize(text, 3)  # 3 cümlelik özet
        st.header("Özet")
        st.write(summary)
