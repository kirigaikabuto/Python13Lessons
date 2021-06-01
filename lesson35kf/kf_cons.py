from kafka import KafkaConsumer
import json

consumer = KafkaConsumer("quiz_app")
for msg in consumer:
    jsonData = msg.value
    d = json.loads(jsonData)
    print(d["username"])
