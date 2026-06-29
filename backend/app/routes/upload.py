from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
import os

from app.dependencies import get_db
from app.models.meeting import Meeting
from app.services.indexing_service import build_index 



router = APIRouter()


BASE_DIR = os.path.dirname(

    os.path.dirname(

        os.path.dirname(

            os.path.dirname(__file__)

        )

    )

)

UPLOAD_DIR = os.path.join(
    BASE_DIR,
    "storage",
    "uploads"
)


os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload")
async def upload_transcript(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    if not file.filename.endswith((".txt", ".vtt")):
        raise HTTPException(
            status_code=400,
            detail="Only .txt and .vtt files allowed"
        )


    content = await file.read()


    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )


    with open(file_path, "wb") as f:
        f.write(content)


    text = content.decode(
        "utf-8",
        errors="ignore"
    )


    word_count = len(text.split())


    meeting = Meeting(
        filename=file.filename,
        file_path=file_path,
        word_count=word_count
    )


    db.add(meeting)
    db.commit()
    db.refresh(meeting)

    build_index(
        transcript_text=text,
        meeting_id=meeting.id
    )


    return {
        "meeting_id": meeting.id,
        "filename": meeting.filename,
        "word_count": meeting.word_count,
        "status": "uploaded"
    }