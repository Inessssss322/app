import streamlit as st

st.title('Перевірка додатку')
name = st.text_input("Для перевірки напишіть слово 'name'")
answer = "name"

if name:
    if name == answer:
        st.success(f"Первірка пройдена")
    else:
        st.error(f"Перевірка не пройдена")
