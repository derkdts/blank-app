import streamlit as st
import pandas as pd
import plotly.express as px

# Исходные данные
data = {'Имя': ['Спец', 'Спец2', 'Спец3', 'Спец4', 'Спец5'],
        'Канал': ['Сп', 'Ткт', 'АЦ', 'Сп', 'Ткт'],
        'Обед': ['12:00', '13:00', '14:00', '15:00', '12:00']}
df = pd.DataFrame(data)

# Функция для создания редактируемой таблицы
def create_editable_table(df):
    st.dataframe(df, editable=True)
    if st.button('Обновить'):
        df[:] = st.session_state.df
        st.success('Данные обновлены')

# Функция для создания графика
def create_chart(df):
    fig = px.histogram(df, x='Канал', title='Распределение по каналам')
    st.plotly_chart(fig)

# Функция для сохранения данных
def save_data(df):
    if st.button("Сохранить данные"):
        df.to_csv("data.csv", index=False)
        st.success("Данные сохранены")

# Вкладки
tab1, tab2 = st.tabs(["Данные", "Анализ"])

with tab1:
    # Фильтр по каналу
    channel_filter = st.selectbox("Выберите канал", df['Канал'].unique())
    filtered_df = df[df['Канал'] == channel_filter]

    # Таблица с возможностью редактирования
    edited_df = create_editable_table(filtered_df)
    st.session_state.df = edited_df

    # Кнопка сохранения
    save_data(edited_df)

with tab2:
    # График
    create_chart(df)

# Настройки (например, тема)
theme = st.selectbox("Выберите тему", ["Светлая", "Темная"])
if theme == "Темная":
    st.write("Темная тема выбрана")
