import json

file = open("products.json", "r")
productsJson = file.read()
file.close()
products = json.loads(productsJson)
print("N", "NAME", "PRICE")
for i, v in enumerate(products):
    print(i, "|", v["name"], "|", v["price"], "|")
num = int(input("N="))
choicedProduct = products[num]
print(choicedProduct["name"], choicedProduct["price"], choicedProduct["description"])
