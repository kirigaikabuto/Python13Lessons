import json

file = open("data.json", "r")
peoplesJson = file.read()
file.close()
peoples = json.loads(peoplesJson)
print(peoples)
