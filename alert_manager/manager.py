import json
from uuid import uuid4
from datetime import datetime
from database.connection import get_connection


def create_alert(alert_data: dict):
    alert = {
        "alert_id": str(uuid4()),
        "created_at": datetime.utcnow().isoformat(),
        "status": "open",
        **alert_data
    }

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO alerts (
            alert_id, created_at, status, attack_type, severity,
            confidence, message, username, source_ip, hostname,
            failed_attempts, success_event_id, evidence_event_ids
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            alert["alert_id"],
            alert["created_at"],
            alert["status"],
            alert.get("attack_type"),
            alert.get("severity"),
            alert.get("confidence"),
            alert.get("message"),
            alert.get("username"),
            alert.get("source_ip"),
            alert.get("hostname"),
            alert.get("failed_attempts"),
            alert.get("success_event_id"),
            json.dumps(alert.get("evidence_event_ids", []))
        )
    )

    conn.commit()
    cursor.close()
    conn.close()

    return alert


def get_alerts():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            alert_id, created_at, status, attack_type, severity,
            confidence, message, username, source_ip, hostname,
            failed_attempts, success_event_id, evidence_event_ids
        FROM alerts
        ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    alerts = []
    for row in rows:
        alerts.append({
            "alert_id": row[0],
            "created_at": row[1],
            "status": row[2],
            "attack_type": row[3],
            "severity": row[4],
            "confidence": row[5],
            "message": row[6],
            "username": row[7],
            "source_ip": row[8],
            "hostname": row[9],
            "failed_attempts": row[10],
            "success_event_id": row[11],
            "evidence_event_ids": row[12]
        })

    cursor.close()
    conn.close()

    return alerts