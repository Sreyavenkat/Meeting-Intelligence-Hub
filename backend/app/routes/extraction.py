from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.models.meeting import Meeting
from app.models.decision import Decision
from app.models.action_item import ActionItem

from app.services.ai_service import (
    extract_meeting_insights
)

router = APIRouter()


@router.post("/extract/{meeting_id}")
def extract_meeting_data(
    meeting_id: int,
    db: Session = Depends(get_db)
):

    meeting = db.query(Meeting).filter(
        Meeting.id == meeting_id
    ).first()

    if not meeting:
        return {
            "error": "Meeting not found"
        }

    with open(
        meeting.file_path,
        "r",
        encoding="utf-8"
    ) as file:

        transcript = file.read()

    result = extract_meeting_insights(
        transcript
    )

    for decision_text in result["decisions"]:

        decision = Decision(
            meeting_id=meeting.id,
            decision_text=decision_text
        )

        db.add(decision)

    for item in result["action_items"]:

        action_item = ActionItem(
            meeting_id=meeting.id,
            responsible_person=item.get(
                "responsible_person"
            ),
            task=item.get(
                "task"
            ),
            deadline=item.get(
                "deadline"
            )
        )

        db.add(action_item)

    db.commit()

    return result