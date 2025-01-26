import streamlit as st
import pandas as pd


# Список сотрудников
employees = ["Сотрудник 1", "Сотрудник 2", "Сотрудник 3", "Сотрудник 4", "Сотрудник 5", "Сотрудник 6", "Сотрудник 7"]

# Список каналов
channels = ["Канал 1"]


# Проверяем, есть ли сохраненные данные в сессии
if 'df' not in st.session_state:
    st.session_state.df = create_empty_dataframe(today)

# Заголовок приложения
st.title("Учет каналов и обедов")



# Отображаем таблицу
st.write("Отметьте, кто сегодня обедал по какому каналу:")
for employee in employees:
    st.write(f"**{employee}**")
    for channel in channels:
        st.session_state.df.loc[employee, channel] = st.checkbox(channel, value=st.session_state.df.loc[employee, channel])

# Выводим таблицу
st.dataframe(st.session_state.df)

# Добавляем кнопку для скачивания данных в формате CSV
@st.cache_data
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(st.session_state.df)

st.download_button(
    label="Скачать данные в формате CSV",
    data=csv,
    file_name=f'lunch_data_{st.session_state.df["Дата"].iloc[0]}.csv',
    mime='text/csv',
)
