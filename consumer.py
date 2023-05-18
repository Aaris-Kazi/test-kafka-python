from kafka import KafkaConsumer

consume = KafkaConsumer("topic1", bootstrap_servers = "localhost:9092")
for i in consume:
    print(i.value)