from pydantic import BaseModel
from fastapi import APIRouter, HTTPException
from alert_manager.manager import get_alerts, get_alert_by_id, update_alert_status

router = APIRouter()


class AlertStatusUpdate(BaseModel):
    status: str


@router.get("/alerts")
async def fetch_alerts(
    status: str = None,
    severity: str = None,
    attack_type: str = None
):
    return get_alerts(
        status=status,
        severity=severity,
        attack_type=attack_type
    )

@router.get("/alerts/{alert_id}")
async def fetch_alert(alert_id: str):
    alert = get_alert_by_id(alert_id)

    if alert is None:
        raise HTTPException(status_code=404, detail="Alert not found")

    return alert


@router.patch("/alerts/{alert_id}/status")
async def change_alert_status(alert_id: str, payload: AlertStatusUpdate):
    result = update_alert_status(alert_id, payload.status)

    if result is None:
        raise HTTPException(status_code=404, detail="Alert not found")

    if isinstance(result, dict) and result.get("error") == "invalid_status":
        raise HTTPException(
            status_code=400,
            detail={
                "message": "Invalid alert status",
                "allowed_statuses": result["allowed_statuses"]
            }
        )

    return result