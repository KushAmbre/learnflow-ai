import re

def extract_json(text):

    match = re.search(
        r"\[.*\]",
        text,
        re.DOTALL
    )

    return match.group(0) if match else None



def clean_mcqs(mcqs):

    valid_mcqs = []

    for q in mcqs:

        question = q.get("question")

        options = q.get("options")

        answer = q.get("answer")

        if (
            question
            and options
            and answer
            and isinstance(options, list)
            and len(options) == 4
            and answer in options
        ):

            valid_mcqs.append({
                "question": question,
                "options": options,
                "answer": answer
            })

    return valid_mcqs


def remove_duplicate_mcqs(mcqs):

    unique_mcqs = []

    seen = set()

    for q in mcqs:

        question = (
            q["question"]
            .strip()
            .lower()
        )

        if question not in seen:

            seen.add(question)

            unique_mcqs.append(q)

    return unique_mcqs



