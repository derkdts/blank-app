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

# Кнопка "Сохранить" с улучшенным расположением
col1, col2, _ = st.columns([1, 1, 6])
with col1:
    pass
with col2:
    if st.button("Сохранить"):
        for employee, channel in st.session_state.selected_channels.items():
            st.session_state.df.loc[employee, 'Канал'] = channel
        st.success("Данные сохранены!")

# Выводим итоговую таблицу
st.write("Итоговая таблица:")

# Добавляем нумерацию строк и улучшаем отображение
df_display = st.session_state.df.reset_index()
df_display.index += 1
df_display = df_display.rename(columns={'index': '#'})
st.dataframe(df_display, use_container_width=True, hide_index=True) # Скрываем старый индекс

# Дополнительная информация
st.write("Разработано с использованием Streamlit.")

# Функция для очистки данных с подтверждением
def clear_data():
    if st.session_state.df["Канал"].unique().tolist() != ["Не обедал"]: #Проверка, есть ли что очищать
        if st.confirm("Вы уверены, что хотите очистить данные?"):
            st.session_state.df['Канал'] = "Не обедал"
            st.session_state.selected_channels = {}
            st.experimental_rerun()
            st.success("Данные очищены")
    else:
        st.warning("Данные уже очищены")

if st.button("Очистить данные"):
    clear_data()

# Экспорт в CSV
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8') #Убираем индекс из CSV

csv = convert_df(st.session_state.df)

st.download_button(
    label="Скачать данные в формате CSV",
    data=csv,
    file_name='lunch_data.csv',
    mime='text/csv',
)
