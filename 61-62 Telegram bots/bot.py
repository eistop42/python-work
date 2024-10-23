import requests

token = ''

url = f'https://api.telegram.org/bot{token}/getUpdates'

url_send = f'https://api.telegram.org/bot{token}/sendMessage'


user_bot = 158448812
data = {'chat_id': user_bot, 'text': 'погода не очень'}
res = requests.get(url)




print(res.json())