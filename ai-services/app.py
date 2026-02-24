from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

# Load emotion model (RoBERTa based)
classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

@app.get("/")
def home():
    return {"message": "MoodGuard AI Service Running"}

@app.post("/analyze")
def analyze_text(data: dict):
    text = data["text"]

    result = classifier(text)[0]

    emotions = {}
    for item in result:
        emotions[item["label"]] = round(item["score"], 3)

        dominant_emotion = max(emotions, key=emotions.get)

        mood_score = int(emotions.get("joy", 0) * 100)

        return{
            "text"
        }


