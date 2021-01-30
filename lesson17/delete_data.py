import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["yerassyldb"]
collection = db["products"]
query = {
    "name": "product2.0"
}
collection.delete_one(query)
