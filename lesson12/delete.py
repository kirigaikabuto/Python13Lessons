import json

file = open("products.json", "r")
productsJson = file.read()
file.close()
products = json.loads(productsJson)
print("N", "NAME", "PRICE")
for i, v in enumerate(products):
    print(i, "|", v["name"], "|", v["price"], "|")
num = int(input("N="))
products.pop(num)
file = open("products.json", "w")
productsJson = json.dumps(products, indent=4)
file.write(productsJson)
file.close()
