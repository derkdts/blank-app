import streamlit as st
import pandas as pd

def create_table(data, options_channel, options_lunch):
    """Создает таблицу с выпадающими списками для выбора канала и времени обеда.

    Args:
        data: Словарь с данными для таблицы.
        options_channel: Список вариантов для канала.
        options_lunch: Список вариантов для времени обеда.
    """
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

def save_results(df):
    if st.button("Сохранить результаты"):
        df.to_csv("results.csv", index=False)
        st.success("Результаты сохранены в файл results.csv")

def page1():
    data = {'Имя': ['Спец', 'Спец2', 'Спец3', 'Спец4', 'Спец5']}
    options_channel = ['Сп', 'Ткт', 'АЦ']
    options_lunch = ['12:00', '13:00', '14:00', '15:00']
    df = create_table_with_dropdown(data, options_channel, options_lunch)
    save_results(df)

def page2():
    st.write("Это страница 2")
    # Здесь будет код для второй страницы

# Сохранение текущей страницы в сессии
if 'page' not in st.session_state:
    st.session_state.page = "page1"

# Кнопки для переключения страниц
pages = ["page1", "page2", "page3"]
selected_page = st.radio("Выберите страницу", pages)
st.session_state.page = selected_page

# Отображение содержимого в зависимости от страницы
page_functions = {
    "page1": page1,
    "page2": page2,
    "page3": lambda: st.write("Содержимое третьей страницы")
}
page_functions[st.session_state.page]()
