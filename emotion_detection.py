import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }

    resp = requests.post(url=url, json=obj, headers=headers).text
    emotions = json.loads(resp)["emotionPredictions"][0]["emotion"]

    emotions["dominant_emotion"] = max(emotions, key = lambda x: emotions[x])

    return emotions