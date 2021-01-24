import json


def saveToJsonFile(data, fileName):
    dataJson = json.dumps(data, indent=4)
    file = open(fileName, "w")
    file.write(dataJson)
    file.close()
