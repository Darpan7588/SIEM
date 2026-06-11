from fastapi import FastAPI
from collector.routes import router

app = FastAPI(
    title="Advanced SIEM Collector"
)

app.include_router(router)