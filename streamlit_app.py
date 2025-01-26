import streamlit as st
import pandas as pd

# Создаем DataFrame (пример)
data = {'Имя': ['Алиса', 'Борис', 'Вера'],
        'Возраст': [25, 30, 22],
        'Город': ['Москва', 'Санкт-Петербург', 'Новосибирск']}
df = pd.DataFrame(data)

# Заголовок приложения
st.title('Пример таблицы в Streamlit')

# Отображаем таблицу
st.table(df)
