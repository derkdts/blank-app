import streamlit as st
import pandas as pd

def create_table_with_dropdown(data, options, table_name):
    """
    Создает таблицу с выпадающим меню для выбора значения для каждой строки.

    Args:
        data: Словарь или DataFrame с данными для таблицы.
        options: Список возможных значений для выпадающего меню.
        table_name: Название таблицы для отображения в интерфейсе.

    Returns:
        DataFrame с обновленными данными.
    """
    df = pd.DataFrame(data)
    df['Канал'] = ''
    selected_values = []

    st.title(f'Распределение {table_name}')

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

# Данные для таблиц
data1 = {'Имя': ['Алуа', 'Ерлан', 'Ернар']}
options1 = ['Спланк', 'Тикет', 'АЦ']
data2 = {'Имя': ['Максат', 'Рамазан', 'Рамазан']}
options2 = ['Email', 'Телефон', 'Встреча']

# Создание таблиц
df1 = create_table_with_dropdown(data1, options1, 'Таблица 1')
df2 = create_table_with_dropdown(data2, options2, 'Таблица 2')

# Сохранение результатов (пример)
if st.button("Сохранить результаты"):
    with st.expander("Результаты"):
        st.subheader("Таблица 1")
        st.dataframe(df1)
        st.subheader("Таблица 2")
        st.dataframe(df2)
