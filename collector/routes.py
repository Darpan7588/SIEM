from fastapi import APIRouter
from collector.models import SecurityEvent
from collector.storage import events

router = APIRouter()


@router.post("/events")
async def receive_event(event: SecurityEvent):

    events.append(event.dict())

    return {
        "status": "received",
        "event_type": event.event_type
    }


@router.get("/events")
async def get_events():
    return events