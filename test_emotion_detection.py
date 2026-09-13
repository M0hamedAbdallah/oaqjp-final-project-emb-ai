"""Unit tests for the emotion detector."""

import json
import unittest
from unittest.mock import patch

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def _detect_with_scores(self, scores):
        with patch(
            "EmotionDetection.emotion_detection.requests.post"
        ) as post:
            post.return_value.status_code = 200
            post.return_value.text = json.dumps({
                "emotionPredictions": [{"emotion": scores}]
            })
            return emotion_detector("Test statement")

    def test_detects_anger(self):
        result = self._detect_with_scores({
            "anger": 0.8, "disgust": 0.1, "fear": 0.2,
            "joy": 0.3, "sadness": 0.4,
        })
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_detects_disgust(self):
        result = self._detect_with_scores({
            "anger": 0.1, "disgust": 0.8, "fear": 0.2,
            "joy": 0.3, "sadness": 0.4,
        })
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_detects_fear(self):
        result = self._detect_with_scores({
            "anger": 0.1, "disgust": 0.2, "fear": 0.8,
            "joy": 0.3, "sadness": 0.4,
        })
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_detects_joy(self):
        result = self._detect_with_scores({
            "anger": 0.1, "disgust": 0.2, "fear": 0.3,
            "joy": 0.8, "sadness": 0.4,
        })
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_detects_sadness(self):
        result = self._detect_with_scores({
            "anger": 0.1, "disgust": 0.2, "fear": 0.3,
            "joy": 0.4, "sadness": 0.8,
        })
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_returns_empty_result_for_bad_request(self):
        with patch(
            "EmotionDetection.emotion_detection.requests.post"
        ) as post:
            post.return_value.status_code = 400

            result = emotion_detector("")

        self.assertIsNone(result["anger"])
        self.assertIsNone(result["disgust"])
        self.assertIsNone(result["fear"])
        self.assertIsNone(result["joy"])
        self.assertIsNone(result["sadness"])
        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
