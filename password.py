import streamlit as st
import string
import random

st.title("Şifreni Merak Ediyorsan Haydi Başlayalım!.. 🔐🔒👩🏻‍💻")

# Şifre uzunluğunu seçme
length = st.slider("Şifre uzunluğunu seçin:", 4, 20, 12)

# Şifreyi oluşturma
if st.button("Şifre Oluştur"):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    st.write(f"Oluşturulan Şifre: {password}")
