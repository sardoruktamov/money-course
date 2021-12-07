import requests
import json

input = str(input('valyuta kiriting: '))

url = f'https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/USD'

response = requests.get(url)
rese = json.loads(response.text)