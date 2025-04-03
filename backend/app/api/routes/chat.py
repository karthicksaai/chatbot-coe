from fastapi import APIRouter, HTTPException
from ...models.chat_models import ChatRequest, ChatResponse
from ...services.chat_service import ChatService

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    try:
        response = await ChatService.process_message(request.text)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
