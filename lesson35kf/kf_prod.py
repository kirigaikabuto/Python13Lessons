from kafka import KafkaProducer
import json

d = {
    "username": "yerassyl",
    "password": 414212412,
}
jsonData = json.dumps(d).encode("ascii")
producer = KafkaProducer(bootstrap_servers="localhost:9092")

producer.send("lesson35kf", jsonData)

producer.flush()
