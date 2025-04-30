import requests
import json

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyse } }
    res = requests.post(url, json = obj, headers = header)

    if res.status_code == 200:
        parsed = json.loads(res.text)
        
        emotions = parsed['emotionPredictions'][0]['emotion']

        highest = { "emotion": "", "value": 0 }
        for emotion in emotions:
            if emotions[emotion] > highest['value']:
                highest = {
                    "emotion": emotion,
                    "value": emotions[emotion]
                }

        emotions['dominant_emotion'] = highest['emotion']
    elif res.status_code == 400:
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }

    return emotions