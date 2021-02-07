computerDictionary1 = {
    "name": "asus rog",
    "ram": 8,
    "processor": "intel core i5",
    "price": 420000,
}
computerDictionary2 = {
    "name": "acer predator",
    "ram": 16,
    "processor": "intel core i7",
    "price": 1300000,
}
computerDictionary3 = {
    "name": "acer predator",
    "ram": 16,
    "processor": "intel core i7",
    "prices": 1300000,
}
computers = [computerDictionary1, computerDictionary2, computerDictionary3]
sumi = 0
for i in computers:
    sumi = sumi + i["price"]
print(sumi)
