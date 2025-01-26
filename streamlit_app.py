import streamlit as st
import pandas as pd

# Список сотрудников
employees = ["Сотрудник 1", "Сотрудник 2", "Сотрудник 3", "Сотрудник 4", "Сотрудник 5", "Сотрудник 6", "Сотрудник 7"]

# Список каналов (включая вариант "Не обедал")
channels = ["Не обедал", "Канал 1", "Канал 2", "Канал 3"]

# Создаем DataFrame для хранения выбранных каналов
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(index=employees, columns=['Канал'])
    st.session_state.df['Канал'] = "Не обедал" # Инициализируем значением "Не обедал"

st.title("Учет каналов и обедов")

st.write("Выберите канал для каждого сотрудника:")

for employee in employees:
    default_index = channels.index(st.session_state.df.loc[employee, 'Канал']) # Получаем индекс текущего значения
    selected_channel = st.selectbox(f"**{employee}**", channels, index=default_index, key=employee)
    st.session_state.df.loc[employee, 'Канал'] = selected_channel

st.write("Итоговая таблица:")
st.dataframe(st.session_state.df)
