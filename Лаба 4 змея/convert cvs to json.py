# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(csvFilePath, jsonFilePath) -> None:
    data = []  # TODO считать содержимое csv файла

    with open(csvFilePath, 'r') as file: #читаем файл
        cvs_reader = csv.DictReader(file) #загружаем данные

        for row in cvs_reader: #проебразуем строки из cvs в python dict
            data.append(row)

    with open(jsonFilePath, 'w') as jsonf: # TODO Сериализовать в файл с отступами равными 4
        jsonStr = json.dumps(data, indent=4)
        jsonf.write(jsonStr) #переводим в JSON и записываем в файл


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
