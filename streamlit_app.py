import streamlit as st
import pandas as pd
import datetime

# Список сотрудников
employees = ["Сотрудник 1", "Сотрудник 2", "Сотрудник 3", "Сотрудник 4", "Сотрудник 5", "Сотрудник 6", "Сотрудник 7"]

# Список каналов
channels = ["Канал 1", "Канал 2", "Канал 3"]

# Получаем текущую дату
today = datetime.date.today()

# Функция для создания пустого DataFrame
def create_empty_dataframe(date):
    df = pd.DataFrame(0, index=employees, columns=channels)  # Инициализируем нулями
    df['Дата'] = date.strftime("%d.%m.%Y")
    return df

# Проверяем, есть ли сохраненные данные в сессии
if 'df' not in st.session_state:
    st.session_state.df = create_empty_dataframe(today)

# Заголовок приложения
st.title("Учет каналов и обедов")

# Выбор даты
selected_date = st.date_input("Выберите дату:", today)

# Преобразуем дату из строки в datetime.date для сравнения
try:
    selected_date_obj = datetime.datetime.strptime(st.session_state.df['Дата'].iloc[0], "%d.%m.%Y").date()
except (ValueError, IndexError):  # Обработка исключений при первом запуске
    selected_date_obj = today

# Если выбрана другая дата, создаем новый DataFrame
if selected_date != selected_date_obj:
    st.session_state.df = create_empty_dataframe(selected_date)

# Отображаем таблицу с возможностью редактирования
st.write("Укажите количество обедов по каждому каналу:")
edited_df = st.data_editor(st.session_state.df.drop('Дата', axis=1), key=f"editor_{selected_date}") #Удаляем столбец Дата для редактирования

# Сохраняем изменения обратно в session_state, добавляя столбец Дата
st.session_state.df = pd.concat([edited_df, st.session_state.df[['Дата']]], axis=1)

# Выводим итоговую таблицу для проверки
st.write("Итоговая таблица:")
st.dataframe(st.session_state.df)
