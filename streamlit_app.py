import streamlit as st
import pandas as pd

# Создаем образец данных
data = {'Имя': ['Алуа', 'Ерлан', 'Ернар', 'Максат', 'Рамазан', 'Рамазан']}
df = pd.DataFrame(data)

# Создаем список вариантов для выпадающего меню
options = ['Спланк', 'Тикет', 'АЦ']

# Создаем функцию для обновления данных в таблице
def update_df(new_value):
    df.loc[selected_index, 'Канал'] = new_value
    st.dataframe(df)

# Создаем интерфейс Streamlit
st.title('Таблица с выпадающим меню')

# Отображаем таблицу
st.dataframe(df)

# Добавляем новый столбец с выпадающим меню
df['Канал'] = ''
selected_index = st.number_input('Выберите индекс строки', min_value=0, max_value=len(df)-1, value=0)
new_value = st.selectbox('Выберите значение', options)
st.button('Обновить', on_click=update_df, args=(new_value,))
