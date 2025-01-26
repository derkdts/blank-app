import streamlit as st
import pandas as pd

# Создаем образец данных
data = {'Имя': ['Алуа', 'Ерлан', 'Ернар', 'Максат', 'Рамазан', 'Рамазан']}
df = pd.DataFrame(data)

# Создаем список вариантов для выпадающего меню
options = ['Спланк', 'Тикет', 'АЦ']

# Создаем функцию для обновления данных в таблице
def update_df():
    for i in range(len(df)):
        new_value = selected_values[i]
        df.loc[i, 'Канал'] = new_value
    st.dataframe(df)

# Создаем интерфейс Streamlit
st.title('Таблица с выпадающими меню')

# Добавляем новый столбец с выпадающими меню
df['Канал'] = ''
selected_values = []
for index, row in df.iterrows():
    selected_values.append(st.selectbox(f"Выбор {row['Имя']}", options))

# Кнопка для обновления таблицы
st.button('Обновить', on_click=update_df)
