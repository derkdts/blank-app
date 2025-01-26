import streamlit as st
import pandas as pd
import plotly.express as px

# Исходные данные
data = {'Имя': ['Спец', 'Спец2', 'Спец3', 'Спец4', 'Спец5'],
        'Канал': ['Сп', 'Ткт', 'АЦ', 'Сп', 'Ткт'],
        'Обед': ['12:00', '13:00', '14:00', '15:00', '12:00']}
df = pd.DataFrame(data)

def create_editable_table(df):
    st.dataframe(df, editable=True)
    if st.button('Обновить'):
        df[:] = st.session_state.df
        st.success('Данные обновлены')
        st.session_state.edited_df = df

    # Вкладки должны быть внутри функции
    tab1, tab2 = st.tabs(["Данные", "Анализ"])

    with tab1:
        # Фильтр по каналу
        channel_filter = st.selectbox("Выберите канал", df['Канал'].unique())
        filtered_df = df[df['Канал'] == channel_filter]

        # Таблица с возможностью редактирования
        edited_df = filtered_df.copy()  # Создаем копию отфильтрованных данных
        st.dataframe(edited_df, editable=True)

        # Кнопка сохранения
        if st.button("Сохранить изменения"):
            st.session_state.original_df = edited_df
            st.success("Данные сохранены")

    with tab2:
        # График
        create_chart(st.session_state.original_df)

    # Настройки
    theme = st.selectbox("Выберите тему", ["Светлая", "Темная"])
    if theme == "Темная":
        st.write("Темная тема выбрана")

# Сохраняем исходные данные в сессии
if 'original_df' not in st.session_state:
    st.session_state.original_df = df.copy()

# Вызываем функцию для создания таблицы
create_editable_table(st.session_state.original_df)