from kafka import KafkaConsumer
import json
consumer = KafkaConsumer("python_lesson")
for i in consumer:
    jsonData = i.value
    user = json.loads(jsonData)
    print(user["username"])
