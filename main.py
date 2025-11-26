from fastapi import FastAPI, HTTPException, status
from dotenv import load_dotenv
import os
from pydantic import BaseModel, Field
from typing import Optional, Literal

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

class ProcessTextRequest(BaseModel):
    text: str = Field(min_length=1, description="Text content to process")
    task: Literal["summarize", "classify", "keywords"] = Field(
        description="Type of processing to apply"
    )
    language: Optional[str] = Field(
        default="es",
        description="Language of the input text (for future use with LLMs)",
    )

class ProcessTextResponse(BaseModel):
    task: str
    processed_text: str
    details: dict

@app.post("/process-text", response_model=ProcessTextResponse)
def process_text(payload: ProcessTextRequest):
    """
    Endpoint interno para procesar texto.
    En el futuro se conectará a un LLM.
    Por ahora simula el comportamiento para probar el contrato.
    """

    if len(payload.text) > 10_000:
        # En un sistema real, pondrías límites para no romper la API ni el LLM
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="Text too long. Please send a shorter input.",
        )

    if payload.task == "summarize":
        processed = payload.text[:150] + "..." if len(payload.text) > 150 else payload.text
        details = {"note": "Dummy summary for now. LLM integration pending."}

    elif payload.task == "classify":
        # Dummy classification
        processed = "general"
        details = {"note": "Dummy classification. LLM integration pending."}

    elif payload.task == "keywords":
        # Dummy keywords extraction
        words = payload.text.split()
        processed = ", ".join(words[:5])
        details = {"note": "Dummy keywords. LLM integration pending."}

    else:
        # Esto no debería pasar porque Pydantic ya valida task, pero es buena práctica
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid task type.",
        )

    return ProcessTextResponse(
        task=payload.task,
        processed_text=processed,
        details=details,
    )
