from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers="localhost:9092")
d = {
    "username": "yerassyl",
    "age": 23,
}
jsonData = json.dumps(d).encode("ascii")
producer.send("python_lesson", jsonData)
metrics = producer.metrics()
producer.flush()
print(metrics)
