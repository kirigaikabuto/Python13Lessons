from kafka import KafkaConsumer
import json

consumer = KafkaConsumer("lesson35kf")
for msg in consumer:
    jsonData = msg.value
    d = json.loads(jsonData)
    print(d["username"], d["password"])
