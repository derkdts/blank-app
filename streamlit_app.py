import streamlit as st
import pandas as pd

# Исходные данные
data = {'Имя': ['Спец', 'Спец2', 'Спец3', 'Спец4', 'Спец5'],
        'Канал': ['Сп', 'Ткт', 'АЦ', 'Сп', 'Ткт'],
        'Обед': ['12:00', '13:00', '14:00', '15:00', '12:00']}
df = pd.DataFrame(data)

# Список возможных значений для столбцов
channels = ['Сп', 'Ткт', 'АЦ', 'Другой']
lunch_times = ['12:00', '13:00', '14:00', '15:00']

def create_app():
    # Сохраняем исходные данные в сессии
    if 'original_df' not in st.session_state:
        st.session_state.original_df = df.copy()

    # Таблица для редактирования с ограниченными значениями
    edited_df = st.data_editor(st.session_state.original_df,
                              column_config={
                                  'Канал': dict(options=channels, read_only=True),
                                  'Обед': dict(options=lunch_times, read_only=True)
                              })

    # Кнопка сохранения
    if st.button("Сохранить изменения"):
        st.session_state.original_df = edited_df
        st.success("Данные сохранены")

# Запускаем приложение
create_app()
