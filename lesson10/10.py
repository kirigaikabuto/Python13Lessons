people1 = {
    "name": "kir",
    "age": 14
}
people2 = {
    "name": "kiri",
    "age": 12
}
people3 = {
    "name": "kiro",
    "age": 10
}
peoples = [people1, people2, people3]
name = input("write name:")
for i in peoples:
    if i["name"] == name:
        print(i)
