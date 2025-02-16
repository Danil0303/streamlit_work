import streamlit as st
import pandas as pd


class DataEditorApp:
    def __init__(self):
        # Инициализация заголовка приложения
        if 'selected_button' not in st.session_state:
            st.session_state.selected_button = None
            self.create_sidebar()
        elif st.session_state.selected_button in ['Clickhouse','SQL']:
            self.show_container()

    def create_sidebar(self):
        # Сайдбар с кнопками
        st.sidebar.title("Выберите опцию")

        # Если состояние с контейнером не инициализировано, создаём его

        # Обработка нажатий кнопок
        if st.sidebar.button("Clickhouse", use_container_width=True):
            self.toggle_container("Clickhouse")

        if st.sidebar.button("SQL", use_container_width=True):
            self.toggle_container("SQL")

    def toggle_container(self, button_name):
        # Переключение состояния контейнера
        if st.session_state.selected_button == button_name:
            st.session_state.selected_button = None  # Закрыть контейнер
        else:
            st.session_state.selected_button = button_name  # Открыть контейнер

        self.show_container()

    def show_container(self):
        if st.session_state.selected_button:
            self.create_container(st.session_state.selected_button)

    def create_container(self, button_name):
        st.header(button_name)

        # Создаем пример данных для таблицы
        data = {
            'Column 1': ['Value 1', 'Value 2', 'Value 3'],
            'Column 2': ['Value A', 'Value B', 'Value C']
        }

        # Создаем DataFrame и используем data_editor для редактирования
        df = pd.DataFrame(data)

        # Используем session_state для хранения отредактированных данных
        if f'edited_df_{button_name}' not in st.session_state:
            st.session_state[f'edited_df_{button_name}'] = df

        edited_df = st.data_editor(
            data=st.session_state[f'edited_df_{button_name}'],
            key=f'editor_{button_name}',  # Изменено ключ для редактора
            num_rows="dynamic",
            use_container_width=True
        )

        # Кнопка для сохранения данных
        if st.button(f"Сохранить {button_name}", use_container_width=True):
            st.session_state[f'edited_df_{button_name}'] = edited_df
            st.success(f"Данные для {button_name} успешно сохранены!")
            st.write(st.session_state[f'edited_df_{button_name}'])


# Запуск приложения
DataEditorApp()
