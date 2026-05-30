import streamlit as st
from Services.youtube_service import youtube_links

st.title("📚 YouTube Resources")

if "current_course" not in st.session_state:

    st.warning("⚠️ Generate a course first")

    st.stop()

data = st.session_state["current_course"]
for topic in data["learning_plan"]["plan"]:
    st.markdown("---")
    st.markdown(f"### {topic['step']}. {topic['title']}")

    videos = topic["videos"]

    st.markdown("---")

    for idx, video in enumerate(topic["videos"], start=1):
        col_video, col_text = st.columns([2, 3])

        with col_video:
            st.video(video["url"])

        with col_text:
            st.markdown("""
            <style>
            .custom-title {
                font-family: 'Trebuchet MS', sans-serif;
                font-size: 22px;
                color: #C9C0BB;
                font-weight: bold;
            }
            </style>
            """, unsafe_allow_html=True)


            st.markdown(
                f"<div class='custom-title'>{video['title']}</div>",
                unsafe_allow_html=True
            )
                