from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat_service import answer_question


router = APIRouter()


class ChatRequest(BaseModel):

    question: str



@router.post("/chat/{meeting_id}")
def chat(
    meeting_id: int,
    request: ChatRequest
):

    answer = answer_question(
        request.question,
        meeting_id
    )


    return {
        "meeting_id": meeting_id,
        "question": request.question,
        "answer": answer
    }