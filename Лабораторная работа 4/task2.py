import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f:
        reader = csv.DictReader(f)
        data = [line for line in reader]
    with open(OUTPUT_FILENAME,"w") as w:
        json.dump(data, w, indent = 4, ensure_ascii=True)


    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
