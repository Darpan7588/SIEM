from fastapi import APIRouter
from collector.models import SecurityEvent
from collector.storage import events
from uuid import uuid4
from fastapi import HTTPException
from parser.normalizer import normalize_event

router = APIRouter()


@router.post("/events")
async def receive_event(event: SecurityEvent):
    event_data = event.model_dump()
    event_data["event_id"] = str(uuid4())

    normalized_event = normalize_event(event_data)
    events.append(normalized_event)

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

@router.get("/events")
async def get_events():
    return events