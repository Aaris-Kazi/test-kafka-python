from kafka import KafkaProducer

prod = KafkaProducer(bootstrap_servers = "localhost:9092")
    
print(prod.bootstrap_connected())
for i in range(10):
    prod.send("topic1", str(i).encode("utf-8"))

prod.flush()