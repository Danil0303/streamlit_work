import streamlit as st

pages = {
    "База данных": [
        st.Page("pages/databases.py", title="База данных"),
    ],
    "Документация": [
        st.Page("pages/documentation.py", title="Документация"),
    ],
}

pg = st.navigation(pages)
pg.run()