import json
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable, KafkaTimeoutError

producer = None


def get_producer():
    global producer

    if producer is None:
        producer = KafkaProducer(
            bootstrap_servers="127.0.0.1:9092",
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
            api_version=(2, 8, 0),
            request_timeout_ms=5000,
            metadata_max_age_ms=5000,
            max_block_ms=5000
        )

    return producer


def send_event(event: dict):
    try:
        kafka_producer = get_producer()
        kafka_producer.send("security-events", event)
        kafka_producer.flush()
        print("Event sent to Kafka topic: security-events")

    except (NoBrokersAvailable, KafkaTimeoutError) as error:
        print(f"Kafka unavailable. Event stored only in memory. Error: {error}")

    except Exception as error:
        print(f"Unexpected Kafka error. Event stored only in memory. Error: {error}")