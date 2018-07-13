from kafka import KafkaConsumer

consumer = KafkaConsumer("mytest", bootstrap_servers="192.168.7.111:9092")
while True:
    raw_messages = consumer.poll(timeout_ms=1000, max_records=5000)
    if len(raw_messages) == 0:
        continue
    for topic_partition, message in raw_messages.items():
        print topic_partition
        print message[0].value
