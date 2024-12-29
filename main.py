import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

url = 'https://qiita.com/api/v2/items'
headers = {'Authorization': f'Bearer {API_KEY}'}
params = {'page': 1, 'per_page': 20, 'query': 'title:Udemy'}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()

    # for i in range(len(data)):
    #     print(i+1, data[i]["title"], data[i]["url"])
    #     print()

    if data:
        print(data[12]["title"])
        print(data[12]["rendered_body"])
        # print(data[12]["body"])
        print(data[12]["url"])
        # fields = data[0].keys()
        # print("フィールド名")
        # for field in fields:
        #     print(field)

else:
    print("エラー")

# for item in data:
#     print(item['title'])