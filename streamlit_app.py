import streamlit as st
import pandas as pd
import plotly.express as px

# Исходные данные
data = {'Имя': ['Спец', 'Спец2', 'Спец3', 'Спец4', 'Спец5'],
        'Канал': ['Сп', 'Ткт', 'АЦ', 'Сп', 'Ткт'],
        'Обед': ['12:00', '13:00', '14:00', '15:00', '12:00']}
df = pd.DataFrame(data)

# Сохраняем исходные данные в сессии
if 'original_df' not in st.session_state:
    st.session_state.original_df = df.copy()

def create_editable_table(df):
    # ... (код для создания редактируемой таблицы)
    st.session_state.edited_df = df

def create_chart(df):
    # ... (код для создания графика)

# Вкладки
tab1, tab2 = st.tabs(["Данные", "Анализ"])

with tab1:
    # Фильтр по каналу
    channel_filter = st.selectbox("Выберите канал", df['Канал'].unique())
    filtered_df = df[df['Канал'] == channel_filter]

    # Таблица с возможностью редактирования
    edited_df = create_editable_table(filtered_df)

    # Кнопка сохранения
    if st.button("Сохранить изменения"):
        st.session_state.original_df = st.session_state.edited_df
        st.success("Данные сохранены")

with tab2:
    create_chart(st.session_state.original_df)

# Настройки
theme = st.selectbox("Выберите тему", ["Светлая", "Темная"])
if theme == "Темная":
    st.write("Темная тема выбрана")
