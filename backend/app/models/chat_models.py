from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ChatRequest(BaseModel):
    text: str

class ChatResponse(BaseModel):
    response: str

class QAPair(BaseModel):
    question: str
    answer: str
    created_at: datetime = datetime.now()
    updated_at: Optional[datetime] = None
