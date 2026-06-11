import json


def process_event(event: dict):
    print("Processing security event:")
    print(json.dumps(event, indent=4))

    return {
        "status": "processed",
        "event_id": event.get("event_id"),
        "event_type": event.get("event_type")
    }