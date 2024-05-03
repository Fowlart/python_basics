import json as j
import time

brake_counter = 0
jsons_array = []

with open("input.txt", "r", encoding="utf-8") as file:
    for line in file.read().splitlines():

        if brake_counter == 0:
            json_obj = {"videoUrl": "", "composition": "", "name": str(line), "id": {
                "$oid": f"{time.time()}"
            }, "group": 'Номінація "Фортепіано соло"'}

            brake_counter += 1
            continue

        if brake_counter == 1:
            json_obj["composition"] = str(line)
            brake_counter += 1
            continue

        elif brake_counter == 2:
            json_obj["videoUrl"] = str(line)
            brake_counter += 1
            continue

        elif brake_counter == 3:
            jsons_array.append(json_obj)
            brake_counter = 0
            continue

print(jsons_array)

with open('output.txt', 'w', encoding='utf8') as json_file:
    j.dump(jsons_array, json_file, ensure_ascii=False, indent=3)
