import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

class Raspred:

# Инициализируем сессию для хранения данных
    def main(self):
        if 'user_input' not in st.session_state:
            st.session_state.user_input = pd.DataFrame(columns=['Дата', 'Фамилия'])

        # Выбор даты
        date = st.date_input("Выберите дату:",
                             value=(datetime.today() - timedelta(days=1)),
                             format='YYYY-MM-DD',
                             max_value=datetime.today())

        col_input, col_add, col_del = st.columns((2, 1, 1), vertical_alignment='bottom')

        with col_input:
            user_input = col_input.text_input(label="Введите ФИО оператора",
                                               placeholder="Петров Д.Д",
                                               help="Введите ФИО оператора, затем нажмите кнопку 'Добавить'",
                                               key='user_input_text')

        with col_add:
            if st.button("Добавить", use_container_width=True):
                if user_input:
                    new_row = pd.DataFrame({'Дата': [str(date)], 'Фамилия': [user_input]})
                    st.session_state.user_input = pd.concat([st.session_state.user_input, new_row], ignore_index=True)


        with col_del:
            if st.button("Удалить", use_container_width=True):
                if user_input in st.session_state.user_input["Фамилия"].values:
                    st.session_state.user_input = st.session_state.user_input[st.session_state.user_input["Фамилия"] != user_input]

        if not st.session_state.user_input.empty:
            st.subheader("Текущая таблица:")
            st.dataframe(st.session_state.user_input, use_container_width= True)
        else:
            st.subheader("Текущая таблица: (пусто)")





Raspred().main()