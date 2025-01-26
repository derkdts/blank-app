import streamlit as st
import pandas as pd

def create_table_with_dropdown(data, options):
    df = pd.DataFrame(data)
    df['Обед'] = ''  # Добавляем новый столбец "Обед"
    selected_values = []

    st.title('Распределение')

    for index, row in df.iterrows():
        unique_identifier = f"{row['Имя']} ({index+1})"
        selected_values.append(st.selectbox(f"Время обеда для {unique_identifier}", options))

    def update_df():
        for i in range(len(df)):
            new_value = selected_values[i]
            df.loc[i, 'Обед'] = new_value
        st.dataframe(df)

    st.button('Обновить', on_click=update_df)

    return df

# Данные для таблиц
data = {'Имя': ['Алуа', 'Ерлан', 'Ернар', 'Максат', 'Рамазан']}
options = ['12:00', '13:00', '14:00', '15:00']

df = create_table_with_dropdown(data, options)

# Сохранение результатов (пример)
if st.button("Сохранить результаты"):
    df.to_csv("results.csv", index=False)
    st.success("Результаты сохранены в файл results.csv")
