from fastapi import APIRouter
from app.core.config import OPENAI_API_KEY

router = APIRouter()


@router.get("/health")
def health_check():
    """
    Endpoint de salud usado por monitoreo y DevOps.
    Sirve para saber si el servicio está vivo.
    """
    return {"status": "ok"}


@router.get("/config-status")
def config_status():
    """
    Endpoint solo para desarrollo:
    Permite verificar si la API key de OpenAI está configurada.
    Nunca debe devolver la key, solo un booleano.
    """
    return {
        "openai_key_configured": OPENAI_API_KEY is not None
    }