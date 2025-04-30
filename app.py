import streamlit as st

st.title('Перевірка додатку')
name = st.text_input("Для перевірки напишіть слово 'name'")
answer = "name"

if st.text_input:
    if name == answer:
        st.success(f"Первірка пройдена")
    else:
        st.error(f"Перевірка не пройдена")
