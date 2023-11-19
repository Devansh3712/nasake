import os

from transformers import pipeline, Pipeline

current_path = os.path.dirname(os.path.realpath(__file__))


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
