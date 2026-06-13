from fastapi import APIRouter
from alert_manager.manager import get_alerts

router = APIRouter()


@router.get("/alerts")
async def fetch_alerts():
    return get_alerts()