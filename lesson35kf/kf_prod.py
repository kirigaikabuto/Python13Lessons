from kafka import KafkaProducer
import json

d = {
    "username": "asdsad",
    "password": 12321,
}
jsonData = json.dumps(d)
producer = KafkaProducer(bootstrap_servers="localhost:9092")

producer.send("lesson35kf", jsonData)

producer.flush()
