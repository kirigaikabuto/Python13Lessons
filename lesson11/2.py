# 1) считать данные из файла
# 2) преобразовать данные обратно в массив
# 3) добавить новый элемент в массив
# 4) сохранить данные в файл
# 1
import json
file = open("data.json", "r")
peoplesJson = file.read()
file.close()
# 2
peoples = json.loads(peoplesJson)
# 3
people = {
    "name": "name4",
    "age": 222
}
peoples.append(people)
# 4
peoplesJson = json.dumps(peoples, indent=4)
file = open("data.json", "w")
file.write(peoplesJson)
file.close()
