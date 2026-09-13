import unittest
from EmotionPredict.emotionPredict_analysis import emotionPredict_analyzer


class TestEmotionPredictAnalyzer(unittest.TestCase):
	 def test_sentiment_analyzer(self):
            # Test case for positive sentiment
            result_1 = emotionPredict_analyzer('I am glad this happened')
            self.assertEqual(result_1['label'], 'joy')
            # Test case for negative sentiment
            result_2 = emotionPredict_analyzer('I am really mad about this')
            self.assertEqual(result_2['label'], 'anger')
            # Test case for neutral sentiment
            result_3 = emotionPredict_analyzer('I feel disgusted just hearing about this')
            self.assertEqual(result_3['label'], 'disgust')
            # Test case for neutral sentiment
            result_3 = emotionPredict_analyzer('I am so sad about this')
            self.assertEqual(result_3['label'], 'sadness')
            # Test case for neutral sentiment
            result_3 = emotionPredict_analyzer('I am really afraid that this')
            self.assertEqual(result_3['label'], 'fear')
    


if __name__ == "__main__":
	unittest.main()
