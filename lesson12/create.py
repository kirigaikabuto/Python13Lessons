import json

file = open("products.json", "r")
productsJson = file.read()
file.close()
products = json.loads(productsJson)
name = input("name:")
price = int(input("price:"))
description = input("description:")
product = {
    "name": name,
    "price": price,
    "description": description,
}
products.append(product)
file = open("products.json", "w")
productsJson = json.dumps(products, indent=4)
file.write(productsJson)
file.close()
