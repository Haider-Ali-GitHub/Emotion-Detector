import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}
    
    response = requests.post(url, headers=headers, json=data)
    response_dict = json.loads(response.text)
    
    emotions = response_dict['document_tone']['tones']
    scores = {tone['tone_id']: tone['score'] for tone in emotions}
    
    # Extract required emotions with default score 0.0 if not present
    required_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    emotion_scores = {emotion: scores.get(emotion, 0.0) for emotion in required_emotions}
    
    # Find the dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    return {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
    }
