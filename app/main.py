from fastapi import FastAPI
from app.routes import health, process_text

app = FastAPI(
    title="AI Processing Service",
    description="Base API for AI-related processing (LLMs, embeddings, etc.)",
    version="0.1.0",
)

# Registrar los routers
app.include_router(health.router)
app.include_router(process_text.router)