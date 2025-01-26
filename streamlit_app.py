import streamlit as st
import pandas as pd
import plotly.express as px

# Данные для таблицы
data = {'Имя': ['Спец', 'Спец2', 'Спец3', 'Спец4', 'Спец5'],
        'Канал': ['Сп', 'Ткт', 'АЦ', 'Сп', 'Ткт'],
        'Обед': ['12:00', '13:00', '14:00', '15:00', '12:00']}
df = pd.DataFrame(data)

# Функция для создания таблицы с возможностью редактирования
def create_editable_table(df):
    # ... (код для создания редактируемой таблицы)

# Функция для создания графика
def create_chart(df):
    # ... (код для создания графика)

# Вкладки
tab1, tab2, tab3 = st.tabs(["Данные", "Анализ", "Настройки"])

with tab1:
    df = create_editable_table(df)
    save_button = st.button("Сохранить изменения")
    if save_button:
        # Сохранение данных в файл или базу данных

with tab2:
    fig = create_chart(df)
    st.plotly_chart(fig)

with tab3:
    # Настройки приложения (например, выбор темы)
    st.selectbox("Выберите тему", ["Светлая", "Темная"])
