from fastapi import APIRouter
from schemas.chat_schema import chatRequest,chatResponse
from services.llm_service import generate_response

router = APIRouter()

@router.post("/chat",response_model=chatResponse)
def chat(request:chatRequest):
    response = generate_response(request.prompt)
    return chatResponse(response=response)

@router.get("/health")
def health_check():
    return {
        'status':'healthy'
    }

@router.get("/model-info")
def model_info():
    return {
        "model_name":"DeepSeek-Coder",
        "model-version":"1.0.0",
        "provider":"ollama",
        "status":"loaded"
    }