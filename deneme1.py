# import json

# import requests

# from openai import OpenAI

# client = OpenAI()
# url = "https://opentdb.com/api.php?amount=8&category=23&type=multiple"
# data = {}
# questions_options = []

# api_get = requests.get(url)
# data = json.loads(api_get.text)
# questions = data["results"]

# # print(questions)

# for i in range(len(questions)):
#     questions[i]["incorrect_answers"].append(questions[i]["correct_answer"])
#     questions_options.append({
#         'question': questions[i]["question"],
#         'options': questions[i]["incorrect_answers"],
#     })

# print(questions_options)
# for question in questions:
#     completion = client.chat.completions.create(
#         model= "gpt-3.5-turbo",
#         messages= [
#             {"role": "system", "content": "You are a super assistant"},
#             {"role": "user", "content": f"""Sana verdiğim her bir soru için yanlış bir seçenek üret ve bu seçenekleri bir listeye kaydedip yaz.
# Şu şekilde:
# ["birinci soru için üretilen yanlış şık","ikinci soru için üretilen yanlış şık".]

# İşte sorular ve mevcut şıklar: {questions_options}
# """}
#         ]
#     )


# print(completion.choices[0].message.content)


import json
import random

import requests

from openai import OpenAI

client = OpenAI()  # API anahtarınızı buraya girin

url = "https://opentdb.com/api.php?amount=8&category=9&type=multiple"
api_get = requests.get(url)
data = json.loads(api_get.text)
questions = data["results"]

extra_options = []

for question in questions:
    prompt = f"""Generate a wrong option: 
    Question: {question['question']}
    current options: {question['incorrect_answers'] + [question['correct_answer']]}
    Alert: Do not return anything except the wrong choice, and do not rewrite an option that already exists.
    expected response format: {{"wrong_option": "text here"}}""" 
    
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        # response_format={ "type": "json_object" },
        messages= [
            {"role": "system", "content": "You are a super assistant"},
            {"role": "user", "content": prompt}])

    extra_option = json.loads(response.choices[0].message.content)
    print(extra_option)
    extra_options.append(extra_option)
    

with open("easy.json","r") as file:
    easy_datasets = json.load(file)

with open("medium.json","r") as file:
    medium_datasets = json.load(file)

with open("hard.json","r") as file:
    hard_datasets = json.load(file)

options_name = ["A","B","C","D","E"]

def getTrueOption(options, trueAnswer) -> int:
    return options.index(trueAnswer)

# Yanlış seçenekleri her soruya ekleyin
for i, question in enumerate(questions):
    question["incorrect_answers"].append(extra_options[i]["wrong_option"])
    question["incorrect_answers"].append(question['correct_answer'])
    random.shuffle(question["incorrect_answers"])
    
    create_dataset =  {
            "question": question["question"],
            "options": {
                "A": question["incorrect_answers"][0],
                "B": question["incorrect_answers"][1],
                "C": question["incorrect_answers"][2],
                "D": question["incorrect_answers"][3],
                "E": question["incorrect_answers"][4]
            },
            "true_answer": question["correct_answer"],
            "correct_answer": options_name[getTrueOption(question["incorrect_answers"], question["correct_answer"])]
        },
    if question["difficulty"] == "easy":
        easy_datasets.append(create_dataset)
    elif question["difficulty"] == "medium":
        medium_datasets.append(create_dataset)
    else:
        hard_datasets.append(create_dataset)
    
    # Sonuçları istenen formatta yazdırın
    print({
        'question': question["question"],
        'options': question["incorrect_answers"],
    })
    

with open("easy.json", "w") as file:
    json.dump(easy_datasets, file,indent=4)

with open("medium.json","w") as file:
    json.dump(medium_datasets,file, indent=4)
    
with open("hard.json","w") as file:
    json.dump(hard_datasets,file, indent=4)
    
    

