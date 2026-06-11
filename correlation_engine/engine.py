event_window = []


def correlate_event(event: dict):
    event_window.append(event)

    if len(event_window) > 20:
        event_window.pop(0)

    failed_logins = [
        e for e in event_window
        if e.get("event_type") == "authentication_failure"
    ]

    successful_logins = [
        e for e in event_window
        if e.get("event_type") == "authentication_success"
    ]

    if len(failed_logins) >= 5 and len(successful_logins) >= 1:
        alert = {
            "alert_type": "possible_brute_force",
            "severity": "high",
            "message": "Multiple failed logins followed by a successful login",
            "failed_attempts": len(failed_logins),
            "success_events": len(successful_logins),
            "source": event.get("source")
        }

        event_window.clear()
        return alert

    return None