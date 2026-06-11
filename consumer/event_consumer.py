import json
from kafka import KafkaConsumer
from consumer.processor import process_event


consumer = KafkaConsumer(
    "security-events",
    bootstrap_servers="127.0.0.1:9092",
    auto_offset_reset="latest",
    enable_auto_commit=True,
    group_id="siem-consumer-group",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)


print("Kafka consumer started. Listening for new security events...")


for message in consumer:
    event = message.value
    result = process_event(event)
    print("Processor result:")
    print(json.dumps(result, indent=4))