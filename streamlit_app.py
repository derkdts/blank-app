import streamlit as st
import pandas as pd

def create_table_with_dropdown(data, options):
    df = pd.DataFrame(data)
    df['Канал'] = ''
    selected_values = []

    st.title('Таблица с выпадающими меню')

    for index, row in df.iterrows():
        # Добавляем порядковый номер для пользователей с одинаковыми именами
        unique_identifier = f"{row['Имя']} ({index+1})"
        selected_values.append(st.selectbox(f"Выбор для {unique_identifier}", options))

    def update_df():
        for i in range(len(df)):
            new_value = selected_values[i]
            df.loc[i, 'Канал'] = new_value
        st.dataframe(df)

    st.button('Обновить', on_click=update_df)

    return df

# Пример использования
data = {'Имя': ['Алуа', 'Ерлан', 'Ернар', 'Максат', 'Рамазан']}
options = ['Спланк', 'Тикет', 'АЦ']
df = create_table_with_dropdown(data, options)

# Сохранение результатов (пример)
if st.button("Сохранить результаты"):
    df.to_csv("results.csv", index=False)
    st.success("Результаты сохранены в файл results.csv")
