# import random

# liste = [1, 2, 3, 4, 5] + [15,19]

# # Listeyi karıştır
# random.shuffle(liste)

# print("Karıştırılmış liste:", liste)

# print(liste.index(5))

# import json

# data = [
#   {
#     "selam": 15
#   },
#   {
#     "evet": 15
#   },
# ]

# with open("hard.json", "r") as file:
#     veri = json.load(file)

# veri += data
# print(veri)
# with open("hard.json", "w") as file:
#   json.dump(veri, file, indent=4)



# def sayHello(liste, trueOption):
#   return liste.index(trueOption)

# x = [1,2,3,4]

# y = sayHello(x, 3)

# print(y)

def sayHello():
  return "5115"

data = {
  "selam": 123,
  "merhaba": sayHello()
}

print(data)