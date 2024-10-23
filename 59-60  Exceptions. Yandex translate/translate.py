import requests

token = 'AQVNx-xYiG1GgnvTHG8-UF5Yw5p3PCuY92xGDuKz'
catalog = 'b1gtphdg2vndncqf33o7'

text = 'как тебя зовут?'

payload = {
    "sourceLanguageCode": "ru",
    "targetLanguageCode": "en",
    "format": "HTML",
    "texts": [
        f"{text}"
    ],
    "folderId": f"{catalog}",
    "speller": False
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Api-Key {token}"
}

url = 'https://translate.api.cloud.yandex.net/translate/v2/translate'
response = requests.post(url, json=payload, headers=headers)

print(response.json())
