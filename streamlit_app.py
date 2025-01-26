import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

# Исходные данные
data = {'Имя': ['Спец', 'Спец2', 'Спец3', 'Спец4', 'Спец5'],
        'Канал': ['Сп', 'Ткт', 'АЦ', 'Сп', 'Ткт'],
        'Обед': ['12:00', '13:00', '14:00', '15:00', '12:00']}
df = pd.DataFrame(data)

# Список возможных значений для столбцов
channels = ['Сп', 'Ткт', 'АЦ', 'Другой']
lunch_times = ['12:00', '13:00', '14:00', '15:00']

def create_app():
    # Вкладки
    tab1, tab2 = st.tabs(["Редактирование", "Просмотр"])

    with tab1:
        # Создаем словарь для конфигурации столбцов
        columnDefs = [
            {
                'headerName': 'Канал',
                'field': 'Канал',
                'cellEditor': 'agSelectCellEditor',
                'cellEditorParams': {'values': channels}
            },
            {
                'headerName': 'Обед',
                'field': 'Обед',
                'cellEditor': 'agSelectCellEditor',
                'cellEditorParams': {'values': lunch_times}
            }
        ]

        # Создаем таблицу с помощью AgGrid
        gridOptions = {'columnDefs': columnDefs, 'rowData': df.to_dict('records')}
        grid_response = AgGrid(
            df,
            gridOptions=gridOptions,
            enable_enterprise_modules=True,
            fit_columns_on_grid_load=True,
            height=350
        )

        # Получаем обновленные данные из таблицы
        edited_df = pd.DataFrame(grid_response['data'])

        # Кнопка сохранения
        if st.button("Сохранить изменения"):
            st.session_state.original_df = edited_df
            st.success("Данные сохранены")

    with tab2:
        # Таблица для просмотра
        st.dataframe(st.session_state.original_df, use_container_width=True)

# Сохраняем исходные данные в сессии
if 'original_df' not in st.session_state:
    st.session_state.original_df = df.copy()

# Запускаем приложение
create_app()
