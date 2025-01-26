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
    # Создание формы для редактирования
    with st.form("my_form"):
        # Ввод имени
        name = st.text_input("Имя", value=df['Имя'][0])
        # Выбор канала
        channel = st.selectbox("Канал", options=channels, index=0)
        # Выбор времени обеда
        lunch_time = st.selectbox("Обед", options=lunch_times, index=0)

        # Кнопка сохранения
        if st.form_submit_button("Сохранить изменения"):
            # Обновление данных
            # ... (здесь нужно реализовать логику обновления DataFrame)
            st.success("Данные сохранены")

    # Таблица для просмотра
    st.dataframe(st.session_state.original_df, use_container_width=True)

# Сохраняем исходные данные в сессии
if 'original_df' not in st.session_state:
    st.session_state.original_df = df.copy()

# Запускаем приложение
create_app()
