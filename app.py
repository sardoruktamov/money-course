import requests
import json
from pprint import pprint as print

inputs = str(input('valyuta kiriting: '))

url = 'https://v6.exchangerate-api.com/v6/e06e1270a84ce6eb8b4c162a/latest/'+inputs

response = requests.get(url)
res = json.loads(response.text)
print(res['conversion_rates']['UZS'])