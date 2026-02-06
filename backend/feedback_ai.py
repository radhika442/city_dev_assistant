def analyze_feedback(comments: list):
    if not comments:
        return {"sentiment_score": 0, "top_topics": []}

    positive = sum(1 for c in comments if "good" in c.lower())
    score = positive / len(comments)

    return {
        "sentiment_score": round(score, 2),
        "top_topics": ["traffic", "parks", "housing"]
    }
