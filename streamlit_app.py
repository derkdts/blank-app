import streamlit as st
import pandas as pd

# Исходные данные
data = {'Имя': ['Спец', 'Спец2', 'Спец3', 'Спец4', 'Спец5'],
        'Канал': ['Сп', 'Ткт', 'АЦ', 'Сп', 'Ткт'],
        'Обед': ['12:00', '13:00', '14:00', '15:00', '12:00']}
df = pd.DataFrame(data)

# Сохраняем исходные данные в сессии
if 'original_df' not in st.session_state:
    st.session_state.original_df = df.copy()

def create_app():
    # Таблица для редактирования
    edited_df = st.data_editor(st.session_state.original_df)

    # Кнопка сохранения
    if st.button("Сохранить изменения"):
        st.session_state.original_df = edited_df
        st.success("Данные сохранены")

# Запускаем приложение
create_app()
