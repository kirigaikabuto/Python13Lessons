from kafka import KafkaConsumer

consumer = KafkaConsumer("lesson35kf")
for msg in consumer:
    # some conditions
    print(msg)
    print(msg.value)
