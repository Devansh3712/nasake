import os

from transformers import pipeline, Pipeline

current_path = os.path.dirname(os.path.realpath(__file__))

moods = {
    "admiration": 0.8,
    "amusement": 0.9,
    "anger": 0.3,
    "annoyance": 0.4,
    "approval": 0.7,
    "caring": 0.8,
    "confusion": 0.4,
    "curiosity": 0.6,
    "desire": 0.7,
    "disappointment": 0.3,
    "disapproval": 0.3,
    "disgust": 0.2,
    "embarrassment": 0.4,
    "excitement": 1,
    "fear": 0.2,
    "gratitude": 0.8,
    "grief": 0.1,
    "joy": 1,
    "love": 0.9,
    "nervousness": 0.3,
    "optimism": 0.8,
    "pride": 0.8,
    "realization": 0.7,
    "relief": 0.7,
    "remorse": 0.2,
    "sadness": 0.1,
    "surprise": 0.8,
    "neutral": 0.5,
}


def calculate_mood(emotions: dict[str, float]) -> float:
    mood = 0.0
    for emotion in emotions:
        mood += moods[emotion] * emotions[emotion]
    return mood / 100


def emotion_analyzer() -> Pipeline:
    analyzer = ...
    model_path = os.path.join(current_path, "models/emotion")
    if os.path.isdir(model_path):
        analyzer = pipeline("text-classification", model_path, top_k=None)
    else:
        analyzer = pipeline(
            "text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None
        )
        analyzer.save_pretrained(model_path)
    return analyzer
