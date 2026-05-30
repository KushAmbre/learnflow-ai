import streamlit as st

Page1 = st.Page(
    page = r"Pages\learning_plan_page.py",
    title = "Learn",
    icon="📘"
)

Page2 = st.Page(
    page = r"Pages\youtube_page.py",
    title = "Video",
    icon="🎥"
)

Page3 = st.Page(
    page = r"Pages\quiz_page.py",
    title = "Test",
    icon="🧠"
)

pages = [Page1, Page2, Page3]


pg = st.navigation(pages=pages)
pg.run()