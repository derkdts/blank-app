import streamlit as st
import pandas as pd

# Список сотрудников
employees = ["Сотрудник 1", "Сотрудник 2", "Сотрудник 3", "Сотрудник 4", "Сотрудник 5", "Сотрудник 6", "Сотрудник 7"]

# Список каналов (включая "Не обедал")
channels = ["Не обедал", "Канал 1", "Канал 2", "Канал 3"]

# Инициализация DataFrame в session_state
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(index=employees, columns=['Канал'])
    st.session_state.df['Канал'] = "Не обедал"

st.title("Учет каналов и обедов")

st.write("Выберите канал для каждого сотрудника:")

# Создаем словарь для хранения выбранных каналов в текущей сессии
if 'selected_channels' not in st.session_state:
    st.session_state.selected_channels = {}

for employee in employees:
    # Используем значение из session_state или значение по умолчанию "Не обедал"
    default_channel = st.session_state.df.loc[employee, 'Канал'] if employee in st.session_state.df.index else "Не обедал"
    default_index = channels.index(default_channel)

    selected_channel = st.selectbox(
        f"**{employee}**",
        channels,
        index=default_index,
        key=f"channel_select_{employee}" # Улучшенный ключ
    )
    st.session_state.selected_channels[employee] = selected_channel #Сохраняем в словаре

# Кнопка "Сохранить"
if st.button("Сохранить"):
    for employee, channel in st.session_state.selected_channels.items():
        st.session_state.df.loc[employee, 'Канал'] = channel
    st.success("Данные сохранены!") # Сообщение об успехе

# Выводим итоговую таблицу
st.write("Итоговая таблица:")
st.dataframe(st.session_state.df)

#Дополнительная информация
st.write("Разработано с использованием Streamlit.")
