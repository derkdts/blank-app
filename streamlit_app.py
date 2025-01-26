import streamlit as st
import pandas as pd

# Исходные данные
data = {'Имя': ['Спец', 'Спец2', 'Спец3', 'Спец4', 'Спец5'],
        'Канал': ['Сп', 'Ткт', 'АЦ', 'Сп', 'Ткт'],
        'Статус': ['Активен', 'Неактивен', 'Активен', 'Неактивен', 'Активен']}
df = pd.DataFrame(data)

# Список возможных значений для столбца "Статус"
status_options = ['Активен', 'Неактивен', 'В ожидании']

def create_app():
    # Вкладки
    tab1, tab2 = st.tabs(["Редактирование", "Просмотр"])

    with tab1:
        # Таблица для редактирования с выпадающим списком для столбца "Статус"
        edited_df = st.data_editor(df, column_config={'Статус': dict(options=status_options)})

        # Кнопка сохранения
        if st.button("Сохранить изменения"):
            st.session_state.original_df = edited_df
            st.success("Данные сохранены")

    with tab2:
        # Таблица для просмотра
        st.dataframe(st.session_state.original_df, use_container_width=True)

# Запускаем приложение
create_app()
