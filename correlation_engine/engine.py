print("LOADED INTELLIGENT CORRELATION ENGINE")

from datetime import datetime, timedelta

event_window = []


def parse_time(timestamp: str):
    return datetime.fromisoformat(timestamp)


def correlate_event(event: dict):
    event_window.append(event)

    current_time = parse_time(event.get("timestamp"))
    cutoff_time = current_time - timedelta(minutes=5)

    recent_events = [
        e for e in event_window
        if parse_time(e.get("timestamp")) >= cutoff_time
    ]

    event_window.clear()
    event_window.extend(recent_events)

    username = event.get("username")
    source_ip = event.get("source_ip")
    hostname = event.get("hostname")

    if event.get("event_type") != "authentication_success":
        return None

    failed_logins = [
        e for e in recent_events
        if e.get("event_type") == "authentication_failure"
        and e.get("username") == username
        and e.get("source_ip") == source_ip
        and e.get("hostname") == hostname
    ]

    if len(failed_logins) >= 5:
        alert = {
            "attack_type": "brute_force_login",
            "severity": "high",
            "confidence": "high",
            "message": "Multiple failed logins followed by a successful login from the same user, IP, and host",
            "username": username,
            "source_ip": source_ip,
            "hostname": hostname,
            "failed_attempts": len(failed_logins),
            "success_event_id": event.get("event_id"),
            "evidence_event_ids": [e.get("event_id") for e in failed_logins]
        }

        return alert

    return None