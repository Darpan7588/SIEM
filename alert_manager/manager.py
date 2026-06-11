from uuid import uuid4
from datetime import datetime

alerts = []


def create_alert(alert_data: dict):
    alert = {
        "alert_id": str(uuid4()),
        "created_at": datetime.utcnow().isoformat(),
        "status": "open",
        **alert_data
    }

    alerts.append(alert)

    return alert


def get_alerts():
    return alerts