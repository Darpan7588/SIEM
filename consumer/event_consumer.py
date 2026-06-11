import json
from kafka import KafkaConsumer


consumer = KafkaConsumer(
    "security-events",
    bootstrap_servers="127.0.0.1:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="siem-consumer-group",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)


print("Kafka consumer started. Listening for security events...")

for message in consumer:
    event = message.value
    print("Received event from Kafka:")
    print(json.dumps(event, indent=4))