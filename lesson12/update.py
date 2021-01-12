import json

file = open("products.json", "r")
productsJson = file.read()
file.close()
products = json.loads(productsJson)
print("N", "NAME", "PRICE")
for i, v in enumerate(products):
    print(i, "|", v["name"], "|", v["price"], "|")
num = int(input("N="))
field = input("fieldName:")
field = field.lower()
value = input("value:")
if field == "price":
    value = int(value)
products[num][field] = value
file = open("products.json", "w")
productsJson = json.dumps(products, indent=4)
file.write(productsJson)
file.close()

