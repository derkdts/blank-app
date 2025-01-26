import streamlit as st
import pandas as pd

# Исходные данные
data = {'Имя': ['Спец', 'Спец2', 'Спец3', 'Спец4', 'Спец5'],
        'Канал': ['Сп', 'Ткт', 'АЦ', 'Сп', 'Ткт'],
        'Обед': ['12:00', '13:00', '14:00', '15:00', '12:00']}
df = pd.DataFrame(data)

# Список возможных значений для столбцов
option = ['Сп', 'Ткт', 'АЦ', 'Другой']
option2 = ['12:00', '13:00', '14:00', '15:00']

def create_app():
    # Вкладки
    tab1, tab2 = st.tabs(["Редактирование", "Просмотр"])

    with tab1:
        # Таблица для редактирования с выпадающими списками
        edited_df = st.data_editor(df, column_config={
            'Канал': option,
            'Обед': option2
        })

        # Кнопка сохранения
        if st.button("Сохранить изменения"):
            st.session_state.original_df = edited_df
            st.success("Данные сохранены")

    with tab2:
        # Таблица для просмотра
        st.dataframe(st.session_state.original_df, use_container_width=True)

# Сохраняем исходные данные в сессии
if 'original_df' not in st.session_state:
    st.session_state.original_df = df.copy()

# Запускаем приложение
create_app()
