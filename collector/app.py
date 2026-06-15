from fastapi import FastAPI
from collector.routes import router as collector_router
from alert_manager.routes import router as alert_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Advanced SIEM Collector"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(collector_router)
app.include_router(alert_router)