import streamlit as st
import copy
from Services.roadmap_service import generate_learning_plan  # <-- your plan generator
from Services.youtube_service import youtube_links

if "saved_courses" not in st.session_state:
    st.session_state["saved_courses"] = []

st.title("LearnFlow AI")
st.subheader("What do you want to learn and at what level?")

# Course
course = st.text_input("Enter the course")
if " " in course:
    course = course.replace(" ", "-")

# Level
level = st.selectbox(
    "Select Level",
    ("Beginner", "Intermediate", "Advanced"),
    index=None,
    placeholder="Level..."
)
st.write("You selected:", level)

# -------------------------------
# Generate Course
# -------------------------------
if st.button("Generate Learning Plan"):
    if course.strip() == "":
        st.error("Fill which course you want to learn")
    elif not level:
        st.error("Pls select the Level")
    else:
        # Learning Plan
        progress = st.progress(0)

        progress.progress(20)
        learning_plan = generate_learning_plan(course, level)

        progress.progress(50)
        for topic in learning_plan['plan']:
            topic['videos'] = youtube_links(topic["title"], level, course)

        progress.progress(100)

        st.session_state["current_course"] = {
            "title": course,
            "level": level,
            "schedule": "Daily",
            "learning_plan": learning_plan,
        }

        st.success(f"Generated Course: {course} ({level})")

# ===============================
# Render Course (STATIC SECTION)
# ===============================
if "current_course" in st.session_state:
    data = st.session_state["current_course"]

    # -------- Learning Plan (FIXED) --------
    st.markdown("## 📘 Learning Plan")
    st.markdown("---")

    for topic in data["learning_plan"]["plan"]:
        st.markdown(f"### {topic['step']}. {topic['title']}")
        st.write(topic["description"])
        st.caption(f"🎯 Outcome: {topic['outcome']}")
        st.markdown("---")