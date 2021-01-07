import json

people1 = {
    "name": "Yerassyl",
    "age": 23,
}
people2 = {
    "name": "Yerassyl",
    "age": 22,
}
people3 = {
    "name": "Yerassyl",
    "age": 21,
}
peoples = [people1, people2, people3]
print(peoples[0])
peoplesJson = json.dumps(peoples, indent=4)
file = open("data.json", "w")
file.write(peoplesJson)
file.close()
