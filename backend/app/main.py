from fastapi import FastAPI

from app.database import engine, Base
from app.models import (
    meeting,
    decision,
    action_item,
    sentiment
)
from app.routes import upload
from app.routes import extraction
from app.routes import export
from app.routes import chat
from app.routes import sentiment

Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Meeting Intelligence Hub"
)


app.include_router(
    upload.router,
    prefix="/api"
)

app.include_router(
    extraction.router,
    prefix="/api"
)

app.include_router(
    export.router,
    prefix="/api"
)

app.include_router(
    chat.router,
    prefix="/api"
)

app.include_router(
    sentiment.router,
    prefix="/api"
)


@app.get("/")
def root():
    return {
        "message": "Meeting Intelligence Hub API running"
    }