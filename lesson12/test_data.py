import json

product1 = {
    "name": "product1",
    "price": 100,
    "description": "it is product1"
}
product2 = {
    "name": "product2",
    "price": 200,
    "description": "it is product2"
}
products = [product1, product2]
jsonProducts = json.dumps(products, indent=4)
file = open("products.json", "w")
file.write(jsonProducts)
file.close()

