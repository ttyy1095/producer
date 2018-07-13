from kafka import KafkaProducer
from time import sleep
producer = KafkaProducer(bootstrap_servers="192.168.7.111:9092")
msg = b"Hello,I am Jax!"
producer.send("mytest",msg)
sleep(2)
