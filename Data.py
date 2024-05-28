import streamlit as st
import pandas as pd
import numpy as np

st.title("Veri Görselleştirmek İçin Hazırız... 📽
📊")

# Rastgele veri oluşturma
data = pd.DataFrame({
    'x': np.arange(1, 101),
    'y': np.random.randn(100).cumsum()
})

# Çizgi grafiği gösterme
st.line_chart(data.set_index('x'))
