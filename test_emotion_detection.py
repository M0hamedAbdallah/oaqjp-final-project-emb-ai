"""Unit tests for the emotion detector."""

import json
import unittest
from unittest.mock import patch

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_returns_all_emotions_and_dominant_emotion(self):
        api_response = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.8,
                        "disgust": 0.1,
                        "fear": 0.2,
                        "joy": 0.3,
                        "sadness": 0.4,
                    }
                }
            ]
        }

        with patch(
            "EmotionDetection.emotion_detection.requests.post"
        ) as post:
            post.return_value.status_code = 200
            post.return_value.text = json.dumps(api_response)

            result = emotion_detector("I am really mad about this")

        self.assertEqual(result["anger"], 0.8)
        self.assertEqual(result["disgust"], 0.1)
        self.assertEqual(result["fear"], 0.2)
        self.assertEqual(result["joy"], 0.3)
        self.assertEqual(result["sadness"], 0.4)
        self.assertEqual(result["dominant_emotion"], "anger")

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
