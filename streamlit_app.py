import streamlit as st
import pandas as pd

def create_table_with_dropdown(data, options_channel, options_lunch):
    df = pd.DataFrame(data)
    df['Канал'] = ''
    df['Обед'] = ''
    selected_values_channel = []
    selected_values_lunch = []

    st.title('Распределение')

    for index, row in df.iterrows():
        unique_identifier = f"{row['Имя']} ({index+1})"
        selected_values_channel.append(st.selectbox(f"Выбор канала для {unique_identifier}", options_channel))
        selected_values_lunch.append(st.selectbox(f"Время обеда для {unique_identifier}", options_lunch))

    def update_df():
        for i in range(len(df)):
            df.loc[i, 'Канал'] = selected_values_channel[i]
            df.loc[i, 'Обед'] = selected_values_lunch[i]
        st.dataframe(df)

    st.button('Обновить', on_click=update_df)

    return df

# Данные для таблиц
data = {'Имя': ['Спец', 'Спец2', 'Спец3', 'Спец4', 'Спец5']}
options_channel = ['Сп', 'Ткт', 'АЦ']
options_lunch = ['12:00', '13:00', '14:00', '15:00']

# Сохранение результатов (пример)
def save_results(df):
    if st.button("Сохранить результаты"):
        df.to_csv("results.csv", index=False)
        st.success("Результаты сохранены в файл results.csv")

# Создание таблицы и кнопок навигации
if st.session_state.page == "page1":
    df = create_table_with_dropdown(data, options_channel, options_lunch)
    save_results(df)
elif st.session_state.page == "page2":
    # Содержимое второй страницы
    st.write("Это страница 2")
    # ... ваш код для второй страницы
else:
    st.write("Содержимое третьей страницы")
    # ... ваш код для третьей страницы

# Кнопки для переключения страниц
pages = ["page1", "page2", "page3"]
selected_page = st.radio("Выберите страницу", pages)
st.session_state.page = selected_page
