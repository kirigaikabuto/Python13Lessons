import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["yerassyldb"]
collection = db["products"]
d = {
    "name": "product4",
    "price": 15
}
collection.insert_one(d)
