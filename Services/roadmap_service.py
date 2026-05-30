from langchain_core.prompts import ChatPromptTemplate
from Services.llm_service import get_llm
from Utils.prompt import Learning_Plan_Prompt
import json

def generate_learning_plan(course, level, schedule="Daily"):

        if schedule == "Daily":
            steps = 10
        elif schedule == "3 Days a Week":
            steps = 6
        else:
            steps = 4

        prompt = ChatPromptTemplate.from_template(Learning_Plan_Prompt)

        chain = prompt | get_llm()

        response = chain.invoke({
        "course": course,
        "level": level,
        "schedule": schedule,
        "steps": steps
    })

        clean_text = (
            response
            .replace("```python", "")
            .replace("```", "")
            .strip()
        )

        print("========== RAW RESPONSE ==========")
        print(response)
        print("========== CLEAN TEXT ==========")
        print(clean_text)


        try:
            if not clean_text or not clean_text.strip().startswith("{"):
                raise ValueError("Model did not return valid JSON")

            return json.loads(clean_text)

        except Exception as e:
            print("Learning Plan Parsing Error:", e)
            return {
                "course": course,
                "level": level,
                "schedule": schedule,
                "plan": [
                    {
                        "step": 1,
                        "title": f"Introduction to {course}",
                        "description": f"Learn the basics of {course}.",
                        "outcome": f"Understand fundamentals of {course}"
                    }
                ]
            }