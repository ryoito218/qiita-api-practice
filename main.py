import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

url = 'https://qiita.com/api/v2/items'
headers = {'Authorization': f'Bearer {API_KEY}'}
params = {'page': 1, 'per_page': 10, 'query': 'title:python'}

response = requests.get(url, headers=headers, params=params)
data = response.json()

for item in data:
    print(item['title'])