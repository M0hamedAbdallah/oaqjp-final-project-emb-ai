import requests , json

def emotionPredict_analyzer(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text)

    # Extracting emotion label and score from the response
    label = formatted_response['documentEmotion']['label']
    score = formatted_response['documentEmotion']['score']

    # Returning a dictionary containing emotion analysis results
    return {'label': label, 'score': score}