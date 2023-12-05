import json


# Verilerinizi düzenlemek için gerekli işlemleri yapacak bir fonksiyon tanımlayın.
def düzenle_json(veri):
    düzenlenmiş_json = {}
    
    # Her bir dataset için döngü başlatın
    for dataset_adı, dataset in veri.items():
        dataset_listesi = []
        
        # Her bir soru için döngü başlatın
        for soru_adı, soru in dataset.items():
            düzenlenmiş_soru = {
                "question": soru["question"],
                "options": soru["options"],
                "correct_answer": soru["correct_answer"],
                "difficulty": soru["difficulty"]
            }
            dataset_listesi.append(düzenlenmiş_soru)
        
        # Her dataseti düzenlenmiş_json'a ekleyin
        düzenlenmiş_json[dataset_adı] = dataset_listesi
    
    return düzenlenmiş_json

# JSON dosyasını okuyun
with open("questions.json", "r") as file:
    veri = json.load(file)

# Veriyi düzenlenmiş haline çevirin
düzenlenmiş_veri = düzenle_json(veri)

# Düzenlenmiş JSON verisini yazdırın
print(json.dumps(düzenlenmiş_veri, indent=4))

# Düzenlenmiş JSON verisini bir dosyaya yazabilirsiniz
with open("düzenlenmiş_veri.json", "w") as output_file:
    json.dump(düzenlenmiş_veri, output_file, indent=4)
