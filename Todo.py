import streamlit as st

st.title("Todo Listesi Uygulaması ✔️")

if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

# Yeni görev ekleme
new_task = st.text_input("Yeni görev ekle:")
if st.button("Ekle"):
    st.session_state.tasks.append(new_task)

# Görevleri gösterme
for i, task in enumerate(st.session_state.tasks):
    st.write(f"{i + 1}. {task}")
