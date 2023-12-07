import json

import requests

from openai import OpenAI

# client = OpenAI()
url = "https://opentdb.com/api.php?amount=8&category=23&type=multiple"
data = {}
questions_options = []

api_get = requests.get(url)
data = json.loads(api_get.text)
questions = data["results"]

# print(questions)

for i in range(len(questions)):
    questions_options.append({
        'question': questions[i]["question"],
        'correct_answer': questions[i]["correct_answer"],
        'incorrect_answers': questions[i]["incorrect_answers"],
    })

for i in questions_options:
    print(i)
# for question in questions:
#     completition = client.chat.completions.create(
#         model= "gpt-3.5-turbo",
#         messages= [
#             {"role": "system", "content": "You are a super assistant designed to output JSON"}
#             {"role": "user", "content": """I will give you questions with 4 options. These questions must have 5 options. Therefore, in order to complete each question with 5 options, I want you to produce an incorrect option related to that question.

# Expected list: ["option for question1 here", "option for question2 here"] 

# here is questions {}

# """}
#         ]
#     )


