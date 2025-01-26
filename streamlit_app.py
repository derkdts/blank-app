import streamlit as st
import pandas as pd
import datetime

# Список сотрудников
employees = ["Сотрудник 1", "Сотрудник 2", "Сотрудник 3", "Сотрудник 4", "Сотрудник 5", "Сотрудник 6", "Сотрудник 7"]

# Список каналов
channels = ["Канал 1"]

# Получаем текущую дату
today = datetime.date.today()

# Функция для создания пустого DataFrame
def create_empty_dataframe(date):
    df = pd.DataFrame(index=employees, columns=channels)
    df['Дата'] = date.strftime("%d.%m.%Y")  # Добавляем столбец с датой
    df = df.fillna(False)  # Заполняем значениями False
    return df

# Проверяем, есть ли сохраненные данные в сессии
if 'df' not in st.session_state:
    st.session_state.df = create_empty_dataframe(today)

# Заголовок приложения
st.title("Учет каналов и обедов")

# Выбор даты
selected_date = st.date_input("Выберите дату:", today)

# Конвертируем дату из строки в объект datetime.date для сравнения
selected_date_obj = datetime.datetime.strptime(st.session_state.df['Дата'].iloc[0], "%d.%m.%Y").date()

# Если выбрана другая дата, создаем новый DataFrame
if selected_date != selected_date_obj:
    st.session_state.df = create_empty_dataframe(selected_date)

# Отображаем таблицу и чекбоксы
st.write("Отметьте, кто сегодня обедал по какому каналу:")
for employee in employees:
    st.write(f"**{employee}**")
    for channel in channels:
        st.session_state.df.loc[employee, channel] = st.checkbox(channel, value=st.session_state.df.loc[employee, channel], key=f"{employee}_{channel}_{selected_date}") # Добавили key

# Выводим таблицу
st.dataframe(st.session_state.df)
