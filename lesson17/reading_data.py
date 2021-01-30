import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["yerassyldb"]
collection = db["products"]
products = collection.find()
for i in products:
    print(i["_id"], i["name"], i["price"])
