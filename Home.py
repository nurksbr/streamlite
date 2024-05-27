import streamlit as st
import pandas as pd
# Başlık
st.title("Merhaba, Fevziye Nur!")

# Alt başlık
st.subheader("Fevziye Nur ile Basit Bir Merhaba Sayfası")

# Metin ve emoji
st.write("👋 Merhaba! Streamlit ile web uygulamaları oluşturmak çok kolay!")
st.write("🌟 Bu bir örnek uygulamadır.")
st.write("🚀 Hadi başlayalım!")

# Liste ve emojiler
st.write("""
### Bu sayfada neler bulabilirsiniz?
- 📈 Veri görselleştirme örnekleri
- 📊 Etkileşimli grafikler
- 📝 Metin ve veri giriş formları
- 🌐 Web veri çekme örnekleri
""")

# Kullanıcıdan girdi almak için bir metin kutusu
name = st.text_input("Adınızı girin:", "")
if name:
    st.write(f"Merhaba, {name}! 👋")

# Buton
if st.button('Beni tıkla!'):
    st.write("Butona tıkladınız! 🎉")

# Seçim kutusu
option = st.selectbox(
    'En sevdiğiniz emoji hangisi?',
    ('👋', '🌟', '🚀', '📈', '📊', '📝', '🌐')
)
st.write('Seçtiğiniz emoji:', option)

# Resim
st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)
