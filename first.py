import json
import os

from openai import OpenAI

# API anahtarınızı buraya girin
client = OpenAI()

# İlk JSON dosyası
current_file_number = 16
questions_file = f"questions{current_file_number}.json"

# JSON dosyasını yüklemek ve dosya numarasını güncellemek için fonksiyon


def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file), current_file_number
    else:
        return {}, current_file_number + 1


# Veri yüklemesi ve dosya numarasını kontrol etme
data, current_file_number = load_data(questions_file)

# Sonsuz döngü
while True:
    if len(data) >= 100:  # Eğer mevcut dosya doluysa
        current_file_number += 1  # Dosya numarasını artır
        # Yeni dosya adını oluştur
        questions_file = f"questions{current_file_number}.json"
        data = {}  # Veriyi sıfırla

    try:
        completion = client.chat.completions.create(
            model="gpt-4-1106-preview",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "You are a super assistant designed to output JSON and prepare questions for all Q&A applications in the world."},
                {"role": "user", "content": """Generate 4 sets of 8 multiple-choice questions each. For each set, randomly select 8 topics from the following list and create one question per topic: History, Technology, General Knowledge, Science, Mathematics, Literature, Cinema & TV, Music, Geography, Sports, Computer Science, Health & Medicine, Economics, Environmental Science, Philosophy, Video Games, Art & Design, Psychology, Astronomy, Politics, Mythology, Food & Cuisine, World Cultures, Current Events, Automotive, Heavy Industry & Machine industry,  Popular Science, Future, Mind Games, Great Leaders, Language & Linguistics. Ensure each question has increasing difficulty from 1 to 8 within its set (The second question is harder than the first question, the third question is harder than the second question, etc.). Include five options (A, B, C, D, E) for each question and indicate the correct answer. For each topic, incorporate recent developments, unique historical events, or specific aspects that are less commonly known to enhance the uniqueness of the questions. 
Expected format:
{
  "dataset1": [
    {
      "question": "Question text here",
      "options": {
        "A": "Option A",
        "B": "Option B",
        "C": "Option C",
        "D": "Option D",
        "E": "Option E"
      },
      "correct_answer": "C",
      "difficulty": 1
    },
    // 7 more questions following this format
  ],
  // Similar structure for dataset2, dataset3, and dataset4
}
Alert: Make sure the questions you generate are not the same questions you generated before! Additionally, aim to incorporate innovative angles or perspectives in each question to ensure diversity and uniqueness. Avoid repeating themes or concepts previously used in your question sets.
"""

                 }
            ]
        )

        # API çıktısını işle
        api_output = json.loads(completion.choices[0].message.content)

        # Yeni dataset'leri dosyaya ekleyin
        for key, dataset in api_output.items():
            dataset_name = 'dataset' + str(len(data) + 1)
            data[dataset_name] = dataset

        # JSON olarak kaydet
        with open(questions_file, "w") as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        continue  # Hata durumunda döngüyü sürdür

    # İsteğe bağlı: Belirli bir dosya numarası sonrası döngüyü durdur
    if current_file_number > 35:  # Örneğin 10'dan büyük bir dosya numarası için döngüden çık
        break
