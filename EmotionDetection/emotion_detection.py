"""Emotion detection client for the Watson NLP service."""

import json
from typing import Any

import requests


EMOTION_NAMES = ("anger", "disgust", "fear", "joy", "sadness")
SERVICE_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_HEADER = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
}


def _empty_result() -> dict[str, Any]:
    """Return the required result shape for invalid input."""
    return {emotion: None for emotion in EMOTION_NAMES} | {
        "dominant_emotion": None
    }


def emotion_detector(text_to_analyse: str) -> dict[str, Any]:
    """Return emotion scores and the dominant emotion for the supplied text."""
    payload = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(
        SERVICE_URL,
        json=payload,
        headers=MODEL_HEADER,
        timeout=30,
    )

    if response.status_code == 400:
        return _empty_result()

    response.raise_for_status()
    data = json.loads(response.text)
    emotions = data["emotionPredictions"][0]["emotion"]
    result = {emotion: emotions[emotion] for emotion in EMOTION_NAMES}
    result["dominant_emotion"] = max(
        EMOTION_NAMES,
        key=lambda emotion: result[emotion],
    )
    return result
