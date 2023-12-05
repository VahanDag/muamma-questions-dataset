import json

data_file = {}

with open("questions1.json", "r") as file:
    data_file = json.load(file)

data_file = {
   "dataset1" : [
        {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
    ],
   "dataset2" : [
        {
            "name": "vaahan",
            "age": 35,
            "city": "New York"
        }
    ],
   "dataset3" : [
        {
            "name": "sevasd",
            "age": 54,
            "city": "N York"
        }
    ]
}

# print(data_file)

for y,x in data_file.items():
    print(x[0])


# with open("questions1.json","w") as file:
#     json.dump(data_file,file, indent=4)


# for x in range(len(data_file) + 1, len(data_file) + 5):
#     data_file[f"dataset{x}"] = [
#         {"merhaba": f"iyiyim{x}"}
#     ]

# print(data_file)

# for e,soru in data_file.items():
#     for x in soru:
#         print(x)
