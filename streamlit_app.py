import streamlit as st
import pandas as pd

# Пример данных (замените на свои данные)
data = {'Дата': pd.date_range('2023-01-01', periods=100),
        'Продукт': ['A', 'B', 'C'] * 33,
        'Клиент': ['Клиент1', 'Клиент2', 'Клиент3'] * 33,
        'Сумма': np.random.randint(100, 1000, 100)}
df = pd.DataFrame(data)

# Фильтр по продукту
product_filter = st.selectbox('Выберите продукт', df['Продукт'].unique())
filtered_df = df[df['Продукт'] == product_filter]

# Отображение таблицы
st.dataframe(filtered_df)

# График продаж по месяцам
fig = px.line(filtered_df, x='Дата', y='Сумма', title='Динамика продаж')
st.plotly_chart(fig)
