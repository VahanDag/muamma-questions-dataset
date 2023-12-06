import json

import requests

data = {}

url = "https://opentdb.com/api.php?amount=10&category=23&type=multiple"

api_get = requests.get(url)

data = json.loads(api_get.text)

questions = data["results"]

