from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.meeting import Meeting

from app.services.sentiment_processing_service import (
    process_sentiment
)


router = APIRouter(
    tags=["Sentiment"]
)


@router.post("/sentiment/{meeting_id}")
def analyze_meeting_sentiment(
    meeting_id: int,
    db: Session = Depends(get_db)
):

    meeting = (
        db.query(Meeting)
        .filter(Meeting.id == meeting_id)
        .first()
    )

    if meeting is None:
        raise HTTPException(
            status_code=404,
            detail="Meeting not found"
        )

    with open(
        meeting.file_path,
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as file:

        text = file.read()

    result = process_sentiment(
        text,
        meeting_id,
        db
    )

    return result