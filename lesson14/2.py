def printInfo(peoples):
    for i in peoples:
        print(i["name"], i["age"])


def getAverageAge(peoples):
    sumi = 0
    n = len(peoples)
    for i in peoples:
        sumi = sumi + i["age"]
    return sumi / n


people1 = {
    "name": "name1",
    "age": 23
}
people2 = {
    "name": "name2",
    "age": 21
}
people3 = {
    "name": "name3",
    "age": 20
}
peoples = [people1, people2, people3]

printInfo(peoples)
averageAge = getAverageAge(peoples)
print(averageAge)
