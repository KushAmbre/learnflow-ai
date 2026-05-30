import json
from Utils.prompt import MCQ_PROMPT
from Utils.parsers import extract_json, clean_mcqs, remove_duplicate_mcqs
from Services.llm_service import get_llm

def generate_mcqs_by_difficulty(
    course_name,
    level,
    topics,
    difficulty,
    count
):

    topic_text = "\n".join(
        [f"- {topic}" for topic in topics]
    )

    prompt = MCQ_PROMPT.format(
        course_name=course_name,
        level=level,
        topic_text=topic_text,
        difficulty=difficulty,
        count=count
    )

    try:

        llm_model = get_llm()

        content = llm_model.invoke(prompt)

        json_text = extract_json(content)

        if not json_text:

            return []

        mcqs = json.loads(json_text)

        cleaned_mcqs = clean_mcqs(mcqs)

        return cleaned_mcqs

    except Exception as e:

        print(f"MCQ Generation Error: {e}")

        return []

# =========================================
# MAIN FUNCTION
# =========================================

def generate_course_mcqs(
    course_name,
    level,
    topics
):

    # -------------------------------------
    # Generate Separate Difficulty Sets
    # -------------------------------------

    easy_mcqs = generate_mcqs_by_difficulty(
        course_name=course_name,
        level=level,
        topics=topics,
        difficulty="Easy",
        count=10
    )

    medium_mcqs = generate_mcqs_by_difficulty(
        course_name=course_name,
        level=level,
        topics=topics,
        difficulty="Medium",
        count=10
    )

    hard_mcqs = generate_mcqs_by_difficulty(
        course_name=course_name,
        level=level,
        topics=topics,
        difficulty="Hard",
        count=10
    )

    # -------------------------------------
    # Merge MCQs
    # -------------------------------------

    all_mcqs = (
        easy_mcqs
        + medium_mcqs
        + hard_mcqs
    )

    # -------------------------------------
    # Remove Duplicate Questions
    # -------------------------------------

    all_mcqs = remove_duplicate_mcqs(
        all_mcqs
    )

    return all_mcqs