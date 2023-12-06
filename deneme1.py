import json

import requests

data = {}

url = "https://opentdb.com/api.php?amount=99"

api_get = requests.get(url)

data = json.loads(api_get.text)

questions = data["results"]

print(len(questions))
