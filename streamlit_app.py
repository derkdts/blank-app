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

# Отображаем выпадающие списки
for employee in employees:
    default_channel = st.session_state.df.loc[employee, 'Канал'] if employee in st.session_state.df.index else "Не обедал"
    default_index = channels.index(default_channel)

    selected_channel = st.selectbox(
        f"**{employee}**",
        channels,
        index=default_index,
        key=f"channel_select_{employee}"
    )
    st.session_state.selected_channels[employee] = selected_channel

# Кнопка "Сохранить"
col1, col2, _ = st.columns([1,1,6]) #Создаем колонки для размещения кнопки по центру
with col1:
    pass
with col2:
    if st.button("Сохранить"):
        for employee, channel in st.session_state.selected_channels.items():
            st.session_state.df.loc[employee, 'Канал'] = channel
        st.success("Данные сохранены!")
with _ :
    pass

# Выводим итоговую таблицу
st.write("Итоговая таблица:")

# Добавляем нумерацию строк
df_display = st.session_state.df.reset_index()
df_display.index += 1
df_display = df_display.rename(columns={'index': '#'})

st.dataframe(df_display, use_container_width=True) #Растягиваем таблицу на всю ширину

# Дополнительная информация
st.write("Разработано с использованием Streamlit.")

# Функция для очистки данных
def clear_data():
    st.session_state.df['Канал'] = "Не обедал"
    st.session_state.selected_channels = {}
    st.experimental_rerun() #Перезапускаем приложение для обновления данных
    st.success("Данные очищены")

if st.button("Очистить данные"):
    clear_data()
