from functools import reduce


def addAge(di):
    realAge = 2021 - di["year"]
    di["age"] = realAge
    return di


def filterByYear(di):
    if di["year"] < 2000:
        return True
    else:
        return False


def calculate(di1, di2):
    if di1["age"] > di2["age"]:
        return di1
    else:
        return di2


def calculateAllAges(di1, di2):
    if isinstance(di1, dict):
        return di1["age"] + di2["age"]
    else:
        return di1 + di2["age"]


peoples = [
    {
        "name": "name1",
        "year": 1998,
    },
    {
        "name": "name2",
        "year": 2000,
    },
    {
        "name": "name3",
        "year": 1962,
    },
    {
        "name": "name4",
        "year": 2003,
    },
    {
        "name": "name5",
        "year": 2012,
    },
]

peoples1 = list(map(addAge, peoples))
print(peoples1)
peoples2 = list(filter(filterByYear, peoples1))
print(peoples2)
personWithMaxAge = reduce(calculate, peoples1)
print(personWithMaxAge)
personSumAge = reduce(calculateAllAges, peoples1)
print(personSumAge / len(peoples1))
