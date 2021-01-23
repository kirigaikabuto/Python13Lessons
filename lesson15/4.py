def addAge(di):
    realAge = 2021 - di["year"]
    di["age"] = realAge
    return di


peoples = [
    {
        "name": "name1",
        "year": 1998,
    },
    {
        "name": "name2",
        "year": 2000,
    }
]

newPeoples = list(map(addAge, peoples))
print(newPeoples)
