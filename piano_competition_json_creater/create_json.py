import json as j
import os
from os import path
import time

from anyio import sleep


def read_internal_input():
    print(f"Current working directory: {os.getcwd()}")

    executable_dir = path.dirname(__file__)

    print(f"Current file name {__file__}")

    print(f"Executable directory: {executable_dir}")

    brake_counter = 0

    jsons_array = []

    with open(f"{executable_dir}/pianists_input.txt", "r", encoding="utf-8") as file:
        for line in file.read().splitlines():

            time.sleep(0.01)

            if brake_counter == 0:
                json_obj = {"videoUrl": "", "composition": "", "name": str(line), "id": {
                    "$oid": f"{time.time()}"
                }, "group": 'Номінація «Концертмейстер»'}

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

    for e in jsons_array:
        print(e)

    with open('output.txt', 'w', encoding='utf8') as json_file:
        j.dump(jsons_array, json_file, ensure_ascii=False, indent=3)


if __name__ == "__main__":
    read_internal_input()
