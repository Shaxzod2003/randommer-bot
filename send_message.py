from settings import URL
import requests

endpoint="/sendMessage"
url = URL+endpoint

def send_message(chat_id, text):
    payload = {
        "chat_id": chat_id,
        "text": text,
    }
    requests.get(url, params=payload)

send_message('5451611180', 'hi shaxzod')
