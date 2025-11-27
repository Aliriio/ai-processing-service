from fastapi import APIRouter, HTTPException, status
from app.models.process_text import ProcessTextRequest, ProcessTextResponse

router = APIRouter()


@router.post("/process-text", response_model=ProcessTextResponse)
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