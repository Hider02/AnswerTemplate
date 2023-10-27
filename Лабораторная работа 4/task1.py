# TODO решите задачу
import json
def task() -> float:
    with open("input.json") as f:
        data = json.load(f)
    list_ = [i["score"] * i["weight"] for i in data]
    return round(sum(list_), 3)

print(task())
