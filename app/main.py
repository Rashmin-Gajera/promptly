from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Agentic AI System")
app.include_router(router)
