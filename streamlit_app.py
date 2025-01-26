import streamlit as st
import pandas as pd

def create_table_with_dropdown(data, options, table_name):
    df = pd.DataFrame(data)
    df['Канал'] = ''
    selected_values = []

    st.title(f'Таблица {table_name}')

    for index, row in df.iterrows():
        unique_identifier = f"{row['Имя']} ({index+1})"
        selected_values.append(st.selectbox(f"Выбор для {unique_identifier}", options))

    def update_df():
        for i in range(len(df)):
            new_value = selected_values[i]
            df.loc[i, 'Канал'] = new_value
        st.dataframe(df)

    st.button('Обновить', on_click=update_df)

    return df

# Первая таблица
data1 = {'Имя': ['Алуа', 'Ерлан', 'Ернар'], 'Канал': ''}
options1 = ['Спланк', 'Тикет', 'АЦ']
df1 = create_table_with_dropdown(data1, options1, 'Таблица 1')

# Вторая таблица
data2 = {'Имя': ['Максат', 'Рамазан', 'Рамазан'], 'Канал': ''}
options2 = ['Email', 'Телефон', 'Встреча']
df2 = create_table_with_dropdown(data2, options2, 'Таблица 2')
