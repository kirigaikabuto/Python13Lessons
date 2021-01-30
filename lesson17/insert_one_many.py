import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["yerassyldb"]
collection = db["products"]
d1 = {
    "name": "product5",
    "price": 15
}
d2 = {
    "name": "product6",
    "price": 201,
}
products = [d1, d2]
# collection.insert_one(d1)
collection.insert_many(products)
