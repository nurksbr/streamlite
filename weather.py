import streamlit as st
import requests

st.title("Hava Durumu Uygulaması ☀️")

api_key = "YOUR_API_KEY"  # OpenWeatherMap API anahtarınızı buraya ekleyin.
city = st.text_input("Şehir Adı:")

if st.button("Hava Durumunu Getir"):
    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] == 200:
            st.write(f"Şehir: {data['name']}")
            st.write(f"Sıcaklık: {data['main']['temp']} °C")
            st.write(f"Hava Durumu: {data['weather'][0]['description']}")
        else:
            st.error("Şehir bulunamadı.")
