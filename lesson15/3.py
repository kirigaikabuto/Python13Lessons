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

d1 = {
         "name": "name1",
         "year": 1998,
     }

newD = addAge(d1)
print(newD)
