from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class Severity(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class SecurityEvent(BaseModel):
    source: str
    event_type: str
    severity: Severity
    message: str
    timestamp: datetime
