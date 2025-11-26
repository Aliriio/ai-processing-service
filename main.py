from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Carga variables de entorno desde .env
load_dotenv()

app = FastAPI(
    title="AI Processing Service",
    description="Base API for AI-related processing (LLMs, embeddings, etc.)",
    version="0.1.0",
)

# Ejemplo: leer la key (sin exponerla)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.get("/health")
def health_check():
    """
    Endpoint de salud usado por monitoreo y DevOps.
    Sirve para saber si el servicio está vivo.
    """
    return {"status": "ok"}

@app.get("/config-status")
def config_status():
    """
    Endpoint solo para desarrollo:
    Permite verificar si la API key de OpenAI está configurada.
    Nunca debe devolver la key, solo un booleano.
    """
    return {
        "openai_key_configured": OPENAI_API_KEY is not None
    }