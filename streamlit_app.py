import streamlit as st
import pandas as pd
import plotly.express as px

# Data for the table
data = {'Имя': ['Спец', 'Спец2', 'Спец3', 'Спец4', 'Спец5'],
        'Канал': ['Сп', 'Ткт', 'АЦ', 'Сп', 'Ткт'],
        'Обед': ['12:00', '13:00', '14:00', '15:00', '12:00']}
df = pd.DataFrame(data)

# Function to create an editable table
def create_editable_table(df):
    # ... (code for creating an editable table)

def create_chart(df):  # Add indentation here
    """
    This function creates a chart to visualize the data in the DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data to be visualized.

    Returns:
        plotly.express.Figure: The chart created from the DataFrame.
    """
    # ... (code for creating a chart)
    return fig  # Assuming the chart is assigned to the variable 'fig'

# Tabs
tab1, tab2, tab3 = st.tabs(["Данные", "Анализ", "Настройки"])

with tab1:
    df = create_editable_table(df)
    save_button = st.button("Сохранить изменения")
    if save_button:
        # Save data to file or database

with tab2:
    fig = create_chart(df)
    st.plotly_chart(fig)

with tab3:
    # App settings (e.g., select theme)
    st.selectbox("Выберите тему", ["Светлая", "Темная"])
