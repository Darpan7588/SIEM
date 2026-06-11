import json
from correlation_engine.engine import correlate_event

def process_event(event: dict):
    print("Processing security event:")
    print(json.dumps(event, indent=4))
    
    alert = correlate_event(event)
    
    if alert:
        print("ALERT GENERATED:")
        print(json.dumps(alert, indent=4))

    return {
        "status": "processed",
        "event_id": event.get("event_id"),
        "event_type": event.get("event_type"),
        "username": event.get("username"),
        "source_ip": event.get("source_ip"),
        "hostname": event.get("hostname"),
        "alert_generated": alert is not None
    }