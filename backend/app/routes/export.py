from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

import csv
import io

from app.dependencies import get_db
from app.models.decision import Decision
from app.models.action_item import ActionItem


router = APIRouter()


@router.get("/export/csv/{meeting_id}")
def export_csv(
    meeting_id: int,
    db: Session = Depends(get_db)
):

    decisions = db.query(Decision).filter(
        Decision.meeting_id == meeting_id
    ).all()


    action_items = db.query(ActionItem).filter(
        ActionItem.meeting_id == meeting_id
    ).all()


    output = io.StringIO()

    writer = csv.writer(output)


    writer.writerow(
        [
            "Type",
            "Content",
            "Responsible Person",
            "Deadline"
        ]
    )


    for decision in decisions:

        writer.writerow(
            [
                "Decision",
                decision.decision_text,
                "",
                ""
            ]
        )


    for item in action_items:

        writer.writerow(
            [
                "Action Item",
                item.task,
                item.responsible_person,
                item.deadline
            ]
        )


    output.seek(0)


    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=meeting_report.csv"
        }
    )