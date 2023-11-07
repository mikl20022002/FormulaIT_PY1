import json
# TODO решите задачу
def task() -> float:
    with open('input.json' , 'r') as file:
        data = json.load(file)

    sum = 0
    for i in range(len(data)):
        values = list(data[i].values())
        sum += values[0] * values[1]
    return round(sum, 3)

print(task())
