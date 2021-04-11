from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")
producer.send("python_lesson", b'Hello from kafak')
metrics = producer.metrics()
producer.flush()
print(metrics)