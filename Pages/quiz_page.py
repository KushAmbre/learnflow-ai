import streamlit as st
from Services.mcq_service import generate_course_mcqs

st.title("🧠 Course Assessment")

# =========================================
# CHECK COURSE EXISTS
# =========================================

if "current_course" not in st.session_state:

    st.warning("⚠️ Generate a course first")

    st.stop()

# =========================================
# GET COURSE DATA
# =========================================

course_data = st.session_state["current_course"]

course_name = course_data["title"]

level = course_data["level"]

learning_plan = course_data["learning_plan"]["plan"]

# =========================================
# EXTRACT TOPIC NAMES
# =========================================

topics = []

for topic in learning_plan:

    topics.append(topic["title"])

# =========================================
# SESSION STATE
# =========================================

if "course_mcqs" not in st.session_state:

    st.session_state.course_mcqs = []

if "course_submitted" not in st.session_state:

    st.session_state.course_submitted = False

# =========================================
# COURSE INFO
# =========================================

st.header(f"📘 {course_name}")

st.write(f"🎯 Level: {level}")

st.subheader("📚 Included Topics")

for i, topic in enumerate(topics):

    st.write(f"{i+1}. {topic}")

st.markdown("---")

# =========================================
# GENERATE COURSE MCQS
# =========================================

st.info(
    "⚠️ Please wait until assessment generation completes before switching pages."
)

if st.button("Generate Full Course Assessment"):

    with st.spinner(
        "Generating assessment... This may take 1-2 mins."
    ):

        mcqs = generate_course_mcqs(
            course_name=course_name,
            level=level,
            topics=topics
        )

        st.session_state.course_mcqs = mcqs

        st.session_state.course_submitted = False

    st.rerun()

# =========================================
# DISPLAY MCQS
# =========================================

mcqs = st.session_state.course_mcqs

if mcqs:

    st.success(
        f"✅ {len(mcqs)} Questions Generated"
    )

    with st.form("course_quiz_form"):

        user_answers = {}

        # ---------------------------------
        # QUESTIONS
        # ---------------------------------

        for i, q in enumerate(mcqs):

            # Difficulty Labels
            if i < 10:
                difficulty = "🟢 Easy"

            elif i < 20:
                difficulty = "🟠 Medium"

            else:
                difficulty = "🔴 Hard"

            st.markdown(
                f"### Q{i+1}. {q['question']}"
            )

            st.caption(difficulty)

            user_answers[i] = st.radio(
                "Choose your answer:",
                q["options"],
                key=f"course_q_{i}"
            )

            # ---------------------------------
            # FEEDBACK AFTER SUBMISSION
            # ---------------------------------

            if st.session_state.course_submitted:

                if user_answers[i] == q["answer"]:

                    st.success("✅ Correct")

                else:

                    st.error(
                        f"❌ Correct Answer: "
                        f"{q['answer']}"
                    )

            st.markdown("---")

        # ---------------------------------
        # SUBMIT BUTTON
        # ---------------------------------

        submit_button = st.form_submit_button(
            "Submit Assessment"
        )

        if submit_button:

            st.session_state.course_submitted = True

            st.rerun()

    # =====================================
    # FINAL SCORE
    # =====================================

    if st.session_state.course_submitted:

        score = 0

        for i, q in enumerate(mcqs):

            if user_answers[i] == q["answer"]:

                score += 1

        total_questions = len(mcqs)

        percentage = (
            score / total_questions
        ) * 100

        st.success(
            f"🎯 Final Score: "
            f"{score}/{total_questions}"
        )

        st.progress(percentage / 100)

        st.write(
            f"📊 Percentage: "
            f"{percentage:.2f}%"
        )

        # =================================
        # PERFORMANCE MESSAGE
        # =================================

        if percentage >= 80:

            st.success(
                "🏆 Excellent Performance!"
            )

        elif percentage >= 60:

            st.info(
                "👍 Good Understanding!"
            )

        else:

            st.warning(
                "📚 Needs More Practice"
            )

else:

    st.info(
        "Click 'Generate Full Course Assessment'"
    )