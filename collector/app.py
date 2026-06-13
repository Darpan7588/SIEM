from fastapi import FastAPI
from collector.routes import router as collector_router
from alert_manager.routes import router as alert_router

app = FastAPI(
    title="Advanced SIEM Collector"
)

app.include_router(collector_router)
app.include_router(alert_router)