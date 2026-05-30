import ast
from youtubesearchpython import VideosSearch

def youtube_links(topic, level, course):

    # -------- SAFETY LAYER --------
    topic = topic or "General Topic"
    course = course or "Course"
    level = level or "Beginner"

    try:
        query = f"{topic} in {course} tutorial {level}"

        search = VideosSearch(query, limit=3)
        results = search.result()

        videos = []

        for v in results.get("result", []):
            videos.append({
                "title": v.get("title", "No Title"),
                "url": v.get("link", "")
            })

        return videos

    except Exception as e:
        print("YouTube Error:", e)
        return []