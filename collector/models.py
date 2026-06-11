from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class Severity(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class EventSource(str, Enum):
    windows = "windows"
    linux = "linux"
    suricata = "suricata"
    github = "github"
    trivy = "trivy"
    semgrep = "semgrep"
    docker = "docker"
    kubernetes = "kubernetes"


class SecurityEvent(BaseModel):
    source: EventSource
    event_type: str
    severity: Severity
    message: str
    timestamp: datetime