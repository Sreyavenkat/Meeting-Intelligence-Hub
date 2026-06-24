from fastapi import APIRouter, UploadFile, File, HTTPException
import os


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

print("UPLOAD DIR =", UPLOAD_DIR)

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload")
async def upload_transcript(
    file: UploadFile = File(...)
):

    # validate extension
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


    return {
        "filename": file.filename,
        "word_count": len(text.split()),
        "size_bytes": len(content),
        "status": "uploaded"
    }