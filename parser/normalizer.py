def normalize_event(event: dict) -> dict:
    source = event.get("source")
    raw_event = event.get("raw_event") or {}

    normalized_type = event.get("event_type")

    if source == "windows":
        event_id = raw_event.get("EventID")

        if event_id == 4625:
            normalized_type = "authentication_failure"

        elif event_id == 4624:
            normalized_type = "authentication_success"

    if source == "linux":
        action = raw_event.get("action")
        service = raw_event.get("service")

        if service == "ssh" and action == "failed_password":
            normalized_type = "authentication_failure"
        elif service == "ssh" and action == "accepted_password":
            normalized_type = "authentication_success"
        
    normalized_event = {
        "event_id": event.get("event_id"),
        "source": source,
        "event_type": normalized_type,
        "severity": event.get("severity"),
        "message": event.get("message"),
        "timestamp": event.get("timestamp"),
        "raw_event": raw_event,
        "normalized": True
    }

    return normalized_event