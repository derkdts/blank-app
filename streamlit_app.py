import streamlit as st
import pandas as pd

# Исходные данные
data = {'Имя': ['Спец', 'Спец2', 'Спец3', 'Спец4', 'Спец5'],
        'Канал': ['Сп', 'Ткт', 'АЦ', 'Сп', 'Ткт'],
        'Обед': ['12:00', '13:00', '14:00', '15:00', '12:00']}
df = pd.DataFrame(data)

# Список возможных значений для обеда
lunch_times = ['12:00', '13:00', '14:00', '15:00']

def create_app():
    # Сохраняем исходные данные в сессии
    if 'original_df' not in st.session_state:
        st.session_state.original_df = df.copy()

    # Таблица для редактирования
    edited_df = st.data_editor(st.session_state.original_df,
                              column_config={'Обед': dict(options=lunch_times)})

    # Кнопка сохранения
    if st.button("Сохранить изменения"):
        # Проверяем, были ли изменения
        if edited_df.equals(st.session_state.original_df):
            st.warning("Изменений не обнаружено")
        else:
            st.session_state.original_df = edited_df
            st.success("Данные сохранены")

# Запускаем приложение
create_app()
