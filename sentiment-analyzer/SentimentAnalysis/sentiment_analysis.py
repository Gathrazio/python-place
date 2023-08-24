import requests
import json

def sentiment_analyzer(text_to_analyze):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 200:
        return {'label': json.loads(response.text)["documentSentiment"]['label'], 'score': json.loads(response.text)["documentSentiment"]['score']}
    else:
        return {'label': None, 'score': None}