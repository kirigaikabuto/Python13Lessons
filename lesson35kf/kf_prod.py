from kafka import KafkaProducer
import json


def send_message_to_kf(data, topicName):
    jsonData = json.dumps(data).encode("ascii")
    producer = KafkaProducer(bootstrap_servers="localhost:9092")

    producer.send(topicName, jsonData)

    producer.flush()
