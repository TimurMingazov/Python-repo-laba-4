# TODO решите задачу
import json

filename = 'input.json' #

def task(file_path) -> float:
    """ Читаем файл, считаем сумму """
    with open(file_path) as file:
        data = json.load(file) # прочитали файл

    sum_ = sum([item["score"] * item["weight"] for item in data]) #воспользовались
    # list comprehension и получили сумму произведений двух значние в словаре
    return round(sum_, 3)


print(task(filename))
