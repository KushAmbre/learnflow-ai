Learning_Plan_Prompt = """
    You are an expert AI Course Designer.

    Create a COMPLETE learning plan for the entire course.

    Course: {course}
    Level: {level}
    Schedule: {schedule}

    Rules:
    - Generate EXACTLY {steps} steps
    - Beginner: fundamentals → basics → practice
    - Intermediate: concepts → applied usage
    - Advanced: real-world + project-driven topics
    - Each step should take 30–45 minutes
    - Steps must be progressive (no repetition)
    - Give the course title search friendly so when we search the topic title on youtube it gives only the required answer

    Return ONLY valid JSON in this EXACT format:
    {{
    "course": "{course}",
    "level": "{level}",
    "schedule": "{schedule}",
    "plan": [
        {{
        "step": 1,
        "title": "Topic Title",
        "description": "2–3 lines explaining what the learner will study.",
        "outcome": "One clear skill the learner gains"
        }}
    ]
    }}

    IMPORTANT:
    - The plan array MUST contain {steps} items
    - No markdown
    - No comments

    ABSOLUTE RULES (DO NOT BREAK):
    - Output MUST start with {{
    - Output MUST end with }}
    - NO text before or after JSON
    - NO explanations
    - NO thinking"""



MCQ_PROMPT = """
Generate EXACTLY {count} {difficulty}
difficulty MCQs for a {level}
level course on {course_name}.

Topics:
{topic_text}

STRICT RULES:
- Return ONLY valid JSON array
- No markdown
- No explanation
- Questions must be UNIQUE
- Do NOT repeat concepts
- Each question must test a different idea
- Each question must contain:
    - question
    - options
    - answer
- Each question must have EXACTLY 4 options
- answer must EXACTLY match one option

Example:
[
    {{
        "question": "What is Python?",
        "options": [
            "Programming Language",
            "Snake",
            "Browser",
            "Game"
        ],
        "answer": "Programming Language"
    }}
]
"""