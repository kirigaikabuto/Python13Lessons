from kafka import KafkaConsumer
import json
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client["quiz_app_logs"]
loginCollection = db["login_logs"]
createQuizCollection = db["create_quiz_logs"]
consumer = KafkaConsumer("quiz_app")
for msg in consumer:
    jsonData = msg.value
    d = json.loads(jsonData)
    if d["action"] == "login":
        loginCollection.insert_one(d)
    elif d["action"] == "create_quiz":
        createQuizCollection.insert_one(d)
