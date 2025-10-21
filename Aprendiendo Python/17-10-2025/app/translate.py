import requests
from flask_babel import _
from app import app


def translate(text, source_language, dest_language):
    url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        "q": text,
        "source": source_language,
        "target": dest_language
    }
    headers = {
        "x-rapidapi-key": app.config['MS_TRANSLATOR_KEY'],
        "x-rapidapi-host": "deep-translate1.p.rapidapi.com",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)

    # return response.json()['data']['translations']['translatedText'][0]
