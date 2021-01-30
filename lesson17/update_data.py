import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["yerassyldb"]
collection = db["products"]
query = {
    "name": "product2.0"
}
update = {
    "$set": {
        "price": 123456789,
        "name": "product2.0",
    }
}
collection.update_one(query, update)
