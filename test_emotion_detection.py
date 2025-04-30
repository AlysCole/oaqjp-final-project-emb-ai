from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        expectJoy = emotion_detector("I am glad this happened")
        self.assertEqual(expectJoy['dominant_emotion'], 'joy')

        expectAnger = emotion_detector("I am really mad about this")
        self.assertEqual(expectAnger['dominant_emotion'], 'anger')

        expectDisgust = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(expectDisgust['dominant_emotion'], 'disgust')

        expectSadness = emotion_detector("I am so sad about this")
        self.assertEqual(expectSadness['dominant_emotion'], 'sadness')

        expectFear = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(expectFear['dominant_emotion'], 'fear')

unittest.main()