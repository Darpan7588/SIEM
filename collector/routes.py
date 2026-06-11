from fastapi import APIRouter
from collector.models import SecurityEvent
from collector.storage import events
from uuid import uuid4
from fastapi import HTTPException
from parser.normalizer import normalize_event
from collector.kafka_producer import send_event
from datetime import datetime

router = APIRouter()


@router.post("/events")
async def receive_event(event: SecurityEvent):
    event_data = event.model_dump(mode = "json")
    event_data["event_id"] = str(uuid4())

    normalized_event = normalize_event(event_data)
    events.append(normalized_event)
    send_event(normalized_event)
    
    return {
        "status": "received",
        "event_id": event_data["event_id"],
        "event_type": event.event_type
    }
    
@router.get("/events/{event_id}")
async def get_event(event_id: str):
    for event in events:
        if event["event_id"] == event_id:
            return event

    raise HTTPException(
        status_code=404,
        detail="Event not found"
    )
    
@router.post("/simulate/brute-force")
async def simulate_brute_force():

    events_to_generate = []

    # 5 failed logins
    for _ in range(5):
        event = {
            "source": "windows",
            "event_type": "authentication_failure",
            "severity": "high",
            "message": "Simulated failed login",
            "timestamp": datetime.utcnow().isoformat(),
            "event_id": str(uuid4()),
            "raw_event": {
                "EventID": 4625,
                "AccountName": "Administrator",
                "IpAddress": "192.168.1.50"
            },
            "normalized": True
        }

        events.append(event)
        send_event(event)
        events_to_generate.append(event)

    # 1 successful login
    success_event = {
        "source": "windows",
        "event_type": "authentication_success",
        "severity": "low",
        "message": "Simulated successful login",
        "timestamp": datetime.utcnow().isoformat(),
        "event_id": str(uuid4()),
        "raw_event": {
            "EventID": 4624,
            "AccountName": "Administrator",
            "IpAddress": "192.168.1.50"
        },
        "normalized": True
    }

    events.append(success_event)
    send_event(success_event)
    events_to_generate.append(success_event)

    return {
        "status": "simulation_complete",
        "events_generated": len(events_to_generate)
    }

@router.get("/events")
async def get_events():
    return events